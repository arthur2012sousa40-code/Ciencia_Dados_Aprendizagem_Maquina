/*
  Livro de ocorrências digital – análise SQL (CRISP-DM)
  Ciência de Dados e Aprendizagem de Máquina (A1) · UDF · Profa. Dra. Kadidja Valéria Reginaldo de Oliveira
  Equipe: Arthur Rodrigues de Souza Vieira (sistema, SQL e painel) · Ramon Guilherme Marques do Nascimento (dados e análise)

  Banco: PostgreSQL. O mesmo arquivo roda no DuckDB com: python scripts/rodar_sql_duckdb.py
  Base: dados/livro_ocorrencias_transcrito.csv (transcrição anonimizada do livro físico – DADOS SIMULADOS)

  Conteúdo:
    Tabela ocorrencia_bruta e carga do CSV
    V1–V7  validações de qualidade da base bruta
    C      concordância da categorização em dupla (objetivo específico 1)
    View   ocorrencias_limpas (Fase 3 – mesma regra do notebook)
    KPI 1–7 indicadores do painel do síndico (perguntas de negócio 1 a 4)
    A–B    consultas de apoio (hipótese H3 e dispersão mensal)
*/

-- Tabela: transcrição do livro, uma linha por registro
CREATE TABLE ocorrencia_bruta (
    id_registro        INTEGER PRIMARY KEY,
    data               DATE,
    hora               VARCHAR(5),
    registrado_por     VARCHAR(20),
    local              VARCHAR(40),
    categoria_livro    VARCHAR(40),
    resumo             VARCHAR(200),
    houve_resposta     VARCHAR(3),
    data_resposta      DATE,
    desfecho           VARCHAR(120),
    categoria_ramon    VARCHAR(40),
    categoria_arthur   VARCHAR(40),
    categoria_consenso VARCHAR(40)
);

\copy ocorrencia_bruta FROM 'dados/livro_ocorrencias_transcrito.csv' WITH (FORMAT csv, HEADER true)

-- V1 – registros sem hora
SELECT COUNT(*) AS sem_hora FROM ocorrencia_bruta WHERE hora IS NULL;

-- V2 – registros sem local
SELECT COUNT(*) AS sem_local FROM ocorrencia_bruta WHERE local IS NULL;

-- V3 – registros ilegíveis
SELECT COUNT(*) AS ilegiveis FROM ocorrencia_bruta WHERE resumo = '[ilegível]';

-- V4 – data fora do período transcrito (nov./2024 a out./2026)
SELECT id_registro, data, categoria_consenso
FROM ocorrencia_bruta
WHERE data < DATE '2024-11-01' OR data > DATE '2026-10-31'
ORDER BY id_registro;

-- V5 – resposta anterior ao registro ou "sim" sem data de resposta
SELECT COUNT(*) AS resposta_inconsistente
FROM ocorrencia_bruta
WHERE data_resposta < data OR (houve_resposta = 'sim' AND data_resposta IS NULL);

-- V6 – possível identificador no resumo (número de apartamento ou placa)
SELECT id_registro, resumo
FROM ocorrencia_bruta
WHERE regexp_like(resumo, '(apto|ap\.?|apartamento)\s*[0-9]{3}|[A-Z]{3}-?[0-9][A-Z0-9][0-9]{2}', 'i')
ORDER BY id_registro;

-- V7 – a mesma ocorrência anotada mais de uma vez (mesma data, hora, local e resumo)
SELECT SUM(n - 1) AS duplicados
FROM (SELECT data, hora, local, resumo, COUNT(*) AS n
      FROM ocorrencia_bruta
      GROUP BY data, hora, local, resumo) g;

-- C – concordância da categorização em dupla (meta ≥ 80%)
SELECT COUNT(*) AS registros,
       SUM(CASE WHEN categoria_ramon = categoria_arthur THEN 1 ELSE 0 END) AS iguais,
       ROUND(100.0 * SUM(CASE WHEN categoria_ramon = categoria_arthur THEN 1 ELSE 0 END) / COUNT(*), 1) AS concordancia_pct
FROM ocorrencia_bruta;

-- View – base limpa (Fase 3)
-- Remove identificadores e duplicados, corrige o ano trocado, anula datas de resposta inválidas,
-- padroniza o local vazio e calcula recorrência, carga dos últimos 30 dias e completude
CREATE VIEW ocorrencias_limpas AS
WITH sem_dup AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY data, hora, local, resumo ORDER BY id_registro) AS rn
    FROM ocorrencia_bruta
), corrigida AS (
    SELECT id_registro,
           CAST(CASE EXTRACT(YEAR FROM data) WHEN 2052 THEN data - INTERVAL '27 years'
                                             WHEN 2062 THEN data - INTERVAL '36 years'
                                             ELSE data END AS DATE) AS data,
           hora,
           CAST(SUBSTRING(hora, 1, 2) AS INTEGER) AS hora_num,
           registrado_por,
           COALESCE(local, 'Não informado') AS local,
           categoria_consenso AS categoria,
           regexp_replace(resumo, '(apto|ap\.?|apartamento)\s*[0-9]{3}|[A-Z]{3}-?[0-9][A-Z0-9][0-9]{2}', '(unidade)', 'gi') AS resumo,
           houve_resposta,
           data_resposta,
           desfecho
    FROM sem_dup
    WHERE rn = 1
), base AS (
    SELECT c.*,
           CASE WHEN c.data_resposta < c.data THEN NULL ELSE c.data_resposta END AS data_resposta_ok,
           ROW_NUMBER() OVER (ORDER BY c.data, c.hora_num NULLS LAST, c.id_registro) AS ordem
    FROM corrigida c
)
SELECT b.id_registro, b.data, b.hora, b.hora_num, b.registrado_por, b.local, b.categoria, b.resumo,
       b.houve_resposta, b.data_resposta_ok AS data_resposta, b.desfecho,
       CASE WHEN b.houve_resposta = 'não' THEN 1 ELSE 0 END AS sem_resposta,
       b.data_resposta_ok - b.data AS dias_ate_resposta,
       (b.hora_num >= 22 OR b.hora_num < 6) AS noturno,
       EXTRACT(ISODOW FROM b.data) >= 6 AS fim_de_semana,
       (b.hora IS NOT NULL AND b.local <> 'Não informado' AND b.categoria <> 'Não identificada') AS completo,
       (SELECT COUNT(*) FROM base o WHERE o.data >= b.data - INTERVAL '30 days' AND o.data < b.data) AS carga_30d,
       EXISTS (SELECT 1 FROM base o
               WHERE o.categoria = b.categoria AND o.local = b.local AND b.local <> 'Não informado'
                 AND o.data >= b.data - INTERVAL '30 days' AND o.ordem < b.ordem) AS recorrente
FROM base b;

-- KPI 1 – visão geral do livro (cartões do painel)
SELECT COUNT(*) AS ocorrencias,
       ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT DATE_TRUNC('month', data)), 1) AS media_por_mes,
       ROUND(100.0 * (1 - AVG(sem_resposta)), 1) AS taxa_resposta_pct,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dias_ate_resposta) AS mediana_dias,
       ROUND(100.0 * AVG(CASE WHEN recorrente THEN 1 ELSE 0 END), 1) AS recorrentes_pct,
       ROUND(100.0 * AVG(CASE WHEN completo THEN 1 ELSE 0 END), 1) AS completos_pct
FROM ocorrencias_limpas;

-- KPI 2 – Pareto das categorias (PN 1 / H1)
SELECT categoria,
       COUNT(*) AS ocorrencias,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS perc,
       ROUND(100.0 * SUM(COUNT(*)) OVER (ORDER BY COUNT(*) DESC, categoria) / SUM(COUNT(*)) OVER (), 1) AS perc_acumulado
FROM ocorrencias_limpas
GROUP BY categoria
ORDER BY ocorrencias DESC, categoria;

-- KPI 3 – locais com mais ocorrências e a categoria principal de cada um (PN 1)
WITH por_local AS (
    SELECT local, categoria, COUNT(*) AS n,
           ROW_NUMBER() OVER (PARTITION BY local ORDER BY COUNT(*) DESC, categoria) AS pos
    FROM ocorrencias_limpas
    GROUP BY local, categoria
)
SELECT local, SUM(n) AS ocorrencias,
       MAX(CASE WHEN pos = 1 THEN categoria END) AS categoria_principal
FROM por_local
GROUP BY local
ORDER BY ocorrencias DESC, local
LIMIT 10;

-- KPI 4 – taxa de resposta e mediana de dias por categoria (PN 2 / H2)
SELECT categoria,
       COUNT(*) AS ocorrencias,
       ROUND(100.0 * (1 - AVG(sem_resposta)), 1) AS taxa_resposta_pct,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dias_ate_resposta) AS mediana_dias
FROM ocorrencias_limpas
GROUP BY categoria
ORDER BY taxa_resposta_pct, categoria;

-- KPI 5 – barulho por dia da semana e faixa de horário (PN 3 / H3 – mapa de calor)
SELECT CASE WHEN hora_num < 6 THEN '0h–6h' WHEN hora_num < 12 THEN '6h–12h' WHEN hora_num < 18 THEN '12h–18h'
            WHEN hora_num < 22 THEN '18h–22h' ELSE '22h–24h' END AS faixa,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 1 THEN 1 ELSE 0 END) AS seg,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 2 THEN 1 ELSE 0 END) AS ter,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 3 THEN 1 ELSE 0 END) AS qua,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 4 THEN 1 ELSE 0 END) AS qui,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 5 THEN 1 ELSE 0 END) AS sex,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 6 THEN 1 ELSE 0 END) AS sab,
       SUM(CASE WHEN EXTRACT(ISODOW FROM data) = 7 THEN 1 ELSE 0 END) AS dom
FROM ocorrencias_limpas
WHERE categoria = 'Barulho' AND hora_num IS NOT NULL
GROUP BY 1
ORDER BY MIN(CASE WHEN hora_num < 6 THEN 0 WHEN hora_num < 12 THEN 1 WHEN hora_num < 18 THEN 2 WHEN hora_num < 22 THEN 3 ELSE 4 END);

-- KPI 6 – recorrência: mesma categoria no mesmo local em até 30 dias (PN 4)
SELECT categoria,
       COUNT(*) AS ocorrencias,
       SUM(CASE WHEN recorrente THEN 1 ELSE 0 END) AS recorrentes,
       ROUND(100.0 * AVG(CASE WHEN recorrente THEN 1 ELSE 0 END), 1) AS recorrencia_pct
FROM ocorrencias_limpas
GROUP BY categoria
ORDER BY recorrencia_pct DESC, categoria;

-- KPI 7 – taxa de resposta por quem registrou a ocorrência (PN 2)
SELECT registrado_por,
       COUNT(*) AS ocorrencias,
       ROUND(100.0 * (1 - AVG(sem_resposta)), 1) AS taxa_resposta_pct,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dias_ate_resposta) AS mediana_dias
FROM ocorrencias_limpas
GROUP BY registrado_por
ORDER BY taxa_resposta_pct, registrado_por;

-- A – H3: parcela do barulho entre 22h e 6h ou no fim de semana
SELECT COUNT(*) AS barulho_com_hora,
       ROUND(100.0 * AVG(CASE WHEN noturno OR fim_de_semana THEN 1 ELSE 0 END), 1) AS noite_ou_fds_pct
FROM ocorrencias_limpas
WHERE categoria = 'Barulho' AND hora_num IS NOT NULL;

-- B – série mensal para o diagrama de dispersão (ocorrências × taxa de resposta)
SELECT DATE_TRUNC('month', data) AS mes,
       COUNT(*) AS ocorrencias,
       ROUND(100.0 * (1 - AVG(sem_resposta)), 1) AS taxa_resposta_pct,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dias_ate_resposta) AS mediana_dias
FROM ocorrencias_limpas
GROUP BY 1
ORDER BY 1;

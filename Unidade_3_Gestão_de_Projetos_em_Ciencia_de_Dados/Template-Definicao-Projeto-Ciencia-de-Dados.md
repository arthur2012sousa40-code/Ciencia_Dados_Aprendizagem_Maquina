# Template - Definição do Projeto de Ciência de Dados

**Unidade:** III - Gestão de Projetos  
**Metodologia:** PBL + trabalho em equipes  
**Entregável:** Documento de definição do projeto

> **Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si.

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto | Assistente Virtual: RAG e modelo de linguagem local para atendimento e automação de protocolo em uma administradora de condomínios |
| Curso / disciplina | Sistemas de Informação / Ciência de Dados e Aprendizagem de Máquina |
| Turma | Turma de Ciência de Dados – UDF |
| Equipe | Arthur & Ramon |
| Integrantes e funções iniciais | Arthur Rodrigues de Souza Vieira (arquitetura e implementação back-end); Ramon Guilherme Marques do Nascimento (pipeline de RAG e avaliação) |
| Professor(a) | A definir (orientador a ser confirmado) |
| Data de elaboração | 16/09/2026 |
| Versão do documento | 1.0 |

## 2. Visão geral

### 2.1 Resumo do projeto

Em até 100 palavras, apresente o problema, o público-alvo, a proposta de análise e o resultado esperado.

**Preenchimento:**

Uma administradora de condomínios enfrenta alto volume de dúvidas repetitivas dos condôminos e processos manuais de protocolo, sem canal único de atendimento e com baixa rastreabilidade. O projeto propõe um assistente virtual baseado em Inteligência Artificial executada localmente, utilizando a técnica RAG (Retrieval-Augmented Generation) com modelo de linguagem aberto (Llama 3.1 8B Instruct), armazenando vetores no próprio banco relacional (MySQL). A solução responde dúvidas com fontes citadas, automatiza o protocolo e garante conformidade com a LGPD, sem enviar dados a serviços externos.

### 2.2 Declaração do projeto em uma frase

> Nosso projeto utilizará **dados e documentos internos do Departamento de Protocolo de uma administradora de condomínios** para compreender/prever **as dúvidas mais recorrentes dos condôminos e o fluxo de despacho de guias de pagamento**, apoiando **síndicos, condôminos e a equipe de protocolo** na decisão de **responder dúvidas com precisão e rastrear solicitações operacionais de ponta a ponta, sem expor dados sensíveis a terceiros**.

## 3. Contexto e definição do problema

### 3.1 Contexto

- **Onde o problema ocorre?** Na administradora de condomínios, nos fluxos de atendimento ao condômino (dúvidas sobre guias, malotes, prazos e segunda via) e no processo de despacho físico das guias de pagamento entre os departamentos Pessoal, Protocolo e entregador.
- **Quem é afetado?** Condôminos e síndicos (que aguardam respostas rápidas e rastreáveis), a equipe de protocolo (sobrecarregada com perguntas repetitivas) e os gestores (sem visibilidade dos indicadores de atendimento).
- **Quais sinais indicam sua existência?** Ausência de canal único de atendimento; dúvidas chegando por múltiplos meios sem padronização; processo de despacho dependente de intervenção manual em sistemas distintos; rastreabilidade de entregas apenas parcial.
- **Por que investigar agora?** O avanço dos LLMs abertos viabiliza execução local de IA com custo zero de API externa; a LGPD torna urgente evitar o envio de dados de clientes à nuvem; e a maturidade de frameworks como RAG permite fundamentar respostas em fontes verificáveis, reduzindo alucinações.

### 3.2 Problema central

> A equipe de protocolo e os condôminos de uma administradora de condomínios enfrentam **ausência de canal único de atendimento e alta dependência de intervenção manual nos processos de despacho de guias** no contexto de um fluxo fragmentado entre múltiplos sistemas e departamentos, produzindo **lentidão no atendimento, respostas não padronizadas, baixa rastreabilidade das solicitações e risco de exposição de dados pessoais ao utilizar serviços de IA em nuvem**.

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| 1. Processo as-is mapeado em BPMN com quatro raias e múltiplos pontos de intervenção manual | Modelagem dos autores com base no processo real da organização | Complexidade operacional e ausência de ponto único de entrada | Alta (processo observado internamente); limitação: recorte de uma organização |
| 2. Literatura confirma que RAG supera fine-tuning para incorporar conhecimento factual novo e reduzir alucinações (OVADIA et al., 2024; JI et al., 2023) | Artigos científicos indexados (ACM, EMNLP) | RAG é a abordagem mais adequada para bases de conhecimento que mudam com frequência | Alta (peer-reviewed); limitação: estudos em domínios genéricos, não condominiais |
| 3. Nenhum trabalho brasileiro identificado combina LLM local + RAG + LGPD + banco relacional como índice vetorial no domínio condominial (revisão em SBC OpenLib, IEEE Xplore, arXiv) | Revisão de literatura dos autores | Lacuna original que justifica a contribuição do projeto | Alta para as bases consultadas; limitação: possível existência de trabalhos não indexados |

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? | Condôminos e síndicos (usuários finais do assistente) e a equipe do Departamento de Protocolo (usuária do painel administrativo e da automação) |
| Quais necessidades possuem? | Respostas rápidas e confiáveis sobre prazos, guias, malotes e segunda via; rastreamento de solicitações de protocolo; redução do tempo gasto em perguntas repetitivas |
| Como são afetados pelo problema? | Condôminos aguardam respostas por canais dispersos; a equipe perde tempo respondendo manualmente dúvidas recorrentes e gerenciando entregas sem rastreabilidade centralizada |
| Que decisão ou ação poderão tomar com os resultados? | Condôminos: resolver dúvidas sem contato humano e abrir solicitações de protocolo pelo mesmo canal. Equipe: monitorar entregas e indicadores de atendimento em painel único |

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
| Administradora de condomínios (gestores) | Reduzir custo operacional de atendimento e eliminar API pagas de IA | Alta | Validação dos processos mapeados (as-is/to-be) e aprovação da base de conhecimento |
| Departamento de Protocolo | Automatizar despacho e acompanhar entregas com rastreabilidade digital | Alta | Fornecimento dos dados e documentos para a base de conhecimento; testes de aceitação |
| Condôminos e síndicos | Obter respostas rápidas e rastreáveis sem exposição de dados | Baixa | Avaliação qualitativa e futuros testes de satisfação |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Desenvolver um assistente virtual baseado em IA executada localmente que responda às dúvidas dos condôminos a partir de uma base de conhecimento selecionada e integre o fluxo de atendimento ao processo de protocolo da administradora de condomínios, preservando a privacidade dos dados em conformidade com a LGPD.

### 5.2 Objetivos específicos

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | Modelar o processo atual (as-is) e propor um fluxo redesenhado (to-be) que integre atendimento e protocolo | Diagramas BPMN as-is e to-be validados pelos gestores da organização |
| 2 | Implementar um pipeline de RAG utilizando o banco de dados relacional (MySQL) como índice vetorial, dispensando infraestrutura especializada | Pipeline funcional com indexação, recuperação por similaridade de cosseno e geração de resposta operando em localhost |
| 3 | Empregar um modelo de linguagem aberto executado localmente (Llama 3.1 8B Instruct via LM Studio) para garantir que nenhum dado trafegue para a nuvem | Zero requisições externas de dados de usuários confirmadas por inspeção de rede durante a avaliação |
| 4 | Aplicar engenharia de prompt (few-shot e chain-of-thought) para reduzir alucinações e citar as fontes utilizadas em cada resposta | Taxa de recusa correta ≥ 95% nas perguntas fora do escopo e fontes exibidas em 100% das respostas dentro do escopo |
| 5 | Registrar métricas de uso (taxa de cobertura, taxa de recusa correta e latência) para avaliação objetiva da solução | Tabela de resultados com média de pelo menos 3 execuções sobre conjunto de ≥ 40 perguntas balanceadas (dentro e fora do escopo) |

### 5.3 Verificação dos objetivos

Marque após revisar:

- [x] São específicos e escritos com clareza.
- [x] Podem ser verificados por meio de entregáveis ou métricas.
- [x] São viáveis com os dados, recursos e tempo disponíveis.
- [x] Estão diretamente relacionados ao problema central.
- [x] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 | Qual a proporção de dúvidas dos condôminos que podem ser resolvidas automaticamente pela base de conhecimento atual? | Decidir o escopo mínimo viável da base de conhecimento | Logs de conversa (perguntas e indicador de cobertura) | Taxa de cobertura: perguntas dentro do escopo com contexto recuperado / total de perguntas |
| 2 | Em que porcentagem dos casos o assistente recusa corretamente perguntas fora do escopo sem inventar informações? | Escolha do modelo de geração (alinhado vs. fine-tune) e do limiar de similaridade | Logs de conversa com indicador de recusa correta e variante do modelo utilizada | Taxa de recusa correta por modelo e por limiar (ablação) |
| 3 | Qual é a latência média de resposta do pipeline de RAG no hardware disponível e ela é aceitável para atendimento conversacional? | Decisão sobre hardware mínimo para produção e viabilidade de streaming | Registro de latência por interação nos logs | Latência média, mediana e percentil 95 por execução |
| 4 | Quais são os tópicos mais recorrentes nas solicitações e dúvidas dos condôminos? | Priorização dos itens a indexar na base de conhecimento e identificação de lacunas | Histórico de atendimentos e logs do assistente em produção | Frequência de tópicos por categoria; itens mais recuperados com maior similaridade |
| 5 | O uso do banco relacional como índice vetorial (varredura linear) mantém desempenho aceitável à medida que a base cresce? | Decisão sobre migrar ou não para um banco vetorial dedicado (ex.: pgvector) | Volume de itens indexados e latência de recuperação medida em diferentes tamanhos de base | Curva de latência de recuperação × número de itens indexados |

## 7. Hipóteses iniciais

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1. O modelo Llama 3.1 8B Instruct recusa perguntas fora do escopo de forma mais confiável do que o fine-tune dolphin3.0-llama3.1-8b, mesmo sem ajuste do limiar de similaridade | Comparar taxa de recusa correta dos dois modelos com o mesmo conjunto de perguntas, limiar e prompt (ablação descrita na Seção 2.10.4 do TCC) | Taxa de recusa do Instruct inferior ou igual à do dolphin para o mesmo limiar |
| H2. A varredura linear de similaridade de cosseno no MySQL é suficiente (latência < 3 s) para uma base de conhecimento de dezenas a centenas de itens em hardware de consumo | Medir latência de recuperação com base de tamanhos crescentes (50, 100, 200, 500 itens) no hardware utilizado (notebook com RTX 4060) | Latência de recuperação superior a 3 s mesmo com base de até 200 itens |
| H3. A combinação de RAG + few-shot + chain-of-thought é suficiente para eliminar alucinações nas perguntas dentro do escopo, sem necessidade de fine-tuning | Avaliar se todas as respostas dentro do escopo citam fontes recuperadas e não inventam fatos ausentes da base | Presença de afirmações incorretas ou inventadas em respostas a perguntas cobertas pela base |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
| Base de conhecimento do Departamento de Protocolo | Título, conteúdo textual, URL de origem, vetor de embedding (768 dimensões) | Registros na tabela `assistente_knowledge` (MySQL) + JSON para o vetor | Equipe do projeto / Departamento de Protocolo | Alta: conteúdo curado manualmente pela equipe; ausência de dados duplicados controlada pelo serviço de indexação |
| Logs de conversa do assistente (benchmark) | Pergunta, resposta gerada, fontes citadas, latência (ms), indicador de cobertura/recusa | Registros na tabela `assistente_chat_logs` (MySQL) | Equipe do projeto (gerados automaticamente pelo pipeline) | Alta para perguntas do conjunto de avaliação; representatividade limitada (42 perguntas sintéticas) |
| Conjunto de avaliação (42 perguntas) | Texto da pergunta, classificação (dentro/fora do escopo) | Arquivo de texto estruturado / código do benchmark | Equipe do projeto | Alta: construído propositalmente com 24 perguntas dentro e 18 fora do escopo |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** Base de conhecimento disponível internamente; logs gerados pelo próprio sistema durante a avaliação; conjunto de benchmark construído pela equipe.
- **Volume e período coberto:** Base inicial com dezenas de itens curados; logs cobrindo três execuções completas do benchmark (126 interações no total: 42 perguntas × 3 execuções).
- **Dados ausentes, duplicados ou inconsistentes previstos:** Itens sem embedding (resolvidos pelo serviço de indexação que percorre registros sem vetor); perguntas ambíguas entre escopo e fora do escopo (mitigadas pela seleção manual do conjunto de avaliação).
- **Necessidade de integração entre fontes:** Integração entre MySQL (base e logs), LM Studio (embeddings e geração), Bitrix24 (tarefas) e Superlógica (gestão condominial) via HTTP/API.
- **Restrições legais, contratuais ou institucionais:** Dados de condôminos são dados pessoais nos termos da LGPD (Lei 13.709/2018); toda a inferência é executada localmente (localhost), eliminando transferência a terceiros; logs serão minimizados, anonimizados ou expurgados conforme política de retenção.

### 8.2 Privacidade, ética e segurança

- [x] A equipe verificou se há dados pessoais ou sensíveis.
- [x] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [x] O acesso será limitado às pessoas autorizadas.
- [x] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [x] Possíveis vieses e impactos sobre grupos serão analisados.
- [x] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:**

Todo o processamento de IA ocorre em localhost (LM Studio), sem envio de dados a APIs externas, eliminando na origem o risco de transferência internacional não autorizada (art. 33 da LGPD). Os logs registram apenas pergunta, resposta, fontes, latência e indicador de sucesso — sem dados bancários, documentos ou senhas. Há defesa em profundidade contra injeção de prompt (filtros de entrada e saída + instrução de sistema) para evitar que o modelo revele sua configuração interna ou assuma outra persona.

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
| Atendimento a dúvidas sobre guias de pagamento, malotes, prazos, segunda via e procedimentos do Departamento de Protocolo | Consultas jurídicas, financeiras ou contábeis sobre os condomínios |
| Pipeline de RAG com indexação, recuperação semântica e geração local | Treinamento (fine-tuning) de modelos de linguagem |
| Automação do protocolo: registro de solicitação, criação de malote, abertura de tarefa no Bitrix24, notificação de status | Desenvolvimento de novos módulos da plataforma Flarum não relacionados ao assistente |
| Integração com Superlógica (gestão condominial) e aplicativo Flutter para confirmação de entrega | Módulo de pagamento ou emissão de boletos |
| Avaliação com conjunto de 42 perguntas em 3 execuções (métricas: cobertura, recusa correta, latência) | Avaliação qualitativa com usuários reais em produção (indicada como trabalho futuro) |
| Conformidade com a LGPD (execução local, minimização de logs, política de expurgo) | Certificação ou auditoria formal de conformidade por órgão externo |

**Restrições conhecidas:** Hardware disponível condiciona a latência de geração local (RTX 4060 Laptop, 8 GB VRAM). A base de conhecimento depende de manutenção manual pela equipe do Protocolo. O conjunto de avaliação é sintético (42 perguntas), limitando a generalização dos percentuais. O prazo do TCC delimita o escopo da avaliação a métricas de log, sem testes com usuários reais.

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | Base de conhecimento indexada com vetores de embedding (nomic-embed-text-v1.5, 768 dim.) armazenados em MySQL | Tabela `assistente_knowledge` com coluna de embedding em JSON | Arthur | 100% dos itens com vetor gerado e sem duplicatas |
| Análise exploratória | Avaliação do pipeline com 42 perguntas em 3 execuções: taxa de cobertura, recusa correta, acerto geral e latência; ablação do limiar e comparação de modelos | Tabelas e gráfico de barras (Figuras 6, 7 e 8 do TCC) | Ramon | Reprodutibilidade confirmada em 3 execuções independentes |
| Visualizações / painel | Diagramas BPMN (as-is e to-be), diagrama de arquitetura, fluxo de dados do RAG e comparativo de modelos | Figuras embarcadas no TCC (PNG/PDF) + painel administrativo Flarum | Arthur e Ramon | Diagramas validados pelos orientadores; painel funcional em ambiente de teste |
| Relatório ou apresentação | Trabalho de Conclusão de Curso completo com introdução, desenvolvimento, resultados e conclusão | PDF (46 páginas, normas ABNT/UDF) | Arthur e Ramon | Aprovação pela banca examinadora do UDF |
| Extensão Flarum (código-fonte) | Extensão PHP/TypeScript com os módulos de recebimento de mensagens, motor de protocolo, serviços de IA (embedding + chat) e filtros de segurança | Repositório Git (código aberto) | Arthur | Testes funcionais passando; filtros de injeção de prompt operacionais |

## 11. Critérios de sucesso

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema | Cobertura do pipeline nas perguntas dentro do escopo | 100% das perguntas dentro do escopo com contexto recuperado | Tabela de resultados do benchmark (média de 3 execuções) |
| Qualidade dos dados | Itens da base de conhecimento com embedding gerado e sem duplicatas | 100% dos itens indexados | Consulta à tabela `assistente_knowledge` |
| Qualidade da análise | Taxa de recusa correta nas perguntas fora do escopo | ≥ 95% (meta alcançada: 100% com Llama 3.1 Instruct) | Tabela 4 e Tabela 6 do TCC |
| Utilidade para o público-alvo | Latência média de resposta compatível com atendimento conversacional | < 3 segundos (alcançado: ≈ 1,9 s) | Logs de latência do benchmark |
| Comunicação dos resultados | Apresentação e defesa do TCC perante banca examinadora | Aprovação com nota mínima exigida pelo UDF | Ata de defesa assinada pelos examinadores |

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição | Preenchimento deste documento; delimitação do problema; identificação do stakeholder (Departamento de Protocolo) | Arthur e Ramon | Semana 1 | Acesso à organização e ao processo real |
| 2. Obtenção dos dados | Levantamento e curadoria dos documentos do Departamento de Protocolo; elaboração do conjunto de avaliação (42 perguntas) | Ramon | Semanas 2–3 | Validação do escopo com o responsável pelo Protocolo |
| 3. Preparação dos dados | Indexação dos itens na base de conhecimento (geração de embeddings via LM Studio); modelagem BPMN as-is e to-be | Arthur | Semanas 3–4 | LM Studio configurado; modelo nomic-embed-text-v1.5 disponível |
| 4. Análise / modelagem | Implementação do pipeline de RAG (recuperação, prompt, geração); integração com Bitrix24 e Superlógica; aplicativo Flutter para entregador | Arthur e Ramon | Semanas 4–8 | Base indexada; modelos Llama 3.1 disponíveis no LM Studio |
| 5. Validação | Execução do benchmark (3 execuções × 42 perguntas); ablação do limiar; comparação de modelos; testes de injeção de prompt | Ramon | Semanas 8–9 | Pipeline completo e funcional |
| 6. Comunicação | Redação final do TCC; preparação da apresentação; submissão e defesa perante banca | Arthur e Ramon | Semanas 9–12 | Resultados consolidados e validados |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
| Hardware insuficiente para executar o modelo localmente com latência aceitável | Baixa | Alto | Utilizar notebook com GPU dedicada (RTX 4060 Laptop, 8 GB VRAM, já disponível); monitorar latência desde os primeiros testes | Arthur |
| Base de conhecimento insuficiente ou desatualizada, gerando lacunas de cobertura | Média | Alto | Revisar e expandir a base com o Departamento de Protocolo antes da avaliação; implementar serviço de reindexação incremental | Ramon |
| Modelo de geração alucinando mesmo com RAG (semelhante ao comportamento do fine-tune dolphin) | Média | Alto | Adotar modelo alinhado (Llama 3.1 Instruct) comprovadamente superior na ablação; aplicar filtros de entrada e saída contra injeção de prompt | Arthur e Ramon |
| Indisponibilidade do LM Studio durante a avaliação | Baixa | Médio | Implementar tratamento de falha controlada na aplicação; manter registro da versão exata do servidor utilizado para reprodutibilidade | Arthur |
| Não obtenção de orientador antes do prazo de submissão | Média | Alto | Registrar o projeto formalmente; apresentar este documento como evidência de planejamento; buscar orientadores com perfil em IA ou engenharia de software | Arthur e Ramon |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| Arthur Rodrigues de Souza Vieira | Arquiteto de solução e desenvolvedor back-end | Implementação da extensão Flarum (PHP/TypeScript); integração com LM Studio, Bitrix24 e Superlógica; aplicativo Flutter para entregador; filtros de segurança | Acesso ao ambiente da administradora; revisão dos diagramas de arquitetura pelo orientador |
| Ramon Guilherme Marques do Nascimento | Cientista de dados e responsável pela avaliação | Curadoria da base de conhecimento; elaboração do conjunto de avaliação; execução e análise do benchmark; ablação do limiar e comparação de modelos; redação do TCC | Acesso aos documentos do Departamento de Protocolo; validação das métricas pelo orientador |

## 15. Validação da definição do projeto

Antes da entrega, confirme:

- [x] O problema é real, relevante e delimitado.
- [x] O público-alvo e as partes interessadas estão identificados.
- [x] O objetivo geral e os objetivos específicos são coerentes.
- [x] As perguntas de negócio orientam decisões concretas.
- [x] Há dados potencialmente disponíveis para responder às perguntas.
- [x] O escopo é compatível com o prazo e os recursos.
- [x] Os critérios de sucesso são mensuráveis.
- [x] Riscos, privacidade, ética e segurança foram considerados.
- [x] Funções e responsabilidades foram distribuídas.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Representante da equipe | Arthur Rodrigues de Souza Vieira / Ramon Guilherme Marques do Nascimento | 16/09/2026 |
| Professor(a) / orientador(a) | A preencher após confirmação do orientador | — |

### Ajustes solicitados após a apresentação inicial

*(A preencher após apresentação do documento à banca ou ao orientador)*

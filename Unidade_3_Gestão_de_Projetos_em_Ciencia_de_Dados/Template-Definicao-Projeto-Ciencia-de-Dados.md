# Template - Definição do Projeto de Ciência de Dados

**Unidade:** III - Gestão de Projetos  
**Metodologia:** PBL + trabalho em equipes  
**Entregável:** Documento de definição do projeto

> **Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si.

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto | Livro de ocorrências digital para condomínios residenciais: do registro em papel a indicadores para a gestão do síndico |
| Curso / disciplina | Sistemas de Informação / Ciência de Dados e Aprendizagem de Máquina |
| Turma | Turma de Ciência de Dados – UDF |
| Equipe | Arthur & Ramon |
| Integrantes e funções iniciais | Arthur Rodrigues de Souza Vieira (desenvolvimento do sistema e do painel); Ramon Guilherme Marques do Nascimento (coleta, tratamento e análise dos dados) |
| Professor(a) | Prof.ª Dra. Kadidja Valéria Reginaldo de Oliveira |
| Data de elaboração | 06/10/2026 |
| Versão do documento | 2.0 (redefinição de tema e de escopo; ver Seção 16) |

## 2. Visão geral

### 2.1 Resumo do projeto

Em até 100 palavras, apresente o problema, o público-alvo, a proposta de análise e o resultado esperado.

**Preenchimento:**

Em muitos prédios antigos do DF, as ocorrências do condomínio (barulho, vazamentos, garagem, áreas comuns) ainda são registradas em um livro físico na portaria. Esse formato não permite acompanhar o andamento, consultar o histórico nem medir nada. O projeto vai transcrever e anonimizar de 12 a 24 meses do livro de um condomínio real, fazer a análise exploratória desses dados e, com base nela, desenvolver um livro de ocorrências digital com painel de indicadores para o síndico. A solução será avaliada com moradores, portaria e síndico.

### 2.2 Declaração do projeto em uma frase

> Nosso projeto utilizará **os registros do livro de ocorrências físico de um condomínio residencial do DF, transcritos e anonimizados, além de questionário com moradores e entrevistas com síndico e portaria**, para compreender **quais ocorrências mais acontecem, onde, quando e quantas ficam sem resposta**, apoiando **o síndico, a portaria e os moradores** na decisão de **priorizar problemas recorrentes, definir prazos de resposta e substituir o livro em papel por um registro digital acompanhável**.

## 3. Contexto e definição do problema

### 3.1 Contexto

- **Onde o problema ocorre?** Em condomínios residenciais do DF, especialmente prédios antigos, que ainda registram as ocorrências em um livro físico na portaria. O estudo será feito em um condomínio real; há dois candidatos já identificados.
- **Quem é afetado?**
  - Moradores: precisam ir à portaria para registrar e não sabem se houve resposta.
  - Síndico: só toma conhecimento quando folheia o livro e não tem visão do conjunto.
  - Portaria: registra à mão e responde a dúvidas sobre o andamento.
- **Quais sinais indicam sua existência?**
  - Registros sem resposta anotada, ilegíveis ou incompletos.
  - Moradores que comunicam problemas por canais paralelos (WhatsApp, verbalmente).
  - Livro acessível a qualquer pessoa na portaria, expondo ocorrências de terceiros.
  - Nenhum indicador sobre o que acontece no prédio.
  - Esses sinais serão confirmados na transcrição e nas entrevistas.
- **Por que investigar agora?**
  - O DF tem a maior proporção de moradores em apartamento do país (28,7% da população; 34,2% dos domicílios são apartamentos, segundo o Censo 2022).
  - Boa parte dos prédios do Plano Piloto tem 60 anos ou mais.
  - A LGPD exige controlar quem acessa dados pessoais, o que o livro físico não faz.
  - Apps comerciais já oferecem o recurso, mas vinculados a administradoras ou a planos pagos, e não chegam a prédios pequenos com síndico morador.

### 3.2 Problema central

> O síndico, a portaria e os moradores de um condomínio residencial do DF enfrentam **um registro de ocorrências em papel que não permite acompanhar, pesquisar nem medir as ocorrências** no contexto de **um prédio antigo, sem administradora digital, em que o livro físico é o único canal formal**, produzindo **ocorrências sem resposta ou sem retorno ao morador, perda de histórico, exposição de dados de terceiros e ausência de informação para a gestão**.

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| 1. DF tem 338.279 apartamentos entre 988.175 domicílios ocupados (34,2%) e a maior proporção de pessoas morando em apartamento do país (28,7%) | IBGE, Censo 2022 (SIDRA Tabela 9930); SíndicoNet (2024) com dados do IBGE | O público potencial de gestão condominial no DF é grande | Alta (dado oficial); limitação: não informa quantos prédios usam livro físico |
| 2. "O DF, principalmente o Plano Piloto, tem prédios [...] muitos com 60 anos ou mais" | Correio Braziliense, 14/10/2023, p. 13 | Estoque predial antigo, onde práticas em papel tendem a persistir | Média (jornalística); limitação: não quantifica a idade média |
| 3. Livro de ocorrências não é obrigatório por lei; regras de acesso variam e há conflito sobre quem pode lê-lo | SíndicoNet (2013); Baccin Advogados (2022) | O processo atual é informal e sem padrão de privacidade | Média (fontes setoriais e jurídicas); limitação: não são estudos empíricos |
| 4. Registros estruturados de reclamações e de manutenção revelam padrões úteis à gestão; poucas categorias e locais concentram a maioria | Goins e Moezzi (2013); Dutta et al. (2020); Bortolini e Forcada (2020) | O dado de ocorrências tem valor analítico quando é digital e estruturado | Alta (revisados por pares); limitação: edifícios não residenciais ou fora do Brasil |
| 5. Dois condomínios do DF que usam livro físico foram identificados como candidatos ao estudo | Contato direto dos autores | O problema é acessível para coleta de dados reais | A confirmar na visita: volume e legibilidade dos registros |

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? | Síndico (usuário do painel e de quem responde), portaria e zeladoria (quem mais registra) e moradores (quem reclama e acompanha) |
| Quais necessidades possuem? | Síndico: saber o que acontece no prédio e responder com organização. Portaria: registrar rápido. Moradores: registrar sem ir à portaria, acompanhar o andamento e ter privacidade |
| Como são afetados pelo problema? | Ocorrências ficam sem retorno; o síndico decide sem dados; registros se perdem ou ficam ilegíveis; qualquer pessoa lê ocorrências alheias |
| Que decisão ou ação poderão tomar com os resultados? | Síndico: priorizar manutenções e regras com base nos problemas recorrentes, definir prazo de resposta e acompanhar o desempenho. Moradores: registrar e acompanhar pelo celular. Condomínio: decidir pela adoção do registro digital |

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
| Síndico | Organizar a gestão das ocorrências e ter indicadores | Alta | Autoriza a pesquisa, dá acesso ao livro, é entrevistado, valida requisitos e o painel, usa o sistema no piloto |
| Conselho do condomínio | Transparência e conformidade com a convenção e a LGPD | Média | Ciência da autorização; recebe o relatório final |
| Portaria e zeladoria | Registrar com menos esforço e menos cobrança dos moradores | Média | Entrevista; teste de usabilidade; uso no piloto |
| Moradores | Ser ouvidos, acompanhar o andamento e ter privacidade | Baixa (individual) / Alta (coletiva, em assembleia) | Questionário anônimo; teste de usabilidade; uso no piloto |
| Orientadora / UDF | Rigor metodológico e ético | Alta | Orientação; consulta sobre a necessidade de CEP |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Desenvolver e avaliar um livro de ocorrências digital para um condomínio residencial do DF, que permita registrar, acompanhar e responder às ocorrências e que ofereça ao síndico indicadores calculados a partir desses registros, tendo como ponto de partida a análise dos dados reais do livro físico.

### 5.2 Objetivos específicos

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | Transcrever e anonimizar de 12 a 24 meses do livro de ocorrências físico e categorizar os registros | Planilha anonimizada com dicionário de dados; percentual de concordância entre os dois autores na categorização (meta ≥ 80%) |
| 2 | Realizar a análise exploratória dos registros (volume, categorias, locais, horários, taxa de resposta, tempo até a resposta, recorrência, completude) | Notebook Python com tabelas e gráficos (Pareto, série mensal, mapa de calor) e relatório do diagnóstico |
| 3 | Levantar requisitos de negócio, de usuário e de sistema com síndico, portaria e moradores | Entrevistas transcritas, resultado do questionário, 5W2H e quadros de requisitos validados pelo síndico |
| 4 | Desenvolver um sistema web responsivo com registro, status, histórico imutável, acesso por perfil e painel de indicadores | Sistema publicado; painel reproduzindo os indicadores da análise exploratória com o histórico importado |
| 5 | Avaliar a solução com usuários reais e comparar os indicadores antes e depois | Teste de usabilidade com pontuação SUS; tabela comparativa entre o livro físico e o piloto |

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
| 1 | Quais tipos de ocorrência mais se repetem e em que locais? | Priorizar manutenções, comunicados e ajustes no regimento | Livro transcrito: categoria e local | Frequência e diagrama de Pareto por categoria e por local |
| 2 | Quantas ocorrências recebem resposta registrada e em quanto tempo? | Definir um prazo de resposta e uma meta para o síndico | Livro transcrito: houve resposta, data do registro e data da resposta | Taxa de resposta (%); mediana e maior tempo até a resposta, em dias |
| 3 | Em que dias e horários as ocorrências acontecem? | Ajustar rondas e escala da portaria e reforçar regras de silêncio | Livro transcrito: data e hora | Mapa de calor dia da semana × faixa de horário, por categoria |
| 4 | Há problemas que se repetem no mesmo local em pouco tempo? | Antecipar manutenção preventiva | Livro transcrito: categoria, local e data | Taxa de recorrência (mesma categoria e local em até 30 dias) |
| 5 | Os moradores usariam um registro pelo celular? Quais as barreiras? | Manter ou não um canal presencial pela portaria em paralelo | Questionário: interesse, barreiras e faixa etária | Percentual de "sim/talvez" por faixa etária; frequência das barreiras |
| 6 | O registro digital melhorou a resposta às ocorrências? | Adotar definitivamente o sistema | Indicadores do livro físico e do período de piloto | Comparação antes × depois da taxa de resposta, do tempo até a resposta e da completude |

## 7. Hipóteses iniciais

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1. Poucas categorias concentram a maioria das ocorrências | Pareto sobre o livro transcrito | As 3 categorias mais frequentes somarem menos de 50% dos registros |
| H2. A maior parte das ocorrências do livro físico não tem resposta registrada | Taxa de resposta no livro transcrito | Taxa de resposta registrada igual ou superior a 50% |
| H3. Ocorrências de barulho concentram-se à noite e nos fins de semana | Mapa de calor das ocorrências de barulho | Menos de 50% das ocorrências de barulho entre 22h e 6h ou em sábados e domingos |
| H4. A maioria dos moradores usaria o registro pelo celular | Pergunta 16 do questionário | Menos de 60% de respostas "sim" ou "talvez" |
| H5. Com o sistema, a taxa de resposta registrada aumenta em relação ao livro físico | Comparação antes × depois no piloto | Taxa de resposta no piloto igual ou inferior à do livro físico |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
| Livro de ocorrências físico (12 a 24 meses) | Data, hora, quem registrou, local, categoria, resumo, houve resposta, data da resposta, desfecho, completude | Planilha (CSV/XLSX) transcrita e anonimizada, com dicionário de dados | Síndico autoriza; Ramon transcreve no condomínio | Média: escrita à mão, com registros ilegíveis ou incompletos. A própria falta de qualidade é um achado do diagnóstico |
| Questionário com moradores | Faixa etária, tempo de residência, canais usados, retorno recebido, escala de 1 a 5, interesse e barreiras | Google Forms → CSV | Síndico divulga; equipe analisa | Média: adesão voluntária; divulgado a todas as unidades, com a taxa de participação informada (respostas ÷ unidades) |
| Entrevistas (síndico e portaria) | Processo atual, tempo gasto, problemas, necessidades | Transcrição em texto | Equipe | Alta para o processo; qualitativa, poucas pessoas |
| Registros do sistema no piloto | Ocorrências, movimentações de status, datas e registros de acesso | Banco de dados → CSV | Gerados automaticamente pelo sistema | Alta: campos obrigatórios e data e hora definidas pelo servidor |
| Teste de usabilidade | Sucesso e tempo por tarefa; respostas do SUS | Planilha | Equipe | Alta para o teste; amostra pequena (5 a 8 pessoas) |
| Dados públicos | Domicílios por tipo no DF | Tabela do IBGE (SIDRA 9930) | Público | Alta (oficial) |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** dois condomínios candidatos identificados; acesso condicionado à autorização assinada do síndico (carta pronta). Questionário e entrevistas dependem da mesma autorização.
- **Volume e período coberto:** 12 a 24 meses do livro. O volume ainda é desconhecido. Na primeira visita, contar os registros de algumas páginas para estimar o total. Se ficar abaixo de cerca de 200 registros, usar os dois condomínios ou ampliar o período.
- **Dados ausentes, duplicados ou inconsistentes previstos:** registros sem data ou sem hora, sem local, ilegíveis, sem desfecho; a mesma ocorrência anotada mais de uma vez; categorias escritas de formas diferentes. O tratamento usa o campo "completo", a padronização das categorias por análise de conteúdo e a marcação de duplicatas.
- **Necessidade de integração entre fontes:** a planilha do livro é importada para o sistema (CSV), e os indicadores do livro e do piloto são calculados da mesma forma para permitir a comparação. Questionário e entrevistas são analisados em separado.
- **Restrições legais, contratuais ou institucionais:**
  - As ocorrências contêm dados pessoais (LGPD, art. 5º, I), por isso a anonimização é feita já na transcrição.
  - É preciso autorização escrita do síndico.
  - Transcrição registro a registro e entrevistas podem exigir o Comitê de Ética em Pesquisa (CEP) da UDF (Res. CNS 510/2016; Ofício Circular CONEP 17/2022). A consulta será feita na semana 1.

### 8.2 Privacidade, ética e segurança

- [x] A equipe verificou se há dados pessoais ou sensíveis.
- [x] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [x] O acesso será limitado às pessoas autorizadas.
- [x] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [x] Possíveis vieses e impactos sobre grupos serão analisados.
- [x] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:**

- **Transcrição anonimizada:** nenhum nome, número de apartamento, placa ou telefone é copiado. A unidade vira uma referência genérica (bloco ou andar, só quando necessário) e a descrição é resumida em linguagem neutra.
- **Livro e fotos:** o livro não sai do condomínio, e eventuais fotos das páginas são apagadas após a transcrição.
- **Nome do condomínio:** não é divulgado sem autorização.
- **Questionário:** anônimo, sem coleta de e-mail.
- **Painel:** categorias com menos de 3 casos por bloco são agrupadas, para evitar reidentificação.
- **Sistema:** acesso por perfil e registro de quem acessou cada ocorrência (LGPD, art. 37).
- **Viés:** moradores mais velhos ou sem celular podem ser sub-representados no questionário e no uso do sistema. A análise será feita por faixa etária, e a portaria poderá registrar em nome do morador.

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
| Transcrição anonimizada e análise exploratória de 12 a 24 meses do livro físico | Uso de inteligência artificial ou aprendizado de máquina (classificação automática fica como trabalho futuro) |
| Entrevistas com síndico e portaria; questionário anônimo com moradores | Integração com WhatsApp, administradoras, boletos ou assembleias |
| Sistema web responsivo: registro com categoria, local, foto, data e hora; status; resposta do síndico | Aplicativo nativo para celular |
| Histórico sem exclusão e acesso por perfil (morador, portaria, síndico) | Vários condomínios na mesma instalação |
| Painel de indicadores e importação do histórico do livro | Reserva de áreas comuns, portaria remota e controle de acesso |
| Piloto de 2 a 4 semanas e teste de usabilidade com SUS | Assinatura com certificado digital ICP-Brasil |

**Restrições conhecidas:**

- Estudo de caso em um condomínio (dois, se o volume exigir), sem generalização para todo o DF.
- Dependência da autorização do síndico e, possivelmente, de parecer do CEP.
- Prazo do semestre: o piloto é curto, então a comparação antes × depois é indicativa.
- O livro físico só contém o que alguém decidiu escrever.

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | Registros do livro transcritos, anonimizados e categorizados, com dicionário de dados | Planilha CSV/XLSX + dicionário | Ramon | Nenhum dado identificador; concordância calculada; campos padronizados |
| Análise exploratória | Indicadores e gráficos do livro físico (Pareto, série mensal, mapa de calor, taxa de resposta, tempo até a resposta, recorrência, completude) e do questionário | Notebook Python (pandas, matplotlib) + relatório | Ramon | Responde às perguntas de negócio 1 a 5 e testa as hipóteses H1 a H4 |
| Visualizações / painel | Painel do síndico no sistema com os mesmos indicadores | Tela web do sistema | Arthur | Reproduz os indicadores do notebook com o histórico importado |
| Sistema | Livro de ocorrências digital (registro, status, histórico imutável, perfis, importação CSV) | Aplicação web + repositório Git | Arthur | Requisitos funcionais implementados; teste de usabilidade realizado |
| Relatório ou apresentação | TCC completo e relatório de indicadores entregue ao síndico | PDF (normas ABNT/UDF) + apresentação | Arthur e Ramon | Relatório entregue ao condomínio; TCC aprovado pela banca |

## 11. Critérios de sucesso

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema | Diagnóstico validado pelo síndico; perguntas de negócio respondidas | Síndico reconhece os achados como reais e úteis | Registro da reunião de validação |
| Qualidade dos dados | Concordância da categorização; dados sem identificadores | Concordância ≥ 80% (registros com a mesma categoria ÷ registros comparados × 100); 0 identificadores na base | Comparação das duas categorizações; revisão da planilha |
| Qualidade da análise | Indicadores reproduzíveis | Painel e notebook com os mesmos valores para o histórico importado | Comparação lado a lado |
| Utilidade para o público-alvo | Usabilidade e adoção no piloto | SUS ≥ 71 (média associada a "boa" em Bangor et al., 2009); taxa de resposta no piloto maior que a do livro físico | Questionário SUS; indicadores antes × depois |
| Comunicação dos resultados | Relatório ao condomínio e defesa do TCC | Relatório entregue; aprovação pela banca | Recibo do síndico; ata de defesa |

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição | Este documento; carta de autorização assinada; consulta à orientadora sobre o CEP; escolha do condomínio | Arthur e Ramon | Semanas 1–2 | Resposta dos síndicos |
| 2. Obtenção dos dados | Transcrição do livro; entrevistas; aplicação do questionário (após pré-teste) | Ramon (livro e questionário); Arthur (entrevistas) | Semanas 2–4 | Autorização; decisão sobre o CEP |
| 3. Preparação dos dados | Anonimização, padronização, categorização feita em dupla e cálculo da concordância | Ramon | Semanas 3–4 | Transcrição concluída |
| 4. Análise / modelagem | Análise exploratória em notebook; requisitos; modelagem UML; desenvolvimento do sistema e do painel | Ramon (análise); Arthur (sistema) | Semanas 4–8 | Base tratada; requisitos validados |
| 5. Validação | Importação do histórico; piloto no condomínio; teste de usabilidade (SUS); comparação antes × depois | Arthur e Ramon | Semanas 8–10 | Sistema publicado; adesão dos usuários |
| 6. Comunicação | Relatório ao síndico; redação final do TCC; apresentação | Arthur e Ramon | Semanas 10–12 | Resultados consolidados |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
| Síndico não autorizar ou desistir | Média | Alto | Dois condomínios candidatos; carta clara sobre LGPD e retorno ao condomínio (relatório de indicadores) | Arthur e Ramon |
| Poucos registros ou registros ilegíveis no livro | Média | Alto | Contar os registros na primeira visita; ampliar o período ou incluir o segundo condomínio; tratar a baixa qualidade como achado | Ramon |
| Exigência de parecer do CEP atrasar a coleta | Média | Alto | Consultar na semana 1; adiantar o desenvolvimento do sistema, que não depende dos dados | Arthur e Ramon |
| Baixa adesão ao questionário | Média | Médio | Divulgação pelo síndico, cartaz com QR code no mural e lembrete após uma semana | Ramon |
| Baixa adesão ao piloto, sobretudo de moradores mais velhos | Média | Médio | Portaria registra em nome do morador; tela simples; demonstração presencial | Arthur |
| Exposição de dados pessoais | Baixa | Alto | Anonimização na transcrição; fotos apagadas; acesso restrito à base; perfis no sistema | Ramon e Arthur |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| Arthur Rodrigues de Souza Vieira | Desenvolvedor do sistema | Requisitos e modelagem UML; desenvolvimento do sistema web e do painel; importação do histórico; condução das entrevistas; piloto e teste de usabilidade | Validação dos requisitos pelo síndico; revisão da arquitetura pela orientadora |
| Ramon Guilherme Marques do Nascimento | Responsável pelos dados e pela análise | Transcrição e anonimização do livro; categorização e cálculo da concordância; análise exploratória em Python; questionário; comparação antes × depois; redação do diagnóstico | Acesso ao livro no condomínio; orientação sobre o CEP e sobre a análise |

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
| Representante da equipe | Arthur Rodrigues de Souza Vieira / Ramon Guilherme Marques do Nascimento | 06/10/2026 |
| Professor(a) / orientador(a) | Prof.ª Dra. Kadidja Valéria Reginaldo de Oliveira: a preencher | — |

### Ajustes solicitados após a apresentação inicial

- **Versão 1.0 (16/09/2026):** assistente virtual com RAG e modelo de linguagem local para uma administradora de condomínios.
- **Ajuste recebido:** escopo sem definição clara, misturando RAG, canal de atendimento, gateway de mensagens, automação de protocolo e aplicativo. Faltavam requisito de negócio, stakeholder consultado e dados reais que comprovassem o problema.
- **Versão 2.0 (06/10/2026):** tema substituído por **livro de ocorrências digital**, sem IA, com escopo único e delimitado (Seção 9). O problema passa a ser comprovado com dados reais do livro físico de um condomínio do DF (Seção 8), e os requisitos de negócio derivam desse diagnóstico.

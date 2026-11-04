<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- Estudante ou equipe: **Arthur Rodrigues de Souza Vieira**
- Turma: **Sistemas de Informação — UDF**
- Data de realização: **16/10/2026**
- Integrantes e contribuições (se em equipe): **Trabalho individual. Na seção 5 uso como exemplo o projeto da Unidade III, que desenvolvo em dupla com Ramon Guilherme Marques do Nascimento; as respostas desta atividade são minhas.**

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

1. Como um modelo aprende com dados? **Penso nisso como desenvolvedor: na programação tradicional eu escrevo a função que transforma entrada em saída; no aprendizado de máquina eu entrego pares de entrada e saída já conhecidos e um procedimento que ajusta os parâmetros de uma função genérica até que ela reproduza bem esses pares. "Aprender" é esse ajuste, que mede o erro em cada exemplo e muda os parâmetros na direção que reduz o erro. O que diz se aprendeu, e não só decorou, é o desempenho em exemplos que ficaram guardados fora do ajuste.**
2. Qual diferença entre algoritmo e modelo? **O algoritmo é o procedimento genérico de ajuste (por exemplo, o método que constrói uma árvore de decisão escolhendo a melhor pergunta a cada nó). O modelo é o artefato que esse procedimento produz a partir de um conjunto específico de dados: a árvore concreta, com seus limites numéricos, que pode ser salva em arquivo e chamada por um sistema. Uma analogia da minha área: o algoritmo é o compilador; o modelo é o executável gerado para um programa específico. Mudando os dados de treino, o mesmo algoritmo gera outro modelo.**
3. Compare uma regra de bloqueio de palavra com um modelo de spam. **A regra `if "prêmio" in assunto: bloquear` é determinística: qualquer pessoa consegue ler, testar e explicar por que uma mensagem foi barrada, e a manutenção é trocar a lista de palavras. O problema é que ela não generaliza: "pr3mio" passa, e um e-mail do RH sobre premiação é bloqueado. O modelo de spam é treinado com milhares de mensagens já marcadas e aprende quanto cada sinal (palavras, domínio do remetente, quantidade de links, formatação) pesa para a decisão; ele acerta variações que ninguém listou e pode ser retreinado quando o padrão muda. Em troca, exige rótulos de qualidade, erra de maneiras menos previsíveis, precisa de monitoramento e é mais difícil de justificar para o usuário que teve o e-mail barrado.**
4. Dê um exemplo de atributo e alvo e defina o momento da previsão. **No meu projeto da disciplina, o sistema de livro de ocorrências digital: quando o morador ou a portaria registra uma ocorrência, o sistema já conhece a categoria escolhida, o local, a hora, o dia da semana e quem registrou; esses são os atributos. O alvo é "a ocorrência vai ficar sem resposta registrada", que só se conhece semanas depois. O momento da previsão é o instante em que o registro é salvo, então o modelo não pode usar nada que venha depois (data da resposta, desfecho). No laboratório da Aula 2, a lógica é a mesma: atributos até a semana 4, alvo no fim do semestre, previsão feita na semana 4.**

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Existe uma coluna-resposta preenchida para cada exemplo (uma classe ou um número). | Não existe coluna-resposta; o algoritmo só enxerga os atributos. |
| Pergunta que pode responder | "Dado um caso novo, qual é a resposta mais provável?" | "Que estrutura há nestes dados: grupos parecidos, casos destoantes, dimensões que se repetem?" |
| Tipo de saída | Classe prevista (com uma estimativa de confiança) ou valor numérico. | Rótulo de grupo sem nome prévio, pontuação de anomalia ou representação reduzida. |
| Tarefas e exemplo | Classificação: destacar uma ocorrência como "risco de ficar sem resposta". Regressão: estimar os dias até a resposta. | Agrupamento: semanas com padrão de ocorrências parecido. Detecção de anomalias: uma semana com volume fora do comum em um bloco. |
| Dados necessários | Histórico com atributos **e** resposta registrada de forma consistente; a resposta precisa ter sido conhecida depois dos atributos, não antes. | Atributos comparáveis (mesma escala ou padronizados) e volume suficiente para os grupos se formarem. |
| Forma de avaliação | Métricas contra a resposta real em dados separados: acurácia, matriz de confusão, sensibilidade, MAE, R², sempre comparadas a uma referência trivial. | Não há gabarito: medidas internas de coesão (silhueta) e, principalmente, o julgamento de quem conhece o domínio sobre se os grupos fazem sentido e servem para alguma decisão. |
| Limitação | O modelo herda os erros e vieses dos rótulos; rotular custa tempo; o desempenho cai quando o contexto muda. | O resultado depende das escolhas de atributos, escala e número de grupos; pode "encontrar" grupos que não existem na prática. |

## 3. Situações-problema

| Caso | Situação-problema |
| --- | --- |
| 1 Educação | Prever evadiu/permaneceu com histórico rotulado de turmas anteriores. |
| 2 Saúde | Estimar o tempo de espera em minutos a partir de registros de atendimento. |
| 3 Comércio | Descobrir perfis de compra sem categorias prévias de clientes. |
| 4 Finanças | Prever inadimplente/adimplente com contratos e desfechos conhecidos. |
| 5 Segurança digital | Distinguir spam/legítima com mensagens já revisadas. |
| 6 Comércio | Estimar o total de vendas em reais na próxima semana. |
| 7 Educação | Agrupar perfis de acesso ao ambiente virtual sem rótulo de evasão. |
| 8 Saúde | Classificar exames em categorias previamente definidas por especialistas. |

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| 1 Educação | Alvo: evadiu / permaneceu, registrado nas turmas anteriores | Categoria (binária) | Supervisionado — **classificação**. O desfecho já existe para cada estudante antigo, então o modelo pode aprender a associação entre sinais do início do semestre e o desfecho. Foi o que executei no laboratório (acurácia de teste 0,78 contra 0,59 da referência). | Frequência, notas e entregas até a data da previsão; definição oficial de evasão. Limitação: turmas antigas podem não representar as novas (mudança de currículo, pandemia); o modelo só deve priorizar um convite voluntário, nunca decidir sozinho. |
| 2 Saúde | Alvo: minutos de espera de cada atendimento encerrado | Quantidade | Supervisionado — **regressão**. O alvo é contínuo e fica registrado no sistema quando o paciente é chamado; avaliação por MAE em minutos contra a referência "média do turno". | Hora de chegada, dia, classificação de risco, fila no momento, profissionais escalados. Limitação: a espera depende de decisões da própria unidade (abrir um consultório a mais), e eventos raros (acidente com várias vítimas) não têm histórico suficiente. |
| 4 Finanças | Alvo: inadimplente / adimplente ao fim do contrato | Categoria (binária) | Supervisionado — **classificação**. Contratos encerrados dão o rótulo; a previsão acontece na concessão. | Renda, valor, prazo, histórico de pagamento, idade do cadastro. Limitação: só há desfecho de quem foi aprovado antes, então o histórico é enviesado; variáveis ligadas a CEP ou profissão podem produzir discriminação indireta, e um erro afeta o acesso de uma pessoa ao crédito. |
| 5 Segurança digital | Alvo: spam / legítima, marcado por revisores | Categoria (binária) | Supervisionado — **classificação**. É o exemplo clássico da questão 3: o rótulo existe e o custo de rotular é baixo (o próprio usuário marca). | Texto, cabeçalhos, remetente, links, horário. Limitação: os spammers mudam de estratégia (o padrão aprendido envelhece); a classe spam pode ser muito mais frequente que a legítima em certas caixas, o que exige olhar a matriz e não só a acurácia. |
| 7 Educação | Sem alvo: não há rótulo de evasão | Grupos | Não supervisionado — **agrupamento**. A pergunta não é "quem vai evadir", é "que padrões de uso do AVA existem"; depois, pessoas dão nome aos grupos (por exemplo, "acessa só na véspera da entrega"). | Logs de acesso agregados por estudante e semana: número de acessos, horários, recursos abertos, tempo entre acessos. Limitação: o grupo "acessa pouco" não é necessariamente problema (pode estudar off-line); logs são dados pessoais e precisam de minimização e finalidade declarada. |
| 8 Saúde | Alvo: categoria do exame definida pelos especialistas | Categoria (multiclasse) | Supervisionado — **classificação multiclasse**. As classes já existem e há exames laudados para servir de rótulo. | Exames com laudo confirmado e, de preferência, revisado por mais de um especialista. Limitação: laudos discordantes viram rótulos ruidosos; classes raras têm poucos exemplos; o custo de um falso negativo é alto, por isso o modelo só pode apoiar a triagem, com decisão final humana. |

## 4. Raciocínio crítico

“Detectar fraude” define sozinho o tipo de aprendizado? **Não. "Detectar fraude" é um objetivo de negócio, e o tipo de aprendizado é definido pelos dados que existem para persegui-lo. Se há um histórico de transações investigadas e marcadas (fraude confirmada / legítima), dá para treinar um classificador supervisionado; ele vai bem com os padrões de fraude já vistos, mas tende a não reconhecer um golpe novo e sofre com o desbalanceamento (fraude é rara, então 99% de acurácia pode significar "nunca detecta nada"). Se não há rótulos, ou eles são poucos e atrasados, a saída é não supervisionada: detecção de anomalias ou agrupamento para separar transações atípicas. Isso encontra o inédito, mas "atípico" não é "fraudulento" (uma compra grande em viagem é atípica e legítima), e cada alerta precisa de verificação humana. Do ponto de vista do sistema, as duas abordagens convivem: a anomalia gera um caso para análise; o analista confirma ou descarta; a confirmação vira um rótulo que alimenta o classificador supervisionado. A decisão de bloquear uma pessoa nunca deveria ser automática em nenhum dos dois casos.**

## 5. Conexão com o projeto da disciplina — livro de ocorrências digital

No projeto da Unidade III ([definição do projeto](../../Unidade_3_Gestão_de_Projetos_em_Ciencia_de_Dados/Template-Definicao-Projeto-Ciencia-de-Dados.md)), desenvolvo com Ramon Guilherme Marques do Nascimento um livro de ocorrências digital para um condomínio residencial do DF. A minha parte é o sistema web (registro, status, histórico imutável, perfis morador/portaria/síndico), o painel de indicadores, a importação do histórico transcrito e o piloto com teste de usabilidade (SUS). O documento de definição deixa IA e ML **fora do escopo** e os coloca como trabalho futuro, então o que segue são **propostas** olhando pelo lado do sistema e do painel: onde um modelo entraria na tela e qual decisão ele apoiaria. A transcrição do livro real ainda está pendente; a única base disponível é uma simulação.

| Problema visto pelo sistema / painel | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| **Fila do síndico:** ordenar as ocorrências abertas colocando no topo as que tendem a ficar sem resposta | Alvo: ficou sem resposta registrada (sim/não), conhecido semanas depois | Categoria | Supervisionado — **classificação binária**, com atributos disponíveis no momento do registro (categoria, local, quem registrou, hora, dia). Antes de adotar um modelo, comparar com a regra trivial "taxa histórica da categoria", que o painel já mostra. Experimento na [atividade 07](07-aplicacao-ocorrencias.md). | Histórico transcrito e, depois, os registros do próprio sistema. Limitação: "sem resposta no livro" pode ser "resolvido sem anotar"; na simulação, o modelo quase não supera a regra da categoria. |
| **Aviso de registro repetido:** ao salvar, perguntar "isto é a mesma ocorrência registrada ontem?" | Alvo: par de registros é duplicata (sim/não), marcado na transcrição (16 duplicatas na base simulada) | Categoria | Supervisionado — **classificação de pares**, usando diferença de data, mesmo local, mesma categoria e similaridade do texto. Pode começar como regra fixa (mesma categoria, mesmo local, até 2 dias) e só virar modelo se a regra errar muito. | Pares rotulados como "mesma ocorrência"; poucos exemplos positivos. Limitação: duplicata verdadeira e recorrência legítima (mesmo vazamento voltando) se parecem; o aviso não pode impedir o registro. |
| **Escala da portaria:** quantas ocorrências por semana e categoria esperar no próximo mês | Alvo: contagem semanal por categoria | Quantidade | Supervisionado — **regressão com ordem temporal** (treinar nas semanas antigas, testar nas recentes). Referência obrigatória: média das últimas 4 semanas. Dificilmente um modelo vence essa referência com 24 meses de dados. | Série semanal por categoria, feriados, período de chuvas. Limitação: série curta; mudanças de regra do condomínio (nova norma de silêncio) quebram o padrão. |
| **Alerta de semana atípica no painel:** marcar automaticamente uma semana e um bloco com volume fora do padrão | Sem alvo | Grupos / anomalias | Não supervisionado — **detecção de anomalias** sobre contagens agregadas por semana, bloco e categoria. O alerta leva o síndico a olhar; não conclui nada sozinho. | Contagens agregadas (sem identificar unidades). Limitação: com poucos blocos, "atípico" pode ser um único morador insistente, e o alerta reidentificaria alguém; por isso o painel agrupa categorias com menos de 3 casos por bloco, como já previsto no projeto. |

## Entrega

Salve este arquivo preenchido. Critérios: distinção conceitual, pertinência dos dados, justificativa e clareza. [Voltar ao início](README.md).

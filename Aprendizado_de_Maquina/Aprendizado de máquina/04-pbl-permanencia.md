<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL integrador — Apoio à Permanência

## Identificação

- Estudante ou equipe: **Arthur Rodrigues de Souza Vieira**
- Turma: **Sistemas de Informação — UDF**
- Data de realização: **16/10/2026**
- Integrantes e contribuições (se em equipe): **Trabalho individual: proposta, avaliação e limites escritos por mim, com base na minha execução do laboratório.**

## Contexto

Uma instituição quer compreender sinais associados à evasão e oferecer apoio antes do fim do semestre. Público-alvo: estudantes matriculados e equipe de apoio acadêmico. O cenário é didático e a prática usa dados sintéticos.

**Questão norteadora:** como identificar situações que merecem atenção e oferecer apoio, reconhecendo erros do modelo e dificuldades que os dados não capturam?

## Proposta da equipe

### 1. Delimitação

- Problema e público: **A equipe de apoio só fica sabendo de quem está em dificuldade quando o estudante some ou pede ajuda, geralmente tarde. Público: estudantes matriculados (destinatários do convite) e a equipe de apoio acadêmico (quem usa a lista e faz o contato). Abordo o problema como quem vai construir a tela que a equipe usa: o modelo é uma das fontes dessa tela, não a tela inteira.**
- Decisão que o resultado pode apoiar: **Em que ordem a equipe faz os contatos da semana e que regras de sinalização aparecem na tela como justificativa ("nota parcial baixa e frequência abaixo de 65%"), para que a pessoa que liga saiba sobre o que conversar.**
- Definição de evasão, unidade e horizonte: **Evasão = não concluir o semestre (abandono ou cancelamento sem trancamento formal), conforme a secretaria. Unidade: um estudante em um semestre. Horizonte: lista gerada ao fim da semana 4, com atualização semanal até a semana 8, usando só dados disponíveis em cada data.**

### 2. Perguntas de negócio

1. **Quais combinações de sinais da semana 4 (frequência, nota parcial, entregas) estão associadas à evasão, expressas em regras que a equipe de apoio consiga ler, discutir e contestar?**
2. **Para cada tamanho de lista que a equipe consegue atender, quantos contatos desnecessários (falsos positivos) a lista gera e quantas evasões ficam de fora (falsos negativos)? A equipe aceita essa troca?**

### 3. Dados necessários

| Dado | Papel no projeto | Disponível quando? | Origem pretendida | Necessidade e risco |
| --- | --- | --- | --- | --- |
| Frequência acumulada (%) | Atributo | Toda semana, a partir da 2ª | Diário de classe eletrônico | Necessário; risco de lançamento atrasado pelo professor, que viraria "falta" no modelo. |
| Nota parcial | Atributo | Semana 4 (primeira avaliação) | Sistema acadêmico | Necessário; frequentemente ausente (avaliação não lançada), então a imputação faz parte do método. |
| Entregas de atividades (contagem) | Atributo | Toda semana | AVA | Útil; depende de o professor usar o AVA, o que varia por disciplina. |
| Situação final no semestre | Alvo | Fim do semestre | Secretaria | Necessário para treinar; precisa de definição única (abandono ≠ trancamento). |
| Semestre e curso | Divisão temporal e auditoria (não entram como atributo no primeiro modelo) | Sempre | Secretaria | Necessário para testar em semestre posterior e comparar erro por curso. |
| Chave pseudonimizada | Juntar fontes e gerar a lista | Sempre | Secretaria | Risco alto: é o que permite reidentificar; guardada separada, acesso só da equipe. |
| Dados socioeconômicos e de saúde | **Não entram no modelo** | — | — | Discriminação; só em auditoria agregada, com base legal e comitê de ética. |

Diferencie dados usados na simulação e dados que seriam necessários para uma investigação real: **Na simulação, 600 registros independentes, 3 atributos gerados por uma fórmula, alvo sorteado a partir de uma probabilidade e ausências aleatórias. Em uma investigação real: vários semestres (para treinar no passado e testar no futuro), muitas disciplinas e cursos, a definição oficial de evasão, dados de qualidade desigual (faltas não lançadas, notas atrasadas), grupos para auditoria de equidade, o consentimento ou a base legal para o tratamento (LGPD) e a escuta dos estudantes sobre os motivos reais, que nenhum dos três atributos captura.**

### 4. Abordagem e algoritmo

- Classificação, regressão ou outra formulação, com justificativa: **Classificação binária supervisionada: o alvo é uma categoria registrada no histórico. Também considerei tratar como "ordenação" (ranquear pela estimativa da folha), que é como a lista seria usada; o classificador continua sendo a base, e a ordenação é só a forma de apresentar.**
- Algoritmo introdutório escolhido: **Árvore de decisão com imputação pela mediana no `Pipeline` (`max_depth=5`, `min_samples_leaf=10`), porque as regras podem ser mostradas na tela; no laboratório conferi que uma árvore de 2 níveis (4 regras) perde só 0,04 de validação para a completa, o que permite exibir as regras principais mesmo usando o modelo completo.**
- Referência simples: **`DummyClassifier(strategy='most_frequent')` (sempre "permaneceu"), com acurácia 0,593 e sensibilidade zero no teste.**

### 5. Avaliação

- Preparação, divisão e validação: **Holdout estratificado 75/25 (450/150) com semente 42; imputação aprendida só no treino; profundidade escolhida por validação cruzada estratificada de 5 partes; teste aberto uma vez. Em dados reais: treinar em semestres anteriores e testar no seguinte, e reavaliar a cada semestre.**
- Métricas e razão da escolha: **Sensibilidade da classe "evadiu" (quantas evasões a lista alcança) e precisão (quantos contatos são necessários), lidas na matriz de confusão para cada tamanho de lista; acurácia só como visão geral, porque com classes desbalanceadas ela engana. Comparação obrigatória com a referência.**
- Resultados efetivamente calculados e link da evidência: **Validação 0,7222 ± 0,0391; teste 0,7800 (referência 0,5933). Matriz: TN = 75, FP = 14, FN = 19, TP = 42; sensibilidade 0,689; precisão 0,750. Regras dos dois primeiros níveis (treino): nota ≤ 6,2 e frequência ≤ 64,4% → 95 de 128 evadiram; nota > 6,2 e frequência > 65,5% → 1 de 90. Evidências: [notebook executado](notebooks/laboratorio-equipe.ipynb), [registro do laboratório](03-aula2-laboratorio.md), [matriz](assets/matriz-confusao.png), [árvore](assets/arvore.png).**
- Erros relevantes e consequências: **56 sinalizados no teste de 150: 42 corretos e 14 desnecessários (1 contato em 4 seria "em vão"); 19 evasões (31%) ficariam fora da lista. Se a equipe só conseguir atender, por exemplo, 30 contatos, a ordenação pela estimativa da folha define quem entra primeiro, e a sensibilidade cai; esse número precisa ser medido e mostrado na tela, não escondido.**

### 6. Limites e proteção

- Por que os resultados não demonstram causalidade? **O modelo descreve associações no histórico. Nada foi manipulado: ninguém reduziu a frequência de um grupo para ver se evadia mais. Frequência baixa e evasão podem ser consequências do mesmo motivo (emprego novo, saúde, distância), e quem já decidiu sair naturalmente deixa de ir. Na simulação, a "causa" é literalmente a fórmula que gerou os dados.**
- Por que dados sintéticos não validam uso institucional? **Os dados sintéticos carregam só o que o autor da simulação decidiu: três atributos, uma fórmula, ruído uniforme, ausências aleatórias, nenhum grupo. Eles servem para testar o método (vazamento, validação, leitura da matriz), não para estimar o desempenho em pessoas reais, cujos registros têm atrasos, erros de lançamento e mudanças de contexto que a simulação não contém.**
- Que grupos podem ser mal representados? Como investigar isso com evidências apropriadas? **Estudantes que trabalham (frequência baixa por horário, não por desinteresse), ingressantes por cotas ou com bolsa, pessoas com deficiência, estudantes de cursos pequenos (poucos exemplos) e quem estuda à noite. Investigar com dados reais autorizados: sensibilidade e taxa de falsos positivos por grupo, com tamanho mínimo de amostra por grupo, acompanhamento de comitê de ética e conversa com os próprios estudantes. O conjunto sintético não tem grupos, então nada pode ser afirmado sobre equidade.**
- Como minimizar dados, restringir acesso e definir retenção? **Requisitos que eu escreveria para o sistema: o modelo recebe só os três atributos e a chave pseudonimizada; a tabela que liga chave e matrícula fica em outro serviço, acessível só ao perfil "equipe de apoio"; cada abertura da lista é registrada (quem, quando); professores não têm acesso; a lista e as estimativas são apagadas ao fim do semestre, ficando apenas totais agregados (contatos feitos, aceitos) para reavaliar o modelo; o estudante pode pedir os dados que geraram a sinalização.**
- Como garantir revisão humana e contestação? **Nenhum contato parte do sistema: a lista é uma sugestão de ordem para uma pessoa da equipe, que lê as regras exibidas, decide se faz sentido e registra o que fez. O convite informa que é voluntário e que o estudante pode pedir correção dos dados (faltas lançadas errado são comuns). Uma correção reclassifica o caso na hora. A sinalização nunca entra em histórico escolar, avaliação ou decisão de matrícula.**

### 7. Recomendações de apoio

- Ação voluntária proposta: **Mensagem curta da coordenação oferecendo uma conversa com a equipe de apoio, monitoria e informação sobre auxílios, sem mencionar previsão ou risco; o estudante escolhe se responde. A tela da equipe mostra o motivo da sinalização em linguagem simples para orientar a conversa.**
- Como acolher estudantes não sinalizados pelo modelo: **Divulgação dos mesmos serviços para a turma inteira; botão de "quero conversar" no AVA (autoencaminhamento); professores podem indicar casos manualmente na mesma tela, que trata indicação humana e sinalização do modelo do mesmo jeito.**
- O que precisa ser verificado antes de aplicação real: **Desempenho com dados reais em divisão temporal; auditoria por grupos; capacidade real da equipe (quantos contatos por semana) e a sensibilidade correspondente; parecer ético e jurídico (LGPD); definição oficial de evasão; piloto curto com medição do efeito dos convites (quantos aceitos, o que mudou) antes de expandir.**

Previsões não são certezas. Priorize apoio e revisão humana, sem punições ou decisões automáticas prejudiciais.

## Apresentação de cinco minutos

| Tempo | Conteúdo | Responsável |
| --- | --- | --- |
| 1 minuto | Problema, decisão apoiada e dados | Arthur Rodrigues de Souza Vieira |
| 2 minutos | Método, matriz de confusão e regras da árvore | Arthur Rodrigues de Souza Vieira |
| 1 minuto | Limitações e proteção dos dados | Arthur Rodrigues de Souza Vieira |
| 1 minuto | Recomendações de apoio e o que falta verificar | Arthur Rodrigues de Souza Vieira |

## Contribuições

| Integrante | Contribuição verificável |
| --- | --- |
| Arthur Rodrigues de Souza Vieira | Execução do [notebook](notebooks/laboratorio-equipe.ipynb), seções 1 a 7 desta proposta e os requisitos de sistema das seções 6 e 7 (trabalho individual). |

[Voltar ao início](README.md).

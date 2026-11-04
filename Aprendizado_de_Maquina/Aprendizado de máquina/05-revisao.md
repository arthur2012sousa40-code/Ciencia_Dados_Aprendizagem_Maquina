<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Questões de revisão — Registro individual

## Identificação

- Estudante ou equipe: **Arthur Rodrigues de Souza Vieira**
- Turma: **Sistemas de Informação — UDF**
- Data de realização: **16/10/2026**
- Integrantes e contribuições (se em equipe): **Trabalho individual.**

Responda com suas palavras e apresente os cálculos quando solicitados. Os números dos exercícios manuais não são os resultados do laboratório.

## 1. Explique a diferença entre regra programada para bloquear uma palavra e modelo de spam treinado com exemplos.

**Resposta:** A regra é código que eu escrevo e consigo testar com um caso de teste: "se o assunto contém X, bloquear". Ela é transparente e barata, mas só conhece o que foi escrito nela: uma grafia nova passa, e um e-mail legítimo com a palavra é barrado. O modelo de spam é produzido a partir de mensagens já marcadas como spam ou legítimas; o algoritmo descobre quais combinações de sinais (palavras, remetente, links, formatação) separam as duas classes e devolve uma pontuação. Ele reconhece variações que ninguém listou e pode ser retreinado com mensagens novas, mas depende de rótulos bons, erra de forma menos óbvia e precisa de monitoramento e de um jeito de explicar a decisão ao usuário.

## 2. Por que codificar evadiu/permaneceu como 1/0 não transforma classificação em regressão?

**Resposta:** Porque 1 e 0 são apenas nomes numéricos de duas categorias; não existe "0,5 evadido", e a diferença entre as classes não é uma distância. O que define a tarefa é a natureza do alvo e da pergunta: "a qual classe pertence?" é classificação, avaliada com matriz de confusão, sensibilidade e acurácia. Se eu usasse regressão nesses 0/1, um MAE de 0,3 não teria significado prático. Alguns algoritmos até estimam uma probabilidade internamente, mas a decisão final continua sendo escolher uma classe.

## 3. Uma biblioteca quer estimar empréstimos e descobrir perfis. Que tarefas correspondem a cada pergunta?

**Resposta:** "Quantos empréstimos na próxima semana" tem alvo numérico conhecido no histórico: é **regressão** (supervisionado), avaliada por MAE em empréstimos. "Que perfis de usuário existem" não tem alvo: é **agrupamento** (não supervisionado); o algoritmo junta usuários parecidos e cabe à equipe dar nome e utilidade aos grupos, sempre com dados agregados e sem identificar pessoas.

## 4. O que são atributo, alvo e unidade de análise no laboratório educacional?

**Resposta:** Unidade de análise: um estudante fictício em um semestre (cada linha do CSV). Atributos: as entradas do modelo, conhecidas na semana 4: `frequencia_sem4`, `nota_sem4` e `entregas_sem4`. Alvo: a saída que se quer prever, `evasao_fim_semestre` (0 permaneceu, 1 evadiu), que só existe no fim do semestre. A regra que uso para checar se algo pode ser atributo é "esse valor já existiria no momento em que o sistema faria a previsão?".

## 5. Por que calcular a mediana antes de dividir os dados pode invalidar a avaliação?

**Resposta:** Porque a mediana passaria a conter informação dos registros de teste, e o teste deixaria de ser "dados nunca vistos": é vazamento. Na prática o modelo seria preparado com algo que não existiria quando ele fosse usado em dados novos, e a estimativa de desempenho ficaria otimista. No meu laboratório, a mediana só do treino foi 5,146 e a dos 600 registros, 4,962; neste caso a acurácia de teste não mudou (7 ausentes no teste caíram no mesmo ramo da árvore), mas o erro de método é o mesmo e, com mais ausentes ou com padronização, apareceria. O `Pipeline` resolve isso aprendendo a mediana só no treino e em cada dobra da validação cruzada.

## 6. Em uma matriz didática com TN=80, FP=5, FN=10, TP=5, calcule acurácia e sensibilidade. O resultado é suficiente para aprovar o modelo?

**Resposta:**
- Total = 80 + 5 + 10 + 5 = 100.
- Acurácia = (TN + TP) / total = (80 + 5) / 100 = **0,85**.
- Sensibilidade = TP / (TP + FN) = 5 / (5 + 10) = **0,333**.

Não é suficiente. Há 15 positivos em 100; um modelo que respondesse "negativo" para tudo teria acurácia 85/100 = 0,85, igual à deste, e o modelo encontra só 1 em cada 3 positivos. Para aprovar, eu precisaria saber o custo dos 10 falsos negativos no contexto, comparar com a referência, ver a precisão (5/10 = 0,5: metade dos alertas é falsa) e confirmar que a matriz veio de dados de teste separados.

## 7. Valores reais 100, 120, 140 e previsões 110, 115, 130. Calcule MAE e informe a unidade se o alvo for vendas em reais.

**Resposta:** |100 − 110| = 10; |120 − 115| = 5; |140 − 130| = 10. MAE = (10 + 5 + 10) / 3 = 25 / 3 ≈ **8,33**. Unidade: **reais** (R$ 8,33 de erro médio por previsão). Se o alvo fosse vendas em unidades, o MAE seria em unidades; a métrica herda a unidade do alvo.

## 8. Um R² de -0,2 significa “20% de acertos negativos”? Explique.

**Resposta:** Não. R² = 1 − (soma dos erros quadráticos do modelo ÷ soma dos erros quadráticos de prever sempre a média do conjunto avaliado). R² = −0,2 quer dizer que o erro quadrático do modelo é 20% **maior** do que o de prever a média: o modelo é pior que a referência mais boba. Não há "acertos" em regressão, e R² não é porcentagem de nada. Vi isso na prática na atividade 07: a regressão de dias até a resposta deu R² = −0,97 no teste, e a média (e a mediana por categoria) venceu o modelo.

## 9. Uma árvore tem acurácia 1,00 no treino e 0,65 na validação. Que hipótese investigar e como?

**Resposta:** Sobreajuste: a árvore cresceu até isolar cada registro do treino (folhas de 1 elemento) e decorou o ruído. Investigo com validação cruzada no treino: limito `max_depth`, aumento `min_samples_leaf` ou aplico poda (`ccp_alpha`) e observo se a distância treino–validação diminui e se a validação sobe. No laboratório, a configuração mais livre (folha 5, sem limite) tinha 0,868 no treino e 0,713 na validação; folha 40 caiu para 0,776 no treino e subiu para 0,729 na validação. Também conferiria se há vazamento (um atributo que "revela" o alvo) e se o teste está realmente separado.

## 10. Por que escolher a profundidade pelo teste prejudica a estimativa final?

**Resposta:** Porque o teste vira parte do processo de ajuste: ao escolher a configuração que vai melhor no teste, eu me aproveito das particularidades daquele conjunto, e a acurácia reportada fica otimista, ou seja, deixa de estimar o que acontecerá com dados novos. O teste precisa ser usado uma vez, no fim. Se eu quiser comparar configurações, uso validação dentro do treino; se já abri o teste e quero reescolher, preciso de um novo teste independente. Foi por isso que, no laboratório, mantive o modelo do roteiro mesmo quando a grade sugeriu folha 40 com uma média um pouco maior.

## 11. Baixa frequência associada à evasão demonstra causa? Proponha explicação alternativa.

**Resposta:** Não. O histórico mostra que as duas coisas andam juntas, não que uma produz a outra. Explicação alternativa: um emprego novo com horário conflitante faz o estudante faltar **e** abandonar, sem que a falta cause o abandono; forçar presença não resolveria o motivo. Outra: causalidade reversa, quem já decidiu sair deixa de frequentar, então a frequência baixa é consequência da decisão. Na simulação do laboratório, a "causa" é a fórmula que gerou os dados.

## 12. Um modelo sinaliza um estudante como possível evasão. Que ação responsável pode ser adotada?

**Resposta:** Uma pessoa da equipe de apoio revisa o caso (inclusive conferindo se os dados estão certos) e, se fizer sentido, envia um convite voluntário para conversar, com oferta de monitoria, orientação e informação sobre auxílios, sem usar palavras como "risco" ou "evasão" com o estudante. Nenhuma consequência acadêmica decorre da sinalização; o estudante pode recusar, pedir explicação e corrigir dados; o acesso à lista é restrito e registrado, e a lista é descartada no fim do semestre. Do lado do sistema, isso vira requisito: a sinalização nunca aciona nada automaticamente, só aparece para uma pessoa.

## Fontes adicionais consultadas

- Material da disciplina (Módulo IV) e o [notebook didático](notebooks/laboratorio.ipynb).
- SCIKIT-LEARN. *User Guide*; *Common pitfalls and recommended practices*. Disponível em: https://scikit-learn.org/stable/. Acesso em: 16 out. 2026.
- Definição do projeto da disciplina (livro de ocorrências digital), para os exemplos das questões 5, 8 e 12: [documento](../../Unidade_3_Gestão_de_Projetos_em_Ciencia_de_Dados/Template-Definicao-Projeto-Ciencia-de-Dados.md).
- Ferramentas utilizadas: Python 3.13, Jupyter, scikit-learn, pandas, NumPy e matplotlib.
- Uso de ferramentas de IA: **PREENCHER pelo estudante**.

[Voltar ao início](README.md).

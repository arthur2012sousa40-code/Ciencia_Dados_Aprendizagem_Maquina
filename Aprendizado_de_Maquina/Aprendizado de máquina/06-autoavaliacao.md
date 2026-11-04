<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Autoavaliação e conferência da entrega

## Identificação

- Estudante ou equipe: **Arthur Rodrigues de Souza Vieira**
- Turma: **Sistemas de Informação — UDF**
- Data de realização: **16/10/2026**
- Integrantes e contribuições (se em equipe): **Trabalho individual: todas as atividades do módulo foram feitas por mim.**

## Checklist

- [x] Diferenciei IA, Ciência de Dados e ML com um exemplo.
- [x] Completei o quadro supervisionado/não supervisionado.
- [x] Justifiquei pelo menos cinco situações-problema.
- [x] Registrei a investigação da biblioteca.
- [x] Identifiquei atributos, alvo, unidade e momento da previsão.
- [x] Executei e documentei a prática em Python ou Orange.
- [x] Escolhi configurações usando treino/validação.
- [x] Mantive o teste fora do ajuste e da seleção.
- [x] Interpretei acurácia, matriz, MAE e R².
- [x] Comparei com uma referência e discuti erros.
- [x] Registrei limitações, dados sintéticos, privacidade e vieses.
- [x] Formulei recomendações de apoio com revisão humana.
- [x] Respondi às questões individuais.
- [x] Conferi os links e os arquivos de evidências.
- [ ] Substituí os campos PREENCHER ou justifiquei os não aplicáveis. *(Pendente: a declaração sobre uso de ferramentas de IA, neste arquivo e na [revisão](05-revisao.md), está marcada como "PREENCHER pelo estudante". Os campos que dependem da apresentação em sala estão como "A registrar após a apresentação".)*

## Reflexão individual

- O que aprendi e consigo explicar: **A separar três coisas que eu misturava: o algoritmo, o modelo que ele gera e o sistema que usa o modelo. Consigo explicar por que a preparação dos dados tem de ficar dentro do `Pipeline` (vazamento), por que a acurácia engana quando uma classe domina (vi isso duas vezes: 59% de permanência no laboratório e 70% de "sem resposta" na base simulada do projeto), como ler a matriz de confusão como uma decisão de negócio (quantos contatos em vão, quantos casos perdidos) e por que R² não é taxa de acerto, inclusive quando é negativo.**
- Qual foi minha principal dificuldade: **Aceitar que configurações com médias diferentes na validação eram, na verdade, indistinguíveis dentro do desvio entre dobras, e resistir à tentação de trocar o modelo depois de ver o teste. A segunda dificuldade foi a regressão da atividade 07: demorei a entender que um modelo pode ser pior do que prever a média quando há poucos dados e muitas colunas.**
- Qual evidência mostra meu avanço: **O [notebook executado](notebooks/laboratorio-equipe.ipynb), com os seis exercícios resolvidos em código e os três experimentos próprios (imputação e vazamento, poda, quantidade de regras); a conferência manual da matriz no [registro do laboratório](03-aula2-laboratorio.md) (117/150 = 0,78; 42/61 = 0,689); e a [atividade 07](07-aplicacao-ocorrencias.md), em que apliquei o mesmo roteiro ao meu projeto e concluí, com números, que uma regra de painel quase empata com a árvore.**
- Como contribuímos com a equipe: **Trabalho individual. A ligação com a equipe aparece no projeto da Unidade III, feito em dupla com Ramon Guilherme Marques do Nascimento: a atividade 07 usa a base simulada que ele gerou no notebook CRISP-DM e olha o problema pelo lado que me cabe, o sistema e o painel.**
- O que preciso revisar: **Métricas para classes desbalanceadas além da sensibilidade (precisão, F1, curva de precisão × cobertura e escolha de limiar); regressão com atributos categóricos em amostras pequenas (regularização); e avaliação com divisão temporal, que é a que vale para o painel do projeto.**
- Ferramentas de apoio utilizadas, incluindo IA quando houver, e como verifiquei as respostas: **Python 3.13.18 com Jupyter/nbconvert, scikit-learn 1.9.1, pandas 3.0.5, NumPy 2.5.3 e matplotlib 3.11.2; Git e GitHub para o repositório. Verifiquei as respostas executando os notebooks do início ao fim com a semente 42, comparando os números dos relatórios com os arquivos `resultados_*.json` e refazendo os cálculos da matriz e do MAE à mão. Uso de ferramentas de IA: PREENCHER pelo estudante.**

## Critérios de avaliação

Escala sugerida do material: nível 3 consistente, 2 adequado com lacunas, 1 parcial, 0 ausente/incoerente. Nota do critério = peso × nível/3. A professora pode ajustar a aplicação.

| Critério | Peso aula 1 | Peso aula 2/PBL |
| --- | --- | --- |
| Problema e conceitos | 3,0 | 2,0 |
| Dados e justificativa | 2,0 | 2,0 |
| Método e avaliação | 1,0 | 3,0 |
| Interpretação e responsabilidade | 2,0 | 2,0 |
| Clareza e colaboração | 2,0 | 1,0 |
| Total | 10,0 | 10,0 |

Na aula 1, método corresponde à avaliação proposta. Na aula 2, inclui execução e interpretação. A maior acurácia isolada não assegura a melhor avaliação da atividade.

## Fontes de apoio

- SCIKIT-LEARN. *User Guide*. https://scikit-learn.org/stable/user_guide.html.
- SCIKIT-LEARN. *Common pitfalls and recommended practices*. https://scikit-learn.org/stable/common_pitfalls.html.
- ORANGE DATA MINING. *Test and Score*. https://orangedatamining.com/widget-catalog/evaluate/testandscore/.

Referências indicadas no material didático do módulo, consultadas em 14 out. 2026. Registre a data da sua própria consulta quando utilizar novas fontes. Minha consulta: 16 out. 2026.

[Voltar ao início](README.md).

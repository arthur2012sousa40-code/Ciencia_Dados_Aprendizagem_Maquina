<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Módulo IV — Exercícios realizados

Esta pasta guarda as atividades do Módulo IV (introdução ao Machine Learning e aprendizado supervisionado). Cada arquivo mantém o enunciado da professora e, nos espaços indicados, as minhas respostas. Todos os números citados nos relatórios saíram dos notebooks executados que estão em `notebooks/`.

## Identificação do repositório

- Estudante: **Arthur Rodrigues de Souza Vieira** (trabalho individual)
- Turma: **Sistemas de Informação — UDF**
- Repositório: **[arthur2012sousa40-code/Ciencia_Dados_Aprendizagem_Maquina](https://github.com/arthur2012sousa40-code/Ciencia_Dados_Aprendizagem_Maquina)** — conteúdo na pasta `Aprendizado_de_Maquina/Aprendizado de máquina/`
- Projeto da disciplina usado como contexto nas atividades 01 e 07: *Livro de ocorrências digital para condomínios residenciais do DF*, em dupla com Ramon Guilherme Marques do Nascimento. Minha parte no projeto é o sistema web e o painel de indicadores ([definição do projeto](../../Unidade_3_Gestão_de_Projetos_em_Ciencia_de_Dados/Template-Definicao-Projeto-Ciencia-de-Dados.md); [parte prática do projeto, CRISP-DM](../../Projeto_DataScience/)).

## Atividades

| Arquivo | Entregável |
| --- | --- |
| [01-aula1-conceitos.md](01-aula1-conceitos.md) | Quadro comparativo e classificação justificada de pelo menos cinco problemas |
| [02-pbl-biblioteca.md](02-pbl-biblioteca.md) | Canvas da investigação |
| [03-aula2-laboratorio.md](03-aula2-laboratorio.md) | Registro do modelo, métricas, erros e experimentos em Python |
| [04-pbl-permanencia.md](04-pbl-permanencia.md) | Proposta de apoio educacional, com avaliação e limites |
| [05-revisao.md](05-revisao.md) | Respostas individuais às questões de revisão |
| [06-autoavaliacao.md](06-autoavaliacao.md) | Checklist, contribuições e reflexão final |
| [07-aplicacao-ocorrencias.md](07-aplicacao-ocorrencias.md) | Aplicação ao projeto do livro de ocorrências: o que o painel do síndico deveria destacar como risco de ficar sem resposta, e se dá para estimar os dias até a resposta |

## Arquivos de apoio

| Arquivo | O que é | Colab |
| --- | --- | --- |
| [notebooks/laboratorio.ipynb](notebooks/laboratorio.ipynb) | Notebook didático da professora, sem alterações | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arthur2012sousa40-code/Ciencia_Dados_Aprendizagem_Maquina/blob/main/Aprendizado_de_Maquina/Aprendizado%20de%20m%C3%A1quina/notebooks/laboratorio.ipynb) |
| [notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb) | Minha execução do laboratório, com interpretações, os seis exercícios de investigação em código e três experimentos próprios | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arthur2012sousa40-code/Ciencia_Dados_Aprendizagem_Maquina/blob/main/Aprendizado_de_Maquina/Aprendizado%20de%20m%C3%A1quina/notebooks/laboratorio-equipe.ipynb) |
| [notebooks/ocorrencias-painel-sem-resposta.ipynb](notebooks/ocorrencias-painel-sem-resposta.ipynb) | Experimento da atividade 07 sobre a transcrição **simulada** do livro de ocorrências | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arthur2012sousa40-code/Ciencia_Dados_Aprendizagem_Maquina/blob/main/Aprendizado_de_Maquina/Aprendizado%20de%20m%C3%A1quina/notebooks/ocorrencias-painel-sem-resposta.ipynb) |

- [dados/educacionais-sinteticos.csv](dados/educacionais-sinteticos.csv): os 600 registros fictícios da prática de classificação (material da disciplina).
- [dados/livro_ocorrencias_transcrito.csv](dados/livro_ocorrencias_transcrito.csv): cópia da transcrição **simulada** do livro de ocorrências, gerada pelo notebook CRISP-DM do projeto (a original fica em `Projeto_DataScience/dados/`). Não descreve nenhum condomínio real.
- [notebooks/resultados_execucao.json](notebooks/resultados_execucao.json) e [notebooks/resultados_ocorrencias.json](notebooks/resultados_ocorrencias.json): números gravados pelas execuções, usados nos relatórios.
- `assets/`: logomarca e figuras geradas pelos notebooks (`matriz-confusao.png`, `arvore.png`, `regressao-observado-previsto.png`, `regressao-residuos.png` e as `ocorrencias-*.png` da atividade 07).

**Todos os registros são sintéticos ou simulados.** Não representam estudantes da UDF nem moradores ou ocorrências de condomínios reais.

## Como colocar no GitHub

1. Esta pasta fica em `Aprendizado_de_Maquina/Aprendizado de máquina/` do repositório, com o `README.md` na raiz dela.
2. Para enviar pelo site: **Add file > Upload files**, incluindo as subpastas `assets/`, `dados/` e `notebooks/`. Registre um commit descrevendo a atividade.
3. Para reproduzir os notebooks: no Colab, clique em **Abrir no Colab** e use **Ambiente de execução > Executar tudo** (as figuras vão para `./assets/` e os CSVs são baixados do GitHub). Localmente, instale `numpy pandas matplotlib scikit-learn jupyter` e, de dentro de `notebooks/`, rode `jupyter nbconvert --to notebook --execute --inplace <notebook>.ipynb`; as figuras vão para `../assets/`.
4. Semente 42 em todos os notebooks. Com as versões registradas (Python 3.13.18, scikit-learn 1.9.1, pandas 3.0.5, NumPy 2.5.3, matplotlib 3.11.2), os números são os mesmos dos relatórios.
5. Confira se os links relativos abrem no GitHub antes de enviar o endereço no ambiente indicado pela professora.

## Convenções de registro

- Mantive os enunciados e escrevi as respostas em negrito ou nas tabelas.
- Separo **resultado calculado**, **interpretação** e **hipótese**.
- Os valores vêm das execuções salvas nos notebooks: versões, semente, divisão dos dados e configurações estão registradas em cada relatório.
- Não há matrículas, telefones, credenciais nem dados pessoais reais.
- Fontes adicionais estão citadas em cada atividade. A declaração sobre uso de ferramentas de IA está marcada como **PREENCHER pelo estudante** nas atividades 05 e 06.

## Situação das entregas

- [x] Aula 1: quadro comparativo e problemas justificados.
- [x] PBL Biblioteca em Foco.
- [x] Aula 2: notebook e relatório.
- [x] PBL Apoio à Permanência.
- [x] Revisão e autoavaliação.
- [x] Aplicação ao projeto da disciplina (livro de ocorrências digital).

## Fonte da atividade

Material do estudante do Módulo IV — Aprendizado de Máquina. Profa. Kadidja Valéria, UDF, 2026. Consulte as referências do material e a documentação oficial indicada nas atividades.

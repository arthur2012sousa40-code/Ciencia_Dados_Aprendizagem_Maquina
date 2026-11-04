<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL — Biblioteca em Foco

## Identificação

- Estudante ou equipe: **Arthur Rodrigues de Souza Vieira**
- Turma: **Sistemas de Informação — UDF**
- Data de realização: **16/10/2026**
- Integrantes e contribuições (se em equipe): **Trabalho individual: delimitação, canvas e conclusão feitos por mim.**

## Situação-problema

Uma biblioteca universitária enfrenta filas em horários específicos e baixa utilização de alguns serviços. A coordenação deseja melhorar o atendimento e planejar recursos. Este é um cenário didático.

**Público-alvo:** estudantes usuários, equipe de atendimento e gestão.

**Questão norteadora:** como os dados podem orientar o planejamento da biblioteca e a oferta de serviços sem identificar ou discriminar seus usuários?

## Investigação em equipe

1. Delimitem o problema e a decisão a apoiar.
2. Registrem o que já sabem e o que precisam investigar.
3. Formulem duas perguntas de negócio.
4. Definam a unidade de análise, os atributos e o alvo, quando houver.
5. Justifiquem a abordagem e indiquem se uma análise descritiva já seria suficiente.
6. Proponham avaliação, cuidados com os dados e limitações.

## Canvas da equipe

| Campo | Registro |
| --- | --- |
| Problema e decisão | Dois sintomas que podem ter a mesma causa: fila no balcão em certos horários e serviços pouco usados (salas de estudo em grupo, cabines, equipamentos). Minha hipótese de partida, como quem desenvolve sistemas, é que parte da baixa utilização vem de **reservas feitas e não usadas** (no-show), que bloqueiam o recurso e ainda geram ida ao balcão para "ver se liberou". Decisões: (a) quantos atendentes escalar por faixa horária; (b) se vale adotar confirmação de reserva e liberação automática do recurso não ocupado. |
| Público-alvo | Estudantes (menos fila e recurso disponível de verdade), equipe de atendimento (escala previsível) e gestão (usar o que já existe antes de comprar mais). |
| O que sabemos | A fila acontece em horários específicos; alguns serviços têm pouca procura; o sistema de reservas e o de empréstimo registram data e hora de cada operação; não existe hoje medição da fila em si (ninguém anota quem esperou ou desistiu). |
| O que precisamos investigar | Em que faixas de hora e dia a fila se forma e se ela coincide com devoluções, início de aula ou provas; que proporção das reservas de sala/cabine é efetivamente usada; se os serviços pouco usados são desconhecidos ou só inconvenientes (horário, burocracia); quanto tempo o balcão gasta por tipo de atendimento. |
| Pergunta de negócio 1 | Quantos atendimentos o balcão deve esperar em cada faixa de 30 minutos, por dia da semana e por período do calendário (aulas, provas, férias), nas próximas duas semanas? |
| Pergunta de negócio 2 | Dada uma reserva de sala de estudo ou cabine, qual é a chance de ela não ser usada? Em quais condições (antecedência, horário, histórico agregado da faixa) o no-show é mais comum, para decidir a regra de confirmação? |
| Unidade de análise e período | P1: uma faixa de 30 minutos em um dia (ex.: terça, 12h00–12h30), nos últimos dois semestres. P2: uma reserva de recurso, no mesmo período. |
| Atributos, unidades e origem pretendida | P1: dia da semana, faixa horária, semana do calendário acadêmico, devoluções previstas para o dia (sistema de empréstimo), aulas que terminam na faixa (grade de horários), atendentes escalados. P2: antecedência da reserva (horas), faixa horária, dia, duração pedida, tipo de recurso, taxa de ocupação agregada da faixa; **nenhum dado da pessoa** que reservou. Origem: sistema de reservas, sistema de empréstimo, grade de horários. Para medir a fila, proponho um **totem de senha** simples no balcão, que registra chegada e chamada sem identificar o usuário. |
| Alvo e momento em que será conhecido, ou ausência de alvo | P1: alvo numérico = atendimentos na faixa (conhecido ao fim da faixa, pelas senhas chamadas); previsão feita na semana anterior. P2: alvo binário = reserva usada / não usada (conhecido 15 minutos após o início da reserva, pelo check-in no totem ou na catraca da sala). |
| Abordagem e justificativa | P1: **regressão** com ordem temporal; mas, antes, uma tabela dia × faixa com a média e o percentil 90 de atendimentos por período do calendário. Minha aposta é que essa tabela resolve a escala e que um modelo só se justifica se reduzir o MAE em relação à "média da mesma faixa nas últimas 4 semanas". P2: **classificação** supervisionada; o rótulo nasce sozinho no sistema (check-in ou ausência). Aqui a descritiva é o primeiro passo (taxa de no-show por antecedência e por horário) e provavelmente já indica a regra de confirmação; o classificador entra se a taxa variar muito entre combinações que uma tabela não capta. |
| Alternativa sem ML | Painel com mapa de calor dia × faixa de senhas chamadas e tempo médio de espera; taxa de no-show por antecedência; política de confirmação da reserva 1 hora antes, com liberação automática; pesquisa de dois cliques no totem ("conhecia este serviço?") para separar desconhecimento de desinteresse. |
| Como avaliar a proposta | P1: MAE em atendimentos por faixa nas semanas futuras reservadas (divisão temporal), contra a referência das últimas 4 semanas; resultado de negócio = tempo de espera medido pelo totem antes e depois da nova escala. P2: sensibilidade e precisão da classe "não usada" em reservas futuras, contra a referência "taxa média de no-show"; resultado de negócio = ocupação real das salas e número de reservas canceladas por confirmação. |
| Privacidade e limitações | Só dados agregados por faixa; a reserva entra no modelo sem matrícula, curso ou nome; a senha do totem não identifica ninguém; retenção dos dados brutos de reserva por um semestre; nenhuma penalidade individual por no-show calculada pelo modelo (a política de confirmação vale para todos). Limitações: a fila só passa a ser medida depois do totem, então o histórico é curto; semestre atípico (greve, obra) distorce; estudantes que nunca reservam porque o sistema é ruim não aparecem nos dados (viés de sobrevivência). |

## Registro de colaboração

| Integrante | Papel | Contribuição |
| --- | --- | --- |
| Arthur Rodrigues de Souza Vieira | Analista e relator (atividade individual) | Delimitação do problema, hipótese do no-show, definição de unidades, atributos e alvos, proposta de medição com totem de senha, avaliação, privacidade e conclusão. |

## Conclusão da equipe

**Proposta:** Primeiro medir: instalar o totem de senha e passar a registrar check-in das reservas, porque hoje a fila e o no-show não existem como dado. Em paralelo, montar o painel descritivo (mapa de calor dia × faixa; taxa de no-show por antecedência) e ajustar a escala e a regra de confirmação a partir dele. Só depois testar a regressão de atendimentos por faixa e o classificador de no-show, adotando cada um apenas se vencer a referência simples em semanas futuras.

**Dúvida ainda aberta:** Se a confirmação obrigatória reduzir o no-show, ela também pode reduzir reservas legítimas de quem esquece de confirmar; como medir esse efeito colateral sem identificar quem deixou de reservar?

**Feedback recebido e melhoria realizada:** A registrar após a apresentação.

## Entrega

Canvas preenchido e síntese para apresentação de dois minutos. Avaliar coerência da pergunta, dados, abordagem, responsabilidade e colaboração. [Voltar ao início](README.md).

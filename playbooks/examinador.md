# playbooks/examinador.md - Examinador socrático

Modo despachável de estudo activo. Não é uma camada permanente nem um sub-agente persistente - é um modo que o aluno invoca quando quer treinar uma matéria, diagnosticar buracos, ou simular exame. Corre em ciclos curtos, não em maratonas. Tudo o que produz ancora-se ao que a wiki já tem verificado: o Examinador não introduz Direito novo não confirmado - testa e revela, não inventa.

Serve o aluno: treino e revisão activa, geração de hipóteses no padrão real das provas, e diagnóstico de cobertura que liga o estudo ao calendário de avaliação.

---

## Quatro modos

### 1. Treino socrático
O agente escolhe (ou o aluno indica) um instituto ou matéria e conduz por perguntas, não por exposição. Pergunta → o aluno responde → o agente confronta a resposta com as notas de instituto (Bloco I/II/III), aponta o que falta ou está impreciso, e aprofunda. Ciclo de 3 a 5 perguntas por sessão. O valor está na recuperação activa: o aluno produz a resposta; o agente corrige contra a wiki.

Output secundário: lista de pontos onde a wiki está oca face à pergunta - alimenta a fila de ingestão.

### 2. Modo exame
O aluno escolhe a faculdade e a cadeira (a vista em `wiki/Faculdades/<Faculdade>.md`); o agente gera 5 a 10 hipóteses representativas do padrão de avaliação dessa cadeira nessa faculdade. O padrão ancora-se, em primeiro lugar, nas **fontes de avaliação reais** dessa cadeira e docente já ingeridas (`wiki/Avaliação/`) - exames e casos práticos anteriores -, e, na sua falta, no «Histórico de avaliações» descritivo da vista. Conduz a resolução com o aluno e devolve um relatório de cobertura: que tópicos do programa saíram bem, quais expuseram lacunas. Usa `modelo-caso-pratico.md` para as hipóteses, ligando cada uma ao enunciado real de origem quando exista. O corpo de conhecimento é o mesmo para todas as faculdades; o que muda com a faculdade é o recorte - o programa e o padrão de avaliação dessa vista. Resolver provas reais já ingeridas, não só hipóteses geradas, é parte central do treino. Quando a vista regista o **padrão de ensino do docente** (a leitura que perfilha, de fonte verificada), o agente gera e corrige também por esse critério, nos limites da regra de padrão de ensino abaixo. E o recorte ordena sem amputar: a resposta-modelo constrói-se primeiro pelo padrão do docente da vista; as posições de outras escolas convocam-se como contraste marcado («diferentemente, na doutrina de {escola}…») - em exame, a divergência bem atribuída soma, e o corpo multi-faculdade existe para isso.

### 3. Diagnóstico de cobertura
Sem treino - só mapeamento. O agente cruza o **programa** de uma cadeira de uma faculdade (na sua vista, `wiki/Faculdades/<Faculdade>.md`) com o que a wiki cobre, e produz a lista de lacunas, ordenada por: peso no programa × proximidade da avaliação. Output: entradas na lista de lacunas do `index.md` e proposta de fila de ingestão. É o modo que liga o calendário de cada vista à construção da wiki.

### 4. Exposição invertida
Os papéis trocam-se: o aluno expõe o instituto ou a matéria como se a ensinasse; o agente faz de interlocutor que sonda - pede o porquê de cada regra, o problema que resolve, o que se seguiria se fosse de outro modo - e confronta a exposição com as notas verificadas, apontando o salto, a imprecisão, o buraco. Quem não consegue expor simples ainda não reconstruiu o ponto: é a forma exigente da recuperação activa e o teste natural do raciocínio de primeiros princípios. Ciclos curtos, como nos demais modos.

Output secundário: os pontos onde a exposição falhou ou a wiki está oca - alimentam a revisão e a fila de ingestão.

---

## Regras

- **Ancoragem.** Cada pergunta e cada correcção assentam nas notas verificadas. Onde a wiki não cobre, o Examinador diz «a wiki não cobre isto» - não improvisa a resposta de memória.
- **Hipóteses realistas, não fabricação de fontes.** As hipóteses de exame são factos inventados para subsumir (legítimo - é o género), mas o Direito que se lhes aplica é o verificado na wiki. Não se inventam acórdãos nem posições doutrinárias para enriquecer a hipótese.
- **Sem maratonas.** Ciclos curtos. A fadiga degrada a recuperação activa.
- **Cobertura honesta.** O relatório distingue «coberto e testado com êxito» de «coberto mas frágil» de «não coberto». Não inflaciona a cobertura.
- **Discordância construtiva.** Quando a resposta parte de um pressuposto errado, o Examinador qualifica o erro (que norma, que pressuposto, que consequência), não diagnostica o aluno.
- **Respeita a supressão.** Antes de propor tópicos a treinar, o Examinador consulta `wiki/SUPRESSAO-LIST.md` e não levanta o que o aluno marcou com ❌ como dominado ou irrelevante. Quando apresenta vários tópicos de uma vez, segue o formato item-a-item (`playbooks/formato-apresentacao.md`), para o aluno marcar ✅/⏸/❌ em cada um.
- **Padrão de ensino do docente, sob a regra-âncora - só na medida em que não gere confusão nem erro.** Quando a vista regista a leitura que o docente perfilha (posições que adopta ou rejeita, ênfases) e essa leitura assenta em fonte verificada - obra do docente ou apontamento de aula fiel -, o Examinador usa-a como critério ao gerar e ao corrigir: gera no enquadramento do docente, corrige pela leitura dele. Três limites, intransponíveis, que são a condição de a usar: (1) **só de fonte efectivamente lida** - a posição do docente nunca se infere de «o que ele provavelmente defende»; sem registo verificado na vista, o Examinador não a fabrica e atém-se ao padrão de avaliação e ao corpo de conhecimento geral; (2) **sempre marcada como dele** - apresenta-se como «segundo a leitura do Prof. X», nunca como o Direito firmado nem como a posição dominante; (3) **a divergência não se apaga** - onde a leitura do docente diverge do entendimento dominante, o Examinador assinala ambas (para o exame conta a do docente; a doutrina maioritária diz outra coisa), em vez de fazer passar a leitura do docente por Direito assente. A leitura do docente molda o recorte do exame; não reescreve as páginas de instituto, que continuam a guardar a construção dogmática geral, com a voz do docente marcada como uma entre outras. Em caso de dúvida sobre se uma posição é mesmo do docente ou inferência, trata-se como inferência - e não entra.

## Invocação
- «examinador treino {instituto}» - modo 1.
- «examinador exame {faculdade} {cadeira}» - modo 2.
- «examinador cobertura {faculdade} {cadeira}» - modo 3.
- «examinador exposição {instituto ou matéria}» - modo 4.

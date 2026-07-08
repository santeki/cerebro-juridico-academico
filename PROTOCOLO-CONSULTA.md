# PROTOCOLO-CONSULTA.md

Como o agente responde a uma pergunta a partir da wiki. A resposta nasce das páginas, não da memória do modelo; e as boas respostas voltam à wiki.

---

## Calibração ao tipo de pergunta

A forma da resposta varia com o registo (regra de `CLAUDE.md`):

- **Exame ou dissertação** — estrutura completa: qualificar o problema, jurisdição e ramo; norma aplicável com referência completa e versão vigente; doutrina relevante (autor, obra, edição/ano) só quando ilumina; jurisprudência (tribunal, data, processo, ECLI) só quando decide o ponto; divergências doutrinárias vivas; síntese com nuance e ressalvas.
- **Consulta prática** — orientação operativa: qualificação rápida, prazos, ónus, armadilhas, próximos passos.
- **Dúvida pontual de estudo** — resposta curta e densa, com remissão para o ponto exacto na wiki.
- **Exploratória ou brainstorm** — abrir o mapa, mostrar caminhos alternativos com os custos respectivos.

Se a pergunta for ambígua quanto ao registo, perguntar antes de responder.

## Passos

1. **Ler o índice.** Abrir `wiki/index.md` e localizar as páginas relevantes. Para wiki grande, usar pesquisa sobre os ficheiros markdown. À escala — quando `index.md` ultrapassa o seu orçamento (`CONVENCOES.md`) — começar por `wiki/ESTADO-RESUMO.md`, a fotografia podada do estado, e descer ao índice completo só quando a consulta o exigir.
2. **Abrir as páginas — todas as que o ponto convoca.** Ler as páginas de entidade e as páginas de fonte que as sustentam; não responder só pelo índice. Antes de fechar a resposta, confrontar as páginas convocadas com as que o índice, as vistas e as ligações apontam para o ponto — o instituto canónico, as aplicações de ramo, os debates abertos, a linha jurisprudencial — e usar todas ou declarar na resposta a exclusão e a razão. «Todo o conteúdo» é confronto por listagem, não esperança de recolha.
3. **Verificar o estado.** Se a página relevante tem `estado_verificacao: parcial` ou `em-aberto`, a resposta herda essa incerteza e di-lo na frase. Se um ponto crítico depende de bloco por confirmar, sinalizar e, se possível, verificar contra fonte primária antes de afirmar.
4. **Abrir com o contrato do terreno; sintetizar com proveniência frase-a-frase.** A primeira linha da resposta declara o estatuto do que a sustenta, antes de qualquer substância: em bloco selado, a linha do selo — data, fontes integradas e dispensadas (`PROTOCOLO-AUDITORIA.md`); fora dele, o que falta, dito na abertura («ponto monocamada: só {fonte}; a segunda obra do programa está por ingerir», «página `parcial`: {bloco} por confirmar»), e a procedência quando misto («densificado por fonte local; actualização confirmada no DRE a {data}»). O aluno sabe onde pisa antes de ler o resto; a sinalização junto à afirmação (regra 7) mantém-se para o detalhe. Depois, cada afirmação substantiva liga-se à página (e à fonte) que a sustenta. Quando a wiki não tem o ponto, dizê-lo: a resposta não inventa para preencher. E quando o ponto convoca diploma cuja página tem `legislacao_verificada_em` ausente ou a mais de 90 dias, o Vigia corre antes da resposta — que abre com a data («confirmado no DRE a {data}») ou com a cegueira declarada. No fecho, appenda-se uma linha a `wiki/telemetria.md` — data | consulta | páginas convocadas (`PROTOCOLO-PAINEL.md`, Frente 4).
5. **Convocar as três lentes** consoante a pergunta pede, sem rotulagem visível.
6. **Cálculo explícito** quando houver prazo, juros ou fórmula.
7. **Despachar modos quando a pergunta os convoca.** Pergunta que pede a posição contrária → Advogado do diabo; que toca um diploma cuja actualidade importa → Vigia legislativo; que pede ecos noutros ramos → Mapeador transversal; cujo desfecho depende do sentido de uma norma → Intérprete (`playbooks/modos-analiticos.md`). Pergunta de treino ou de simulação de exame → Examinador (`playbooks/examinador.md`). Os modos correm sobre a wiki, não a substituem.

## Devolver à wiki

Uma comparação pedida, uma análise, uma conexão descoberta, uma estrutura de exame com correcção-modelo — são valiosas e não devem desaparecer no histórico de conversa. Quando a resposta tem valor durável:

1. Filtrar a resposta para a forma de página (remover o que era específico da conversa).
2. Gravá-la em `wiki/` na subpasta certa (`Temas/`, `Debates/`, ou uma página de entidade nova), a partir do template adequado.
3. Actualizar `index.md` e acrescentar entrada `## [AAAA-MM-DD] consulta | <pergunta resumida>` ao `log.md`.

Assim as explorações compõem-se na base de conhecimento, tal como as fontes ingeridas.

## Formatos de saída

A resposta pode tomar formas diferentes consoante a pergunta: página markdown, tabela comparativa, esquema de exame, mapa de instituto, ficha de revisão. Para o aluno, ver os formatos de estudo em `playbooks/aluno.md`.

## O que a consulta nunca faz

- Não afirma redacção de norma, processo, ECLI, data ou página de memória — verifica ou sinaliza.
- Não atribui posição a autor sem patamar N1 ou N2.
- Não fecha taxonomias além do que as fontes fecham.
- Não emite juízo próprio sobre o que a lei deveria ser; reporta iure condendo só com atribuição expressa.

---
tipo: estado-resumo
titulo: "Resumo de estado (fotografia podada do conhecimento)"
estado_verificacao: verificado
ultima_actualizacao: AAAA-MM-DD
---

# Resumo de estado

Fotografia enxuta do que a wiki contém agora, regenerada a cada passagem. Não é o índice nem o painel.

Existe por uma razão de escala. Enquanto a wiki é pequena, o agente lê `index.md` inteiro à entrada de uma consulta sem custo. Quando o índice cresce além do seu orçamento (60 KB — ver `CONVENCOES.md`), lê-lo por inteiro a cada operação fica caro. Este ficheiro é a destilação do estado corrente que o agente passa a ler primeiro: orienta depressa, e só se desce ao índice completo ou às páginas quando a consulta o exige.

A separação espelha a do sistema da Augusta — lá, o estado completo cresce append-only e nenhuma tarefa o lê; o que se lê é um resumo podado regenerado a cada ciclo. Aqui, a fonte de verdade que cresce é o conjunto `index.md` (catálogo) + `log.md` (história) + as próprias páginas; este resumo é a leitura rápida sobre elas.

## Distinção de papéis (para não duplicar)

- **`index.md`** — catálogo completo: uma linha por página, todas as categorias. Fonte de verdade do que existe. Cresce com a wiki.
- **`PAINEL.md`** — orientado à acção: o que rever hoje (revisão espaçada), dúvidas a fechar, fila de ingestão. Diz o que *fazer* agora.
- **Este ficheiro** — orientado à orientação: quanto há, onde está concentrado, o que mudou há pouco. Diz o que *existe* agora, em forma podada. Para acção, remete ao painel; para o catálogo exaustivo, ao índice.

## Estado da wiki (contagens por categoria)

_Vazio no arranque. Regenerado a partir de `index.md`: uma linha por categoria, com a contagem de páginas. Só os números correntes._

| Categoria | Páginas | Nota |
|---|---|---|
<!-- Institutos | N | -->
<!-- Conceitos | N | -->
<!-- Doutrina | N | -->
<!-- Jurisprudência | N | -->
<!-- Legislação | N | (⚠ M com vacatio a vencer) -->
<!-- Temas | N | -->
<!-- Debates (divergências vivas) | N | -->

## Notas-âncora

_As páginas centrais — as mais ligadas, as que servem de porta de entrada a uma cadeira ou instituto. Uma linha cada. Regeneradas pela contagem de backlinks ou por marcação manual._

<!-- - [[Institutos/Boa-fé]] — porta de entrada ao instituto; liga a M aplicações de ramo. -->

## Mudanças recentes (últimos 7 dias)

_Deltas dos últimos sete dias, um por linha, mais recente primeiro. Extraídos de `log.md`. No máximo uma linha por dia e por tipo de operação; descarta-se o que é mais antigo do que sete dias._

<!-- - [AAAA-MM-DD] Ingestão | <fonte> → <páginas tocadas> -->
<!-- - [AAAA-MM-DD] Consulta | <pergunta> devolvida a [[Temas/...]] -->

## Última passagem completa

_AAAA-MM-DD — regeneração total deste resumo._

---

## Regras de regeneração

1. **Fonte.** Lê-se de `index.md` (contagens, notas-âncora) e de `log.md` (deltas recentes). Nunca se modifica nenhum dos dois a partir daqui.
2. **Reescrita, não acumulação.** Este ficheiro é reescrito por inteiro a cada passagem — guarda só o estado corrente, não história. (Comporta-se como um `-RESUMO`; ver sufixos em `CONVENCOES.md`.)
3. **Tecto.** Alvo ≤ 30 KB. Se exceder após as regras acima, aparar primeiro as «Mudanças recentes», do mais antigo para o mais recente, até ficar abaixo do tecto.
4. **Salvaguarda contra fonte corrompida.** Se `index.md` ou `log.md` estiverem truncados ou ilegíveis, **não** reescrever este ficheiro: registar a falha em `log.md` e parar. Um resumo desactualizado é preferível a um resumo construído sobre fonte partida.
5. **Quando regenerar.** No arranque de uma sessão de consulta à escala (índice acima do orçamento), e ao fim de cada ingestão que altere as contagens. Enquanto a wiki for pequena, este ficheiro pode permanecer vazio — o agente lê o índice directamente, e nada se perde.

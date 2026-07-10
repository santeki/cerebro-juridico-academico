---
tipo: estado-resumo
titulo: "Resumo de estado (fotografia podada do conhecimento)"
estado_verificacao: verificado
ultima_actualizacao: 2026-07-10
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

| Categoria | Páginas | Nota |
|---|---|---|
| Vistas de faculdade | 5 | NOVA, FDUP, Católica Porto, Católica Lisboa, FDUL — todas monocamada BM |
| Conceitos | 14 | teoria do Direito (BM caps. I-VI); tudo `verificado` |
| Fontes ingeridas | 6 | 5 fichas institucionais + BM (em ingestão capitular: caps. I-VI de XI) |
| Institutos · Doutrina · Jurisprudência · Legislação · Temas · Debates · Avaliação | 0 | por abrir |

## Notas-âncora

- [[Fontes/Baptista Machado, Introdução ao Direito e ao Discurso Legitimador]] — reservatório em construção; `progresso:` diz onde a leitura vai (segue cap. VII).
- [[Conceitos/Tutela do Direito]] — porta de entrada da matéria da tutela; ligada por 5 conceitos e 5 vistas.
- [[Conceitos/Noção de Direito]] e [[Conceitos/Coercibilidade]] — o par que estrutura o arco caps. II-VI (sentido/coacção; auto-referência; positivação).
- [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] — o par do cap. VI (produção do Direito; dinâmica temporal e hierárquica da norma posta).

## Mudanças recentes (últimos 7 dias)

- [2026-07-10] ingestão | BM cap. VI (fontes e vigência) → [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] criadas; integrações em 4 conceitos + errata na Tutela; 5 vistas actualizadas (FDUP 18/28, NOVA 7/21, C.Porto I-V, C.Lisboa 6/15, FDUL 11/19); errata MD 33 entradas; erratas da edição arts. 5º/2 e 7º/4 CC (DRE) e art. 1º CPC (dúvida do cap. V fechada); hipótese CN circunscrita (BFD LI, 1975).
- [2026-07-10] ingestão | BM cap. V (tutela) → [[Conceitos/Tutela do Direito]] e [[Conceitos/Jurisdição]] criadas; integrações em 4 conceitos; 5 vistas actualizadas (FDUP 15/28, NOVA 5/21, C.Porto I-IV, C.Lisboa 5/15, FDUL 5/19); errata MD 19 entradas; errata da edição «91º→21º» verificada.
- [2026-07-09] ingestão | 5 fichas institucionais (FDUP, C.Porto, C.Lisboa, FDUL, NOVA) → 5 vistas; BM Fase 0 + caps. I-IV → 10 conceitos criados.
- [2026-07-09] Arquitectura | 6.10 (perspectiva curricular) · 6.11 (derivados desactualizados) · 6.12 (voz evolutiva; contrato deste resumo).
- [2026-07-08] Arquitectura | 6.7 (referências nos produtos) · 6.8 (CHANGELOG; git; telemetria; relações tipadas) · 6.9 (sedes; paridade; modos).
- [2026-07-07] Arquitectura | 4.1.2→6.6 (charter consolidada; protocolos; certificação; produção; empacotamento).

## Última passagem completa

2026-07-10 — regeneração total deste resumo (segunda, no fecho do cap. VI do BM).

---

## Regras de regeneração

1. **Fonte.** Lê-se de `index.md` (contagens, notas-âncora) e de `log.md` (deltas recentes). Nunca se modifica nenhum dos dois a partir daqui.
2. **Reescrita, não acumulação.** Este ficheiro é reescrito por inteiro a cada passagem — guarda só o estado corrente, não história. (Comporta-se como um `-RESUMO`; ver sufixos em `CONVENCOES.md`.)
3. **Tecto.** Alvo ≤ 30 KB. Se exceder após as regras acima, aparar primeiro as «Mudanças recentes», do mais antigo para o mais recente, até ficar abaixo do tecto.
4. **Salvaguarda contra fonte corrompida.** Se `index.md` ou `log.md` estiverem truncados ou ilegíveis, **não** reescrever este ficheiro: registar a falha em `log.md` e parar. Um resumo desactualizado é preferível a um resumo construído sobre fonte partida.
5. **Quando regenerar.** No arranque de uma sessão de consulta à escala (índice acima do orçamento), e ao fim de cada ingestão que altere as contagens. Enquanto a wiki for pequena, este ficheiro pode permanecer vazio — o agente lê o índice directamente, e nada se perde.

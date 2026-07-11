---
tipo: estado-resumo
titulo: "Resumo de estado (fotografia podada do conhecimento)"
estado_verificacao: verificado
ultima_actualizacao: 2026-07-11
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
| Conceitos | 16 | teoria do Direito (BM caps. I-VII); tudo `verificado` |
| Fontes ingeridas | 6 | 5 fichas institucionais + BM (em ingestão capitular: caps. I-VII propagados; cap. VIII lido e verificado, propagação a aguardar ok) |
| Institutos · Doutrina · Jurisprudência · Legislação · Temas · Debates · Avaliação | 0 | por abrir |

## Notas-âncora

- [[Fontes/Baptista Machado, Introdução ao Direito e ao Discurso Legitimador]] — reservatório em construção; `progresso:` diz onde a leitura vai (cap. VIII extraído; retoma pela propagação, após ok; segue-se o cap. IX).
- [[Conceitos/Interpretação da Lei]] e [[Conceitos/Integração da Lei]] — o par do cap. VII (hermenêutica e lacunas; arts. 8º-11º e 13º CC na redacção mantida de 1966).
- [[Conceitos/Noção de Direito]] e [[Conceitos/Coercibilidade]] — o par que estrutura o arco caps. II-VII (sentido/coacção; auto-referência; positivação; dialéctica positivo/trans-positivo).
- [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] — o par do cap. VI (produção do Direito; dinâmica temporal e hierárquica da norma posta).
- [[Conceitos/Tutela do Direito]] — porta de entrada da matéria da tutela; ligada por 5 conceitos e 5 vistas.

## Mudanças recentes (últimos 7 dias)

- [2026-07-11] ingestão | BM cap. VIII (aplicação da lei no tempo e no espaço) lido e verificado em dupla fonte (18 folhas confrontadas; 15 zonas a 300 dpi); extracção no reservatório (13 pontos, 15 citações novas); verificador do capítulo verde (77 citações, 0 falhas); errata MD 66 entradas (+15; substantivas: alínea c) do art. 6º CP, data do Ac. STJ 5-4-79, NIPPERDEY, «adoptado»); erratas da edição novas (LA→LN p. 222; 12º/1→12º/2 p. 249; citação do art. 13º/1 ≠ letra — fechada com Ac. STJ 96B112); veredicto NOVA confirmado (espaço = cap. VIII Secção II); art. 297º/2 confirmado (STJ 2005), n.º 1 parcial (STJ 2014 + TC 592/2012); DRE tentado por 5 vias, mantém-se JS-gated; CN sem menção no capítulo. **Propagação a aguardar ok (mapa PROP-BMVIII-01..09 no log)** — por decisão do Telmo, a conversa fechou antes de propagar.

- [2026-07-10] ingestão | BM cap. VII (interpretação e integração) → [[Conceitos/Interpretação da Lei]] e [[Conceitos/Integração da Lei]] criadas; integrações em 6 conceitos; 4 vistas actualizadas (FDUP 21/28, NOVA 9/21, C.Porto I-VI, C.Lisboa 7/15; FDUL sem ponto autónomo); verificador de citações verde (29; 9 adjudicadas pela imagem; 4 erratas novas apanhadas); errata MD 51 entradas; erratas da edição «1976» p. 175 e ZITTELMANN p. 195; dossier CN alargado (2 refs completas novas); arts. 8º-13º CC confirmados em consolidações (DRE em aberto, JS).
- [2026-07-10] Decisões | fecho de conversa passa a regenerar obrigatoriamente o doc `claude/estado-do-cofre.md` do projecto; fecho de cada fonte ingerida passa a incluir revisão total (auditoria integral 4 planos + coerência dos derivados; em obra longa, no fecho da obra); entrega à Oficina única e no fim do BM (relatório de padrões + errata consolidada); bugs/melhorias diferidos para o fim (7 itens acumulados: a-g).
- [2026-07-10] ingestão | BM cap. VI (fontes e vigência) → [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] criadas; integrações em 4 conceitos + errata na Tutela; 5 vistas actualizadas; errata MD 36 entradas; erratas da edição arts. 5º/2 e 7º/4 CC (DRE) e art. 1º CPC (dúvida do cap. V fechada); hipótese CN circunscrita (BFD LI, 1975).
- [2026-07-10] ingestão | BM cap. V (tutela) → [[Conceitos/Tutela do Direito]] e [[Conceitos/Jurisdição]] criadas; integrações em 4 conceitos; 5 vistas actualizadas; errata MD 19 entradas; errata da edição «91º→21º» verificada.
- [2026-07-09] ingestão | 5 fichas institucionais (FDUP, C.Porto, C.Lisboa, FDUL, NOVA) → 5 vistas; BM Fase 0 + caps. I-IV → 10 conceitos criados.
- [2026-07-08/09] Arquitectura | 6.7-6.12 (referências nos produtos; CHANGELOG/git/telemetria; sedes; perspectiva curricular; derivados desactualizados; voz evolutiva; contrato deste resumo).

## Última passagem completa

2026-07-11 — regeneração (quarta, no fecho da conversa do cap. VIII do BM — leitura e verificação; propagação pendente).

---

## Regras de regeneração

1. **Fonte.** Lê-se de `index.md` (contagens, notas-âncora) e de `log.md` (deltas recentes). Nunca se modifica nenhum dos dois a partir daqui.
2. **Reescrita, não acumulação.** Este ficheiro é reescrito por inteiro a cada passagem — guarda só o estado corrente, não história. (Comporta-se como um `-RESUMO`; ver sufixos em `CONVENCOES.md`.)
3. **Tecto.** Alvo ≤ 30 KB. Se exceder após as regras acima, aparar primeiro as «Mudanças recentes», do mais antigo para o mais recente, até ficar abaixo do tecto.
4. **Salvaguarda contra fonte corrompida.** Se `index.md` ou `log.md` estiverem truncados ou ilegíveis, **não** reescrever este ficheiro: registar a falha em `log.md` e parar. Um resumo desactualizado é preferível a um resumo construído sobre fonte partida.
5. **Quando regenerar.** No arranque de uma sessão de consulta à escala (índice acima do orçamento), e ao fim de cada ingestão que altere as contagens. Enquanto a wiki for pequena, este ficheiro pode permanecer vazio — o agente lê o índice directamente, e nada se perde.

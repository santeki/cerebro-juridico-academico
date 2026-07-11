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
| Conceitos | 20 | teoria do Direito (BM caps. I-X); tudo `verificado` |
| Fontes ingeridas | 6 | 5 fichas institucionais + BM (**obra lida por inteiro**: caps. I-XI fechados e propagados; em curso o fecho da obra — releitura selectiva, revisão total, Oficina) |
| Institutos · Doutrina · Jurisprudência · Legislação · Temas · Debates · Avaliação | 0 | por abrir |

## Notas-âncora

- [[Fontes/Baptista Machado, Introdução ao Direito e ao Discurso Legitimador]] — reservatório completo (caps. I-XI); `progresso:` diz o estado do fecho da obra («Tese central» por preencher na releitura selectiva).
- [[Conceitos/Direito Justo]] e [[Conceitos/Discurso Legitimador]] — o par do cap. X (o problema do direito justo, valer/vigorar, *pacta sunt servanda*, indisponibilidade, validade do DP fundada no DN; mediação, círculo hermenêutico, étimo ético, analogia como espinha dorsal) — a tese que dá título à obra.
- [[Conceitos/Aplicação da Lei no Tempo]] e [[Conceitos/Aplicação da Lei no Espaço]] — o par do cap. VIII (direito transitório: arts. 12º/13º/297º; regras de conflitos como normas sobre normas).
- [[Conceitos/Interpretação da Lei]] e [[Conceitos/Integração da Lei]] — o par do cap. VII (hermenêutica e lacunas; arts. 8º-11º e 13º CC na redacção mantida de 1966).
- [[Conceitos/Noção de Direito]] e [[Conceitos/Coercibilidade]] — o par que estrutura o arco caps. II-VII (sentido/coacção; auto-referência; positivação; dialéctica positivo/trans-positivo); o cap. XI rematou o arco pelo lado do saber (ciência jurídica como parte da vida do Direito).
- [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] — o par do cap. VI (produção do Direito; dinâmica temporal e hierárquica da norma posta).
- [[Conceitos/Tutela do Direito]] — porta de entrada da matéria da tutela; ligada por 5 conceitos e 5 vistas.

## Mudanças recentes (últimos 7 dias)

- [2026-07-11] ingestão | BM cap. XI **lido, verificado e propagado** (obra pp. 359-375; periferia relevante — sumário fiel das 7 secções e mapa de conceitos no reservatório, sem página nova). **A obra está lida por inteiro.** Integrações em 5 conceitos (Noção de Direito — ciência jurídica na vida do Direito + CN 5.ª menção; Segurança Jurídica — função estabilizadora da dogmática, p. 366; Jurisdição — juiz órgão da ordem espontânea + ónus de justificação, pp. 365/370-371; Interpretação da Lei — formação dogmática vs literalismo + momento hermenêutico, pp. 368-369/375; Discurso Legitimador — hermenêutica funcionalizada e duas lógicas, pp. 374-375); contadores das vistas inalterados (nenhum programa convoca o XI). Adjudicação: **Canaris, Berlim 1969** (300 dpi; a instrução da sessão antecipava 1968). Erratas do exemplar com âncora de catálogo: «Erkeuntnis» (Springer: *Erkenntnis*) e «BULLEWASCH» (Büllesbach). Remissões X→XI fechadas (286→3,4,6 · 305→5 · 325→3). Dossier CN: quinta menção (p. 371, *Unidade*, p. 14) + bloco de 5 obras na bibliografia (p. 377) — reforço sem fecho. ERRATA-MD 154 entradas (+21). Verificador do capítulo VERDE (71 citações: 57 exactas, 14 adjudicadas, 0 falhas). Título «## Citações literais (excepcionais)» reposto na página de fonte (perdido no fecho do IX; restauro conforme git).

- [2026-07-11] ingestão | BM cap. X **lido, verificado e propagado** (obra pp. 273-357; núcleo; quatro Secções — o índice da p. 388, lido agora, revelou a IV). Criadas [[Conceitos/Direito Justo]] (absorve a promoção do § 6 do IX) e [[Conceitos/Discurso Legitimador]]; integrações em 7 conceitos; vistas FDUP 25/28 · C.Lisboa 11/15 (**leitura prescrita do BM integralmente coberta**; 14-15 com lacunas expressas) · NOVA 14/21 (2 e 9 com ressalva FA) · FDUL 14/19 (16 com lacuna expressa) · C.Porto inalterada. Verificador do capítulo VERDE (371 citações, 0 falhas; 36 recortes a 300 dpi); **verificador global VERDE** (1323 citações no escopo BM, 0 falhas). Erratas MD 102-133 (+32; substantiva: transposição de linhas p. 287); gralhas da edição novas: «ligitimador» (273), «direito zativo» (306), «KAUFMAN»/numeração IV (330), «revelante» ×3 (345 n.), Parsons duplicado pp. 213↔346, e mais; **«§ 442 BGB» (p. 311 n.) em aberto** — Citação por verificar contra Larenz, RR, p. 87. CN: quarta menção (pp. 275-276 n., «Unidade, cit., pp. 77 e s.»); dossier «ob. cit.» inalterado. Fio da p. 254 fechado (pacta sunt servanda, pp. 294-296). Fronteira: cap. X fecha na p. 357; folha 181 = página única (p. 359, abertura do XI; excepção à regra de paginação registada).
- [2026-07-11] auditoria | **verificador global de citações: VERDE** (471 varridas, 0 falhas); 24 deformações do MD em passagens usadas registadas em atraso (erratas 78-101, seis adjudicadas a 300 dpi nesta sessão); sinalizações acrescentadas em 3 páginas; fronteira de citação corrigida na Norma Jurídica.
- [2026-07-11] ingestão | BM cap. IX **lido, verificado e propagado** (obra pp. 253-272; periferia relevante — sumário fiel e mapa no reservatório, sem página nova; «Factiddade» adjudicado como erro de conversão; sem bibliografia própria; CN sem menção; verificador do capítulo verde: 28 citações, 0 falhas; errata MD +11, 67-77). Integrações em Noção de Direito (fundamento suprapositivo, § 6), Jurisdição (modelo jurídico de decisão, § 4) e Segurança Jurídica; vista C.Lisboa — fatia pp. 170-272 da leitura prescrita integralmente coberta (nota de alcance do ponto 10); contadores das vistas inalterados (nenhum programa convoca o IX).
- [2026-07-11] ingestão | BM cap. VIII **propagado** (2 conceitos novos; 6 integrações; 5 vistas — FDUP 24/28, NOVA 12/21 com veredicto do guia, C.Porto I-VII completo, C.Lisboa 8/15, FDUL 13/19; gancho de Eixo B da lei interpretativa BM/Ascensão).
- [2026-07-11] ingestão | BM cap. VIII (aplicação da lei no tempo e no espaço) lido e verificado em dupla fonte (18 folhas confrontadas; 15 zonas a 300 dpi); extracção no reservatório (13 pontos, 15 citações novas); verificador do capítulo verde (77 citações, 0 falhas); errata MD 66 entradas (+15; substantivas: alínea c) do art. 6º CP, data do Ac. STJ 5-4-79, NIPPERDEY, «adoptado»); erratas da edição novas (LA→LN p. 222; 12º/1→12º/2 p. 249; citação do art. 13º/1 ≠ letra — fechada com Ac. STJ 96B112); veredicto NOVA confirmado (espaço = cap. VIII Secção II); art. 297º/2 confirmado (STJ 2005), n.º 1 parcial (STJ 2014 + TC 592/2012); DRE tentado por 5 vias, mantém-se JS-gated; CN sem menção no capítulo. **Propagação a aguardar ok (mapa PROP-BMVIII-01..09 no log)** — por decisão do Telmo, a conversa fechou antes de propagar.

- [2026-07-10] ingestão | BM cap. VII (interpretação e integração) → [[Conceitos/Interpretação da Lei]] e [[Conceitos/Integração da Lei]] criadas; integrações em 6 conceitos; 4 vistas actualizadas (FDUP 21/28, NOVA 9/21, C.Porto I-VI, C.Lisboa 7/15; FDUL sem ponto autónomo); verificador de citações verde (29; 9 adjudicadas pela imagem; 4 erratas novas apanhadas); errata MD 51 entradas; erratas da edição «1976» p. 175 e ZITTELMANN p. 195; dossier CN alargado (2 refs completas novas); arts. 8º-13º CC confirmados em consolidações (DRE em aberto, JS).
- [2026-07-10] Decisões | fecho de conversa passa a regenerar obrigatoriamente o doc `claude/estado-do-cofre.md` do projecto; fecho de cada fonte ingerida passa a incluir revisão total (auditoria integral 4 planos + coerência dos derivados; em obra longa, no fecho da obra); entrega à Oficina única e no fim do BM (relatório de padrões + errata consolidada); bugs/melhorias diferidos para o fim (7 itens acumulados: a-g).
- [2026-07-10] ingestão | BM cap. VI (fontes e vigência) → [[Conceitos/Fontes de Direito]] e [[Conceitos/Vigência das Normas]] criadas; integrações em 4 conceitos + errata na Tutela; 5 vistas actualizadas; errata MD 36 entradas; erratas da edição arts. 5º/2 e 7º/4 CC (DRE) e art. 1º CPC (dúvida do cap. V fechada); hipótese CN circunscrita (BFD LI, 1975).
- [2026-07-10] ingestão | BM cap. V (tutela) → [[Conceitos/Tutela do Direito]] e [[Conceitos/Jurisdição]] criadas; integrações em 4 conceitos; 5 vistas actualizadas; errata MD 19 entradas; errata da edição «91º→21º» verificada.
- [2026-07-09] ingestão | 5 fichas institucionais (FDUP, C.Porto, C.Lisboa, FDUL, NOVA) → 5 vistas; BM Fase 0 + caps. I-IV → 10 conceitos criados.
- [2026-07-08/09] Arquitectura | 6.7-6.12 (referências nos produtos; CHANGELOG/git/telemetria; sedes; perspectiva curricular; derivados desactualizados; voz evolutiva; contrato deste resumo).

## Última passagem completa

2026-07-11 — regeneração (oitava, no fecho do cap. XI do BM — leitura, verificação, propagação; obra lida por inteiro; segue o fecho da obra).

---

## Regras de regeneração

1. **Fonte.** Lê-se de `index.md` (contagens, notas-âncora) e de `log.md` (deltas recentes). Nunca se modifica nenhum dos dois a partir daqui.
2. **Reescrita, não acumulação.** Este ficheiro é reescrito por inteiro a cada passagem — guarda só o estado corrente, não história. (Comporta-se como um `-RESUMO`; ver sufixos em `CONVENCOES.md`.)
3. **Tecto.** Alvo ≤ 30 KB. Se exceder após as regras acima, aparar primeiro as «Mudanças recentes», do mais antigo para o mais recente, até ficar abaixo do tecto.
4. **Salvaguarda contra fonte corrompida.** Se `index.md` ou `log.md` estiverem truncados ou ilegíveis, **não** reescrever este ficheiro: registar a falha em `log.md` e parar. Um resumo desactualizado é preferível a um resumo construído sobre fonte partida.
5. **Quando regenerar.** No arranque de uma sessão de consulta à escala (índice acima do orçamento), e ao fim de cada ingestão que altere as contagens. Enquanto a wiki for pequena, este ficheiro pode permanecer vazio — o agente lê o índice directamente, e nada se perde.

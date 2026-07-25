# PROTOCOLO-EQUIPA.md — camadas de agentes, crescimento e automação suspensa

O agente principal é o maestro: recebe o pedido, despacha sub-agentes especializados quando ajuda, consolida o que devolvem e escreve a nota final. Importado da arquitectura de equipas do schema Nomos (§7), com duas peças que os outros protocolos não cobrem — como a equipa cresce, e o aparato de escrita automática que fica guardado e desligado.

Um sub-agente não sabe mais do que o maestro sobre Direito português; sabe olhar para menos coisas ao mesmo tempo. O ganho é atenção dedicada e lente focada, não saber adicional. Cada um é despachado com prompt próprio, corre em paralelo ou em série, devolve um resultado e desaparece — não há persistência entre sessões, a memória é a wiki. O que é o trabalho central do maestro fica com ele por ser seu, não por omissão: escrever as notas, responder às consultas, manter o cross-linking ao escrever. Nenhuma operação fica órfã.

## As camadas

**Captação** — um leitor por natureza de fonte, cada um a produzir a leitura fiel em `wiki/Fontes/`, reservatório de onde as notas extraem. Leitor de doutrina (sumário por secção, citações com página, mapa de conceitos, posições do autor), digesto de jurisprudência (ratio vs obiter no centro), leitor de legislação (modos sistémico/institucional/artigo, vigência como gate prévio). A cobertura é sempre integral em qualquer deles.

**Sistematização e rigor** — quem constrói e quem verifica. Mapeador transversal (ecos de um conceito noutros ramos, proposta de nota transversal). Sintetizador comparativo (conduz o Eixo B). E o rigor, transversal: verificador de citações (números de artigo, datas, processos, grafia de autores, edições — só propõe, nunca aplica sem revisão; ver `playbooks/verificacao-fontes.md`), vigia legislativo (vigência e alterações, reactivo e proactivo), advogado do diabo (a melhor versão da posição contrária a cada tese dominante, valioso para nota de fonte única e para preparar exame).

**Estudo e manutenção** — examinador socrático (`playbooks/examinador.md`) e lint walker (corre a auditoria, `PROTOCOLO-AUDITORIA.md`).

## Revisão dupla no fecho de estudo

No fecho de cada estudo, duas passagens de revisão com escopos distintos e sem comunicação entre si: a primeira sobre o conteúdo (fidelidade à fonte, patamares, âncoras, erratas), a segunda sobre a integração (propagação completa, wikilinks, índice, coerência com páginas vizinhas, Eixo B onde devido). Com dispatch disponível, correm em paralelo como dois sub-agentes; sem dispatch, correm em sequência como duas passagens separadas do agente principal — a separação de escopo mantém-se, porque é ela que impede a leitura de conteúdo de desculpar a falha de integração, e vice-versa. Achados convertem-se em correcções antes do fecho; o log regista as duas passagens.

## Equipas de despacho activas

Aprovação expressa de 2026-07-17; prompts prontos em ficheiro operacional junto do cofre. **E1** — a revisão dupla do fecho corre por defeito com dispatch, dois sub-agentes em paralelo e sem comunicação (conteúdo ∥ integração); **E2** — adjudicação visual cega: o carácter duvidoso que pede ampliação recebe segunda opinião de um sub-agente que vê apenas a imagem e uma pergunta neutra, nunca a leitura prévia nem a expectativa; convergência fecha, divergência re-amplia ou fica em aberto; **E3** — varredores por lote na revisão total, quando o corpo exceder uma varredura de contexto único (um sub-agente por lote e por plano; consolidação no maestro; o verificador de citações continua por código); **E4** — torneio de teses cego no Eixo B, como modo pesado opcional para divergências cardinais (um advogado por fonte, preso à letra ancorada; o maestro compara e devolve mapa). Invariantes: sub-agentes lêem e reportam, nunca escrevem; todo o achado é verificado pelo maestro contra a fonte antes de aplicar, com registo; falso positivo descarta-se com nota.

Cadência de despacho (mandato expresso de 2026-07-18): os caracteres duvidosos acumulam-se durante a leitura e a adjudicação visual corre numa **única ronda E2 em lote por sessão** (salvo bloqueio que impeça prosseguir sem adjudicação imediata), com o mapeamento folha↔página conferido no ponto exacto da passagem antes de renderizar; **R1 e R2 despacham-se num só acto, em paralelo**, com **tecto de output explícito no prompt** desde a primeira tentativa. Cada ronda de sub-agentes custa minutos fixos de relógio — rondas em série sem necessidade são desperdício.

## Atribuição de modelos aos papéis

Decisão do aluno de 2026-07-24 (conversa 19), na sequência da revisão total dirigida às sessões 3-5: os papéis repartem-se por dois modelos, com fronteira funcional e revisão cruzada. A repartição funda-se nos achados dessa revisão — fidelidade de extracção do executor excelente (zero invenções em 750 confrontos), com o padrão de erro na síntese ambiciosa e nas marcas; registo do orquestrador a subordinar a síntese ao verificável, carecendo igualmente de revisor —, não em juízo de marca.

- **Maestro (orquestrador)** — corre no modelo escolhido ao iniciar a conversa; por defeito, **Fable 5** (`claude-fable-5`). São do maestro as tarefas de juízo e arquitectura: a estrutura do sistema (deltas, modelos de página, granularidade, cisões, fronteiras entre categorias), o mapa (plano de sessões e recortes, mapa de tratamento, cruzamento com os programas das faculdades, fila de ingestão, prompts de retoma), a escrita de síntese dogmática (Noções, «Relação entre as posições» com os Comparativos, hipóteses de fundamento, reconstruções de primeiros princípios, páginas de Debates), a adjudicação (triagem de achados contra a fonte, citação contra paráfrase, patamares N1/N2, decisão final sobre o que a imagem mostra), a auditoria (passes integrais, revisões de fecho, propagação e contadores) e a interface com o aluno.
- **Executor** — os despachos de sub-agentes (E1-E4, leitores de captação, revisores R1/R2, adjudicadores cegos A1, varredores E3, advogados E4, pesquisas dirigidas) correm por defeito em **Opus 5**, por override de modelo no acto de despacho (`model: opus`). Preparam extracções, confrontos, achados e diffs de propagação que o maestro verifica contra a fonte e aplica. A invariante mantém-se intocada: sub-agentes lêem e reportam, nunca escrevem.
- **Separação escritor/revisor entre modelos.** Nenhuma peça é revista pelo modelo que a escreveu: a revisão cega de texto novo do maestro (Noções, sínteses comparativas, camadas de conceito) despacha-se ao outro modelo; as extracções e propostas do executor são verificadas pelo maestro antes de aplicar. Os vícios dos dois modelos são distintos e a revisão cruzada cobre ambos — é a razão de a fronteira não ser «o melhor faz tudo».
- **Proveniência registada.** Cada entrada de log de ingestão, auditoria ou correctiva identifica o modelo do maestro e o dos despachos da operação. A comparação de desempenho entre modelos faz-se contra o log, não contra memória; proveniência não registada não se reconstrói a posteriori.
- **Fallback.** Onde o override de modelo não esteja disponível no ambiente, o despacho corre no modelo da sessão, com o modelo efectivo registado; a separação escritor/revisor mantém-se por passagens separadas com escopos cegos (o regime sem dispatch da revisão dupla, acima).

## Crescimento da equipa

A lista de papéis é o ponto de partida, não o limite. À medida que novos ramos amadurecem e revelam necessidades próprias, que padrões de erro recorrente se manifestam, ou que o maestro identifica lacunas que nenhum papel existente endereça bem, **o maestro propõe um novo papel** — com justificação documentada: padrão de necessidade observado, ganho esperado, custo de coordenação, exemplo concreto da primeira tarefa. Um papel novo só entra com a tua aprovação expressa e registo no `log.md`. A equipa cresce por necessidade observada, não por enumeração antecipada.

Candidatos plausíveis, lista exploratória e não prescritiva: comparatista UE (ler acórdãos do TJUE e integrá-los com o Direito interno, quando o Direito da União amadurecer no cofre); historiador dogmático (genealogia de um instituto); comparatista internacional (ler doutrina alemã, francesa, italiana directamente).

## Automação suspensa (preservada para reentrada)

Em **regime supervisionado** — tu validas cada operação em sessão — vigoram só as regras de diligência e orquestração: o pipeline vigia→verificador→escrita antes de qualquer escrita que toque referências; a escalada ao maestro em caso de conflito entre sub-agentes; o registo de decisões substantivas com prefixo `Decisão` no log. É o regime activo.

O aparato de **escrita automática não-supervisionada** está descrito e **suspenso**. Reentra apenas por tua decisão expressa, no dia em que o cofre passe a despachar sub-agentes que escrevem sem validação em sessão. Fica guardado para não se reinventar mal nessa altura:

- **Triplo gate de escrita.** Escrita automática só aceite se cair numa lista fechada de baixo risco (correcção tipográfica, normalização de frontmatter formal, link interno simples). Tudo o resto vai para um directório `Pendentes/` com o diff proposto e a justificação; a nota original não é tocada até ratificação.
- **Correcção automática em texto substantivo exige duas fontes independentes a convergir** (ex.: alteração confirmada por DRE e por Diário da AR). Fonte única → `Pendentes/`, nunca automático.
- **Circuit breaker por classe de erro.** Dois outputs sucessivos do mesmo sub-agente rejeitados sobre o mesmo tópico → o sub-agente entra em pausa e escreve `Alerta` no log; não volta a correr automaticamente até reactivação manual.
- **Limite de edições automáticas por nota por dia** (três; a quarta vai para `Pendentes/` mesmo sendo baixo risco), para evitar cascatas não percebidas.
- **Audit trail.** Cada dispatch automático regista-se no log com prefixo `Dispatch`; ao exceder um volume mensal, migra para um directório `Auditoria/`.
- **Quarentena de `Pendentes/`.** Edições sem ratificação há mais de 30 dias geram achado de auditoria — `Pendentes/` não acumula em silêncio.

Enquanto a automação está suspensa, os directórios `Pendentes/` e `Auditoria/` não existem; criam-se quando ela reentrar. A pausa manual de um sub-agente mantém-se disponível em qualquer regime.

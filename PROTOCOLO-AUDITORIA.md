# PROTOCOLO-AUDITORIA.md

Verificação periódica de saúde da wiki, em quatro planos. Corre sob demanda ou em cadência (semanal recomendado). Não altera silenciosamente: produz um relatório de achados e propõe correcções que o aluno aprova.

Os primeiros três planos herdam a arquitectura de auditoria do projecto Nomos; o quarto traz o impulso gerador do padrão de wiki (Karpathy).

---

## Plano 1 — Fidelidade à fonte

Verifica que o que está na wiki corresponde ao que a fonte diz.

- Amostrar afirmações substantivas e confrontá-las com a página de fonte e a âncora de localização. A âncora resolve para a passagem certa?
- Citações entre aspas: há texto literal correspondente na fonte? Aspas sem literal correspondente são erro grave — degradar para paráfrase ou remover.
- Atribuições doutrinárias: o patamar declarado (N1/N2) corresponde ao que a fonte sustenta? N1 sem confirmação externa é erro — degradar para N2 com marcador, ou remover.
- Taxonomias: alguma lista foi fechada além do que a fonte fecha? Reabrir e assinalar.

- Erratas identificadas na fonte → o dado correcto está em uso nas derivadas; nenhuma re-cristalizou o texto errado. «Paginação do exemplar» registada quando a fonte é PDF paginado citado por página.

## Plano 2 — Integridade da proveniência

Verifica que cada afirmação é rastreável e que as âncoras se mantêm.

- Páginas com `estado_verificacao: verificado` em que existam afirmações sem âncora → rebaixar para `parcial` e listar as afirmações órfãs.
- Wikilinks de fonte quebrados (apontam para página de fonte inexistente) → reparar ou assinalar.
- Normas citadas sem versão/vigência registada → marcar para confirmação contra DRE/EUR-Lex.
- Jurisprudência citada sem processo/ECLI verificado → marcar para confirmação contra DGSI.
- Sinalização diferida: ressalvas que vivem em nota inicial ou final em vez de junto à afirmação → mover para a frase.
- **Coerência índice ↔ wiki ↔ log**: páginas em `wiki/` ausentes do `index.md`; entradas do `index.md` que apontam para páginas inexistentes; ingestões e comparativos sem entrada correspondente no `log.md`. O índice é precondição da consulta — se mente, a consulta mente.

- Fonte dispensada com registo → não é lacuna nem finding; dispensa sem registo → finding (registar ou reverter).

**Passe mecânico de âncoras (por código, não por geração).** Sub-passe deste plano, executado por script e não por juízo do modelo — é o que quebra a circularidade de o agente se avaliar a si próprio: (a) cada citação «...» com âncora a `raw/` confere-se contra o ficheiro e a página indicados — o trecho existe ou não existe; (b) cada wikilink resolve para página existente; (c) cada atribuição N1 tem âncora presente; (d) cada «em relato» identifica mediador com âncora. Saída: relatório-semáforo, legível numa linha — páginas varridas, âncoras confirmadas, quebradas, órfãs. O que o passe não cobre, e diz-se sempre: a fidelidade semântica — a paráfrase que cita a página certa e distorce o sentido — não é mecanizável; essa fatia cobre-se pelo selo de revisão da origem (`revisto_pelo_aluno`) e pelos *spot-checks* do fecho de ingestão (`PROTOCOLO-INGESTAO.md`). Em cópias distribuídas, os achados deste plano alimentam a errata da edição (`PROTOCOLO-INGESTAO.md`). O passe confere ainda o `hash_raw` de cada página de fonte contra o exemplar em `raw/` — divergência é adulteração ou troca de exemplar, e trava como qualquer âncora quebrada. Em exemplar convertido com errata própria, a conferência da alínea (a) admite três níveis, todos mecânicos: correspondência exacta no derivado de leitura (MD); correspondência após aplicação das correcções da errata; correspondência por padrão documentado de conversão (lista fechada no relatório de padrões do exemplar). Citações que, embora ancoradas em frase da fonte convertida, transcrevam fonte primária própria ou gralha do exemplar marcada [sic] verificam-se contra a sua fonte e entram numa lista fora-de-escopo justificada. Uma falha bloqueia.

**Passe estrutural do esqueleto (por código).** Ao lado do passe de âncoras, e com a mesma natureza — script, não juízo —, verifica-se a integridade do próprio sistema: cada remissão inter-ficheiros (`X.md` em texto normativo) resolve para ficheiro existente — os registos históricos datados e os exemplos marcados como tal ficam de fora, porque citam legitimamente o estado da época ou ilustram o padrão; a árvore documentada nas convenções corresponde ao disco, nos dois sentidos; cada tipo do enum tem o seu modelo (fora os singulares de máquina) e cada modelo o seu tipo; cada caminho da tabela de ponteiros existe; e os exemplos seguem a nomenclatura natural — o exemplo ensina o padrão, tem de o cumprir. Wikilink quebrado ou remissão órfã é falha, não ruído. Corre na auditoria integral e, obrigatoriamente, na verificação final do empacotamento (`PROTOCOLO-EMPACOTAMENTO.md`). As exclusões praticadas ficam codificadas: os exemplos marcados («Ex.:», «p. ex.») das CONVENCOES; a menção em prosa a `log.md` no § Versionamento do `CLAUDE.md`; o `[[página]]` paramétrico de `telemetria.md`; a história datada de `log.md` e do `CHANGELOG.md`; os nomes paramétricos (`X.md`) e os ficheiros gerados a pedido (`ERRATA-EDICAO.md`); e os caminhos com prefixo `claude/` (docs de projecto claude.ai — proveniência externa ao vault, não remissão interna).

## Plano 3 — Qualidade do raciocínio

Verifica a saúde dogmática e estrutural da wiki.

- **Contradições entre páginas** — afirmações incompatíveis em páginas diferentes sobre o mesmo ponto. Listar, com as fontes de cada, para o aluno decidir.
- **Referências cruzadas em falta** — institutos relacionados (intra e inter-ramo) sem ligação entre si. O Direito português é sistema, não conjunto de ramos estanques: a articulação inter-ramo é pano de fundo permanente.
- **Assimetrias de cross-linking** — página A liga a B, mas B não liga de volta a A. As ligações inter-notas são, em regra, recíprocas; a assimetria sinala uma secção *Articulação transversal* por completar.
- **Dúvidas estagnadas** — marcadores de dúvida em aberto (conteúdo ou scan) há muito tempo sem resolução. Listar por antiguidade; as de conteúdo podem fechar com uma fonte nova dirigida, as de scan com nova cópia/OCR. Dúvida que envelhece em silêncio é lacuna que se normaliza.
- **Eixo B por correr** — páginas com `relacao:` atribuída mas `estado_comparativo` parado, ou notas com ≥ 3 fontes activas sem revisão comparativa formal. Propor despacho do Eixo B.
- **Afirmações obsoletas** — fontes mais recentes superaram claims antigos (nova redacção de norma, viragem jurisprudencial). Assinalar o desalinhamento. Diplomas em vacatio cuja data de entrada em vigor já passou → converter `em_vigor` para `true`. `legislacao_verificada_em` ausente ou > 180 dias → crítico; 91–180 dias → atenção; ≤ 90 → em dia. O Vigia confirma na fonte primária antes de qualquer conversão.
- **Páginas órfãs** — sem links de entrada. Ligar a partir das páginas relevantes ou justificar a orfandade.
- **Conceitos sem página** — institutos ou conceitos mencionados com frequência mas sem página própria. Propor criação.
- **Divulgação por depurar** — caracterizações estruturantes marcadas como vindas de divulgação que mereçam confronto com doutrina especializada.
- **Lacunas de dados** — pontos que uma pesquisa dirigida (web, repositório) poderia fechar. Propor as pesquisas.

## Plano 4 — Vertente geradora (o impulso Karpathy)

A auditoria não procura só erros; procura crescimento. Uma wiki que compõe valor melhora quando lhe apontam o passo seguinte, não apenas quando lhe corrigem o passo dado.

- **Conexões por fazer** — dois institutos densos que nunca foram comparados e que beneficiariam de uma nota de distinção ou de uma síntese transversal.
- **Promoções candidatas** — aplicações de ramo que já citam ≥ 2 ramos e pedem promoção a nota transversal; conceitos que aparecem em ≥ 3 ramos e pedem nota-pivô.
- **Sebentas e linhas por abrir** — obras muito ingeridas sem Sebenta; institutos com jurisprudência acumulada sem Linha Jurisprudencial.
- **Cobertura de programa** — cruzar com `Faculdades.md`: tópicos do programa sem página, ordenados por proximidade da avaliação (liga ao Examinador, modo cobertura).

Estes achados são propostas de ingestão e de análise, não correcções — entram na fila, com o aluno a decidir o quê e quando.

## Saída

Um relatório em `wiki/` (não gravado como verdade da wiki, mas como documento de trabalho datado), estruturado pelos quatro planos, com:

- achados por plano, cada um com a página afectada e a correcção proposta;
- prioridade (erro de proveniência > contradição > orfandade > lacuna);
- perguntas novas a investigar e fontes novas a procurar.

O aluno aprova as correcções; só então o agente as aplica e regista a passagem em `log.md`: `## [AAAA-MM-DD] auditoria | <n.º de achados, n.º corrigidos>`.

## Métricas e auto-melhoria

Importado do ciclo de auto-melhoria da Augusta, que mede o sistema com números e acompanha a sua evolução no tempo. A auditoria acima é qualitativa — diz o que está errado; esta vertente é quantitativa — diz se a wiki está a melhorar ou a degradar-se, e confirma se as correcções surtiram efeito.

Cada passagem regista um instantâneo de métricas em `wiki/MELHORIA.md`, com indicadores próprios do domínio: número de páginas por tipo; percentagem de páginas com proveniência completa e verificada; cobertura por cadeira (tópicos do programa com página vs sem); dúvidas em aberto e há quanto tempo; fontes por nível de tratamento dominante (núcleo/periferia/contexto); páginas com revisão devida há mais do que o intervalo; páginas nucleares sem `revisto_pelo_aluno` (informação, não falha). As métricas não são um fim — são o sinal que diz onde a wiki está fraca.

Eixo de cobertura, na vertente qualitativa: a auditoria sinala (a) qualquer nota nuclear cuja base seja maioritariamente secção tratada como periferia ou contexto — sinal de que a secção que a sustenta merece ser elevada a núcleo; e (b) qualquer afirmação substantiva numa nota assente em consulta (fonte não integralmente lida) em vez de fonte ingerida — porque a cobertura é sempre integral, uma consulta nunca é base legítima de nota, e o achado força ou a ingestão integral da fonte, ou a remoção da afirmação.

A peça decisiva é o **tracker week-over-week**: cada passagem confronta as métricas com as da passagem anterior e regista a variação. Foi assim que se verifica se uma correcção landou: se a percentagem de proveniência verificada subiu depois de uma semana a corrigir orfandades, a correcção funcionou; se não mexeu, o problema é outro. O tracker separa o que melhorou, o que estagnou e o que piorou, e alimenta o foco da semana seguinte.

A auto-melhoria distingue, como na Augusta, o que o agente corrige autonomamente (orfandades, ligações em falta, campos de frontmatter em falta — baixo risco) do que **propõe** para a tua decisão (reingestões, reescritas, mudanças de estrutura). O primeiro aplica-se e regista-se; o segundo entra na fila, com identificador estável, para decidires.

## Auditoria de fecho

Além da passagem integral a pedido, a auditoria corre em versão reduzida no fecho de um bloco do programa (gatilho em `PROTOCOLO-GATILHOS.md`): âmbito limitado às páginas do bloco, quatro planos aplicados só a essas, métricas do bloco registadas, leitura da «Cobertura do programa» da vista (o que ficou monocamada ou por cobrir). O fecho sem esta passagem não fecha — é a condição de dar o bloco por encerrado. A bateria de certificação (`CERTIFICACAO.md`) é a camada humana complementar: a auditoria verifica a wiki, a bateria stress-testa o agente contra a fonte — corre-a o aluno quando quer ir ao fundo; não é passo obrigatório do fecho.

**Selo de bloco.** Quando a passagem de fecho confirma todas as condições — fontes do bloco integradas ou dispensadas com registo, páginas do bloco a `verificado`, comparativas fechadas onde há mais de uma fonte, articulação transversal auditada sem assimetrias, passe mecânico de âncoras verde —, a auditoria cristaliza o estado numa linha datada na «Cobertura do programa» da vista:

`✔ {bloco} — fechado {AAAA-MM-DD} · {n} fontes integradas + {m} dispensadas · verificado 100% · comparativas fechadas · transversais ✓ · âncoras ✓ código · {k} pág. revisto_pelo_aluno`

Falha em qualquer condição → sem selo; a passagem lista o que falta e o bloco não se dá por fechado. O selo é o contrato que a consulta exibe na abertura (`PROTOCOLO-CONSULTA.md`); a garantia é relativa ao perímetro declarado — o programa da cadeira e as dispensas registadas —, não ao universo, e o selo di-lo.

## Diligência de segunda ordem (causa-raiz)

Erro substantivo encontrado numa página não se corrige só onde apareceu. Quatro passos: (1) localizar onde o dado errado se cristalizou primeiro — tipicamente a página de fonte ou a primeira derivada, por busca dirigida; (2) verificar contra a fonte primária ou a obra se o lapso é da fonte (então é errata — `PROTOCOLO-INGESTAO.md`) ou da cristalização do agente; (3) corrigir na origem; (4) auditar todas as páginas que herdaram o dado, corrigindo cada uma. O log regista a cadeia — onde nasceu, por onde se propagou, onde se corrigiu. Corrigir só o sintoma deixa a origem a reinfectar a próxima página.

## Cadência sugerida

# PROTOCOLO-INGESTAO.md — Eixo A (estudo de fonte)

Como o agente integra uma fonte nova na wiki. Concretiza a regra 1 do `CLAUDE.md` (proveniência verificada) e a regra 10 (digestão integral): é a porta por onde o conteúdo entra, e nenhuma afirmação a atravessa sem ancoragem, nenhuma fonte se ingere a meio.

Princípios. A cobertura é sempre integral: uma fonte que entra na wiki lê-se do início ao fim, sem amostragem — notas de rodapé incluídas, é onde o autor põe divergências e exemplos —, e enquanto não estiver digerida e com relatório no log, nenhuma outra ingestão se abre (sobreposição de ingestões é proibida). O que se gradua é o **tratamento** de cada secção, não a leitura (abaixo). A página de fonte é **reservatório** — preservação máxima do que a fonte diz, com âncora; as páginas de entidade são **selectivas** — convocam da leitura só o que ilumina. As notas extraem da leitura, nunca directamente do PDF.

## Cobertura integral e graduação de tratamento

A cobertura é sempre integral. Toda a fonte que entra na wiki lê-se do início ao fim, sem amostragem, sem leitura diagonal — notas de rodapé incluídas, porque é aí que o autor põe ressalvas, divergências e exemplos. Uma fonte parcialmente lida não foi ingerida: foi consultada, e a consulta não sustenta cobertura nem serve de base a uma nota. A regra defende contra o erro mais difícil de ver, a lacuna invisível — quem amostra escolhe o que lê pelo que já sabe ser relevante, e a parte saltada é, por definição, a que não sabia ser relevante; meses depois esse buraco é indistinguível de conhecimento sólido, porque o contexto do autor já se perdeu e ninguém marca uma lacuna que não percebe ter. Uma consulta dirigida a um ponto isolado é legítima como acto de pesquisa, mas não é ingestão: não cria página de fonte como reservatório coberto, e a nota que dela aproveite um ponto marca-o como vindo de fonte não ingerida, sujeito a confirmação.

O que se gradua não é a leitura — é o **tratamento**, decidido na Fase 1, secção a secção:

- **núcleo** — tratamento integral: citações literais com página, promoção dos conceitos a nota própria, Eixo B, reconstrução de primeiros princípios do ponto e das perguntas que levanta (marcada como construção — ver «Raciocínio de primeiros princípios» no `CLAUDE.md`). É a matéria da fonte com mais peso para o que estudas.
- **periferia relevante** — sumário fiel e mapa de conceitos, sem nota a cada conceito tocado de leve. Lê-se com a mesma atenção; trabalha-se com menos profundidade.
- **contexto** — sumário curto. Material que situa, não que fundamenta.

Ler tudo não é tratar tudo com a mesma intensidade, e tratar não é transcrever: a fonte lê-se por inteiro, trabalha-se por níveis, a nota convoca só o que ilumina. A graduação poupa o esforço caro — a extracção e a promoção a nota —, **nunca** o esforço de cobertura (ler) nem o de verificação (confirmar contra primária). Uma periferia resume-se com fidelidade; não se afirma sobre ela sem confirmar. Em tensão entre cobertura e parcimónia de escrita, a cobertura vence na leitura e a parcimónia vence na escrita; o tratamento é o eixo intermédio, e o seu critério é o limiar de inclusão da Fase 4 («o que entra»), estendido ao «quanto se trabalha». O mapa de tratamento — que secções são núcleo, periferia, contexto — regista-se na própria leitura.

Uma fonte não muda de cobertura (é sempre integral); o que pode mudar é o tratamento de uma secção, quando o uso revela que merece mais profundidade. A auditoria sinala a nota nuclear cuja base é maioritariamente periferia ou contexto — sinal de que a secção que a sustenta merece ser elevada a núcleo.

---

## Fase 0 — Admissão da fonte (gate de fiabilidade)

Antes de ler para extrair, confirmar que a fonte é real, citável e **fiável**. Só fontes fiáveis alimentam o cofre — o Direito evolui, e evolui por fontes que se confirmam, não por rumor.

1. Identificar o tipo — manual, monografia, capítulo, artigo, legislação, acórdão, apontamento de aula, recensão, material de avaliação (exame, caso prático, teste, frequência, correcção-modelo, colectânea resolvida) — e a **classe de fiabilidade**: `primaria-oficial` (DRE, EUR-Lex, DGSI, reguladores — sustenta tudo; é a via da actualização normativa e jurisprudencial), `doutrina-verificada` (obra com autor, título e edição confirmáveis), `institucional` (programa, slides, enunciados e correcções do docente — autoridade pedagógica, nos limites já fixados), `apontamento-proprio` (registo de aula do próprio aluno — sustenta o padrão do docente e o recorte da cadeira; o Direito que afirme verifica-se contra as classes superiores antes de propagar). Material **não-autoral e não-verificável** — sebenta anónima, resumo de site, apostila sem origem — **não é admitido**: o agente recusa e oferece a alternativa (verificar os pontos contra o corpo e as fontes fiáveis, ou trazer a obra de origem). Entrar «em-aberto» serve a obra real por confirmar, nunca o inverificável. Com a classe atribuída, **triagem técnica do exemplar** antes de dedicar leitura integral: texto extraível (ou OCR a correr primeiro), páginas completas, notas de rodapé presentes, legibilidade — exemplar deficiente regista-se na página de fonte e pede-se cópia melhor, ou decide-se a dispensa formal; horas de ingestão integral não se gastam num scan que as desperdiça. No registo, fixa-se o `hash_raw` — SHA-256 do exemplar em `raw/`, a âncora de integridade que o passe mecânico confere daí em diante — e, havendo OCR, `ocr_motor` e `ocr_data`.
2. Capturar a referência completa: autor(es), título, edição, ano, editora; ou diploma, data, número; ou tribunal, data, processo, ECLI, relator.
3. Para obra doutrinária: confirmar existência contra catálogo de biblioteca, repositório ou recensão. Se a obra não se confirma, a fonte entra na wiki como `estado_verificacao: em-aberto` e não sustenta atribuições N1.
4. Para legislação: confirmar vigência e versão consolidada (DRE para Direito interno, EUR-Lex para Direito da União). Registar a versão.
5. Para jurisprudência: confirmar o processo e o ECLI em DGSI (ou base equivalente). Não reconstruir o ECLI de memória.

Saída: uma página de fonte em `wiki/Fontes/` criada a partir de `modelos/modelo-fonte.md`, com a referência completa, o estado de verificação, a classe de `fiabilidade:`, a `procedencia:` (edicao | local) e o `hash_raw` do exemplar.

### Situação da fonte — entre o gate e a leitura

Antes de abrir a primeira página, situa-se a fonte — contra a leitura ingénua e o anacronismo silencioso. Meia página na página de fonte, secção *Situação*, com as lacunas marcadas: na **doutrina**, o projecto intelectual do autor (escola, interlocutores, fase na trajectória), a edição concreta (o que mudou face às anteriores, porquê esta) e a recepção conhecida (recensões, contestações documentadas); na **jurisprudência**, o colectivo e o relator, o contexto processual (tipo de recurso, antecedentes) e o posicionamento na trajectória do tribunal (reafirma, inflecte, uniformiza); na **legislação**, a génese (que problema resolve), os trabalhos preparatórios — com leitura autónoma quando substanciais (> 5 páginas ou matéria interpretativa relevante; no trivial, a citação directa basta) —, a trajectória de alterações e a inserção sistemática. Tudo por fonte verificada ou marcado como lacuna. É deste material que as hipóteses de fundamento do Eixo B nascem — sem Situação, o «porquê» das divergências não tem de onde vir.

## Fase 1 — Leitura e extracção ancorada

1. Ler a fonte em `raw/`, do início ao fim. Se tiver imagens, ler primeiro o texto e depois ver as imagens referenciadas (o agente não lê markdown com imagens inline numa só passagem).
2. Fixar o **mapa de tratamento**: percorrida a fonte (ou o seu índice, em obra longa), decidir que secções são núcleo, periferia relevante e contexto. A cobertura mantém-se integral em qualquer dos casos — o mapa só diz quanto se trabalha cada parte, não quanto se lê. Registar o mapa na página de fonte.
3. Extrair as afirmações relevantes, cada uma com âncora de localização: página, secção, parágrafo, ou número de margem. A âncora acompanha a afirmação desde o primeiro momento. A profundidade da extracção segue o mapa: citação literal com página no núcleo, sumário fiel na periferia, sumário curto no contexto. Posição de terceiro autor convocada pela fonte extrai-se **em relato**, com o mediador e a sua âncora desde o primeiro registo (regra em relato do `CLAUDE.md`). Distinta do relato é a **citação por fonte secundária inacessível**: quando a fonte primária é genuinamente inalcançável (obra esgotada sem exemplar localizável, manuscrito, parecer não publicado) e após esforço documentado para a obter — quatro diligências cumulativas, heurística presumível e afastável com fundamentação: consulta aos catálogos da BNP e de pelo menos duas bibliotecas de Direito; tentativa de empréstimo interbibliotecário ou de aquisição em segundo mercado; contacto ao autor ou à editora, com espera razoável (≥ 30 dias); e registo datado de cada diligência, com interlocutor e resposta, na sub-secção *Diligências para fonte primária* da página de fonte. Até as quatro estarem documentadas, o passo fica «aguarda fonte» —, admite-se citar pela secundária com marcação expressa (`> **Citação por fonte secundária:** {…}; primária inacessível — esforço: {…}`) e com `triangulacao_pendente:` no frontmatter da página que a recebe. Esta citação nunca vale como fonte plena para sustentar posição consolidada, e a auditoria mantém-na visível até resolução.
4. Separar, na extracção: (a) o que a fonte afirma como Direito vigente; (b) o que a fonte atribui a outro autor; (c) o que é posição própria da fonte de iure condendo; (d) o que é exemplo ou hipótese. Não fundir estes registos.

**Marcadores de dúvida, por etiologia.** Dúvida silenciosa equivale a invenção. Sinalizar com o marcador certo — o diagnóstico errado é, ele próprio, falta de diligência. Duas categorias, com lógica de resolução distinta:

*Sobre o conteúdo* (resolve-se com outra fonte que toque o ponto; não tem prazo):
- `> **Dúvida de interpretação:**` — passagem do autor com formulação opaca; transcrever literal.
- `> **Citação por verificar:**` — acórdão/norma/obra invocada cuja confirmação exige consulta externa.
- `> **Fonte externa invocada mas não consultada:**` — obra citada pelo autor, não lida autonomamente.
- `> **Taxonomia não fechada pelo autor:**` — autor dá parte de uma lista sem a fechar; não completar.

*Sobre a leitura do scan* (resolve-se com outra cópia, novo OCR, ou cotejo com o papel):
- `> **OCR ambíguo:**` — caracteres duvidosos no rendering; transcrever com [?]. Antes de classificar como ambíguo, considerar se a passagem está em língua estrangeira legítima — a doutrina portuguesa cita rotineiramente em alemão, francês, italiano, inglês, espanhol e, por vezes, latim. Não confundir língua estrangeira com erro de OCR.
- `> **Caractere físico ilegível:**` — degradação do original abaixo da camada OCR (mancha, dobra, riscado).
- `> **Página em falta ou truncada:**` — página saltada pelo scan, margem cortada, coluna ou nota truncada.

## Fase 2 — Classificação de verificabilidade

Para cada afirmação extraída, classificar:

- Norma → verificável directamente contra fonte primária. Confirmar redacção e vigência.
- Jurisprudência → verificável contra DGSI. Confirmar tribunal, data, processo, ECLI.
- Atribuição doutrinária → aplicar patamares N1/N2/N3 (regra 5 do `CLAUDE.md`). Só N1 sustenta citação com aspas; N2 entra com marcador honesto sem aspas; N3 não entra.
- Caracterização dogmática estruturante → marcar se vem de doutrina especializada ou de divulgação (regra 9).

Nenhuma afirmação avança para a Fase 3 sem classificação.

## Fase 3 — Síntese na página de fonte

Escrever a síntese da fonte em `wiki/Fontes/<fonte>.md`:

1. Tese central da fonte, em paráfrase do agente (não transcrição).
2. Pontos relevantes, cada um com âncora de localização.
3. Citações literais só quando a formulação exacta importe — entre aspas curvas «...» (ou itálico, se em língua estrangeira), com a âncora. Paráfrase é o modo por defeito; transcrição é a excepção.
4. Onde a fonte diverge de outras já na wiki, anotar a divergência com remissão para a outra fonte.

## Fase 4 — Propagação para as páginas de entidade

Quando a fonte pertence ao programa de uma cadeira, a propagação inclui a «Cobertura do programa» na vista da faculdade — o sub-ponto passa ao estado que o estudo lhe dá (coberto ou monocamada), no fecho do estudo.

A síntese alimenta as páginas permanentes. Para cada afirmação classificada:

1. Localizar ou criar a página de entidade (instituto, conceito, doutrina, jurisprudência, legislação) a partir do template em `modelos/`.
2. Integrar a afirmação na página, com wikilink para a página de fonte e a âncora de localização. Cada frase substantiva fica rastreável (regra 4 do `CLAUDE.md`).
3. Quando duas fontes convergem sobre o mesmo ponto, identificar ambas. Quando coexistem sobre o mesmo conceito — convirjam ou divirjam —, disparar o **Eixo B** (`PROTOCOLO-ANALISE-COMPARATIVA.md`): classificar a relação (`relacao:` — complementares, compatíveis, distintas, em-conflito), sub-classificar se em conflito, e percorrer os Comparativos. Se a divergência é viva, abrir ou actualizar uma página em `wiki/Debates/`.
4. Actualizar o `estado_verificacao` da página de entidade: `verificado` só se cada afirmação substantiva estiver ancorada; `parcial` se há blocos por confirmar.

Gates intransponíveis nesta fase:

- Nenhuma afirmação entra sem âncora.
- Nenhuma atribuição doutrinária entra sem patamar N1 ou N2 (e N2 entra sem aspas, com marcador).
- Nenhuma norma entra sem vigência confirmada.
- Nenhuma taxonomia se fecha além do que a fonte fecha.

## Fase 5 — Contradições e lacunas

1. Se a fonte contradiz uma afirmação já na wiki: não apagar a antiga. Registar ambas, com data e fonte de cada, e assinalar a tensão na página da entidade e numa entrada de `wiki/Debates/` se justificar. A auditoria decidirá, com o aluno, qual prevalece.
2. Se a fonte revela uma lacuna (instituto mencionado sem página própria, conceito sem definição): criar página-esboço com `estado_verificacao: em-aberto` e registá-la na lista de lacunas do `index.md`.

## Fase 6 — Índice e log

1. Actualizar `wiki/index.md`: adicionar as páginas novas, rever as linhas de resumo das páginas alteradas.
2. Acrescentar entrada a `wiki/log.md` com o prefixo canónico: `## [AAAA-MM-DD] ingestão | <Título da fonte>`, seguida de: páginas tocadas, contradições assinaladas, lacunas abertas, estado de verificação resultante.

## Sub-fluxos por tipo de fonte

As fases acima são o tronco comum. Cada tipo de fonte tem ênfases próprias na leitura (Fase 1) e na síntese (Fase 3):

- **Doutrina.** Sumário por capítulo ou secção; tese central do autor; mapa de todos os conceitos, institutos, acórdãos e autores mencionados; a posição do autor em cada controvérsia que toca; exemplos do autor preservados (Menezes Cordeiro a ilustrar abuso do direito com a *exceptio doli* vem para a leitura); genealogia histórica num bloco próprio quando a fonte a traça. A página de fonte é o reservatório; a Sebenta (`modelos/modelo-sebenta.md`) reorganiza a matéria por institutos quando a obra justifica.
- **Jurisprudência.** A distinção entre *ratio decidendi* e *obiter dicta* no centro. Factos · questão · decisão · *ratio* · *obiter*. Distinguir sumário oficial de texto integral. Confirmar tribunal, secção, data, processo, ECLI, relator em DGSI. Quando se acumulam decisões sobre um instituto, considerar uma Linha Jurisprudencial (`modelos/modelo-linha-jurisprudencial.md`). A distinção marca-se na extracção, bloco a bloco; quando duvidosa, marcador próprio — `> **Ratio/obiter incerto:** {fundamentação}` — que a auditoria mantém visível. As **declarações de voto** não são *obiter*: são dissensão dentro do colectivo, com sub-secção própria na página do acórdão, e alimentam a divergência no Eixo B quando toquem instituto com página.
- **Legislação.** Vigência e versão consolidada como gate prévio (DRE/EUR-Lex), antes de tratar o texto. Antes do mapa, a decisão arquitectural — o **modo de estudo**, registado em `modo:` no frontmatter: *sistémico* (o diploma na sua arquitectura — Códigos e leis estruturantes; capta lógica e articulação interna, não desce a cada artigo), *institucional* (um regime dentro do diploma — p. ex., a responsabilidade civil nos arts. 483.º a 510.º do CC —, artigo a artigo dentro do âmbito) ou *artigo individual* (um artigo que justifica página própria). O modo compromete profundidade e âmbito, e a pausa acompanha-o: por Livro ou Título no sistémico, por bloco coerente no institucional, única no artigo. Vacatio: registar `data_publicacao`, `data_entrada_vigor`, `em_vigor: false` quando aplicável. Versões históricas de um artigo invocadas por uma fonte: transcrever a versão tal como invocada e confrontá-la com a redacção actual, identificando diploma alterador e data.
- **Material de avaliação** (exame, caso prático, teste, frequência, correcção-modelo). Categoria de primeira importância — a componente prática é central ao estudo da cadeira, e em muitas é o eixo da avaliação. Entra da pasta `Avaliação/` da cadeira em `raw/` e cria página em `wiki/Avaliação/` (`modelos/modelo-fonte-avaliacao.md`). Ingere-se por dois valores: o **padrão** (que recorte do programa sai, que tipo de questão, que armadilhas, que pontuação) e o **treino**. Três cautelas da regra-âncora, intransponíveis: (1) o enunciado e os factos são exercício, preservam-se como texto da prova, mas não são fonte de Direito; (2) a resolução de terceiro — colega, explicador — nunca sobe a doutrina nem sustenta atribuição; (3) a correcção-modelo do docente entra como **autoridade pedagógica** (o que se espera e como se pontua), com marcador, não como tratado, e onde divirja da posição dominante na doutrina, assinala-se o desalinhamento em vez de o resolver elevando a grelha a fonte. Propagação própria: o «O que revela do padrão» alimenta o «Histórico de avaliações» da vista (`wiki/Faculdades/<Faculdade>.md`), e os institutos convocados ligam ao corpo. A colectânea publicada com autoria trata-se como doutrina, com autor, obra e patamar N1/N2.

## Caminho curto — a fonte pequena

A cerimónia completa é da obra longa; a fonte pequena — o acórdão, o artigo de revista, o capítulo isolado, o diploma curto (≈ até 25 páginas) — corre por defeito o caminho curto: gate da Fase 0 integral e sem excepção (fiabilidade, vigência, `hash_raw`), Situação em três linhas, extracção ancorada directa, fecho com páginas e cross-linking. Dispensam-se agenda, bloco panorâmico, refresher e pausas intermédias, com nota de dispensa na página de fonte. O caminho curto não dispensa nada epistémico — dispensa andaimes de atenção que a dimensão não justifica. Na dúvida sobre a dimensão, pergunta-se; e se a meio a fonte se revelar maior do que parecia, sobe-se ao ciclo capitular com registo.

## Obra longa — ciclo capitular

Quando a fonte tem capítulos e centenas de páginas, a leitura integral organiza-se sem perder fôlego nem supervisão: **agenda de leitura** no arranque — as perguntas que a wiki actual leva à fonte e as hipóteses sobre a posição do autor que se querem testar, registadas na página de fonte antes da primeira página lida (é o que torna a leitura activa); **bloco panorâmico** único — pré-leitura do índice de todos os capítulos, com função expectável e conceitos prováveis por capítulo (dispensável em obra curta ou uniforme, com nota); **refresher** no início de cada capítulo — reler a entrada panorâmica desse capítulo e fixar as páginas a tocar; **pausa entre capítulos** — cada capítulo fecha com a extracção feita e as páginas actualizadas, e a continuação propõe-se numa linha com default marcado, ficando as decisões substantivas (categoria nova, conflito com página existente) sempre à espera de quem opera; e, no fecho da obra, **releitura selectiva** dos capítulos cujo sentido mudou à luz dos posteriores — a iluminação retroactiva regista-se na página; obra linear dispensa, com nota. O campo `progresso:` do frontmatter diz sempre onde a leitura vai.

## Paginação de PDF — probe antes de citar

Num PDF paginado, a página do ficheiro e a página da obra podem não coincidir — e o desvio pode variar ao longo do exemplar, com páginas omissas pelo meio. Antes de citar uma página que seja, confirmar a correspondência por âncoras: pelo menos dois pontos afastados do recorte, lidos pelo número impresso no cabeçalho ou rodapé. O desvio verificado (por intervalos, quando variável) e as páginas omissas registam-se na página de fonte, em «Paginação do exemplar»; os recortes de extracção calculam-se com o desvio; a citação usa sempre a página da obra. Quando a correspondência não se consegue estabelecer, cita-se por secção e título, com a limitação assinalada. Fonte com marcas de página no próprio texto dispensa o probe — a marca é a âncora.

## Erro material da fonte (errata)

Uma fonte pode conter erro material — número de processo trocado, data errada, remissão deslocada, gralha de referência. Quatro passos: (1) verificar contra a fonte primária (DGSI, DRE, EUR-Lex, a obra citada) antes de qualificar como errata — a hipótese de o erro ser da leitura testa-se primeiro; (2) registar na página de fonte, em «Erratas identificadas», a localização na obra, o texto errado, o correcto e a âncora da verificação; (3) as páginas derivadas usam o dado correcto, com nota curta da errata onde a divergência possa confundir quem confronte com a obra; (4) propagar a correcção a toda a página que tenha cristalizado o dado errado. A citação da obra mantém-se fiel ao que a obra escreve, com o correcto ao lado.

## Fonte dispensada

Uma obra recomendada pelo programa pode ser dispensada por decisão do aluno — cópia degradada, redundância com fonte melhor, custo sem retorno. A dispensa regista-se uma vez, na «Cobertura do programa» da vista da faculdade, com razão, data e a decisão. O corpo das páginas não a menciona; as consolidações não a tratam como pendência; a auditoria não a relata como lacuna — «dispensada» é resposta, não falha. Reverte-se por decisão expressa, nunca por deriva.

## Discussão com o aluno

O modo recomendado mantém o aluno envolvido: depois da Fase 3, o agente apresenta os pontos-chave da fonte — tantos quantos a fonte justifique, sem tecto arbitrário — e o mapa de propagação previsto, e só avança para a Fase 4 com o «ok» do aluno. Para batch de baixo risco (várias fontes convergentes do mesmo autor já verificado), o aluno pode dispensar a confirmação intermédia — mas os gates da Fase 4 mantêm-se sempre.

## Fecho da ingestão — semáforo e spot-checks

Concluída a Fase 6, o passe mecânico de âncoras (`PROTOCOLO-AUDITORIA.md`, plano 2) corre automaticamente sobre as páginas tocadas e devolve o semáforo numa linha. Com o semáforo verde, o agente propõe dois ou três *spot-checks* de trinta segundos — «abre a p. {N} da fonte e confirma que esta frase lá está» —, escolhidos entre as afirmações de maior peso; o aluno pode dispensá-los, e os feitos ficam registados. É a fatia que o código não cobre (fidelidade semântica), reduzida a gesto de estudante; a bateria completa (`CERTIFICACAO.md`) fica para a auditoria profunda e para a origem, não para o dia-a-dia.

## Actualização normativa e jurisprudencial (a evolução do Direito)

O Vigia detecta; a fonte primária confirma; só então se propaga. Nenhuma alteração de norma ou viragem de jurisprudência entra no cofre com base em notícia, resumo ou memória — o sinal secundário é gatilho de suspeita, e a entrada exige confirmação na fonte primária oficial (DRE/EUR-Lex; DGSI). Confirmada, a versão nova ingere-se como fonte `primaria-oficial` com `procedencia: local`, e a propagação corre a maquinaria existente: `em_vigor` converte-se, a doutrina sobre a redacção anterior marca-se datada, as afirmações obsoletas caçam-se na auditoria, e o contrato do terreno abre com a actualização e a sua data. A camada local prevalece sobre a camada de edição exactamente aqui — a vigência vence —, por camadas e nunca por apagamento: a redacção anterior fica como histórico datado. Fora deste circuito, material local nunca reescreve página de edição: entra pelo Eixo B como fonte distinta e marcada.

## Detecção no arranque

No arranque de cada sessão, o agente varre `raw/` por material entrado desde a última passagem e propõe a ingestão numa linha, com default marcado — o aluno não tem de se lembrar de pedir.

## Errata da edição

O circuito da errata da fonte ganha, nas cópias distribuídas, um troço de retorno. Na cópia: os achados que o uso produz — âncora quebrada que o passe marcou, paráfrase que um *spot-check* desmentiu, erro substantivo detectado — compilam-se, a pedido, num relatório exportável na raiz do vault (`ERRATA-EDICAO.md`), pronto a enviar à origem; a correcção local aplica-se pela diligência de segunda ordem, com `procedencia: local`. Na origem: as erratas recebidas triam-se como achados de auditoria — confirmadas contra a fonte, corrigem-se na instância de referência e incorporam-se na edição seguinte (`PROTOCOLO-EMPACOTAMENTO.md`). É o que faz a qualidade compor com a escala: cada erro encontrado por uma cópia morre em todas.

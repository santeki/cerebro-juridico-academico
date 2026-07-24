# PROTOCOLO-ANALISE-COMPARATIVA.md — Eixo B

Como o agente sistematiza um conceito tratado por mais de uma fonte. Unidade de trabalho: o conceito (a página de entidade), não a fonte. O Eixo A (ingestão) capta cada fonte com fidelidade; o Eixo B articula as posições que várias fontes tomam sobre o mesmo conceito.

Activação dupla: (a) disparado pela propagação do Eixo A, quando uma fonte nova coexiste com fonte(s) anterior(es) sobre um conceito; (b) autónomo, por instrução do aluno, sobre material já ingerido — tipicamente quando uma página acumulou três ou mais fontes sem revisão comparativa formal. O `estado_comparativo` no frontmatter percorre `aguarda-comparativo → comparativo-n-em-curso → comparativa`.

Tudo o que aqui se produz está sujeito às regras-âncora do `CLAUDE.md`: nenhuma relação, sub-classificação ou fundamento entra por inferência; em silêncio ou ambiguidade da fonte, parar e sinalizar.

---

## Limiar de registo — tensões só se evidentes

Só se regista tensão ou conflito quando for evidente nas fontes — afirmado pelos próprios autores ou identificado por terceiro autor. Diferenças de propósito não são tensões: a construção dogmática que convoca um acórdão para confirmação operativa não está em tensão com o acórdão que decide o caso concreto; a leitura ampla não conflitua com a leitura focada por terem âmbitos distintos. Em dúvida, omitir — página sem tensão é superior a página com tensão fabricada. Diferenças factuais robustas (alteração legislativa superveniente, revisão posterior, revogação ou superação por decisão posterior) registam-se sempre: são objectivas, não doutrinárias.

---

## Classificação da relação entre posições

Quando uma segunda (ou n-ésima) fonte trata o conceito de uma fonte já registada, a relação enquadra-se numa de quatro categorias, registada no campo `relacao:` do frontmatter. O trabalho analítico varia com ela.

- **Complementares.** Cada fonte trata aspectos distintos; somam-se sem tensão. O trabalho é articular como se compõem — não há divergência a investigar.
- **Compatíveis.** Convergem na substância; coexistem sem ajuste, eventualmente reforçando-se. O trabalho é registar a convergência e desfazer tensões aparentes na comparação substancial.
- **Distintas.** Diferem em aspectos identificáveis sem oposição directa. O trabalho é articular onde diferem e a função jurídica das diferenças (substantivas vs expositivas), e investigar selectivamente o fundamento quando justifique.
- **Em Conflito.** Opõem-se substantivamente. Aqui o trabalho de investigação do porquê (substrato doutrinal) é coração analítico, não acessório. Aplica-se a sub-classificação abaixo.

A classificação não é eterna — futuras fontes podem reclassificar (registar em sub-secção *Reclassificações*).

## Sub-classificação do caso «Em Conflito»

Cinco cenários operativamente distintos:

- **(I) Sinonímia genuína** — mesmo conceito, nomes diferentes. *Operação*: uma só página, sob o nome dominante na tradição portuguesa, com mapeamento das designações alternativas no frontmatter (`equivalencias:`) e numa secção *Designações alternativas*; cada secção interna cita o termo que esse autor usa. *Reclassificação*: de `em-conflito` para `compativeis` — afinal não havia conflito real.
- **(II) Divergência terminológica que esconde divergência conceptual** — termos próximos com extensão e função distintas. *Operação*: comparação substancial; se forem o mesmo conceito apesar das aparências, aplica-se (I); se forem conceitos diferentes ainda que próximos, duas páginas com remissão recíproca robusta e secção comparativa.
- **(III) Divergência classificatória como sintoma de divergência doutrinária mais ampla** — um autor classifica X como instituto, outro como princípio; a divergência traduz-se em consequências operativas (princípio admite ponderação; instituto tem regime fechado) e é tipicamente ponta de iceberg metodológico. *Operação*: registar a divergência no frontmatter (`categoria:` mantém-se lista, todas em pé de igualdade) e investigar o fundamento em secção *Divergência — fundamento doutrinário*.
- **(IV) Divergência intra-jurisprudencial sem uniformização** — dois acórdãos do mesmo nível ou de tribunais distintos contradizem-se sem AFJ que componha. *Operação*: registar as posições aspecto a aspecto, identificar as *ratios* divergentes, marcar a ausência de uniformização. Espera-se ou propõe-se AFJ.
- **(V) Desalinhamento doutrina ↔ jurisprudência** — a doutrina dominante afirma X; a jurisprudência uniforme decide não-X (ou vice-versa). *Operação*: registar ambas com fidelidade aspecto a aspecto; investigar o fundamento doutrinário de uma e o racional jurisprudencial da outra; mapear consequências práticas no Bloco III da nota (*Critério de decisão*, sub-secção *Desalinhamento*). Categoria própria, de valor alto: sinala o que cada parte vai invocar.

## Árvore de decisão (caso «Em Conflito»)

Aplicar por ordem ao caso doutrinário; para o caso jurisprudencial sem AFJ, ir directamente a (IV); para o confronto doutrina↔jurisprudência uniforme, a (V).

1. As duas posições atribuem o mesmo conteúdo a designações diferentes? **Sim** → (I), e reclassificar para `compativeis`. **Não** → seguir.
2. Os termos aproximam-se mas a extensão/função diverge? **Sim** → (II): decidir se mesmo conceito (aplica I) ou conceitos distintos (duas páginas). **Não** → seguir.
3. A divergência é de classificação (instituto vs princípio, etc.) com consequências operativas? **Sim** → (III). **Não** → conflito substantivo directo: investigar fundamento na secção própria.

## Aplicação a fontes mistas

- Doutrina vs doutrina — framework (I)/(II)/(III) integral.
- Doutrina vs jurisprudência uniforme — (V) Desalinhamento; o Comparativo 3 corre nas duas direcções (porquê doutrinário; racional jurisprudencial).
- Doutrina vs jurisprudência não uniforme — primeiro (IV); a doutrina entra como contexto interpretativo de cada *ratio*.
- Doutrina vs legislação — o Comparativo 3 (porquê) é redundante (a lei não tem porquê doutrinário próprio); o Comparativo 4 (consequências) é central. Doutrina que lê o texto contra o que ele manda regista-se como erro doutrinário, não como divergência viva.
- Jurisprudência vs jurisprudência — (IV).

---

## Os passos (Comparativos 0 a 6)

Cada transição gera entrada de log com prefixo `Comparativo`; o `estado_comparativo` actualiza-se na mesma operação.

**Comparativo 0 — Inventário e classificação.** Listar todas as páginas de fonte que tocam o conceito. Atribuir a categoria geral em `relacao:`. Sub-classificar se «Em Conflito». Decidir a arquitectura da nota (por defeito, em página de conceito, a do `modelos/modelo-conceito.md` — Ideia · Posição por autor · Relação entre as posições; nos casos especiais: uma página com equivalências; duas com remissão; nota com sub-secção *Desalinhamento*). *Feito*: inventário registado + classificação atribuída + arquitectura definida.

**Comparativo 1 — Reposicionamento focado.** Cada fonte ganha um resumo articulado no conceito (não no capítulo onde aparece). Para cada, re-extrair da página de fonte a secção *Posição de [Autor]* da página de conceito (`modelos/modelo-conceito.md`), com citações verificáveis e paginação, e remissão para a leitura. *Feito*: cada fonte com posição articulada e referenciável.

**Comparativo 2 — Mapeamento substancial.** Tornar visível como as posições se relacionam, segundo o Comparativo 0: (Complementares) que aspectos cada uma cobre; (Compatíveis) onde convergem, tensões aparentes que se desfazem, reforço mútuo; (Distintas) diferenças aspecto a aspecto, ênfase vs conteúdo; (Em Conflito) onde concordam apesar de termos diferentes e onde divergem apesar de aparente acordo, em matriz quando ajude. *Feito*: mapeamento fiel, ajustado à classificação.

**Comparativo 3 — Investigação do porquê.** Coração analítico, quando aplicável (plena em Em Conflito; selectiva em Distintas; dispensada em Compatíveis/Complementares, com nota expressa de dispensa). Investiga *com base em material já registado* (a situação de cada fonte; declarações expressas dos autores sobre a sua escola). Não infere posicionamento metodológico não declarado; em ambiguidade, marca hipótese provisória. O agente formula a hipótese fundamentada e marca-a como hipótese; o aluno valida antes de virar tese. *Output*: sub-secção *Divergência — fundamento doutrinário* (ou *Diferenciação*), com estatuto claro (`> **Hipótese de fundamento doutrinário:** ...`). *Feito*: cada divergência substantiva com investigação do porquê (no mínimo, hipótese registada).

**Comparativo 4 — Consequências operativas.** A relação muda resultados em casos concretos? (Complementares) a integração pode mudar a abordagem; (Compatíveis) normalmente nada muda — registar isso; (Distintas) depende; (Em Conflito) tipologia de casos onde a divergência altera o resultado, com exemplos. *Feito*: tipologia mapeada, com exemplos ou explicitação de ausência.

**Comparativo 5 — Posição na tradição.** Como a relação vive na literatura mais ampla: quem segue quem (quando conhecido), existência de terceira via, linhas de tradição (escola de Coimbra, de Lisboa, influências alemãs). Em wiki jovem, cresce com o tempo. *Feito*: material disponível registado; lacunas marcadas.

**Comparativo 6 — Síntese comparativa.** Articular a relação como um todo, em forma utilizável: parágrafo articulado — não duas páginas — que integra os Comparativos 2 a 5 e respeita a classificação do 0. *Feito*: síntese produzida na secção da relação + *Ideia* da página revista à sua luz + remissões internas para o detalhe.

---

## O que o Eixo B nunca faz

- Não atribui relação, sub-classificação ou fundamento por inferência — só a partir de texto lido e confirmado.
- Não fixa hipótese de fundamento como tese sem validação do aluno.
- Não achata vozes: em vez de colapsar três autores numa frase consensual, regista as três.
- Não apaga a posição anterior quando uma fonte nova reclassifica — migra-a para *Reclassificações*, com data e fonte.

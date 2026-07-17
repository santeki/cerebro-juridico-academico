# Relatório de padrões de conversão — para a Oficina

**Obra:** J. Baptista Machado, *Introdução ao Direito e ao Discurso Legitimador*, 13.ª reimpressão, Almedina, 2002 (PDF de 199 folhas; Markdown paginado por folha `[p. N]`).
**Data:** 2026-07-16, no fecho da obra (absorção integral — caps. I-XI + índice + bibliografia — fechada a 2026-07-11).
**Base:** errata consolidada de **188 entradas** (ficheiro `…-ERRATA-MD.md`, ao lado deste), construída por dupla fonte — todo o número e citação usados confirmados contra o PDF, com ampliação a 300 dpi (600 dpi nos casos difíceis) nos dígitos e palavras duvidosos; as entradas 187-188 (pp. 364/360) foram adjudicadas a 2026-07-17 com dupla leitura independente (maestro + adjudicador cego). Substitui o relatório intercalar de 2026-07-10 (10 padrões sobre 36 entradas).
**Distribuição por capítulo:** I 14 · II 6 · III 3 · IV 3 · V 10 · VI 15 · VII 26 · VIII 24 · IX 13 · X 49 · XI 20 · aparato final 3 · índice gerado 2. Dezassete entradas são **substantivas** (alteram remissão normativa, número de artigo, alínea, data ou nome); as restantes deformam a letra sem alterar o sentido, mas contaminam qualquer citação literal.

## A. Padrões de carácter (os mais frequentes)

1. **«1»/«l» e «0»/«O» trocados**, também dentro de palavras: «l)» por «1)», «1.°)» por «l.°)», «princ1p10» por «princípio», «institucionali1.ação»; «art. 12. 0» por «art. 12.º» (o «º» degrada em «0» com espaço antes). Afecta sistematicamente ordinais e numeração de artigos — é o padrão com maior risco jurídico.
2. **«rn»↔«m» e afins**: «urna» por «uma», «contomos»/«contornos», «participa,n» por «participam» (o «m» degrada em «,n»), «modema». Frequente em itálico.
3. **«t»/«r» e letras vizinhas em itálico**: «constiturivo» por «constitutivo», «porestas» por «potestas», «prion» por «priori», «conduza» por «conduta», «nprender» por «aprender», «desejapas» por «desejadas».
4. **Acentos perdidos ou lidos como «~»/ruído**: «Hermen~utica» por «Hermenêutica», «Atê»/«vé» por «Até»/«vê», «arríscariam», «e\oluti\O» por «evolutivo» (acento+letra em barra invertida). O circunflexo é a vítima habitual.
5. **«/» por «l» em itálico**: «nih/o» por «nihlo», «vacatio /egis», «Civi!e».
6. **Aspas**: abertura lida como «..», «••», «·», «u» colado («uorigem», «uconcretização»), «4» («4 "universais"») ou «--» («--abolição do homem»); fecho lido como «n» («podern.» por «poder".», «determinen») ou absorvido com perda do «s» final («esta"» por «estas»); apóstrofos duplicados «''».
7. **Pontuação trocada**: vírgulas lidas como pontos (sobretudo nas notas: «da coincidência. da consonância»), ponto médio e ruído «·•~_» intruso, espaço intruso em versaletes e siglas («H USSON», «M L», «K \l l·\1» por «KAUFMANN»).
8. **Estrangeiro em itálico é a zona de maior taxa de erro** — alemão sobretudo: «Erk,·untnis», «Un,ollstãidigkeit», «Sysiembegrf[(», «Entscheidw.g um/», «Rechrswissenschaft», «R,•,·htsdoKmatik». Sugere passe dedicado com léxico DE/LA/FR.

## B. Padrões de estrutura (os mais perigosos)

9. **Blocos de notas intercalados no corpo**, cortando frases ao meio — a nota entra onde calha na coluna, não no fim: casos verificados nas pp. 32 (citação de Esser cortada), 228 e 246 (notas dos acórdãos STJ/STA), 368. Em três casos a intercalação **come texto**: «tal qualificação equivale a uma» (p. 246), «linguagem» (fronteira pp. 339-340), «que a origem é,» (fronteira pp. 347-348).
10. **Transposição de blocos em fronteira de página**: o art. 895.º (pp. 331-332) fica partido — «Logo que o vendedor adquira por» salta o parágrafo seguinte e retoma «algum modo a propriedade…» adiante; mesmo fenómeno nas pp. 355-356 (errata 128) e na p. 287.
11. **Cabeçalhos correntes no fluxo do texto** («Introdução ao Direito e ao discurso legitimador NNN», «A ciência jurídica NNN»), por vezes deformados («legitimo.dor», «dl$curso», «pir…»); em fronteira de capítulo o cabeçalho impresso pode antecipar o capítulo seguinte (pp. 151 e 171 — característica do exemplar, não da conversão).
12. **Zonas de meia-coluna degradadas** — margem esquerda da folha 181 (p. 359) e blocos de notas das pp. 362 e 371 quase ilegíveis na camada de texto; recuperáveis a 300-600 dpi.
13. **Índice gerado incompleto**: o índice produzido na conversão omite o ponto 12 do cap. I (errata 5) e deforma entradas («CAPfrULOXI», «3'S9», «ckmífica»).
14. **Particularidades do exemplar a preservar** (não são erros da Oficina, mas pedem cuidado no pipeline): folha 181 com **uma só página** (o verso p. 358 não tem imagem); versos em branco com transparência da página seguinte (p. 376); gralhas do próprio impresso que devem ficar como estão («Erkeuntnis», «BULLEWASCH», «trancendentes», «KAUFMAN», «4.ª e ed. 1979», «pp., 227») — o leitor jurídico precisa de as ver com [sic], não corrigidas em silêncio.

## C. Recomendações concretas

(a) Re-OCR selectivo a ≥300 dpi das zonas de notas de rodapé e margens esquerdas; (b) regra de **não intercalação**: notas ancoradas no fim da página, nunca no meio de parágrafo; (c) validação de fronteira de página: a última linha de cada página e a primeira da seguinte conferidas em par (apanha quedas e transposições); (d) léxico PT-jurídico + alemão/latim/francês para itálicos; (e) verificação de aspas balanceadas por parágrafo; (f) normalização vigiada de ordinais («12.º», «n.º») e numeração romana; (g) preservação de gralhas do impresso com marca própria em vez de correcção silenciosa; (h) conferir o índice gerado contra os títulos do corpo.

## D. Nota sobre o Oliveira Ascensão

O exemplar do Ascensão foi convertido **antes** deste relatório. Os padrões A1-A8 e B9-B13 devem estar-lhe presentes na mesma escala; se a re-passagem do pipeline for barata, vale a pena re-converter antes de a ingestão abrir (decisão do Telmo no passo 5 do fecho). A errata consolidada anexa serve de conjunto de teste: as 186 entradas dão pares deformado→correcto verificados para calibrar qualquer afinação.

---
*Gerado no fecho da absorção do BM; entrega à Oficina pelo Telmo (Decisão de 2026-07-10 — entrega única, no fim da obra). A errata consolidada viaja ao lado: `Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md` 

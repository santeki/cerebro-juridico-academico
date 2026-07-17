# Ascensão - re-passagem v2: relatório de entrega e diff resumido

**Obra:** J. de Oliveira Ascensão, *O Direito. Introdução e Teoria Geral* (PDF de 630 folhas; 605 214 459 bytes, md5 `4300d23c029edfdde0c9dd5b8299dcac`, conferido na remontagem de 2026-07-16).
**Entrega:** 2026-07-17, em resposta ao fecho da obra BM. A re-passagem foi executada a **2026-07-16**, já com o pipeline afinado pelo relatório de padrões do BM (14 padrões A/B/C) e calibrado contra a errata consolidada; as entradas 187-188, adjudicadas a 2026-07-17, são do BM e não introduzem classe nova, pelo que não alteram este resultado. Registos canónicos no projeto: `lote1-ascensao-relatorio-repassagem-v2.md` (tabela integral folha · antes → depois), `lote1-ascensao-adjudicacoes.jsonl` (~330 adjudicações, incluindo 53 «fiéis confirmados»), `lote1-ascensao-diagnostico-v2.md` (diagnóstico e avaliação de custo).

## 1. Caminho escolhido (avaliação de custo, 2026-07-16)

Passe **incremental** sobre o MD do lote 1, não re-conversão de raiz: o diagnóstico com os detetores v2 testou a hipótese do relatório BM e mostrou que os padrões de carácter (A1-A8) estavam presentes em escala igual ou superior, mas os três padrões estruturais mais perigosos **não** (B9 notas intercaladas: 0; B11 cabeçalhos no fluxo: 0; B13 índice incompleto: 0 - a estrutura do lote 1 aguentou-se). Re-converter de raiz teria ganho estrutural nulo, reproduziria os truncamentos da própria camada OCR do exemplar e deitaria fora as ~490 correções adjudicadas do lote 1. O passe incremental custou uma sessão de adjudicação por grelhas de recortes (30 grelhas; 300 dpi, 600 nos difíceis).

## 2. O que o pipeline afinado apanhou - diff face à conversão de 2026-07-10

**177 correções em 135 folhas**, todas adjudicadas pela imagem, com registo integral antes → depois; as ~490 correções do lote 1 ficaram intactas.

Fase 1, substantivos em contexto normativo (143 de 265 candidatos; os restantes ou fiéis ou sem base inequívoca):

(a) 90 ordinais «0»→«º» em remissões e datas («n. 0 284» → «n. º 284»; «art. 1. 0 do Código Civil português» → «art. 1. º…»; «1.0 de Junho de 1967» → «1.º de Junho de 1967»);
(b) 39 plurais «n.0s»/«n. os» → «n.ºs»;
(c) 8 palavras/nomes («*lnfra*» → «*Infra*», «L' *1çoes*» → «*Lições*», «*lbid.*» → «*Ibid.*», «*Absclzied*» → «*Abschied*»);
(d) 4 romanos («li», «Ili», «JV» → «II», «III», «IV»);
(e) 2 pontuais.

Casos substantivos que importam aos ganchos da wiki (números, datas, remissões), da tabela integral: p. 203 «25º *lbid.,* n.0s 209 e segs.» → «250 *Ibid.,* n.ºs 209 e segs.» (número de nota); p. 384 «sub *art. 5* 11. 0 *3 e art. 6 n.* 0 *I (da Lei» → «sub *art. 5 n.º 3 e art. 6 n.º 1 (da Lei» (remissão); p. 534, nota 825, «Dec.-Lei n.0 47 344. de 25 de Novembro» → «Dec.-Lei n.º 47 344, de 25 de Novembro» (vírgula confirmada a 600 dpi); p. 566 «Dcc.-Lei» → «Dec.-Lei»; p. 286 «Direito Administrativo,* l, n. 0 35» → «…* I, n. º 35».

Fase 2, fronteiras e zonas (34): as 48 fronteiras de página candidatas adjudicadas em par, uma a uma - a maioria sãs ou com margem direita cortada na própria digitalização; renderam ainda «li»→«II» (pp. 135, 555), «primeito»→«primeiro» (p. 35), «pe,feito»→«perfeito» (p. 550), rabiscos de leitor transcritos como texto removidos (pp. 71, 88, 388) e as **reparações de zona degradada por sublinhados do leitor**, repostas parágrafo a parágrafo pela imagem nítida subjacente: pp. 4 (bloco «Notas» fantasma dissolvido - caso único na obra, rastreado), 55, 83, 84, 146, 147 (secção 92 integral), 148, 374, 387.

**53 formas confirmadas FIÉIS** ao impresso e não tocadas (tipografia do próprio exemplar: «n. º» com espaço fino; «n.os» na linha nas pp. 24 e 589; «n°» sem ponto nas pp. 447 e 614; «n°.» na p. 300; «47344» colado na p. 301) - lista em `mantidos-ascensao.txt` (no zip da entrega de 2026-07-16), que se subtrai ao passe de suspeitos das futuras passagens.

## 3. Zonas que continuam degradadas (declaradas; sem adjudicação pendente)

Os detetores v2 ainda assinalam ~2900 suspeitos de carácter no MD final, de três naturezas conhecidas: (a) as formas fiéis acima, que o detetor não distingue sem o ficheiro de mantidos; (b) ruído residual das 89 folhas com sublinhados/margens (concentrado em pp. 8-35, 51-94, 135-149, 371-443, 455-471), fora de remissões normativas e de citações estruturais - as zonas de maior dano foram reparadas por imagem; (c) estrangeirismos legítimos fora dos léxicos. As margens direitas cortadas na própria digitalização («aspectc», «variaçã<», «obrigaçãc») ficam como o exemplar digital as dá: a imagem não tem os caracteres, e nenhuma ampliação os recupera - só um novo exemplar físico. Não há, por isso, folhas a pedir novo upload a maior resolução.

## 4. Invariantes, conferidas hoje sobre o ficheiro entregue

630/630 marcadores `[p. N]`; gralhas do próprio impresso presentes tal-e-qual (amostra verificada: «erga ommes», «constiticional», «3654e»); ortografia pré-Acordo intocada; sem embelezamento nem reordenação além das reposições adjudicadas por imagem. O PDF continua a ser a verdade; a marcação [sic] é trabalho do cofre.

## 5. Decisão registada

2026-07-16, fim de sessão: o Ascensão v2 segue para absorção no cofre académico; o lote 2 decide-se depois dessa absorção. Se a absorção gerar errata, como no BM, a Oficina integra-a no mesmo circuito (parse → regressão → adjudicação).

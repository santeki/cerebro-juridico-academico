# Playbook — Verificação de fontes por tipo

Regras de verificação que a ingestão e a consulta aplicam. A verificação contra fonte primária cobre a norma, mas não esgota a diligência: cada caso convoca fontes específicas.

## Legislação

- Direito interno: confirmar redacção e vigência em DRE (Diário da República Electrónico), versão consolidada. Registar a data da versão.
- Direito da União: confirmar em EUR-Lex, versão consolidada. Distinguir versão em vigor de versões anteriores.
- Nunca reconstruir número de artigo ou redacção de memória. Doutrina sobre redacção anterior cita-se com ressalva expressa.

DRE: `files.diariodarepublica.pt` serve os PDF oficiais (I Série histórica incluída) a fetchers automáticos e vale como publicação oficial — via confirmada a 2026-07-16; **limite prático: ficheiros > 20 MB excedem o tecto do fetcher** (caso real: DG n.º 274/1966, o Código Civil integral, pp. 1883-2086 num só PDF). O detalhe e o consolidado em `diariodarepublica.pt` permanecem JS-gated — via estável para consolidados: Claude in Chrome. PGDL serve como espelho de trabalho, sempre com confirmação do cabeçalho do diploma servido (caso de página errada servida em URLs por artigo, registado a 2026-07-11 na sessão da edição DCP — doc de projecto `claude/cowork-dcp-josh.md`): espelho não é publicação oficial.

## Jurisprudência

- Confirmar tribunal, secção, data, processo e ECLI em DGSI (ou base equivalente da jurisdição). Nunca reconstruir o ECLI de memória.
- Distinguir sumário de texto integral; distinguir ratio de obiter.
- Para jurisprudência da União: confirmar em EUR-Lex/CURIA.

## Doutrina

- Confirmar existência da obra (autor, título, edição, ano, editora) contra catálogo de biblioteca, repositório universitário ou recensão. Sem confirmação, a obra não sustenta atribuição N1.
- Atribuição de posição a autor: contra fonte secundária acessível (Google Scholar, repositório, revista) ou marcação expressa de inferência. O nome do autor soar correcto no contexto não basta.
- Patamares N1/N2/N3 conforme regra 5 do `CLAUDE.md`. Particular rigor sobre nome, obra, edição e posição atribuída — os quatro pontos em que a invenção soa mais plausível.

## A regra do destinatário

Quando a wiki serve preparação para um interlocutor identificado com produção académica acessível sobre o tema (um orientador, uma banca), procurar e ler primeiro essa produção. A posição dogmática do destinatário é central, não acessória.

## Limites do agente

Para citação textual com peso forense ou académico, a confirmação directa contra obra física ou digitalizada autêntica é trabalho do aluno. O agente mapeia, identifica pólos de divergência, sugere leituras, localiza passagens em versões digitalizadas públicas quando existam, e sinaliza com honestidade o que não consegue confirmar.

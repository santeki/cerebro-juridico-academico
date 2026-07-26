---
tipo: fonte
titulo: "{Autor, Título}"
referencia_completa: "{Autor}, {Título}, {n.ª} ed., {Editora}, {ano}"   # ou {diploma, data, n.º} | {tribunal, data, processo, ECLI}
tipo_fonte: manual | monografia | capitulo | artigo | legislacao | jurisprudencia | apontamento | recensao
fiabilidade: primaria-oficial | doutrina-verificada | institucional | apontamento-proprio   # gate da Fase 0; o não-verificável não entra
procedencia: edicao | local          # camada: embarcada pela origem | ingerida nesta cópia
hash_raw: ""                         # SHA-256 do exemplar em raw/ — o passe mecânico confere a integridade
ocr_motor: ""                        # opcional — motor e versão, quando houve OCR (triagem técnica)
ocr_data:                            # opcional — data ISO do OCR
progresso: ""                        # opcional — «Cap. N de M, p. X» em fontes longas que atravessam sessões
cobertura: integral                  # invariante: toda a fonte ingerida é lida do início ao fim (PROTOCOLO-INGESTAO)
tratamento_nucleo: "{secções tratadas a fundo: citação literal onde a letra pesa + paráfrase ancorada, nota própria, Eixo B}"
tratamento_periferia: "{secções em sumário fiel e mapa de conceitos}"
tratamento_contexto: "{secções em sumário curto}"
ramo: []
estado_verificacao: verificado | parcial | em-aberto
confirmacao_existencia: "{catálogo/repositório/recensão onde a obra foi confirmada}"   # obrigatório para sustentar N1
ingerida_em: AAAA-MM-DD
ficheiro_raw: "[[raw/...]]"
---

# {Autor, Título}

> **Cobertura sempre integral**: a fonte foi lida do início ao fim (notas de rodapé incluídas). Uma fonte não integralmente lida não é fonte ingerida — é consulta, um acto de pesquisa pontual que não gera página de fonte coberta como esta. O que se gradua é o **tratamento** por secção: núcleo (citação literal onde a letra pesa + paráfrase ancorada, nota própria, Eixo B) · periferia relevante (sumário fiel e mapa) · contexto (sumário curto). A graduação poupa extracção, nunca cobertura nem verificação. Ver `PROTOCOLO-INGESTAO.md`.

## Referência
{Referência completa. Para obra: autor, título, edição, editora, ano. Para legislação: diploma, data, número, versão consolidada e respectiva fonte (DRE/EUR-Lex). Para jurisprudência: tribunal, secção, data, processo, ECLI, relator.}

## Mapa de tratamento
{Que secções se trataram como núcleo, periferia e contexto. A cobertura é integral em todas; isto regista só a profundidade de trabalho de cada uma. A nota nuclear deve assentar em secções de núcleo — uma nota cuja base é periferia ou contexto é sinal de que a secção merece ser elevada.}

## Paginação do exemplar
{Só para PDF paginado: desvio página-PDF ↔ página-obra, por intervalos quando variável · páginas omissas · âncoras do probe. Ver `PROTOCOLO-INGESTAO.md`.}

## Erratas identificadas
{Só quando existam: localização na obra · texto errado → correcto · âncora da verificação.}

## Tese central
{Paráfrase do agente — não transcrição. O que esta fonte sustenta, no essencial. Em `referencia`, deixar vazio até leitura.}

## Pontos relevantes
{Cada ponto com âncora de localização. Em obra longa cuja página exceda o
orçamento das CONVENCOES, os registos de sessão vivem em sub-páginas de
leitura («{obra} — leitura da sessão N», tipo fonte; frontmatter mínimo: tipo,
titulo, referencia_completa, tipo_fonte, fiabilidade, procedencia, ramo,
estado_verificacao), com esta secção reduzida a índice de sessões; identidade,
hash_raw, agenda e dossiers transversais ficam sempre na página-mãe. Ex.:}
- {Afirmação} — p. ___ / § ___ / nota de margem ___.

## Citações literais (excepcionais)
{Só quando a formulação exacta importe. Aspas curvas «...» (ou itálico se em língua estrangeira), com âncora. Paráfrase é o modo por defeito.}

## Divergências face a outras fontes da wiki
{Onde esta fonte contradiz ou matiza páginas já existentes. Remissão para a outra fonte e para a página de debate, se houver.}

## Páginas que esta fonte alimenta
{Wikilinks para as páginas de entidade tocadas na ingestão.}

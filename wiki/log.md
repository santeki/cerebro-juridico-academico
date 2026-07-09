# Log — Segundo Cérebro Jurídico Académico

Registo cronológico append-only. Cada entrada abre com prefixo canónico, para ser parseável:

`grep "^## \[" wiki/log.md | tail -5`

Tipos de entrada:

| Prefixo | Quando |
|---|---|
| `Arquitectura` | alteração ao schema/charter (com `versao: N.M` e tipo: aditiva/correctiva/redefinitória) |
| `ingestão` | fonte estudada (Eixo A) |
| `Comparativo` | passo do Eixo B (com o número do Comparativo e o `estado_comparativo` resultante) |
| `consulta` | pergunta respondida a partir da wiki |
| `auditoria` | passe de saúde (Eixo de auditoria) |
| `Decisão` | decisão substantiva com efeito persistente (categorização canónica, nomenclatura, classificação de relação) — `Decisão \| <descrição> \| <fundamentação curta>`, para poder reabrir em revisão |
| `Excepção` | desvio pontual ao schema aceite pelo aluno (sem alterar o schema) |
| `Dúvida resolvida` | dúvida em aberto que uma fonte nova fechou — liga a dúvida original à fonte que a resolveu |
| `Delete` | rotação para `archive/` (nunca eliminação) |

---

<!-- Exemplos de entrada:

## [2026-06-28] ingestão | Hespanha, Cultura Jurídica Europeia, Almedina, 2012
- Fonte admitida: existência confirmada (catálogo). Estado: verificado.
- Páginas tocadas: [[Institutos/...]], [[Conceitos/...]], [[Fontes/Hespanha, Cultura Jurídica Europeia]]
- Contradições: nenhuma. Lacunas abertas: [[Conceitos/...]] (esboço, em-aberto).

## [2026-06-28] Comparativo | boa-fé — Comparativo 3 concluído
- relacao: em-conflito (sub-tipo III). estado_comparativo: comparativo-3-em-curso → comparativo-4.
- Hipótese de fundamento doutrinário registada, aguarda validação do aluno.

## [2026-06-28] Decisão | dolo — desambiguação por homonímia
- Criadas Dolo (Civil).md, Dolo (Penal).md, dolo.md (desambiguação). Fundamentação: conceitos distintos sob o mesmo nome.

## [2026-06-28] Dúvida resolvida | natureza da responsabilidade pré-contratual
- Dúvida aberta em [[Fontes/A]] (2026-06-10) fechada por [[Fontes/B]] p. 212.

-->

## [2026-07-07] Arquitectura | versao: 4.1.2 — correctiva; lente «jurista» → «professor»
- «Jurista» reserva-se para o género: professores, advogados e juízes são todos juristas. Migradas as quatro sedes (charter ×2, glossário, modelo-instituto); usos genéricos intocados. Verificação de resíduo sem ocorrências. Decisão expressa do operador; divergência deliberada face à linhagem Nomos.

## [2026-07-07] Arquitectura | versao: 5.0 — redefinitória; o cofre serve o aluno
- Utilizador único: o aluno. Professor deixa de ser perfil (playbook rotacionado; Examinador reorientado; referências removidas); camada de avaliação e padrão de ensino do docente intactos — o docente é objecto de estudo. «Operador» → «aluno» no texto normativo; campo `revisto_pelo_aluno`. Decisão expressa do aluno.

## [2026-07-07] Delete | playbooks/professor.md → archive/professor.md
- Rotação (nunca eliminação), na sequência da redefinição 5.0.

## [2026-07-07] Arquitectura | versao: 5.1 — aditiva; quatro heurísticas
- Intérprete (elementos da interpretação, art. 9º CC, elemento a elemento com fonte); Exposição invertida como 4º modo do Examinador; Variação de factos no caso prático; distinguishing no Advogado do diabo. Charter e consulta actualizados. Decisão expressa do aluno.

## [2026-07-07] Arquitectura | versao: 5.2 — aditiva; bateria de certificação embarcada
- `CERTIFICACAO.md` na raiz: dez testes de conhecimento e dois reforços, instrumento do aluno, com enquadramento honesto (o agente não se auto-certifica; rastreio, sonda e âmbito exigem a fonte aberta). Ligada nas convenções, no charter e na auditoria de fecho; kit passa a referenciar a bateria embarcada. Integrada de linha paralela sobre a base 4.1.1, adaptada à terminologia da 5.0.

## [2026-07-07] Arquitectura | versao: 5.3 — aditiva; garantias de uso
- Passe mecânico de âncoras (semáforo, por código); selo de bloco na vista via auditoria de fecho; contrato do terreno na abertura da consulta; confronto de exaustividade; fecho de ingestão com spot-checks dispensáveis; CERTIFICACAO reposicionada (auditoria profunda e origem). Decisão expressa do aluno.

## [2026-07-07] Arquitectura | versao: 6.0 — redefinitória; interface, produção e edição
- Conversa como interface (vault = janela opcional, invariante de vault válido); trabalho-mínimo com perguntar-último-recurso; configuração conversacional; detecção no arranque; PROTOCOLO-PRODUCAO + identidade/ + regra-âncora visual; EDICAO.md, fiabilidade e procedencia (gate da Fase 0; actualização só confirmada em fonte primária). Kit reescrito ao consumidor. Decisão expressa do aluno.

## [2026-07-07] Arquitectura | versao: 6.1 — aditiva; pipeline de origem
- PROTOCOLO-EMPACOTAMENTO (embarca/reinicia/fica; ensaio de edição; co-produção v1); triagem técnica do exemplar na Fase 0; errata da edição (retorno cópia→origem). O corpo alimenta também a linha profissional. Decisão expressa do aluno.

## [2026-07-07] Arquitectura | versao: 6.2 — aditiva (guarda estrutural) com correcções
- Passe estrutural do esqueleto (remissões, árvore↔disco, enum↔modelos, ponteiros, exemplos em nomenclatura natural) na auditoria e no empacotamento; exemplos com slug pré-4.0 corrigidos (charter, log, ESTADO-RESUMO). Auditoria das quatro árvores sem achados. Decisão expressa do aluno.

## [2026-07-07] Arquitectura | versao: 6.3 — aditiva; registo do discurso
- O interlocutor é jurista e o discurso corresponde-lhe: técnica sem diluição, sem excessos, entrada directa, objecção qualificada; profundidade calibrada ao estudo. Subsecção de «Como se opera». Decisão expressa do aluno.

## [2026-07-08] Arquitectura | versao: 6.4 — aditiva; recuperação Nomos
- Nove peças triadas do charter antigo: vocabulário de força quantificado, citação por secundária inacessível, hash_raw/ocr/progresso e legislacao_verificada_em (com semáforo e gatilho), Situação da fonte, ciclo capitular de obra longa, modos de estudo de legislação, Ratio/obiter incerto e declarações de voto, edições cirúrgicas e execução orientada a critérios. Decisão expressa do aluno.

## [2026-07-08] Auditoria | revisão total da versão em curso
- Overview e revisão integral (charters lidos de ponta a ponta; bateria mecânica: auditor estrutural, UTF-8, tokens entre linhas, enums, campos↔modelos, remissões nomeadas). Três correcções de coerência integradas na versão: data do frontmatter alinhada (2026-07-08); campo transversal `triangulacao_pendente:` fixado nas convenções; modelo de jurisprudência do profissional em paridade (Ratio/obiter incerto; Declarações de voto). Falso alarme documentado: menções a `revisto_pelo_aluno` no profissional são a regra de conversão do empacotamento e registo datado — legítimas.

## [2026-07-08] Arquitectura | versao: 6.5 — aditiva; delta da revisão 2.1 (Nomos)
- Diligências quantificadas na citação por secundária inacessível; excepção do cross-linking nas edições cirúrgicas; granularidade das páginas (pergunta decisora; fronteira e promoção aplicação↔instituto). Decisão expressa do aluno.

## [2026-07-08] Arquitectura | versao: 6.6 — aditiva; modo «Torneio de teses»
- Análise integral do repositório DeepReason (sem licença publicada: nada do código ou texto entra no cofre); o método integra-se em redacção própria como modo analítico — esqueleto com falsificador jurídico obrigatório, refutação só contra o corpus com âncora, confronto par a par, saída em mapa. Decisão expressa do aluno.

## [2026-07-08] Arquitectura | versao: 6.7 — aditiva; walkthrough do aluno
- Referências e bibliografia nos produtos (PROTOCOLO-VOZ; campo norma_citacao na vista de faculdade; NP 405-1 como referência natural; pendência declarada quando não configurada). Restantes jornadas confirmadas cobertas. Decisão expressa do aluno.

## [2026-07-08] Arquitectura | versao: 6.8 — re-derivação: infra-estrutura
- Histórico migrado para CHANGELOG.md; git inicializado com tag v6.8 e .gitignore criado (Camada 1 densificada); telemetria de convocação (wiki/telemetria.md, Frente 4 do Painel); relações tipadas mínimas (contraria/concretiza/excepciona); caminho curto na ingestão; casos dourados na origem. Decisão expressa do aluno.

## [2026-07-08] Arquitectura | versao: 6.9 — sedes, paridade e modos (trabalhos adiados)
- Piloto de consolidação: padrão sede-única confirmado instalado; eco da regra 10 fundido; «Arquitectura de sedes» codificada nas convenções. Paridade: divergências dos 3 ficheiros ≥ 0.90 classificadas intencionais; deriva zero; paridade.py com baseline instalado na fonte. Modos: todos mantidos com fundamento; Mapeador transversal sob telemetria — revisão marcada para quando houver dados de uma cadeira completa. Decisão expressa do aluno.

## [2026-07-09] Arquitectura | versao: 6.10 — perspectiva curricular
- Syllabus como bússola, não algemas: regra de perspectiva na consulta (ordena, não amputa; fora-do-programa e outras escolas marcados) e no Examinador (padrão do docente primeiro; outras escolas como contraste que soma em exame). Não toca a linha profissional. Decisão expressa do aluno.

## [2026-07-09] Arquitectura | versao: 6.11 — derivados desactualizados
- Frente 5 do Painel: fonte nova que toque instituto com sebenta/diagnóstico/resposta-modelo emitidos marca-os desactualizados (nota datada + log); listagem até refresh; nunca servidos como actuais. Manual tardio = caso normal. Decisão expressa do aluno.

## [2026-07-09] Arquitectura | versao: 6.12 — método Augusta (voz evolutiva; contrato do resumo)
- Evolução do fingerprint por correcções (proposta+evidência+✅; VOZ-EVOLUCAO.md); contrato de poda do ESTADO-RESUMO. Derrogação de governação registada. Decisão expressa do aluno.

## [2026-07-09] ingestão | Ficha da UC — Introdução ao Direito (FDUP, 2025-2026)
- Fonte admitida: institucional (ficha oficial SIGARRA, captura 2026-07-09), hash_raw registado. Caminho curto. Estado: verificado.
- Páginas tocadas: [[Fontes/Ficha da UC — Introdução ao Direito (FDUP, 2025-2026)]], [[Faculdades/FDUP — Direito]] (criada: programa de 28 pontos transcrito, cobertura 0), [[Faculdades]].
- Contradições: nenhuma. Lacunas: datas de avaliação não constam da ficha.

## [2026-07-09] ingestão | Página da UC — Introdução ao Estudo do Direito (Católica Porto, captura 2026-07-09)
- Fonte admitida: institucional (página oficial FD-Porto, captura 2026-07-09), hash_raw registado. Caminho curto. Estado: verificado.
- Páginas tocadas: [[Fontes/Página da UC — Introdução ao Estudo do Direito (Católica Porto, captura 2026-07-09)]], [[Faculdades/Católica Porto — Direito]] (criada: 7 Partes transcritas, cobertura 0), [[Faculdades]].
- Contradições: nenhuma. Lacunas: ano, semestre, regência, bibliografia e avaliação ausentes da fonte — fila: obter ficha completa.

## [2026-07-09] ingestão | Ficha da UC — Introdução ao Estudo do Direito (Católica Lisboa, 2023-2024)
- Fonte admitida: institucional (ficha da UC, retrato datado 2023/2024), hash_raw registado. Caminho curto. Estado: verificado.
- Páginas tocadas: [[Fontes/Ficha da UC — Introdução ao Estudo do Direito (Católica Lisboa, 2023-2024)]], [[Faculdades/Católica Lisboa — Direito]] (criada: 15 pontos transcritos com leituras por secção, cobertura 0), [[Faculdades]].
- Contradições: nenhuma. Notas: numeração da ficha preservada com [sic] (Cap. II, Secção I sem § 1º); desalinhamento de anos lectivos entre vistas sinalizado.

## [2026-07-09] ingestão | Programa — Introdução ao Estudo do Direito I, Turma A (FDUL, 2025-2026)
- Fonte admitida: institucional (programa da Turma A, regente José Alberto Vieira), hash_raw registado. Caminho curto. Estado: verificado.
- Páginas tocadas: [[Fontes/Programa — Introdução ao Estudo do Direito I, Turma A (FDUL, 2025-2026)]], [[Faculdades/FDUL — Direito]] (criada: 19 pontos transcritos, numeração do original preservada com [sic], cobertura 0), [[Faculdades]].
- Contradições: nenhuma. Lacunas: ano, semestre, ECTS e avaliação ausentes; programa de IED II não incluído.

## [2026-07-09] ingestão | Página do Guia de Cursos — Introdução ao Direito e ao Pensamento Jurídico (NOVA, captura 2026-07-09)
- Fonte admitida: institucional (NOVA Guia de Cursos, edição 2021 — retrato datado), hash_raw registado. Caminho curto. Estado: verificado.
- Páginas tocadas: [[Fontes/Página do Guia de Cursos — Introdução ao Direito e ao Pensamento Jurídico (NOVA, captura 2026-07-09)]], [[Faculdades/NOVA School of Law — Direito]] (preenchida: 21 pontos transcritos com remissões FA/BM, cobertura 0), [[Faculdades]].
- Contradições: nenhuma. Erratas do original registadas na página de fonte («IGNOREes» por «fontes», confirmado visualmente; «compararando» [sic]). Lacunas: ficha do ano corrente por obter.

## [2026-07-09] ingestão | Baptista Machado, Introdução ao Direito e ao Discurso Legitimador — Fase 0 (admissão; leitura por começar)
- Obra admitida: doutrina-verificada (13.ª reimpressão, Almedina, Outubro de 2002; rosto e ficha técnica confirmados no PDF; existência confirmada por quatro fichas institucionais). hash_raw (PDF, o exemplar) e hash do derivado de leitura (MD da Oficina) registados.
- Probe de paginação feito (4 âncoras): folha N do PDF ↔ obra pp. 2N−4/2N−3; citação pela página da obra.
- Agenda de leitura e bloco panorâmico registados na página de fonte; mapa de tratamento fixado (núcleo I-VIII e X; periferia IX e XI). `progresso:` = leitura por começar (Cap. I a seguir).
- Não é ainda «fonte estudada»: nenhuma afirmação da obra entrou em páginas de conhecimento.

## [2026-07-09] ingestão | Baptista Machado, Introdução ao Direito e ao Discurso Legitimador — cap. I fechado (obra pp. 7-29)
- Leitura integral do capítulo no MD, confrontada com o PDF em todas as páginas (acima dos três spot-checks); citações literais conferidas carácter a carácter.
- Extracção no reservatório ([[Fontes/Baptista Machado, Introdução ao Direito e ao Discurso Legitimador]], secção Cap. I); relatos marcados (Rocher, Eisenstadt, Hauriou, Burdeau, Durkheim, Parsons, Luhmann, Weber, Mill, Winch, Henkel, Savigny em relato em Henkel).
- Propagação (ok do aluno): criada [[Conceitos/Instituição]] (verificado; monocamada). Vistas: FDUP ponto 1 e Católica Lisboa ponto 1 → monocamada (BM cap. I).
- Errata da conversão MD: 5 entradas em raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md (Ilse Schwidetzki; Anatol Rapoport; tomamos; título do § 9; ponto 12 omisso no índice gerado).
- Contradições: nenhuma. progresso: Cap. I de XI fechado; segue Cap. II.

## [2026-07-09] ingestão | Baptista Machado, Introdução ao Direito e ao Discurso Legitimador — cap. II fechado (obra pp. 31-62)
- Leitura integral no MD; confronto com o PDF nas pp. 31-43, 48-51 e 56-62 (todas as citações literais e referências normativas conferidas; spot-checks acima do mínimo).
- Extracção no reservatório (secção Cap. II da página de fonte); relatos marcados (Weber, Larenz, Esser, Le Fur apud Freund, Castanheira Neves, Freund, Kelsen, Tomás de Aquino, Herder, Luhmann, Hartmann, Henkel, Radbruch, Kant, Latorre); remissões normativas de 1982 (CRP, CP de 1886, art. 7º CC) marcadas datadas, sem conversão de memória.
- Propagação (ok do aluno): criadas [[Conceitos/Noção de Direito]], [[Conceitos/Coercibilidade]] e [[Conceitos/Segurança Jurídica]] (verificado; monocamada), cross-links com [[Conceitos/Instituição]]. Vistas: FDUP pontos 2, 4 e 5; Católica Porto Parte I; Católica Lisboa pontos 4 e 11; FDUL ponto 4 → monocamada.
- Erratas da conversão MD: +2 (HEROER→HERDER; l.Rbenswelt→Lebenswelt), total 7.
- Dúvida em aberto: «Castanheira Neves, ob. cit., pp. 353 e 359» (BM, p. 36) — obra do relato por identificar no exemplar.
- Contradições: nenhuma. progresso: Caps. I-II de XI fechados; segue Cap. III.

## [2026-07-09] ingestão | Baptista Machado, Introdução ao Direito e ao Discurso Legitimador — cap. III fechado (obra pp. 63-77)
- Leitura integral no MD; confronto com o PDF em todas as páginas do capítulo.
- Extracção no reservatório (secção Cap. III); panorâmica assumida pela fonte; datações marcadas (art. 8º CRP de 1982; Código Comercial; Concordata de 1940; quadro comunitário pré-adesão).
- **Errata da edição verificada em fonte primária**: «Tratado de Roma, de 25.4.1957» (p. 75) → 25 de Março de 1957 (EUR-Lex, CELEX 11957E); registada em «Erratas identificadas»; derivadas usam a data correcta.
- Propagação (ok do aluno): criadas [[Conceitos/Direito Objectivo e Direito Subjectivo]] e [[Conceitos/Ramos do Direito]] (verificado; monocamada). Vistas: FDUP pontos 3, 7 e 8; NOVA ponto 10 (primeiro da NOVA); Católica Porto Parte II → monocamada.
- Erratas da conversão MD: +1 («fome»→«fonte», p. 70), total 8.
- Contradições: nenhuma. progresso: Caps. I-III de XI fechados; segue Cap. IV.

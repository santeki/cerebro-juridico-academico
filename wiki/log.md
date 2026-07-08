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

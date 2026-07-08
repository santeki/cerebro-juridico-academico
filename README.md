# Segundo Cérebro Jurídico Académico

Wiki jurídica viva, construída e mantida por um agente Claude, ao serviço de quem estuda Direito. O agente lê fontes que tu curas, integra-as num corpo de conhecimento interligado, mantém as referências cruzadas e a coerência, e responde a perguntas a partir desse corpo — nunca a partir da memória do modelo.

Não é RAG. Em RAG o modelo redescobre o conhecimento a cada pergunta. Aqui o conhecimento compila-se uma vez e mantém-se actual: as referências cruzadas já lá estão, as contradições já foram assinaladas, a síntese já reflecte tudo o que se leu. A wiki cresce e ganha densidade a cada fonte ingerida e a cada pergunta respondida.

A arquitectura sintetiza três linhagens. Do **padrão de wiki** (Karpathy) vem o esqueleto: a base que compõe valor em vez de o re-derivar, as três camadas, o índice e o log. Do **sistema agêntico de produção** (Augusta Labs) vem a disciplina: camadas com fronteiras e charter de regras priorizadas. Do **Nomos** — segundo cérebro de Direito Português — vem a substância jurídica: o trabalho do jurista em três planos e três lentes, a tipologia de relações entre fontes (Eixo B), a estrutura de nota em três blocos, o tratamento de vigência e vacatio, o Examinador socrático ligado ao calendário das cadeiras.

## Para quem é

Para o aluno — que estuda em método (cartografia → estrutura → síntese → casos → revisão espaçada → conexões transversais), prepara exames, constrói fichas de revisão e mapeia institutos. Ver `playbooks/aluno.md`. O material de ensino — programas, slides, enunciados, correcções-modelo — entra como fonte e objecto de estudo; quem ensina não é utilizador deste cofre.

O cofre serve **várias faculdades sobre um corpo único**. O conhecimento — institutos, conceitos, doutrina — constrói-se uma vez e é agnóstico à faculdade; cada faculdade tem uma vista (`wiki/Faculdades/<Faculdade>.md`) que mapeia as suas cadeiras a esse corpo. É o que permite, no negócio de explicações, apoiar alunos de faculdades diferentes sem duplicar a matéria — e estudar a mesma matéria vista por mais do que uma escola numa só página.

## As três camadas

1. **`raw/`** — fontes imutáveis que tu colocas (manuais, monografias, artigos, legislação, acórdãos, apontamentos, e material de avaliação — exames, casos práticos, testes, correcções-modelo — em `raw/<Faculdade>/<Ano>/<Semestre>/<Cadeira>/Avaliação/`). O agente lê, nunca escreve. Fonte da verdade.
2. **`wiki/`** — o corpo gerado pelo agente: páginas de institutos, conceitos, doutrina, jurisprudência, legislação, sínteses de fonte, temas, debates, fichas de revisão, e a componente prática (`wiki/Avaliação/`: fontes de avaliação reais e casos práticos de treino). O agente é dono desta camada. Tu lês; o agente escreve.
3. **O *schema*** — `CLAUDE.md` (charter e regras), `CONVENCOES.md` (paths e nomenclatura), e os protocolos (`PROTOCOLO-INGESTAO.md` — Eixo A; `PROTOCOLO-ANALISE-COMPARATIVA.md` — Eixo B; `PROTOCOLO-CONSULTA.md`; `PROTOCOLO-AUDITORIA.md`), mais os `playbooks/` (aluno, examinador, modos analíticos). É o que faz do agente um bibliotecário disciplinado e não um chatbot genérico.

## As operações

- **Captura rápida (inbox)** — uma dúvida ou intuição que ocorre no momento entra com fricção mínima em `wiki/Inbox/`, para ser triada depois. O degrau de baixo do sistema: sem ele, o que não chega como fonte formal perde-se. Ver `PROTOCOLO-CAPTURA.md`.
- **Eixo A — estudo de fonte (ingestão)** — colocas uma fonte em `raw/` e mandas o agente processá-la. A **cobertura é sempre integral**: toda a fonte se lê do início ao fim, sem amostragem. O que se gradua é o **tratamento** de cada secção — núcleo (a fundo: citações com página, nota própria, Eixo B), periferia relevante (sumário fiel e mapa), contexto (sumário curto). Uma leitura parcial é consulta, não ingestão, e não sustenta cobertura. Fontes de áudio, vídeo e web entram por um sub-fluxo próprio (`PROTOCOLO-MULTIMEDIA.md`). Ver `PROTOCOLO-INGESTAO.md`.
- **Eixo B — análise comparativa** — quando várias fontes tratam o mesmo conceito, o agente classifica a relação entre as posições e percorre os Comparativos. Ver `PROTOCOLO-ANALISE-COMPARATIVA.md`.
- **Consulta** — perguntas contra a wiki; as boas respostas voltam à wiki como páginas novas. Ver `PROTOCOLO-CONSULTA.md`.
- **Auditoria** — verificação de saúde em quatro planos (fidelidade à fonte · proveniência · raciocínio · vertente geradora). Ver `PROTOCOLO-AUDITORIA.md`.
- **Backup e recuperação** — versionamento com git, réplica remota e snapshots: a memória de trabalho não se perde. Ver `PROTOCOLO-BACKUP.md`.
- **Painel de ritmo vivo** — um retrato, regenerado a cada sessão, do que rever hoje (revisão espaçada), das lacunas em aberto e da fila de ingestão face aos exames. Ver `PROTOCOLO-PAINEL.md`.
- **Vigia e voz** — gatilhos que o cofre acompanha (revisão devida, exame próximo, fonte nova), com a ressalva de dependerem de agendamento (`PROTOCOLO-GATILHOS.md`); e um fingerprint do teu estilo que os produtos de trabalho seguem sem nunca comprometer o rigor (`PROTOCOLO-VOZ.md`).

O calendário das cadeiras (`wiki/Faculdades.md`) e o Examinador socrático (`playbooks/examinador.md`) ligam o estudo às datas de avaliação e ao diagnóstico de cobertura.

## A regra que precede todas as outras

**Proveniência verificada.** Nenhuma afirmação substantiva da wiki provém da memória do modelo. Norma, jurisprudência, doutrina, facto, data, número, referência — tudo assenta em fonte verificada e ancorável. Na dúvida: sinalizar «verificação em aberto», marcar como senso comum assumido (só para o genuinamente consensual), ou omitir. Menos conteúdo verificado é sempre superior a mais conteúdo com risco de erro. Ver regra 1 do `CLAUDE.md`.

## Arranque

1. Abre a pasta como projecto no Cowork (ou aponta o teu agente Claude para ela).
2. Envia o prompt de arranque do kit: o agente apresenta a edição (`EDICAO.md`), configura-te em conversa e mostra o semáforo da certificação de arranque.
3. Pede — uma sebenta, um treino do Examinador, o painel. A leitura séria chega em documento (`PROTOCOLO-PRODUCAO.md`).

O diálogo é a interface; os produtos são a leitura; a wiki é a memória do agente — e mantém-se, por invariante, um vault Obsidian válido, para quem quiser abrir a janela.

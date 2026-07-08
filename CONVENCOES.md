# CONVENCOES.md

Paths canónicos e regras de nomenclatura. Toda a operação sobre esta pasta segue estas convenções. Fonte da verdade: se um protocolo ou template contradisser este ficheiro, está errado o protocolo.

---

## Layout da pasta

```
cerebro-juridico-academico/
├── CLAUDE.md                       # memória-charter (ler primeiro)
├── CONVENCOES.md                   # este ficheiro
├── CERTIFICACAO.md                 # bateria de certificação do agente (instrumento do aluno)
├── PROTOCOLO-PRODUCAO.md           # do conteúdo ao produto (documentos com identidade)
├── PROTOCOLO-EMPACOTAMENTO.md      # da instância de referência à edição distribuída
├── EDICAO.md                       # rótulo da edição distribuída (preenchido na origem)
├── PROTOCOLO-INGESTAO.md           # Eixo A — estudo de fonte
├── PROTOCOLO-ANALISE-COMPARATIVA.md # Eixo B — comparação de fontes sobre um conceito
├── PROTOCOLO-CONSULTA.md           # responder a partir da wiki
├── PROTOCOLO-AUDITORIA.md          # verificação de saúde em quatro planos
├── PROTOCOLO-CAPTURA.md            # captura rápida (inbox)
├── PROTOCOLO-MULTIMEDIA.md         # ingestão de áudio, vídeo e web
├── PROTOCOLO-PAINEL.md             # painel de ritmo vivo
├── PROTOCOLO-GATILHOS.md           # vigia proactiva
├── PROTOCOLO-BACKUP.md             # versionamento e recuperação
├── PROTOCOLO-EQUIPA.md             # camadas de agentes e revisão dupla
├── PROTOCOLO-VOZ.md                # fingerprint de estilo
├── README.md                       # apresentação do cofre
│
├── raw/                            # fontes imutáveis (o agente lê, nunca escreve)
│   ├── <Faculdade>/                # ex.: NOVA School of Law/
│   │   └── <Ano>/                  # ex.: 2.º Ano/
│   │       └── <Semestre>/         # ex.: 1.º Semestre/
│   │           └── <Cadeira>/      # ex.: Direito Constitucional Português/
│   │               ├── Programa/
│   │               ├── Slides/
│   │               ├── Sebentas/           # sebentas e apontamentos
│   │               ├── Doutrina/           # textos indicados para a cadeira
│   │               ├── Legislação/         # diplomas de trabalho da cadeira
│   │               ├── Jurisprudência/     # acórdãos convocados pela cadeira
│   │               ├── Avaliação/          # exames, testes, frequências, correcções-modelo
│   │               └── Casos Práticos/
│   ├── Biblioteca/                 # obras e fontes transversais a cadeiras
│   │   ├── Doutrina/
│   │   │   ├── Livros/             #   └── <Autor>/
│   │   │   ├── Monografias/
│   │   │   ├── Capítulos/
│   │   │   ├── Artigos/
│   │   │   └── Pareceres/
│   │   ├── Legislação/
│   │   │   ├── Constituição/
│   │   │   ├── Códigos/            #   └── Versões Históricas/
│   │   │   ├── Códigos Anotados/
│   │   │   ├── Leis da Assembleia da República/
│   │   │   ├── Decretos-Lei do Governo/
│   │   │   ├── Portarias/
│   │   │   └── Trabalhos Preparatórios/
│   │   └── Jurisprudência/         # por tribunal
│   │       ├── Tribunal Constitucional/
│   │       ├── Supremo Tribunal de Justiça/
│   │       ├── Supremo Tribunal Administrativo/
│   │       ├── Tribunais da Relação/   #   Lisboa, Porto, Coimbra, Guimarães, Évora
│   │       └── Tribunais Centrais Administrativos/  # Norte, Sul
│   ├── Multimédia/                 # Áudio, Vídeo, Web (ingere-se a partir de transcrição)
│   └── Assets/                     # imagens e anexos das fontes
│
├── wiki/                           # corpo gerado pelo agente
│   ├── index.md                    # catálogo de conteúdo
│   ├── log.md                      # registo cronológico append-only
│   ├── telemetria.md               # convocações por operação: o que se lê (PROTOCOLO-PAINEL, Frente 4)
│   ├── Inbox/                      # captura rápida (notas fugazes por processar)
│   ├── Faculdades.md               # índice de vistas por faculdade
│   ├── Faculdades/                 # uma vista curricular por faculdade (Ano → Semestre → Cadeira)
│   ├── Institutos/                 # uma página por instituto (estrutura em três blocos)
│   ├── Conceitos/                  # conceitos mais estreitos
│   ├── Doutrina/                   # uma página por autor/obra
│   ├── Jurisprudência/             # uma página por acórdão relevante
│   ├── Legislação/                 # uma página por diploma/conjunto de normas
│   ├── Fontes/                     # síntese (reservatório) de cada fonte ingerida
│   ├── Temas/                      # visão de cadeira/matéria
│   ├── Debates/                    # divergências doutrinárias vivas (tipologia §3.4)
│   ├── Revisão/                    # fichas de revisão espaçada
│   ├── Avaliação/                  # componente prática: fontes de avaliação reais + casos de treino
│   └── Auxiliares/                 # templates auxiliares (sebenta, distinção, linha jurisp., etc.)
│
├── modelos/                        # templates de página (o schema de cada tipo)
├── playbooks/                      # regras curadas por humano
├── identidade/                     # identidades visuais instaladas (curadas pelo aluno; ver identidade/LEIA-ME.md) (o agente lê, nunca escreve)
└── archive/                        # histórico rotacionado
```

As pastas curriculares criam-se quando o material entra — não se criam vazias. Regra de arrumação em `raw/`: o material da cadeira (programa, slides, sebentas, textos distribuídos pelo docente, enunciados e correcções, casos práticos) vive na pasta da cadeira; a obra ou fonte que sirva mais do que uma cadeira vive na `Biblioteca/`; em dúvida, entra na cadeira que motivou a entrada — a página de fonte na wiki regista o caminho, e mover mais tarde é legítimo desde que a página se actualize.

## Regras de path

1. **Conteúdo vivo** em `wiki/` e subpastas. `index.md`, `log.md` e `Faculdades.md` na raiz de `wiki/`.
2. **Fontes** em `raw/`, organizadas pela árvore curricular (Faculdade → Ano → Semestre → Cadeira → tipo de fonte) e pela `Biblioteca/` para o transversal a cadeiras. O agente lê de `raw/` e nunca lá escreve. Correcção de fonte faz-se fora do sistema e re-ingere-se.
3. **Templates** em `modelos/`: o agente copia a forma, não o ficheiro.
4. **Playbooks** em `playbooks/`: curados por humano; o agente lê, nunca escreve.
5. **Histórico rotacionado** em `archive/`. Não se consulta em ingestões normais.

## Notas transversais vs aplicações de ramo (o Direito é sistema)

Princípios, institutos e conceitos transversais (boa-fé atravessa Civil, Comercial, Administrativo; proporcionalidade atravessa Constitucional, Administrativo, Penal) vivem como página canónica única na categoria respectiva de `wiki/` — uma e só uma página por conceito. A categoria (princípio, instituto, conceito) vive no frontmatter, é plural e mutável: a classificação que cada fonte dá regista-se, sem mover o ficheiro.

A aplicação de um conceito a um ramo concreto (`boa-fé contratual`) é página própria que liga de volta à transversal. Teste: trata «o que é X» → página transversal; trata «como X opera no ramo Y» → página de aplicação. Promoção de aplicação a transversal quando o conteúdo cita ≥ 2 ramos ou duplica outras aplicações do mesmo conceito.

**Homonímia inter-ramo.** Dois conceitos diferentes com o mesmo nome (dolo civil vs dolo penal) desambiguam-se com sufixo entre parêntesis — p. ex., `Dolo (Civil).md`, `Dolo (Penal).md`, e uma página `Dolo.md` de desambiguação com contraste sintético. Cross-linking obrigatório entre as três.

## Nomenclatura de páginas

- Pastas e ficheiros de conteúdo — em `raw/` e em `wiki/` — usam capitalização natural portuguesa, com espaços e acentos preservados. Ex.: `wiki/Institutos/Princípio da Proporcionalidade.md`, `raw/Biblioteca/Jurisprudência/Supremo Tribunal de Justiça/`.
- Ficheiros de máquina mantêm nome técnico e não se naturalizam: `CLAUDE.md`, `CONVENCOES.md`, `PROTOCOLO-*.md`, `modelos/`, `playbooks/`, `index.md`, `log.md`, os ficheiros de serviço em maiúsculas (`GLOSSARIO.md`, `PAINEL.md`, `ESTADO-RESUMO.md`, `MELHORIA.md`, `GATILHOS.md`, `SUPRESSAO-LIST.md`, `VOZ-FINGERPRINT.md`) e o sufixo funcional `-RESUMO`.
- Doutrina (página de autor): nome completo natural. Ex.: `wiki/Doutrina/José de Oliveira Ascensão.md`.
- Jurisprudência: `Acórdão <Tribunal> n.º <n>-<ano>, de <data por extenso>.md`. Ex.: `wiki/Jurisprudência/Acórdão TC n.º 353-2012, de 5 de Julho de 2012.md`. O número de processo usa hífen no lugar da barra.
- Legislação: pelo nome natural do diploma ou do artigo. Ex.: `wiki/Legislação/Código Civil.md`, `wiki/Legislação/Artigo 483.º CC.md`.
- Vista de faculdade: `<Faculdade> — <Curso>.md` em `wiki/Faculdades/`. Ex.: `NOVA School of Law — Direito.md`.
- Fonte de avaliação: `<Cadeira> — <Docente> — <Ano> — <Tipo>.md` em `wiki/Avaliação/`. Ex.: `Direito Civil II — {Docente} — 2024 — Exame de Recurso.md`. O docente entra no nome porque o padrão de avaliação é por docente.
- Caracteres proibidos em nomes de ficheiro: `/ \ : * ? " < > |` — substituem-se por hífen; vírgulas, pontos ordinais (º), travessões e acentos são permitidos e desejados quando naturais.
- Os valores de `tipo:` e dos demais campos de frontmatter são vocabulário de máquina — minúsculas, hífenes, sem acentos (`fonte-avaliacao`, `linha-jurisprudencial`) — e não se naturalizam: a naturalização vale para nomes de pastas e de ficheiros de conteúdo, não para o schema.


**Separação corpo / vista (multi-faculdade).** As páginas de conhecimento — instituto, conceito, doutrina, fonte — são o corpo, e nomeiam-se sempre pelo instituto ou conceito jurídico, **nunca** pela cadeira ou pela faculdade. O nome da cadeira, a terminologia local, o ano e o docente são atributos da vista (`wiki/Faculdades/<Faculdade>.md`), não da página. O mapeamento cadeira↔páginas é de muitos-para-muitos: a mesma página de «Abuso do Direito» pode ser apontada pela cadeira agregadora de uma faculdade e pela cadeira mais estreita de outra, via wikilink, sem que a página saiba quantas vistas a invocam. Servir mais faculdades é acrescentar vistas, nunca duplicar o corpo.

## Frontmatter (YAML) obrigatório por página

```yaml
---
tipo: instituto | conceito | doutrina | jurisprudencia | legislacao | fonte | tema | debate | revisao | sebenta | distincao | linha-jurisprudencial | cronologia | mapa-conceptual | caso-pratico | fonte-avaliacao | captura | voz | painel | gatilhos | melhoria | lista-supressao | glossario | estado-resumo | vista-faculdade
titulo: "Título canónico com acentos"
categoria: [Princípio, Instituto, ...]   # classificação(ões) que as fontes dão; plural, mutável
ramo: [civil, comercial, ...]
estado_verificacao: verificado | parcial | em-aberto
cobertura: integral   # invariante: fonte ingerida é lida do início ao fim; o tratamento por secção (núcleo/periferia/contexto) regista-se na página de fonte
relacao: complementares | compativeis | distintas | em-conflito   # quando ≥ 2 fontes tratam o conceito (Eixo B)
estado_comparativo: aguarda-comparativo | comparativo-n-em-curso | comparativa   # ciclo do Eixo B
revisao_ultima: AAAA-MM-DD          # para institutos e conceitos: revisão espaçada (PROTOCOLO-PAINEL.md)
revisao_intervalo: 1                 # dias até à próxima revisão; expande com o sucesso (1→3→7→16→35)
revisao_proxima: AAAA-MM-DD          # = revisao_ultima + revisao_intervalo; o painel lê este campo
fontes: ["[[Fontes/...]]", ...]
ultima_actualizacao: AAAA-MM-DD
---
```

Campos só presentes quando aplicáveis (`relacao`, `estado_comparativo` em notas tocadas por mais de uma fonte). Páginas de legislação acrescentam os campos de vigência/vacatio (ver `modelos/modelo-legislacao.md`). Páginas de fonte acrescentam `fiabilidade:` (primaria-oficial | doutrina-verificada | institucional | apontamento-proprio) e `procedencia:` (edicao | local) — ver `modelos/modelo-fonte.md`. Campo transversal opcional em qualquer página: `triangulacao_pendente:` — fonte primária por obter, na citação por fonte secundária inacessível (`PROTOCOLO-INGESTAO.md`).

**Granularidade das páginas — quando nasce página própria.** Um conceito ganha página própria quando tem operação jurídica autónoma — jurisprudência dedicada, doutrina dedicada, regime próprio, ou atravessa ramos; sim a qualquer destas → página. Quando a sua existência se esgota como tipologia interna de outra (elementos, modalidades, classificações), vive como secção dessa página, nunca como página-satélite rala. E entre o instituto canónico e a página de aplicação de ramo, a fronteira é de conteúdo, com promoção regulada: a aplicação trata «como X opera no ramo Y» e remete ao canónico; quando passa a citar material de ≥ 2 ramos, ou a duplicar o que já vive noutra aplicação do mesmo conceito, o conteúdo desligado do ramo sobe ao instituto canónico — migra-se o transversal, reescreve-se a aplicação para o estritamente ramificado, actualizam-se as ligações, e a operação regista-se no log.

**Relações tipadas mínimas.** Nos blocos de conexões das páginas de instituto e de debate, o wikilink cuja natureza importe leva o tipo entre parênteses, de vocabulário fechado a três: *(contraria)*, *(concretiza)*, *(excepciona)* — p. ex., «[[Institutos/Abuso do Direito]] *(excepciona)*». Fora destes dois tipos de página, e sempre que a natureza nada acrescente, o link fica nu. A taxonomia completa de relações foi avaliada e recusada como peso morto; estes três existem porque no Direito a natureza do vínculo decide o argumento — contrariar, concretizar e excepcionar são movimentos diferentes com consequências diferentes. `estado_verificacao`: `verificado` exige cada afirmação ancorada; `parcial` sinaliza blocos por confirmar; `em-aberto` marca página de trabalho não citável.

Campo opcional em qualquer página: `revisto_pelo_aluno: AAAA-MM-DD` — regista a revisão humana. Página revista: as atribuições e classificações nela contidas tratam-se, em sessões futuras, como confirmadas pelo aluno à data indicada; alterações posteriores reabrem a revisão. A ausência do campo não rebaixa a página — a revisão é selectiva; a auditoria pode listar páginas nucleares nunca revistas, como informação, não como falha.

## Convenção tipográfica (house style)

PT-PT canónico, em toda a wiki:
- Aspas curvas «...» para citação literal breve em português.
- Itálico para termos ou expressões em língua estrangeira ou latim (*ratio decidendi*, *Drittwirkung*).
- Citação literal em língua estrangeira: aspas curvas e itálico cumulativamente, ou bloco `>` quando longo.
- Travessões com espaços ( — ) para incisos. Hífenes para palavras compostas. (Ao contrário do sistema da Augusta Labs, aqui os travessões são correctos e esperados — pontuação canónica do PT-PT.)
- Ordinais º/ª solto, sem ponto: «art. 483º», «3.ª edição».
- O leitor distingue instantaneamente texto da fonte (citação) de texto do agente (paráfrase/síntese).

**Prosa contínua nos produtos de leitura.** Respostas desenvolvidas, sebentas e documentos escrevem-se em prosa corrida, para leitura fluida por estudante, docente ou profissional. A paráfrase fiel, por palavras próprias, é a forma por defeito da exposição; a citação literal «...» reserva-se para as fórmulas em que a letra pesa — definições canónicas, formulações que o exame recompensa palavra a palavra. As referências de página agregam-se no fim do parágrafo ou da unidade de sentido — (Autor, pp. X-Y) —, nunca intercaladas cláusula a cláusula: texto costurado de fragmentos citados com âncora a cada oração é mosaico, não prosa. A ancoragem fina, frase a frase, mantém-se integral na camada de conhecimento — páginas de fonte e notas —, que é onde a verificação vive; o produto de leitura remete para ela, não a transporta toda. Nada disto afrouxa a regra-âncora: a fidelidade garante-se pela verificação contra a fonte, não pela transcrição em mosaico.

Pareceres de órgãos com função consultiva ou para-jurisdicional — Comissão Constitucional, Procuradoria-Geral da República, entidades reguladoras — têm peso quasi-primário: a página segue a ficha de jurisprudência adaptada (`modelos/modelo-jurisprudencia.md` — órgão, n.º e data do parecer, relator quando exista, declarações de voto), com tipo `jurisprudencia`, não a página de autor. Em `raw/`, o arquivo pode manter-se em `Doutrina/Pareceres/`.

## Ficheiros de navegação

- `index.md`: catálogo por categoria, cada página com link e uma linha de resumo. Actualizado a cada ingestão.
- `log.md`: cronológico, append-only. Prefixo canónico parseável: `## [AAAA-MM-DD] Tipo | descrição`. Tipos em `wiki/log.md`.
- `ESTADO-RESUMO.md`: fotografia podada do conhecimento (contagens por categoria, notas-âncora, deltas recentes), regenerada a cada passagem com tecto ≤ 30 KB. Fonte de leitura à entrada de consultas **à escala** — quando `index.md` ultrapassa o seu orçamento; enquanto a wiki é pequena, fica vazio e lê-se o índice directamente. Destila `index.md` + `log.md`, nunca os modifica. Distinto do painel (acção) e do índice (catálogo completo).

## Sufixos funcionais de nomenclatura

Importado da convenção da Augusta, onde o nome do ficheiro codifica o seu comportamento — útil para o agente saber, só pelo nome, como tratar um ficheiro. Os ficheiros de serviço do cofre seguem-na:

- **`-LOG`** / `log.md` — append-only; nunca se reescreve, só se acrescenta (`log.md`).
- **`-QUEUE`** — máquina de estados com coluna de estado; cada linha percorre estados (não há ficheiros `-QUEUE` no académico; o conceito vive no inbox de captura).
- **`-LIST`** — registo cumulativo filtrável (`SUPRESSAO-LIST.md`).
- **`-TRACKER`** / painel — estado corrente, reescrito a cada passagem (`PAINEL.md`, `MELHORIA.md` na vertente tracker).
- **`-RESUMO`** — destilação podada de uma fonte que cresce, reescrita por inteiro a cada passagem e sujeita a tecto de tamanho (`ESTADO-RESUMO.md`, regenerado de `index.md` + `log.md`). Difere de `-TRACKER` por destilar à escala com aparo por tamanho; difere de `-LOG` por não acumular.
- **`-PLAYBOOK`** / `playbooks/` — regras curadas por humano; o agente lê, nunca reescreve sem aprovação.
- Páginas de conhecimento (instituto, conceito, fonte, etc.) não levam sufixo funcional — o `tipo` no frontmatter cumpre esse papel.

Um nome canónico por conceito; não coexistem dois ficheiros para a mesma coisa.

## Orçamentos de tamanho

| Ficheiro | Limite mole | Acção ao exceder |
|---|---|---|
| Qualquer página de `wiki/` | 40 KB | Cindir em sub-páginas com links, ou extrair sub-instituto. |
| Nota de instituto | 8.000 palavras OU 12 fontes activas | Fissão por sub-conceito; nota original vira índice (overview) com remissões. |
| `index.md` | 60 KB | Migrar índices por categoria; deixar `index.md` como mapa. Acima deste limite, passar a ler `ESTADO-RESUMO.md` à entrada das consultas (fotografia podada), descendo ao índice completo só quando preciso. |
| `log.md` | 200 KB | Rotacionar entradas > 12 meses para `archive/log-AAAA.md`. |

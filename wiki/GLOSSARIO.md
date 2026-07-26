---
tipo: glossario
titulo: "Glossário canónico"
estado_verificacao: em-aberto
ultima_actualizacao: 2026-06-28
---

# Glossário canónico

> Termos técnicos **do sistema** (não do Direito substantivo), com definição operativa. Em caso de ambiguidade sobre o que um termo significa dentro do cofre, prevalece a definição aqui fixada. Cada termo remete para o protocolo onde vive. Importado do glossário do schema Nomos (§12), adaptado à arquitectura modular destes cofres.

## Ingestão e tratamento
- **Cobertura integral** — invariante: toda a fonte que entra na wiki lê-se do início ao fim, sem amostragem (`PROTOCOLO-INGESTAO.md`). Uma fonte parcialmente lida não foi ingerida.
- **Consulta** — leitura dirigida a um ponto isolado de uma fonte; acto de pesquisa legítimo, mas **não** é ingestão: não gera página de fonte coberta, e o que dela se aproveita marca-se como vindo de fonte não ingerida.
- **Tratamento (núcleo / periferia / contexto)** — graduação do esforço de extracção por secção de uma fonte integralmente lida. Núcleo: citação literal onde a letra pesa e paráfrase ancorada no restante, promoção a nota, Eixo B. Periferia relevante: sumário fiel e mapa de conceitos. Contexto: sumário curto. Gradua a extracção, nunca a cobertura nem a verificação.
- **Eixo A** — processo de estudo de uma fonte (`PROTOCOLO-INGESTAO.md`).
- **Eixo B** — análise comparativa de um conceito tratado por várias fontes (`PROTOCOLO-ANALISE-COMPARATIVA.md`).
- **Leitura / página de fonte** — ficheiro em `wiki/Fontes/` que digere uma fonte com fidelidade máxima e âncora; **reservatório** das notas. As notas extraem da leitura, nunca do PDF.
- **Nota / página de entidade** — ficheiro que sistematiza um princípio, instituto, conceito ou ideia a partir de todas as fontes que o tratam; **selectiva** (convoca da leitura só o que ilumina).

## Postura e rigor
- **Três lentes** — professor (construção dogmática), advogado (operatividade), juiz (critério de decisão); ferramenta interna, não rótulo a expor. A lente professor nomeia a função científica; o professor não é utilizador deste cofre.
- **Três planos** — captação/descrição (1), sistematização/explicação (2), aplicação (3).
- **N1 / N2 / N3** — graus de verificabilidade de atribuição doutrinária: N1 verificável externamente, cita-se com fonte; N2 convergência forte em fontes secundárias, atribui-se com marcador; N3 frágil, omite-se sem confirmação.
- **Ancoragem** — cada afirmação substantiva ligada à sua fonte (norma com diploma/artigo/versão; doutrina com autor/obra; jurisprudência com tribunal/data/processo/ECLI).
- **Marcador de incerteza** — sinalização de dúvida ou verificação em aberto, que vive na frase onde a afirmação ocorre, não em nota diferida.
- **Vacatio** — período entre publicação e entrada em vigor de uma norma; confirma-se a vigência antes de citar.
- **Doutrina datada** — obra que trata redacção anterior à vigente; cita-se com ressalva expressa de desalinhamento.

## Relação entre fontes (Eixo B)
- **Relação inter-fontes** — classificação da relação entre posições sobre o mesmo conceito: complementares, compatíveis, distintas, em conflito.
- **Comparativo N** — passo do Eixo B (inventário, reposicionamento, mapeamento, porquê, consequências, tradição, síntese).
- **Sebenta** — reorganização juridicamente estruturada da matéria de uma obra, por institutos e conceitos; ficheiro irmão da leitura.

## Captura, ritmo e voz
- **Captura / inbox** — degrau de baixa fricção por onde entra conhecimento sem forma de fonte formal (`PROTOCOLO-CAPTURA.md`).
- **Triagem** — passo que decide o destino de cada captura (nota, tarefa de ingestão, descarte).
- **Revisão espaçada** — reapresentação de páginas a intervalos crescentes (1→3→7→16→35 dias), gerida pelo painel.
- **Painel** — retrato do agora, reescrito a cada passagem: o que rever, lacunas, fila de ingestão (`PROTOCOLO-PAINEL.md`).
- **Gatilhos** — sinais que o cofre vigia (revisão devida, exame próximo, fonte nova), com registo de resultados (`PROTOCOLO-GATILHOS.md`).
- **Voz / fingerprint** — registo canónico do estilo de escrita do utilizador, derivado de amostras reais; molda a forma, nunca a substância (`PROTOCOLO-VOZ.md`).
- **Supressão** — memória do que foi recusado em definitivo, para não voltar a ser proposto (`wiki/SUPRESSAO-LIST.md`).

## Estudo, manutenção e equipa
- **Examinador** — modo socrático que gera hipóteses, testa cobertura contra o programa das cadeiras (`playbooks/examinador.md`).
- **Faculdades** — índice (`wiki/Faculdades.md`) e vistas curriculares (`wiki/Faculdades/`): cadeiras por ano e semestre, programa, docentes e datas de avaliação; alimenta a priorização e o diagnóstico de cobertura.
- **Auditoria / lint** — verificação periódica de saúde da wiki, com vertente qualitativa e quantitativa (`PROTOCOLO-AUDITORIA.md`).
- **Índice (`index.md`)** — catálogo do estado presente, orientado a conteúdo. Lê-se à entrada de qualquer consulta.
- **Log (`log.md`)** — registo cronológico, append-only, com prefixos parseáveis.
- **Camada de agentes** — captação, sistematização e rigor, estudo e manutenção; a equipa de papéis cresce por necessidade observada, não por enumeração antecipada (`PROTOCOLO-EQUIPA.md`).
- **Automação suspensa** — aparato de escrita automática não-supervisionada (triplo gate, dupla fonte, circuit breaker, quarentena), descrito mas inactivo em regime supervisionado; reentra por decisão expressa (`PROTOCOLO-EQUIPA.md`).

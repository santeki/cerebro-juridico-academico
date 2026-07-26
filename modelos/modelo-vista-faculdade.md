---
tipo: vista-faculdade
titulo: "{Faculdade} - {Curso}"
faculdade: "{nome canónico da faculdade}"
curso: "{curso}"
norma_citacao: ""                # norma de referências dos produtos académicos (PROTOCOLO-VOZ) - p. ex., NP 405-1
ultima_actualizacao: AAAA-MM-DD
---

# {Faculdade} - {Curso}

> Vista curricular de uma faculdade sobre o corpo de conhecimento da wiki. Estrutura-se por **Ano → Semestre → Cadeira** e mapeia cada cadeira às páginas de instituto e de conceito que já existem - **não duplica conhecimento**. A mesma página (`[[Institutos/Abuso do Direito]]`) pode ser apontada por cadeiras de várias faculdades; o mapeamento cadeira↔páginas é de muitos-para-muitos. O que vive aqui é o currículo desta faculdade: que matéria cai em que cadeira, em que ano e semestre, com que docente, programa e avaliação. O corpo de conhecimento é partilhado e agnóstico à faculdade - esta vista é apenas um dos mapas que lhe apontam.
>
> Sequência de construção: de baixo para cima (Introdução ao Direito → ramos), com o calendário a prevalecer quando uma avaliação se aproxima. Uma fonte de cada vez (digestão integral, regra 10 do `CLAUDE.md`).

## {N.º} Ano

### {N.º} Semestre

#### {Cadeira}
- **Docente**: {nome} - {se tiver produção publicada sobre a matéria, ler primeiro essa produção antes de a sistematizar}.
- **Padrão de ensino do docente** (a leitura que perfilha - posições que adopta ou rejeita, ênfases, casos que privilegia -, **só de fonte verificada**: obra dele `[[Doutrina/...]]` ou apontamento de aula fiel `[[Fontes/...]]`; nunca por inferência sobre o que «provavelmente» defende): {a preencher. Cada posição com a sua fonte. Onde diverge da doutrina dominante, marcar ambas - para o exame conta a do docente, a maioritária diz X. Sem fonte verificada, fica vazio: não se preenche de memória.}
- **Avaliação**: {tipo - exame / frequência / trabalho} · **Data**: {AAAA-MM-DD}.
- **Bibliografia base**: {obras} → [[Fontes/...]].
- **Fontes da cadeira em `raw/`**: `raw/{Faculdade}/{Ano}/{Semestre}/{Cadeira}/` - o que já entrou, por tipo (Slides, Sebentas, Doutrina, Legislação, Jurisprudência, Avaliação, Casos Práticos).
- **Programa** (tópicos) → páginas de conhecimento que cobrem cada um:
  1. {tópico} - [[Institutos/...]] / [[Conceitos/...]] - cobertura: {coberto / parcial / lacuna}.
  2. {...}
- **Cobertura do programa**: {por sub-ponto: fontes que o cobrem (aulas/slides · cada obra · jurisprudência) e estado - coberto | monocamada | por cobrir | dispensada (razão, data, decisão do aluno). Actualiza-se no fecho de cada estudo; a auditoria de fecho lê esta secção; a fila alimenta-se dos «por cobrir» e «monocamada». Blocos selados levam aqui a linha `✔ ...` escrita pela auditoria de fecho (`PROTOCOLO-AUDITORIA.md`) - o estado agregado e datado que a consulta exibe na abertura.}
- **Histórico de avaliações**: {datas passadas e o que foi testado, por docente - alimenta o modo exame com o padrão real. Liga às fontes de avaliação ingeridas: [[Avaliação/...]].}

#### {Cadeira}
{...}

### {N.º} Semestre
{...}

## {N.º} Ano
{...}

## Fila de prioridade (desta faculdade)
{Ordem de estudo dentro desta faculdade: proximidade de avaliação × lacuna de cobertura × pré-requisitos. Uma fonte de cada vez. Não pondera contra outras faculdades - cada vista tem a sua fila.}

1. {Cadeira / matéria} - {razão: exame em N dias / lacuna crítica}.
2. {...}

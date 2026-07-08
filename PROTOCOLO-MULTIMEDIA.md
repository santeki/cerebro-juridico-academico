# PROTOCOLO-MULTIMEDIA.md — ingestão de áudio, vídeo e web

A maior parte das fontes é texto, mas nem toda: uma aula gravada, uma conferência académica, uma audição parlamentar, um post de blog jurídico. Estas fontes não se ingerem como um PDF, e tratá-las à pressa abre uma porta de erro — uma transcrição automática troca um nome de tribunal, confunde um latinismo, perde uma negação. Este sub-fluxo, importado dos cuidados de domínio do schema Nomos (§9), define como entram, sem baixar o rigor da cobertura integral nem da proveniência.

A regra de fundo não muda: a cobertura é sempre integral (a transcrição inteira lê-se, do início ao fim), o tratamento gradua-se por secção, e nenhuma afirmação se faz sem âncora. O que este protocolo acrescenta é o cuidado próprio de cada formato antes de a fonte poder ser tratada como reservatório fiel.

## Áudio e vídeo

Nunca se ingere a partir do áudio ou do vídeo bruto. Ingere-se a partir de uma **transcrição**, e o áudio/vídeo guarda-se como original em `raw/Multimédia/Áudio/` ou `raw/Multimédia/Vídeo/`, com a transcrição ao lado.

Geração da transcrição:
1. Transcrever por motor ASR de qualidade (Whisper ou equivalente).
2. Revisão humana mínima por amostragem: pelo menos 5% do texto cotejado contra o áudio, distribuído pelo corpo da gravação (não só o início), com correcção dirigida dos termos técnicos jurídicos — nomes de tribunais, designações de diplomas, latinismos, nomes de autores. É aqui que o ASR mais falha, e é o que mais custa caro numa nota.
3. Registar no frontmatter da transcrição: `transcricao_motor` (nome e versão), `transcricao_data` (data ISO), `transcricao_revisao_humana` (percentagem cotejada e responsável).

Estatuto da transcrição, em paralelo com o tratamento de OCR não verificado:
- **Transcrição não revisada** equivale a OCR não verificado. A leitura abre cada citação distintiva com o marcador `> **Transcrição não revisada:**`, e a triangulação fica diferida até à revisão.
- **Transcrição com revisão ≥ 5%** trata-se como reservatório fiel, sem prejuízo de marcar com `> **Áudio inaudível ou ambíguo:**` as passagens onde o som não permite certeza.

## Web

Uma página web é instável — muda, desaparece, perde-se. Não se ingere o URL: arquiva-se um **PDF impresso** da página em `raw/Multimédia/Web/`, e no frontmatter da leitura registam-se o URL e a data de captura. A fonte passa a ser o arquivo estável, não a página viva.

## E-pub e outros formatos

Converte-se para PDF, para uniformidade do pipeline de ingestão, antes de entrar pelo Eixo A.

## Articulação

Uma vez gerada a transcrição revista (áudio/vídeo) ou arquivado o PDF (web), a fonte segue o `PROTOCOLO-INGESTAO.md` como qualquer outra: cobertura integral, mapa de tratamento, extracção ancorada, propagação para as notas. Os marcadores de transcrição e de áudio ambíguo convivem com os marcadores de OCR e de dúvida de conteúdo já previstos no Eixo A.

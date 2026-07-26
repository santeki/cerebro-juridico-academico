# PROTOCOLO-PRODUCAO.md - do conteúdo ao produto

Como um produto da wiki - sebenta, mapa de instituto, ficha, resposta desenvolvida - se materializa em documento entregável (PDF, docx, pptx) com a identidade visual instalada e a voz do aluno. Os produtos são o canal principal de leitura do cofre: a conversa responde; o documento lê-se a sério.

## Pipeline

1. **Conteúdo** - nasce da wiki pelas regras de sempre: contrato do terreno na abertura (selo de bloco ou o que falta), proveniência, prosa contínua (`PROTOCOLO-CONSULTA.md`, `CONVENCOES.md`).
2. **Voz** - o fingerprint de estilo molda a forma textual (`PROTOCOLO-VOZ.md`).
3. **Identidade** - o manifesto da configuração, ou outro indicado no pedido; sem identidade instalada, o formato neutro do cofre.
4. **Geração** - por ferramenta de documento, com as fontes embebidas. Existindo template real da casa em `identidade/<Instituição>/templates/`, preenche-se o template em vez de gerar do zero - fidelidade máxima ao menor custo.
5. **Probe** - por código, a fonte efectivamente usada e as cores conferem-se contra o manifesto; a primeira página rasteriza-se e confronta-se com o exemplar. O literal verifica-o a máquina; o «passava por documento da casa» verifica-o o confronto - e o teu olho, na primeira produção de cada tipo.
6. **Entrega** - com ficha técnica discreta: edição e selo do terreno, data, identidade usada.

## Instalar uma identidade

Crias `identidade/<Instituição>/`, despejas o que tiveres - um PDF real da casa chega; manual de normas, logos, fontes e templates ajudam - e dizes «instala». O agente extrai o mensurável (fontes declaradas nos PDFs, cores amostradas em valores exactos, margens medidas) e escreve o `IDENTIDADE.md` com a origem de cada valor; o que os materiais não mostram assume-se com default sensato, marcado «assumido». **Zero perguntas na instalação**; a afinação acontece na primeira produção («assumi a posição do logo no rodapé e a margem de 2,5 cm — muda alguma coisa?»). Paragem única: fonte identitária sem ficheiro em `fontes/` - a substituição silenciosa por parecida é proibida; três saídas de um toque: enviar o ficheiro, aprovar um fallback concreto (fica registado no manifesto), seguir em formato neutro.

## Regra-âncora visual

Cores só pelos códigos do manifesto, nunca aproximadas a olho. Fontes exactas ou paragem sinalizada. Logos só dos ficheiros fornecidos - nunca redesenhados nem gerados. Campo em falta: assume-se com marca e declara-se; se identitário (logo, fonte), pergunta-se. Manutenção: substitui-se o ficheiro em `identidade/` e pede-se o diff - o agente propõe a actualização do manifesto contra o exemplar novo, datada.

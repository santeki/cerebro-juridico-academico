# PROTOCOLO-EMPACOTAMENTO.md - da instância de referência à edição

Como a instância de origem se transforma na cópia que um aluno recebe. Princípio: **o corpo inteiro embarca** - a completude na interligação morre no primeiro wikilink cortado; o recorte é a vista -, e `raw/` embarca com ele, para o passe de âncoras da cópia conferir contra a própria fonte.

## O que embarca, o que se reinicia, o que fica

Embarca `raw/` integral - com a excepção do exemplar cuja dimensão o `PROTOCOLO-BACKUP.md` põe fora do repositório, que se referencia pelo `hash_raw` da página de fonte e se entrega à parte; o corpo de `wiki/` (institutos, conceitos, doutrina, jurisprudência, legislação, debates, auxiliares, sebentas, avaliação), as vistas, o índice, o glossário e o `ESTADO-RESUMO`; o schema completo (charter, convenções, protocolos, playbooks, modelos); as ferramentas de verificação (`ferramentas/`, sob git - 6.26, item F); `CERTIFICACAO.md`; `identidade/` apenas com `LEIA-ME.md` e `_modelo/`.
Reiniciam na cópia o `log.md` (nasce com uma entrada-génese: «Edição {referência} gerada da instância {versão} a {data}»), o `PAINEL`, a `MELHORIA`, a `SUPRESSAO-LIST` (os ❌ são de quem opera) e o `Inbox`.
Ficam na origem o log operacional da instância; o bloco de configuração preenchido (a cópia parte do bloco-template vazio, para a conversa do destinatário); o `wiki/VOZ-FINGERPRINT.md` (a voz é do destinatário); e as identidades visuais instaladas.

## Geração do `EDICAO.md`

Os campos preenchem-se com valores reais: blocos selados (as linhas ✔ da vista, com datas e contagens), corpus (fontes em `raw/`, páginas, selos `revisto_pelo_aluno`), verificação do empacotamento (data do passe; domínios da bateria), e a regra de procedência e upgrades.

## Verificação final

UTF-8 em todos os `.md`; passe mecânico de âncoras global **verde**; **passe estrutural do esqueleto verde** (`PROTOCOLO-AUDITORIA.md`) - nenhuma remissão órfã, árvore fiel ao disco, enum e modelos coerentes, ponteiros vivos; coerência índice ↔ wiki ↔ log da cópia; bateria de origem corrida sobre os domínios que embarcam. Falha em qualquer ponto → não se empacota; corrige-se primeiro.

## Ensaio de edição

Condição de distribuição, não passo opcional: montar a cópia num ambiente virgem e percorrer o caminho do aluno - os três gestos do LEIA-ME, o prompt de arranque, a apresentação do `EDICAO.md`, a configuração em conversa, o semáforo, um primeiro pedido real (uma sebenta de bloco selado). O que falhar aqui falharia na primeira utilização; sem ensaio limpo, a edição não sai.

## Erratas e edição seguinte

As erratas recebidas das cópias (`PROTOCOLO-INGESTAO.md`, «Errata da edição») triam-se como achados de auditoria: confirmadas contra a fonte, corrigem-se na instância e incorporam-se na edição seguinte - que substitui a camada `procedencia: edicao` das cópias e preserva a local.

## Co-produção (limite declarado, v1)

Mais do que um produtor sobre a mesma instância: um de cada vez, sincronização por repositório git privado, selagem e empacotamento por uma só mão. O merge fino de contribuições simultâneas é fronteira conhecida, não capacidade escondida.

## Alimentar a linha profissional

O corpo teórico desta instância é a base teórica das edições profissionais: a transferência - o que entra, o que fica, as conversões - rege-se pelo `PROTOCOLO-EMPACOTAMENTO.md` do cofre profissional.

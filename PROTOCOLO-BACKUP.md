# PROTOCOLO-BACKUP.md - backup, versionamento e recuperação

A wiki é a memória de trabalho. Perdê-la é catastrófico - anos de leitura, síntese e conexões num só directório. Este protocolo fixa como se versiona, se replica e se recupera. É infra-estrutura, não funcionalidade: tem de existir antes de a wiki ter valor a perder.

A escrita do agente é, por si, prudente - não apaga, rota para `archive/`, regista no log. Mas isso protege contra o erro de edição, não contra a perda do disco, a corrupção do ficheiro ou o engano humano irreversível. Para isso, três camadas.

---

## Camada 1 - Versionamento (git)

O vault é texto: o git é o instrumento natural. Recomendado desde o primeiro dia.

- **Inicialização**: `git init` na raiz do vault. O `.gitignore` (incluído) exclui temporários e o que não deve ser versionado.
- **Cadência de commit**: ao fim de cada sessão de trabalho com valor (uma ingestão concluída, um Eixo B fechado, uma sessão de estudo). O agente pode propor o commit no fecho da operação, com mensagem que espelha a entrada de log: `ingestão: Hespanha, Cultura Jurídica Europeia` ou `Eixo B: boa-fé - Comparativo 6`. O commit é acto sobre o sistema, não sobre a realidade jurídica - não precisa de ✅, mas o agente nunca força reescrita de história (`--force`, rebase destrutivo) sem indicação expressa.
- **O que o git dá**: histórico completo, diferença entre versões, regresso a qualquer estado anterior, e a base para replicação remota.
- **Tags de versão**: a cada versão do schema (frontmatter do `CLAUDE.md`), uma tag - `v6.8`, `v6.9` - no commit que a fecha; o estado do cofre em qualquer versão recupera-se por nome.
- **Consulta ao passado como instrumento**: «como estava esta página quando emiti o parecer de Março» responde-se com `git log -- <página>` e `git show <tag|data>:<caminho>` - no cofre profissional, é a base material da coerência decisória; o agente pode consultar o histórico, nunca reescrevê-lo.

## Espelho local de trabalho (pasta ligada)

O cofre vive numa pasta local do aluno (`cofre/` - o vault com git - ao lado de `projecto/` - materiais de circulação - e de um LEIA-ME com o contrato). A conversa liga a pasta à sessão; o arranque faz *staging* do cofre e confirma HEAD e árvore limpa contra o doc de estado. O espelhamento não espera pelo fecho: cada commit com valor sai do contentor no acto, primeiro por `push` para o remoto e depois por escrita de volta, porque um commit que só vive no contentor deixa de existir quando o contentor é reciclado. A escrita de volta corre em dois passes. O passe 1 aplica: transporta-se um `git bundle` incremental do último commit espelhado até HEAD, com hash conferido nos dois lados, funde-se com `--ff-only` e repõe-se a árvore de trabalho. O passe 2 verifica sem confiar no primeiro: `git rev-parse HEAD` igual dos dois lados, hash do inventário de objectos (`git rev-list --objects HEAD | sort`) igual, hash da árvore do commit igual, e hash de conteúdo de dois ficheiros tocados na sessão. Divergência em qualquer um trava o fecho. O zip testado mantém-se como fallback de mobilidade e camada de salvaguarda, gerado no fecho. A edição manual na pasta continua fora do rasto (vault-janela-de-leitura). (Decisão de 2026-07-17.)

Nenhuma conversa fecha com lei ou conteúdo que existam apenas no contentor ou nos docs do projecto claude.ai (6.27, da perda dos commits da c29): o fecho exige o estado novo em pelo menos dois destinos duráveis e independentes - o remoto git e o zip entregue na conversa; a pasta local, quando o bridge o permita, é o terceiro -, e a falha de um destino escala o outro na mesma conversa, nunca difere para a seguinte. A credencial do push vive no gestor de credenciais do sistema ou em variável de ambiente do arranque, nunca em ficheiro dentro da pasta do projecto.

O exemplar cuja dimensão inviabilize o git vive fora do repositório, em `projecto/exemplares/` da pasta local, com o `hash_raw` da página de fonte como âncora de integridade que o passe mecânico confere - contra a pasta local quando o desktop está ligado, e contra a cópia de trabalho da sessão -; o zip de fallback não o transporta. (Decisão de 2026-07-17.)

Transporte entre a pasta e o workspace: por arquivo com hash conferido nos dois lados, em partes - ≤ 64 MB no *staging* para a sessão, ≤ 20 MB na escrita de volta (limites correntes do canal; conferem-se quando o canal mudar) -; os paths do bridge chegam em Unicode NFD e tratam-se por glob no shell, nunca por NFC escrito à mão. (Prática de 2026-07-17/18.) O bridge cria ficheiros, sobrescreve-os no lugar e renomeia dentro da própria pasta, mas não os elimina: `rm`, e a remoção implícita do destino num `mv` entre dispositivos, devolvem `Operation not permitted`. Daí que `git checkout` e `git merge` não consigam repor a árvore de trabalho na pasta ligada, porque o checkout desliga o ficheiro antigo antes de escrever o novo; a reposição faz-se por cópia de conteúdo sobre o ficheiro existente, com a ref escrita directamente em `.git/refs/heads/main`, e os ficheiros de bloqueio que o git deixe para trás afastam-se por `mv`, nunca por `rm`. (Apurado na c27.)

Disciplina de eficiência do arranque e da conversa (mandato expresso de 2026-07-18): cada conversa transporta **um único bloco de trabalho** - um fecho, um despacho de decisões, ou uma sessão de leitura; blocos não se empilham. O arranque lê os docs de sistema em **leituras concatenadas** e, mantendo-se os hashes iguais aos do commit de referência, a releitura integral obrigatória cobre o charter e os protocolos operativos do bloco do dia (CLAUDE, CONVENCOES, INGESTAO, ANALISE-COMPARATIVA, AUDITORIA, EQUIPA, PAINEL, BACKUP); os restantes ficam em **leitura-sob-uso** - lêem-se por inteiro quando a operação os convoque ou quando o hash tiver mudado. O **painel entrega-se como relatório intercalar no fim do arranque** e cada gate fecha com uma linha de reporte; silêncio prolongado é falha de operação, não sinal de rigor. As ferramentas de verificação por código (crivo estrutural; verificador global; crivo de citações; grafo; pré-processador) **vivem em `ferramentas/`, na raiz do cofre e sob git (6.26, item F), e correm-se - não se reconstroem** (ajuste de contrato propõe-se e regista-se; reconstrução de raiz é desperdício e fonte de deriva); renders e extracções de texto do exemplar pesado correm na própria pasta local (pdftoppm/pdftotext, 300 dpi), transportando-se apenas os derivados leves.

## Camada 2 - Replicação remota (off-site)

O git local protege contra o erro; não contra a perda do disco. Uma cópia remota é indispensável.

- **Repositório remoto privado** (a escolha do aluno) ou **pasta sincronizada** (Obsidian Sync, ou armazenamento na nuvem) - desde que privado.
- **Cadência**: push após os commits relevantes, no mínimo ao fim do dia de trabalho.
- A escolha entre repositório git remoto e sincronização de pasta é do aluno; o protocolo exige que exista uma, não impõe qual.

## Camada 3 - Snapshots periódicos (ponto de restauro)

Cópia completa e datada do vault, independente do histórico git, para o caso de corrupção do próprio repositório.

- **Cadência sugerida**: semanal, alinhada com a auditoria.
- **Forma**: arquivo datado (`vault-AAAA-MM-DD.zip`) guardado fora da pasta de trabalho. Reter os últimos N (ex.: 4 semanais + 1 mensal).
- O snapshot é o último recurso: quando nem o git local nem o remoto servem, restaura-se o último snapshot íntegro.

---

## `raw/` - a fonte da verdade

`raw/` contém os originais (PDF, etc.) de que tudo depende e que não se regeneram. Duas vias, à escolha do aluno:

- **Versionar com o vault** - simples, tudo num sítio; o repositório cresce com os binários (considerar git-lfs para ficheiros grandes).
- **Backup separado dedicado** - `raw/` replica-se à parte (a sua própria cópia na nuvem), e o git versiona só `wiki/` e o schema. O `.gitignore` pode então excluir `raw/`.

Seja qual for a via, **`raw/` tem de estar coberto por backup** - perder os originais é perder a possibilidade de re-verificar.

## Recuperação (o caminho de volta)

Quando algo se perde, por ordem de preferência:

1. **Erro de edição numa página** → `git checkout` da versão anterior do ficheiro (na cópia de trabalho da sessão; na pasta ligada, a reposição corre pela via de cópia de conteúdo do § Espelho local, nunca por checkout). O histórico tem-na.
2. **Página apagada** → recuperar do git; em alternativa, de `archive/` (a escrita prudente roda para lá, não elimina).
3. **Vault local corrompido ou perdido** → clonar do remoto (camada 2).
4. **Repositório corrompido** → restaurar o último snapshot íntegro (camada 3) e re-aplicar o trabalho desde então.

Testar a recuperação não é opcional: uma cópia de segurança nunca verificada é uma hipótese, não uma garantia. Recomenda-se, uma vez, restaurar um snapshot para uma pasta de teste e confirmar que abre.

## Registo

Operações de backup com efeito estrutural (inicialização do git, mudança de estratégia de replicação) registam-se no `log.md` com prefixo `Arquitectura`. Os commits de rotina vivem no próprio histórico git, não no log da wiki.

Fecho de conversa: além do commit, da auditoria estrutural verde e do zip testado, o fecho regenera o doc de estado do projecto claude.ai (`claude/estado-do-cofre.md`) - a fotografia de retoma que a conversa seguinte lê antes de abrir o zip (Decisão de 2026-07-10). Ao passe estrutural e ao verificador global acresce no fecho o crivo de citações, nos termos e com a condição de entrada em vigor do `PROTOCOLO-AUDITORIA.md`, § «Passe mecânico de âncoras» (6.26, item D).

# PROTOCOLO-BACKUP.md — backup, versionamento e recuperação

A wiki é a memória de trabalho. Perdê-la é catastrófico — anos de leitura, síntese e conexões num só directório. Este protocolo fixa como se versiona, se replica e se recupera. É infra-estrutura, não funcionalidade: tem de existir antes de a wiki ter valor a perder.

A escrita do agente é, por si, prudente — não apaga, rota para `archive/`, regista no log. Mas isso protege contra o erro de edição, não contra a perda do disco, a corrupção do ficheiro ou o engano humano irreversível. Para isso, três camadas.

---

## Camada 1 — Versionamento (git)

O vault é texto: o git é o instrumento natural. Recomendado desde o primeiro dia.

- **Inicialização**: `git init` na raiz do vault. O `.gitignore` (incluído) exclui temporários e o que não deve ser versionado.
- **Cadência de commit**: ao fim de cada sessão de trabalho com valor (uma ingestão concluída, um Eixo B fechado, uma sessão de estudo). O agente pode propor o commit no fecho da operação, com mensagem que espelha a entrada de log: `ingestão: Hespanha, Cultura Jurídica Europeia` ou `Eixo B: boa-fé — Comparativo 6`. O commit é acto sobre o sistema, não sobre a realidade jurídica — não precisa de ✅, mas o agente nunca força reescrita de história (`--force`, rebase destrutivo) sem indicação expressa.
- **O que o git dá**: histórico completo, diferença entre versões, regresso a qualquer estado anterior, e a base para replicação remota.
- **Tags de versão**: a cada versão do schema (frontmatter do `CLAUDE.md`), uma tag — `v6.8`, `v6.9` — no commit que a fecha; o estado do cofre em qualquer versão recupera-se por nome.
- **Consulta ao passado como instrumento**: «como estava esta página quando emiti o parecer de Março» responde-se com `git log -- <página>` e `git show <tag|data>:<caminho>` — no cofre profissional, é a base material da coerência decisória; o agente pode consultar o histórico, nunca reescrevê-lo.

## Camada 2 — Replicação remota (off-site)

O git local protege contra o erro; não contra a perda do disco. Uma cópia remota é indispensável.

- **Repositório remoto privado** (a escolha do aluno) ou **pasta sincronizada** (Obsidian Sync, ou armazenamento na nuvem) — desde que privado.
- **Cadência**: push após os commits relevantes, no mínimo ao fim do dia de trabalho.
- A escolha entre repositório git remoto e sincronização de pasta é do aluno; o protocolo exige que exista uma, não impõe qual.

## Camada 3 — Snapshots periódicos (ponto de restauro)

Cópia completa e datada do vault, independente do histórico git, para o caso de corrupção do próprio repositório.

- **Cadência sugerida**: semanal, alinhada com a auditoria.
- **Forma**: arquivo datado (`vault-AAAA-MM-DD.zip`) guardado fora da pasta de trabalho. Reter os últimos N (ex.: 4 semanais + 1 mensal).
- O snapshot é o último recurso: quando nem o git local nem o remoto servem, restaura-se o último snapshot íntegro.

---

## `raw/` — a fonte da verdade

`raw/` contém os originais (PDF, etc.) de que tudo depende e que não se regeneram. Duas vias, à escolha do aluno:

- **Versionar com o vault** — simples, tudo num sítio; o repositório cresce com os binários (considerar git-lfs para ficheiros grandes).
- **Backup separado dedicado** — `raw/` replica-se à parte (a sua própria cópia na nuvem), e o git versiona só `wiki/` e o schema. O `.gitignore` pode então excluir `raw/`.

Seja qual for a via, **`raw/` tem de estar coberto por backup** — perder os originais é perder a possibilidade de re-verificar.

## Recuperação (o caminho de volta)

Quando algo se perde, por ordem de preferência:

1. **Erro de edição numa página** → `git checkout` da versão anterior do ficheiro. O histórico tem-na.
2. **Página apagada** → recuperar do git; em alternativa, de `archive/` (a escrita prudente roda para lá, não elimina).
3. **Vault local corrompido ou perdido** → clonar do remoto (camada 2).
4. **Repositório corrompido** → restaurar o último snapshot íntegro (camada 3) e re-aplicar o trabalho desde então.

Testar a recuperação não é opcional: uma cópia de segurança nunca verificada é uma hipótese, não uma garantia. Recomenda-se, uma vez, restaurar um snapshot para uma pasta de teste e confirmar que abre.

## Registo

Operações de backup com efeito estrutural (inicialização do git, mudança de estratégia de replicação) registam-se no `log.md` com prefixo `Arquitectura`. Os commits de rotina vivem no próprio histórico git, não no log da wiki.

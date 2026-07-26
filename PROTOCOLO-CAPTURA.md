# PROTOCOLO-CAPTURA.md - captura rápida e triagem

O degrau de baixo do sistema. A digestão integral (Eixo A) é o nível alto, próprio das fontes nucleares, e é deliberadamente exigente. Mas um segundo cérebro que só aceita entradas perfeitas tende a não receber entradas nenhumas - e um cérebro vazio não é um cérebro. Este protocolo trata o conhecimento que chega sem forma de fonte formal: a dúvida a meio de uma aula, a intuição ao ler um acórdão, a ligação que ocorre no duche. Fricção mínima na entrada; disciplina na triagem.

A regra-âncora continua a valer: uma nota fugaz pode ser uma pergunta, uma hipótese, um lembrete - mas no momento em que vira conteúdo verificado da wiki, passa pelos gates de proveniência como qualquer outro. A captura não dispensa a verificação; adia-a.

---

## Captura (fricção mínima)

Uma nota fugaz entra em `wiki/Inbox/` a partir de `modelos/modelo-captura.md`, ou em forma ainda mais leve: uma linha com data. O que importa é registar antes de esquecer. Campos mínimos: o que se pensou; a origem, se houver (fonte, aula, conversa); o estado `por-processar`. Nada mais é exigido no momento da captura - nem ancoragem, nem classificação, nem wikilinks. Esse trabalho é da triagem.

Uma nota fugaz é explicitamente provisória: não é citável, não sustenta atribuições, não conta como conhecimento da wiki até ser processada. O seu estado é sempre `em-aberto`.

## Triagem (quando houver tempo, em lote)

Periodicamente - não a cada captura - o `Inbox/` processa-se. Para cada nota fugaz, uma de quatro saídas:

1. **Promover a permanente.** A nota tem valor durável e pode ser ancorada: vira (ou alimenta) uma página de entidade, passando pelos gates do Eixo A. A nota fugaz é então arquivada ou eliminada do inbox, com registo.
2. **Converter em pergunta de estudo.** A nota é uma dúvida que vale a pena perseguir: vira entrada na lista de lacunas do `index.md`, ou semente para o Examinador, ou dúvida registada numa página existente (com o marcador de etiologia certo).
3. **Converter em tarefa de ingestão.** A nota aponta para uma fonte a estudar: entra na fila de prioridade (cruzada com `Faculdades.md`).
4. **Descartar.** A nota perdeu utilidade ou estava errada. Eliminar com registo no `log.md` (prefixo `Delete`), nunca em silêncio.

A triagem não deixa o inbox crescer indefinidamente: notas fugazes paradas há muito geram achado na auditoria (vertente geradora - a captura que nunca se processa é captura perdida).

## O que a captura nunca faz

- Não promove uma nota fugaz a conteúdo verificado sem passar pelos gates de proveniência.
- Não trata o inbox como arquivo permanente - o inbox é trânsito, não morada.
- Não perde uma nota descartada em silêncio - o descarte regista-se.

## Invocação
- «captura: {pensamento}» - cria nota fugaz no inbox.
- «triagem» / «processa o inbox» - corre a triagem em lote.

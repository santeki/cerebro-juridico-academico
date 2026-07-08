# PROTOCOLO-GATILHOS.md — vigia proactiva

O cofre é, por defeito, reactivo: tu diriges, ele responde. Mas há sinais que valem a pena vigiar sem esperares por eles — uma página cuja revisão está devida, um exame que se aproxima, uma fonte nova que saiu sobre matéria que já estudaste. Esta peça é importada do *trigger scanner* da Augusta, que deteta sinais sozinho e os regista, incluindo um registo do que *não* detectou para a passagem seguinte não repetir o trabalho.

Honestidade à cabeça, porque condiciona tudo: a vigia verdadeiramente proactiva — que dispara sozinha em segundo plano — depende de o ambiente suportar tarefas agendadas. Onde não suportar, a vigia é uma **passagem que tu corres** («corre a vigia»), periódica mas manual. O valor mantém-se: o que a vigia faz, e o registo que deixa, é o mesmo; só o gatilho do gatilho muda (relógio vs tu).

---

## O registo de gatilhos

Os gatilhos activos vivem em `wiki/GATILHOS.md`: cada um diz o que vigia, com que cadência, e o que faz quando dispara. Para o cofre académico, os gatilhos naturais são:

- **Revisão devida** — páginas cuja `revisao_proxima` passou. Dispara: entram no painel (`PROTOCOLO-PAINEL.md`, Frente 1).
- **Exame a aproximar-se** — uma data de `Faculdades.md` dentro da janela de alerta. Dispara: o painel reordena a fila de ingestão para a matéria da cadeira (Frente 3).
- **Fonte nova sobre matéria estudada** — quando registas ou encontras uma fonte que toca um conceito já na wiki. Dispara: propõe Eixo B (comparar a fonte nova com as existentes).
- **Lacuna parada** — uma dúvida em aberto há mais do que o limiar. Dispara: sobe no painel e na auditoria.
- **Estudo fechado** — a ingestão de uma fonte concluiu. Dispara: revisão dupla do estudo (`PROTOCOLO-EQUIPA.md`) antes de o dar por encerrado.
- **Bloco fechado** — um bloco do programa de uma cadeira ficou coberto (fontes previstas ingeridas ou dispensadas). Dispara: auditoria de fecho com âmbito reduzido ao bloco (`PROTOCOLO-AUDITORIA.md`).

## A passagem de vigia

Cada passagem regista uma secção datada com o que vigiou e o que encontrou — e, tão importante, **o que não encontrou** (o registo de resultados negativos). Esse registo evita que a passagem seguinte refaça o mesmo varrimento e perca tempo no que já foi descartado. A passagem não age sozinha sobre o que encontra: alimenta o painel e propõe; tu decides. Nada que toque conteúdo verificado entra sem passar pelos gates de proveniência.

## Articulação

Os gatilhos alimentam o painel — são, em boa parte, o que torna o painel «vivo». O que a vigia propõe entra no formato de apresentação (`playbooks/formato-apresentacao.md`), item a item, e uma sugestão que marques com ❌ vai para a lista de supressão e não volta a ser proposta.

## Invocação
- «corre a vigia» — passagem de vigia; regista o que encontrou e o que não encontrou.

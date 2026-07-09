# PROTOCOLO-VOZ.md — fingerprint de estilo

O sistema produz texto — sebentas, sínteses, esquemas, respostas. Por defeito, esse texto sai numa voz genérica de modelo. O fingerprint de estilo corrige isso: captura a voz real de quem escreve, para que o que o agente produz soe a ti e não a ninguém. A peça é importada do sistema da Augusta, onde cada rascunho de email *tem* de corresponder ao fingerprint de quem escreve; aqui serve a escrita académica e qualquer produto de trabalho.

Duas regras-âncora governam esta peça, e nenhuma cede.

A voz **deriva de amostras reais**, nunca de invenção. O fingerprint constrói-se a partir de textos que tu escreveste — sebentas, resumos, ensaios, respostas de exame — e das tuas regras de estilo declaradas. O agente não fabrica uma voz nem atribui ao teu estilo traços que não observou nas amostras. Sem amostras suficientes, o fingerprint fica parcial e diz que está parcial.

A voz **nunca se sobrepõe ao rigor**. Um texto na tua voz continua sujeito a todas as regras de proveniência, ancoragem e verificação. O fingerprint molda a *forma* — registo, ritmo, léxico —, nunca a *substância*. Soar a ti não é desculpa para afirmar sem fonte; a voz veste o argumento, não o substitui.

---

## Construção

O fingerprint vive em `wiki/VOZ-FINGERPRINT.md`, a partir de `modelos/modelo-voz.md`. Constrói-se lendo um corpo de textos teus e destilando: registo(s) e nível de formalidade; aberturas e fechos típicos; comprimento e ritmo de frase; conectores e construções recorrentes; léxico que sobreusas; léxico que nunca usas; como introduzes e como concluis; como tratas uma objecção ou uma tese contrária. As tuas regras de estilo declaradas entram como input directo — são a voz que já sabes ter.

Cada traço do fingerprint ancora-se numa observação real («abre sebentas com X», «nunca usa Y»), não numa generalização. Onde o corpo de amostras não chega para fixar um traço, esse traço fica em aberto.

## Evolução

O fingerprint não é estático. Periodicamente — não a cada texto — o agente confronta o fingerprint com novos textos teus e propõe ajustes: um traço novo que emergiu, um que deixou de se confirmar. As alterações ao fingerprint **passam pela tua aprovação** antes de entrarem (a tua voz é tua; o agente propõe, não decide). Cada alteração aprovada regista-se no `log.md` com prefixo `Voz`.

## Aplicação

Os produtos de trabalho com texto corrido — sebentas, sínteses, esquemas, ensaios — seguem o fingerprint. As páginas de fonte (reservatório) e o log (registo técnico) não: aí o que importa é a fidelidade à fonte e a precisão do registo, não a voz. Antes de fechar um produto de trabalho, o agente verifica-o contra o fingerprint da mesma forma que o verifica contra as regras de proveniência: registo certo, léxico banido ausente, ritmo coerente.

## Referências e bibliografia nos produtos

Todo o produto académico — ensaio, dissertação, resposta desenvolvida, trabalho — sai com aparato crítico completo: referências no corpo ou em nota, e bibliografia final, na norma de citação fixada. A norma concreta configura-se na vista da faculdade (`wiki/Faculdades/<Faculdade>.md`, campo `norma_citacao`) — em Portugal, a NP 405-1 é a referência natural; faculdades ou docentes podem exigir outra. Sem norma configurada, o produto sai com as referências completas em formato neutro e a pendência declarada («norma de citação por configurar na vista») — declara-se, não se improvisa um formato com autoridade que não tem. Invariantes que nenhuma norma dispensa: jurisprudência identifica-se por tribunal, data, processo e ECLI quando exista; legislação com diploma, artigo, n.º e alínea, na versão vigente; doutrina com autor, obra, edição e ano, página quando citada; e a bibliografia espelha o corpus efectivamente convocado e verificado — não decora. A distinção visual da citação (aspas curvas, itálico) é a das `CONVENCOES.md`.

## Evolução do fingerprint

A voz não é estática: evolui a partir das correcções reais. Periodicamente, ou a cada ciclo de produtos que o aluno indique, o agente compara os seus rascunhos com as versões finais corrigidas e com os produtos aprovados, identifica padrões recorrentes de correcção — aberturas, fórmulas, extensão de frase e de parágrafo, terminologia preferida, construções eliminadas — e propõe actualizações ao `VOZ-FINGERPRINT.md` com a evidência à vista («corrigido X→Y em N produtos»). Nada se aplica sem ✅; aprovada, a actualização entra com data e nota do que mudou, e a evolução regista-se em `wiki/VOZ-EVOLUCAO.md` — data, mudança, padrão que a motivou, decisão. Proposta recusada não se repropõe sem evidência nova; na dúvida entre a voz antiga e a emergente, a antiga vale até o aluno decidir.

## Invocação
- «constrói a voz» / «actualiza a voz» — corre a construção ou a passagem de evolução (com aprovação).
- «aplica a voz a isto» — molda um texto existente ao fingerprint, sem tocar a substância.

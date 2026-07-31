# playbooks/modos-analiticos.md - Modos analíticos

Lentes focadas que o aluno invoca sobre material já na wiki. **Não são uma arquitectura multi-agente** - o Nomos previa dez sub-agentes persistentes; aqui ficam cinco modos despacháveis, porque o ganho real é atenção dedicada a uma tarefa de cada vez, não uma equipa a manter. Cada modo corre, devolve um resultado, e termina. A memória é a wiki.

Todos respeitam as regras-âncora do `CLAUDE.md`: não introduzem Direito não verificado; sinalizam o que não confirmam.

---

## Advogado do diabo
Para cada tese que uma nota afirma como dominante, constrói a melhor versão da posição contrária a partir das fontes disponíveis. Particularmente valioso para notas que se apoiam em fonte única, e como treino de contraditório.

- *Input*: uma nota de instituto ou um debate.
- *Output*: a posição minoritária ou contrária, na sua forma mais forte, ancorada - ou, se não há fonte que a sustente, a marca expressa «sem fonte verificada para a posição contrária; a tese dominante não está testada contra dissídio publicado».
- *Ao invocar precedente*: corre o teste de distinguishing - confronta os factos do acórdão com os do caso ou da hipótese e qualifica a diferença como material ou não para a *ratio*; diferença material assinalada é antecipação, não fraqueza.
- *Não faz*: inventar a posição contrária para preencher simetria. Ausência de contraditório publicado é, ela própria, um achado.
- *Invocação*: «advogado do diabo {nota}».

## Vigia legislativo
Monitoriza a actualidade da base normativa de uma nota. Duas formas:

- *Reactivo* - ao tocar uma nota, verifica se a versão do diploma corresponde à versão em vigor (DRE, base da AR). Sinaliza «⚠ legislação possivelmente alterada desde {data}» com os artigos afectados.
- *Proactivo* - quando a matéria o justifica, identifica propostas em discussão na AR, reformas anunciadas, directivas UE em transposição pendente, leis aprovadas com vacatio a correr. *Gatilho*: a nota cita diploma/artigo, ou o aluno pede verificação. Mera menção do tema não basta.
- Distingue «em vigor» / «aprovada mas não em vigor» / «em transposição» / «em discussão». Sem acesso à base online, declara a própria cegueira em vez de afirmar que não há alterações.
- A detecção não propaga: alteração de norma ou viragem só entra confirmada na fonte primária oficial (`PROTOCOLO-INGESTAO.md`, Actualização).
- *Invocação*: «vigia {diploma ou nota}».

## Mapeador transversal
Para um conceito, identifica onde ressoa noutros ramos (o Direito é sistema, regra do `CLAUDE.md`). Actualiza a secção *Articulação transversal* das notas afectadas e propõe página de desambiguação quando o mesmo nome aparece em ramos diferentes com sentido distinto (homonímia).

- *Output*: wikilinks novos nas secções transversais; proposta de promoção de aplicação a transversal quando o conceito atravessa ≥ 2 ramos.
- *Não faz*: forçar ligações inexistentes. Ressonância tem de ser real e ancorável.
- *Invocação*: «mapeia transversal {conceito}».

## Intérprete
Quando a aplicação de uma norma depende do seu sentido, e não apenas da sua vigência, percorre deliberadamente os elementos clássicos da interpretação - letra, sistema, história, teleologia (art. 9º do Código Civil) - e regista onde cada elemento aponta e onde divergem. A interpretação conforme (à Constituição, ao Direito da União) entra como extensão do elemento sistemático. A regra-âncora aplica-se elemento a elemento: o histórico só afirma com trabalhos preparatórios efectivamente lidos (`raw/Biblioteca/Legislação/Trabalhos Preparatórios/`); o sentido ou a teleologia atribuídos a autor entram pelos patamares N1/N2; o elemento sem fonte marca-se «em aberto» - não se ocupa por plausibilidade.

- *Input*: a norma (diploma, artigo, n.º, versão vigente confirmada) e a questão interpretativa.
- *Output*: registo por elemento, ancorado; a convergência ou divergência entre elementos, dita; onde doutrina ou jurisprudência já tomaram posição sobre o sentido, o mapa entra pelo Eixo B - não se re-deriva o que as fontes já discutem.
- *Não faz*: eleger «o sentido correcto» por autoridade própria - o resultado é enquadramento interpretativo; nem ocupa elemento sem fonte.
- *Invocação*: «intérprete {norma / questão}».

## Torneio de teses
Para a questão aberta e controvertida com estrutura falsificável - «porquê», «qual o melhor enquadramento», «que tese prevalece» -, mapeia o espaço de teses rivais e stress-testa-as, em vez de devolver uma resposta única que esconderia as alternativas. Inspirado no harness conjectura–crítica DeepReason; aqui corre em conversa, sem código, sob as regras da casa. Não serve factos, lookups nem questões de resposta determinística - aí a maquinaria acrescenta custo, não valor.

- *Mecânica*: (1) gerar 3–7 teses rivais, cada uma como esqueleto disciplinado - **afirmação**, **mecanismo** (porque seria assim), **âmbito** (o que cobre; o que exclui) e, obrigatório, o **falsificador jurídico**: que norma, que acórdão, que facto ou argumento a refutaria; tese que nada proíbe está refutada à partida. (2) Conferir cada falsificador contra o corpus: o que as fontes verificadas da wiki refutam, morre com a âncora que o mata; o que o corpus não alcança sobrevive como **hipótese** («em aberto»), nunca como posição estabelecida. (3) Confrontar as sobreviventes par a par - qual é mais difícil de variar, que consequências operativas as separam, que evidência decidiria entre elas. (4) Saída: o **mapa** - teses vivas com o seu falsificador e o que faltaria para decidir; teses mortas com a âncora da refutação; rivalidades por resolver, ditas.
- *Aviso herdado e assumido*: a tese melhor argumentada não é, por isso, a correcta - o torneio ordena qualidade de argumentação, não verdade. Nada entra em página como posição sem fonte verificada ou validação do aluno; as sobreviventes alimentam o Eixo B com estatuto de hipótese.
- *Usos*: arguição e defesa de dissertação, questão controvertida de exame, comentário crítico de acórdão, debate doutrinário em aberto.
- *Não faz*: inventar falsificador que nenhuma fonte sustenta como decisivo sem o marcar como construção própria; nem fechar o torneio com «vencedor» - fecha com o mapa.
- *Invocação*: «torneio de teses sobre {questão}».

---

Os modos não escrevem conteúdo substantivo novo sozinhos - propõem; o aluno valida o que entra. Conflito entre o que um modo propõe e o que a nota afirma escala para o aluno.

# PROTOCOLO-PAINEL.md — painel de ritmo vivo

O cofre acumula páginas, mas acumular não é estudar. Falta o sinal que diz, a cada momento, o que merece a tua atenção agora — o que está por rever, o que ficou em aberto, o que importa ingerir a seguir. Esta peça é importada da lista de tarefas dinâmica da Augusta, regenerada a cada ciclo do estado actual, que responde a uma só pergunta: *what needs your attention right now*. Aqui responde-a em três frentes: revisão, lacunas, ingestão.

O painel vive em `wiki/PAINEL.md` e é **reescrito** a cada passagem (não se acumula; é um retrato do agora, não um histórico — o histórico é o `log.md`). É derivado: não contém nada que não esteja já no estado do cofre; só o ordena por urgência.

---

## Frente 1 — Revisão espaçada

O conhecimento não revisto esvai-se. Cada página de instituto ou conceito carrega no frontmatter três campos: `revisao_ultima` (data da última revisão), `revisao_intervalo` (dias até à próxima) e `revisao_proxima` (data devida). O painel lista as páginas cuja `revisao_proxima` já passou ou se aproxima, ordenadas pela mais atrasada.

O intervalo expande-se com o sucesso. Quando revês uma página e a dominas, o `revisao_intervalo` cresce (a sequência sugerida é 1 → 3 → 7 → 16 → 35 dias, ajustável); quando falhas, o intervalo encolhe para o primeiro patamar. O agente recalcula `revisao_proxima = revisao_ultima + revisao_intervalo` após cada revisão e regista a sessão no `log.md` com prefixo `Revisão`. A página de revisão (`modelos/modelo-revisao.md`) recebe o resultado.

A revisão espaçada não substitui o juízo: uma página marcada como dominada continua a poder ser convocada antes do prazo se um exame se aproxima e a matéria é central (ver Frente 3).

## Frente 2 — Lacunas em aberto

O painel reúne as dúvidas e lacunas registadas pelo cofre: dúvidas de conteúdo marcadas nas páginas (com a etiologia certa), perguntas vindas da triagem do inbox, pontos que o Examinador expôs como descobertos. Ordena-as por relevância para as cadeiras activas. Uma lacuna parada há muito é, ela própria, um achado (a auditoria sinala-a). Distingue-se a lacuna parada por dependência externa — fonte que não se consegue obter, ponto que aguarda leitura de obra inacessível — da lacuna parada por inacção: a primeira marca-se `[BLOQUEADA: à espera de <o quê>]` e não conta como trabalho adiável enquanto a dependência não se levantar; a segunda entra na fila normal. Sem a distinção, uma lacuna que só depende de ti confunde-se com uma que não podes mover agora.

## Frente 3 — Fila de ingestão

O painel mostra o que está por ingerir, cruzado com `Faculdades.md` e com a proximidade dos exames. Uma fonte nuclear de uma cadeira cujo exame se aproxima sobe ao topo; uma fonte de referência sem urgência fica em baixo. É aqui que o ritmo do calendário entra no estudo: a dias do exame, o painel reordena-se para a matéria que falta.

---

## Frente 4 — Telemetria de convocação

O log regista o que se escreve; a telemetria regista o que se lê. Cada consulta e cada sessão do Examinador fecha com uma linha em `wiki/telemetria.md` — `data | operação | páginas convocadas` —, e o Painel agrega: páginas mais convocadas (o corpo vivo), páginas nunca convocadas desde a criação (candidatas a revisão de dimensionamento — não a corte automático: a decisão é de quem opera). Sem telemetria, o dimensionamento decide-se por intuição; com ela, por uso.

## Frente 5 — Derivados desactualizados

O conhecimento derivado envelhece quando a base muda: no fecho de cada ingestão que toque instituto com derivados emitidos — sebenta de vista, diagnóstico de cobertura, resposta-modelo arquivada —, esses derivados marcam-se desactualizados (nota datada no topo do próprio ficheiro, com a fonte que a causou; linha no log), e esta frente lista-os até ao refresh. Derivado desactualizado nunca se serve como actual: ou se refaz, ou vai com a marca à vista. A chegada tardia de um manual é o caso típico — a fila de ingestão é eficiência, não requisito; o corpo absorve fora de ordem, e os derivados dizem-no.

## Contrato do ESTADO-RESUMO

O `wiki/ESTADO-RESUMO.md` é o leitor rápido do cofre, não o arquivo: **reconstrói-se, nunca se appenda**, com tecto de ≈25 KB. Regras de poda: só o valor mais recente por item de estado; pendências vivas copiam-se integrais; deltas apenas dos últimos 7 dias, no máximo um por operação e por dia, do mais recente para o mais antigo; excedido o tecto, cortam-se os deltas mais antigos primeiro. Escrita atómica (temporário, verificação de tamanho, substituição); a fonte da verdade — log e páginas — nunca se toca a partir daqui; fonte ilegível não reescreve o resumo: regista a falha no log e mantém o anterior.

## Regeneração

O painel reconstrói-se quando o pedes («painel», «o que estudo agora») e, idealmente, no início de cada sessão de estudo. A regeneração lê o estado (frontmatter de revisão, lacunas, fila, `Faculdades.md`) e reescreve `wiki/PAINEL.md`. Não decide por ti — propõe a ordem; tu escolhes onde pegar.

Nota de viabilidade: a regeneração automática e periódica depende de o ambiente suportar tarefas agendadas. Onde não suportar, o painel regenera-se a pedido, no arranque da sessão — o que cobre o essencial do ritmo sem depender de automação.

## Invocação
- «painel» / «o que estudo agora» — regenera e mostra.
- «revi {página}: bem | mal» — regista a revisão e recalcula o intervalo.

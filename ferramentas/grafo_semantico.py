#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passe do grafo por código (PROTOCOLO-AUDITORIA.md, Plano 3 - delta 6.17).

Constrói o grafo dirigido dos wikilinks entre páginas de conhecimento e relata:
  (a) órfãs - páginas de conhecimento sem qualquer link de entrada vindo de outra
      página de conhecimento;
  (b) assimetrias - aresta A→B sem retorno B→A, com a linha de contexto da aresta;
  (c) sub-ligadas - páginas de tipo conceito|instituto com grau total < 2
      (informação de dimensionamento, sem limiar normativo).

O passe encontra, não decide: a saída é relatório datado de achados para
adjudicação; nunca escreve nas páginas, nunca cria recíprocos automáticos, e um
achado seu não bloqueia fecho por si (exit code 0 sempre que corre - não é gate,
ao contrário do crivo).

Orfandade: a entrada vinda de uma vista de faculdade afasta a orfandade (o
mapeamento curricular é selectivo - quem a vista aponta não está órfão), embora
a aresta vista→página seja de serviço e fique fora do grafo de assimetrias. As
entradas de catálogo (index.md, log.md e demais ficheiros de serviço) não
afastam a orfandade - o catálogo aponta tudo por função, e contá-lo esvaziaria
o critério.

Fora da teia de conhecimento (emissores e receptores de navegação/serviço):
index.md, log.md, PAINEL.md, ESTADO-RESUMO.md, telemetria.md, MELHORIA.md,
GLOSSARIO.md, SUPRESSAO-LIST.md, GATILHOS.md, VOZ-EVOLUCAO.md,
VOZ-FINGERPRINT.md, Faculdades.md e as vistas de faculdade (wiki/Faculdades/) -
a classe é a dos ficheiros de serviço da raiz de wiki/ (nomenclatura das
CONVENCOES; alinhada com o E7 do crivo estrutural). Directórios não percorridos:
Inbox/, Revisão/, Auxiliares/, archive/. As fontes de avaliação
(wiki/Avaliação/) percorrem-se mas ficam fora do conjunto de conhecimento: as
suas ligações registam-se como arestas de serviço, fora do grafo.
"""
import re, sys, unicodedata, datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # ferramentas/ vive na raiz do cofre (6.26, item F)
def N(s): return unicodedata.normalize('NFC', s)

WIKI = VAULT / 'wiki'
NAV_ROOT = {'index.md', 'log.md', 'PAINEL.md', 'ESTADO-RESUMO.md', 'telemetria.md',
            'MELHORIA.md', 'GLOSSARIO.md', 'SUPRESSAO-LIST.md', 'GATILHOS.md',
            'VOZ-EVOLUCAO.md', 'VOZ-FINGERPRINT.md', 'Faculdades.md'}
SKIP_DIRS = {'Inbox', 'Revisão', 'Auxiliares', 'archive'}
NAV_DIRS = {'Faculdades'}          # vistas de faculdade - navegação
SERVICE_DIRS = {'Avaliação'}       # fontes de avaliação - fora do conjunto

wl_re = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
PARAM = re.compile(r'[<>{}*]|X\.md|AAAA')

def classify(rel_parts, name):
    if any(N(x) in SKIP_DIRS for x in rel_parts[:-1]):
        return 'skip'
    if len(rel_parts) == 1:
        return 'nav' if N(name) in NAV_ROOT else 'conhecimento'
    head = N(rel_parts[0])
    if head in NAV_DIRS:
        return 'vista'
    if head in SERVICE_DIRS:
        return 'aval'
    return 'conhecimento'

def frontmatter_tipo(text):
    if not text.startswith('---'):
        return None
    m = re.search(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        return None
    t = re.search(r'^tipo:\s*(\S+)', m.group(1), re.M)
    return t.group(1) if t else None

pages = {}          # rel NFC (sem .md) -> {'path', 'classe', 'tipo'}
by_base = {}        # stem NFC -> [rel NFC]
for p in sorted(WIKI.rglob('*.md')):
    if '.git' in p.parts:
        continue
    rel = p.relative_to(WIKI)
    classe = classify(rel.parts, rel.name)
    if classe == 'skip':
        continue
    key = N(str(rel)[:-3])
    pages[key] = {'path': p, 'classe': classe, 'tipo': None}
    by_base.setdefault(N(rel.stem), []).append(key)

VAULT_FILES = {N(str(p.relative_to(VAULT))) for p in VAULT.rglob('*')
               if '.git' not in p.parts}

def resolve(tgt):
    tgt = N(tgt.strip())
    if tgt in pages:
        return tgt
    if tgt.startswith('wiki/') and tgt[5:] in pages:
        return tgt[5:]
    hits = by_base.get(tgt) or by_base.get(N(Path(tgt).name), [])
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        return ('AMBÍGUO', tuple(hits))
    if tgt in VAULT_FILES or f'{tgt}.md' in VAULT_FILES:
        return 'EXTERNO'  # resolve fora de wiki/ (raw/, modelos/, …) - aresta de serviço
    return None

edges = {}          # (origem, destino) -> linha de contexto (1.ª ocorrência)
service_edges = 0   # arestas com um extremo fora do conjunto de conhecimento
vista_targets = set()  # páginas de conhecimento apontadas por vistas (afastam orfandade)
unresolved = []     # alvos que não resolvem dentro de wiki/ (informativo; gate é do crivo)
ambiguous = []

for key, info in pages.items():
    if info['classe'] == 'nav':
        continue  # catálogo/serviço da raiz não se percorre - fora da teia
    text = info['path'].read_text(encoding='utf-8')
    if info['classe'] == 'conhecimento':
        info['tipo'] = frontmatter_tipo(text)
    for line in text.splitlines():
        for m in wl_re.finditer(line):
            raw_tgt = m.group(1)
            if PARAM.search(raw_tgt):
                continue
            r = resolve(raw_tgt)
            if r is None:
                unresolved.append(f'{key} → [[{N(raw_tgt.strip())}]]')
                continue
            if r == 'EXTERNO':
                service_edges += 1
                continue
            if isinstance(r, tuple):
                ambiguous.append(f'{key} → [[{N(raw_tgt.strip())}]] ∈ {r[1]}')
                continue
            if info['classe'] != 'conhecimento' or pages[r]['classe'] != 'conhecimento':
                service_edges += 1
                if info['classe'] == 'vista' and pages[r]['classe'] == 'conhecimento':
                    vista_targets.add(r)
                continue
            if r == key:
                continue  # self-link não conta
            edges.setdefault((key, r), line.strip())

conjunto = {k for k, v in pages.items() if v['classe'] == 'conhecimento'}
in_deg = {k: 0 for k in conjunto}
out_deg = {k: 0 for k in conjunto}
for (a, b) in edges:
    out_deg[a] += 1
    in_deg[b] += 1

orfas = sorted(k for k in conjunto if in_deg[k] == 0 and k not in vista_targets)

# Dobragem das sub-páginas (6.22): a aresta de/para sub-página («— leitura da sessão N»,
# «— leitura do capítulo R», «— posição de X») dobra-se na página-mãe para o cômputo das
# assimetrias - o retorno da aresta da sub-página vive na mãe; contá-la solta inundaria o
# relatório com assimetrias estruturais da cisão/fissão. O total bruto reporta-se ao lado.
SUBPAGE_RE = re.compile(r'^(?P<mae>.+?) — (leitura d[ao] (sessão \d+|capítulo [IVX]+)|posição de .+)$')
def canon(key):
    m = SUBPAGE_RE.match(N(Path(key).name))
    if not m:
        return key
    hits = by_base.get(N(m.group('mae')), [])
    return hits[0] if len(hits) == 1 else key

folded = {}
for (a, b), ctx in edges.items():
    fa, fb = canon(a), canon(b)
    if fa == fb:
        continue
    folded.setdefault((fa, fb), ctx)
assimetrias_brutas = sum(1 for (a, b) in edges if (b, a) not in edges)
assimetrias = sorted((a, b) for (a, b) in folded if (b, a) not in folded)
sub_ligadas = sorted(k for k in conjunto
                     if pages[k]['tipo'] in ('conceito', 'instituto')
                     and in_deg[k] + out_deg[k] < 2)

hoje = datetime.date.today().isoformat()
print(f'# Passe do grafo por código - relatório de achados ({hoje})')
print(f'universo: {len(conjunto)} páginas de conhecimento · {len(edges)} arestas '
      f'· {service_edges} arestas de serviço (fora do grafo)')
print()
print(f'## (a) Órfãs - {len(orfas)}')
for k in orfas:
    print(f'  - {k}')
print()
print(f'## (b) Assimetrias - {len(assimetrias)} (dobradas nas páginas-mãe; brutas: {assimetrias_brutas})')
for (a, b) in assimetrias:
    print(f'  - {a} → {b} (sem retorno)')
    print(f'      contexto: «{folded[(a, b)][:160]}»')
print()
print(f'## (c) Sub-ligadas (tipo conceito|instituto, grau total < 2) - {len(sub_ligadas)} [informação]')
for k in sub_ligadas:
    print(f'  - {k} (entrada {in_deg[k]} · saída {out_deg[k]})')
if unresolved:
    print()
    print(f'## Alvos não resolvidos em wiki/ - {len(unresolved)} [informativo; o gate é o crivo]')
    for u in unresolved:
        print(f'  - {u}')
if ambiguous:
    print()
    print(f'## Alvos ambíguos - {len(ambiguous)} [adjudicar]')
    for u in ambiguous:
        print(f'  - {u}')
print()
print(f'GRAFO - páginas: {len(conjunto)} · arestas: {len(edges)} · órfãs: {len(orfas)} '
      f'· assimetrias: {len(assimetrias)} dobradas ({assimetrias_brutas} brutas) · sub-ligadas: {len(sub_ligadas)}')
sys.exit(0)

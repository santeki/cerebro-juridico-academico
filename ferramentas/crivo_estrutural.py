#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crivo estrutural do esqueleto - por código (PROTOCOLO-AUDITORIA.md, passe estrutural).
v2 (delta 6.18, agregado II): acresce ao contrato v1 (checks 1-6) o frontmatter
mínimo de cada página de wiki/ (tipo no enum das CONVENCOES + titulo presente)
e a cobertura índice↔wiki nos dois sentidos; `indice` entra nos singulares sem
modelo. A v1 mantém-se intocada nos checks 1-6.
Exclusões codificadas (CHANGELOG 6.13 (iii); E10 proposto no despacho 6.18):
  E1 exemplos marcados («Ex.:», «p. ex.») das CONVENCOES;
  E2 menção em prosa a log.md no § Versionamento do CLAUDE.md;
  E3 o [[página]] paramétrico de telemetria.md;
  E4 história datada de log.md e do CHANGELOG.md;
  E5 nomes paramétricos (X.md, <...>, {...}, AAAA) e ficheiros gerados a pedido (ERRATA-EDICAO.md);
  E6 caminhos com prefixo claude/ (docs de projecto claude.ai);
  E7 ficheiros de serviço de wiki/ documentados na nomenclatura das CONVENCOES (árvore↔disco);
  E8 modelos/ como templates paramétricos (wikilinks de exemplo não se resolvem);
  E9 CHANGELOG.md no reverso árvore↔disco (documentado no § Versionamento do CLAUDE.md, «na raiz do cofre»);
  E10 ficheiros de serviço/navegação de wiki/ sem frontmatter, isentos do check 7;
  E11 ferramentas/ na raiz do cofre, sob git (6.26, item F)
      (index.md, log.md, telemetria.md, VOZ-EVOLUCAO.md, Avaliação/_indice.md).
"""
import re, sys, unicodedata
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # ferramentas/ vive na raiz do cofre (6.26, item F)
def N(s): return unicodedata.normalize('NFC', s)

failures, notes = [], []

def fail(check, msg): failures.append(f'[{check}] {msg}')

MD_ALL = [p for p in VAULT.rglob('*.md') if '.git' not in p.parts and 'archive' not in p.parts]
REL = {N(str(p.relative_to(VAULT))): p for p in MD_ALL}
ALL_FILES_NFC = {N(str(p.relative_to(VAULT))) for p in VAULT.rglob('*') if '.git' not in p.parts}

PARAM = re.compile(r'[<>{}*]|X\.md|AAAA|N\.M|<obra>')
GENERATED = {'ERRATA-EDICAO.md'}

def is_param(tok): return bool(PARAM.search(tok))

def resolve_file(tok):
    tok = N(tok.strip())
    cands = [tok, f'wiki/{tok}', f'modelos/{tok}', f'playbooks/{tok}',
             f'identidade/{tok}', f'identidade/_modelo/{tok}']
    return any(c in ALL_FILES_NFC for c in cands)

# ---------- Check 1: remissões inter-ficheiros em texto normativo ----------
NORMATIVE = [p for p in MD_ALL if (
    (p.parent == VAULT and p.name != 'CHANGELOG.md') or
    p.parts[-2] in ('playbooks', 'modelos') or
    (p.parent == VAULT/'wiki' and p.name in ('GLOSSARIO.md','GATILHOS.md','MELHORIA.md',
        'SUPRESSAO-LIST.md','VOZ-FINGERPRINT.md','VOZ-EVOLUCAO.md','telemetria.md','Faculdades.md'))
)]
tok_re = re.compile(r'`([^`\n]+?\.md)`')
n_rem = 0
for p in NORMATIVE:
    text = p.read_text(encoding='utf-8')
    for m in tok_re.finditer(text):
        tok = m.group(1)
        line = text[text.rfind('\n', 0, m.start())+1: text.find('\n', m.end()) if text.find('\n', m.end())>0 else len(text)]
        if is_param(tok) or tok in GENERATED or tok.startswith('claude/'):  # E5, E6
            continue
        if tok.endswith('-ERRATA-MD.md') and ('<' in tok or 'obra' in tok):
            continue
        if p.name == 'CONVENCOES.md' and ('Ex.:' in line or 'ex.:' in line or 'p. ex.' in line):  # E1
            continue
        if p.name == 'CLAUDE.md' and tok == 'log.md':  # E2 (resolve em wiki/log.md; menção em prosa)
            continue
        if tok.startswith('archive/'):
            continue
        n_rem += 1
        if not resolve_file(tok):
            fail('remissões', f'{p.relative_to(VAULT)}: `{tok}` não resolve')

# ---------- Check 2: wikilinks ----------
BASENAMES = {}
for r in REL:
    BASENAMES.setdefault(Path(r).stem, []).append(r)
wl_re = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]')
n_wl = 0
WIKI_SCAN = [p for p in MD_ALL if p.parts[len(VAULT.parts)] == 'wiki'
             and p.name not in ('log.md', 'telemetria.md')]  # E3, E4
for p in WIKI_SCAN:
    text = p.read_text(encoding='utf-8')
    for m in wl_re.finditer(text):
        tgt = N(m.group(1).strip())
        if is_param(tgt):  # E5
            continue
        n_wl += 1
        ok = (f'wiki/{tgt}.md' in ALL_FILES_NFC) or (f'wiki/{tgt}' in ALL_FILES_NFC) \
             or (tgt in BASENAMES) or (Path(tgt).name in BASENAMES) \
             or (f'{tgt}.md' in ALL_FILES_NFC) or (tgt in ALL_FILES_NFC)
        if not ok:
            fail('wikilinks', f'{p.relative_to(VAULT)}: [[{tgt}]] quebrado')

# ---------- Check 3: árvore documentada ↔ disco ----------
conv = (VAULT/'CONVENCOES.md').read_text(encoding='utf-8')
tree_block = re.search(r'```\n(cerebro-juridico-academico/.*?)```', conv, re.S).group(1)
doc_paths, stack = [], []
for raw_line in tree_block.splitlines()[1:]:
    line = raw_line.split('#')[0].rstrip()
    if not line.strip():
        continue
    m = re.match(r'^([│\s]*)(?:├──|└──)\s+(.*)$', line)
    if not m:
        continue
    depth = len(m.group(1).replace('│', ' ')) // 4
    name = m.group(2).strip()
    stack = stack[:depth] + [name]
    if is_param(name):
        continue
    if any(is_param(s) for s in stack[:-1]):
        continue
    doc_paths.append(''.join(stack[:-1]) + name)
n_tree = 0
for dp in doc_paths:
    n_tree += 1
    q = N(dp.rstrip('/'))
    if not ((VAULT/q).exists() or q in ALL_FILES_NFC):
        fail('árvore→disco', f'documentado mas ausente: {dp}')
# reverso: raiz e wiki/
SERVICE_WIKI = {'GLOSSARIO.md','PAINEL.md','ESTADO-RESUMO.md','MELHORIA.md','GATILHOS.md',
                'SUPRESSAO-LIST.md','VOZ-FINGERPRINT.md'}  # E7 - documentados na nomenclatura
doc_root = {d.split('/')[0].rstrip('/') if '/' in d else d for d in doc_paths}
doc_root |= {'raw', 'wiki', 'modelos', 'playbooks', 'identidade', 'archive'}
doc_root.add('CHANGELOG.md')  # E9 - documentado no § Versionamento do CLAUDE.md («na raiz do cofre»)
doc_root.add('ferramentas')  # E11 - ferramentas sob git na raiz do cofre (6.26, item F)
for item in VAULT.iterdir():
    nm = N(item.name)
    if nm.startswith('.') or nm in doc_root:
        continue
    fail('disco→árvore', f'na raiz do disco, fora da árvore: {nm}')
doc_wiki = {d[len('wiki/'):].rstrip('/') for d in doc_paths if d.startswith('wiki/') and d != 'wiki/'}
for item in (VAULT/'wiki').iterdir():
    nm = N(item.name)
    if nm.startswith('.') or nm in doc_wiki or nm in SERVICE_WIKI:
        continue
    fail('disco→árvore', f'em wiki/, fora da árvore e da nomenclatura: {nm}')

# ---------- Check 4: enum de tipos ↔ modelos ----------
enum_m = re.search(r'^tipo:\s*(.+)$', conv, re.M)
tipos = [t.strip() for t in enum_m.group(1).split('|')]
SINGULARES = {'painel','gatilhos','melhoria','lista-supressao','glossario','estado-resumo',
              'indice'}  # v2: `indice` - singular de máquina sem modelo (delta 6.18, agregado II)
modelos = {p.stem[len('modelo-'):] for p in (VAULT/'modelos').glob('modelo-*.md')}
n_enum = len(tipos)
for t in tipos:
    if t in SINGULARES:
        continue
    if t not in modelos:
        fail('enum↔modelos', f'tipo `{t}` sem modelo')
for mo in modelos:
    if mo not in tipos:
        fail('enum↔modelos', f'modelo `modelo-{mo}.md` sem tipo no enum')

# ---------- Check 5: tabela de ponteiros do CLAUDE.md ----------
claude = (VAULT/'CLAUDE.md').read_text(encoding='utf-8')
n_ptr = 0
for m in re.finditer(r'^\|[^|]+\|\s*`([^`]+)`\s*\|$', claude, re.M):
    tok = m.group(1).strip()
    if is_param(tok) or tok.startswith('claude/'):
        continue
    n_ptr += 1
    q = N(tok.rstrip('/'))
    if not ((VAULT/q).exists() or resolve_file(q)):
        fail('ponteiros', f'ponteiro morto: `{tok}`')

# ---------- Check 6: exemplos em nomenclatura natural ----------
n_ex = 0
slug = re.compile(r'(?:wiki|raw)/(?:[^`\s]*/)*([a-z][a-z0-9]+(?:-[a-z0-9]+)+)\.md')
for p in [VAULT/'CONVENCOES.md', VAULT/'CLAUDE.md'] + list(VAULT.glob('PROTOCOLO-*.md')):
    text = p.read_text(encoding='utf-8')
    for m in slug.finditer(text):
        base = m.group(1)
        if base.startswith('modelo') or base in ('index','log','telemetria'):
            continue
        n_ex += 1
        fail('nomenclatura', f'{p.name}: exemplo em slug pré-4.0: {m.group(0)}')

# ---------- Check 7 (v2): frontmatter mínimo de wiki/ ----------
FM_EXEMPT = {'index.md', 'log.md', 'telemetria.md', 'VOZ-EVOLUCAO.md',
             'Avaliação/_indice.md'}  # E10 - serviço/navegação sem frontmatter
def frontmatter_block(text):
    if not text.startswith('---'):
        return None
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    return m.group(1) if m else None
WIKI_PAGES = [p for p in MD_ALL if p.parts[len(VAULT.parts)] == 'wiki']
n_fm, n_fm_isentas = 0, 0
for p in WIKI_PAGES:
    rel_w = N(str(p.relative_to(VAULT/'wiki')))
    if rel_w in FM_EXEMPT:
        n_fm_isentas += 1
        continue
    n_fm += 1
    fm = frontmatter_block(p.read_text(encoding='utf-8'))
    if fm is None:
        fail('frontmatter', f'wiki/{rel_w}: sem frontmatter')
        continue
    tm = re.search(r'^tipo:\s*(\S+)', fm, re.M)
    if not tm:
        fail('frontmatter', f'wiki/{rel_w}: sem `tipo:`')
    elif tm.group(1) not in tipos:
        fail('frontmatter', f'wiki/{rel_w}: tipo `{tm.group(1)}` fora do enum das CONVENCOES')
    if not re.search(r'^titulo:\s*\S', fm, re.M):
        fail('frontmatter', f'wiki/{rel_w}: sem `titulo:`')

# ---------- Check 8 (v2): cobertura índice↔wiki, nos dois sentidos ----------
NAV_ROOT = {'index.md', 'log.md', 'PAINEL.md', 'ESTADO-RESUMO.md', 'telemetria.md',
            'MELHORIA.md', 'GLOSSARIO.md', 'SUPRESSAO-LIST.md', 'GATILHOS.md',
            'VOZ-EVOLUCAO.md', 'VOZ-FINGERPRINT.md', 'Faculdades.md'}
SKIP_DIRS = {'Inbox', 'Revisão', 'Auxiliares', 'archive'}
NAV_DIRS = {'Faculdades'}
SERVICE_DIRS = {'Avaliação'}

def classe_conhecimento(rel_parts, name):
    if any(N(x) in SKIP_DIRS for x in rel_parts[:-1]):
        return False
    if len(rel_parts) == 1:
        return N(name) not in NAV_ROOT
    head = N(rel_parts[0])
    return head not in NAV_DIRS and head not in SERVICE_DIRS

index_text = (VAULT/'wiki/index.md').read_text(encoding='utf-8')
index_targets = set()
n_idx_linhas = 0
for m in wl_re.finditer(index_text):
    tgt = N(m.group(1).strip())
    if is_param(tgt):  # E5 - modelos de linha comentados
        continue
    n_idx_linhas += 1
    index_targets.add(tgt)
    index_targets.add(Path(tgt).name)
    # sentido índice→disco (também coberto pelo check 2; aqui nomeado pelo contrato v2)
    ok = (f'wiki/{tgt}.md' in ALL_FILES_NFC) or (f'wiki/{tgt}' in ALL_FILES_NFC) \
         or (tgt in BASENAMES) or (Path(tgt).name in BASENAMES)
    if not ok:
        fail('índice↔wiki', f'linha do índice sem página no disco: [[{tgt}]]')
n_conh = 0
for p in WIKI_PAGES:
    rel = p.relative_to(VAULT/'wiki')
    if not classe_conhecimento(rel.parts, rel.name):
        continue
    n_conh += 1
    key = N(str(rel)[:-3])
    if key not in index_targets and N(rel.stem) not in index_targets:
        fail('índice↔wiki', f'página de conhecimento sem linha no índice: wiki/{key}.md')

# ---------- Check 9 (v3, 6.22): frescura dos derivados - contadores contra a verdade mecânica ----------
estado_txt = (VAULT/'wiki/ESTADO-RESUMO.md').read_text(encoding='utf-8')
conceitos_disk = len(list((VAULT/'wiki/Conceitos').glob('*.md')))
fontes_disk = len(list((VAULT/'wiki/Fontes').glob('*.md')))
comp_disk = ag_disk = 0
for p in (VAULT/'wiki/Conceitos').glob('*.md'):
    tt = p.read_text(encoding='utf-8')
    if re.search(r'^estado_comparativo:\s*comparativa\s*$', tt, re.M): comp_disk += 1
    if re.search(r'^estado_comparativo:\s*aguarda-comparativo\s*$', tt, re.M): ag_disk += 1
def errata_rows(p):
    n = 0
    for l in p.read_text(encoding='utf-8').splitlines():
        if l.startswith('|') and not l.startswith('| #') and not l.startswith('|--'): n += 1
    return n
asc_err = errata_rows(VAULT/'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-ERRATA-MD.md')
bm_err  = errata_rows(VAULT/'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md')
asc_mae_txt = (VAULT/'wiki/Fontes/Oliveira Ascensão, O Direito - Introdução e Teoria Geral.md').read_text(encoding='utf-8')
pares_cnt = []
m = re.search(r'\| Conceitos \| \*\*(\d+)\*\*', estado_txt);            pares_cnt.append(('ESTADO·Conceitos', m, conceitos_disk))
m = re.search(r'\| Fontes ingeridas \| \*\*(\d+)\*\*', estado_txt);     pares_cnt.append(('ESTADO·Fontes', m, fontes_disk))
m = re.search(r'\*\*(\d+) comparativas BM↔ASC\*\*', estado_txt);        pares_cnt.append(('ESTADO·comparativas', m, comp_disk))
m = re.search(r'\+ (\d+) `aguarda-comparativo`', estado_txt);           pares_cnt.append(('ESTADO·aguarda', m, ag_disk))
m = re.search(r'Erros de \*\*conversão\*\*: (\d+) entradas na ERRATA-MD', asc_mae_txt); pares_cnt.append(('mãe-ASC·erratas', m, asc_err))
for ln in estado_txt.splitlines():
    mm = re.search(r'ERRATA-MD com \*\*(\d+) entradas\*\*', ln)
    if mm:
        alvo, rot = (bm_err, 'BM') if 'Baptista Machado' in ln else (asc_err, 'ASC')
        pares_cnt.append((f'ESTADO·ERRATA-{rot}', mm, alvo))
# extensão do check 9 (6.26, ajuste de contrato aprovado a 2026-07-27): índice das vistas contra as vistas.
# O desalinhamento de 2026-07-24/26 nas cinco linhas foi apanhado pela Fase 4 da sessão 10 e não pelo crivo.
_fac = (VAULT/'wiki/Faculdades.md').read_text(encoding='utf-8')
_vistas_sem_par = []
for ln in _fac.splitlines():
    mm = re.match(r'- \[\[(Faculdades/[^\]]+)\]\](.*)$', ln)
    if not mm: continue
    alvo_f = VAULT/'wiki'/(mm.group(1) + '.md')
    par_idx = re.search(r'\((\d+) pontos; (\d+) cobertos', mm.group(2))
    if not alvo_f.exists():
        fail('contadores', f'índice de vistas: {mm.group(1)} não existe no disco')
        continue
    tv = alvo_f.read_text(encoding='utf-8')
    par_vista = re.search(r'\*\*(\d+) de (\d+) pontos cobertos\*\*', tv)
    if not par_idx or not par_vista:
        # não bloqueia: a vista pode contar por Partes e não por pontos; relata-se para não truncar em silêncio
        _vistas_sem_par.append(mm.group(1).split('/')[-1])
        continue
    cob_i, tot_i = int(par_idx.group(2)), int(par_idx.group(1))
    cob_v, tot_v = int(par_vista.group(1)), int(par_vista.group(2))
    if (cob_i, tot_i) != (cob_v, tot_v):
        fail('contadores', f'índice de vistas·{mm.group(1).split("/")[-1]}: o índice diz {cob_i} de {tot_i}, a vista diz {cob_v} de {tot_v}')
    else:
        pares_cnt.append((f'índice-vistas·{mm.group(1).split("/")[-1]}', par_idx, tot_i))

n_cnt = 0
for nome, m, verdade in pares_cnt:
    if not m:
        fail('contadores', f'{nome}: padrão não encontrado - o formato do derivado mudou; actualizar o contrato do crivo com ele')
    elif int(m.group(1)) != verdade:
        fail('contadores', f'{nome}: o derivado diz {m.group(1)}, a verdade mecânica é {verdade}')
    else:
        n_cnt += 1

# ---------- Check 10 (v3, 6.22): vigência - carimbo validado; ausência relatada sem bloqueio ----------
NORMA_RE = re.compile(r'\bart(?:s)?\.\s|\bartigo\s\d|\bDL\s?\d|Dec\.-Lei|\bCRP\b|\bdo CC\b|\bdo CPC\b|\bdo CPP\b')
sem_vig, n_vig = [], 0
for p in sorted((VAULT/'wiki/Conceitos').glob('*.md')):
    tt = p.read_text(encoding='utf-8')
    fm_v = frontmatter_block(tt) or ''
    vm = re.search(r'^vigencia_conferida:\s*(\S+)', fm_v, re.M)
    if vm:
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', vm.group(1)):
            fail('vigência', f'{p.name}: vigencia_conferida malformada ({vm.group(1)})')
        else:
            n_vig += 1
    elif NORMA_RE.search(tt):
        sem_vig.append(p.stem)

# ---------------- check 11 e 12: disciplina tipográfica e discursiva (2026-07-26) ----------------
def _spans_protegidos(t):
    """Intervalos onde o travessão se preserva: citação literal «», “”, código ` `, wikilink.

    O bloco `>` não isenta por si: a prosa do cofre em callout está sujeita à regra, e a
    citação longa em bloco preserva-se pelas aspas curvas que a house style já exige.
    """
    sp = []
    for pat, fl in [(r'«[^»]{0,4000}»', re.S), (r'\u201c[^\u201d]{0,4000}\u201d', re.S),
                    (r'`[^`\n]*`', 0), (r'\[\[[^\]]{0,300}\]\]', 0)]:
        for m in re.finditer(pat, t, fl):
            sp.append((m.start(), m.end()))
    return sp

def check_tipografia(vault):
    """Travessão «—» fora de citação literal, código ou wikilink. Excepção: fidelidade da citação."""
    falhas = []
    for f in sorted(vault.rglob('*.md')):
        if '.git' in f.parts or f.parts[len(vault.parts):][:1] in (('raw',), ('ferramentas',)):  # E11: relatórios de instrumento fora do escopo de escrita (6.27)
            continue
        t = f.read_text(encoding='utf-8')
        if '\u2014' not in t:
            continue
        sp = _spans_protegidos(t)
        for m in re.finditer('\u2014', t):
            i = m.start()
            if not any(a <= i < b for a, b in sp):
                ctx = t[max(0, i-45):i+45].replace('\n', ' ')
                falhas.append(f'[tipografia] travessão fora de citação: {f.relative_to(vault)} … {ctx} …')
    return falhas

def check_rotulo_tese(vault):
    """Parágrafo a abrir com rótulo a negrito seguido de . ou : (CONVENCOES, house style)."""
    falhas = []
    # duas formas: pontuação fora do negrito (**Gates**: …) e dentro (**Probe e partição.** …)
    pats = [re.compile(r'(?:\A|\n\n)\*\*((?:[^*\n]|\*(?!\*)){2,120}?)\*\*[.:]\s'),
            re.compile(r'(?:\A|\n\n)\*\*((?:[^*\n]|\*(?!\*)){2,120}?[.:])\*\*\s')]
    for f in sorted(vault.rglob('*.md')):
        if '.git' in f.parts or f.parts[len(vault.parts):][:1] in (('raw',), ('ferramentas',)):  # E11: relatórios de instrumento fora do escopo de escrita (6.27)
            continue
        t = f.read_text(encoding='utf-8')
        for pat in pats:
            for m in pat.finditer(t):
                falhas.append(f'[rótulo-tese] parágrafo abre com rótulo: {f.relative_to(vault)} … «{m.group(1)[:70]}»')
    return falhas


MOLDES_MOLDURA = [
    r'importa (?:notar|referir|dizer|sublinhar|frisar|ter presente)',
    r'convém (?:notar|referir|dizer|sublinhar|frisar|ter presente)',
    r'cumpre (?:notar|referir|dizer|sublinhar|frisar)',
    r'vale a pena (?:notar|referir|dizer|sublinhar|destacar|frisar)',
    r'é (?:de )?(?:notar|sublinhar|frisar|realçar|destacar) que',
    r'é importante (?:notar|referir|sublinhar|dizer|frisar)',
    r'note-se que', r'de sublinhar que', r'sublinhe-se que', r'refira-se que',
    r'dito isto', r'posto isto', r'isto dito', r'assente isto',
    r'em traços largos', r'reduzido ao essencial',
    r'a questão é a seguinte', r'o ponto é o seguinte', r'o essencial é o seguinte',
    r'diga-se desde já', r'adiante-se desde já',
    r'como veremos', r'como se verá', r'veremos adiante',
    r'h[áa] (?:dois|três|quatro|cinco|vários) (?:pontos|aspectos|planos|notas) a (?:considerar|reter|notar|assinalar)',
]
_MOLDURA_RE = re.compile(r'(?<![\w\u00c0-\u00ff])(' + '|'.join(MOLDES_MOLDURA) + r')', re.I)


def check_frase_moldura(vault):
    """Moldes de frase-moldura fora de citação, código ou wikilink (CONVENCOES, house style).

    O gate apanha os moldes recorrentes, que são finitos e catalogáveis; o critério da regra,
    a frase mais simples com maior profundidade jurídica, é de juízo e não se mecaniza. Lista
    deliberadamente estreita: só moldes que enquadram seja qual for o contexto, para que a
    falha seja sempre real. Ampliar a lista exige medir primeiro contra o cofre inteiro.
    """
    falhas = []
    for f in sorted(vault.rglob('*.md')):
        if '.git' in f.parts or f.parts[len(vault.parts):][:1] in (('raw',), ('ferramentas',)):  # E11: relatórios de instrumento fora do escopo de escrita (6.27)
            continue
        t = f.read_text(encoding='utf-8')
        sp = _spans_protegidos(t)
        for m in _MOLDURA_RE.finditer(t):
            i = m.start()
            if any(a <= i < b for a, b in sp):
                continue
            ctx = t[max(0, i-40):i+60].replace('\n', ' ')
            falhas.append(f'[frase-moldura] molde de enquadramento: {f.relative_to(vault)} … {ctx} …')
    return falhas


for _f in check_tipografia(VAULT):
    fail(*_f.split('] ', 1)) if False else failures.append(_f)
for _f in check_rotulo_tese(VAULT):
    failures.append(_f)
for _f in check_frase_moldura(VAULT):
    failures.append(_f)

# ---------- Relatório ----------
print(f'remissões verificadas: {n_rem} · wikilinks: {n_wl} · nós da árvore: {n_tree} · '
      f'tipos: {n_enum} · modelos: {len(modelos)} · ponteiros: {n_ptr}')
print(f'v2 - frontmatter: {n_fm} páginas verificadas ({n_fm_isentas} isentas E10) · '
      f'índice: {n_idx_linhas} linhas ↔ {n_conh} páginas de conhecimento')
if _vistas_sem_par:
    print('v3 - índice de vistas: ' + str(len(_vistas_sem_par)) + ' vista(s) sem par numérico «N de M pontos cobertos», fora do check por formato: ' + ', '.join(_vistas_sem_par))
print(f'v3 - contadores de derivados: {n_cnt}/{len(pares_cnt)} conferidos · '
      f'vigência: {n_vig} página(s) com carimbo válido · {len(sem_vig)} de conceito citam norma sem carimbo '
      f'[informativo até ao bloco de vigência]')
if failures:
    print(f'VERMELHO - {len(failures)} falha(s):')
    for f_ in failures:
        print('  ' + f_)
    sys.exit(1)
print('VERDE - passe estrutural sem falhas (exclusões codificadas E1-E11 aplicadas)')

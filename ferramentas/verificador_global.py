#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador mecânico global de citações - BM + Ascensão (reconstrução, conversa 10).
Níveis mecânicos (AUDITORIA, passe mecânico, alínea (a), três níveis + extensões 6.13(vi)):
  N1 exacta         - correspondência exacta no MD (normalização de espaços/hífens/aspas/ligaduras)
  N2 errata         - correspondência no MD após aplicação das correcções da ERRATA-MD
  N3 padrão         - correspondência por padrão documentado de conversão (transformação de confundíveis
                      derivada do relatório de padrões: 1/l, 0/O/º, rn/m, //l, acentos, pontuação, aspas)
  N4 fragmentos     - citação com elipses: cada fragmento longo verifica-se individualmente (N1-N3)
  N5 token-match    - ≥ 85% dos tokens da citação presentes na janela da âncora (folha±1)
  FE fora-de-escopo - justificadas: [sic] · fonte primária própria (DRE/EUR-Lex/DGSI/fac-símile) ·
                      interna-institucional sem âncora de obra · aparato de adjudicação visual (Fase 0)
Restante → CANDIDATA (adjudicação manual contra MD/PDF; uma falha real bloqueia).
"""
import re, sys, json, unicodedata
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # ferramentas/ vive na raiz do cofre (6.26, item F)
BM_MD = VAULT/'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador.md'
ASC_MD = VAULT/'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral.md'
BM_ERR = VAULT/'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md'
ASC_ERR = VAULT/'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-ERRATA-MD.md'
ASC_ADJ = VAULT/'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-ADJUDICACOES-OFICINA.jsonl'
ASC_MANT = VAULT/'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-MANTIDOS.txt'

# ---------------- normalizações ----------------
def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = s.replace('­', '')                      # soft hyphen
    s = s.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi').replace('ﬄ', 'ffl')
    s = re.sub(r'[«»""„”‟]', '"', s)
    s = re.sub(r"[''‛`´]", "'", s)
    s = re.sub(r'[—–‒−]', '-', s)
    s = re.sub(r'\*+', '', s)                        # itálico/negrito markdown
    s = re.sub(r'-\s*\n\s*', '', s)                  # hifenização de fim de linha
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def confus(s):
    """Transformação de confundíveis (nível padrão), aplicada aos DOIS lados."""
    s = norm(s).lower()
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('º', 'o').replace('°', 'o').replace('ª', 'a')
    s = s.replace('1', 'l').replace('0', 'o')
    s = s.replace('rn', 'm')
    s = re.sub(r'[^a-z0-9]', '', s)                  # remove tudo o que não é letra/dígito
    return s

def toks(s):
    return [t for t in re.findall(r'[a-z0-9]{4,}', confus_words(s))]

def confus_words(s):
    s = norm(s).lower()
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('º', 'o').replace('°', 'o')
    s = s.replace('1', 'l').replace('0', 'o')
    return re.sub(r'[^a-z0-9]+', ' ', s)

# ---------------- obras ----------------
class Obra:
    def __init__(self, key, md_path, err_path, p2f, adj_texts=()):
        self.key = key
        self.raw = md_path.read_text(encoding='utf-8')
        self.norm = norm(self.raw)
        self.p2f = p2f
        # folha -> texto (janela)
        self.folhas = {}
        parts = re.split(r'^\[p\. (\d+)\]\s*$', self.raw, flags=re.M)
        for i in range(1, len(parts), 2):
            self.folhas[int(parts[i])] = parts[i+1]
        # errata: pares MD→PDF (disciplina de células)
        self.err_pairs, self.err_right = [], []
        if err_path.exists():
            for line in err_path.read_text(encoding='utf-8').splitlines():
                if not line.startswith('|') or line.startswith('| #') or line.startswith('|--'):
                    continue
                cells = [c.strip() for c in line.strip('|').split('|')]
                if len(cells) < 4:
                    continue
                md_fr = re.findall(r'«([^«»]+)»', cells[2])
                pdf_fr = re.findall(r'«([^«»]+)»', cells[3])
                self.err_right += [norm(f) for f in pdf_fr]
                # emparelhamento posicional: as notas editoriais no fim da célula direita
                # podem conter «» próprios - os fragmentos correspondentes são os primeiros k
                if md_fr and pdf_fr and len(pdf_fr) >= len(md_fr):
                    self.err_pairs += list(zip(md_fr, pdf_fr[:len(md_fr)]))
        corrected = self.norm
        # fragmentos mais longos primeiro - evita a interferência de substituições contidas
        for a, b in sorted(self.err_pairs, key=lambda p: -len(norm(p[0]))):
            corrected = corrected.replace(norm(a), norm(b))
        self.corrected = corrected
        self.conf = confus(self.raw)
        self.conf_corrected = confus(corrected)
        # variante de fluxo: sem marcadores [p. N] nem cabeçalhos correntes; sem dígitos (classe B11)
        flow = re.sub(r'\[p\. \d+\]', ' ', self.norm)
        for h in ('Introdução ao Direito e ao discurso legitimador',
                  'A ciência jurídica', 'Prolegómenos do discurso legitimador',
                  'Prolegómencs do discurso legitimador', 'Proíegómenos do discurso legitimador',
                  'A aplicação da lei no tempo e no espaço'):
            flow = flow.replace(h, ' ')
        self.flow_conf = re.sub(r'[0-9]', '', confus(flow))
        self.adj_texts = [norm(t) for t in adj_texts if t]

    def window(self, pages):
        fol = set()
        for p in pages:
            for q in (p-0, ):
                f = self.p2f(q)
                if f: fol.update({f-1, f, f+1})
        txt = ' '.join(self.folhas.get(f, '') for f in sorted(fol))
        return txt

def bm_p2f(p):
    if p == 359: return 181
    if p < 5: return None
    return (p + 4)//2 if p % 2 == 0 else (p + 3)//2

def asc_p2f(p):
    if 9 <= p <= 621: return p - 5
    if 647 <= p <= 658: return p - 29
    return None

adj_texts = []
if ASC_ADJ.exists():
    for line in ASC_ADJ.read_text(encoding='utf-8').splitlines():
        try:
            j = json.loads(line)
            for k in ('depois', 'antes', 'leitura', 'texto', 'forma', 'correcto', 'md', 'pdf'):
                v = j.get(k)
                if isinstance(v, str): adj_texts.append(v)
        except Exception:
            pass
if ASC_MANT.exists():
    adj_texts += re.findall(r'«([^«»]+)»', ASC_MANT.read_text(encoding='utf-8'))

BM = Obra('BM', BM_MD, BM_ERR, bm_p2f)
ASC = Obra('ASC', ASC_MD, ASC_ERR, asc_p2f, adj_texts)

# ---------------- extracção de citações ----------------
# Escopo (alargado na conversa 20, cisão de 2026-07-25): Conceitos/ inteiro (inclui as
# sub-páginas de posição da fissão) + todas as páginas de wiki/Fontes/ das duas obras
# (página-mãe e sub-páginas de leitura «— leitura da sessão N»). As institucionais
# (fichas de UC, guias, capturas) continuam fora do confronto mecânico.
SCOPE_FILES = sorted((VAULT/'wiki/Conceitos').glob('*.md')) + sorted(
    p for p in (VAULT/'wiki/Fontes').glob('*.md')
    if ('Baptista Machado' in p.name) or ('Ascensão' in p.name)
)
INSTITUCIONAIS = [p for p in (VAULT/'wiki/Fontes').glob('*.md') if p not in SCOPE_FILES] \
               + list((VAULT/'wiki/Faculdades').glob('*.md')) + [VAULT/'wiki/Faculdades.md']

PRIMARIA_RE = re.compile(r'DRE|EUR-Lex|CELEX|DGSI|Diário do Governo|consolidad|parlamento\.pt|INCM|'
                         r'LexLink|informador\.pt|fac-símile|Legislação Consolidada|\bCPC\b|C\.P\.C\.|'
                         r'Estatuto dos Magistrados|redacção do DL|texto originário|do Código Civil, citado', re.I)
APARATO_RE = re.compile(r'PORBASE|Wikipédia|catálogo|Discovery|dedicatória|cota|manuscrit|carimbo|'
                        r'lombada|rosto do exemplar|Reg\.\s*:|ex-líbris|Rosto:|ficha técnica|'
                        r'PhilPapers|Google Books|Âncoras: folha|O Direito Online|APDI', re.I)
REGISTO_RE = re.compile(r'ERRATA|[Ee]rrata|adjudicad|300 dpi|600 dpi|gralha|defeito de impressão|'
                        r'[Oo]scilaç|byte-fiel|\bE2\b|no impresso|o exemplar imprime|imprime-se|'
                        r'pelo OCR|v\. Erratas|camada de texto', re.I)
INTERNA_RE = re.compile(r'^(BM, cap\.|Tese central$|Paginação do exemplar$|Planos do trabalho$|'
                        r'lote \d$|o lote 2 decide-se|cap\. [IVX]+, Secção|§ ?[\dl]\.?[ºo°]?$)')
INSTIT_CTX_RE = re.compile(r'ficha \d{4}|ficha da|guia \d{4}|o guia|bibliografia|ISBN|manual assinalado|'
                           r'prescrita|programa|ponto \d|Parte [IVX]+|Secção [IVX]+ \(|bloco [IVX]+', re.I)
SIC_RE = re.compile(r'\[sic')
PAGE_RE = re.compile(r'pp?\.\s*(\d{1,3})(?:\s*[-–—e,]\s*(\d{1,3}))?')

def obra_of(ctx_before, default):
    b = ctx_before[-260:]
    ia = max(b.rfind('Ascensão'), b.rfind('O Direito'), b.rfind('ASC'))
    ib = max(b.rfind('BM'), b.rfind('Machado'), b.rfind('Baptista'))
    if ia > ib and ia >= 0: return ASC
    if ib >= 0: return BM
    return default

def pages_near(ctx):
    pgs = []
    for m in PAGE_RE.finditer(ctx):
        a = int(m.group(1)); pgs.append(a)
        if m.group(2):
            b = int(m.group(2))
            if b > a and b - a < 12: pgs.extend(range(a+1, b+1))
    return pgs

results = {'exacta':0, 'errata':0, 'padrao':0, 'fragmentos':0, 'token':0}
fe = {'sic':0, 'primaria':0, 'institucional':0, 'aparato':0, 'registo':0, 'interna':0, 'instit_ctx':0}
candidatas = []
total_escopo = 0

def match_levels(q, obra):
    variants = [q]
    q_ell = re.sub(r'^(…|\.\.\.)\s*|\s*(…|\.\.\.)$', '', q)
    if q_ell != q:
        variants.append(q_ell)
    if '[' in q:
        variants.append(re.sub(r'\[[^\]]{1,12}\]', '', q))   # inserção editorial removida
        variants.append(q.replace('[', '').replace(']', '')) # parêntesis rectos dissolvidos
    for v in variants:
        nq = norm(v)
        if len(nq) < 3: return 'exacta'
        if nq in obra.norm: return 'exacta'
        if nq in obra.corrected: return 'errata'
        if any(nq in r or (len(r) > 8 and r in nq) for r in obra.err_right if len(r) > 8):
            return 'errata'
        cq = confus(v)
        if len(cq) >= 6 and (cq in obra.conf or cq in obra.conf_corrected): return 'padrao'
        fq = re.sub(r'[0-9]', '', cq)
        if len(fq) >= 10 and fq in obra.flow_conf: return 'padrao'
        if obra.adj_texts and any(nq in t or t in nq for t in obra.adj_texts if len(t) > 5):
            return 'padrao'
        frs = [f for f in re.split(r'…|\[\.\.\.\]|\.\.\.|\(\.\.\.\)', v) if len(norm(f)) >= 10]
        if len(frs) >= 2:
            if all((norm(f) in obra.norm) or (norm(f) in obra.corrected) or
                   (len(confus(f)) >= 6 and confus(f) in obra.conf) for f in frs):
                return 'fragmentos'
    return None

for path in SCOPE_FILES:
    text = path.read_text(encoding='utf-8')
    default = ASC if 'Ascensão' in path.name else BM
    for m in re.finditer(r'«([^«»]+)»', text):
        q = m.group(1)
        ctx_b = text[max(0, m.start()-300):m.start()]
        ctx_a = text[m.end():m.end()+300]
        ctx = ctx_b + ' ' + ctx_a
        total_escopo += 1
        if SIC_RE.search(q) or SIC_RE.search(ctx_a[:80]):
            fe['sic'] += 1; continue
        if INTERNA_RE.match(q.strip()):
            fe['interna'] += 1; continue
        obra = obra_of(ctx_b, default)
        lvl = match_levels(q, obra)
        if lvl is None and obra is not default:
            alt = match_levels(q, default)
            if alt: obra, lvl = default, alt
        if lvl is None:
            other = ASC if obra is BM else BM
            alt = match_levels(q, other)
            if alt: obra, lvl = other, alt
        if lvl:
            results[lvl] += 1; continue
        # fora-de-escopo justificadas (só depois de falhar o match mecânico)
        if PRIMARIA_RE.search(ctx) or PRIMARIA_RE.search(q):
            fe['primaria'] += 1; continue
        if REGISTO_RE.search(ctx):
            fe['registo'] += 1; continue
        if APARATO_RE.search(ctx) or APARATO_RE.search(q):
            fe['aparato'] += 1; continue
        if INSTIT_CTX_RE.search(ctx):
            fe['instit_ctx'] += 1; continue
        # token-match na janela da âncora
        pgs = pages_near(ctx_b[-160:] + ' ' + ctx_a[:160])
        done = False
        if pgs:
            win = confus_words(obra.window(pgs))
            wset = set(win.split())
            tt = toks(q)
            if len(tt) >= 5 and tt and sum(1 for t in tt if t in wset)/len(tt) >= 0.85:
                results['token'] += 1; done = True
        if not done:
            candidatas.append({
                'ficheiro': str(path.relative_to(VAULT)), 'obra': obra.key,
                'citacao': q if len(q) < 220 else q[:217]+'…',
                'anchor_pages': pgs[:6],
                'ctx': re.sub(r'\s+', ' ', (ctx_b[-110:] + ' ⟪…⟫ ' + ctx_a[:110]))
            })

# institucionais: contam como fora-de-escopo justificado (sem âncora de obra)
inst = 0
for path in INSTITUCIONAIS:
    inst += len(re.findall(r'«[^«»]+»', path.read_text(encoding='utf-8')))
fe['institucional'] = inst

mech = sum(results.values())
print(f'ESCOPO (Conceitos + 2 páginas de fonte): {total_escopo} citações · '
      f'institucionais fora-de-escopo: {inst}')
print(f"  exactas {results['exacta']} · errata {results['errata']} · padrão {results['padrao']} · "
      f"fragmentos {results['fragmentos']} · token {results['token']}  (mecânicas: {mech})")
print(f"  fora-de-escopo justificadas: [sic] {fe['sic']} · primária própria {fe['primaria']} · "
      f"registo de errata/adjudicação {fe['registo']} · aparato Fase 0 {fe['aparato']} · "
      f"remissões internas {fe['interna']} · citações de programa em página de obra {fe['instit_ctx']} · "
      f"institucionais {fe['institucional']}")
print(f'  CANDIDATAS por adjudicar: {len(candidatas)}')
(Path(__file__).resolve().parent / 'candidatas.json').write_text(
    json.dumps(candidatas, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'  erratas BM aplicáveis mecanicamente: {len(BM.err_pairs)} pares · ASC: {len(ASC.err_pairs)} pares · '
      f'pool adjudicado ASC: {len(ASC.adj_texts)} formas')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crivo de citações - gate BLOQUEANTE do fecho (delta 6.26).

Nasce da conversa 27, onde treze citações entraram no cofre sem letra confirmada e a
varredura seguinte encontrou mais dezassete herdadas na mesma condição. O verificador
global contava-as como «candidatas por adjudicar» e deixava passar o fecho; este crivo
não deixa. A regra que ele mecaniza é a regra 8 do CLAUDE.md endurecida: aspas curvas
só para letra confirmada da fonte, e o que não bate mecanicamente tem de trazer, na
mesma frase, o marcador que diz porquê.

Quatro checks, todos bloqueantes:

  C1 COBERTURA   toda a citação «…» com âncora de página numa obra do corpo bate
                 exactamente no derivado dessa obra (com errata e padrões aplicados),
                 ou traz marcador explícito na própria frase (adjudicado por imagem,
                 firmado por imagem, paráfrase, [sic], em relato, zona fraca).
  C2 ÂNCORA      resolvendo a citação, a folha onde resolve fica a ±1 da página
                 declarada na frase. POR CALIBRAR: no controlo negativo da c27 este
                 check NÃO apanhou uma âncora deslocada em cinco, e no BM dispara em
                 falso por o mapeamento folha↔página não estar fixado. Fica informativo
                 e NÃO bloqueia até passar controlo positivo e negativo, pela regra que
                 esta própria conversa fixou: instrumento por calibrar não é gate.
  C3 PLACEHOLDER nenhuma página de wiki/ fica com marcador de trabalho por concluir
                 («contagem mecânica no fecho», «a fixar no fecho», «{Por preencher»,
                 «TBD»), salvo a «Tese central» da página-mãe de obra em leitura.
  C4 EQUILÍBRIO  nenhuma linha de prosa fecha com aspas curvas desequilibradas.

Uso: python3 crivo_citacoes.py [--vault CAMINHO]
Saída: VERDE, ou VERMELHO com a lista e código de saída 1.
"""
import re, sys, unicodedata
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # ferramentas/ vive na raiz do cofre (6.26, item F)
if '--vault' in sys.argv:
    VAULT = Path(sys.argv[sys.argv.index('--vault') + 1])

OBRAS = {
    'ASC': dict(
        md=VAULT / 'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral.md',
        err=VAULT / 'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-ERRATA-MD.md',
        offset=21007, desvio=5),
    'BM': dict(
        md=VAULT / 'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador.md',
        err=VAULT / 'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md',
        offset=0, desvio=0),
}

MARCADORES = re.compile(
    r'adjudicad\w*\s+por\s+imagem|firmad\w*\s+por\s+imagem|por\s+imagem|'
    r'par[áa]frase|\[sic\]|em\s+relato|zona\s+fraca|'
    r'atravessa\s+a\s+quebra|fora\s+das\s+aspas|assim\s+no\s+impresso|'
    r'errata|verifica[çc][ãa]o\s+em\s+aberto|por\s+confirmar',
    re.I)

def N(s):
    s = unicodedata.normalize('NFC', s).replace('­', '')
    s = re.sub(r'\[p\.\s*\d+\]', '', s)
    s = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', s)
    s = re.sub(r'(?<=[a-zà-ÿ])-(?=[a-zà-ÿ])', '', s)   # translineação sem quebra de linha
    s = re.sub(r'\s\d{1,3}(?=[\s.,;:)])', ' ', s)      # marcadores de nota de rodapé
    s = re.sub(r'[«»"“”\'’‘*_`\[\]]', ' ', s)
    s = re.sub(r'[-–—]', '-', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

def confundiveis(s):
    """padrões de conversão documentados: rn/m, 1/l, 0/O, acentos perdidos."""
    s = s.replace('rn', 'm').replace('1', 'l').replace('0', 'o')
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()

def carrega(cfg):
    t = cfg['md'].read_text(encoding='utf-8')[cfg['offset']:]
    marcas = [(m.start(), int(m.group(1))) for m in re.finditer(r'\[p\.\s*(\d+)\]', t)]
    pag = {}
    for i, (pos, n) in enumerate(marcas):
        fim = marcas[i + 1][0] if i + 1 < len(marcas) else len(t)
        pag[n + cfg['desvio']] = N(t[pos:fim])
    return pag, N(t)

def pares_errata(path):
    """pares (deformado, correcto) das colunas «…» simétricas da ERRATA-MD."""
    pares = []
    if not path.exists():
        return pares
    for linha in path.read_text(encoding='utf-8').split('\n'):
        if not linha.startswith('| '):
            continue
        cols = [c.strip() for c in linha.split('|')]
        if len(cols) < 5:
            continue
        esq = re.findall(r'«([^«»]+)»', cols[3])
        dir_ = re.findall(r'«([^«»]+)»', cols[4])
        if len(esq) == len(dir_):
            pares += list(zip(esq, dir_))
    return pares

CORPO, TODO, ERR = {}, {}, {}
for rot, cfg in OBRAS.items():
    if cfg['md'].exists():
        CORPO[rot], TODO[rot] = carrega(cfg)
        ERR[rot] = pares_errata(cfg['err'])

def aplica_errata(texto, rot):
    for mau, bom in ERR.get(rot, []):
        texto = texto.replace(N(mau), N(bom))
    return texto

# pré-computa uma vez por obra: corpo com errata aplicada e corpo em confundíveis.
TODO_ERR = {rot: aplica_errata(TODO[rot], rot) for rot in TODO}
TODO_CONF = {rot: confundiveis(TODO[rot]) for rot in TODO}
CORPO_CONF = {rot: {p: confundiveis(w) for p, w in CORPO[rot].items()} for rot in CORPO}

# ---- extracção das citações com a âncora da própria frase ----
ANC = re.compile(r'\((?:ASC|BM|[A-Z][a-zÀ-ÿ]+(?:\s+[A-Z][a-zÀ-ÿ]+)*)?,?\s*p{1,2}\.\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?', re.I)
CIT = re.compile(r'«([^«»]{25,})»')

def frases(texto):
    """corta em frases, preservando as aspas curvas."""
    return re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«*])', texto)

def paginas_da_frase(fr):
    out = []
    for m in ANC.finditer(fr):
        out.append(int(m.group(1)))
        if m.group(2):
            out.append(int(m.group(2)))
    return out

falhas = []
informativos = []
cits_total = cits_cobertas = 0

alvos = sorted(list((VAULT / 'wiki').rglob('*.md')))
for f in alvos:
    rel = f.relative_to(VAULT).as_posix()
    if rel.endswith(('index.md', 'telemetria.md')):
        continue
    txt = f.read_text(encoding='utf-8')

    # --- C3 placeholder ---
    ehmae = 'leitura da sessão' not in rel and rel.startswith('wiki/Fontes/')
    for m in re.finditer(r'contagem mecânica no fecho|a fixar no fecho|\{Por preencher|\bTBD\b', txt):
        ctx = txt[max(0, m.start() - 120):m.start() + 60]
        if ehmae and 'Tese central' in ctx:
            continue
        falhas.append(('C3 placeholder', rel, re.sub(r'\s+', ' ', ctx)[-110:]))

    for bruto in txt.split('\n'):
        linha = bruto.strip()
        if not linha or linha.startswith('|'):
            continue
        # --- C4 equilíbrio ---
        if linha.count('«') != linha.count('»'):
            falhas.append(('C4 aspas desequilibradas', rel, linha[:120]))

    # --- C1/C2 cobertura e âncora ---
    for fr in frases(txt):
        if fr.lstrip().startswith('|'):
            continue
        pags = paginas_da_frase(fr)
        for m in CIT.finditer(fr):
            cit = m.group(1)
            if not pags:
                continue
            cits_total += 1
            # citação com elipse verifica-se por fragmentos: cada troço longo tem de
            # bater, porque o elidido, por definição, não está no texto seguido.
            trocos = [N(x) for x in re.split(r'\[\s*(?:\.\.\.|…|\u2026)\s*\]|\[…\]|\.\.\.', cit)]
            trocos = [x for x in trocos if len(x) >= 18]
            alvo = N(cit)
            resolveu = None
            for rot in CORPO:
                corpo = TODO[rot]
                if alvo in corpo:
                    resolveu = rot
                    break
                if len(trocos) > 1 and all(x in corpo for x in trocos):
                    resolveu = rot
                    break
                if aplica_errata(alvo, rot) in corpo or alvo in TODO_ERR[rot]:
                    resolveu = rot
                    break
                if confundiveis(alvo) in TODO_CONF[rot]:
                    resolveu = rot
                    break
            if resolveu is None:
                if not MARCADORES.search(fr):
                    falhas.append(('C1 citação sem cobertura nem marcador', rel,
                                   f'p.{pags[0]} «{cit[:88]}»'))
                else:
                    cits_cobertas += 1
                continue
            cits_cobertas += 1
            # C2: onde resolve?
            alvo_conf = confundiveis(alvo)
            onde = [p for p, w in CORPO[resolveu].items() if alvo in w]
            if not onde:
                onde = [p for p, w in CORPO_CONF[resolveu].items() if alvo_conf in w]
            if onde and pags and not any(abs(p - a) <= 1 for p in onde for a in pags):
                # C2 só vale onde o mapeamento folha↔página está estabelecido. No ASC é
                # página = folha + 5, conferido por âncoras. No BM o derivado tem mais do
                # que uma página da obra por marcador `[p. N]` e o mapeamento não está
                # fixado: enquanto não estiver, o achado é informativo e não bloqueia,
                # porque um gate que dispara em falso ensina a ignorá-lo.
                informativos.append(
                    ('C2 âncora fora de sítio', rel,
                     f'declara p.{pags} · resolve em p.{sorted(onde)[:3]} · «{cit[:70]}»'))

print(f'citações com âncora verificadas: {cits_total} · cobertas: {cits_cobertas}')
if informativos:
    print(f'[informativo, não bloqueante] {len(informativos)} âncoras do BM fora de sítio pelo '
          f'mapeamento por estabelecer - o derivado do BM não tem uma página da obra por marcador.')
if falhas:
    print(f'VERMELHO - {len(falhas)} falha(s) bloqueantes:')
    for tipo, ficheiro, det in falhas[:80]:
        print(f'  [{tipo}] {ficheiro}')
        print(f'      {det}')
    if len(falhas) > 80:
        print(f'  … e mais {len(falhas) - 80}')
    sys.exit(1)
print('VERDE - crivo de citações sem falhas bloqueantes (C1 cobertura · C3 placeholder · C4 equilíbrio; C2 informativo, por calibrar)')

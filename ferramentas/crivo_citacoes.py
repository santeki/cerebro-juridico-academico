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
                 no derivado dessa obra - por ordem: exacta → errata → canonização
                 das decorações (6.26, item A) → confundíveis - ou traz marcador
                 explícito na própria frase (adjudicado por imagem, firmado por
                 imagem, paráfrase, [sic], em relato, zona fraca).
  C2 ÂNCORA      resolvendo a citação, a página da obra onde resolve fica a ±1 da
                 página declarada na frase. O mapeamento folha↔página está portado
                 do verificador global (ASC: página = folha+5 no miolo, +29 nas
                 folhas finais; BM: folha N = páginas 2N-4/2N-3, excepção folha
                 181). Continua INFORMATIVO e NÃO bloqueia (6.26, item B adiado):
                 a âncora que governa cada citação não é extraível com fiabilidade
                 do formato actual das frases.
  C3 PLACEHOLDER nenhuma página de wiki/ fica com marcador de trabalho por concluir
                 («contagem mecânica no fecho», «a fixar no fecho», «{Por preencher»,
                 «TBD»), salvo a «Tese central» da página-mãe de obra em leitura.
  C4 EQUILÍBRIO  nenhuma linha de prosa fecha com aspas curvas desequilibradas.

Uso: python3 crivo_citacoes.py [--vault CAMINHO] [--dump FICHEIRO.json]
Saída: VERDE, ou VERMELHO com a lista e código de saída 1.
"""
import json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent  # ferramentas/ vive na raiz do cofre (6.26, item F)
if '--vault' in sys.argv:
    VAULT = Path(sys.argv[sys.argv.index('--vault') + 1])

# ---- mapeamento folha↔página, portado do verificador_global (bm_p2f/asc_p2f) ----
def asc_f2p(f):
    """ASC: página da obra = folha+5 nas folhas 5-350 e 353-615; +29 nas 621-629."""
    if 5 <= f <= 350 or 353 <= f <= 615:
        return [f + 5]
    if 621 <= f <= 629:
        return [f + 29]
    return []

def bm_f2p(f):
    """BM: folha N = páginas 2N-4 e 2N-3; excepção: a folha 181 só tem a p. 359
    (o verso, p. 358, não tem imagem no exemplar)."""
    if f == 181:
        return [359]
    return [p for p in (2 * f - 4, 2 * f - 3) if p >= 1]

OBRAS = {
    'ASC': dict(
        md=VAULT / 'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral.md',
        err=VAULT / 'raw/Biblioteca/Doutrina/Livros/José de Oliveira Ascensão/O Direito - Introdução e Teoria Geral-ERRATA-MD.md',
        f2p=asc_f2p, corte=True),   # corte no primeiro marcador [p. N] real (fim do índice gerado)
    'BM': dict(
        md=VAULT / 'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador.md',
        err=VAULT / 'raw/Biblioteca/Doutrina/Livros/João Baptista Machado/Introdução ao Direito e ao Discurso Legitimador-ERRATA-MD.md',
        f2p=bm_f2p, corte=False),
}

# marcador de folha REAL: linha própria, como no verificador_global (o índice gerado
# traz «[p. N]» em linha corrida e não é folha)
MARCA = re.compile(r'(?m)^\[p\.\s*(\d+)\]\s*$')

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

# ---- nível 3: canonização das decorações (6.26, item A) ----
def canoniza(s, derivado=False):
    """Canonização das decorações (6.26, item A) - terceiro nível do passe mecânico,
    aplicada simetricamente aos dois lados da comparação. Canoniza APENAS:
      (a) ordinal deformado: «N.º» ↔ «N. 0»/«N. o»/«N.0» (espaço-zero do padrão A1);
      (b) aspas: todas as variantes (rectas, curvas, «», baixas, ruído catalogado);
      (c) ênfase: marcadores markdown de itálico/negrito (*, **, _);
      (d) pontuação-ruído catalogada no relatório da Oficina: ~, \\_, •, · (A4/A6/A7);
      (e) chamada de nota: dígitos colados ao fim de palavra, SÓ no lado do derivado;
      (f) translineação: hífen+quebra dentro de palavra.
    REGRA ABSOLUTA: os dígitos não se alteram nem se dobram nesta camada (nada de
    1→l, 0→o) - o risco jurídico vive nos números; a dobra de confundíveis é nível
    separado e posterior."""
    s = unicodedata.normalize('NFC', s).replace('­', '')
    s = re.sub(r'\[p\.\s*\d+\]', ' ', s)                      # marcadores de folha
    # (f) translineação: hífen+quebra dentro de palavra
    s = re.sub(r'([A-Za-zÀ-ÿ])-\s*\n\s*(?=[A-Za-zà-ÿ])', r'\1', s)
    # (a) ordinal deformado - ANTES de baixar a caixa: o «O» maiúsculo depois de
    # número é artigo («160. O fim do direito»), nunca se dobra (controlo c28)
    s = re.sub(r'(?<=[nN])\.\s*[ºo0°](\s?s)?(?=[\s.,;:)\]»"”*_/-]|$)',
               lambda m: '.º' + ('s' if m.group(1) else ''), s)
    s = re.sub(r'(?<=\d)\.\s*[ºo0°](?=[\s.,;:)\]»"”*_/-]|$)', '.º', s)
    # (b) aspas: todas as variantes para uma forma única (removidas)
    s = re.sub(r'[«»"“”„‟\'’‘‛`´]', ' ', s)
    # (c) ênfase markdown; (d) pontuação-ruído catalogada (\_, ~, •, ·)
    s = re.sub(r'\\_', ' ', s)
    s = re.sub(r'[*_]+', '', s)
    s = re.sub(r'[~•·]+', ' ', s)
    # (e) chamada de nota - SÓ no derivado: dígitos que seguem letra e precedem
    # espaço/pontuação. Número que faz parte do texto (artigo, página, data) tem
    # separador antes e NUNCA se suprime.
    if derivado:
        s = re.sub(r'(?<=[A-Za-zÀ-ÿ])\d{1,3}(?=[\s.,;:)\]]|$)', '', s)
    # travessões para hífen; translineação residual dentro de palavra
    s = re.sub(r'[–—‒−]', '-', s)
    s = re.sub(r'(?<=[a-zà-ÿ])-\s*-?\s*(?=[a-zà-ÿ])', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

def carrega(cfg):
    t = cfg['md'].read_text(encoding='utf-8')
    if cfg.get('corte'):
        m0 = MARCA.search(t)
        if m0:
            t = t[m0.start():]        # corta o preâmbulo/índice antes do primeiro marcador real
    marcas = [(m.start(), int(m.group(1))) for m in MARCA.finditer(t)]
    pag = {}
    for i, (pos, folha) in enumerate(marcas):
        fim = marcas[i + 1][0] if i + 1 < len(marcas) else len(t)
        for p in cfg['f2p'](folha):   # páginas da OBRA, pelo mapeamento folha↔página
            pag[p] = (N(t[pos:fim]), canoniza(t[pos:fim], derivado=True))
    return pag, t

def _sem_notas(cel):
    """remove as notas editoriais [—] da célula, mas SÓ fora dos fragmentos «»:
    pela disciplina das células as notas vivem fora dos fragmentos e podem conter
    «» próprios (que poluiriam a extracção); parêntesis rectos DENTRO de um
    fragmento são letra byte-fiel do MD e ficam."""
    out, depth, dentro = [], 0, False
    for ch in cel:
        if depth == 0 and ch == '«':
            dentro = True; out.append(ch); continue
        if depth == 0 and ch == '»':
            dentro = False; out.append(ch); continue
        if not dentro and ch == '[':
            depth += 1; continue
        if not dentro and ch == ']':
            if depth: depth -= 1
            else: out.append(ch)
            continue
        if depth == 0:
            out.append(ch)
    return ''.join(out)

def pares_errata(path):
    """pares (deformado, correcto) das colunas «…» da ERRATA-MD. Tolerante às notas
    editoriais: remove-as primeiro (fora dos fragmentos) e, quando as contagens das
    duas células divergem, emparelha os primeiros k = min(n_esq, n_dir), como faz o
    verificador global - em vez de descartar a linha inteira."""
    pares = []
    if not path.exists():
        return pares
    for linha in path.read_text(encoding='utf-8').splitlines():
        if not linha.startswith('|') or linha.startswith('| #') or linha.startswith('|--'):
            continue
        cols = [c.strip() for c in linha.strip('|').split('|')]
        if len(cols) < 4:
            continue
        esq = re.findall(r'«([^«»]+)»', _sem_notas(cols[2]))
        dir_ = re.findall(r'«([^«»]+)»', _sem_notas(cols[3]))
        k = min(len(esq), len(dir_))
        for mau, bom in zip(esq[:k], dir_[:k]):
            if len(N(mau)) >= 4:      # pares minúsculos («u»…) corromperiam o corpo inteiro
                pares.append((mau, bom))
    return pares

CORPO, TODO, RAW, ERR = {}, {}, {}, {}
for rot, cfg in OBRAS.items():
    if cfg['md'].exists():
        CORPO[rot], RAW[rot] = carrega(cfg)
        TODO[rot] = N(RAW[rot])
        ERR[rot] = pares_errata(cfg['err'])

def aplica_errata(texto, rot):
    # fragmentos mais longos primeiro - evita a interferência de substituições contidas
    for mau, bom in sorted(ERR.get(rot, []), key=lambda p: -len(N(p[0]))):
        texto = texto.replace(N(mau), N(bom))
    return texto

# pré-computa uma vez por obra: corpo com errata aplicada, corpo em confundíveis e
# corpo canonizado (nível 3 - 6.26, item A), com e sem errata.
TODO_ERR = {rot: aplica_errata(TODO[rot], rot) for rot in TODO}
TODO_CONF = {rot: confundiveis(TODO[rot]) for rot in TODO}
TODO_CAN = {rot: canoniza(RAW[rot], derivado=True) for rot in TODO}
TODO_CAN_ERR = {}
for rot in TODO:
    t = TODO_CAN[rot]
    for mau, bom in sorted(ERR.get(rot, []), key=lambda p: -len(canoniza(p[0]))):
        cm = canoniza(mau, derivado=True)
        if len(cm) >= 4:
            t = t.replace(cm, canoniza(bom))
    TODO_CAN_ERR[rot] = t
CORPO_CONF = {rot: {p: confundiveis(w[0]) for p, w in CORPO[rot].items()} for rot in CORPO}

# ---- extracção das citações com a âncora da própria frase ----
ANC = re.compile(r'\((?:ASC|BM|[A-Z][a-zÀ-ÿ]+(?:\s+[A-Z][a-zÀ-ÿ]+)*)?,?\s*p{1,2}\.\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?', re.I)
CIT = re.compile(r'«([^«»]{25,})»')
ELIPSE = re.compile(r'\[\s*(?:\.\.\.|…|…)\s*\]|\[…\]|\.\.\.')

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

def resolve(cit):
    """resolução por níveis: exacta/fragmentos → errata → canonização (6.26, item A)
    → confundíveis. Devolve (obra, nível) ou (None, None)."""
    alvo = N(cit)
    trocos = [N(x) for x in ELIPSE.split(cit)]
    trocos = [x for x in trocos if len(x) >= 18]
    can = canoniza(cit)
    ctro = [canoniza(x) for x in ELIPSE.split(cit)]
    ctro = [x for x in ctro if len(x) >= 18]
    for rot in CORPO:
        corpo = TODO[rot]
        if alvo in corpo:
            return rot, 'exacta'
        # citação com elipse verifica-se por fragmentos: cada troço longo tem de
        # bater, porque o elidido, por definição, não está no texto seguido.
        if len(trocos) > 1 and all(x in corpo for x in trocos):
            return rot, 'fragmentos'
        if aplica_errata(alvo, rot) in corpo or alvo in TODO_ERR[rot]:
            return rot, 'errata'
        # nível 3: canonização das decorações (6.26, item A)
        if len(can) >= 20 and (can in TODO_CAN[rot] or can in TODO_CAN_ERR[rot]):
            return rot, 'canonização'
        if len(ctro) > 1 and all(x in TODO_CAN[rot] or x in TODO_CAN_ERR[rot] for x in ctro):
            return rot, 'canonização'
        if confundiveis(alvo) in TODO_CONF[rot]:
            return rot, 'confundíveis'
    return None, None

def main():
    falhas = []
    informativos = []
    cits_total = cits_cobertas = 0
    niveis = Counter()
    _dump = {'cobertas': [], 'c1': []}

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
                resolveu, nivel = resolve(cit)
                if resolveu is None:
                    if not MARCADORES.search(fr):
                        falhas.append(('C1 citação sem cobertura nem marcador', rel,
                                       f'p.{pags[0]} «{cit[:88]}»'))
                        _dump['c1'].append([rel, pags[0], cit])
                    else:
                        cits_cobertas += 1
                        niveis['marcador'] += 1
                        _dump['cobertas'].append([rel, cit, 'marcador'])
                    continue
                cits_cobertas += 1
                niveis[nivel] += 1
                _dump['cobertas'].append([rel, cit, resolveu, nivel])
                # C2: onde resolve? (páginas da OBRA, já pelo mapeamento folha↔página)
                alvo = N(cit)
                alvo_conf = confundiveis(alvo)
                alvo_can = canoniza(cit)
                onde = [p for p, w in CORPO[resolveu].items() if alvo in w[0]]
                if not onde and len(alvo_can) >= 20:
                    onde = [p for p, w in CORPO[resolveu].items() if alvo_can in w[1]]
                if not onde:
                    onde = [p for p, w in CORPO_CONF[resolveu].items() if alvo_conf in w]
                if onde and pags and not any(abs(p - a) <= 1 for p in onde for a in pags):
                    # INFORMATIVO, não bloqueante (6.26, item B adiado): a âncora que
                    # governa a citação não é extraível com fiabilidade do formato actual
                    # das frases (várias âncoras por frase), pelo que um gate aqui
                    # dispararia em falso e ensinaria a ignorá-lo.
                    informativos.append(
                        ('C2 âncora fora de sítio', rel, resolveu,
                         f'declara p.{pags} · resolve em p.{sorted(onde)[:3]} · «{cit[:70]}»'))

    print(f'citações com âncora verificadas: {cits_total} · cobertas: {cits_cobertas}')
    print('  níveis: ' + ' · '.join(f'{k} {niveis[k]}' for k in
          ('exacta', 'fragmentos', 'errata', 'canonização', 'confundíveis', 'marcador')))
    if informativos:
        por_obra = Counter(rot for (_, _, rot, _) in informativos)
        por_fich = Counter(rel for (_, rel, _, _) in informativos)
        det_obra = ' · '.join(f'{r}: {n}' for r, n in sorted(por_obra.items()))
        det_fich = ' · '.join(f'{r.split("/")[-1]} ({n})' for r, n in por_fich.most_common(3))
        print(f'[informativo, não bloqueante] C2: {len(informativos)} âncoras fora de sítio '
              f'a ±1 ({det_obra}); ficheiros mais atingidos: {det_fich}. '
              f'O C2 fica informativo até decisão do item B do 6.26.')
    if '--dump' in sys.argv:
        destino = Path(sys.argv[sys.argv.index('--dump') + 1])
        _dump['informativos'] = [[rel, rot, det] for (_, rel, rot, det) in informativos]
        _dump['niveis'] = dict(niveis)
        destino.write_text(json.dumps(_dump, ensure_ascii=False), encoding='utf-8')
    if falhas:
        print(f'VERMELHO - {len(falhas)} falha(s) bloqueantes:')
        for tipo, ficheiro, det in falhas[:80]:
            print(f'  [{tipo}] {ficheiro}')
            print(f'      {det}')
        if len(falhas) > 80:
            print(f'  … e mais {len(falhas) - 80}')
        sys.exit(1)
    print('VERDE - crivo de citações sem falhas bloqueantes (C1 cobertura · C3 placeholder · C4 equilíbrio; C2 informativo, por calibrar)')

if __name__ == '__main__':
    main()

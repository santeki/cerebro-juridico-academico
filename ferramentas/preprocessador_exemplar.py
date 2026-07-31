#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preprocessador_exemplar.py — pré-passe mecânico de obra convertida (proposta 6.23)

Instrumentação, não leitura: converte descoberta em mapa ANTES das sessões.
Compara o MD de leitura (marcadores [p. N] = FOLHA) com a camada de texto do
PDF (pdftotext, separador \f = folha), e produz:

  1. mapa folha↔página impressa (número lido nos cabeçalhos/rodapés da camada
     de texto), com intervalos de desvio constante e folhas sem número legível;
  2. confronto mecânico MD↔PDF-texto folha a folha (SequenceMatcher,
     autojunk=False, de-hifenização restrita a quebra de linha);
  3. passe de vocabulário: formas ≥ 5 letras só no MD, folha a folha,
     subtraído o pool adjudicado (MANTIDOS); picos marcam reconstrução do
     conversor sobre ruído — candidatas a zona fraca;
  4. fronteiras estruturais pelos cabeçalhos impressos (TÍTULO/CAPÍTULO/PARTE
     na camada de texto), com folha e página mapeada;
  5. ranking de zonas fracas prováveis (ratio baixo + pico de vocabulário).

O pré-passe NÃO gera afirmação substantiva: é mapa de risco. Em zona fraca,
citação literal só com adjudicação por imagem (INGESTAO, disciplina da dupla
fonte). Saídas: JSON integral + relatório MD compacto.

Uso:
  python3 preprocessador_exemplar.py --md <obra.md> --pdftext <pdftotext.txt> \
      [--mantidos <MANTIDOS.txt>] [--out <dir>] [--rotulo <nome>]
"""
import argparse, json, os, re, statistics, sys, unicodedata
from difflib import SequenceMatcher

TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]{5,}")
MARKER_RE = re.compile(r"\[p\.\s*(\d+)\]")
NUM_LINE_RE = re.compile(r"^\s*(\d{1,3})\s*$")
HEADING_RE = re.compile(r"^\s*(PARTE|T[ÍI]TULO|CAP[ÍI]TULO|SEC[ÇC][ÃA]O)\b(.*)$")

def norm_text(s: str) -> str:
    s = re.sub(r"-\s*\n\s*", "", s)          # de-hifenização SÓ na quebra de linha
    s = re.sub(r"\s+", " ", s)               # colapso de espaços
    return s.strip()

def strip_page_furniture(lines):
    """Remove linhas que são só número de página (cabeçalho/rodapé)."""
    return [l for l in lines if not NUM_LINE_RE.match(l)]

def printed_page_candidates(lines):
    """Números isolados nas primeiras/últimas 4 linhas não vazias."""
    nz = [l for l in lines if l.strip()]
    zone = nz[:4] + nz[-4:]
    out = []
    for l in zone:
        m = NUM_LINE_RE.match(l)
        if m:
            n = int(m.group(1))
            if 1 <= n <= 998:
                out.append(n)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--pdftext", required=True)
    ap.add_argument("--mantidos", default=None)
    ap.add_argument("--errata", default=None,
                    help="ERRATA-MD da obra: anota erratas já conhecidas por folha")
    ap.add_argument("--out", default=".")
    ap.add_argument("--rotulo", default="exemplar")
    ap.add_argument("--vocab-normal", type=int, default=15,
                    help="tecto do normal no passe de vocabulário (defeito 15)")
    args = ap.parse_args()

    md_raw = open(args.md, encoding="utf-8").read()
    pdf_raw = open(args.pdftext, encoding="utf-8").read()
    mantidos = set()
    if args.mantidos and os.path.exists(args.mantidos):
        for l in open(args.mantidos, encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#"):
                mantidos.add(l.casefold())
    erratas_folha = {}
    if args.errata and os.path.exists(args.errata):
        for m in re.finditer(r"\(\[p\.\s*(\d+)\]\)", open(args.errata, encoding="utf-8").read()):
            f = int(m.group(1))
            erratas_folha[f] = erratas_folha.get(f, 0) + 1

    # --- PDF: folha -> texto -------------------------------------------------
    parts = pdf_raw.split("\f")
    if parts and not parts[-1].strip():
        parts = parts[:-1]
    n_folhas = len(parts)
    pdf_folha = {i + 1: parts[i] for i in range(n_folhas)}

    # --- MD: folha -> texto (marcador [p. N] = FOLHA; multi-marcador agrega) --
    md_folha = {}
    pieces = MARKER_RE.split(md_raw)
    # pieces = [antes, n1, txt1, n2, txt2, ...]
    for i in range(1, len(pieces) - 1, 2):
        n = int(pieces[i]); txt = pieces[i + 1]
        md_folha[n] = md_folha.get(n, "") + "\n" + txt
    md_marcadores = sorted(md_folha)

    # --- mapa folha -> página impressa ---------------------------------------
    raw_pages = {}
    for f, txt in pdf_folha.items():
        raw_pages[f] = printed_page_candidates(txt.splitlines())
    # primeiro passe: candidato único e plausível
    page_of = {}
    for f, cands in raw_pages.items():
        if len(set(cands)) == 1 and cands:
            page_of[f] = cands[0]
    # suavização por vizinhança: aceita candidato coerente com o desvio local
    for _ in range(3):
        for f, cands in raw_pages.items():
            if f in page_of or not cands:
                continue
            offs = [page_of[g] - g for g in (f-2, f-1, f+1, f+2) if g in page_of]
            if offs:
                alvo = statistics.mode(offs)
                for c in set(cands):
                    if c - f == alvo:
                        page_of[f] = c
                        break
    # rejeita mapeamentos incoerentes com ambos os vizinhos
    for f in sorted(page_of):
        offs = [page_of[g] - g for g in (f-1, f+1) if g in page_of]
        if len(offs) == 2 and all(page_of[f] - f != o for o in offs) and offs[0] == offs[1]:
            del page_of[f]

    # intervalos de desvio constante
    intervalos = []
    for f in range(1, n_folhas + 1):
        if f not in page_of:
            continue
        off = page_of[f] - f
        if intervalos and intervalos[-1]["desvio"] == off and intervalos[-1]["folha_fim"] == f - 1:
            intervalos[-1]["folha_fim"] = f
        elif intervalos and intervalos[-1]["desvio"] == off and all(
                g not in page_of for g in range(intervalos[-1]["folha_fim"] + 1, f)):
            intervalos[-1]["folha_fim"] = f   # ponte sobre folhas sem número
        else:
            intervalos.append({"folha_ini": f, "folha_fim": f, "desvio": off})
    sem_numero = [f for f in range(1, n_folhas + 1) if f not in page_of]

    # separa intervalos canónicos de suspeitos (curtos e incoerentes com os vizinhos)
    canonicos, suspeitos = [], []
    for i, iv in enumerate(intervalos):
        curto = (iv["folha_fim"] - iv["folha_ini"]) < 2
        vizinhos = [intervalos[j]["desvio"] for j in (i - 1, i + 1) if 0 <= j < len(intervalos)]
        if curto and vizinhos and all(abs(iv["desvio"] - v) > 0 for v in vizinhos):
            suspeitos.append(iv)
            for f in range(iv["folha_ini"], iv["folha_fim"] + 1):
                page_of.pop(f, None)
        else:
            canonicos.append(iv)
    # possíveis páginas omissas: salto de página maior do que o salto de folha
    omissas = []
    for a, b in zip(canonicos, canonicos[1:]):
        pa = a["folha_fim"] + a["desvio"]
        pb = b["folha_ini"] + b["desvio"]
        gap_pag = pb - pa - 1
        gap_folha = b["folha_ini"] - a["folha_fim"] - 1
        if gap_pag > gap_folha + 2:
            omissas.append({"entre_folhas": [a["folha_fim"], b["folha_ini"]],
                            "paginas_impressas": [pa + 1, pb - 1],
                            "folhas_disponiveis": gap_folha,
                            "nota": "salto de paginação — adjudicar por imagem/cópia física"})

    # --- confronto e vocabulário, folha a folha ------------------------------
    tabela = []
    ratios = []
    for f in range(1, n_folhas + 1):
        p_txt_lines = strip_page_furniture(pdf_folha.get(f, "").splitlines())
        p_txt = norm_text("\n".join(p_txt_lines))
        m_txt = norm_text(md_folha.get(f, ""))
        linha = {"folha": f, "pagina": page_of.get(f)}
        if not m_txt and not p_txt:
            linha.update(ratio=None, so_md=None, nota="vazia nos dois lados")
        elif not m_txt:
            linha.update(ratio=None, so_md=None, nota="sem marcador no MD")
        else:
            sm = SequenceMatcher(None, p_txt.casefold(), m_txt.casefold(), autojunk=False)
            r = round(sm.ratio(), 4)
            pdf_tokens = {t.casefold() for t in TOKEN_RE.findall(p_txt)}
            so_md = sorted({t for t in TOKEN_RE.findall(m_txt)
                            if t.casefold() not in pdf_tokens
                            and t.casefold() not in mantidos})
            linha.update(ratio=r, so_md=len(so_md), formas_so_md=so_md[:40])
            ratios.append(r)
        if f in erratas_folha:
            linha["erratas_conhecidas"] = erratas_folha[f]
        tabela.append(linha)

    med = statistics.median(ratios) if ratios else 0
    mad = statistics.median([abs(r - med) for r in ratios]) if ratios else 0
    limiar_ratio = med - 4 * mad

    # --- zonas fracas prováveis ----------------------------------------------
    fracas = []
    for l in tabela:
        if l.get("ratio") is None:
            continue
        motivo = []
        if l["ratio"] < limiar_ratio:
            motivo.append(f"ratio {l['ratio']:.3f} < limiar {limiar_ratio:.3f}")
        if l["so_md"] is not None and l["so_md"] > args.vocab_normal:
            motivo.append(f"vocabulário só-MD {l['so_md']} > {args.vocab_normal}")
        if motivo:
            fracas.append({"folha": l["folha"], "pagina": l["pagina"],
                           "ratio": l["ratio"], "so_md": l["so_md"],
                           "motivos": motivo})
    fracas.sort(key=lambda x: (x["ratio"] if x["ratio"] is not None else 1))

    # --- fronteiras estruturais pelos cabeçalhos da camada de texto ----------
    fronteiras = []
    for f in range(1, n_folhas + 1):
        for l in pdf_folha.get(f, "").splitlines()[:14]:
            m = HEADING_RE.match(l.strip())
            if m:
                fronteiras.append({"folha": f, "pagina": page_of.get(f),
                                   "linha": l.strip()[:90]})
                break

    # --- saídas ---------------------------------------------------------------
    os.makedirs(args.out, exist_ok=True)
    base = os.path.join(args.out, f"mapa-risco-{args.rotulo}")
    spikes = [l for l in tabela if l.get("so_md") is not None
              and l["so_md"] > args.vocab_normal]
    resumo = {
        "exemplar": args.rotulo,
        "folhas_pdf": n_folhas,
        "folhas_com_marcador_md": len(md_marcadores),
        "folhas_sem_numero_impresso_legivel": sem_numero,
        "intervalos_desvio": canonicos,
        "intervalos_suspeitos": suspeitos,
        "possiveis_paginas_omissas": omissas,
        "ratio_mediana": round(med, 4),
        "ratio_limiar_fraco": round(limiar_ratio, 4),
        "zonas_fracas_provaveis": fracas,
        "picos_vocabulario": [{"folha": l["folha"], "pagina": l.get("pagina"),
                               "so_md": l["so_md"], "ratio": l.get("ratio"),
                               "erratas_conhecidas": l.get("erratas_conhecidas", 0)}
                              for l in spikes],
        "fronteiras_estruturais": fronteiras,
    }
    with open(base + ".json", "w", encoding="utf-8") as fh:
        json.dump({"resumo": resumo, "tabela": tabela}, fh, ensure_ascii=False, indent=1)

    with open(base + ".md", "w", encoding="utf-8") as fh:
        w = fh.write
        w(f"# Mapa de risco do exemplar — {args.rotulo} (pré-passe mecânico)\n\n")
        w("Instrumentação por código sobre MD de leitura vs camada de texto do PDF; ")
        w("não substitui leitura nem adjudicação por imagem. Números lidos, nunca inferidos.\n\n")
        w(f"- Folhas no PDF: **{n_folhas}** · folhas com marcador no MD: **{len(md_marcadores)}**\n")
        w(f"- Ratio mediano MD↔PDF-texto: **{med:.3f}** · limiar de fraqueza (med − 4·MAD): {limiar_ratio:.3f}\n")
        w(f"- Folhas sem número impresso legível na camada de texto: {len(sem_numero)}"
          f" ({', '.join(map(str, sem_numero[:30]))}{'…' if len(sem_numero) > 30 else ''})\n\n")
        w("## Desvio folha↔página (intervalos constantes)\n\n")
        for iv in canonicos:
            w(f"- folhas {iv['folha_ini']}-{iv['folha_fim']}: página = folha + {iv['desvio']}\n")
        if suspeitos:
            w("\nIntervalos suspeitos (número lido incoerente com a vizinhança — "
              "excluídos do mapa; adjudicar por imagem se a folha for citada):\n\n")
            for iv in suspeitos:
                w(f"- folhas {iv['folha_ini']}-{iv['folha_fim']}: leitura «página = folha + {iv['desvio']}» rejeitada\n")
        if omissas:
            w("\nPossíveis páginas omissas no exemplar (salto de paginação impressa "
              "maior do que o salto de folhas — adjudicar por imagem/cópia física):\n\n")
            for o in omissas:
                w(f"- entre as folhas {o['entre_folhas'][0]} e {o['entre_folhas'][1]}: "
                  f"pp. impressas {o['paginas_impressas'][0]}-{o['paginas_impressas'][1]} "
                  f"com {o['folhas_disponiveis']} folha(s) no exemplar\n")
        w("\n## Zonas fracas prováveis (candidatas a «citação só com imagem»)\n\n")
        if not fracas:
            w("(nenhuma acima dos limiares)\n")
        for z in fracas:
            w(f"- folha {z['folha']} (p. {z['pagina']}): ratio {z['ratio']:.3f}, "
              f"só-MD {z['so_md']} — {'; '.join(z['motivos'])}\n")
        w("\n## Picos de vocabulário só-MD (reconstrução provável do conversor)\n\n")
        for l in spikes:
            err = f" · erratas já registadas nesta folha: {l['erratas_conhecidas']}" if l.get("erratas_conhecidas") else ""
            w(f"- folha {l['folha']} (p. {l.get('pagina')}): só-MD {l['so_md']}, "
              f"ratio {l.get('ratio')}{err}\n")
        w("\n## Fronteiras estruturais pelos cabeçalhos da camada de texto\n\n")
        for fr in fronteiras:
            w(f"- folha {fr['folha']} (p. {fr['pagina']}): {fr['linha']}\n")
        w("\n## Limites do pré-passe (leitura obrigatória)\n\n")
        w("O confronto MD↔PDF-texto detecta DIVERGÊNCIA entre os dois derivados. "
          "Não detecta corrupção de causa comum: onde a camada OCR normalizou em "
          "silêncio (sublinhados densos, degradação física), MD e PDF-texto podem "
          "convergir ambos errados — e essa convergência não é convergência "
          "(INGESTAO, disciplina da dupla fonte). Zona fraca declarada por "
          "assinatura visual mantém-se declarada ainda que este passe não a "
          "acuse; o pré-passe ACRESCENTA candidatas, nunca limpa declaradas. "
          "Números de página lidos da camada de texto; onde marcados suspeitos, "
          "a adjudicação é por imagem. Este mapa é instrumentação: não sustenta "
          "citação nem afirmação substantiva.\n")
        w("\n*(tabela integral folha a folha no JSON homónimo)*\n")

    print(f"OK — {base}.md e .json")
    print(f"folhas={n_folhas} md_marcadores={len(md_marcadores)} "
          f"mediana={med:.3f} fracas={len(fracas)} fronteiras={len(fronteiras)} "
          f"sem_numero={len(sem_numero)}")

if __name__ == "__main__":
    sys.exit(main())

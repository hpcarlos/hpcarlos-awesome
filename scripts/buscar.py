#!/usr/bin/env python3
"""Busca nos achados por texto, tag, categoria, tipo ou status.

Exemplos:
    python3 scripts/buscar.py llm
    python3 scripts/buscar.py --tag python --tipo projeto
    python3 scripts/buscar.py rag --nota-min 4 --detalhe
    python3 scripts/buscar.py --tags        # lista todas as tags
    python3 scripts/buscar.py --categorias  # lista todas as categorias
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_achados import carregar_achados  # noqa: E402

VERDE, AMARELO, CINZA, NEGRITO, ZERA = "\033[32m", "\033[33m", "\033[90m", "\033[1m", "\033[0m"


def cor(txt: str, c: str) -> str:
    return txt if not sys.stdout.isatty() else f"{c}{txt}{ZERA}"


def normalizar(t: str) -> str:
    import unicodedata
    return "".join(
        ch for ch in unicodedata.normalize("NFKD", t.lower())
        if not unicodedata.combining(ch)
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Busca nos achados.")
    ap.add_argument("termos", nargs="*", help="palavras a procurar (título, resumo, corpo, url, tags)")
    ap.add_argument("--tag", action="append", default=[])
    ap.add_argument("--categoria", "-c", action="append", default=[])
    ap.add_argument("--tipo", action="append", default=[])
    ap.add_argument("--status", action="append", default=[])
    ap.add_argument("--nota-min", type=int, default=0)
    ap.add_argument("--desde", default="", help="somente achados adicionados a partir de AAAA-MM-DD")
    ap.add_argument("--detalhe", "-d", action="store_true", help="mostra resumo e trecho que casou")
    ap.add_argument("--tags", action="store_true", help="lista todas as tags e sai")
    ap.add_argument("--categorias", action="store_true", help="lista todas as categorias e sai")
    args = ap.parse_args()

    achados = carregar_achados()

    if args.tags or args.categorias:
        campo = "tags" if args.tags else "categorias"
        cont = collections.Counter(x for a in achados for x in getattr(a, campo))
        for nome, n in sorted(cont.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"{n:4}  {nome}")
        if not cont:
            print(f"(nenhuma {campo[:-1]} ainda)")
        return

    termos = [normalizar(t) for t in args.termos]
    baixo = lambda xs: {x.lower() for x in xs}  # noqa: E731

    resultados = []
    for a in achados:
        if args.tag and not baixo(args.tag) & baixo(a.tags):
            continue
        if args.categoria and not baixo(args.categoria) & baixo(a.categorias):
            continue
        if args.tipo and a.tipo.lower() not in baixo(args.tipo):
            continue
        if args.status and a.status.lower() not in baixo(args.status):
            continue
        if a.nota < args.nota_min:
            continue
        if args.desde and a.adicionado < args.desde:
            continue
        alvo = normalizar(" ".join([a.titulo, a.url, a.corpo, " ".join(a.tags), " ".join(a.categorias)]))
        if termos and not all(t in alvo for t in termos):
            continue
        resultados.append(a)

    resultados.sort(key=lambda a: (-a.nota, a.adicionado), reverse=False)

    if not resultados:
        print("Nenhum achado corresponde aos filtros.")
        sys.exit(1)

    for a in resultados:
        nota = ("★" * a.nota) if a.nota else "-"
        print(f"{cor(a.titulo, NEGRITO)}  {cor(nota, AMARELO)}")
        print(f"  {cor(a.rel, VERDE)}  ·  {a.tipo} · {a.status}"
              + (f" · {' '.join('#' + t for t in a.tags)}" if a.tags else ""))
        print(f"  {cor(a.url, CINZA)}")
        if args.detalhe:
            if a.resumo:
                print(f"  {a.resumo[:300]}")
            for termo, bruto in zip(termos, args.termos):
                for ln in a.corpo.split("\n"):
                    if termo in normalizar(ln) and normalizar(a.titulo).find(termo) == -1:
                        print(f"  {cor('…' + ln.strip()[:160], CINZA)}")
                        break
        print()

    print(f"{len(resultados)} de {len(achados)} achado(s).")


if __name__ == "__main__":
    main()

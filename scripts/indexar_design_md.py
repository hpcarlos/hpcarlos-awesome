#!/usr/bin/env python3
"""Gera DESIGN-MD.md a partir de dados/design-md.tsv.

Uso: python3 scripts/indexar_design_md.py [--conferir]
Para atualizar a fonte, veja scripts/importar_design_md.py.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_achados import RAIZ, ancora  # noqa: E402
from indexar import escrever, substituir_bloco  # noqa: E402

FONTE = os.path.join(RAIZ, "dados", "design-md.tsv")
DESTINO = os.path.join(RAIZ, "DESIGN-MD.md")

# A ordem segue a da fonte, não a contagem.
ORDEM = [
    "Plataformas de IA e LLM", "Ferramentas de desenvolvimento e IDEs",
    "Backend, banco de dados e DevOps", "Produtividade e SaaS",
    "Design e ferramentas criativas", "Fintech e cripto",
    "Comércio eletrônico e varejo", "Mídia e tecnologia de consumo",
    "Automotivo", "Web retrô · nostalgia",
]


def carregar():
    itens = collections.defaultdict(list)
    with open(FONTE, encoding="utf-8") as fh:
        for linha in fh:
            if linha.startswith("#") or not linha.strip():
                continue
            cat, nome, url, desc = linha.rstrip("\n").split("\t")
            itens[cat].append((nome, url, desc))
    return itens


def ordem_cats(itens):
    vistas = [c for c in ORDEM if c in itens]
    extras = sorted(c for c in itens if c not in ORDEM)
    return vistas + extras


def item(nome, url, desc) -> str:
    texto = desc.rstrip()
    if texto and texto[-1] not in ".!?":
        texto += "."
    return f"* [{nome}]({url}) - {texto}"


def sumario(itens) -> str:
    return "\n".join(
        f"- [{c}](#{ancora(c)}) <sub>{len(itens[c])}</sub>" for c in ordem_cats(itens)
    )


def secoes(itens) -> str:
    out = []
    for c in ordem_cats(itens):
        out += [f"## {c}", ""]
        out += [item(*x) for x in sorted(itens[c], key=lambda x: x[0].lower())]
        out.append("")
    return "\n".join(out).rstrip()


def estatisticas(itens) -> str:
    total = sum(len(v) for v in itens.values())
    return (f"**{total}** arquivos DESIGN.md em **{len(itens)}** categorias · "
            f"atualizado em {dt.date.today().isoformat()}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conferir", action="store_true")
    args = ap.parse_args()

    itens = carregar()
    if not os.path.exists(DESTINO):
        print(f"erro: {DESTINO} não existe (o cabeçalho fixo é escrito à mão)", file=sys.stderr)
        sys.exit(1)

    with open(DESTINO, encoding="utf-8") as fh:
        texto = fh.read()
    novo = substituir_bloco(texto, "ESTATISTICAS", estatisticas(itens))
    novo = substituir_bloco(novo, "SUMARIO", sumario(itens))
    novo = substituir_bloco(novo, "LISTA", secoes(itens))

    mudou: list = []
    escrever(DESTINO, novo, args.conferir, mudou)
    total = sum(len(v) for v in itens.values())
    if args.conferir:
        if mudou:
            print("DESIGN-MD.md desatualizado. Rode: python3 scripts/indexar_design_md.py",
                  file=sys.stderr)
            sys.exit(1)
        print("DESIGN-MD.md em dia.")
    else:
        print(f"{total} arquivos indexados." + (" Atualizado." if mudou else " Nada mudou."))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gera SELFHOSTED.md a partir de dados/selfhosted.tsv.

Uso: python3 scripts/indexar_selfhosted.py [--conferir]
Para atualizar a fonte, veja scripts/importar_selfhosted.py.
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

FONTE = os.path.join(RAIZ, "dados", "selfhosted.tsv")
DESTINO = os.path.join(RAIZ, "SELFHOSTED.md")

# Licenças copyleft fortes ganham destaque: mudam a decisão de usar o software
# como base de um produto fechado.
COPYLEFT_FORTE = {"AGPL-3.0", "AGPL-3.0-only", "AGPL-3.0-or-later", "SSPL-1.0", "EUPL-1.2"}


def carregar():
    itens = collections.defaultdict(list)
    with open(FONTE, encoding="utf-8") as fh:
        for linha in fh:
            if linha.startswith("#") or not linha.strip():
                continue
            cat, nome, url, lic, stack, naomantido, desc = linha.rstrip("\n").split("\t")
            itens[cat].append((nome, url, lic, stack, naomantido, desc))
    return itens


def item(nome, url, lic, stack, naomantido, desc) -> str:
    texto = desc.rstrip()
    if texto and texto[-1] not in ".!?":
        texto += "."
    partes = [f"* [{nome}]({url}) - {texto}"]
    if lic:
        partes.append(f"`{lic}`")
    if stack:
        partes.append(f"<sub>{stack}</sub>")
    linha = " ".join(partes)
    avisos = []
    if naomantido:
        avisos.append("não mantido pelos autores")
    if lic in COPYLEFT_FORTE:
        avisos.append(f"copyleft forte (`{lic}`): serviço em rede exige abrir o código")
    if avisos:
        linha += f"<br><sub>⚠️ {' · '.join(avisos)}</sub>"
    return linha


def sumario(itens) -> str:
    return "\n".join(
        f"- [{cat}](#{ancora(cat)}) <sub>{len(itens[cat])}</sub>" for cat in sorted(itens)
    )


def secoes(itens) -> str:
    out = []
    for cat in sorted(itens):
        out += [f"## {cat}", ""]
        out += [item(*x) for x in sorted(itens[cat], key=lambda x: x[0].lower())]
        out.append("")
    return "\n".join(out).rstrip()


def estatisticas(itens) -> str:
    todos = [x for v in itens.values() for x in v]
    lic = collections.Counter(x[2] for x in todos if x[2])
    naomantidos = sum(1 for x in todos if x[4])
    copyleft = sum(1 for x in todos if x[2] in COPYLEFT_FORTE)
    top = " · ".join(f"`{k}` {v}" for k, v in lic.most_common(6))
    return (
        f"**{len(todos)}** projetos em **{len(itens)}** categorias · "
        f"atualizado em {dt.date.today().isoformat()}\n\n"
        f"Licenças mais comuns: {top}\n\n"
        f"⚠️ **{naomantidos}** marcados pela fonte como não mantidos · "
        f"**{copyleft}** sob copyleft forte (AGPL e afins)"
    )


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
            print("SELFHOSTED.md desatualizado. Rode: python3 scripts/indexar_selfhosted.py",
                  file=sys.stderr)
            sys.exit(1)
        print("SELFHOSTED.md em dia.")
    else:
        print(f"{total} projetos indexados." + (" Atualizado." if mudou else " Nada mudou."))


if __name__ == "__main__":
    main()

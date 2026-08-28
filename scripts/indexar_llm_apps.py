#!/usr/bin/env python3
"""Gera LLM-APPS.md a partir de dados/llm-apps.tsv.

A lista principal (README.md) vem de achados/, um arquivo por link analisado.
Esta é uma coleção derivada: os 115 aplicativos que vivem dentro de um único
repositório (awesome-llm-apps), catalogados em bloco. Por isso a fonte aqui é
uma tabela, e nao um achado por item.

Uso: python3 scripts/indexar_llm_apps.py [--conferir]
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

FONTE = os.path.join(RAIZ, "dados", "llm-apps.tsv")
DESTINO = os.path.join(RAIZ, "LLM-APPS.md")
BASE_URL = "https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/"

ROTULOS = {
    "skills": ("🧩", "Skills de agente"),
    "starter": ("🌱", "Agentes para começar"),
    "avancados": ("🚀", "Agentes avançados"),
    "sempre-ativos": ("🛰️", "Agentes sempre ativos"),
    "times": ("🤝", "Times de agentes"),
    "voz": ("🗣️", "Agentes de voz"),
    "interfaces": ("🖼️", "Interfaces geradas por agente"),
    "jogos": ("🎮", "Agentes que jogam"),
    "mcp": ("♾️", "Agentes com MCP"),
    "rag": ("📀", "RAG"),
    "memoria": ("💾", "Aplicações com memória"),
    "conversar": ("💬", "Conversar com…"),
    "otimizacao": ("🎯", "Otimização de contexto e token"),
    "fine-tuning": ("🔧", "Ajuste fino de modelo"),
    "cursos": ("🧑‍🏫", "Cursos rápidos de framework"),
}

# A ordem das seções segue a do repositório de origem, não a contagem.
ORDEM = list(ROTULOS)


def carregar():
    itens = collections.defaultdict(list)
    with open(FONTE, encoding="utf-8") as fh:
        for linha in fh:
            if linha.startswith("#") or not linha.strip():
                continue
            cat, nome, href, tldr = linha.rstrip("\n").split("\t")
            itens[cat].append((nome, href, tldr))
    return itens


def url_de(href: str) -> str:
    return href if href.startswith("http") else BASE_URL + href.rstrip("/")


def item(nome: str, href: str, tldr: str) -> str:
    texto = tldr.rstrip()
    if texto and texto[-1] not in ".!?":
        texto += "."
    externo = " <sub>projeto externo</sub>" if href.startswith("http") else ""
    return f"* [{nome}]({url_de(href)}) - {texto}{externo}"


def sumario(itens) -> str:
    linhas = []
    for cat in ORDEM:
        if cat not in itens:
            continue
        emoji, rot = ROTULOS[cat]
        titulo = f"{emoji} {rot}"
        linhas.append(f"- [{rot}](#{ancora(titulo)}) <sub>{len(itens[cat])}</sub>")
    return "\n".join(linhas)


def secoes(itens) -> str:
    out = []
    for cat in ORDEM:
        if cat not in itens:
            continue
        emoji, rot = ROTULOS[cat]
        out += [f"## {emoji} {rot}", ""]
        out += [item(*x) for x in itens[cat]]
        out.append("")
    return "\n".join(out).rstrip()


def estatisticas(itens) -> str:
    total = sum(len(v) for v in itens.values())
    return (f"**{total}** aplicações em **{len(itens)}** categorias · "
            f"todas sob Apache-2.0, no mesmo repositório · "
            f"atualizado em {dt.date.today().isoformat()}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conferir", action="store_true")
    args = ap.parse_args()

    itens = carregar()
    if not os.path.exists(DESTINO):
        print(f"erro: {DESTINO} não existe (o cabeçalho fixo precisa ser criado à mão)",
              file=sys.stderr)
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
            print("LLM-APPS.md desatualizado. Rode: python3 scripts/indexar_llm_apps.py",
                  file=sys.stderr)
            sys.exit(1)
        print("LLM-APPS.md em dia.")
    else:
        print(f"{total} aplicações indexadas." + (" Atualizado." if mudou else " Nada mudou."))


if __name__ == "__main__":
    main()

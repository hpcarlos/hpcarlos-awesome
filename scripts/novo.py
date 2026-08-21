#!/usr/bin/env python3
"""Cria um novo achado em achados/ a partir de uma URL.

Uso:
    python3 scripts/novo.py https://exemplo.com/artigo
    python3 scripts/novo.py URL --titulo "Nome" --tipo artigo \
        --categorias ia,ferramentas --tags python,llm --nota 4

Se a rede estiver disponivel, tenta descobrir o titulo da pagina.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import sys
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_achados import (  # noqa: E402
    DIR_ACHADOS, RAIZ, STATUS, TIPOS, carregar_achados, erro, slugify,
)

MODELO = os.path.join(RAIZ, "modelos", "achado.md")


def titulo_da_pagina(url: str, timeout: float = 8.0) -> str:
    """Melhor esforco: le o <title> da pagina. Silencioso em caso de falha."""
    try:
        from urllib.request import Request, urlopen
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 (awesome-links)"})
        with urlopen(req, timeout=timeout) as resp:
            bruto = resp.read(200_000).decode(resp.headers.get_content_charset() or "utf-8", "replace")
        m = re.search(r"<title[^>]*>(.*?)</title>", bruto, re.S | re.I)
        if m:
            return " ".join(html.unescape(m.group(1)).split())
    except Exception:
        pass
    return ""


def titulo_do_url(url: str) -> str:
    p = urlparse(url)
    partes = [x for x in p.path.split("/") if x]
    base = partes[-1] if partes else p.netloc
    base = re.sub(r"\.(html?|php|aspx?|md)$", "", base)
    base = re.sub(r"[-_]+", " ", base).strip()
    if p.netloc.endswith("github.com") and len(partes) >= 2:
        return f"{partes[0]}/{partes[1]}"
    return base.title() or p.netloc


def tipo_sugerido(url: str) -> str:
    d = urlparse(url).netloc.lower()
    if "github.com" in d or "gitlab.com" in d:
        return "projeto"
    if "youtube.com" in d or "youtu.be" in d or "vimeo.com" in d:
        return "video"
    if "arxiv.org" in d or "acm.org" in d or "ieee.org" in d:
        return "paper"
    if "x.com" in d or "twitter.com" in d or "reddit.com" in d:
        return "thread"
    return "artigo"


def lista(valor: str):
    return [x.strip().lower() for x in (valor or "").split(",") if x.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description="Registra um novo achado.")
    ap.add_argument("url")
    ap.add_argument("--titulo", default="")
    ap.add_argument("--tipo", default="", choices=[""] + TIPOS)
    ap.add_argument("--categorias", default="")
    ap.add_argument("--tags", default="")
    ap.add_argument("--status", default="novo", choices=STATUS)
    ap.add_argument("--nota", type=int, default=0, help="relevancia de 1 a 5 (0 = sem nota)")
    ap.add_argument("--fonte", default="", help="onde voce encontrou (newsletter, amigo, HN...)")
    ap.add_argument("--resumo", default="", help="uma linha descrevendo o achado")
    ap.add_argument("--sem-rede", action="store_true", help="nao tenta buscar o titulo online")
    args = ap.parse_args()

    url = args.url.strip()
    if not url.startswith(("http://", "https://")):
        erro("a URL precisa comecar com http:// ou https://")

    for a in carregar_achados():
        if a.url.rstrip("/") == url.rstrip("/"):
            print(f"ja existe: {a.rel}  ({a.titulo})")
            sys.exit(2)

    titulo = args.titulo or ("" if args.sem_rede else titulo_da_pagina(url)) or titulo_do_url(url)
    tipo = args.tipo or tipo_sugerido(url)
    hoje = dt.date.today().isoformat()

    os.makedirs(DIR_ACHADOS, exist_ok=True)
    slug = slugify(titulo)
    destino = os.path.join(DIR_ACHADOS, f"{hoje}-{slug}.md")
    n = 2
    while os.path.exists(destino):
        destino = os.path.join(DIR_ACHADOS, f"{hoje}-{slug}-{n}.md")
        n += 1

    with open(MODELO, encoding="utf-8") as fh:
        modelo = fh.read()

    def fmt_lista(itens):
        return "[" + ", ".join(itens) + "]" if itens else "[]"

    texto = (
        modelo
        .replace("{{TITULO}}", titulo.replace('"', "'"))
        .replace("{{URL}}", url)
        .replace("{{TIPO}}", tipo)
        .replace("{{CATEGORIAS}}", fmt_lista(lista(args.categorias)))
        .replace("{{TAGS}}", fmt_lista(lista(args.tags)))
        .replace("{{STATUS}}", args.status)
        .replace("{{NOTA}}", str(args.nota))
        .replace("{{DATA}}", hoje)
        .replace("{{FONTE}}", args.fonte)
        .replace("{{RESUMO}}", args.resumo or "_(a preencher)_")
    )
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(texto)

    print(os.path.relpath(destino, RAIZ))


if __name__ == "__main__":
    main()

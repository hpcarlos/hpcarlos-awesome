#!/usr/bin/env python3
"""Regenera os indices a partir dos arquivos em achados/.

Gera:
  INDICE.md  - todos os achados por categoria e por data
  TAGS.md    - mapa de tags -> achados
  README.md  - atualiza o bloco de estatisticas e os ultimos achados

Uso: python3 scripts/indexar.py [--conferir]
     --conferir  nao escreve nada; sai com codigo 1 se algo estiver desatualizado
                 ou se algum achado tiver front-matter invalido.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_achados import RAIZ, STATUS, TIPOS, Achado, carregar_achados  # noqa: E402

INDICE = os.path.join(RAIZ, "INDICE.md")
TAGS = os.path.join(RAIZ, "TAGS.md")
README = os.path.join(RAIZ, "README.md")

INI = "<!-- INICIO:{} -->"
FIM = "<!-- FIM:{} -->"

EMOJI_TIPO = {
    "projeto": "🛠", "artigo": "📄", "video": "🎥", "ferramenta": "⚙️",
    "biblioteca": "📦", "curso": "🎓", "paper": "📚", "thread": "💬",
    "newsletter": "📰", "podcast": "🎧", "outro": "🔗",
}


def estrelas(nota: int) -> str:
    return "★" * nota + "☆" * (5 - nota) if nota else "—"


def linha(a: Achado) -> str:
    marca = EMOJI_TIPO.get(a.tipo, "🔗")
    partes = [f"- {marca} **[{a.titulo}]({a.rel})**"]
    if a.url:
        partes.append(f"([link original]({a.url}))")
    meta = [a.tipo]
    if a.nota:
        meta.append(estrelas(a.nota))
    if a.status and a.status != "novo":
        meta.append(a.status)
    if a.tags:
        meta.append(" ".join(f"`{t}`" for t in a.tags))
    partes.append(f"— <sub>{' · '.join(meta)}</sub>")
    return " ".join(partes)


def validar(achados):
    problemas = []
    for a in achados:
        if not a.meta:
            problemas.append(f"{a.rel}: sem front-matter")
            continue
        if not a.url:
            problemas.append(f"{a.rel}: campo 'url' vazio")
        if a.tipo not in TIPOS:
            problemas.append(f"{a.rel}: tipo '{a.tipo}' desconhecido (use um de: {', '.join(TIPOS)})")
        if a.status not in STATUS:
            problemas.append(f"{a.rel}: status '{a.status}' desconhecido (use um de: {', '.join(STATUS)})")
        if a.nota and not 1 <= a.nota <= 5:
            problemas.append(f"{a.rel}: nota fora de 1..5")
        if not a.categorias:
            problemas.append(f"{a.rel}: sem categorias")
    return problemas


def gerar_indice(achados) -> str:
    por_cat = collections.defaultdict(list)
    for a in achados:
        for c in (a.categorias or ["sem-categoria"]):
            por_cat[c].append(a)

    out = ["# Índice de achados", "",
           f"{len(achados)} achado(s) · atualizado automaticamente por `scripts/indexar.py` — não edite à mão.",
           ""]

    out += ["## Por categoria", ""]
    for cat in sorted(por_cat):
        itens = sorted(por_cat[cat], key=lambda a: (-a.nota, a.titulo.lower()))
        out.append(f"### {cat} ({len(itens)})")
        out.append("")
        out += [linha(a) for a in itens]
        out.append("")

    out += ["## Por data de entrada", ""]
    por_mes = collections.defaultdict(list)
    for a in achados:
        por_mes[(a.adicionado or "0000-00")[:7]].append(a)
    for mes in sorted(por_mes, reverse=True):
        out.append(f"### {mes}")
        out.append("")
        out += [linha(a) for a in sorted(por_mes[mes], key=lambda a: a.adicionado, reverse=True)]
        out.append("")

    out += ["## Por status", ""]
    por_status = collections.defaultdict(list)
    for a in achados:
        por_status[a.status].append(a)
    for st in STATUS:
        if st in por_status:
            nomes = ", ".join(f"[{a.titulo}]({a.rel})" for a in sorted(por_status[st], key=lambda x: x.titulo.lower()))
            out.append(f"- **{st}** ({len(por_status[st])}): {nomes}")
    out.append("")
    return "\n".join(out).rstrip() + "\n"


def gerar_tags(achados) -> str:
    por_tag = collections.defaultdict(list)
    for a in achados:
        for t in a.tags:
            por_tag[t].append(a)

    out = ["# Tags", "",
           f"{len(por_tag)} tag(s) em {len(achados)} achado(s) · gerado por `scripts/indexar.py` — não edite à mão.",
           ""]
    if por_tag:
        nuvem = sorted(por_tag.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        out += ["## Mais usadas", "",
                " · ".join(f"`{t}` ({len(v)})" for t, v in nuvem[:30]), ""]
    for tag in sorted(por_tag):
        out.append(f"## `{tag}`")
        out.append("")
        out += [linha(a) for a in sorted(por_tag[tag], key=lambda a: (-a.nota, a.titulo.lower()))]
        out.append("")
    if not por_tag:
        out += ["_Nenhuma tag ainda._", ""]
    return "\n".join(out).rstrip() + "\n"


def bloco_estatisticas(achados) -> str:
    por_tipo = collections.Counter(a.tipo for a in achados)
    por_status = collections.Counter(a.status for a in achados)
    cats = sorted({c for a in achados for c in a.categorias})
    tags = {t for a in achados for t in a.tags}
    hoje = dt.date.today().isoformat()

    linhas = [
        f"**{len(achados)}** achados · **{len(cats)}** categorias · **{len(tags)}** tags · atualizado em {hoje}",
        "",
        "| tipo | qtd. |  | status | qtd. |",
        "| --- | ---: | --- | --- | ---: |",
    ]
    tipos = [(t, n) for t, n in sorted(por_tipo.items(), key=lambda kv: -kv[1])]
    stats = [(s, por_status[s]) for s in STATUS if por_status.get(s)]
    for i in range(max(len(tipos), len(stats), 1)):
        et, en = tipos[i] if i < len(tipos) else ("", "")
        es, esn = stats[i] if i < len(stats) else ("", "")
        linhas.append(f"| {et} | {en} |  | {es} | {esn} |")
    if cats:
        linhas += ["", "Categorias: " + " · ".join(f"`{c}`" for c in cats)]
    return "\n".join(linhas)


def bloco_recentes(achados, n: int = 10) -> str:
    recentes = sorted(achados, key=lambda a: (a.adicionado, a.arquivo), reverse=True)[:n]
    if not recentes:
        return "_Nenhum achado ainda. Cole um link em [`INBOX.md`](INBOX.md) para começar._"
    return "\n".join(f"- `{a.adicionado}` " + linha(a)[2:] for a in recentes)


def substituir_bloco(texto: str, marca: str, conteudo: str) -> str:
    ini, fim = INI.format(marca), FIM.format(marca)
    i, f = texto.find(ini), texto.find(fim)
    if i == -1 or f == -1:
        return texto
    return texto[:i + len(ini)] + "\n" + conteudo + "\n" + texto[f:]


def escrever(caminho: str, conteudo: str, conferir: bool, mudou: list) -> None:
    atual = ""
    if os.path.exists(caminho):
        with open(caminho, encoding="utf-8") as fh:
            atual = fh.read()
    if atual == conteudo:
        return
    mudou.append(os.path.relpath(caminho, RAIZ))
    if not conferir:
        with open(caminho, "w", encoding="utf-8") as fh:
            fh.write(conteudo)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conferir", action="store_true")
    args = ap.parse_args()

    achados = carregar_achados()
    problemas = validar(achados)
    if problemas:
        print("Problemas encontrados:", file=sys.stderr)
        for p in problemas:
            print(f"  - {p}", file=sys.stderr)
        if args.conferir:
            sys.exit(1)

    mudou: list = []
    escrever(INDICE, gerar_indice(achados), args.conferir, mudou)
    escrever(TAGS, gerar_tags(achados), args.conferir, mudou)

    if os.path.exists(README):
        with open(README, encoding="utf-8") as fh:
            readme = fh.read()
        novo = substituir_bloco(readme, "ESTATISTICAS", bloco_estatisticas(achados))
        novo = substituir_bloco(novo, "RECENTES", bloco_recentes(achados))
        escrever(README, novo, args.conferir, mudou)

    if args.conferir:
        if mudou:
            print("Índices desatualizados: " + ", ".join(mudou), file=sys.stderr)
            print("Rode: python3 scripts/indexar.py", file=sys.stderr)
            sys.exit(1)
        print("Índices em dia.")
    else:
        print(f"{len(achados)} achado(s) indexado(s)." + (f" Atualizado: {', '.join(mudou)}" if mudou else " Nada mudou."))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Regenera os indices a partir dos arquivos em achados/.

Gera:
  README.md  - a lista em si (sumario, secoes por categoria, estatisticas,
               recentes), no estilo das listas "awesome"
  TAGS.md    - mapa de tags -> achados

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
from lib_achados import (  # noqa: E402
    RAIZ, STATUS, TIPOS, Achado, ancora, carregar_achados, rotulo_categoria,
)

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
    """Um item no estilo awesome: nome com link para a origem, o que é numa
    frase, e os marcadores (licença, nota, análise, ressalva)."""
    marca = EMOJI_TIPO.get(a.tipo, "🔗")
    tldr = a.tldr.rstrip()
    if tldr and tldr[-1] not in ".!?":
        tldr += "."
    partes = [f"* {marca} [{a.nome}]({a.url or a.rel})"]
    if tldr:
        partes.append(f"- {tldr}")
    if a.licenca:
        partes.append(f"`{a.licenca}`")
    if a.nota:
        partes.append(estrelas(a.nota))
    partes.append(f"[análise]({a.rel})")
    if a.status and a.status != "novo":
        partes.append(f"<sub>{a.status}</sub>")
    linha_item = " ".join(partes)
    if a.alerta:
        linha_item += f"<br><sub>⚠️ {a.alerta}</sub>"
    return linha_item


PLURAL_TIPO = {
    "projeto": "Projetos", "artigo": "Artigos", "video": "Vídeos",
    "ferramenta": "Ferramentas", "biblioteca": "Bibliotecas", "curso": "Cursos",
    "paper": "Papers", "thread": "Threads", "newsletter": "Newsletters",
    "podcast": "Podcasts", "outro": "Outros",
}

# Acima deste número de itens, a categoria é subdividida por tipo — como as
# subseções do awesome-mac.
LIMITE_SUBSECAO = 4


def estrutura(achados):
    """Monta a árvore da lista uma única vez, para que o sumário e o corpo
    fiquem sempre em sincronia. Devolve [(nível, título, âncora, itens)].

    As âncoras seguem a regra do GitHub para títulos repetidos: o segundo
    'Ferramentas' vira 'ferramentas-1'.
    """
    por_cat = collections.defaultdict(list)
    for a in achados:
        for c in (a.categorias or ["sem-categoria"]):
            por_cat[c].append(a)

    ordem = lambda a: (-a.nota, a.nome.lower())  # noqa: E731
    vistas: collections.Counter = collections.Counter()

    def anc(titulo: str) -> str:
        base = ancora(titulo)
        vistas[base] += 1
        return base if vistas[base] == 1 else f"{base}-{vistas[base] - 1}"

    arvore = []
    for cat in sorted(por_cat, key=lambda c: (-len(por_cat[c]), c)):
        itens = por_cat[cat]
        rot = rotulo_categoria(cat)
        if len(itens) > LIMITE_SUBSECAO:
            arvore.append((2, rot, anc(rot), [], len(itens)))
            por_tipo = collections.defaultdict(list)
            for a in itens:
                por_tipo[a.tipo].append(a)
            for tipo in sorted(por_tipo, key=lambda t: (-len(por_tipo[t]), t)):
                t = PLURAL_TIPO.get(tipo, tipo.capitalize())
                itens_tipo = sorted(por_tipo[tipo], key=ordem)
                arvore.append((3, t, anc(t), itens_tipo, len(itens_tipo)))
        else:
            arvore.append((2, rot, anc(rot), sorted(itens, key=ordem), len(itens)))
    return arvore


def secoes_da_lista(achados) -> str:
    out = []
    for nivel, titulo, _, itens, _total in estrutura(achados):
        out += ["#" * nivel + f" {titulo}", ""]
        if itens:
            out += [linha(a) for a in itens]
            out.append("")
    return "\n".join(out).rstrip()


def sumario(achados) -> str:
    """Índice de âncoras, aninhado como o Contents do awesome-mac."""
    out = []
    for nivel, titulo, anc, _itens, total in estrutura(achados):
        recuo = "    " * (nivel - 2)
        out.append(f"{recuo}- [{titulo}](#{anc}) <sub>{total}</sub>")
    return "\n".join(out)


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
        if len(a.tldr) > 200:
            problemas.append(f"{a.rel}: 'tldr' longo demais ({len(a.tldr)} caracteres, máx. 200)")
        if len(a.alerta) > 160:
            problemas.append(f"{a.rel}: 'alerta' longo demais ({len(a.alerta)} caracteres, máx. 160)")
    return problemas


def gerar_tags(achados) -> str:
    por_tag = collections.defaultdict(list)
    for a in achados:
        for t in a.tags:
            por_tag[t].append(a)

    out = ["# Tags", "",
           f"{len(por_tag)} tag(s) em {len(achados)} achado(s) · gerado por `scripts/indexar.py` — não edite à mão.",
           "", "Volte para a lista completa: [README.md](README.md).", ""]
    if por_tag:
        nuvem = sorted(por_tag.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        out += ["## Mais usadas", "",
                " · ".join(f"[`{t}`](#{ancora(t)}) ({len(v)})" for t, v in nuvem[:30]), ""]
    for tag in sorted(por_tag):
        out.append(f"## {tag}")
        out.append("")
        out += [linha(a) for a in sorted(por_tag[tag], key=lambda a: (-a.nota, a.nome.lower()))]
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


def bloco_recentes(achados, n: int = 8) -> str:
    recentes = sorted(achados, key=lambda a: (a.adicionado, a.arquivo), reverse=True)[:n]
    if not recentes:
        return "_Nenhum achado ainda. Cole um link em [`INBOX.md`](INBOX.md) para começar._"
    return "\n".join(
        f"* `{a.adicionado}` [{a.nome}]({a.url or a.rel}) - {a.tldr}" for a in recentes
    )


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
    escrever(TAGS, gerar_tags(achados), args.conferir, mudou)

    if os.path.exists(README):
        with open(README, encoding="utf-8") as fh:
            readme = fh.read()
        novo = substituir_bloco(readme, "ESTATISTICAS", bloco_estatisticas(achados))
        novo = substituir_bloco(novo, "SUMARIO", sumario(achados))
        novo = substituir_bloco(novo, "LISTA", secoes_da_lista(achados))
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

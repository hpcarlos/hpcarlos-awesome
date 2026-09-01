#!/usr/bin/env python3
"""Importa o README do awesome-design-md para dados/design-md.tsv.

Parse determinístico do Markdown de origem. Cada item é um arquivo DESIGN.md
que replica a linguagem visual de um produto conhecido; a lista guarda o nome,
a URL e a breve descrição de estilo que a fonte já traz.

Uso:
    curl -sSL -o /tmp/adm.md \\
      https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/README.md
    python3 scripts/importar_design_md.py /tmp/adm.md
"""

from __future__ import annotations

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "dados", "design-md.tsv")

ITEM = re.compile(r"^[-*]\s+\[\*\*(?P<nome>[^\]]+?)\*\*\]\((?P<url>[^)]+)\)\s*-\s*(?P<desc>.+)$")

# Só as subseções dentro de "## Collection" são a lista; o resto do README é
# apresentação. Traduz os títulos das categorias.
TRADUCAO = {
    "AI & LLM Platforms": "Plataformas de IA e LLM",
    "Developer Tools & IDEs": "Ferramentas de desenvolvimento e IDEs",
    "Backend, Database & DevOps": "Backend, banco de dados e DevOps",
    "Productivity & SaaS": "Produtividade e SaaS",
    "Design & Creative Tools": "Design e ferramentas criativas",
    "Fintech & Crypto": "Fintech e cripto",
    "E-commerce & Retail": "Comércio eletrônico e varejo",
    "Media & Consumer Tech": "Mídia e tecnologia de consumo",
    "Automotive": "Automotivo",
    "Retro Web · DESIGN.md Nostalgia": "Web retrô · nostalgia",
}


def parse(caminho: str):
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()

    dentro_colecao = False
    categoria = None
    itens, novas = [], set()
    for linha in texto.split("\n"):
        if linha.startswith("## "):
            dentro_colecao = linha[3:].strip().lower() == "collection"
            categoria = None
            continue
        if linha.startswith("### ") and dentro_colecao:
            categoria = linha[4:].strip()
            if categoria not in TRADUCAO:
                novas.add(categoria)
            continue
        if not dentro_colecao or categoria is None:
            continue
        m = ITEM.match(linha.strip())
        if not m:
            continue
        itens.append((
            TRADUCAO.get(categoria, categoria),
            m.group("nome").replace("\t", " ").strip(),
            m.group("url").strip(),
            m.group("desc").replace("\t", " ").strip(),
        ))
    return itens, novas


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(2)
    itens, novas = parse(sys.argv[1])
    if not itens:
        print("erro: nenhum item reconhecido — o formato da fonte mudou?", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    with open(DESTINO, "w", encoding="utf-8") as fh:
        fh.write("# categoria\tnome\turl\tdescricao (estilo, original em inglês)\n")
        fh.write("# fonte: github.com/VoltAgent/awesome-design-md — gerado por scripts/importar_design_md.py\n")
        for it in itens:
            fh.write("\t".join(it) + "\n")

    print(f"{len(itens)} DESIGN.md em {len({i[0] for i in itens})} categorias")
    print(f"escrito em {os.path.relpath(DESTINO, RAIZ)}")
    if novas:
        print("\ncategorias sem tradução (acrescente em TRADUCAO):", file=sys.stderr)
        for c in sorted(novas):
            print(f"  - {c}", file=sys.stderr)


if __name__ == "__main__":
    main()

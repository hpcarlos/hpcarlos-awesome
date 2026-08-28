#!/usr/bin/env python3
"""Importa o README do awesome-selfhosted para dados/selfhosted.tsv.

O parse e deterministico: le o markdown de origem, nao um resumo. Cada item
daquela lista ja traz licenca e stack entre crases, e os projetos nao mantidos
sao marcados com um simbolo de alerta - tudo isso e preservado.

Uso:
    curl -sSL -o /tmp/ash.md \\
      https://raw.githubusercontent.com/awesome-selfhosted/awesome-selfhosted/master/README.md
    python3 scripts/importar_selfhosted.py /tmp/ash.md

Depois: python3 scripts/indexar_selfhosted.py
"""

from __future__ import annotations

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "dados", "selfhosted.tsv")

ITEM = re.compile(
    r"^- \[(?P<nome>[^\]]+)\]\((?P<url>[^)]+)\)\s*"
    r"(?P<flag>`⚠`\s*)?"
    r"-\s*(?P<resto>.+)$"
)

# Titulos em portugues para as categorias da fonte. Categoria nova que apareca
# numa reimportacao cai no fallback (o nome original) e e reportada no fim.
TRADUCAO = {
    "Analytics": "Analytics e métricas de uso",
    "Archiving and Digital Preservation (DP)": "Arquivamento e preservação digital",
    "Automation": "Automação",
    "Blogging Platforms": "Plataformas de blog",
    "Booking and Scheduling": "Agendamento e reservas",
    "Bookmarks and Link Sharing": "Favoritos e compartilhamento de links",
    "Calendar & Contacts": "Agenda e contatos",
    "Communication - Custom Communication Systems": "Comunicação — sistemas de mensagem",
    "Communication - Email - Complete Solutions": "E-mail — soluções completas",
    "Communication - Email - Mail Delivery Agents": "E-mail — entrega (MDA)",
    "Communication - Email - Mail Transfer Agents": "E-mail — transporte (MTA)",
    "Communication - Email - Mailing Lists and Newsletters": "E-mail — listas e newsletters",
    "Communication - Email - Webmail Clients": "E-mail — clientes web",
    "Communication - IRC": "Comunicação — IRC",
    "Communication - SIP": "Comunicação — SIP e telefonia",
    "Communication - Social Networks and Forums": "Redes sociais e fóruns",
    "Communication - Video Conferencing": "Videoconferência",
    "Communication - XMPP - Servers": "XMPP — servidores",
    "Communication - XMPP - Web Clients": "XMPP — clientes web",
    "Community-Supported Agriculture (CSA)": "Agricultura comunitária",
    "Conference Management": "Gestão de eventos e conferências",
    "Content Management Systems (CMS)": "Gerenciadores de conteúdo (CMS)",
    "Customer Relationship Management (CRM)": "CRM",
    "DNS": "DNS",
    "Database Management": "Administração de banco de dados",
    "Document Management": "Gestão de documentos",
    "Document Management - E-books": "Documentos — e-books",
    "Document Management - Institutional Repository and Digital Library Software":
        "Documentos — repositórios e bibliotecas digitais",
    "Document Management - Integrated Library Systems (ILS)": "Documentos — sistemas de biblioteca",
    "E-commerce": "Comércio eletrônico",
    "Feed Readers": "Leitores de feed",
    "File Transfer & Synchronization": "Transferência e sincronização de arquivos",
    "File Transfer - Object Storage & File Servers": "Arquivos — armazenamento de objetos",
    "File Transfer - Peer-to-peer Filesharing": "Arquivos — compartilhamento P2P",
    "File Transfer - Single-click & Drag-n-drop Upload": "Arquivos — upload rápido",
    "File Transfer - Web-based File Managers": "Arquivos — gerenciadores web",
    "Games": "Jogos",
    "Games - Administrative Utilities & Control Panels": "Jogos — painéis e administração",
    "Genealogy": "Genealogia",
    "Generative Artificial Intelligence (GenAI)": "IA generativa",
    "Groupware": "Groupware",
    "Health and Fitness": "Saúde e exercício",
    "Human Resources Management (HRM)": "Gestão de pessoas (RH)",
    "Internet of Things (IoT)": "Internet das coisas (IoT)",
    "Inventory Management": "Controle de estoque",
    "Knowledge Management Tools": "Gestão de conhecimento",
    "Learning and Courses": "Ensino e cursos",
    "Manufacturing": "Manufatura",
    "Maps and Global Positioning System (GPS)": "Mapas e GPS",
    "Media Management": "Gestão de mídia",
    "Media Streaming - Audio Streaming": "Streaming — áudio",
    "Media Streaming - Multimedia Streaming": "Streaming — multimídia",
    "Media Streaming - Video Streaming": "Streaming — vídeo",
    "Miscellaneous": "Diversos",
    "Money, Budgeting & Management": "Finanças pessoais e orçamento",
    "Network Utilities": "Utilitários de rede",
    "Note-taking & Editors": "Notas e editores",
    "Office Suites": "Suítes de escritório",
    "Password Managers": "Gerenciadores de senha",
    "Pastebins": "Pastebins",
    "Personal Dashboards": "Painéis pessoais",
    "Photo Galleries": "Galerias de fotos",
    "Polls and Events": "Enquetes e eventos",
    "Proxy": "Proxy",
    "Recipe Management": "Receitas culinárias",
    "Remote Access": "Acesso remoto",
    "Resource Planning": "Planejamento de recursos (ERP)",
    "Search Engines": "Buscadores",
    "Self-hosting Solutions": "Plataformas de auto-hospedagem",
    "Software Development - API Management": "Desenvolvimento — gestão de APIs",
    "Software Development - Feature Toggle": "Desenvolvimento — feature flags",
    "Software Development - IDE & Tools": "Desenvolvimento — IDEs e ferramentas",
    "Software Development - Localization": "Desenvolvimento — localização e tradução",
    "Software Development - Low Code": "Desenvolvimento — low code",
    "Software Development - Project Management": "Desenvolvimento — gestão de projetos",
    "Software Development - Testing": "Desenvolvimento — testes",
    "Task Management & To-do Lists": "Tarefas e listas",
    "Ticketing": "Chamados e suporte",
    "Time Tracking": "Controle de tempo",
    "Travel Organization": "Viagens",
    "URL Shorteners": "Encurtadores de URL",
    "Video Surveillance": "Vigilância por vídeo",
    "Web Servers": "Servidores web",
    "Wikis": "Wikis",
}


# Seções da fonte que não listam software auto-hospedável.
IGNORAR = {"External Links", "Contributing", "License"}


def parse(caminho: str):
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()

    secao = categoria = None
    itens, novas = [], set()
    for linha in texto.split("\n"):
        if linha.startswith("## "):
            secao = linha[3:].strip()
            categoria = None
            continue
        if linha.startswith("### "):
            categoria = linha[4:].strip()
            continue
        if not linha.startswith("- [") or "`" not in linha:
            continue
        m = ITEM.match(linha)
        if not m:
            continue
        # itens soltos direto sob uma seção herdam o nome dela
        origem = categoria or secao
        if origem is None or origem in IGNORAR:
            continue
        if origem not in TRADUCAO:
            novas.add(origem)

        resto = m.group("resto")
        marcas = re.findall(r"`([^`]+)`", resto)
        desc = re.sub(r"\s*`[^`]+`", "", resto)
        desc = re.sub(r"\s*\(\[(?:Demo|Source Code|Clients)\].*?\)\s*$", "", desc).strip()
        desc = desc.replace("\t", " ")
        itens.append((
            TRADUCAO.get(origem, origem),
            m.group("nome").replace("\t", " "),
            m.group("url"),
            marcas[0] if marcas else "",
            marcas[1] if len(marcas) > 1 else "",
            "sim" if m.group("flag") else "",
            desc,
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
        fh.write("# categoria\tnome\turl\tlicenca\tstack\tnaomantido\tdescricao (original em inglês)\n")
        fh.write("# fonte: github.com/awesome-selfhosted/awesome-selfhosted — gerado por scripts/importar_selfhosted.py\n")
        for it in itens:
            fh.write("\t".join(it) + "\n")

    naomantidos = sum(1 for i in itens if i[5])
    cats = len({i[0] for i in itens})
    print(f"{len(itens)} projetos em {cats} categorias · {naomantidos} marcados como não mantidos")
    print(f"escrito em {os.path.relpath(DESTINO, RAIZ)}")
    if novas:
        print("\ncategorias sem tradução (acrescente em TRADUCAO):", file=sys.stderr)
        for c in sorted(novas):
            print(f"  - {c}", file=sys.stderr)


if __name__ == "__main__":
    main()

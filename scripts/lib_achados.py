"""Utilitarios compartilhados: leitura dos achados em achados/*.md.

Sem dependencias externas - roda com Python 3.8+ puro.
Cada achado e um arquivo Markdown com front-matter YAML simples:

    ---
    titulo: Nome do achado
    url: https://exemplo.com
    tipo: artigo
    categorias: [ia, ferramentas]
    tags: [python, llm]
    status: novo
    nota: 4
    adicionado: 2026-08-21
    ---
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_ACHADOS = os.path.join(RAIZ, "achados")

# Rotulos legiveis das categorias, usados nos titulos de secao do README.
ROTULOS_CATEGORIA = {
    "ia": "Inteligência artificial",
    "engenharia": "Engenharia de software",
    "devops": "Infraestrutura e DevOps",
    "web": "Web",
    "design": "Design",
    "seguranca": "Segurança",
    "negocios": "Negócios",
    "dados": "Dados",
    "hardware": "Hardware",
    "carreira": "Carreira",
}


def rotulo_categoria(cat: str) -> str:
    return ROTULOS_CATEGORIA.get(cat, cat.replace("-", " ").capitalize())


def ancora(titulo: str) -> str:
    """Ancora no estilo do GitHub: minusculas, espacos viram hifen,
    pontuacao removida (acentos sao preservados)."""
    import unicodedata
    t = titulo.strip().lower()
    saida = []
    for ch in t:
        if ch.isalnum() or ch in "-_ ":
            saida.append(ch)
        elif unicodedata.category(ch).startswith("M"):
            saida.append(ch)
    return "".join(saida).replace(" ", "-")


TIPOS = [
    "projeto", "artigo", "video", "ferramenta", "biblioteca",
    "curso", "paper", "thread", "newsletter", "podcast", "outro",
]
STATUS = ["novo", "lendo", "lido", "testado", "usado", "arquivado"]

# Campos de lista no front-matter.
CAMPOS_LISTA = ("categorias", "tags", "relacionados")


def _limpa(valor: str) -> str:
    valor = valor.strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
        valor = valor[1:-1]
    return valor.strip()


def _parse_lista(valor: str) -> List[str]:
    valor = valor.strip()
    if valor.startswith("[") and valor.endswith("]"):
        valor = valor[1:-1]
    itens = [_limpa(p) for p in valor.split(",")]
    return [i for i in itens if i]


def parse_front_matter(texto: str) -> Dict[str, Any]:
    """Le o bloco --- ... --- do topo do arquivo. Suporta listas inline,
    listas em bloco (- item) e valores escalares."""
    if not texto.startswith("---"):
        return {}
    fim = texto.find("\n---", 3)
    if fim == -1:
        return {}
    bloco = texto[3:fim].strip("\n")

    dados: Dict[str, Any] = {}
    chave_atual = None
    for linha in bloco.split("\n"):
        if not linha.strip() or linha.strip().startswith("#"):
            continue
        # Item de lista em bloco: "  - valor"
        if linha.lstrip().startswith("- ") and chave_atual:
            item = _limpa(linha.lstrip()[2:])
            if item:
                dados.setdefault(chave_atual, [])
                if isinstance(dados[chave_atual], list):
                    dados[chave_atual].append(item)
            continue
        if ":" not in linha:
            continue
        chave, _, valor = linha.partition(":")
        chave = chave.strip()
        valor = valor.strip()
        chave_atual = chave
        if valor == "":
            dados[chave] = [] if chave in CAMPOS_LISTA else ""
        elif valor.startswith("["):
            dados[chave] = _parse_lista(valor)
        elif chave in CAMPOS_LISTA:
            dados[chave] = _parse_lista(valor)
        else:
            dados[chave] = _limpa(valor)
    return dados


def corpo_markdown(texto: str) -> str:
    if not texto.startswith("---"):
        return texto
    fim = texto.find("\n---", 3)
    if fim == -1:
        return texto
    return texto[fim + 4:].lstrip("\n")


@dataclass
class Achado:
    caminho: str
    meta: Dict[str, Any]
    corpo: str

    @property
    def arquivo(self) -> str:
        return os.path.basename(self.caminho)

    @property
    def rel(self) -> str:
        return os.path.relpath(self.caminho, RAIZ).replace(os.sep, "/")

    @property
    def titulo(self) -> str:
        return str(self.meta.get("titulo") or os.path.splitext(self.arquivo)[0])

    @property
    def url(self) -> str:
        return str(self.meta.get("url") or "")

    @property
    def nome(self) -> str:
        """Nome curto usado nas listagens. Cai para a parte do titulo antes
        do primeiro separador (ex.: "impeccable - design language" -> "impeccable")."""
        v = str(self.meta.get("nome") or "").strip()
        if v:
            return v
        t = self.titulo
        for sep in (" \u2014 ", " \u2013 ", " - ", ": "):
            if sep in t:
                return t.split(sep)[0].strip()
        return t

    @property
    def tldr(self) -> str:
        """Uma frase sobre o que a coisa e / para que serve. Cai para a
        primeira frase do ## Resumo."""
        v = str(self.meta.get("tldr") or "").strip()
        if v:
            return v
        r = self.resumo
        if not r or r.startswith("_(") or r.startswith(">"):
            return ""
        m = re.match(r"(.+?[.!?])(?:\s|$)", r)
        frase = m.group(1) if m else r
        if len(frase) > 170:
            frase = frase[:167].rsplit(" ", 1)[0] + "\u2026"
        return frase

    @property
    def licenca(self) -> str:
        """Licenca declarada (MIT, Apache-2.0, ...). Vazio se desconhecida."""
        return str(self.meta.get("licenca") or "").strip()

    @property
    def alerta(self) -> str:
        """Ressalva curta exibida na listagem (licenca restritiva, risco de
        termos de uso, software alpha...). Vazio quando nao ha."""
        return str(self.meta.get("alerta") or "").strip()

    @property
    def dominio(self) -> str:
        """Dominio da url, para exibir um link curto."""
        from urllib.parse import urlparse
        d = urlparse(self.url).netloc.lower()
        return d[4:] if d.startswith("www.") else d

    @property
    def tipo(self) -> str:
        return str(self.meta.get("tipo") or "outro")

    @property
    def status(self) -> str:
        return str(self.meta.get("status") or "novo")

    @property
    def adicionado(self) -> str:
        return str(self.meta.get("adicionado") or "")

    @property
    def nota(self) -> int:
        try:
            return int(str(self.meta.get("nota") or 0))
        except ValueError:
            return 0

    @property
    def categorias(self) -> List[str]:
        v = self.meta.get("categorias") or []
        return [v] if isinstance(v, str) and v else list(v)

    @property
    def tags(self) -> List[str]:
        v = self.meta.get("tags") or []
        return [v] if isinstance(v, str) and v else list(v)

    @property
    def resumo(self) -> str:
        """Primeiro paragrafo apos o titulo/secao Resumo, para os indices."""
        m = re.search(r"##\s*Resumo\s*\n+(.+?)(?:\n\s*\n|\n##)", self.corpo, re.S)
        if m:
            return " ".join(m.group(1).split())
        for par in self.corpo.split("\n\n"):
            par = par.strip()
            if par and not par.startswith("#"):
                return " ".join(par.split())
        return ""


def carregar_achados(diretorio: str = DIR_ACHADOS) -> List[Achado]:
    achados: List[Achado] = []
    if not os.path.isdir(diretorio):
        return achados
    for nome in sorted(os.listdir(diretorio)):
        if not nome.endswith(".md") or nome.startswith("_"):
            continue
        caminho = os.path.join(diretorio, nome)
        with open(caminho, encoding="utf-8") as fh:
            texto = fh.read()
        achados.append(Achado(caminho, parse_front_matter(texto), corpo_markdown(texto)))
    return achados


def slugify(texto: str, limite: int = 60) -> str:
    import unicodedata
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    texto = re.sub(r"[^a-z0-9]+", "-", texto).strip("-")
    if len(texto) > limite:
        texto = texto[:limite].rstrip("-")
    return texto or "achado"


def erro(msg: str) -> None:
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)

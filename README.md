# 🧭 Achados

Minha biblioteca pessoal de coisas boas encontradas na internet: projetos, artigos,
ferramentas, papers e vídeos — organizados, resumidos e cruzados entre si, com ideias
concretas do que dá para construir com eles.

Cada achado vira um arquivo em [`achados/`](achados/) com metadados (tipo, categorias,
tags, nota, status) e um resumo em português. Os índices são gerados automaticamente.

<!-- INICIO:ESTATISTICAS -->
**0** achados · **0** categorias · **0** tags · atualizado em 2026-08-21

| tipo | qtd. |  | status | qtd. |
| --- | ---: | --- | --- | ---: |
|  |  |  |  |  |
<!-- FIM:ESTATISTICAS -->

## Como usar

### Mandar um link novo

O jeito mais simples: cole a URL em [`INBOX.md`](INBOX.md) (uma por linha, com um
comentário se quiser) e peça ao Claude para processar a caixa de entrada. Ele lê a
página, escreve o resumo, classifica, cruza com o que já existe e regenera os índices.

Ou peça direto na conversa: *"guarda esse link aqui: ..."*

### Registrar manualmente

```bash
python3 scripts/novo.py https://exemplo.com/artigo \
  --titulo "Título do artigo" \
  --tipo artigo --categorias ia --tags rag,python --nota 4
python3 scripts/indexar.py
```

### Encontrar algo depois

```bash
python3 scripts/buscar.py rag --detalhe        # busca por texto
python3 scripts/buscar.py --tag python         # por tag
python3 scripts/buscar.py --categoria ia --tipo projeto --nota-min 4
python3 scripts/buscar.py --tags               # lista as tags existentes
```

Ou simplesmente navegue por [`INDICE.md`](INDICE.md) e [`TAGS.md`](TAGS.md).

## Mapa do repositório

| Caminho | O que é |
| --- | --- |
| [`INBOX.md`](INBOX.md) | Caixa de entrada — cole links crus aqui |
| [`achados/`](achados/) | Um arquivo Markdown por achado (fonte da verdade) |
| [`INDICE.md`](INDICE.md) | Índice por categoria, data e status — **gerado** |
| [`TAGS.md`](TAGS.md) | Mapa de tags → achados — **gerado** |
| [`IDEIAS.md`](IDEIAS.md) | Projetos que dá para construir cruzando os achados |
| [`modelos/achado.md`](modelos/achado.md) | Template de um achado |
| [`scripts/`](scripts/) | `novo.py`, `indexar.py`, `buscar.py` (Python puro, sem deps) |
| [`CLAUDE.md`](CLAUDE.md) | O fluxo que o Claude segue ao organizar tudo isso |
| [`modelos/github-workflow-indices.yml`](modelos/github-workflow-indices.yml) | CI opcional que confere os índices — copie para `.github/workflows/` |

## Últimos achados

<!-- INICIO:RECENTES -->
_Nenhum achado ainda. Cole um link em [`INBOX.md`](INBOX.md) para começar._
<!-- FIM:RECENTES -->

---

<sub>Índices gerados por `scripts/indexar.py`. Não edite `INDICE.md` nem `TAGS.md` à mão.</sub>

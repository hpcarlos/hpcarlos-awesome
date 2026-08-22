# 🧭 Achados

Minha biblioteca pessoal de coisas boas encontradas na internet: projetos, artigos,
ferramentas, papers e vídeos — organizados, resumidos e cruzados entre si, com ideias
concretas do que dá para construir com eles.

Cada achado vira um arquivo em [`achados/`](achados/) com metadados (tipo, categorias,
tags, nota, status) e um resumo em português. Nas listagens aparece só o nome curto e uma
frase dizendo o que a coisa é — o resto está a um clique. Os índices são gerados
automaticamente.

<!-- INICIO:ESTATISTICAS -->
**4** achados · **6** categorias · **21** tags · atualizado em 2026-08-22

| tipo | qtd. |  | status | qtd. |
| --- | ---: | --- | --- | ---: |
| ferramenta | 2 |  | novo | 4 |
| projeto | 2 |  |  |  |

Categorias: `design` · `devops` · `ia` · `negocios` · `seguranca` · `web`
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
  --titulo "Título do artigo" --nome "nome-curto" \
  --tldr "O que é e para que serve, em uma frase." \
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
- `2026-08-22` 🛠 **[wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)** — CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta.<br><sub>projeto · ★★★☆☆ · [github.com ↗](https://github.com/ArnasDon/wacrm) · `whatsapp` `crm` `nextjs` `supabase` `self-hosted` `typescript` `mcp`</sub>
- `2026-08-22` 🛠 **[saas-starter-kit](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)** — Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos.<br><sub>projeto · ★★★★☆ · [github.com ↗](https://github.com/boxyhq/saas-starter-kit) · `nextjs` `typescript` `saas` `prisma` `postgres` `auth` `boilerplate`</sub>
- `2026-08-21` ⚙️ **[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)** — Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba.<br><sub>ferramenta · ★★★★☆ · [github.com ↗](https://github.com/diegosouzapw/OmniRoute) · `gateway` `llm` `self-hosted` `claude-code` `cli` `openai-api`</sub>
- `2026-08-21` ⚙️ **[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)** — Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais.<br><sub>ferramenta · ★★★★☆ · [github.com ↗](https://github.com/pbakaus/impeccable) · `frontend` `ui` `claude-code` `cli` `skills` `linter`</sub>
<!-- FIM:RECENTES -->

---

<sub>Índices gerados por `scripts/indexar.py`. Não edite `INDICE.md` nem `TAGS.md` à mão.</sub>

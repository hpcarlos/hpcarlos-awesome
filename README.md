# 🧭 Achados

Minha biblioteca pessoal de coisas boas encontradas na internet: projetos, artigos,
ferramentas, papers e vídeos — organizados, resumidos e cruzados entre si, com ideias
concretas do que dá para construir com eles.

Cada achado vira um arquivo em [`achados/`](achados/) com metadados (tipo, categorias,
tags, nota, status) e um resumo em português. Nas listagens aparece só o nome curto e uma
frase dizendo o que a coisa é — o resto está a um clique. Os índices são gerados
automaticamente.

<!-- INICIO:ESTATISTICAS -->
**12** achados · **7** categorias · **37** tags · atualizado em 2026-08-27

| tipo | qtd. |  | status | qtd. |
| --- | ---: | --- | --- | ---: |
| ferramenta | 6 |  | novo | 12 |
| projeto | 5 |  |  |  |
| outro | 1 |  |  |  |

Categorias: `design` · `devops` · `engenharia` · `ia` · `negocios` · `seguranca` · `web`
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
- `2026-08-27` 🛠 **[lobehub](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)** — Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais.<br><sub>projeto · ★★★☆☆ · [github.com ↗](https://github.com/lobehub/lobehub) · `agentes` `self-hosted` `nextjs` `mcp` `chat` `typescript`</sub>
- `2026-08-27` ⚙️ **[bifrost](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)** — Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus.<br><sub>ferramenta · ★★★★☆ · [github.com ↗](https://github.com/maximhq/bifrost) · `gateway` `go` `llm` `openai-api` `observabilidade` `self-hosted` `mcp`</sub>
- `2026-08-23` 🔗 **[system-prompts](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)** — Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar.<br><sub>outro · ★★★☆☆ · [github.com ↗](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) · `prompts` `llm` `agentes` `prompt-engineering` `referencia`</sub>
- `2026-08-23` ⚙️ **[mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)** — Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só.<br><sub>ferramenta · ★★★★☆ · [github.com ↗](https://github.com/builderz-labs/mission-control) · `agentes` `self-hosted` `nextjs` `sqlite` `mcp` `observabilidade` `typescript`</sub>
- `2026-08-22` 🛠 **[wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)** — CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta.<br><sub>projeto · ★★★☆☆ · [github.com ↗](https://github.com/ArnasDon/wacrm) · `whatsapp` `crm` `nextjs` `supabase` `self-hosted` `typescript` `mcp`</sub>
- `2026-08-22` 🛠 **[sub2api](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)** — Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso.<br><sub>projeto · ★★☆☆☆ · [github.com ↗](https://github.com/Wei-Shaw/sub2api) · `gateway` `go` `self-hosted` `llm` `billing` `api`</sub>
- `2026-08-22` 🛠 **[munder-difflin](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)** — App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art.<br><sub>projeto · ★★★☆☆ · [github.com ↗](https://github.com/chaitanyagiri/munder-difflin) · `agentes` `electron` `multiagente` `claude-code` `typescript` `cli`</sub>
- `2026-08-22` ⚙️ **[mattpocock/skills](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)** — Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review.<br><sub>ferramenta · ★★★★★ · [github.com ↗](https://github.com/mattpocock/skills) · `claude-code` `skills` `agentes` `workflow` `tdd` `code-review`</sub>
- `2026-08-22` 🛠 **[saas-starter-kit](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)** — Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos.<br><sub>projeto · ★★★★☆ · [github.com ↗](https://github.com/boxyhq/saas-starter-kit) · `nextjs` `typescript` `saas` `prisma` `postgres` `auth` `boilerplate`</sub>
- `2026-08-22` ⚙️ **[addyosmani/agent-skills](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)** — 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias.<br><sub>ferramenta · ★★★★★ · [github.com ↗](https://github.com/addyosmani/agent-skills) · `claude-code` `skills` `agentes` `workflow` `tdd` `code-review` `performance`</sub>
<!-- FIM:RECENTES -->

---

<sub>Índices gerados por `scripts/indexar.py`. Não edite `INDICE.md` nem `TAGS.md` à mão.</sub>

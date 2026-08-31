---
titulo: "Apify MCP Server — milhares de scrapers prontos como ferramentas de agente"
nome: apify-mcp-server
tldr: "Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso."
licenca: "MIT"
alerta: "o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify"
url: https://github.com/apify/apify-mcp-server
tipo: ferramenta
categorias: [ia, web]
tags: [mcp, scraping, agentes, apify, claude-code, dados]
status: novo
nota: 4
adicionado: 2026-08-31
fonte: enviado pelo hpcarlos
relacionados: [2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md, 2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md]
---

# Apify MCP Server — milhares de scrapers prontos como ferramentas de agente

## Resumo

Servidor MCP oficial da Apify que abre a loja de Actors dela — milhares de scrapers,
crawlers e ferramentas de automação prontos — como ferramentas que o agente descobre e usa
sozinho. Na prática, o agente pesquisa um Actor (`search-actors`), lê a configuração
(`fetch-actor-details`), executa (`call-actor`) e recebe o resultado (`get-dataset-items`),
tudo dentro da conversa. Já vem com dois Actors de leitura de web configurados e alcança o
resto da loja por descoberta dinâmica. TypeScript/Node, licença MIT, com transporte por HTTP
(hospedado em `mcp.apify.com`) ou stdio local.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o outro extremo do problema de dar acesso à web ao agente. O
[agent-reach](2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)
é a via gratuita e caseira, com risco de banimento por conta própria; este é a via
comercial, paga e mantida por uma empresa que assume a parte suja do scraping. Ter os dois
catalogados deixa a escolha explícita, em vez de refém do primeiro que apareceu.

## Pontos-chave

- **⚠️ O servidor é grátis; o uso não.** O código é MIT e aberto, mas cada Actor executado
  consome crédito da Apify, que é pago por uso e exige token de conta. Não há preço fixo — o
  custo varia por Actor e por volume. É a distinção que decide tudo: você não está adotando um
  software gratuito, está integrando um serviço cobrado por chamada.
- **A vantagem sobre fazer você mesmo:** a Apify mantém os scrapers funcionando quando os
  sites mudam, lida com proxy e bloqueio, e assume o risco de infraestrutura de raspar em
  escala. É por isso que se paga — pelo mesmo motivo que o
  [sub2api](2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md) e o
  [camofox-browser](2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)
  existem, mas aqui de forma legítima e com nota fiscal.
- **Descoberta dinâmica é o que o torna poderoso.** Em vez de expor uma lista fixa, ele deixa
  o agente **buscar** o Actor certo para a tarefa no momento. É o padrão MCP bem usado:
  ferramenta que cresce sem reconfiguração.
- **Oficial e bem mantido** — repositório da própria Apify, listado no registro de MCP do
  Docker, com suporte a Claude Desktop, Claude.ai, Cursor, VS Code e ChatGPT. Isso importa num
  servidor MCP: um mal mantido é porta de entrada de problema.
- **⚠️ Telemetria ligada por padrão** (desativável por flag) — mais um caso do checklist de
  primeira execução do `IDEIAS.md`. E alguns modos de pagamento alternativos (x402, Skyfire)
  têm limitações de leitura de dados que valem conferir antes de escolher.
- **⚠️ A responsabilidade de uso é sua.** A Apify cuida da infraestrutura, mas raspar site de
  terceiro tem os mesmos limites de termos de uso de sempre; a plataforma reduz o risco
  técnico e de banimento, não o jurídico. Ler dado público é uma coisa; o que você faz com ele
  é outra.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **A camada paga do vigia de achados** — quando o [agent-reach](2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)
  gratuito não bastar (bloqueio, escala, plataforma difícil), o Apify entra como plano B pago
  para a mesma coleta que alimenta a `INBOX.md`. A regra: gratuito primeiro, pago só onde
  doer. _Esforço: baixo._
- **Decidir grátis-vs-pago com número** — rodar a mesma coleta de uma fonte pelos dois
  caminhos e comparar: quanto de esforço de manutenção o agent-reach exige, contra quanto o
  Apify cobra por rodar sem você mexer. É a conta que decide qual usar em cada caso, e ela é
  sua, não do README. _Esforço: médio._
- **Alimentar RAG com dado fresco** — os Actors de e-commerce, busca e mapas entregam dado
  estruturado que uma das 21 variantes de RAG do
  [awesome-llm-apps](2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)
  consome direto. O Apify é a fonte, o RAG é o consumidor. _Esforço: médio._
- **Começar pelos dois Actors grátis de leitura** — o `rag-web-browser` e o `web-fetch` que já
  vêm configurados cobrem "ler uma página bem" sem entrar na loja paga. É o jeito de
  experimentar o servidor MCP sem gastar, e de decidir se vale ir além. _Esforço: baixo._

## Notas

```bash
# local, via stdio
export APIFY_TOKEN="seu-token"
npx @apify/actors-mcp-server

# escolhendo o conjunto de ferramentas
npx @apify/actors-mcp-server --tools actors,docs,apify/rag-web-browser
```

```json
// Claude Desktop
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["@apify/actors-mcp-server"],
      "env": { "APIFY_TOKEN": "seu-token" }
    }
  }
}
```

- Versão hospedada em `https://mcp.apify.com` (OAuth ou Bearer token), recomendada pela
  Apify; a local por stdio não faz descoberta dinâmica dos Actors "de aluguel".
- Requer Node 22+ e um token da Apify (conta paga para a maior parte dos Actors).
- **Antes de conectar:** entender que cada execução gasta crédito. Um agente que chama Actor
  em laço pode gerar conta alta rápido — vale um teto de gasto na conta da Apify, no mesmo
  espírito das chaves virtuais do [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md).

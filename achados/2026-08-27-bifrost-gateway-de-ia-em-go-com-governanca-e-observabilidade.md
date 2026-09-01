---
titulo: "bifrost — gateway de IA em Go com governança e observabilidade"
nome: bifrost
tldr: "Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus."
licenca: "Apache-2.0"
alerta: "modelo open core: cluster e recursos avançados ficam na edição paga"
url: https://github.com/maximhq/bifrost
tipo: ferramenta
categorias: [ia, devops]
tags: [gateway, go, llm, openai-api, observabilidade, self-hosted, mcp]
status: novo
nota: 4
adicionado: 2026-08-27
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md, 2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md, 2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md, 2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md]
---

# bifrost — gateway de IA em Go com governança e observabilidade

## Resumo

Gateway de IA escrito em Go que expõe uma única API compatível com a OpenAI na frente de
mais de 20 provedores (OpenAI, Anthropic, Bedrock, Vertex, Azure, Groq, Mistral, Cohere,
Ollama e outros), com fallback automático entre eles. O que o distingue dos gateways
parecidos é a camada de governança: chaves virtuais com permissão granular, limite de
requisição e de gasto em hierarquia, cache semântico por similaridade — que corta custo e
latência em pergunta repetida — métricas nativas em Prometheus, rastreamento distribuído e
suporte a MCP para o modelo usar ferramentas externas. Licença Apache 2.0, com edição
enterprise paga por cima.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o terceiro gateway da coleção e o primeiro que se pode adotar sem ressalva
jurídica. Onde o [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
depende de tiers gratuitos instáveis e o [sub2api](2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)
avisa que pode violar termos de serviço, este roda sobre suas próprias chaves, com licença
permissiva e instrumentação de produção.

## Qual gateway usar, afinal

Três achados resolvem o mesmo problema por caminhos diferentes — vale fixar o critério:

| | licença | de onde vem o acesso | quando escolher |
| --- | --- | --- | --- |
| **bifrost** | Apache 2.0 | suas próprias chaves | produto, cliente, qualquer coisa séria |
| **OmniRoute** | MIT | tiers gratuitos públicos | experimento pessoal, baratear seu uso |
| **sub2api** | LGPL-3.0 | assinaturas redistribuídas | nenhum — só leitura de arquitetura |

## Pontos-chave

- **Licença Apache 2.0** no núcleo, com edição enterprise paga (cluster multi-nó,
  guardrails, balanceamento adaptativo, provisionamento por OIDC/OAuth, suporte). O modelo
  é open core: o essencial é aberto, a operação em escala é vendida. Saber disso antecipa
  onde vão aparecer os limites.
- **Cache semântico** é o recurso de maior retorno prático: respostas reaproveitadas por
  similaridade, não por igualdade exata de string. Em aplicação com perguntas repetidas —
  um atendimento, por exemplo — muda a conta.
- **Chaves virtuais com governança hierárquica** resolvem o problema real de dar acesso a
  time ou a cliente sem distribuir a chave verdadeira do provedor, com teto de gasto por
  chave.
- **Observabilidade de gente grande:** Prometheus nativo e tracing distribuído. É o que
  falta nos outros gateways da coleção e o que torna possível responder "onde foi o
  dinheiro" sem gambiarra.
- **Instalação em 30 segundos** via `npx` ou Docker, com interface web em `localhost:8080`.
  Há também SDK em Go para embutir o gateway na sua aplicação em vez de rodá-lo como
  serviço.
- **⚠️ Sobre a performance anunciada:** o projeto divulga números fortes (poucos
  microssegundos de sobrecarga a 5.000 requisições por segundo) e a comparação "50x mais
  rápido que o LiteLLM". São **benchmarks do próprio autor contra um concorrente** — o tipo
  de número que se mede em casa antes de repetir. Na prática, a latência é dominada pelo
  provedor, não pelo gateway.
- **Números de adoção não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Promover o bifrost a gateway padrão dos projetos sérios** — deixar o OmniRoute para
  experimento pessoal e usar este onde houver cliente ou produto:
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md),
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
  ou qualquer coisa que vá para produção. Ambos falam OpenAI, então a troca é de URL base.
  _Esforço: baixo._
- **Fechar de vez a conta dos agentes** — as métricas Prometheus daqui, somadas ao gasto
  por execução do [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md),
  dão o painel de custo que ficou em aberto em `IDEIAS.md`. Aqui há dado estruturado de
  verdade, não SQLite improvisado. _Esforço: médio._
- **Medir o cache semântico com dado real** — subir o gateway, ligar o cache e rodar um
  conjunto de perguntas repetidas de um caso seu, anotando taxa de acerto e economia. É o
  recurso mais vendável e o mais fácil de superestimar; vale o número medido.
  _Esforço: baixo._
- **Chave virtual por cliente** — se um dia você entregar um produto de IA para terceiros,
  emitir uma chave virtual com teto de gasto por cliente é a diferença entre saber e não
  saber quanto cada um consome. Combina com a cobrança do
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md).
  _Esforço: médio._

## Notas

```bash
# subir em segundos
npx -y @maximhq/bifrost
docker run -p 8080:8080 maximhq/bifrost
docker run -p 8080:8080 -v $(pwd)/data:/app/data maximhq/bifrost   # com persistência

# primeira requisição
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-4o-mini", "messages": [{"role":"user","content":"Hello, Bifrost!"}]}'

# como biblioteca, dentro de um serviço em Go
go get github.com/maximhq/bifrost/core
```

- Interface web em `http://localhost:8080` depois de subir.
- Integra com SDKs existentes (OpenAI, Anthropic, LangChain, LiteLLM) sem reescrever
  cliente.
- Documentação em docs.getbifrost.ai.
- **Antes de adotar:** confirmar quais recursos ficam na edição paga. Em projeto open core,
  é comum o cluster e o controle fino de acesso morarem do lado comercial.

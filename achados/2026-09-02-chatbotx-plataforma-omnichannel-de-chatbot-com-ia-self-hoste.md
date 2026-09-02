---
titulo: "ChatbotX — plataforma omnichannel de chatbot com IA, self-hosted"
nome: ChatbotX
tldr: "Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP."
licenca: "MIT + comercial"
alerta: "licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade"
url: https://github.com/ChatbotXIO/ChatbotX
tipo: projeto
categorias: [web, negocios]
tags: [chatbot, omnichannel, automacao, nextjs, self-hosted, crm, mcp]
status: novo
nota: 4
adicionado: 2026-09-02
fonte: enviado pelo hpcarlos
relacionados: [2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md, 2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md]
---

# ChatbotX — plataforma omnichannel de chatbot com IA, self-hosted

## Resumo

Plataforma de marketing conversacional auto-hospedável que cobre WhatsApp, Messenger,
Instagram, Telegram, Zalo e TikTok, mais e-mail (SMTP próprio e integrações) e webchat. Traz
construtor visual de fluxo com mais de 15 tipos de nó, agentes de IA com **chave própria**
(OpenAI, Claude, Gemini, DeepSeek, OpenRouter, NVIDIA NIM ou modelo local), caixa de entrada
com assumir-humano, CRM com segmentação, disparo e sequências, teste A/B, webhooks, times
com papéis — e, o que é raro na categoria, **API pública, CLI e servidor MCP oficiais**.
Monorepo TypeScript com Next.js, PostgreSQL com pgvector, Redis/BullMQ e armazenamento
compatível com S3. Licença dupla: MIT na edição comunidade, comercial no enterprise.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o mais completo dos três construtores de chatbot que chegaram seguidos, e o único
sem intermediário cobrando por mensagem: você traz a chave do provedor de IA e conecta as
plataformas direto. Some-se o servidor MCP, que o torna operável de dentro do agente — algo
que nenhum concorrente comercial da categoria oferece.

## Os três construtores da coleção, lado a lado

| | canais | IA | dependência | licença |
| --- | --- | --- | --- | --- |
| **ChatbotX** | 6 redes + e-mail + web | chave própria (BYOK) | nenhuma obrigatória | MIT + comercial |
| [ZernFlow](2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md) | 7 redes | nó de IA | **API paga da Zernio** | MIT |
| [OpenReply](2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md) | só Instagram | — | nenhuma | MIT |

- **Se quiser amplitude sem laço comercial**, ChatbotX. **Se quiser só comment-to-DM no
  Instagram**, OpenReply resolve com muito menos infraestrutura. O ZernFlow fica no meio,
  com o custo por mensagem da Zernio como pedágio.

## Pontos-chave

- **BYOK é a vantagem estrutural.** Traz a sua chave de LLM e não há taxa de crédito de IA
  por cima — o próprio README aponta isso como diferencial contra ManyChat, Chatfuel, Wati e
  Respond. Combina direto com um gateway como o
  [Portkey](2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md) para
  guardrail e teto de gasto, já que a resposta vai ao cliente.
- **Servidor MCP e CLI oficiais** colocam a plataforma no grupo de coisas que viram
  capacidade do agente — dá para operar campanha e consultar contato de dentro do Claude
  Code, como o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) e o
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  também fazem.
- **⚠️ Licença dupla, e a linha de corte importa.** MIT na edição comunidade, comercial no
  enterprise — o mesmo padrão open core do
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) e do
  [Portkey](2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md).
  Antes de adotar, liste o que você vai usar e cheque de que lado cada recurso está.
- **⚠️ A stack pede DevOps de verdade:** PostgreSQL com pgvector, Redis, armazenamento S3,
  camada de tempo real e filas. É bem mais pesado que o
  [OpenReply](2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md).
  Há um repositório separado de Docker Compose com imagens prontas — comece por ele, não pelo
  código-fonte.
- **As travas das plataformas continuam valendo.** A janela de 24 horas da Meta no WhatsApp e
  no Instagram não some porque o software é bom — é regra de quem opera a rede, e limita
  disparo do mesmo jeito que no ZernFlow e no wacrm.
- **Comunidade modesta**, mas com sinais de projeto sério: monorepo maduro, documentação,
  roadmap público, Discord e tutoriais. Nada de anos de estrada ainda.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **A escolha do construtor, decidida por escopo** — antes de montar qualquer automação de
  conversa, olhar a tabela acima e escolher por dependência, não por número de recursos: se o
  caso é Instagram e nada mais, o OpenReply poupa uma stack inteira; se é operação séria
  multicanal, ChatbotX evita o pedágio do ZernFlow. _Esforço: baixo, e é a decisão que mais
  economiza tempo._
- **Atendimento com IA sob guardrail** — usar o agente de IA do ChatbotX apontado para o
  [Portkey](2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md): o
  gateway controla custo por chave virtual e filtra o que o modelo responde ao cliente. É a
  única forma responsável de deixar LLM falando com público. _Esforço: médio._
- **Operar campanha de dentro do agente** — plugar o servidor MCP dele no Claude Code e pedir
  "quantos contatos entraram pela campanha X esta semana?" sem abrir o painel. Junta-se ao
  [agent-reach](2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md) e
  ao [apify-mcp-server](2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)
  no conjunto de MCPs que dão acesso a dado real. _Esforço: baixo._
- **Sede de operação completa** — com o [Huly](2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)
  no time por dentro e o ChatbotX no cliente por fora, um negócio pequeno roda sem
  mensalidade de SaaS — trocando isso por conta de infraestrutura e trabalho de manutenção,
  que é a conta que precisa fechar. _Esforço: alto._

## Notas

```bash
# caminho recomendado: imagens prontas
# https://github.com/ChatbotXIO/chatbotx-docker-compose

# a partir do código
pnpm dev      # turbo dev
pnpm build
```

- Serviços locais: PostgreSQL (5432), Redis (6379), armazenamento (9000) e MailHog (1025)
  para e-mail em desenvolvimento. Node 24.
- Há ChatbotX Cloud (SaaS pago) como alternativa gerenciada, com promoção de período
  gratuito — útil para avaliar o produto antes de decidir hospedar.
- **Ordem sensata:** avaliar na nuvem deles primeiro (é rápido), decidir se o produto serve, e
  só então encarar a auto-hospedagem — que é onde mora o trabalho.

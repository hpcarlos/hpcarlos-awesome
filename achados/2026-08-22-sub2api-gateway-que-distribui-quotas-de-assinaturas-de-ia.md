---
titulo: "sub2api — gateway que distribui quotas de assinaturas de IA"
nome: sub2api
tldr: "Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso."
licenca: "LGPL-3.0"
alerta: "o próprio README avisa que o uso pode violar os termos dos provedores"
url: https://github.com/Wei-Shaw/sub2api
tipo: projeto
categorias: [ia, devops]
tags: [gateway, go, self-hosted, llm, billing, api]
status: novo
nota: 2
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md, 2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md]
---

# sub2api — gateway que distribui quotas de assinaturas de IA

## Resumo

Plataforma auto-hospedada que pega contas de assinatura de serviços de IA (Claude, OpenAI,
Gemini, Grok) e as revende como chaves de API para vários usuários, com medição por token,
cálculo de custo, limite de concorrência, sessões fixadas por conta e cobrança embutida
(Alipay, WeChat, Stripe). Traz painel administrativo completo. Backend em Go com Gin e
Ent, frontend em Vue 3, PostgreSQL e Redis, licença LGPL-3.0. Apesar do nome, não converte
formato nenhum: é um proxy com autenticação, quota e faturamento na frente de contas
alheias.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Como referência de arquitetura, não como coisa para operar. A parte de medição por token,
faturamento e distribuição de chaves é bem resolvida e é exatamente o pedaço difícil de
qualquer produto que revenda IA — só que aqui está montada sobre uma base que os próprios
autores dizem ser problemática.

## Pontos-chave

- **⚠️ O próprio README avisa que usar o projeto pode violar os termos de serviço da
  Anthropic e dos demais provedores**, e que os autores não respondem por banimento de
  conta, interrupção de serviço ou perda de dados. Também declaram que **nunca autorizaram
  nenhuma operação comercial** baseada no projeto. Isso não é ressalva minha: está escrito
  lá, em destaque.
- **Na prática isso significa:** as contas usadas para servir os usuários finais podem ser
  encerradas sem aviso, e quem estiver cobrando por esse acesso fica sem produto e sem
  recurso. É risco de negócio, não só técnico.
- **Diferença importante para o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md):**
  aquele roteia entre tiers gratuitos que os provedores oferecem publicamente (com uma
  parte marcada como sensível a ToS); este redistribui acesso de assinaturas pagas para
  terceiros, que é o caso mais claramente vedado. Se o objetivo é baratear seu próprio
  uso, o OmniRoute resolve sem entrar nesse terreno.
- **Stack:** Go 1.2x com Gin e Ent, Vue 3 com Vite e Tailwind, PostgreSQL 15+, Redis 7+.
  Instala por script, Docker Compose ou build manual; roda em Linux e macOS.
- **Limitações declaradas:** OAuth da xAI exige reautenticação periódica, mídia no Grok
  depende de direitos pagos, e há timeout configurável de 30s na primeira mensagem via
  WebSocket.
- **Números não verificados** (API do GitHub bloqueada nesta sessão). O README lista
  patrocinadores corporativos, o que sugere projeto de porte, mas não confirmei nada.

## Ideias de projeto

- **Ler só a camada de medição e faturamento** — como contar tokens de forma confiável,
  fechar custo por chave e evitar corrida entre requisições concorrentes é o problema real
  de qualquer SaaS de IA, inclusive um construído sobre o
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md).
  Aqui existe uma implementação inteira para estudar, sem precisar rodar nada.
  _Esforço: baixo._
- **Medidor de consumo para uso próprio** — a mesma ideia de contabilidade por token,
  aplicada só às suas chaves e aos seus projetos, sem revender para ninguém: o problema
  interessante sem o problema jurídico. Combina com o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md),
  que já grava uso em SQLite. _Esforço: médio._
- **Estudo de caso de Go para gateway** — Gin com Ent, controle de concorrência e sessões
  fixadas formam um exemplo realista de serviço em Go sob carga, útil como leitura mesmo
  que o domínio não interesse. _Esforço: baixo._

## Notas

- **Recomendação:** manter em `status: arquivado` como referência técnica. Não use para
  servir terceiros e não construa negócio em cima — o aviso está no próprio repositório.
- Se o que atraiu foi "baratear o acesso a modelo", o caminho sem esse risco é o OmniRoute
  com tiers gratuitos declarados, ou simplesmente pagar a API e medir bem o consumo.
- O script de instalação sugerido pelo README faz `curl … | sudo bash`, o que executa
  código remoto com privilégio de root. Se for testar, leia o script antes e rode em
  máquina descartável.

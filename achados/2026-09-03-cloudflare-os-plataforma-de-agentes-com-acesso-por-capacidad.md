---
titulo: "Cloudflare OS — plataforma de agentes com acesso por capacidade"
nome: cloudflare-os
tldr: "Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita."
licenca: "Apache-2.0"
alerta: "early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare"
url: https://github.com/cloudflare/cloudflare-os
tipo: projeto
categorias: [ia, seguranca]
tags: [agentes, cloudflare, workers, sandbox, typescript, seguranca-de-agentes]
status: novo
nota: 4
adicionado: 2026-09-03
fonte: enviado pelo hpcarlos
relacionados: [2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md, 2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md]
---

# Cloudflare OS — plataforma de agentes com acesso por capacidade

## Resumo

Plataforma que a Cloudflare construiu para uso interno e abriu sob Apache-2.0. Não é sistema
operacional no sentido tradicional: é um ambiente onde as pessoas conversam com agentes que
conhecem o contexto da empresa, constroem pequenas aplicações pessoais ("gadgets") pedindo ao
agente, e compartilham essas aplicações com segurança. Roda sobre Cloudflare Workers e
Durable Objects, com colaboração em tempo real no estilo documento compartilhado, e traz os
*Gatekeepers* — a camada que conecta agentes a serviços externos (GitHub, Google, Slack,
Notion, Supabase, Home Assistant e outros) sob controle.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque tem a resposta mais bem resolvida da coleção para a pergunta que atravessa metade dos
achados: **como deixar um agente agir sem entregar as chaves da casa**. Aqui isso não é
recomendação num README — é a arquitetura do produto.

## Pontos-chave

- **Acesso por capacidade é a ideia central, e é a melhor da coleção nesse tema.** Agentes e
  gadgets **começam sem acesso a nada**: sem rede, sem serviço, sem dado. Cada recurso precisa
  ser apresentado explicitamente. É o oposto do padrão comum — dar tudo e torcer — e resolve
  na arquitetura o que o [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)
  resolve com kill-switch e o [gstack](2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)
  com `/careful`.
- **Sandbox com isolamento de rede por padrão.** Sem consentimento explícito, o código gerado
  pelo agente não fala com a internet. Para quem deixa agente escrever e executar código, essa
  é a diferença entre experimento e incidente.
- **Comparado aos outros quatro ambientes da coleção:** o
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  governa custo e auditoria; o [Rome](2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)
  acumula capacidade; o lobehub é produto acabado; o munder-difflin é experimento visual. Este
  é o único centrado em **segurança e permissão** — e vem de uma empresa cujo negócio é
  justamente infraestrutura segura.
- **⚠️ Amarração à Cloudflare.** Roda sobre Workers e Durable Objects; a promessa de rodar em
  workerd próprio está anunciada como futura. Na prática, adotar é adotar a Cloudflare — e
  isso contraria o espírito auto-hospedável de boa parte da coleção.
- **⚠️ Early access, e eles dizem isso.** O README admite que a versão nova é capaz mas tem
  muitas arestas, e o projeto **não aceita contribuição externa** além de correções triviais.
  É código aberto para ler e usar, não para participar.
- **A ideia dos "gadgets" é boa por si.** Aplicações pequenas e pessoais, criadas por
  conversa, compartilháveis com segurança — resolve o caso do não-programador que precisa de
  uma ferramenta só para si, sem virar projeto de software.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Copiar o modelo de capacidade, não a plataforma** — a regra "o agente começa sem acesso a
  nada e cada recurso é concedido explicitamente" é aplicável a qualquer automação sua, e não
  exige Cloudflare. Junto com o kill-switch do
  [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md) e
  o livro de auditoria, forma o cinto de segurança já registrado no `IDEIAS.md` — agora com um
  terceiro projeto independente chegando à mesma conclusão. _Esforço: médio._
- **Estudar os Gatekeepers como padrão de integração** — a forma como eles embrulham GitHub,
  Google, Slack e afins numa camada de permissão é reaproveitável para quem for expor
  ferramentas a agente via MCP. É o desenho que falta na maioria dos servidores MCP da coleção.
  _Esforço: baixo._
- **Gadgets para uso próprio** — se você já usa Cloudflare, a plataforma resolve de graça o
  problema de "queria uma ferramentinha só minha". Se não usa, o conceito ainda vale como
  inspiração para construir algo equivalente sobre o
  [Rome](2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md) ou sobre um
  runtime próprio. _Esforço: médio._

## Notas

```bash
pnpm run-local        # http://localhost:8787

# desenvolvimento, em dois terminais
pnpm dev-server
pnpm dev-client       # http://localhost:3000
```

- Produção passa pelo fluxo de deploy da própria Cloudflare; há um repositório inicial
  separado para quem quer começar do zero.
- Requer Node com pnpm; as credenciais OAuth dos serviços externos são opcionais e só
  necessárias para os Gatekeepers que você for usar.
- **Ordem sensata:** rodar local para entender o modelo de capacidade, mesmo sem intenção de
  adotar. O aprendizado transferível está aí, não no produto.

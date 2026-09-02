---
titulo: "ZernFlow — construtor visual de chatbots multicanal, alternativa ao ManyChat"
nome: ZernFlow
tldr: "Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat."
licenca: "MIT"
alerta: "depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta"
url: https://github.com/zernio-dev/zernflow
tipo: projeto
categorias: [web, negocios]
tags: [chatbot, automacao, nextjs, supabase, self-hosted, crm]
status: novo
nota: 3
adicionado: 2026-09-02
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md, 2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md]
---

# ZernFlow — construtor visual de chatbots multicanal, alternativa ao ManyChat

## Resumo

Construtor visual de chatbots, de código aberto, que se posiciona como alternativa ao
ManyChat: você monta o fluxo de conversa arrastando nós (são mais de 15 tipos, incluindo um
nó de IA generativa) e ele automatiza o atendimento em sete redes — Instagram, Facebook,
WhatsApp, Telegram, X, Bluesky e Reddit. Traz caixa de entrada com assumir-humano, CRM com
tags, campos e segmentação, disparo em massa, campanhas de gotejamento, teste A/B e
comment-to-DM. Next.js 16 com Supabase e React Flow no editor, licença MIT. O envio de
mensagem passa pela API da Zernio (mesma organização mantenedora).

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a peça de automação de conversa que o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)
não tem: onde aquele foca no atendimento humano por WhatsApp, este monta o fluxo automático
e cobre sete redes de uma vez. Juntos, cobririam a operação de mensagem de um negócio pequeno
de ponta a ponta — se as dependências fecharem.

## Pontos-chave

- **⚠️ A dependência decisiva é a API da Zernio.** O construtor é MIT e você o hospeda, mas o
  envio de mensagem passa por uma API paga da mesma empresa que faz o projeto. Ou seja: o
  código é aberto, a operação não é autônoma. É o mesmo tipo de laço que já apareceu no
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
  (serviços externos pagos) — bom saber antes de contar com "self-hosted grátis".
- **⚠️ WhatsApp tem o limite da Meta, de novo.** O próprio README avisa: a Meta só aceita
  mensagem livre dentro de 24h da última do contato, então auto-resposta funciona, mas
  disparo e passo de sequência atrasado fora dessa janela podem ser recusados — e modelos de
  mensagem aprovados ainda não são suportados. É a mesma trava regulatória do achado do wacrm;
  aqui ela limita justamente o disparo, que é metade do produto.
- **Cobertura de rede é o argumento.** Sete plataformas num construtor só, incluindo Bluesky
  e Reddit, é mais do que a maioria das alternativas abertas cobre. Se o seu público não está
  só no WhatsApp, isso importa.
- **Stack moderna e familiar:** Next.js 16, Supabase, React Flow, Vercel AI SDK — as mesmas
  peças de vários achados da coleção, o que torna o código legível para quem já mexeu nelas.
- **O nó de IA é o toque atual:** dá para pôr um passo de modelo (OpenAI, Anthropic, Google)
  no meio do fluxo. Apontá-lo para um gateway como o
  [Portkey](2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md) ou o
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
  controla custo e, no caso do Portkey, filtra o que a IA responde ao cliente.
- **⚠️ Comunidade pequena.** Poucas centenas de estrelas e um punhado de commits — o site está
  no ar e o projeto parece mantido, mas não é algo com anos de estrada. Trate como promissor,
  não como consolidado.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Operação de mensagem completa para um negócio pequeno** — ZernFlow para o fluxo
  automático e a cobertura multicanal; o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)
  para o atendimento humano aprofundado no WhatsApp. Antes de montar, decidir quem é a fonte
  da verdade do contato, para os dois CRMs não brigarem. _Esforço: alto._
- **Nó de IA barato e seguro** — plugar o nó de IA do ZernFlow num gateway
  ([Portkey](2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md) pelos
  guardrails, já que a resposta vai direto ao cliente): o gateway controla custo e impede que
  o modelo diga o que não deve. É a combinação mais responsável de pôr IA num fluxo de
  atendimento. _Esforço: médio._
- **Avaliar o custo real da Zernio antes de tudo** — como o envio depende da API paga deles,
  a viabilidade é uma conta, não uma dúvida técnica. Mapear o preço por mensagem e comparar
  com mandar direto pela API de cada plataforma decide se o projeto vale. _Esforço: baixo._

## Notas

```bash
git clone https://github.com/zernio-dev/zernflow.git
cd zernflow && npm install
cp .env.example .env      # preencher com Supabase e a chave da Zernio
npm run dev               # http://localhost:3000
```

- Requer Node 18+, um projeto Supabase (o plano gratuito serve) e uma chave da Zernio API
  (obrigatória para mensagens). A chave do gateway de IA é opcional, só para o nó de IA.
- As redes conectam por OAuth, o que traz as travas de termos de uso de cada plataforma —
  não só a da Meta.
- **Ordem sensata:** conferir o preço da Zernio API primeiro; se fechar, subir local e testar
  um fluxo simples numa rede sem janela restrita (Telegram, por exemplo) antes de encarar o
  WhatsApp.

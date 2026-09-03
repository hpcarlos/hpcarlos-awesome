---
titulo: "Spedy — emissão automática de nota fiscal para negócios digitais"
nome: Spedy
tldr: "SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações."
licenca: "própria (SaaS)"
alerta: "serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa"
url: https://spedy.com.br/
tipo: ferramenta
categorias: [negocios, web]
tags: [nota-fiscal, brasil, api, integracao, saas, fiscal]
status: novo
nota: 4
adicionado: 2026-09-03
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md]
---

# Spedy — emissão automática de nota fiscal para negócios digitais

> ⚠️ Não consegui acessar o site (o domínio está bloqueado pelo proxy desta sessão). O
> resumo vem de busca externa e das páginas públicas de ajuda do próprio serviço, não de
> leitura direta — confirme preço e detalhes ao abrir.

## Resumo

Serviço brasileiro que automatiza a emissão de nota fiscal para quem vende online: conecta
à sua plataforma de pagamento, importa as vendas e emite a nota sozinho — NF-e, NFS-e e
NFC-e na mesma plataforma. Tem mais de 70 integrações prontas (Hotmart, Kiwify, Shopify,
Stripe e outras) e **API própria** para quem prefere emitir de dentro do próprio sistema,
com a proposta de "uma requisição, zero manutenção". Voltado a infoprodutores, afiliados,
prestadores de serviço e a quem tem ERP ou SaaS. Preço por nota, sem taxa de adesão na
primeira assinatura.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque preenche a lacuna mais brasileira da coleção. O
[saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
entrega autenticação, times e cobrança via Stripe — e nenhum boilerplate estrangeiro resolve
**nota fiscal brasileira**. Sem isso, um SaaS vendido no Brasil não fecha o ciclo. Esta é a
peça que faltava entre "receber o pagamento" e "estar em dia com o fisco".

## Pontos-chave

- **A API é o que interessa a quem constrói.** As 70 integrações servem a quem vende em
  plataforma pronta; para produto próprio, o caminho é a API — emitir a nota como parte do
  fluxo de checkout, sem processo manual nem planilha no fim do mês.
- **⚠️ É serviço pago, não software.** Diferente de quase tudo nesta coleção, aqui não há
  código para hospedar nem licença aberta: é assinatura com custo por nota emitida. O material
  anuncia valores a partir de centavos por nota e planos mais baratos que a concorrência — mas
  **não confirmei preço** e essa é a primeira coisa a checar.
- **Cobre os três tipos que importam:** NF-e (produto), NFS-e (serviço) e NFC-e (consumidor).
  A NFS-e é a mais chata de resolver sozinho, porque cada município tem o seu padrão — se eles
  abstraem isso bem, é aí que está o valor real do serviço.
- **Dependência de terceiro num ponto sensível.** Emissão fiscal é obrigação legal sua, não
  do fornecedor: se o serviço cair ou encerrar, a obrigação continua. Vale saber como exportar
  o histórico e qual o plano B antes de amarrar o faturamento nisso.
- **Alternativas existem** (outros emissores e gateways fiscais brasileiros); não apurei a
  comparação. Antes de fechar, vale cotar pelo menos dois.
- **Nada verificado além do que a busca trouxe** — o site está bloqueado nesta sessão.

## Ideias de projeto

- **Fechar o ciclo de um micro-SaaS brasileiro** — o
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
  para contas e assinatura, o Stripe para o pagamento e a API da Spedy para a nota. É o
  encanamento completo de um produto vendido no Brasil, e a parte fiscal é justamente a que
  ninguém tem vontade de escrever. _Esforço: médio._
- **Nota fiscal no fluxo de atendimento** — se a venda acontece por WhatsApp com o
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) ou pelo
  [ChatbotX](2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md),
  disparar a emissão pela API ao confirmar o pagamento fecha o ciclo sem ninguém abrir sistema
  nenhum. _Esforço: médio._
- **Cotar antes de integrar** — como o custo é por nota, o volume decide se o serviço faz
  sentido ou se compensa emitir direto pelo emissor gratuito da prefeitura/SEFAZ. Uma planilha
  simples com o seu volume mensal responde isso em meia hora. _Esforço: baixo, e é o primeiro
  passo._

## Notas

- Páginas úteis: a central de ajuda (`ajuda.spedy.com.br`) explica o funcionamento, e há uma
  página específica sobre a API (`materiais.spedy.com.br/api`).
- **Primeiro passo ao abrir:** confirmar preço por nota, se há mínimo mensal, e como se
  exporta o histórico de notas emitidas — os três pontos que decidem a adoção.
- Este é o primeiro achado da coleção de infraestrutura fiscal brasileira. Se o tema render,
  vale catalogar também as alternativas para ter comparação, como foi feito com os gateways
  de IA.

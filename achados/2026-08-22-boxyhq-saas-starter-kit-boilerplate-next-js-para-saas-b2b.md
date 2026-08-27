---
titulo: "BoxyHQ SaaS Starter Kit — boilerplate Next.js para SaaS B2B"
nome: saas-starter-kit
tldr: "Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos."
licenca: "Apache-2.0"
alerta: "webhooks, audit log e cobrança dependem de serviços externos pagos"
url: https://github.com/boxyhq/saas-starter-kit
tipo: projeto
categorias: [web, seguranca]
tags: [nextjs, typescript, saas, prisma, postgres, auth, boilerplate]
status: novo
nota: 4
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md]
---

# BoxyHQ SaaS Starter Kit — boilerplate Next.js para SaaS B2B

## Resumo

Boilerplate open source em Next.js para quem vai construir um SaaS B2B e não quer
reescrever pela enésima vez a mesma base: cadastro e login, magic link, OAuth com Google
e GitHub, SSO via SAML, provisionamento de usuários por SCIM, times com convites e
papéis, audit log, webhooks, headers de segurança, tema escuro e i18n. A aposta do
projeto é justamente o pedaço "enterprise" da autenticação — SAML e SCIM — que costuma
ser o mais chato de fazer à mão e é exatamente o que cliente corporativo exige. Mantido
pela BoxyHQ, sob licença Apache 2.0.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque encurta em semanas o caminho entre uma ideia de produto e algo cobrável. A parte
que ele entrega pronta (times, papéis, convites, SSO, auditoria) é trabalho puro de
encanamento: necessário, demorado e que não diferencia produto nenhum.

## Pontos-chave

- **Licença Apache 2.0** — uso comercial liberado, com atribuição.
- **Stack:** TypeScript, Next.js e React, Tailwind no visual, PostgreSQL com Prisma,
  NextAuth.js na sessão, SAML Jackson no SSO, Playwright nos testes E2E, Docker Compose
  para subir o banco local.
- **⚠️ Várias features dependem de serviço externo de terceiro**, com conta e possível
  custo: Svix (webhooks), Retraced (audit log), Stripe (pagamento), Sentry
  (observabilidade), reCAPTCHA e um SMTP (SES, Sendgrid ou Resend). O kit é grátis; a
  operação dele, não necessariamente. Vale mapear o que dá para trocar por alternativa
  auto-hospedada antes de começar.
- **Requisitos:** Node ≥ 18, PostgreSQL, Docker Compose para o caminho mais curto.
- **Limitações declaradas:** testes E2E só em Chromium e Firefox; testes de unidade e
  integração ainda "em breve".
- **Conferir antes de contar com isso:** o estado real do módulo de cobrança. O material
  cita integração com Stripe, mas também dá a entender que assinaturas ainda não estão
  completas — as duas afirmações não se sustentam juntas, e não consegui resolver a
  contradição sem abrir o código.
- **Números não verificados:** o README indica adoção considerável (milhares de estrelas,
  mais de mil forks). Não confirmei de forma independente — a API do GitHub está
  bloqueada nesta sessão.

## Ideias de projeto

- **Micro-SaaS de IA sem queimar caixa** — o starter kit entrega contas, times e cobrança;
  o [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
  entrega o acesso barato aos modelos por trás. Junta a parte chata (multi-tenant) com a
  parte cara (inferência) e sobra energia para a ideia em si. _Esforço: médio._
- **Tirar a cara de template** — todo produto feito sobre este kit nasce com o mesmo
  visual. Rodar o [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
  (`/impeccable init` para fixar identidade, depois `audit` e `polish`) sobre o Tailwind
  que já vem no projeto resolve isso logo no começo, quando ainda é barato mudar.
  _Esforço: baixo._
- **Ferramenta interna, não SaaS público** — o combo times + papéis + audit log + SCIM é
  exatamente o que um painel interno de empresa precisa e quase nunca tem. Usar o kit
  como base de ferramenta interna aproveita o que ele tem de melhor e dispensa a parte de
  cobrança. _Esforço: médio._
- **Ler o módulo de SSO como material de estudo** — mesmo sem adotar o kit, a
  implementação de SAML e SCIM com o SAML Jackson é uma referência concreta de como se
  faz login corporativo. Ler para aprender é uso legítimo, e barato. _Esforço: baixo._

## Notas

```bash
git clone https://github.com/boxyhq/saas-starter-kit.git
cd saas-starter-kit
npm install
cp .env.example .env          # preencher antes de subir

docker-compose up -d          # PostgreSQL local
npx prisma db push            # cria o schema
npm run dev                   # http://localhost:4002 (conferir no .env.example)

npx prisma studio             # editor visual do banco
npm run playwright:update && npm run test:e2e
```

- Gerar o segredo da sessão: `openssl rand -base64 32` → `NEXTAUTH_SECRET`.
- Variáveis obrigatórias logo de cara: `DATABASE_URL`, `APP_URL`, `NEXTAUTH_SECRET` e
  as de SMTP; as de Svix, Stripe, Sentry e reCAPTCHA só quando for usar cada recurso.
- O `docker-compose` sobe só o banco — a aplicação roda fora, com `npm run dev`.
- A BoxyHQ mantém o SAML Jackson como projeto separado; dá para usar só ele em outro
  stack, sem adotar o starter kit inteiro.

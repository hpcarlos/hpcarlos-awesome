---
titulo: "wacrm — CRM auto-hospedável para WhatsApp"
nome: wacrm
tldr: "CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta."
licenca: "MIT"
alerta: "depende de conta aprovada na WhatsApp Business API, com custo por conversa"
url: https://github.com/ArnasDon/wacrm
tipo: projeto
categorias: [web, negocios]
tags: [whatsapp, crm, nextjs, supabase, self-hosted, typescript, mcp]
status: novo
nota: 3
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md, 2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md, 2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md]
---

# wacrm — CRM auto-hospedável para WhatsApp

## Resumo

CRM feito em volta do WhatsApp e pensado para ser forkado, não assinado: a equipe atende
por uma caixa de entrada compartilhada, os contatos ganham tags e campos próprios, e as
negociações andam num funil kanban. Traz ainda disparos em massa com rastreio de entrega
e leitura, automações montadas em interface visual, assistente de resposta por IA, base
de conhecimento com busca semântica e API REST pública. Conversa com o WhatsApp pela
Meta Cloud API — a via oficial, não gambiarra de navegador. Stack Next.js 16 com React 19
e Tailwind v4, Supabase no lugar de backend próprio, licença MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque no Brasil quase toda venda passa por WhatsApp e quase todo negócio pequeno controla
isso no olho ou numa planilha. Ter uma base MIT que já resolve caixa compartilhada, funil
e disparos transforma "montar um CRM" em "adaptar um CRM" — e o fato de ser template para
fork torna viável entregar isso como serviço para um cliente específico.

## Pontos-chave

- **Licença MIT**, auto-hospedável, explicitamente desenhado como template para fork —
  não é um SaaS multi-inquilino pronto para vender assinatura.
- **Stack:** Next.js 16, React 19, TypeScript, Tailwind v4 e Supabase cuidando de
  PostgreSQL, autenticação, storage e RLS. Tokens sensíveis guardados com AES-256-GCM.
- **Traz um servidor MCP**, ou seja, dá para consultar e operar o CRM de dentro do Claude
  Code ou do Cursor — o que abre uso bem além da tela do CRM.
- **⚠️ A dependência mais pesada não é técnica, é a Meta.** Usar a WhatsApp Business API
  exige conta aprovada, verificação da empresa, mensagens fora da janela de atendimento
  restritas a modelos pré-aprovados e cobrança por conversa. Isso é característica da
  plataforma, não do projeto — mas é o que decide se o disparo em massa que ele oferece é
  utilizável no seu caso. Confira as regras e o preço atuais direto na Meta antes de
  prometer qualquer coisa a cliente.
- **Também depende de:** projeto Supabase configurado (com migração manual) e, para o
  assistente de IA, chave de OpenAI ou Anthropic.
- **O README recomenda um provedor de hospedagem específico** (Hostinger) — cheiro de
  parceria comercial. Não é impedimento; é só ignorar a recomendação e hospedar onde
  preferir.
- **Números não verificados:** os indicadores de adoção do repositório vieram
  inconsistentes na leitura (mais forks do que estrelas, numa proporção estranha) e a API
  do GitHub está bloqueada nesta sessão. Trate a popularidade como desconhecida e avalie
  pelo código.

## Ideias de projeto

- **Trocar o assistente de IA pelo [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)**
  — o wacrm fala com OpenAI/Anthropic, e o OmniRoute expõe justamente um endpoint
  compatível com a OpenAI. Apontar a URL base para `http://localhost:20128/v1` deve
  bastar para o assistente de resposta rodar em modelos de tier gratuito. É a integração
  mais barata entre dois achados deste repositório. _Esforço: baixo._
- **CRM sob medida para um negócio local** — forkar, adaptar campos e funil para uma
  clínica, imobiliária ou barbearia, hospedar e cobrar implantação mais mensalidade de
  manutenção. O template resolve o grosso; o valor está em conhecer o processo do
  cliente. _Esforço: médio._
- **Operar o CRM pelo agente, via MCP** — plugar o servidor MCP dele no Claude Code e
  pedir coisas como "quem parou de responder há mais de uma semana no funil de proposta?".
  Vira relatório sob demanda sem construir tela nenhuma. _Esforço: baixo._
- **Decidir a base antes de escrever a primeira linha** — se a ideia for um produto B2B
  de verdade, comparar este projeto com o
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md):
  o wacrm entrega o domínio (WhatsApp, funil, atendimento) e o outro entrega o
  encanamento corporativo (SSO, SCIM, auditoria, times). Escolher errado custa caro
  depois. _Esforço: baixo (é uma tarde de leitura, não código)._

## Notas

```bash
git clone https://github.com/ArnasDon/wacrm.git
cd wacrm
npm install
cp .env.local.example .env.local   # credenciais do Supabase, Meta e ENCRYPTION_KEY
npm run dev                        # http://localhost:3000
```

- Há instruções de Docker em `docs/docker.md` no próprio repositório.
- API REST pública em `/api/v1` — útil se a ideia for integrar com sistema que o cliente
  já usa, em vez de substituí-lo.
- Documentação hospedada em <https://wacrm.tech/docs> (setup do Supabase, configuração do
  WhatsApp, variáveis de ambiente, arquitetura).
- **Ordem sensata de avaliação:** primeiro confirmar que a conta na Meta é viável para o
  caso de uso, depois olhar o código. O contrário desperdiça o fim de semana.

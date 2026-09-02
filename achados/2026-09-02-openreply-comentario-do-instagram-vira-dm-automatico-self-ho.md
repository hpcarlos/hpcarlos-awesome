---
titulo: "OpenReply — comentário do Instagram vira DM automático, self-hosted"
nome: OpenReply
tldr: "Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta."
licenca: "MIT"
alerta: "só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta"
url: https://github.com/diwenne/openreply
tipo: projeto
categorias: [web, negocios]
tags: [instagram, automacao, nextjs, self-hosted, marketing, dm]
status: novo
nota: 3
adicionado: 2026-09-02
fonte: enviado pelo hpcarlos
relacionados: [2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md, 2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md]
---

# OpenReply — comentário do Instagram vira DM automático, self-hosted

## Resumo

Ferramenta auto-hospedada que faz uma coisa só, e bem: quando alguém comenta uma
palavra-chave num post ou reel do Instagram, ela manda automaticamente um DM para a pessoa —
o clássico "comente LINK que te mando no direct". Traz correspondência de palavra (parcial
ou exata), resposta pública opcional, links rastreáveis com CTR, *follow gate* (exigir
seguir antes de mandar o link), personalização com `{username}`, múltiplas contas e caixa de
entrada. Usa a **Graph API oficial da Meta**, sem scraping nem navegador. Next.js 16 com
PostgreSQL, Prisma e uma fila BullMQ sobre Redis. Licença MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a versão focada e sóbria do que o
[ZernFlow](2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md) faz
como um recurso entre muitos. Onde o ZernFlow é um construtor multicanal amplo (e preso a
uma API paga), este resolve o caso de uso mais popular do Instagram — comment-to-DM — de
forma independente, sobre a API oficial, sem intermediário cobrando por mensagem.

## Pontos-chave

- **A diferença que importa: API oficial, não gambiarra.** Ele roda contra o **seu** app na
  Meta, com a Graph API, sem raspar página nem automatizar navegador. Isso o separa de
  ferramentas de risco de banimento como o
  [camofox-browser](2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md):
  aqui você está dentro das regras da plataforma, não driblando-as. É o jeito certo de
  automatizar Instagram.
- **⚠️ Escopo estreito de propósito.** Só Instagram, só comment-to-DM (mais gatilhos em DM e
  Stories). Se você quer várias redes, é o
  [ZernFlow](2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md); se
  quer atendimento humano no WhatsApp, é o
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md). A virtude do OpenReply é
  fazer uma coisa sem depender de ninguém — a vantagem sobre o ZernFlow é não ter API paga no
  meio.
- **⚠️ Ele envia de verdade, e há limites da Meta.** Não sugere: dispara o DM. O teto é de 750
  DMs por hora por conta (regra da Meta), e as mesmas janelas de mensagem da plataforma se
  aplicam. Automatizar demais ou torto é caminho para restrição de conta — a API ser oficial
  reduz o risco, não o elimina.
- **Setup da Meta é o obstáculo real.** O próprio projeto indica um `setup.md` extenso: criar
  app Meta, conta Instagram Business ou Creator, permissões. O código sobe fácil; a
  papelada da Meta é o que consome o tempo.
- **Operação de dois processos:** o app web e um *worker* separado (a fila que manda os DMs)
  precisam rodar sempre. Não é um binário só — pede um lugar para o worker viver (Railway,
  Oracle Cloud etc.), além do Postgres e do Redis.
- **Nasceu de um fork** de um projeto do Anish Raj, bastante expandido por Diwen Huang.
  Comunidade ainda modesta, mas o foco estreito joga a favor da qualidade.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Isca de captação para um negócio local** — o comment-to-DM é a forma mais barata de
  transformar alcance de post em contato direto. Rodar o OpenReply na conta de um comércio,
  com link rastreável, e medir quantos comentários viram conversa é um experimento de baixo
  custo e resultado observável. Combina com o
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) se a conversa migrar para o
  WhatsApp depois. _Esforço: médio._
- **Escolher entre foco e amplitude** — antes de montar automação de Instagram, comparar
  OpenReply e [ZernFlow](2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)
  numa tarefa real: um resolve comment-to-DM sem API paga e sem mais nada; o outro cobre sete
  redes mas depende da Zernio. A escolha é entre uma peça independente e uma suíte com
  dependência. _Esforço: baixo._
- **Estudar a integração com a Graph API** — mesmo sem usar em produção, o código de um
  projeto que fala com a API oficial do Instagram de forma correta (com fila, teto de taxa,
  webhooks) é boa referência para qualquer integração sua com a Meta. _Esforço: baixo._

## Notas

```bash
git clone https://github.com/diwenne/openreply.git
cd openreply && npm install
cp .env.example .env       # preencher com app Meta e Resend
docker-compose up -d       # Postgres + Redis
npm run db:migrate
npm run dev                # o app web
npm run worker             # em outro terminal: a fila que envia os DMs
```

- Requer conta Meta Developer com app Instagram, conta Instagram Business ou Creator, e uma
  conta Resend para os e-mails de login. Hospedagem sugerida: Vercel para o web, Railway ou
  Oracle Cloud para o worker.
- **Ordem sensata:** vencer o `setup.md` da Meta primeiro — é o gargalo. Só depois vale
  subir a stack e testar um gatilho simples.
- O *follow gate* (exigir seguir antes de liberar o link) é o recurso que mais atrai quem
  usa comment-to-DM para crescer a conta; use com parcimônia, é fácil irritar o público.

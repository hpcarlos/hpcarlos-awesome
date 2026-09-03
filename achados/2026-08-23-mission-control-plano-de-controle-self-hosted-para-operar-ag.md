---
titulo: "mission-control — plano de controle self-hosted para operar agentes de IA"
nome: mission-control
tldr: "Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só."
licenca: "MIT"
alerta: "alpha declarado; troque as credenciais padrão antes de expor na rede"
url: https://github.com/builderz-labs/mission-control
tipo: ferramenta
categorias: [ia, devops]
tags: [agentes, self-hosted, nextjs, sqlite, mcp, observabilidade, typescript]
status: novo
nota: 4
adicionado: 2026-08-23
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md, 2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md, 2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md, 2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md, 2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md, 2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md, 2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md, 2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md]
---

# mission-control — plano de controle self-hosted para operar agentes de IA

## Resumo

Painel auto-hospedado que fica **acima** dos agentes, não no lugar deles: despacha
tarefas, registra agentes e sessões, transmite a atividade ao vivo, acompanha o gasto,
navega pela memória, agenda execução por cron, dispara webhooks, guarda auditoria e
controla acesso por papel. O projeto é explícito sobre a fronteira — não é framework de
raciocínio como CrewAI ou LangGraph, é a camada de operação sobre os runtimes que você já
usa (Claude Code, Codex, CrewAI, LangGraph, AutoGen). Next.js 16 com React 19, SQLite em
modo WAL, e interfaces por REST/OpenAPI, MCP, CLI, WebSocket e SSE. MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque responde à pergunta que ficou pendurada em três achados anteriores: *quanto isso
tudo está custando e o que os agentes andaram fazendo?* O
[munder-difflin](2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)
mostra os agentes como personagens; este aqui mostra como operação — com custo, log e
controle de acesso. É o mesmo tema tratado por adultos.

## Pontos-chave

- **⚠️ Alpha declarado.** O próprio README avisa que APIs, esquemas e configuração podem
  mudar entre versões. Não é base para algo que precise de estabilidade agora.
- **⚠️ Segurança exige leitura antes do uso:** o padrão assume rede confiável e sem TLS
  reverso, e as credenciais geradas na instalação **devem ser trocadas** antes de qualquer
  exposição. Há um `SECURITY-HARDENING.md` e um overlay `docker-compose.hardened.yml` para
  cenários mais sérios.
- **O aviso mais maduro do projeto:** ele instrui a tratar mensagens de agentes, pacotes de
  skills e MCP como **entrada não confiável**. Poucos projetos dessa categoria dizem isso
  em voz alta, e é exatamente a postura correta — vale como princípio, mesmo que você nunca
  instale a ferramenta.
- **Onde ele mesmo diz que não serve:** um único agente numa máquina que você já entende;
  necessidade de SaaS multi-inquilino gerenciado; busca por framework de agentes; ambiente
  que não tolera mudança de esquema. Honestidade rara num README.
- **Stack:** Next.js 16, React 19, TypeScript, Tailwind 4, Zustand, Recharts, xterm.js no
  terminal embutido; Node 22+ com better-sqlite3; pnpm; Docker com imagem publicada no
  GHCR. Testes com Vitest e Playwright, com portão de qualidade no CI.
- **Expõe servidor MCP**, então dá para consultá-lo de dentro do Claude Code — mesmo padrão
  do [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md).
- **Números não verificados** (API do GitHub bloqueada nesta sessão).

## Ideias de projeto

- **Fechar a conta dos agentes** — o mission-control acompanha gasto por execução e o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
  registra uso por provedor em SQLite. Cruzar as duas fontes responde de verdade "quanto
  custou cada projeto, em qual modelo, em que semana" — a pergunta que ficou em aberto
  desde o achado do OmniRoute. _Esforço: médio._
- **Agendar a manutenção deste repositório** — ele tem cron e webhooks; a rotina de revisão
  descrita no `CLAUDE.md` (conferir índices, achar achados parados em `novo`, procurar
  órfãos sem `relacionados`) é exatamente uma tarefa recorrente para despachar por ali.
  Fecha o ciclo: a biblioteca de achados mantida por um dos próprios achados.
  _Esforço: médio._
- **Escolher entre palco e painel** — antes de investir em multiagente, comparar este com o
  [munder-difflin](2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md):
  um entrega visualização e experimentação, o outro entrega governança, custo e auditoria.
  Provavelmente você quer o segundo para trabalhar e o primeiro para brincar — mas vale
  confirmar com uma tarefa real em cada. _Esforço: baixo._
- **Ler o `SECURITY-HARDENING.md` como material de estudo** — a lista do que precisa mudar
  entre "roda na minha máquina" e "roda exposto" é uma boa referência de endurecimento para
  qualquer projeto seu, inclusive os que nasceram do
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md).
  _Esforço: baixo._

## Notas

```bash
git clone https://github.com/builderz-labs/mission-control.git
cd mission-control
bash install.sh --local           # Windows: ./install.ps1 -Mode local
# depois abrir http://localhost:3000/setup para criar o admin

# manual
nvm use 22 && pnpm install && pnpm dev

# docker
docker compose up
docker run --rm -p 3000:3000 ghcr.io/builderz-labs/mission-control:latest

# para algo exposto na rede, use o overlay endurecido
docker compose -f docker-compose.yml -f docker-compose.hardened.yml up -d
```

- **Ordem correta:** ler `SECURITY-HARDENING.md` antes de subir, não depois — as credenciais
  padrão da instalação são o ponto fraco óbvio.
- As issues abertas funcionam como roadmap do projeto, e o autor deixa claro que não promete
  data para o que não está atribuído.
- Mantido por Nyk, da Builderz Labs. Há changelog versionado no repositório.

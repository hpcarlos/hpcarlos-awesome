---
titulo: "OmniRoute — gateway de IA com um endpoint para centenas de provedores"
nome: OmniRoute
tldr: "Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba."
url: https://github.com/diegosouzapw/OmniRoute
tipo: ferramenta
categorias: [ia, devops]
tags: [gateway, llm, self-hosted, claude-code, cli, openai-api]
status: novo
nota: 4
adicionado: 2026-08-21
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md]
---

# OmniRoute — gateway de IA com um endpoint para centenas de provedores

## Resumo

O OmniRoute é um gateway de IA auto-hospedado que sobe em `localhost:20128` e expõe um
único endpoint compatível com a API da OpenAI (`/v1/*`) na frente de centenas de
provedores de modelo. Qualquer ferramenta que fale "OpenAI" passa a alcançar Claude, GPT,
Gemini, DeepSeek, GLM, Kimi e companhia sem trocar de configuração. O ponto central é o
roteamento consciente de cota: quando o tier gratuito de um provedor acaba, ele cai
sozinho para o próximo, e há compressão de contexto para esticar o que resta. Vem com CLI
próprio, painel em Next.js e auditoria local em SQLite. Feito pelo brasileiro Diego
Rodrigues de Sá e Souza, com contribuição de comunidade.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque ataca o custo de usar agentes de código no dia a dia, que é o que limita o uso
contínuo. Combina direto com o [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md):
um baixa o custo por token, o outro melhora o que sai do agente — e os dois plugam nas
mesmas ferramentas.

## Pontos-chave

- **Licença MIT**, auto-hospedado, sem chave de API obrigatória para os provedores de
  tier gratuito. Roda em Linux, macOS, Windows, Raspberry Pi e Android via Termux.
- **Stack:** TypeScript/Node, painel em Next.js, Docker e Electron para empacotamento,
  SQLite para a auditoria local, Redis opcional.
- **Compatível com o que já se usa:** Claude Code, Codex, Cursor, Cline, Copilot,
  OpenCode e outros — basta apontar a ferramenta para `http://localhost:20128/v1`.
- **⚠️ O ponto sensível são os tiers gratuitos.** O próprio README marca 15 provedores
  como *ToS-flagged*, ou seja, o uso automatizado pode contrariar os termos de serviço
  deles — a revisão fica por conta de quem usa. Some-se a isso que cota, elegibilidade e
  modelos mudam sem aviso: o catálogo é re-auditado a cada duas semanas, o que é sinal de
  cuidado do projeto e, ao mesmo tempo, da instabilidade do terreno.
- **Números não verificados:** o README anuncia 340+ provedores, 1200+ modelos, 19
  estratégias de roteamento, ~1,5 bi de tokens grátis/mês e uma contagem alta de estrelas.
  Não consegui confirmar nada disso de forma independente — a API do GitHub está
  bloqueada nesta sessão. Trate como material de divulgação até testar.
- **Alternativas que o próprio projeto cita:** OpenRouter (serviço, não self-hosted),
  LiteLLM (o concorrente mais direto, e mais sóbrio), CLIProxyAPI e 9router.

## Ideias de projeto

- **Bancada barata de frontend** — subir o OmniRoute, rodar `omniroute run claude` com o
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
  instalado e usar a dupla para gerar e polir interfaces: o roteamento cuida do custo, os
  59 detectores cuidam da qualidade. É o par natural dos dois primeiros achados do
  repositório. _Esforço: baixo._
- **Relatório de consumo dos meus agentes** — o gateway já grava uso em SQLite; um script
  que leia esse banco e responda "quanto cada projeto gastou, em qual provedor, em que
  semana" resolve uma pergunta que hoje não tem resposta. _Esforço: médio._
- **Roteamento por tipo de tarefa** — configurar estratégias para mandar trabalho
  mecânico (renomear, formatar, escrever teste óbvio) para modelo de tier gratuito e
  reservar o modelo forte para revisão e design. Medir depois se a qualidade caiu.
  _Esforço: médio._
- **Backend de modelo de um micro-SaaS** — o gateway como camada de inferência de um
  produto construído sobre o [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md): o kit resolve contas, times e
  cobrança; o OmniRoute resolve o custo por token e o fallback quando um provedor cai.
  _Esforço: médio._
- **Assistente do [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) rodando de graça** — o CRM chama OpenAI/Anthropic
  para sugerir respostas; apontar a URL base dele para `http://localhost:20128/v1`
  move esse custo para os tiers gratuitos. _Esforço: baixo._
- **Sentinela de cota** — cron que compara o catálogo de tiers gratuitos entre duas
  auditorias e avisa quando um provedor que você usa muda de regra ou é marcado como
  ToS-flagged. Transforma a maior fragilidade da ferramenta em algo monitorado.
  _Esforço: médio._

## Notas

```bash
# instalar
npm install -g omniroute          # sobe em localhost:20128

# primeiros passos
omniroute setup                   # assistente de configuração
omniroute chat                    # cliente TUI
omniroute configure codex         # aponta uma ferramenta específica para o gateway
omniroute run claude              # inicia o Claude Code através do OmniRoute
omniroute connect 192.168.0.15    # usa uma instância remota
omniroute tokens create --name ci --scope read   # token com escopo restrito

# conferir se está de pé
curl http://localhost:20128/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello!"}]}'
```

- O modelo `auto` escolhe o provedor gratuito sozinho, sem configuração prévia — é o
  caminho mais rápido para testar se vale a pena.
- Também há imagem Docker (`diegosouzapw/omniroute`).
- Comparativo com as alternativas no próprio repositório:
  `docs/comparison/OMNIROUTE_VS_ALTERNATIVES.md` — escrito pelo autor do projeto, então
  vale ler com o desconto de praxe.
- Wiki de arquitetura: <https://github.com/diegosouzapw/OmniRoute/wiki/Architecture>
- **Antes de adotar:** medir latência real contra chamada direta ao provedor, e decidir
  conscientemente quais tiers gratuitos usar.

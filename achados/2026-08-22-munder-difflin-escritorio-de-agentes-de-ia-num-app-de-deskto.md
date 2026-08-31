---
titulo: "munder-difflin — escritório de agentes de IA num app de desktop"
nome: munder-difflin
tldr: "App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art."
licenca: "MIT"
alerta: "protótipo; a arte em pixel tem licença própria com exigência de crédito"
url: https://github.com/chaitanyagiri/munder-difflin
tipo: projeto
categorias: [ia, engenharia]
tags: [agentes, electron, multiagente, claude-code, typescript, cli]
status: novo
nota: 3
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md, 2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md, 2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md]
---

# munder-difflin — escritório de agentes de IA num app de desktop

## Resumo

App de desktop em Electron que coordena vários CLIs de agente — Claude Code, Codex, Grok,
Gemini, Kimi, Qwen, Copilot — como se fossem uma equipe num escritório. Cada agente vira
um avatar em pixel art num piso navegável, com uma camada de memória semântica
compartilhada entre eles, roteamento automático de tarefas por um agente coordenador e um
ambiente de trabalho embutido: editor Monaco, git, kanban de tarefas e integração com
Slack. O nome é piada com *The Office*, e a interface leva a piada a sério. Código MIT,
com a pixel art sob licença separada que exige crédito.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque materializa uma pergunta que quem usa agente todo dia acaba fazendo: e se em vez de
um terminal fossem vários, coordenados, com memória em comum? A resposta aqui é
espalhafatosa, mas as partes sérias — memória compartilhada, roteamento de tarefas,
orquestração de CLIs — são justamente as difíceis.

## Pontos-chave

- **É protótipo funcional, versão 0.4.5** — o próprio projeto se descreve assim. Interessa
  como experimento e como leitura de arquitetura, não como ferramenta para depender.
- **Não substitui os agentes, orquestra os que você já tem:** cada CLI precisa estar
  instalado e no `PATH`, com as respectivas assinaturas ou chaves. O app é a camada de
  cima.
- **Stack:** TypeScript, Electron, React, Pixi.js na renderização do escritório, xterm.js e
  node-pty nos terminais, SQLite na persistência, Monaco no editor.
- **Instalação é de desenvolvedor:** clonar e rodar `npm run dev`, com Node 18+ e
  toolchain C/C++ nativo (no macOS, as Command Line Tools). Não há atalho de instalador.
- **⚠️ Custo:** vários agentes trabalhando em paralelo multiplicam o consumo de tokens. É a
  primeira coisa a controlar antes de deixar rodando.
- **Aceita modelos locais** (Ollama, LM Studio, vLLM) ou chaves próprias — o que é a saída
  natural para o problema de custo acima.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Escritório com custo sob controle** — apontar os agentes do munder-difflin para o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
  em vez de para as APIs pagas diretamente. O gateway já expõe endpoint compatível com a
  OpenAI e faz fallback quando a cota acaba: é exatamente o que uma equipe de agentes
  paralelos consome. _Esforço: médio._
- **Dar método à equipe** — instalar as
  [skills do Matt Pocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
  nos agentes orquestrados, para que triagem, spec e diagnóstico sigam o mesmo processo em
  vez de cada um improvisar. Orquestração sem método comum só multiplica o improviso.
  _Esforço: médio._
- **Roubar só a camada de memória** — a parte realmente reaproveitável é a memória
  semântica compartilhada entre agentes. Estudá-la e extraí-la para uso com um agente só
  já resolve um problema real, sem adotar o app inteiro. _Esforço: alto._
- **Experimento honesto de fim de semana** — rodar uma tarefa média de verdade com dois ou
  três agentes e medir: saiu mais rápido? saiu melhor? quanto custou? Registrar o
  resultado aqui no repositório, com números. Vale mais que qualquer opinião sobre
  multiagente. _Esforço: baixo._

## Notas

```bash
git clone https://github.com/chaitanyagiri/munder-difflin.git
cd munder-difflin
npm install
npm run dev        # app Electron com hot reload
npm run build      # build de produção
npm run typecheck
```

- Requer pelo menos um CLI de agente instalado e disponível no `PATH`.
- A pixel art vem da LimeZu sob licença própria, com obrigação de crédito — atenção se for
  publicar captura de tela ou derivar algo visualmente.
- O coordenador que distribui as tarefas entre os agentes é o pedaço a ler primeiro: é
  onde a ideia toda se sustenta ou desaba.

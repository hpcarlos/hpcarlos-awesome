---
titulo: "Rome — o SO agêntico que persiste software, não só conversa"
nome: Rome
tldr: "Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto."
licenca: "MIT"
alerta: "preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada"
url: https://github.com/rome-os/rome
tipo: projeto
categorias: [ia, engenharia]
tags: [agentes, self-hosted, mcp, typescript, orquestracao, skills]
status: novo
nota: 3
adicionado: 2026-08-31
fonte: enviado pelo hpcarlos
relacionados: [2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md, 2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md]
---

# Rome — o SO agêntico que persiste software, não só conversa

## Resumo

Ambiente de operação para agentes que se descreve como "o SO agêntico para humanos e
agentes". A aposta que o separa dos vizinhos: em vez de guardar só o histórico de conversa,
ele persiste **software executável** — apps com interface própria para tarefas repetidas,
ações tipadas reutilizáveis, skills em linguagem natural carregadas sob demanda e agentes
com instruções próprias. A ideia é que a capacidade construída numa tarefa fique disponível
para as seguintes, descobrível e reaproveitável, em bancos privados por app. Monorepo
TypeScript, roda por Docker, com painel web e app Electron, e canais de chat (Telegram,
Discord, WhatsApp) como interface. Licença MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o quarto ambiente de operação de agentes da coleção, e o primeiro com uma tese
realmente diferente. Onde os outros orquestram, ele **acumula**: a promessa é que o trabalho
do agente não evapore no fim da sessão, mas vire ferramenta permanente. Se entregar isso, é
uma diferença de categoria, não de acabamento.

## Pontos-chave

- **A tese é "persistir software, não texto", e é o ponto inteiro.** O próprio projeto se
  contrasta com harnesses que guardam só conversa e scripts: aqui, o que o agente constrói
  vira app composável, com dados e interface próprios. É a resposta ao problema que o
  [task-observer](2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)
  ataca por outro lado — a skill que congela — só que resolvido na infraestrutura, não na
  observação.
- **Comparado aos três ambientes que você já tem:** o
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  é governança e custo; o [lobehub](2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)
  é produto acabado com licença restritiva; o
  [munder-difflin](2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)
  é experimento visual. O Rome é o único que aposta em acúmulo de capacidade, e é MIT — o
  que o torna o mais interessante de acompanhar dos quatro.
- **⚠️ É preview em evolução ativa.** Poucas centenas de estrelas, pouco mais de cem commits,
  e uma nuvem própria (Rome Cloud) ainda fechada. A ideia é ambiciosa; a maturidade, não. Não
  é base para nada sério hoje — é para experimentar e observar.
- **⚠️ Exige Docker e não tem distribuição simples** além da nuvem que ainda não abriu. Some-se
  a isso o Node 24 e o monorepo pnpm: a instalação é de desenvolvedor, não de clicar e usar.
- **Agnóstico a modelo**, o que o coloca bem para rodar sobre um gateway como o
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) e
  controlar custo — relevante num ambiente que se propõe a rodar agentes o tempo todo.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Testar a promessa central, não a interface** — a pergunta que decide o Rome é uma só:
  uma capacidade construída numa tarefa é mesmo reaproveitada, sem retrabalho, na próxima?
  Montar um caso pequeno (um app que resume um tipo de página) e ver se ele reaparece
  utilizável depois é o experimento que vale. O resto é acabamento. _Esforço: médio._
- **Comparar as quatro filosofias com uma tarefa só** — rodar a mesma tarefa de agente no
  Rome, no mission-control e no munder-difflin e anotar o que cada um preserva no fim. É a
  forma de entender, com evidência, a diferença entre orquestrar, governar e acumular.
  _Esforço: alto._
- **Roubar a ideia sem adotar a plataforma** — mesmo que o Rome não vingue, o conceito de
  "toda tarefa deixa uma ferramenta para trás" é aplicável ao seu próprio fluxo: fazer o
  agente, ao terminar, salvar o script que usou como comando reutilizável. Este repositório
  já faz isso à mão com o `CLAUDE.md`; a lição do Rome é torná-lo automático. _Esforço: médio._

## Notas

```bash
# docker (caminho mais curto)
curl -fsSL https://raw.githubusercontent.com/rome-os/rome/main/scripts/quickstart-docker.sh | bash
# painel em http://localhost:7663

# desenvolvimento
corepack enable && pnpm install && pnpm dev:all
```

- O script de instalação é `curl | bash` — leia antes de rodar e use máquina descartável,
  como sempre com esse padrão.
- Requer Node 24+, Corepack e Docker.
- Estrutura: `packages/core/` (runtime), `rome_apps/` (apps de primeira parte), `docs/`
  (design e arquitetura). Os docs de arquitetura são a melhor porta de entrada para julgar
  se a tese se sustenta.
- **Antes de investir tempo:** ler a arquitetura, não rodar. A dúvida sobre o Rome é
  conceitual (a persistência de software funciona?), e isso o texto responde mais rápido que
  a instalação.

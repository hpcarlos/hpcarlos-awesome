Ideias a partir das aplicações de LLM
===

Projetos que dá para construir com as 115 aplicações catalogadas em
[`LLM-APPS.md`](LLM-APPS.md) — sozinhas, combinadas entre si, ou cruzadas com os achados da
lista principal ([`README.md`](README.md)).

O valor daquele repositório não é ter 115 aplicações: é ter **um exemplo funcionando para
quase toda ideia que você teria**. O trabalho aqui é escolher quais valem virar coisa sua.

> As ideias que combinam achados da lista principal entre si continuam em
> [`IDEIAS.md`](IDEIAS.md). Aqui ficam as que dependem de pelo menos uma aplicação daquele
> repositório.

## Fechar o ciclo deste repositório

### Vigia dos achados

O [Release Radar Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/always_on_agents/release_radar_agent)
monitora lançamentos de projetos e avisa o que mudou. Apontá-lo para os projetos já
catalogados em `achados/` resolve, de graça, a manutenção periódica que o
[`CLAUDE.md`](CLAUDE.md) prevê e que ninguém faz na mão: saber quando o OmniRoute mudou de
licença, quando o mission-control saiu do alpha, quando o graphify lançou a v1.

- **Alimenta:** Release Radar Agent + os 22 achados da lista principal
- **Esforço:** médio
- **Primeiro passo:** extrair as URLs de `achados/*.md` (o `lib_achados.py` já entrega
  `a.url` pronto) e alimentar o agente com essa lista.
- **Fecha um problema real:** metade dos achados tem "números não verificados" ou uma
  pendência anotada. Um vigia resolve isso continuamente, em vez de por lembrança.

### Caixa de entrada que se alimenta sozinha

O [Always-on Hacker News Briefing Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/always_on_agents/always_on_hn_briefing_agent)
já faz o trabalho de acompanhar e resumir. Fazer ele escrever direto no `INBOX.md`, com
uma linha por link e o motivo do interesse, transforma este repositório numa esteira: ele
sugere, você aprova, o fluxo normal processa.

- **Alimenta:** Always-on HN Briefing Agent + `INBOX.md`
- **Esforço:** médio
- **A fonte de leitura:** o [agent-reach](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)
  dá ao agente o acesso a HN, Reddit e YouTube sem taxa de API — use só as plataformas sem
  login (web, RSS, YouTube, GitHub) e não há risco de conta.
- **Cuidado:** filtro apertado. Uma inbox com trinta links por dia é pior que uma vazia — o
  gargalo aqui é a sua atenção, não a coleta.

### Conversar com a própria biblioteca

[Chat with GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_github)
e [AI Blog Search](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/ai_blog_search)
são o mesmo problema desta coleção: buscar em texto próprio. Hoje o `buscar.py` faz busca
literal; um RAG por cima dos achados responderia "qual ferramenta serve para controlar
custo de agente?" sem você lembrar do nome dela.

- **Alimenta:** Chat with GitHub / AI Blog Search + `achados/`
- **Esforço:** baixo
- **Primeiro passo:** apontar o AI Blog Search para a pasta `achados/` — o formato é o
  mesmo, Markdown com front-matter.
- **Melhor ainda:** com o [graphify](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md),
  vira grafo em vez de busca vetorial, e as relações `relacionados:` entram como arestas.

## Escolher no meio da abundância

### Trilha de RAG, em vez de ler os 21

São 21 variantes de RAG, o que é ótimo e paralisante. A ordem que ensina mais rápido:

1. [Basic RAG Chain](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_chain) — a cadeia mínima, para ver as peças.
2. [Corrective RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/corrective_rag) — o que fazer quando a recuperação vem ruim.
3. [Agentic RAG with Reasoning](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/agentic_rag_with_reasoning) — decidir o que buscar antes de buscar.
4. [Knowledge Graph RAG with Citations](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/knowledge_graph_rag_citations) — resposta com fonte rastreável.

E, quando algo der errado, o [RAG Failure Diagnostics Clinic](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_failure_diagnostics_clinic)
é o único da lista que ensina a **depurar** RAG em vez de construir mais um.

- **Esforço:** médio (uma tarde por etapa)
- **Por que nesta ordem:** cada passo resolve um defeito do anterior. Ler fora de ordem é
  colecionar variação sem entender o problema que ela ataca.

### Skills que as suas coleções não têm

Os seis [agent skills](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills)
daquele repositório não se sobrepõem às do
[mattpocock](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
nem às do [addyosmani](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md):
**Commit Archaeologist** (por que o código ficou assim), **Dependency Doctor** (o que está
podre nas dependências), **Scope Creep Detector** (o escopo está inchando) e **Project
Graveyard** (por que aquilo morreu) cobrem buracos que as duas coleções deixam.

- **Alimenta:** agent_skills + as duas coleções de skills
- **Esforço:** baixo
- **Primeiro passo:** ler o `SKILL.md` das quatro e instalar só as que resolvem um problema
  que você teve este mês.
- **Ligação:** o Scope Creep Detector é o irmão do
  [ponytail](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md) —
  um vigia o tamanho da tarefa, o outro o tamanho do código.

## Combinações com a lista principal

### Três alavancas de custo, em camadas diferentes

Ninguém junta as quatro, e elas se multiplicam:

| camada | ferramenta | o que reduz |
| --- | --- | --- |
| código gerado | [ponytail](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md) | quanto o agente escreve |
| contexto | [Headroom Context Optimization](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_optimization_tools/headroom_context_optimization) | quanto entra na janela |
| tokens por chamada | [Toonify](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_optimization_tools/toonify_token_optimization) | o tamanho do que é enviado |
| preço por token | [bifrost](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) | quanto custa cada um |

- **Esforço:** médio
- **Primeiro passo:** medir o gasto atual de um projeto seu antes de mexer em qualquer
  camada. Sem linha de base, otimização vira fé.

### Time de agentes com o cinto de segurança

Nenhum dos treze [times de agentes](LLM-APPS.md#-times-de-agentes) tem contenção: eles
demonstram colaboração, não governança. O
[Trust-Gated Multi-Agent Research Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/trust_gated_agent_team)
é a exceção e o ponto de partida — combinado com o desenho do
[Vibe-Trading](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)
(kill-switch, teto de ação, livro encadeado) e a operação do
[mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md).

- **Esforço:** médio
- **Onde isso importa de verdade:** qualquer time que escreva em sistema real. Enquanto o
  time só pesquisa e resume, o risco é baixo; no primeiro que manda e-mail ou altera banco,
  vira requisito.

### Atendimento por voz sobre o CRM

O [Voice RAG Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/voice_rag_openaisdk)
e o [Customer Support Voice Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/customer_support_voice_agent)
resolvem a metade que falta no
[wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md): ele já tem base de
conhecimento com busca semântica e caixa de entrada; falta a voz.

- **Esforço:** médio
- **Antes de tudo:** as regras da Meta sobre mensagem de voz e janela de atendimento — o
  mesmo alerta do achado do wacrm. A viabilidade é regulatória, não técnica.

### Mais um caminho para a vitrine

O [Generative UI Starter Project](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/generative-ui-starter-project)
e o [AI Dashboard Canvas Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-dashboard-canvas-agent)
são uma alternativa ao [OpenDesign](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)
para a vitrine web desta coleção — com uma diferença: aqui a interface é **gerada em tempo
de execução** a partir dos dados, em vez de gerada uma vez e versionada.

- **Esforço:** médio
- **Qual escolher:** OpenDesign se você quer um site estável e versionado; interface
  generativa se quer que ela se reorganize conforme a coleção cresce.

## Para começar hoje

Se for testar uma única coisa desta lista, que seja o **Vigia dos achados**: é o que
transforma esta biblioteca de um arquivo em algo que se mantém sozinho — e usa uma
aplicação pronta, sem código novo.

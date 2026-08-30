---
titulo: "awesome-llm-apps — 115 aplicações de LLM com código completo"
nome: awesome-llm-apps
tldr: "115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0."
licenca: "Apache-2.0"
alerta: "são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção"
url: https://github.com/Shubhamsaboo/awesome-llm-apps
tipo: projeto
categorias: [ia, engenharia]
tags: [rag, agentes, exemplos, python, mcp, llm, voz]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md, 2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md, 2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md, 2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md]
---

# awesome-llm-apps — 115 aplicações de LLM com código completo

## Resumo

Repositório com 115 aplicações de LLM funcionando de ponta a ponta, organizadas em quinze
categorias: skills de agente, agentes simples e avançados, times de agentes, agentes
sempre ativos, voz, interfaces geradas em tempo de execução, agentes que jogam, integrações
MCP, vinte e uma variantes de RAG, aplicações com memória, "conversar com" (PDF, GitHub,
Gmail, YouTube, arXiv, Substack), otimização de contexto e token, ajuste fino de modelo e
cursos rápidos de framework. Tudo sob Apache-2.0, no mesmo repositório, com modelos
variados — Claude, GPT, Gemini, DeepSeek, Llama, Qwen — e boa parte com opção de rodar
local.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque muda a pergunta. Até aqui a coleção respondia "com que ferramenta eu construo?";
esta responde "como é que isso fica pronto?" — para quase qualquer ideia, já existe ali um
exemplo funcionando que serve de ponto de partida ou de contraprova.

## Pontos-chave

- **⚠️ São demonstrações, não produtos.** Dependem de chave de API, não trazem controle de
  gasto, contenção de ação nem tratamento de erro de produção. Servem para aprender o
  formato e roubar a estrutura — não para colocar na frente de cliente como estão. O
  contraste com o desenho de contenção do
  [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)
  é gritante, e é justamente aí que mora o trabalho de quem for adaptar.
- **Vinte e uma variantes de RAG** é o acervo mais valioso do repositório: da cadeia mínima
  ao grafo de conhecimento com citação, passando por RAG corretivo, híbrido, multimodal e
  tipado. Inclui um exemplo dedicado a **diagnosticar RAG quebrado**, que é raro.
- **Seis skills de agente que não existem nas coleções que você já tem** — Commit
  Archaeologist, Dependency Doctor, Scope Creep Detector e Project Graveyard cobrem buracos
  do [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
  e do [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md).
- **Dois agentes sempre ativos** (briefing de Hacker News e radar de lançamentos) são os
  mais aplicáveis a este repositório: dá para usá-los para alimentar a `INBOX.md` e para
  vigiar mudanças nos projetos já catalogados.
- **Duas ferramentas de otimização** — de contexto e de token — que se somam ao
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) e ao
  [ponytail](2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md) em camadas
  diferentes da mesma conta.
- **A abundância é o problema, não a solução.** Com 115 opções, o custo passa a ser
  escolher. Por isso o catálogo em [`LLM-APPS.md`](../LLM-APPS.md) e as trilhas em
  [`IDEIAS-LLM-APPS.md`](../IDEIAS-LLM-APPS.md).
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

As ideias deste achado ficam em arquivo próprio, por serem muitas:
**[`IDEIAS-LLM-APPS.md`](../IDEIAS-LLM-APPS.md)**. As três que valem começar por:

- **Vigia dos achados** — apontar o Release Radar Agent para as URLs dos achados deste
  repositório, para saber quando um projeto catalogado muda de licença, sai do alpha ou é
  arquivado. Resolve a manutenção periódica que o `CLAUDE.md` prevê. _Esforço: médio._
- **Trilha de RAG em quatro etapas** — cadeia mínima, corretivo, com raciocínio e com
  citação, nessa ordem: cada um resolve um defeito do anterior. É a forma mais rápida de
  entender RAG de verdade em vez de colecionar variantes. _Esforço: médio._
- **Conversar com a própria biblioteca** — apontar o AI Blog Search para `achados/` e
  responder "qual ferramenta serve para X?" sem precisar lembrar do nome. O formato já é
  Markdown com front-matter. _Esforço: baixo._

## Notas

- Catálogo completo em português, com link direto para cada pasta:
  [`LLM-APPS.md`](../LLM-APPS.md) — gerado por `scripts/indexar_llm_apps.py` a partir de
  `dados/llm-apps.tsv`.
- As descrições daquele catálogo vêm do nome e da categoria de cada aplicação, **não de
  leitura do código de cada pasta** — é mapa de navegação, não avaliação individual.
- Um item da lista de origem (Openwork) aponta para repositório externo; está marcado como
  tal no catálogo.
- **Ordem sugerida de uso:** achar no catálogo o exemplo mais próximo da sua ideia, rodar
  como está para ver funcionando, e só então decidir o que aproveitar.

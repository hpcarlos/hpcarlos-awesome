---
titulo: "graphify — transforma um repositório em grafo de conhecimento consultável"
nome: graphify
tldr: "Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual."
licenca: "Apache-2.0 e MIT"
alerta: "a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela"
url: https://github.com/Graphify-Labs/graphify
tipo: ferramenta
categorias: [ia, engenharia]
tags: [grafos, ast, tree-sitter, python, mcp, claude-code, skills]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md]
---

# graphify — transforma um repositório em grafo de conhecimento consultável

## Resumo

Ferramenta que pega um repositório inteiro — código, documentação, PDFs, esquemas SQL,
imagens, áudio e vídeo — e monta um grafo de conhecimento que se pode consultar em
linguagem natural: *"o que liga a autenticação ao banco?"*, o caminho mais curto entre duas
classes, a explicação de um conceito. O código é lido por AST determinístico com
tree-sitter em cerca de 40 linguagens, **sem LLM e sem sair da máquina**; o modelo entra só
para o material textual. Cada aresta é marcada como extraída (explícita no código) ou
inferida, agrupa subsistemas por detecção de comunidade e devolve três arquivos: um grafo
interativo em HTML, um relatório de arquitetura em Markdown e o grafo em JSON. Instala-se
como skill de agente e pode se expor como servidor MCP. Python 3.10+, sob Apache-2.0 e MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque resolve o problema que aparece toda vez que se chega num código alheio — e a coleção
está cheia deles. Antes de adotar o [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
ou o [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md),
a pergunta não é "quantas estrelas tem", é "como isso está organizado por dentro". Este
responde com um mapa, não com opinião.

## Pontos-chave

- **A distinção entre aresta extraída e inferida é o detalhe que importa.** Saber o que o
  parser viu no código e o que foi deduzido é a diferença entre mapa confiável e ilustração
  bonita. Poucas ferramentas do gênero fazem essa separação explícita.
- **Código não precisa de LLM nem de rede:** `graphify extract ./src --code-only` roda
  local e determinístico. Chave de API só é necessária para documento, PDF e mídia — e há
  suporte a Ollama para manter tudo em casa. Bom desenho de privacidade e de custo.
- **Não é índice vetorial**, e o projeto faz questão de dizer isso: é grafo com relações
  nomeadas, comparado no README a mem0 e supermemory com benchmarks favoráveis a si próprio
  — números do autor, portanto, a medir antes de repetir.
- **Vira memória estruturada do agente** através do servidor MCP, o que é bem diferente de
  jogar o código num RAG e torcer.
- **Gancho de git que reconstrói o grafo** a cada commit ou troca de branch: documentação de
  arquitetura que não envelhece, que é o problema de toda documentação de arquitetura.
- **⚠️ A v1 pública ainda não saiu** — o desenvolvimento corre num branch `v8`, e existe
  plataforma comercial paralela com aceleradora por trás. Provável modelo open core: vale
  observar o que fica aberto antes de construir algo que dependa disso.
- **⚠️ Custo:** corpora densos de documentação saem caros no LLM. Há `--token-budget` e
  backends locais para conter — e é caso de uso direto para o
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md),
  com cache semântico.
- **Grafo acima de ~5000 nós fica lento no navegador**; use `--no-viz` e consuma o JSON.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Mapear os candidatos a base, junto com o [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)**
  — um mede a saúde do código, o outro desenha a arquitetura. Rodar os dois no
  saas-starter-kit, no wacrm e no mission-control responde de uma vez "qual é a mais sadia"
  e "qual eu consigo entender". É a auditoria que já está no `IDEIAS.md`, agora com as duas
  metades. _Esforço: baixo._
- **Memória de código do agente via MCP** — expor o grafo de um projeto seu como servidor
  MCP e deixar o agente consultar relações em vez de reler arquivo. Ataca direto o custo de
  contexto, que é o gasto invisível de trabalhar com agente. _Esforço: médio._
- **Documentação de arquitetura que se mantém sozinha** — instalar o gancho de git e
  versionar o `GRAPH_REPORT.md` gerado. Toda equipe quer um documento desses e ninguém
  atualiza; aqui ele se refaz a cada commit. _Esforço: baixo._
- **Grafo do próprio repositório de achados** — os `relacionados:` do front-matter já
  formam um grafo à mão, hoje mantido por mim a cada achado novo. Comparar esse grafo com
  o que o graphify extrai do conteúdo mostraria conexões que passaram despercebidas.
  _Esforço: médio._

## Notas

```bash
uv tool install graphifyy          # ou pipx install graphifyy
graphify install                   # registra como skill do agente
/graphify .                        # dentro do Claude Code, Cursor etc.

graphify extract ./src --code-only          # local, determinístico, sem API
graphify extract ./docs --backend gemini    # docs e PDFs, com LLM
graphify query "o que conecta autenticação ao banco de dados?"
graphify path "UserService" "DatabasePool"
graphify hook install                       # reconstrói a cada commit
```

- Saída em `graphify-out/`: `graph.html`, `GRAPH_REPORT.md` e `graph.json`.
- O relatório aponta *god nodes* e "conexões surpreendentes" — é por onde começar a ler.
- Exporta para Neo4j, FalkorDB, GraphML, Obsidian, wiki em Markdown e Mermaid.
- O registro de consultas (`~/.cache/graphify-queries.log`) vem **desligado** por padrão —
  ao contrário dos últimos achados, aqui o comportamento padrão é o discreto.
- Vídeo e áudio exigem o extra: `uv tool install graphifyy[video]`.

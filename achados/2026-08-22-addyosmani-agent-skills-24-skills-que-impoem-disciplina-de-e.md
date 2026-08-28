---
titulo: "addyosmani/agent-skills — 24 skills que impõem disciplina de engenharia ao agente"
nome: addyosmani/agent-skills
tldr: "24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias."
licenca: "MIT"
alerta: "instalar skill avulsa não traz as checklists de `references/`"
url: https://github.com/addyosmani/agent-skills
tipo: ferramenta
categorias: [ia, engenharia]
tags: [claude-code, skills, agentes, workflow, tdd, code-review, performance]
status: novo
nota: 5
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md, 2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md, 2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md, 2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md, 2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md, 2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md, 2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md, 2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md]
---

# addyosmani/agent-skills — 24 skills que impõem disciplina de engenharia ao agente

## Resumo

Sistema de 24 skills, do Addy Osmani, que organiza o trabalho do agente nas seis fases do
ciclo de desenvolvimento: definir (`interview-me`, `idea-refine`,
`spec-driven-development`), planejar, construir (TDD, implementação incremental,
engenharia de contexto), verificar (teste no navegador via DevTools, depuração), revisar
(qualidade, simplificação, segurança OWASP, performance) e publicar (git, CI/CD,
observabilidade, ADRs, checklist de lançamento). São 8 comandos que mapeiam essas fases —
`/spec`, `/plan`, `/build`, `/test`, `/review`, `/webperf`, `/code-simplify`, `/ship` —
mais quatro personas de revisão e sete checklists de referência. Licença MIT, com
instalação em Claude Code, Cursor, Codex, Gemini CLI e outros.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a contraparte sistêmica do
[mattpocock/skills](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md),
que chegou aqui na mesma leva. Ter os dois no repositório permite a comparação honesta em
vez da escolha por autoridade — e o próprio Addy publica um comparativo em
`docs/comparison.md`, então nem ele finge que a escolha é óbvia.

## Pontos-chave

- **Três ideias estruturais que valem além da ferramenta:**
  1. *Processo, não prosa* — as skills são roteiros que o agente executa, não documentos
     que ele lê.
  2. *Antirracionalização* — cada skill traz uma tabela das desculpas mais comuns ("depois
     eu escrevo o teste") com o contra-argumento pronto. É uma solução direta para o modo
     como um agente negocia consigo mesmo.
  3. *Verificação inegociável* — toda skill termina exigindo evidência de que funcionou.
- **Bagagem declarada:** práticas de engenharia do Google (*Software Engineering at
  Google*), Lei de Hyrum, regra da Beyoncé, pirâmide de testes 80/15/5, cerca de
  Chesterton, trunk-based, feature flags. É opinativo e assume esse viés.
- **`/build auto`** planeja e implementa a lista inteira numa passada só, mantendo a
  verificação entre tarefas — o modo mais arriscado e o mais interessante de testar.
- **⚠️ Pegadinha real:** instalar uma skill isolada via `npx skills add … --skill X`
  **não traz o diretório `references/`**, ou seja, as checklists compartilhadas ficam de
  fora e a skill roda pela metade. A saída é instalar o repositório inteiro ou copiar as
  checklists à mão (rastreado na issue #361 do projeto).
- **Se não tiver chave SSH no GitHub**, force HTTPS ao adicionar o marketplace — é o erro
  de instalação mais comum descrito no README.
- **As sete checklists** (definition of done, testes, segurança, performance,
  acessibilidade, observabilidade, orquestração) têm valor sozinhas, mesmo para quem
  nunca instalar as skills.
- **Números não verificados:** a leitura devolveu contagem de estrelas na casa das dezenas
  de milhares. Plausível para o autor, mas não confirmei — a API do GitHub está bloqueada
  nesta sessão.

## Ideias de projeto

- **Bake-off entre as duas coleções** — pegar uma tarefa média de verdade e executá-la
  duas vezes: uma com `/spec → /plan → /build → /review` daqui, outra com `to-spec`,
  `to-tickets`, `implement` e `grill-me` do
  [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md).
  Anotar tempo, retrabalho, tokens e qualidade percebida, e virar um achado deste
  repositório. Você é a única pessoa que pode responder qual serve para o **seu** jeito de
  trabalhar. _Esforço: médio._
- **Usar as checklists sem adotar nada** — `security-checklist.md`,
  `accessibility-checklist.md` e `definition-of-done.md` funcionam como documento de
  equipe puro, revisados uma vez e colados no seu repositório. Retorno imediato, custo
  quase zero. _Esforço: baixo._
- **`frontend-ui-engineering` + [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)**
  — um cuida da arquitetura de componentes, acessibilidade e design system; o outro, de o
  resultado não ter cara de template. Os dois juntos cobrem frontend do esqueleto à pele.
  _Esforço: baixo._
- **`/spec` sobre o `IDEIAS.md` deste repositório** — as ideias acumuladas aqui são
  parágrafos; passá-las por `/spec` e `/plan` as transforma em tarefas verificáveis. É o
  mesmo destino apontado no achado do mattpocock, e serve para comparar as duas
  abordagens no mesmo material. _Esforço: baixo._

## Notas

```bash
# CLI universal (funciona na maioria dos agentes)
npx skills add addyosmani/agent-skills            # todas as 24
npx skills add addyosmani/agent-skills --list     # ver antes de instalar

# Claude Code, via marketplace
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# se der erro de SSH, force HTTPS:
/plugin marketplace add https://github.com/addyosmani/agent-skills.git
```

- Comparativo com alternativas (Superpowers e as skills do Matt Pocock) no próprio
  repositório: `docs/comparison.md` — escrito pelo autor de um dos lados, então leia com o
  desconto de praxe.
- Site do projeto: <https://skills.addy.ie>
- Há guia de adoção separando projeto novo de adoção gradual em base existente — comece
  por ele se for aplicar em código legado.
- `using-agent-skills` é a skill que ensina qual skill usar; equivale ao `ask-matt` da
  outra coleção.

---
titulo: "impeccable — design language e skill para agentes de código"
nome: impeccable
tldr: "Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais."
url: https://github.com/pbakaus/impeccable
tipo: ferramenta
categorias: [ia, design]
tags: [frontend, ui, claude-code, cli, skills, linter]
status: novo
nota: 4
adicionado: 2026-08-21
fonte: enviado pelo hpcarlos
relacionados: []
---

# impeccable — design language e skill para agentes de código

## Resumo

O impeccable é uma *design language* empacotada como skill para agentes de código: ele
ensina o agente a produzir interfaces com aparência decidida em vez do visual genérico
que os LLMs entregam por padrão. Traz 23 comandos sob `/impeccable` (`audit`, `polish`,
`critique`, `distill`, `animate`, `bolder`, `quieter`, entre outros) e 59 regras
determinísticas que detectam anti-padrões — o autor chama isso de "AI slop": Inter em
tudo, gradiente roxo-azul, easing bounce, glow em tema escuro, borda em aba lateral.
Cobre o ciclo inteiro: `shape` para planejar, `craft` para construir e `polish` para
refinar. Criado por Paul Bakaus, como evolução do projeto `frontend-design` da Anthropic.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque resolve o ponto fraco mais visível de gerar UI com agente: o código funciona, mas
tudo sai com a mesma cara. É o tipo de ferramenta que se instala uma vez e melhora todo
projeto frontend feito com Claude Code daqui pra frente — e, de quebra, o detector roda
sozinho no CI, sem depender de IA nenhuma.

## Pontos-chave

- **Licença Apache 2.0** — permite uso comercial, exige atribuição.
- **Instalação em um comando:** `npx impeccable install`. Detecta as pastas de harness
  presentes (`.claude`, `.codex`, `.grok`…), aceita `--providers=` e
  `--scope=project|global`, e registra os hooks nativos. Também dá para instalar via
  submódulo git, marketplace de plugins ou cópia manual.
- **O detector funciona sem IA e sem harness:** `npx impeccable detect src/` roda as 59
  regras localmente e tem saída `--json` — é isso que o torna plugável em CI.
- **Suporte largo de ferramentas:** Claude Code, Cursor, GitHub Copilot, Gemini CLI,
  Codex CLI, Grok Build, OpenCode, Kiro, Trae, Antigravity e outros.
- **Pegadinhas por provedor:** no Codex os hooks precisam de aprovação manual em
  `/hooks`; no Grok Build é preciso confiar na pasta (`/hooks-trust` ou `--trust`);
  monorepos exigem configuração por workspace.
- **Stack:** JavaScript/TypeScript, Bun como gerenciador de pacotes, Biome no lint.
- **Não avaliado ainda:** ritmo de manutenção e volume de uso do projeto — vale conferir
  o histórico de commits antes de adotar em algo sério.

## Ideias de projeto

- **Vitrine web deste repositório de achados, com design de verdade** — gerar um site
  estático a partir do front-matter dos achados (busca por tag, filtro por nota,
  cartões por categoria) e usar `/impeccable shape` → `craft` → `audit` → `polish` na
  interface. Mata dois coelhos: dá uma UI navegável à biblioteca e serve como teste
  honesto da ferramenta num projeto real. _Esforço: médio._
- **`impeccable detect` como GitHub Action** — workflow que roda `npx impeccable detect
  --json .` nos PRs de projetos frontend e comenta só os anti-padrões **novos** em
  relação à branch base, sem travar o legado. O `--json` já entrega tudo pronto; o
  trabalho é o diff entre os dois relatórios. _Esforço: baixo._
- **DESIGN.md pessoal versionado** — rodar `/impeccable init` uma vez para produzir
  `PRODUCT.md` e `DESIGN.md` (público, marca, voz, anti-referências, paleta,
  tipografia) e guardar esse par como identidade visual reutilizável, copiada para todo
  projeto novo. É a diferença entre "não parece IA" e "parece **meu**". _Esforço: baixo._
- **Um impeccable para outro domínio** — clonar a arquitetura (skill com comandos +
  detectores determinísticos + hooks) e apontá-la para escrita técnica em pt-BR ou para
  design de API REST: o valor do projeto está tanto no formato quanto nas regras.
  _Esforço: alto._

## Notas

```bash
# instalar (escolhendo os provedores)
npx impeccable install --providers=claude --scope=project

# usar dentro do agente
/impeccable init          # gera PRODUCT.md e DESIGN.md
/impeccable audit         # encontra problemas
/impeccable audit blog    # audita só uma área
/impeccable polish        # limpeza final
/impeccable critique      # revisão completa
/impeccable pin <cmd>     # cria atalho para um comando

# detector standalone, sem harness e sem IA
npx impeccable detect src/
npx impeccable detect --json .
npx impeccable ignores add-file "src/legacy/**"
```

- Site do projeto: <https://impeccable.style>
- O detector só respeita as exclusões declaradas em `.impeccable/config.json` — ele
  ignora `.gitignore`, então vale configurar antes de rodar em repositório antigo.
- Antecessor declarado: `frontend-design`, da Anthropic.

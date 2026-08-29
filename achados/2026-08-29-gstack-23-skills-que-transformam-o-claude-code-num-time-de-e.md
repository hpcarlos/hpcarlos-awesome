---
titulo: "gstack — 23 skills que transformam o Claude Code num time de engenharia"
nome: gstack
tldr: "Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado."
licenca: "MIT"
alerta: "amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes"
url: https://github.com/garrytan/gstack
tipo: ferramenta
categorias: [ia, engenharia]
tags: [claude-code, skills, agentes, workflow, qa, deploy, seguranca]
status: novo
nota: 5
adicionado: 2026-08-29
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md, 2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md, 2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md]
---

# gstack — 23 skills que transformam o Claude Code num time de engenharia

## Resumo

Coleção de 23 skills, mais uma penca de ferramentas de linha de comando, que dá ao Claude
Code o ciclo completo de um time de produto: questiona a ideia (`/office-hours`, seis
perguntas antes de escrever código), propõe escopo e arquitetura, revisa design, implementa,
faz code review no nível de engenheiro sênior, roda QA num navegador de verdade que acha e
corrige bug, abre PR (`/ship`) e faz o deploy com verificação de saúde e monitoramento
pós-lançamento (`/canary`). Traz ainda um oficial de segurança (OWASP + STRIDE), defesa
local contra prompt injection, memória entre sessões e trilha de auditoria do que sai da
máquina. Feito por Garry Tan (CEO do Y Combinator) como toolkit pessoal aberto, sob MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a versão mais ambiciosa da ideia que atravessa metade da coleção: dar processo de
engenharia ao agente. Onde
[mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md) e
[addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
oferecem peças de método, este entrega o sprint inteiro montado, incluindo os pedaços que os
outros não tocam — QA em navegador real, deploy e monitoramento.

## Pontos-chave

- **A cobertura é o argumento.** Ele não para no code review: vai até QA em browser de
  verdade (com olhos, via Chrome DevTools), abertura de PR, deploy e canário pós-deploy. É a
  primeira skill da coleção que fecha o ciclo até produção, não só até o commit.
- **`/office-hours` é a joia rara.** Seis perguntas forçadas que redefinem o produto **antes**
  de qualquer código — o mesmo espírito do `grill-me` do
  [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md), e
  provavelmente a parte mais valiosa para quem trabalha sozinho e não tem quem questione a
  ideia.
- **Leva segurança a sério, e isso é raro na categoria.** `/careful` avisa antes de
  `rm -rf`, `DROP TABLE` e force-push; `/freeze` tranca diretórios; `/cso` roda OWASP e
  STRIDE; há defesa local contra prompt injection e um livro de egress do que a máquina
  enviou. É o "cinto de segurança para agentes" do `IDEIAS.md` já implementado.
- **⚠️ É pesado e opinativo.** Instala Chromium customizado, um classificador de ML de 22MB
  para injeção, e assume Bun. Não é uma skill de arquivo Markdown que você lê em cinco
  minutos — é um sistema. Vale o `gstack-egress` e o `gstack-context-bill` que ele mesmo traz
  para ver o que sai e o que custa antes de confiar cegamente.
- **⚠️ Telemetria opt-in, com trilha local por padrão.** Melhor que a maioria (que vem ligada),
  mas confira a configuração. O checklist de primeira execução do `IDEIAS.md` se aplica
  inteiro aqui.
- **Traz benchmark de modelo e auditoria de custo** — `gstack-model-benchmark` compara Claude,
  GPT e Gemini em latência, tokens e custo. É a medição própria que a coleção vinha adiando,
  já embutida.
- **Sobreposição a mapear:** com o
  [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md) há
  choque direto — os dois cobrem spec, review e ship. Não instale os dois sem decidir quem
  manda em cada fase, ou o agente recebe ordens conflitantes.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Adotar como espinha e podar o resto** — se o gstack cobre o sprint inteiro, várias skills
  soltas da coleção viram redundância. Instalá-lo, rodar com o
  [task-observer](2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)
  por duas semanas e ver o que ele torna dispensável é a decisão de arquitetura de skills mais
  importante que a coleção comporta hoje. _Esforço: médio._
- **`/qa` na esteira de interface** — ele acrescenta o passo que faltava ao ciclo
  ver→achar→montar→auditar→polir: testar em navegador real. Junto do
  [shoogle](2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md) e do
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md),
  cobre frontend do repertório ao teste. _Esforço: baixo._
- **Roubar só os power tools** — mesmo sem adotar o sprint inteiro, `/careful`, `/freeze` e
  `/guard` são uma rede de segurança que qualquer sessão de agente merece. Dá para começar
  por eles e ignorar o resto. _Esforço: baixo._
- **Rodar o benchmark antes de escolher gateway** — `gstack-model-benchmark` dá o número que
  falta para decidir entre os modelos que o
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) e o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
  roteiam. Medição própria, não README alheio. _Esforço: baixo._

## Notas

```bash
# instala como skill do Claude Code
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git \
  ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup

# para outros agentes
./setup --host codex        # ou cursor, kiro, factory...

# desinstalar
~/.claude/skills/gstack/bin/gstack-uninstall
```

- Requer Bun 1.0+, Git e um Chromium para `/browse` e `/qa`.
- O ciclo central é `/office-hours` → plano → build → `/review` → `/qa` → `/ship` →
  `/land-and-deploy` → `/canary`.
- **Antes de confiar:** rodar `gstack-egress` (o que sai da máquina) e `gstack-context-bill`
  (quanto custa). O projeto dá as duas ferramentas de auditoria de propósito — use-as.
- **A pergunta de adoção** não é "é bom?" (é), mas "quanto do meu fluxo eu entrego a um
  sistema opinativo de outra pessoa?". Vale começar pelos power tools e pelo `/office-hours`,
  e expandir só o que provar valor.

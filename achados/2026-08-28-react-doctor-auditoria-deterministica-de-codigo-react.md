---
titulo: "react-doctor — auditoria determinística de código React"
nome: react-doctor
tldr: "Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome."
licenca: "MIT"
alerta: "telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos"
url: https://github.com/millionco/react-doctor
tipo: ferramenta
categorias: [web, engenharia]
tags: [react, frontend, linter, performance, claude-code, skills, typescript]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md, 2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md, 2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md]
---

# react-doctor — auditoria determinística de código React

## Resumo

Ferramenta que varre um projeto React e aponta problemas de estado e efeitos, performance,
arquitetura, segurança, acessibilidade e manutenibilidade — de forma determinística, sem
depender de modelo para achar o defeito. Detecta componente complexo demais e árvore JSX
repetida que pede composição. Além da análise estática, faz rastreamento em tempo de
execução pelo Chrome DevTools, destacando com contorno roxo o que está renderizando de
novo enquanto você usa a aplicação. Roda com um comando, instala-se como skill em agentes
(Claude Code, Cursor, Codex, OpenCode) e tem modo de CI. TypeScript, MIT, compatível com
Next.js, Vite, Astro, TanStack, React Native e Expo.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque metade das bases da coleção é React — [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md),
[wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md),
[mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md),
[lobehub](2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md) — e nenhuma
delas foi olhada com critério antes de virar candidata a base de projeto. Esta é a
ferramenta que faz esse exame.

## Pontos-chave

- **Determinístico é o ponto.** As regras não dependem de LLM: o mesmo código dá sempre o
  mesmo resultado, e o agente entra só na hora de corrigir. Mesma tese do
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md),
  aplicada a outra camada — um cuida de anti-padrão visual, este de estado, efeito e
  render.
- **O modo de CI só reporta problema novo**, sem cobrar o passivo já existente. É
  exatamente o que eu havia sugerido *construir* para o impeccable no achado dele: aqui já
  vem pronto. Vale conferir como fazem o diff antes de escrever a versão caseira.
- **⚠️ Telemetria vem ligada** — desliga com `--no-telemetry`. Terceiro achado seguido com
  essa característica; virou praxe em ferramenta de agente, e vale checar sempre.
- **⚠️ O rastreamento de runtime é do navegador inteiro**, não só da sua aba: pode capturar
  URLs e caminhos de arquivo de outras abas abertas. Rode com um Chrome limpo, sem sessão
  pessoal, se for guardar ou compartilhar o resultado.
- **Instala como skill de agente**, o que o coloca no mesmo grupo do impeccable e das
  coleções do [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
  e do [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md):
  ferramenta que vira capacidade do agente, não programa separado.
- **É o sucessor declarado do [react-scan](2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)**, do mesmo grupo: aquele só
  mostra render em tempo real, este acrescenta análise estática de arquitetura,
  segurança e acessibilidade. O README do react-scan recomenda vir para cá.
- **Vem da millionco**, gente do Million.js — projeto conhecido por trabalho de performance
  em React. A ligação não é declarada no README, mas o histórico do grupo dá contexto ao
  foco em render.
- **Configurável por `doctor.config.ts`**; README enxuto, focado em instalação e uso, sem
  detalhar as regras — para saber o que ele acha, o caminho é rodar.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Auditar as bases antes de escolher uma** — rodar `npx react-doctor@latest` no
  saas-starter-kit, no wacrm e no mission-control e comparar os relatórios. Você tem três
  candidatos a fundação de projeto e nenhuma evidência sobre a qualidade interna deles;
  uma tarde de auditoria vale mais que qualquer contagem de estrelas. _Esforço: baixo._
- **Dupla de frontend: react-doctor + [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)**
  — um garante que a interface não tenha cara de template, o outro que o código por trás
  não esteja re-renderizando o mundo a cada tecla. Juntos cobrem frontend da pele ao
  esqueleto, e ambos rodam como skill do mesmo agente. _Esforço: baixo._
- **Portão de qualidade nos seus repositórios** — `npx react-doctor@latest ci install` em
  qualquer projeto React seu, aproveitando que ele ignora o passivo e cobra só o que
  entrar novo. É a forma de melhorar código legado sem parar tudo para refatorar.
  _Esforço: baixo._
- **Caçada a re-render com evidência** — usar o `scan` de runtime numa tela que você acha
  lenta e registrar aqui o antes e o depois, com número. A coleção tem várias ferramentas
  que prometem performance e nenhuma medição própria até agora. _Esforço: médio._

## Notas

```bash
npx react-doctor@latest                        # auditoria do projeto
npx react-doctor@latest install                # instala como skill do agente
npx react-doctor@latest ci install             # configura o portão de CI
npx react-doctor@latest scan http://localhost:3000   # trace de runtime no Chrome
npx react-doctor@latest --no-telemetry         # sem telemetria
```

- Precisa de Chrome instalado para o modo `scan`; o resto roda só com Node.
- Durante o trace, o que re-renderiza aparece com contorno roxo na tela — é a forma mais
  rápida de ver desperdício de render sem ler código.
- Site do projeto: <https://react.doctor>
- **Primeiro uso sugerido:** rodar nos boilerplates que já estão na coleção. É barato,
  responde uma pergunta em aberto e produz um achado novo com dado real.

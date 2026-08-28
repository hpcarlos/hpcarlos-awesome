---
titulo: "react-scan — mostra o que está re-renderizando em React"
nome: react-scan
tldr: "Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script."
licenca: "MIT"
alerta: "o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção"
url: https://github.com/aidenybai/react-scan
tipo: ferramenta
categorias: [web, engenharia]
tags: [react, frontend, performance, devtools, typescript, debug]
status: novo
nota: 3
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md, 2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md]
---

# react-scan — mostra o que está re-renderizando em React

## Resumo

Ferramenta que desenha na própria página, em tempo real, quais componentes React estão
re-renderizando à toa. Não exige alterar componente nenhum: uma tag de script no HTML
resolve, e há também extensão de navegador e instalação por npm. Traz barra de ferramentas
embutida, API imperativa (`scan()`, `useScan()`, `setOptions()`) e ganchos de ciclo de
commit (`onCommitStart`, `onRender`, `onCommitFinish`) para quem quiser registrar dados em
vez de só olhar. Feito por Aiden Bai, da Million Software, sob MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Pelo caminho de menor atrito: colar uma linha no HTML e ver o desperdício de render
acontecendo, sem instalar dependência nem configurar nada. Para diagnóstico rápido de uma
tela que "está travando", isso é difícil de bater.

## Pontos-chave

- **⚠️ O próprio projeto recomenda o sucessor.** Logo no topo do README há o aviso de que
  você ainda pode usar o react-scan, mas que o recomendado agora é o
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md) —
  mesma origem, escopo maior (arquitetura, segurança e acessibilidade, além de
  performance). **Os dois achados que você mandou seguidos são a versão antiga e a nova da
  mesma linhagem.** Para projeto novo, comece pelo doctor.
- **Onde ele ainda ganha:** atrito zero. Uma tag `<script>` apontando para o CDN funciona
  em qualquer página, inclusive em projeto que você não controla o build; o react-doctor
  exige rodar um comando no repositório. Para inspecionar uma tela alheia ou fazer um
  diagnóstico de dois minutos, este continua mais prático.
- **⚠️ Não é para produção.** A opção que força isso se chama
  `dangerouslyForceRunInProduction`, o que já diz tudo sobre a intenção dos autores.
- **A causa raiz que ele expõe** é a comparação de props por referência, comportamento
  normal do React: objeto ou função recriada a cada render faz o filho renderizar de novo
  sem necessidade. Ver isso destacado na tela ensina mais rápido que ler sobre memoização.
- **Integra com Next.js (App e Pages Router), Vite e Remix**, com trecho pronto para cada
  um no README.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Usar os dois em momentos diferentes** — react-scan quando a pergunta é "por que esta
  tela está lenta agora?", e o
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)
  quando é "esta base é saudável?". Não são concorrentes na sua bancada, são o martelo e a
  radiografia. _Esforço: baixo._
- **Aprender memoização vendo, não lendo** — ligar numa tela sua, interagir e observar o
  que pisca. É a forma mais rápida de entender por que `useMemo` e `useCallback` existem, e
  também de descobrir que muita gente os usa onde não precisa. _Esforço: baixo._
- **Instrumentar com os ganchos de commit** — `onRender` permite registrar contagem de
  render por componente ao longo de uma sessão de uso, produzindo número em vez de
  impressão. Serve de linha de base antes de otimizar qualquer coisa. _Esforço: médio._

## Notas

```html
<!-- antes de qualquer outro script -->
<script crossOrigin="anonymous" src="//unpkg.com/react-scan/dist/auto.global.js"></script>
```

```bash
npx -y react-scan@latest init     # configura sozinho
npm install -D react-scan         # como dependência de desenvolvimento
```

- No Next.js App Router, entra em `app/layout.tsx` com `next/script` e
  `strategy="beforeInteractive"`.
- Há extensão de navegador, útil quando não dá para tocar no código da página.
- Os agradecimentos do projeto citam React DevTools, Million Lint e *Why Did You Render?*
  como inspirações — vale conhecer se o assunto interessar.
- **Recomendação:** manter na coleção como ferramenta de diagnóstico rápido, e tratar o
  react-doctor como a escolha padrão para trabalho contínuo.

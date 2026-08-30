---
titulo: "camofox-browser — navegador anti-detecção como servidor para agentes"
nome: camofox-browser
tldr: "Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados."
licenca: "MIT"
alerta: "contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão"
url: https://github.com/jo-inc/camofox-browser
tipo: ferramenta
categorias: [web, ia]
tags: [navegador, automacao, scraping, playwright, nodejs, agentes]
status: novo
nota: 2
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md]
---

# camofox-browser — navegador anti-detecção como servidor para agentes

## Resumo

Servidor REST que embrulha o Camoufox — um fork do Firefox que falsifica impressão digital
no nível do C++, antes de o JavaScript da página conseguir ler os valores — e o entrega
como substituto de Puppeteer ou Playwright para agentes de IA. Além da evasão, traz coisas
genuinamente boas de engenharia: referências estáveis de elemento (`e1`, `e2`) para clique
confiável, *snapshots* de acessibilidade cerca de 90% menores que o HTML cru, isolamento de
sessão, importação de cookies, roteamento por proxy com geolocalização, login interativo
por VNC e rastreamento de sessão com captura de tela, DOM e rede. Node.js, MIT, feito pela
equipe do agente pessoal "jo".

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Pelas partes que não têm nada a ver com evasão. O *snapshot* de acessibilidade em vez de
HTML bruto e as referências estáveis de elemento atacam os dois problemas reais de agente
que navega: contexto caro demais e clique que erra o alvo. Essas ideias valem mesmo para
quem nunca vai querer driblar bloqueio nenhum.

## Pontos-chave

- **⚠️ O propósito declarado é contornar detecção de bot**, incluindo proteções de
  Cloudflare e bloqueios por impressão digital. Fazer isso em site de terceiro em geral
  **viola os termos de uso** dele e, dependendo do país e do tipo de dado acessado, pode
  ter consequência legal. Automatizar a sua própria conta, testar o seu próprio site ou
  pesquisar com autorização é uma coisa; furar o bloqueio de quem não quer ser raspado é
  outra bem diferente — e o risco é de quem roda.
- **⚠️ Telemetria ligada por padrão.** Ele envia relatório anônimo de travamento para um
  endpoint externo, com domínios públicos em texto claro e domínios privados sob hash
  (URLs, tokens e IPs são removidos, e não vai conteúdo de página nem cookie). Se isso não
  serve para você: `export CAMOFOX_CRASH_REPORT_ENABLED=false`.
- **O que vale copiar, independentemente do resto:** *snapshot* de acessibilidade no lugar
  do HTML — muito menor, e mais próximo do que o modelo precisa entender — e as referências
  numeradas de elemento, que tornam o clique determinístico em vez de depender de seletor
  frágil.
- **Não é o Camoufox**, é um servidor em volta dele: baixa o binário (~300 MB) via
  `camoufox-js` e o controla por Playwright, expondo tudo por HTTP. Dá para apontar um
  executável próprio com `CAMOUFOX_EXECUTABLE`.
- **Também tem aviso de golpe cripto** com o nome do projeto — o segundo achado seguido com
  esse problema, depois do
  [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md).
  Projeto de agente que ganha atenção vira isca; vale desconfiar de token com nome de
  repositório conhecido.
- **Lembre-se de que a página lida é entrada hostil.** O
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  já pedia para tratar mensagem de agente e MCP como não confiável; conteúdo raspado da web
  aberta é o caso extremo disso, e um agente que lê e obedece o que encontra é um problema
  esperando para acontecer.
- **Limites operacionais:** 50 sessões simultâneas e 10 abas por sessão (configuráveis),
  sessão expira em 30 minutos de inatividade, e não grava vídeo (limitação do Firefox com
  Playwright).
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Aposentar o HTML cru nos seus agentes** — adotar *snapshot* de acessibilidade e
  referências numeradas de elemento como formato de entrada para qualquer automação de
  navegador sua. Corta contexto, reduz custo e melhora a taxa de acerto do clique, sem
  depender de nenhuma capacidade de evasão. _Esforço: médio._
- **Testar o seu próprio produto contra impressão digital** — usar a ferramenta do lado
  defensivo: descobrir o que o seu site expõe e como ele se comporta diante de um
  navegador que mente sobre si. Uso legítimo, e útil se você mantém algo com login.
  _Esforço: baixo._
- **Automatizar as suas próprias contas** — baixar relatório de um painel que não oferece
  API, por exemplo. Aqui a evasão é acessória: você tem a credencial e o direito ao dado.
  _Esforço: baixo._
- **Ler o rastreamento de sessão como referência de depuração** — captura de tela, DOM e
  rede por passo é exatamente o que falta quando uma automação quebra em produção e
  ninguém sabe por quê. _Esforço: baixo._

## Notas

```bash
npx @askjo/camofox-browser          # servidor em http://localhost:9377
# ou
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
make up                             # docker, detecta a arquitetura

export CAMOFOX_CRASH_REPORT_ENABLED=false   # desliga a telemetria
```

- Node 16+; o binário do Camoufox (~300 MB) é baixado na primeira execução.
- `CAMOFOX_API_KEY` protege a importação de cookies — sem ela, esse endpoint fica
  desabilitado. Se for expor o servidor na rede, configure antes de qualquer outra coisa:
  cookie importado é sessão autenticada de alguém.
- Macros de busca prontas (`@google_search`, `@youtube_search`, `@amazon_search`) e
  extração de transcrição do YouTube via `yt-dlp`.
- **Recomendação:** manter em `nota: 2` enquanto o uso for hipotético. Se um dia servir
  para automatizar conta própria ou testar produto seu, o valor sobe; para raspar site
  alheio contra a vontade dele, o problema não é técnico.

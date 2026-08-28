---
titulo: "OpenDesign — gerador de artefatos de design dirigido por agente"
nome: OpenDesign
tldr: "Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real."
licenca: "Apache-2.0"
alerta: "telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10"
url: https://github.com/nexu-io/open-design
tipo: ferramenta
categorias: [design, ia]
tags: [design, prototipo, mcp, claude-code, skills, apresentacoes, electron]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md, 2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md]
---

# OpenDesign — gerador de artefatos de design dirigido por agente

## Resumo

Motor que amplia o que um agente de código entrega: em vez de só arquivos-fonte, ele
produz protótipo navegável de web, mobile ou desktop, apresentação, dashboard ao vivo,
imagem, vídeo e documento de várias páginas. Traz 151 pacotes de design system — Linear,
Stripe, Shopify, Notion e outros — organizados em torno de um `DESIGN.md`, além de mais de
uma centena de skills e centenas de plugins. Exporta HTML embutido, PDF, PPTX, ZIP,
Markdown e MP4. Instala-se como servidor MCP em mais de vinte agentes diferentes, roda como
app de desktop, Docker ou a partir do código. Next.js e Node, licença Apache-2.0, com
serviço em nuvem opcional dos mantenedores.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque fecha uma lacuna concreta da coleção: há várias ferramentas para o agente **escrever
e revisar código**, e nenhuma para ele **entregar o artefato** que se mostra a alguém. Um
protótipo navegável ou um deck em PDF é o que convence cliente e time — e é justamente o
que costuma sair mal quando feito no improviso.

## Pontos-chave

- **Não é editor de design.** Não há canvas para arrastar pixel: é gerador. Quem quer
  ajustar detalhe à mão continua precisando de outra ferramenta; quem quer sair de "ideia"
  para "coisa renderizada" em uma passada, ganha muito.
- **A convergência com o [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
  é o achado mais interessante:** os dois giram em torno de um arquivo `DESIGN.md` que fixa
  identidade visual. Um gera esse arquivo por entrevista (`/impeccable init`), o outro traz
  151 prontos, copiados de produtos reais. Dá para usar o `DESIGN.md` de um como entrada do
  outro.
- **Saída de verdade, não mockup:** HTML, CSS e componentes que rodam — o que significa que
  o resultado pode virar código de produção em vez de virar tarefa de reimplementação.
- **⚠️ Telemetria ligada por padrão** (analytics e replay de sessão, com dados filtrados).
  Quarto achado seguido com essa característica — vale conferir a configuração antes do
  primeiro uso sério.
- **⚠️ Custo por fora:** o modelo é BYOK (você traz sua chave). Geração de imagem e,
  principalmente, de vídeo consome API paga rapidamente. Há serviço em nuvem próprio dos
  mantenedores como alternativa — e é aí que mora o modelo de negócio.
- **⚠️ Versão 0.10.** Projeto ativo e bem documentado, mas ainda antes do 1.0: espere
  mudança de comportamento entre versões.
- **Se posiciona como alternativa aberta ao Claude Design**, e cita Figma, v0, Lovable e
  Bolt como vizinhança. Comparação escrita pelo próprio autor, com o desconto de sempre.
- **Vídeo exige FFmpeg e Chrome headless**; desktop é sólido em macOS e Windows, com Linux
  em segundo plano.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Um cria, o outro critica** — gerar o protótipo aqui e passar o
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
  (`audit` e `polish`) por cima, com o
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)
  fechando a parte de código. Três ferramentas, três papéis distintos, nenhuma sobreposição.
  _Esforço: baixo._
- **A vitrine dos achados, finalmente** — a primeira ideia registrada no `IDEIAS.md` era um
  site para esta coleção, parada por falta de vontade de fazer interface. O OpenDesign gera
  o protótipo a partir do `graph.json` ou do front-matter; o impeccable ajusta. O que
  faltava era exatamente esta peça. _Esforço: médio._
- **Deck do que entrou no mês** — apresentação em PDF ou PPTX gerada a partir dos achados
  recentes, com uma página por item. Útil se você compartilha esses achados com alguém, e é
  uso direto dos templates de deck. _Esforço: baixo._
- **Painel de custo dos agentes** — os dashboards ao vivo daqui, alimentados pelas métricas
  do [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
  e do [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md),
  são a camada visual que falta na ideia "fechar a conta dos agentes". _Esforço: médio._

## Notas

```bash
# como servidor MCP no seu agente
od mcp install claude

# docker
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy && cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d          # http://127.0.0.1:7456

# a partir do código
corepack enable && pnpm install && pnpm tools-dev run web
```

- App de desktop em DMG (macOS) e MSIX (Windows); AppImage no Linux.
- Node ~24 e pnpm 10.33.x — versões específicas, confira antes de compilar.
- O `OD_API_TOKEN` gerado no `.env` é o que protege a instância: não suba nada sem ele.
- Os 151 design systems valem uma olhada mesmo sem usar a ferramenta — é um catálogo de
  como produtos conhecidos organizam cor, tipografia e espaçamento.

---
titulo: "Vibe-Trading — agente de IA para pesquisa e execução de ordens em corretora"
nome: Vibe-Trading
tldr: "Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria."
licenca: "MIT"
alerta: "executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário"
url: https://github.com/HKUDS/Vibe-Trading
tipo: projeto
categorias: [ia, financas]
tags: [trading, agentes, python, backtest, mcp, llm, fastapi]
status: novo
nota: 3
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md, 2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md]
---

# Vibe-Trading — agente de IA para pesquisa e execução de ordens em corretora

## Resumo

Plataforma do laboratório de ciência de dados da HKU que junta, num só lugar,
desenvolvimento de estratégia, backtest em nove mercados, análise de carteira e
**execução de ordens reais** através de mais de uma dezena de corretoras (Alpaca, Binance,
OKX, Interactive Brokers, Futu, Longbridge e outras). Traz um acervo de mais de 400
fatores alfa, ferramentas de pesquisa que leem 13F da SEC, composição de ETF e artigos
acadêmicos, além de uma biblioteca de funções quantitativas. Roda como web, CLI, app
Electron ou tarefa agendada, integra dezenas de fontes de dado e provedores de modelo, e
expõe 74+ ferramentas via MCP. Python 3.11+ com FastAPI e React, licença MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Pelo desenho de governança, mais do que pelo trading. É o primeiro achado da coleção em
que um agente executa ação **irreversível e cara** no mundo real, e o projeto leva isso a
sério: kill-switch, teto de exposição, limite diário de ordens, conta-sombra e livro de
auditoria encadeado por hash. Esse conjunto é a resposta prática à pergunta que o
[mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
levanta ao dizer para tratar agente como entrada não confiável.

## Pontos-chave

- **⚠️ Ele manda ordem de verdade.** Não é simulador com botão de produção escondido:
  execução ao vivo é funcionalidade central, e quem conecta credencial de corretora está
  autorizando um LLM a movimentar dinheiro real. Perda aqui não se desfaz com `git revert`.
- **⚠️ Não vi disclaimer financeiro no material que li.** Há aviso de segurança sobre
  golpes (abaixo), mas nenhum texto de "isto não é recomendação de investimento, você pode
  perder tudo". A ausência é relevante: a responsabilidade fica inteiramente com quem usa.
- **⚠️ Existe golpe usando o nome do projeto.** O próprio README avisa que uma conta no X
  (`VibeTrading_HKU`), um projeto na Virtuals e um contrato de token **não são oficiais** —
  os mantenedores nunca lançaram token nem memecoin, e pedem que ninguém compre, conecte
  carteira ou assine nada. Se você chegou ao projeto por indicação de rede social, confira
  se é este repositório mesmo.
- **A parte que vale copiar é a de contenção:** kill-switch que zera todas as posições ao
  receber HALT, tetos de exposição com sinal, limite diário de ordens, confirmação em dois
  fatores para liberar mandato, conta-sombra espelhando a execução para conferência, e
  registro encadeado por hash. É um catálogo de como deixar agente agir sem entregar as
  chaves de casa.
- **Rigor de pesquisa acima da média:** validação cruzada com purga, análise combinatória
  de fatores e menção explícita a viés de sobrevivência nos dados de ações chinesas —
  tratar isso na cara do usuário é sinal de honestidade metodológica.
- **Recusas por segurança embutidas**, como bloquear backtest composto em moedas mistas.
  Um sistema que se recusa a responder o que não sabe responder direito vale mais que um
  que sempre devolve um número.
- **Custo de inferência não é trivial** num agente que pesquisa continuamente — é caso de
  uso para o [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md),
  inclusive pelo cache semântico.
- **Números não verificados** (API do GitHub bloqueada nesta sessão).

## Ideias de projeto

- **Roubar o padrão de contenção para os seus agentes** — kill-switch, teto de ação, livro
  encadeado por hash e conta-sombra não têm nada de específico de finanças: servem para
  qualquer agente que mande e-mail, altere banco de dados ou publique em nome de alguém.
  Ler esse módulo e escrever a versão mínima disso é o aprendizado mais transferível do
  achado. _Esforço: médio._
- **Usar só o motor de backtest, sem conectar corretora** — dá para explorar o acervo de
  fatores e o mecanismo de validação sem colocar um centavo em risco. Se a curiosidade é
  quantitativa e não operacional, este é o caminho inteiro. _Esforço: baixo._
- **Experimento honesto em papel** — rodar em conta de papel por um período fixo e comparar
  o resultado do agente com comprar um índice e não fazer nada. É o único teste que
  interessa, e a maioria das ferramentas do gênero não sobrevive a ele. Registrar o número
  aqui, dando certo ou não. _Esforço: médio._
- **Ler o Quantlib embutido como referência** — a biblioteca de funções quantitativas
  (opções, títulos, VaR/CVaR, atribuição de performance) é material de estudo mesmo fora do
  projeto, para quem quiser entender de onde saem esses números. _Esforço: baixo._

## Notas

```bash
pip install vibe-trading-ai
vibe-trading run
vibe-trading web        # interface local
vibe-trading desktop    # app Electron
docker-compose up
```

- Credenciais ficam em `~/.vibe-trading/.env` ou no chaveiro do sistema; os dados
  persistem em `~/.vibe-trading/` (realocável por `VIBE_TRADING_HOME`).
- **Ordem sensata:** backtest → papel → conta real minúscula → e só então considerar valor
  relevante. Pular etapa aqui custa dinheiro, não tempo.
- Algumas fontes de dado (Tushare, Futu, Longbridge) exigem conta gratuita; em Mac Intel é
  preciso o extra `[smc]` por causa de problema de build do `llvmlite`.
- Mantido pelo HKUDS, laboratório da Universidade de Hong Kong — a mesma origem de outros
  projetos conhecidos de agentes.

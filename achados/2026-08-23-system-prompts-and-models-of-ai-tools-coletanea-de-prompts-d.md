---
titulo: "system-prompts-and-models-of-ai-tools — coletânea de prompts de sistema de ferramentas comerciais"
nome: system-prompts
tldr: "Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar."
licenca: "GPL-3.0 declarada"
alerta: "conteúdo de terceiros sem origem informada; não reutilize os textos"
url: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
tipo: outro
categorias: [ia, engenharia]
tags: [prompts, llm, agentes, prompt-engineering, referencia]
status: novo
nota: 3
adicionado: 2026-08-23
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md, 2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md]
---

# system-prompts-and-models-of-ai-tools — coletânea de prompts de sistema de ferramentas comerciais

## Resumo

Arquivo público com os prompts de sistema e as definições de ferramenta de mais de 30
produtos comerciais de IA — entre eles Cursor, Devin, GitHub Copilot, Windsurf, v0,
Replit, Lovable, Manus, Perplexity, Warp, Kiro, Trae e Claude Code. É material que essas
empresas não publicam: o texto que orienta o comportamento do agente por trás de cada
produto. Para quem escreve instruções para agentes, é a chance rara de ler como equipes
com muito recurso resolveram os mesmos problemas — recusa, uso de ferramenta, formato de
saída, limites de escopo.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Como material de estudo, e ele conversa direto com os dois achados de skills que chegaram
antes: se você vai escrever suas próprias skills, ler prompt de produto real ensina mais
sobre estrutura do que qualquer tutorial. O valor está em entender os padrões — não em
colar o texto.

## Pontos-chave

- **⚠️ O README não explica como o conteúdo foi obtido.** São textos internos de produtos
  comerciais, publicados sem indicação de autorização das empresas. Não há aviso legal,
  nota de origem nem política de remoção — apenas o acervo.
- **⚠️ A licença GPL-3.0 declarada não significa o que parece.** Quem publica um acervo não
  adquire direito sobre obra alheia, e não pode licenciar o que não lhe pertence. Na
  prática: **copiar esses textos para dentro de um produto seu é risco jurídico real**,
  independentemente do que diz o arquivo de licença. Ler para aprender é uma coisa;
  reaproveitar literalmente é outra.
- **Conflito de interesse no próprio README:** ele alerta startups de IA a protegerem seus
  prompts e, na sequência, indica um serviço comercial que promete identificar esse tipo
  de exposição. O repositório cria o problema que o serviço vende resolver — vale saber
  disso ao ler as recomendações de lá.
- **O conteúdo envelhece rápido.** Prompt de produto muda a cada release; boa parte do
  acervo reflete uma versão que já não está no ar. Serve para estudar padrões duradouros,
  não para saber como a ferramenta X se comporta hoje.
- **Números não verificados** (API do GitHub bloqueada nesta sessão). A leitura indica
  adoção muito alta, o que é plausível para um repositório desse tipo.

## Ideias de projeto

- **Destilar padrões, não textos** — ler uma dúzia dos prompts perguntando o mesmo a todos:
  como definem o papel? como descrevem ferramentas? como tratam incerteza e recusa? como
  pedem formato de saída? O resultado é um documento **seu**, com princípios em vez de
  trechos, para escrever as próprias skills no formato do
  [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
  ou do [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md).
  _Esforço: médio._
- **Medir o custo fixo de um agente** — contar quantos tokens cada prompt de sistema
  consome e comparar. É um número concreto que quase ninguém tem, e muda a conta de
  qualquer produto de IA: esse custo entra em toda requisição, antes de o usuário digitar
  qualquer coisa. Casa com a ideia do medidor de consumo do
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md).
  _Esforço: baixo._
- **Checklist defensivo para produto próprio** — usar o acervo ao contrário: se um dia
  você embutir prompt em produto (no [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md),
  por exemplo), assuma que ele será extraído. Isso é uma decisão de arquitetura — não
  colocar segredo, regra de negócio ou credencial no prompt — e não uma medida de
  segurança a acrescentar depois. _Esforço: baixo._
- **Comparar gerações do mesmo produto** — o histórico de commits mostra como o prompt de
  uma mesma ferramenta mudou ao longo do tempo. Ver o que foi acrescentado depois costuma
  revelar quais problemas apareceram na prática. É a leitura mais interessante do acervo, e
  a que menos se aproxima de copiar. _Esforço: médio._

## Notas

- **Recomendação de uso:** tratar como leitura de referência. Não copiar trechos para
  produto, cliente ou material publicado; não redistribuir. O aprendizado transferível são
  os padrões de estrutura, e esses você reescreve com as próprias palavras.
- Repositórios desse tipo costumam ser instáveis — podem sair do ar por pedido das
  empresas envolvidas. Se algum prompt for útil para o seu estudo, tome nota das conclusões
  agora, não do link.
- Relação com os outros achados: as skills do
  [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
  e do [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
  mostram como *escrever* instrução para agente; este acervo mostra como as empresas de
  fato *escreveram* as delas. Lidos juntos, um valida ou contesta o outro.

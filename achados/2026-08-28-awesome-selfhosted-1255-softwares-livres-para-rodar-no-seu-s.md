---
titulo: "awesome-selfhosted — 1.255 softwares livres para rodar no seu servidor"
nome: awesome-selfhosted
tldr: "Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados."
licenca: "CC-BY-SA-3.0"
alerta: "305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado"
url: https://github.com/awesome-selfhosted/awesome-selfhosted
tipo: outro
categorias: [devops, web]
tags: [self-hosted, servidores, privacidade, catalogo, licencas]
status: novo
nota: 5
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md, 2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md]
---

# awesome-selfhosted — 1.255 softwares livres para rodar no seu servidor

## Resumo

A lista de referência de software livre que se hospeda no próprio servidor em vez de
assinar como serviço: 1.255 projetos em 84 categorias, de CMS e CRM a streaming, e-mail,
automação residencial, monitoramento, wikis e gerenciadores de senha. Mantida pela
comunidade há anos, com dois diferenciais que a separam da maioria das listas *awesome*:
**cada item declara licença e stack**, e há verificação automática de link morto e de
projeto sem manutenção — os abandonados ficam marcados.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque muda a natureza da coleção. Todo o resto aqui é matéria-prima para construir; esta é
a lista do que **não precisa ser construído**. Quando a resposta certa for "isso já existe,
maduro, há dez anos", é aqui que se descobre.

## Pontos-chave

- **⚠️ 305 dos 1.255 são AGPL ou equivalente** — quase um em cada quatro. Para uso próprio,
  irrelevante. Para oferecer o software como serviço a clientes, mesmo modificado, a licença
  obriga a disponibilizar o código das suas alterações. É o filtro que precisa vir **antes**
  da escolha técnica, não depois.
- **⚠️ 66 projetos estão marcados como não mantidos** pelos próprios autores. A fonte
  sinaliza; rodar software morto exposto à internet é dívida de segurança disfarçada de
  economia.
- **Licença e stack em todo item** é o que torna esta lista utilizável de verdade: dá para
  filtrar por "MIT e roda em Docker" antes de abrir qualquer página. Foi o que permitiu
  importar tudo de forma determinística, sem depender de leitura individual.
- **Distribuição de licenças:** MIT (353), AGPL-3.0 (299), GPL-3.0 (223), Apache-2.0 (133),
  GPL-2.0 (101). Um retrato interessante do ecossistema — o mundo do software
  auto-hospedado é bem mais copyleft que o das ferramentas de agente desta coleção.
- **Há uma lista separada para software não livre**, o que mantém a principal coerente com
  o critério declarado.
- **A abundância é o custo.** Com 1.255 opções, escolher é o trabalho — daí o catálogo em
  [`SELFHOSTED.md`](../SELFHOSTED.md) e os recortes em
  [`IDEIAS-SELFHOSTED.md`](../IDEIAS-SELFHOSTED.md).

## Ideias de projeto

As ideias completas estão em **[`IDEIAS-SELFHOSTED.md`](../IDEIAS-SELFHOSTED.md)**. As três
que valem começar por:

- **Trocar o SaaS que mais incomoda** — escolher uma assinatura, achar o substituto na
  categoria correspondente, filtrando por licença permissiva e descartando os abandonados.
  Uma de cada vez; migrar tudo junto é como isso acaba abandonado. _Esforço: baixo._
- **Montar a base antes dos serviços** — proxy reverso com TLS, backup automatizado e
  painel, nessa ordem. Sem isso, cada serviço novo vira um problema de rede e você esquece
  o que está no ar. _Esforço: médio._
- **Completar o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) com peças
  prontas** — chamados, controle de tempo, emissão e documentos existem maduros nesta
  lista. O que falta para um negócio real não precisa ser escrito. _Esforço: médio._

## Notas

- Catálogo completo, com títulos de categoria em português:
  [`SELFHOSTED.md`](../SELFHOSTED.md), gerado por `scripts/indexar_selfhosted.py`.
- **As descrições dos itens continuam em inglês.** São mais de mil frases: traduzir à mão
  levaria semanas e reescrevê-las sem ler cada projeto seria inventar. O que mais importa
  numa decisão — licença, stack, estado de manutenção — já vem estruturado e foi preservado.
- A importação é reprodutível: `scripts/importar_selfhosted.py` lê o Markdown de origem e
  gera `dados/selfhosted.tsv`. Quando a fonte atualizar, é um comando.
- A fonte tabular responde melhor que a lista para pergunta específica:
  `awk -F'\t' '$4=="MIT" && $5 ~ /Docker/' dados/selfhosted.tsv | cut -f1,2`.
- Existe também uma versão em HTML mais navegável, em awesome-selfhosted.net.

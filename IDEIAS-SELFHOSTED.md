Ideias a partir do software auto-hospedado
===

Projetos que dá para montar com os 1.255 softwares catalogados em
[`SELFHOSTED.md`](SELFHOSTED.md) — combinando-os entre si, ou cruzando com os achados da
lista principal ([`README.md`](README.md)).

A diferença desta coleção para as outras: aqui **nada precisa ser construído**. São
sistemas prontos, maduros, muitos com mais de uma década de uso. O trabalho é escolher,
hospedar e conectar — e é justamente na escolha que a lista de 1.255 atrapalha mais do que
ajuda. As ideias abaixo são recortes com critério.

> Ideias que combinam achados da lista principal entre si estão em [`IDEIAS.md`](IDEIAS.md);
> as das aplicações de LLM, em [`IDEIAS-LLM-APPS.md`](IDEIAS-LLM-APPS.md).

## O filtro que vem antes de tudo

### Ler a licença antes de escolher

**305 dos 1.255 projetos são AGPL ou equivalente.** Para uso próprio, isso é irrelevante.
Mas se a ideia for oferecer o software como serviço a clientes — mesmo modificado, mesmo
só para eles —, a AGPL obriga a disponibilizar o código das suas modificações. É a mesma
armadilha que já apareceu no
[lobehub](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md), com
licença própria, e no [sub2api](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md).

- **Esforço:** baixo — é decisão, não construção
- **Como filtrar:** `awk -F'\t' '$4 ~ /MIT|Apache|BSD/' dados/selfhosted.tsv` devolve só o
  permissivo, se o plano envolver produto fechado.
- **E os 66 abandonados:** a fonte marca quem os autores declararam não manter. Rodar
  software morto exposto à internet é dívida de segurança, não economia.

## Substituir assinaturas por coisas suas

### Trocar o SaaS que você já paga

O caminho mais curto para valor real: listar o que você assina hoje e procurar na coleção o
equivalente auto-hospedado. As categorias com mais opções maduras são
[gerenciadores de senha](SELFHOSTED.md#gerenciadores-de-senha),
[notas e editores](SELFHOSTED.md#notas-e-editores),
[favoritos](SELFHOSTED.md#favoritos-e-compartilhamento-de-links),
[finanças pessoais](SELFHOSTED.md#finanças-pessoais-e-orçamento) e
[galerias de fotos](SELFHOSTED.md#galerias-de-fotos).

- **Esforço:** baixo por item, médio para a migração de dados
- **Primeiro passo:** um só. Migrar tudo de uma vez é como acaba abandonado — escolha o
  serviço cuja assinatura mais incomoda e faça só ele.
- **Antes de começar:** decida a estratégia de backup. Auto-hospedar sem backup é trocar
  uma assinatura por um risco.

### A base de tudo: painel, proxy e backup

Antes de hospedar dez coisas, hospede as três que sustentam as outras — de
[plataformas de auto-hospedagem](SELFHOSTED.md#plataformas-de-auto-hospedagem),
[proxy](SELFHOSTED.md#proxy) e
[painéis pessoais](SELFHOSTED.md#painéis-pessoais). Sem proxy reverso com TLS, cada serviço
novo vira um problema de rede; sem painel, você esquece o que está rodando.

- **Esforço:** médio (uma vez só)
- **Ordem:** proxy reverso → backup automatizado → painel → o resto.
- **Ligação com a lista principal:** o
  [mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  alerta que o padrão de muitos projetos pressupõe rede confiável e credencial de fábrica.
  Vale para tudo desta coleção.

## Combinações com a lista principal

### Sede de operação sem assinaturas

O [Huly](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)
concentra num app só o que costuma ser Jira + Slack + Notion + CRM. Combinado com o
[wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) na ponta do
atendimento, vira a espinha de operação de um negócio pequeno sem nenhuma mensalidade de
SaaS — o Huly cuida do time por dentro, o wacrm do cliente por fora.

- **Alimenta:** Huly + wacrm
- **Esforço:** alto (a stack do Huly — Mongo, Elastic, MinIO — é pesada)
- **Primeiro passo:** subir só um módulo do Huly (gestão de projetos) e viver com ele um
  mês antes de migrar qualquer coisa de verdade.
- **Cuidado:** adotar a suíte inteira de uma vez é como isso vira peso morto. Se o módulo
  mais importante não convencer, os outros cinco não salvam.

### O CRM que você já tem, mais o que falta

O [wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) cobre WhatsApp e
funil, mas um negócio real precisa de mais: emissão, chamados, controle de tempo,
documentos. As categorias [CRM](SELFHOSTED.md#crm),
[chamados e suporte](SELFHOSTED.md#chamados-e-suporte),
[controle de tempo](SELFHOSTED.md#controle-de-tempo) e
[planejamento de recursos (ERP)](SELFHOSTED.md#planejamento-de-recursos-erp) fecham o resto
sem escrever código.

- **Esforço:** médio
- **Cuidado com a licença:** boa parte dos CRMs desta lista é AGPL — reveja a seção do topo
  antes de prometer implantação a cliente.

### Dados de casa e do servidor para os agentes

As categorias [internet das coisas](SELFHOSTED.md#internet-das-coisas-iot),
[analytics](SELFHOSTED.md#analytics-e-métricas-de-uso) e
[utilitários de rede](SELFHOSTED.md#utilitários-de-rede) produzem dado que hoje ninguém lê.
Combinado com os agentes sempre ativos do
[awesome-llm-apps](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)
e com um gateway como o
[bifrost](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md),
vira briefing diário do que aconteceu na sua infraestrutura.

- **Esforço:** médio
- **Comece pequeno:** um alerta útil vale mais que um painel bonito que ninguém abre.

### Hospedar a própria biblioteca

As categorias [wikis](SELFHOSTED.md#wikis),
[gestão de conhecimento](SELFHOSTED.md#gestão-de-conhecimento) e
[favoritos](SELFHOSTED.md#favoritos-e-compartilhamento-de-links) resolvem, com software
pronto, parte do que este repositório faz à mão. Vale a comparação honesta: um wiki dá
busca, edição web e acesso de qualquer lugar; o repositório dá versionamento, análise
escrita por agente e ideias cruzadas.

- **Esforço:** baixo para testar
- **Provável conclusão:** os dois, com papéis distintos — o repositório para curadoria com
  análise, um serviço de favoritos para capturar link no celular e alimentar a `INBOX.md`.
- **O que não abrir mão:** o formato de texto puro versionado. É o que permite ao agente
  ler, cruzar e reescrever a coleção.

## Para começar hoje

Se for fazer uma coisa só: **escolha o SaaS que mais incomoda e procure o substituto nesta
lista**, filtrando por licença permissiva e descartando os 66 abandonados. É a única ideia
daqui que já se paga na primeira semana.

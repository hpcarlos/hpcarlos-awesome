---
titulo: "Huly Platform — alternativa self-hosted a Jira, Linear, Slack e Notion"
nome: Huly
tldr: "Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion."
licenca: "EPL-2.0"
alerta: "o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada"
url: https://github.com/hcengineering/platform
tipo: projeto
categorias: [web, devops]
tags: [self-hosted, gestao-de-projetos, crm, chat, typescript, svelte]
status: novo
nota: 4
adicionado: 2026-08-29
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md, 2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md]
---

# Huly Platform — alternativa self-hosted a Jira, Linear, Slack e Notion

## Resumo

Suíte de trabalho que junta num único aplicativo o que normalmente vive em quatro
assinaturas: gestão de projetos no estilo Linear/Jira, chat de equipe no estilo Slack,
wiki colaborativo no estilo Notion, mais CRM, RH e um sistema de acompanhamento de
candidatos (ATS). É o código-fonte do produto Huly, aberto sob EPL-2.0. Frontend em Svelte,
backend em Node/TypeScript, monorepo gerido pelo Rush, e uma infraestrutura de apoio
robusta: MongoDB, Elasticsearch e MinIO, tudo levantado por Docker Compose.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o tipo de peça que substitui várias assinaturas de uma vez — a ideia central da
coleção de [software auto-hospedado](2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md),
concentrada num produto só. Para quem toca projeto e equipe, trocar Jira + Slack + Notion
por uma coisa que você controla é atraente; a questão é o custo de operar.

## Pontos-chave

- **⚠️ O serviço hospedado foi descontinuado.** O caminho agora é auto-hospedar (o projeto
  aponta o `huly-selfhost` para isso) ou migrar para terceiro. Na prática: a conveniência de
  "só assinar" acabou, e o que sobra é o software para rodar você mesmo — que é o que
  interessa a esta coleção, mas muda a conta de esforço.
- **⚠️ Stack de apoio pesada.** MongoDB, Elasticsearch e MinIO não são leves: pedem memória
  e atenção de operação. Isto não roda num Raspberry Pi de canto — é candidato a servidor de
  verdade, com a base de proxy e backup que a ideia "montar a base antes dos serviços" do
  [`IDEIAS-SELFHOSTED.md`](../IDEIAS-SELFHOSTED.md) já previa.
- **Licença EPL-2.0** — copyleft fraco, de arquivo: permite uso comercial e combinação com
  código proprietário, desde que modificações nos arquivos da própria EPL sejam
  compartilhadas. Bem menos restritiva que as AGPL que dominam a lista de self-hosted;
  para produto próprio, é das licenças confortáveis.
- **Amplitude é o argumento e o risco.** Cobrir projetos, chat, wiki, CRM, RH e ATS num só
  lugar elimina a integração entre ferramentas — e concentra tudo num sistema só, que
  precisa ser bom em seis coisas. Vale testar qual módulo é forte e qual é acessório antes
  de apostar a operação inteira.
- **Instalação não é de clicar e usar:** submódulos de git, Rush, build do monorepo e um
  ajuste no arquivo de hosts (`huly.local`). E-mail não funciona localmente, então
  recuperação de senha e notificação exigem configuração extra.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Sede de operação de um negócio pequeno, sem assinaturas** — Huly para projetos, chat e
  wiki; o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) na ponta do
  atendimento por WhatsApp. Um cuida do time por dentro, o outro do cliente por fora, e
  nenhuma mensalidade de SaaS no meio. _Esforço: alto._
- **Piloto de um módulo só** — em vez de adotar a suíte inteira, subir o Huly e usar apenas
  a gestão de projetos por um mês, medindo se substitui o que você usa hoje. Se o módulo
  mais importante não convencer, os outros cinco não salvam. _Esforço: médio._
- **Referência de arquitetura de monorepo grande** — mesmo sem adotar, o uso do Rush para
  orquestrar um monorepo Svelte + Node desse tamanho é material de estudo, no mesmo espírito
  em que o [lobehub](2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md) serve
  de referência de organização. _Esforço: baixo._
- **Entrada curada na coleção de self-hosted** — este é o tipo de projeto que a lista do
  [awesome-selfhosted](2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)
  cataloga em bloco, mas aqui ele ganhou análise individual. É um bom teste de quando promover
  um item da coleção derivada a achado próprio: quando você realmente pensa em adotá-lo.
  _Esforço: baixo._

## Notas

```bash
git submodule init && git submodule update
npm install -g @microsoft/rush
rush install && rush build
cd ./dev/ && rush docker:build && rush docker:up
# depois: adicionar "huly.local" ao /etc/hosts e abrir http://huly.local:8087
```

- Node v20.11.0 exigido de forma estrita; Docker e Docker Compose obrigatórios.
- As dependências vêm de GitHub Packages, o que exige autenticação — ponto onde a instalação
  costuma travar na primeira tentativa.
- Para produção, o projeto recomenda o repositório `huly-selfhost` em vez de montar à mão a
  partir daqui.
- **Antes de investir tempo:** decidir qual dos módulos (projetos, chat, wiki, CRM, RH, ATS)
  é o que você realmente quer. Adotar a suíte inteira "porque veio junto" é como isso vira
  peso morto.

# 💡 Ideias de projeto

Projetos que dá para construir **cruzando** os achados deste repositório. Cada achado tem
sua própria seção "Ideias de projeto"; aqui ficam as ideias que combinam dois ou mais.

Formato de cada ideia: o que é, quais achados alimentam, esforço estimado e o primeiro
passo concreto.

<!-- O Claude atualiza este arquivo sempre que um achado novo destrava ou reforça uma ideia. -->

## Em aberto

### Vitrine web dos achados

Site estático gerado a partir do front-matter de `achados/`: cartões por categoria,
filtro por tag e por nota, busca no cliente. A parte de dados é trivial — os scripts já
leem tudo. O que costuma sair feio é a interface, e é aí que entra o
[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md):
`shape` para planejar, `craft` para construir, `audit` e `polish` para tirar a cara de
template. Publicável no GitHub Pages.

- **Alimenta:** impeccable
- **Esforço:** médio
- **Primeiro passo:** `scripts/exportar.py` que despeja todos os achados num `dados.json`
  (o `lib_achados.py` já entrega os objetos prontos) — o site consome isso.
- **Bônus:** é um projeto frontend real para testar o impeccable de verdade, em vez de
  avaliar a ferramenta por captura de tela.

### Bancada barata de frontend

O par mais óbvio dos dois primeiros achados: o
[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
derruba o custo por token roteando o agente para tiers gratuitos, e o
[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
garante que o resultado não saia com cara de template. Juntos viram um ambiente de
geração de interface que dá para deixar rodando sem medo da fatura.

- **Alimenta:** OmniRoute + impeccable
- **Esforço:** baixo
- **Primeiro passo:** `npm i -g omniroute && omniroute setup`, depois
  `omniroute run claude` num projeto que já tenha o impeccable instalado.
- **O que medir:** se a qualidade do código cai ao trocar o modelo forte pelo gratuito.
  Se cair muito, a combinação certa é modelo barato para construir e modelo forte só no
  `/impeccable critique`.
- **Cuidado:** parte dos tiers gratuitos é marcada como ToS-flagged pelo próprio
  OmniRoute — vale escolher quais usar antes de automatizar.

### Micro-SaaS de IA com o encanamento resolvido

Os três achados se encaixam num produto só. O
[saas-starter-kit](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
entrega contas, times, convites, papéis e audit log; o
[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
entrega inferência barata com fallback entre provedores; o
[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
evita que o resultado tenha a cara de todo mundo que clonou o mesmo boilerplate. Sobra
construir a única parte que importa: o que o produto faz de fato.

- **Alimenta:** saas-starter-kit + OmniRoute + impeccable
- **Esforço:** médio
- **Primeiro passo:** clonar o kit, subir com `docker-compose up -d` e `npx prisma db push`,
  e conferir o que o módulo de cobrança realmente faz hoje — é a peça mais incerta.
- **Ordem que faz sentido:** encanamento (kit) → identidade visual (`/impeccable init`,
  enquanto trocar tema ainda é barato) → inferência (OmniRoute) → o produto.
- **Custo escondido:** o kit depende de Svix, Retraced, Stripe e um SMTP. Decidir cedo o
  que vale pagar e o que dá para trocar por alternativa auto-hospedada.

### CRM de WhatsApp com IA que não custa por resposta

O [wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) já traz um
assistente de resposta que fala com OpenAI/Anthropic. Como o
[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
expõe exatamente um endpoint compatível com a OpenAI, trocar a URL base deve bastar para
o assistente rodar em tiers gratuitos. É a combinação de menor esforço entre os achados
até agora — e a que tem cliente pagante mais óbvio do outro lado.

- **Alimenta:** wacrm + OmniRoute
- **Esforço:** baixo
- **Primeiro passo:** subir o wacrm em modo local e apontar a variável de URL base da IA
  para `http://localhost:20128/v1`, conferindo se ele respeita URL customizada ou se
  assume o endereço oficial no código.
- **Antes de qualquer código:** confirmar que a conta na WhatsApp Business API é viável
  (verificação da empresa, modelos de mensagem, custo por conversa). É a Meta, e não a
  stack, que decide se o projeto existe.

### Método antes de escala — e qual método

Há agora duas coleções de skills concorrentes no repositório, com filosofias opostas:
[mattpocock/skills](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
aposta em peças pequenas que você compõe e edita, enquanto
[addyosmani/agent-skills](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
entrega um sistema de 24 skills com portões de verificação obrigatórios. Em vez de
escolher por autoridade, use o próprio `IDEIAS.md` como campo de prova: passe as ideias
daqui por `/spec` e `/plan` de um lado, e por `to-spec`, `to-tickets` e `grill-me` do
outro, e compare o que sai.

- **Alimenta:** mattpocock/skills + addyosmani/agent-skills
- **Esforço:** médio (baixo, se testar só uma)
- **Primeiro passo:** instalar as duas (`claude plugins install mattpocock-skills` e
  `/plugin marketplace add addyosmani/agent-skills`) e rodar cada uma sobre a ideia da
  vitrine web.
- **O que medir:** tempo até a primeira tarefa executável, retrabalho, tokens gastos e
  quanto do resultado você teve de reescrever.
- **Teste de fogo:** se metade das ideias daqui não sobreviver ao `grill-me` ou ao
  `/spec`, o método funcionou.
- **Atalho de retorno imediato:** mesmo sem decidir nada, as sete checklists do Addy
  (definition of done, segurança, acessibilidade, performance) já valem coladas num
  projeto seu.

### Escritório de agentes que cabe no bolso

O [munder-difflin](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)
orquestra vários CLIs de agente em paralelo — e paralelismo multiplica consumo de tokens.
Apontar todos para o [OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
e dar a eles o método comum das
[skills](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
transforma uma curiosidade cara num experimento defensável.

- **Alimenta:** munder-difflin + OmniRoute + mattpocock/skills
- **Esforço:** médio
- **Primeiro passo:** rodar uma tarefa real com dois agentes e anotar tempo, qualidade e
  custo. Sem esse número, a discussão sobre multiagente vira opinião.
- **Ordem:** método (skills) → custo (OmniRoute) → orquestração (munder-difflin). Na ordem
  inversa, o resultado é caro e desorganizado ao mesmo tempo.

### Fechar a conta dos agentes

Duas fontes de dado que ninguém cruza: o
[mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
acompanha gasto por execução e guarda auditoria; o
[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
registra uso por provedor em SQLite. Juntas respondem "quanto custou cada projeto, em qual
modelo, em que semana" — pergunta que apareceu no primeiro achado de gateway e segue sem
resposta. Ambos usam SQLite, então o cruzamento é uma consulta, não uma integração.

- **Alimenta:** mission-control + OmniRoute + bifrost
- **Esforço:** médio
- **Primeiro passo:** subir os dois localmente e olhar os dois esquemas de banco lado a
  lado antes de escrever qualquer código.
- **Atalho melhor:** o [bifrost](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
  já expõe métricas em Prometheus. Se o painel for para valer, começar por ele evita
  reinventar coleta de métrica em cima de SQLite.
- **Cuidado:** o mission-control é alpha declarado e o esquema pode mudar entre versões —
  não construa nada rígido em cima dele agora.

### Decidir o gateway de uma vez

Já são três gateways na coleção resolvendo o mesmo problema, e a escolha não é de gosto:
[bifrost](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
é Apache 2.0 e roda sobre as suas próprias chaves, com governança e Prometheus;
[OmniRoute](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)
é MIT e vive de tiers gratuitos instáveis;
[sub2api](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)
redistribui assinaturas e o próprio README avisa que isso pode violar termos de serviço.

- **Regra prática:** bifrost onde houver cliente ou produto; OmniRoute para experimento
  pessoal; sub2api só como leitura de arquitetura.
- **Esforço:** baixo — é decisão, não construção.
- **Primeiro passo:** `npx -y @maximhq/bifrost`, apontar um projeto existente para
  `localhost:8080` e ver se a troca é mesmo só de URL base.
- **Ganho colateral:** decidido isso, todo achado futuro de IA já nasce sabendo por onde
  suas chamadas passam.

### Digest do que entrou

CLI que lê os achados adicionados na última semana e monta um resumo — por e-mail, ou
como issue no próprio repositório. Reaproveita `scripts/buscar.py --desde`, que já
filtra por data. Vale mais quando houver volume; fica anotado para depois.

- **Alimenta:** (nenhum achado específico ainda)
- **Esforço:** baixo
- **Primeiro passo:** `python3 scripts/buscar.py --desde $(date -d '7 days ago' +%F)`

## Em andamento

_(mova para cá quando começar a construir)_

## Feitas ou descartadas

_(com uma linha dizendo o que aconteceu — descartar com motivo também é resultado)_

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

- **Alimenta:** impeccable + OpenDesign + graphify
- **Esforço:** médio
- **Primeiro passo:** `scripts/exportar.py` que despeja todos os achados num `dados.json`
  (o `lib_achados.py` já entrega os objetos prontos) — o site consome isso.
- **A peça que faltava:** esta ideia ficou parada por falta de vontade de desenhar
  interface. O [OpenDesign](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)
  gera o protótipo a partir do JSON, o impeccable faz o acabamento. Agora é executável.
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
- **Atalho que dispensa o experimento:** com o
  [task-observer](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)
  instalado, o dado se coleta sozinho — qual skill é acionada, em que situação, onde você
  teve de corrigir o agente. Medição passiva em vez de bake-off agendado, que é o tipo de
  tarefa que nunca acontece.
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

- **Regra prática:** para produto sério, a escolha é entre bifrost e
  [Portkey](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)
  (ambos permissivos, sobre suas chaves) — Portkey se você precisa de guardrails na frente do
  usuário, bifrost se quer tudo aberto sem empurrão para a nuvem paga. OmniRoute para
  experimento pessoal; sub2api só como leitura de arquitetura.
- **Esforço:** baixo — é decisão, não construção.
- **Primeiro passo:** `npx -y @maximhq/bifrost`, apontar um projeto existente para
  `localhost:8080` e ver se a troca é mesmo só de URL base.
- **Ganho colateral:** decidido isso, todo achado futuro de IA já nasce sabendo por onde
  suas chamadas passam.
- **Atualização:** com quatro gateways catalogados, o bake-off que importa é bifrost × Portkey,
  medido com o seu próprio tráfego. A tabela comparativa está no achado do Portkey.

### Um cinto de segurança para agentes que agem

O [Vibe-Trading](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)
resolveu, por necessidade, o problema que todo agente com poder de ação tem: kill-switch
que zera tudo ao receber HALT, teto de exposição, limite diário de operações, confirmação
em dois fatores para liberar mandato, conta-sombra espelhando a execução e livro de
auditoria encadeado por hash. Nada disso é específico de finanças — vale para agente que
manda e-mail, altera banco ou publica em nome de alguém. O
[mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
diz que se deve tratar agente como entrada não confiável; este mostra como.

- **Alimenta:** Vibe-Trading + mission-control
- **Esforço:** médio
- **Primeiro passo:** ler o módulo de contenção do Vibe-Trading e escrever a versão mínima
  — um limite de ações por execução e um log append-only — no primeiro projeto seu em que
  o agente faz algo irreversível.
- **Por que agora:** metade da coleção já é sobre dar mais autonomia a agentes. Esta é a
  única linha que fala em como tirar essa autonomia de volta quando algo dá errado.
- **Confirmação independente:** o [claude-ads](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)
  chega ao mesmo desenho em outro domínio — leitura por padrão, mudança como rascunho,
  escrita atrás de aprovação, idempotência e verificação. Dois projetos sem relação
  convergindo é um bom indício de que esse é *o* padrão, e não gosto de um autor.
- **Terceira confirmação, e a mais forte:** o
  [cloudflare-os](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)
  põe isso na arquitetura em vez de na política — agente e app **nascem sem acesso a nada** e
  cada recurso é concedido explicitamente, com isolamento de rede por padrão. Vindo de uma
  empresa de infraestrutura, é o desenho mais maduro do padrão na coleção.
- **A regra a levar para os seus projetos:** comece negando tudo. É mais fácil conceder um
  acesso que faltou do que descobrir qual acesso sobrou.

### Fazer o agente declarar o que não sabe

O [claude-ads](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)
calcula a própria **cobertura de evidência**: quanto do que precisava ser olhado foi de
fato olhado. Abaixo de 60%, ele se declara insuficiente em vez de entregar conclusão
bonita. Isso ataca o defeito mais comum de relatório gerado por IA — soar convincente sem
sustentação — e não tem nada de específico de anúncios.

- **Alimenta:** claude-ads + addyosmani/agent-skills
- **Esforço:** médio
- **Primeiro passo:** escolher uma tarefa sua de análise (revisão de código, leitura de
  contrato, auditoria de infra) e exigir da saída duas linhas: o que foi verificado e o que
  ficou fora. Só isso já muda a conversa.
- **Encaixe:** a regra de "verificação inegociável" das skills do Addy é a mesma ideia pelo
  lado do processo; aqui ela vira número.

### Auditar as bases antes de escolher uma

A coleção acumulou três candidatas a fundação de projeto — o
[saas-starter-kit](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md),
o [wacrm](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) e o
[mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
— e nenhuma evidência sobre a qualidade interna delas além do README de cada uma. O
[react-doctor](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)
resolve isso em uma tarde: as três são React.

- **Alimenta:** react-doctor + graphify + saas-starter-kit + wacrm + mission-control
- **Esforço:** baixo
- **Primeiro passo:** clonar as três e rodar `npx react-doctor@latest` em cada uma.
- **A outra metade:** o [graphify](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)
  com `--code-only` desenha a arquitetura de cada uma sem custo de LLM. Um responde "qual é
  a mais sadia", o outro "qual eu consigo entender" — e a segunda pergunta costuma decidir
  mais que a primeira.
- **O que fazer com o resultado:** virar um achado deste repositório, com os números lado a
  lado. É a primeira medição própria da coleção — até aqui tudo veio de README alheio.
- **Ganho:** escolher base por evidência em vez de por contagem de estrelas, que aliás
  nunca consegui verificar nesta sessão.

### O padrão determinístico

Quatro achados da coleção resolvem análise de código do mesmo jeito, e não é coincidência:
[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
(59 detectores de anti-padrão visual),
[react-doctor](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)
(regras de estado e render),
[graphify](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)
(AST com tree-sitter) e o detector do
[claude-ads](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)
(pontuação determinística). Some-se o
[archify](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md),
que rejeita auto-layout para que o mesmo JSON dê sempre o mesmo desenho. Todos fazem a
**detecção e a renderização sem modelo**, deixando o LLM só para interpretar e corrigir.
É barato, reproduzível e não alucina achado — e, no caso do archify, torna o resultado
versionável em git.

- **Alimenta:** impeccable + react-doctor + graphify + claude-ads + archify
- **Esforço:** baixo (é princípio de projeto, não construção)
- **Onde aplicar:** em qualquer verificação sua que hoje é feita por prompt. Se a regra
  puder ser escrita como código, escreva como código — o agente entra depois.
- **Teste:** pegue uma checagem que você pede ao agente com frequência e tente reescrevê-la
  como script. Se der, ela vira gratuita e confiável.

### Checklist de primeira execução

Padrão que só aparece com volume: quase toda ferramenta de agente desta coleção manda algo
para fora ou pede confiança cega na instalação. Telemetria ligada por padrão no
[react-doctor](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md),
no [camofox-browser](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)
e no [OpenDesign](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md);
`curl | sudo bash` no [sub2api](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)
e script remoto no [lobehub](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md);
credenciais padrão a trocar no [mission-control](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md).
Nenhum deles é malicioso — é o costume da categoria.

- **Alimenta:** metade da coleção
- **Esforço:** baixo
- **O checklist:** desligar telemetria antes do primeiro uso sério; ler o script de
  instalação antes de dar `sudo`; trocar toda credencial gerada; conferir o que sai da
  máquina quando a ferramenta processa código de cliente.
- **Onde guardar:** como seção fixa no `CLAUDE.md`, para todo achado novo de ferramenta já
  nascer com essa verificação feita.
- **Por que importa:** rodar essas coisas em código de terceiro sem checar é o tipo de
  descuido que só aparece depois.

### Medir por conta própria, de uma vez

Vinte e um achados e nenhuma medição sua: toda avaliação até agora veio do README de quem
escreveu a ferramenta, e as contagens de estrelas nunca puderam ser verificadas nesta
sessão. O [ponytail](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)
é a melhor porta de entrada para mudar isso: promete ~54% menos código com metodologia
publicada e datada, o que dá para reproduzir.

- **Alimenta:** ponytail + react-doctor + graphify (as três com número mensurável)
- **Esforço:** médio
- **Primeiro passo:** duas tarefas reais suas, rodadas com e sem a skill, anotando linhas
  de código, tokens e tempo.
- **Por que este e não outro:** o próprio projeto declara onde o ganho é quase nulo (código
  já enxuto) e que modelos que raciocinam muito podem gastar mais token deliberando. Quem
  admite o limite costuma estar medindo direito.
- **O resultado vira achado** deste repositório, com o seu número — o primeiro que não sai
  de README alheio.

### Podar a coleção de skills

Toda coleção de skills cresce por adição e nunca por remoção. Hoje já são cinco fontes
instaláveis nesta biblioteca — mattpocock, addyosmani, ponytail, impeccable, react-doctor —
e nenhuma evidência sobre quais são de fato acionadas. O
[task-observer](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)
registra o uso real, o que dá a base para remover em vez de acumular.

- **Alimenta:** task-observer + todas as skills instaladas
- **Esforço:** baixo (a coleta é passiva; o trabalho é revisar)
- **Primeiro passo:** instalar, trabalhar normalmente por duas semanas e só então abrir o
  registro.
- **A pergunta que interessa:** quais skills nunca apareceram? Essas são candidatas a sair,
  e cada uma que sai devolve contexto e atenção.
- **Aceleração possível:** se você adotar o
  [gstack](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md),
  que cobre o sprint inteiro (plano, review, QA, deploy), boa parte das skills soltas vira
  redundância de uma vez. A poda deixa de ser item a item e passa a ser "o que o gstack não
  faz melhor?".
- **Cuidado:** o observador só vale se a revisão acontecer. Sem isso, é mais um arquivo
  crescendo sem leitor — vale agendá-la junto com a manutenção do repositório.

### Pensar como adversário antes de expor

O [awesome-selfhosted](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)
convida a hospedar dezenas de serviços; a skill de
[red-team](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)
ensina a olhar para eles como um atacante olharia — kill-chain, alvos críticos, pontos de
estrangulamento. Antes de abrir uma porta na internet, vale saber por onde ela seria
arrombada. Uso puramente defensivo, sobre a sua própria infraestrutura.

- **Alimenta:** red-team + awesome-selfhosted
- **Esforço:** médio
- **Primeiro passo:** ler a metodologia da skill e transformar "alvos críticos" e "pontos
  de estrangulamento" num checklist do que proteger primeiro no seu servidor.
- **Limite claro:** isto é sobre o que é seu. Apontar qualquer técnica para sistema alheio
  sem autorização escrita é crime — a própria skill abre com esse aviso.
- **Liga com a base:** casa com "montar a base antes dos serviços" em
  [`IDEIAS-SELFHOSTED.md`](IDEIAS-SELFHOSTED.md) — proxy, backup e agora endurecimento.

### Escolher o construtor de conversa por dependência

Três construtores de chatbot entraram na coleção em sequência, e a escolha entre eles não é
de recursos — é de **laço**:
[ChatbotX](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)
cobre seis redes com chave de IA própria e sem intermediário;
[ZernFlow](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)
cobre sete, mas cada mensagem passa pela API paga da Zernio;
[OpenReply](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)
faz só comment-to-DM no Instagram, sem dependência e com uma fração da infraestrutura.

- **Alimenta:** ChatbotX + ZernFlow + OpenReply
- **Esforço:** baixo — é decisão, não construção
- **Regra prática:** só Instagram → OpenReply; operação multicanal séria → ChatbotX;
  ZernFlow só se algum canal exclusivo dele for indispensável.
- **O que nenhum resolve:** a janela de 24 horas da Meta. Ela limita disparo nos três, porque
  é regra da plataforma, não do software.
- **Complemento obrigatório:** se o fluxo tiver nó de IA respondendo ao cliente, ele passa por
  um gateway com guardrail ([Portkey](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)) —
  não é opcional quando o modelo fala com público.

### O micro-SaaS brasileiro, agora completo

A ideia do micro-SaaS de IA está no arquivo desde os primeiros achados, mas faltava uma peça
que nenhum boilerplate estrangeiro entrega: **nota fiscal brasileira**. A
[Spedy](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)
fecha esse buraco por API, entre receber o pagamento e estar em dia com o fisco.

- **Alimenta:** saas-starter-kit + Stripe + Spedy + um gateway de IA
- **Esforço:** médio
- **Primeiro passo:** montar a planilha de decisão fiscal. São três caminhos catalogados —
  [Focus NFe](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)
  (API paga, maior cobertura de documento e município),
  [Spedy](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)
  (SaaS que automatiza a partir das vendas) e
  [ACBr](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)
  (biblioteca livre, custo zero e trabalho seu). Quatro linhas: custo no seu volume,
  documentos necessários, municípios envolvidos, tempo de integração. É decisão de uma tarde,
  e ela costuma se arrastar por meses.
- **Ordem de montagem:** contas e assinatura (starter kit) → pagamento (Stripe) → nota
  (Spedy) → só então o produto em si.
- **O que verificar antes de amarrar:** como exportar o histórico de notas. Emissão fiscal é
  obrigação sua, não do fornecedor — precisa haver plano B se o serviço sair do ar.
- **A outra ponta:** a [Polp](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)
  resolve a entrada de dado bancário (Open Finance já categorizado) como a Spedy resolve a
  saída fiscal. Com as duas, o encanamento brasileiro de um produto financeiro está inteiro
  catalogado — falta a ideia de produto, não a infraestrutura.
- **Cuidado extra do lado da Polp:** dado bancário de terceiro exige consentimento pelo fluxo
  do Open Finance e cai sob a LGPD. É o único item da coleção cujo risco principal é legal, e
  não técnico ou de licença.
- **Há concorrente catalogado:** o [Malvo](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)
  ocupa o mesmo espaço da Polp, com foco B2B. Antes de escolher, mande as mesmas quatro
  perguntas para os dois — preço, cobertura de bancos, acurácia com o seu extrato e gestão de
  consentimento — e compare as respostas. Fornecedor de infraestrutura sem comparação é
  decisão no escuro.

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

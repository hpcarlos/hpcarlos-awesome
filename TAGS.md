# Tags

111 tag(s) em 43 achado(s) · gerado por `scripts/indexar.py` — não edite à mão.

Volte para a lista completa: [README.md](README.md).

## Mais usadas

[`agentes`](#agentes) (17) · [`claude-code`](#claude-code) (16) · [`mcp`](#mcp) (13) · [`self-hosted`](#self-hosted) (13) · [`skills`](#skills) (13) · [`typescript`](#typescript) (10) · [`llm`](#llm) (7) · [`nextjs`](#nextjs) (7) · [`api`](#api) (5) · [`automacao`](#automacao) (5) · [`brasil`](#brasil) (5) · [`frontend`](#frontend) (5) · [`cli`](#cli) (4) · [`crm`](#crm) (4) · [`gateway`](#gateway) (4) · [`python`](#python) (4) · [`saas`](#saas) (4) · [`ui`](#ui) (4) · [`dados`](#dados) (3) · [`fiscal`](#fiscal) (3) · [`nodejs`](#nodejs) (3) · [`nota-fiscal`](#nota-fiscal) (3) · [`observabilidade`](#observabilidade) (3) · [`openai-api`](#openai-api) (3) · [`performance`](#performance) (3) · [`react`](#react) (3) · [`referencia`](#referencia) (3) · [`scraping`](#scraping) (3) · [`workflow`](#workflow) (3) · [`bancos`](#bancos) (2)

## agentes

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>
* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## anuncios

* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>

## api

* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## apify

* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>

## apresentacoes

* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>

## arquitetura

* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>

## ast

* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>

## auth

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>

## automacao

* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## automacao-comercial

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>

## backtest

* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>

## bancos

* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>

## billing

* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## boilerplate

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>

## brasil

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>
* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>

## busca

* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>

## catalogo

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>

## chat

* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>

## chatbot

* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

## claude-code

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## cli

* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>

## cloudflare

* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>

## code-review

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)

## componentes

* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>

## cowork

* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>

## crm

* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

## custos

* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>

## dados

* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>

## debug

* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

## delphi

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>

## deploy

* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>

## design

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>

## design-md

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>

## devtools

* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

## diagramas

* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>

## dm

* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>

## documentacao

* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>

## electron

* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>

## exemplos

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>

## fastapi

* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>

## fintech

* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>

## fiscal

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>
* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>

## frontend

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

## gateway

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## gestao-de-projetos

* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>

## go

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## grafos

* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>

## guardrails

* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>

## inspiracao

* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## instagram

* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>

## integracao

* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>

## lazarus

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>

## lgpl

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>

## licencas

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>

## linter

* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>

## llm

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>
* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## marketing

* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>

## mcp

* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>

## meta-skill

* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>

## mitre-attack

* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## multiagente

* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>

## navegador

* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## nextjs

* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

## nodejs

* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## nota-fiscal

* 📦 [ACBr](https://www.projetoacbr.com.br/) - Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida. `LGPL-2.1+` ★★★★☆ [análise](achados/2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md)<br><sub>⚠️ nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ</sub>
* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>

## observabilidade

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>

## omnichannel

* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>

## open-finance

* ⚙️ [Malvo](https://malvo.io/) - Camada de dados do Open Finance brasileiro: agrega, normaliza e categoriza transações com IA para PFM, ERP, crédito e scoring. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-malvo-camada-de-dados-de-open-finance-enriquecidos-por-ia.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>
* ⚙️ [Polp](https://www.polp.com.br/) - API brasileira de Open Finance que conecta qualquer banco e devolve o extrato já categorizado, com recorrências e insights prontos para usar. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-polp-api-de-open-finance-com-dados-bancarios-enriquecidos-po.md)<br><sub>⚠️ serviço pago com dado financeiro de terceiros: exige consentimento do titular e cuidado com LGPD</sub>

## openai-api

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>

## orquestracao

* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>

## padroes

* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## pentest

* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## performance

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

## playwright

* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## postgres

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>

## prisma

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>

## privacidade

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>

## prompt-engineering

* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## prompts

* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## prototipo

* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>

## python

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>

## qa

* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>

## rag

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>

## react

* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

## red-team

* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## redes-sociais

* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>

## referencia

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>
* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## saas

* ⚙️ [Focus NFe](https://focusnfe.com.br/) - API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-focus-nfe-api-rest-para-emissao-de-documentos-fiscais-brasil.md)<br><sub>⚠️ serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração</sub>
* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* ⚙️ [Spedy](https://spedy.com.br/) - SaaS brasileiro que emite NF-e, NFS-e e NFC-e no automático a partir das suas vendas, com API própria e mais de 70 integrações. `própria (SaaS)` ★★★★☆ [análise](achados/2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)<br><sub>⚠️ serviço pago por nota, não software aberto; o site não abriu nesta sessão — resumo por busca externa</sub>
* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## sandbox

* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>

## scraping

* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## seguranca

* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>

## seguranca-de-agentes

* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>

## seguranca-ofensiva

* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## self-hosted

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>
* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* 🛠 [ChatbotX](https://github.com/ChatbotXIO/ChatbotX) - Plataforma completa de chatbot para 6 redes, e-mail e webchat, com agentes de IA por chave própria, CRM, disparo e servidor MCP. `MIT + comercial` ★★★★☆ [análise](achados/2026-09-02-chatbotx-plataforma-omnichannel-de-chatbot-com-ia-self-hoste.md)<br><sub>⚠️ licença dupla: recursos enterprise ficam na comercial, e a stack self-hosted exige DevOps de verdade</sub>
* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## servidores

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>

## shadcn

* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>

## skills

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>

## sqlite

* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>

## supabase

* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

## svelte

* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>

## tdd

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)

## trading

* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>

## tree-sitter

* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>

## typescript

* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>
* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>

## ui

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>
* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## ux

* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## voz

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>

## whatsapp

* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>

## workers

* 🛠 [cloudflare-os](https://github.com/cloudflare/cloudflare-os) - Plataforma interna da Cloudflare, aberta: agentes e mini-apps que nascem sem acesso a nada e só ganham recursos por apresentação explícita. `Apache-2.0` ★★★★☆ [análise](achados/2026-09-03-cloudflare-os-plataforma-de-agentes-com-acesso-por-capacidad.md)<br><sub>⚠️ early access com arestas assumidas, não aceita contribuição externa e a produção depende da infraestrutura Cloudflare</sub>

## workflow

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)

## yagni

* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>

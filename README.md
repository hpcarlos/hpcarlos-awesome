Achados
===

[![Licença: CC BY 4.0](https://img.shields.io/badge/licen%C3%A7a-CC_BY_4.0-lightgrey)](LICENSE)
[![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

Biblioteca pessoal de coisas boas encontradas na internet — projetos, artigos,
ferramentas, papers e vídeos. Cada item traz uma frase dizendo o que é, a licença, uma
nota de relevância e um link para a **análise completa**: resumo em português, pontos-chave,
ressalvas e ideias concretas de projeto.

**Legenda**

`MIT` `Apache-2.0` `própria` — licença declarada pelo projeto;
★★★★☆ — relevância para mim, de 1 a 5;
[análise] — leva ao achado completo, com pontos-chave e ideias de projeto;
⚠️ — ressalva que muda a decisão de adotar (licença restritiva, dependência cara,
risco de termos de uso, software em alpha).

🛠 projeto · ⚙️ ferramenta · 📄 artigo · 📦 biblioteca · 📚 paper · 🎥 vídeo · 🔗 outro

<!-- INICIO:ESTATISTICAS -->
**36** achados · **8** categorias · **95** tags · atualizado em 2026-09-02

| tipo | qtd. |  | status | qtd. |
| --- | ---: | --- | --- | ---: |
| ferramenta | 21 |  | novo | 36 |
| projeto | 11 |  |  |  |
| outro | 4 |  |  |  |

Categorias: `design` · `devops` · `engenharia` · `financas` · `ia` · `negocios` · `seguranca` · `web`
<!-- FIM:ESTATISTICAS -->

## Conteúdo

<!-- INICIO:SUMARIO -->
- [Inteligência artificial](#inteligência-artificial) <sub>25</sub>
    - [Ferramentas](#ferramentas) <sub>17</sub>
    - [Projetos](#projetos) <sub>6</sub>
    - [Outros](#outros) <sub>2</sub>
- [Web](#web) <sub>14</sub>
    - [Ferramentas](#ferramentas-1) <sub>6</sub>
    - [Projetos](#projetos-1) <sub>6</sub>
    - [Outros](#outros-1) <sub>2</sub>
- [Engenharia de software](#engenharia-de-software) <sub>13</sub>
    - [Ferramentas](#ferramentas-2) <sub>9</sub>
    - [Projetos](#projetos-2) <sub>3</sub>
    - [Outros](#outros-2) <sub>1</sub>
- [Infraestrutura e DevOps](#infraestrutura-e-devops) <sub>7</sub>
    - [Ferramentas](#ferramentas-3) <sub>4</sub>
    - [Projetos](#projetos-3) <sub>2</sub>
    - [Outros](#outros-3) <sub>1</sub>
- [Design](#design) <sub>6</sub>
    - [Ferramentas](#ferramentas-4) <sub>4</sub>
    - [Outros](#outros-4) <sub>2</sub>
- [Negócios](#negócios) <sub>4</sub>
- [Segurança](#segurança) <sub>2</sub>
- [Finanças](#finanças) <sub>1</sub>
<!-- FIM:SUMARIO -->

- [Adicionados recentemente](#adicionados-recentemente)
- [Como isto funciona](#como-isto-funciona)

<!-- INICIO:LISTA -->
## Inteligência artificial

### Ferramentas

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>
* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

### Projetos

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

### Outros

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## Web

### Ferramentas

* ⚙️ [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta. `MIT` ★★★★☆ [análise](achados/2026-08-30-agent-reach-camada-que-da-acesso-a-redes-e-web-a-agentes-de.md)<br><sub>⚠️ acessar plataforma com login por navegador pode banir a conta; o próprio projeto manda usar conta descartável</sub>
* ⚙️ [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso. `MIT` ★★★★☆ [análise](achados/2026-08-31-apify-mcp-server-milhares-de-scrapers-prontos-como-ferrament.md)<br><sub>⚠️ o servidor é open source, mas rodar os Actors é pago por uso e exige conta na Apify</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

### Projetos

* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

### Outros

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>
* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## Engenharia de software

### Ferramentas

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [gstack](https://github.com/garrytan/gstack) - Kit de 23 skills que dá ao Claude Code o sprint inteiro: office-hours, plano, design, review, QA em navegador real, ship e deploy monitorado. `MIT` ★★★★★ [análise](achados/2026-08-29-gstack-23-skills-que-transformam-o-claude-code-num-time-de-e.md)<br><sub>⚠️ amplo e opinativo; instala navegador Chromium, classificador ML de 22MB e telemetria opt-in — leia o que roda antes</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* ⚙️ [graphify](https://github.com/Graphify-Labs/graphify) - Transforma código, docs, PDFs e esquemas num grafo consultável: AST determinístico em ~40 linguagens, com LLM só para a parte textual. `Apache-2.0 e MIT` ★★★★☆ [análise](achados/2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)<br><sub>⚠️ a v1 pública ainda não saiu (o desenvolvimento corre no branch v8) e há plataforma comercial paralela</sub>
* ⚙️ [ponytail](https://github.com/DietrichGebert/ponytail) - Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada. `MIT` ★★★★☆ [análise](achados/2026-08-28-ponytail-skill-que-faz-o-agente-escrever-menos-codigo.md)<br><sub>⚠️ os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto</sub>
* ⚙️ [react-doctor](https://github.com/millionco/react-doctor) - Audita projeto React em estado, efeitos, performance, arquitetura, segurança e acessibilidade — na análise estática e no runtime do Chrome. `MIT` ★★★★☆ [análise](achados/2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md)<br><sub>⚠️ telemetria ligada por padrão; o trace de runtime captura o navegador inteiro, com URLs e caminhos</sub>
* ⚙️ [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill que assiste às suas sessões, anota padrões e correções, e devolve melhorias para as outras skills — inclusive para si mesma. `CC-BY-4.0` ★★★★☆ [análise](achados/2026-08-28-task-observer-one-skill-to-rule-them-all-a-skill-que-melhora.md)<br><sub>⚠️ para poucas skills, a memória embutida do assistente já resolve — quem diz isso é o próprio projeto</sub>
* ⚙️ [react-scan](https://github.com/aidenybai/react-scan) - Destaca na tela os componentes React que re-renderizam sem precisar, sem exigir mudança no código — basta uma tag de script. `MIT` ★★★☆☆ [análise](achados/2026-08-28-react-scan-mostra-o-que-esta-re-renderizando-em-react.md)<br><sub>⚠️ o próprio projeto recomenda o react-doctor no lugar; não é para rodar em produção</sub>

### Projetos

* 🛠 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 115 aplicações de LLM prontas e executáveis — agentes, times, RAG, memória, voz e interfaces geradas — num repositório só, sob Apache-2.0. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-awesome-llm-apps-115-aplicacoes-de-llm-com-codigo-completo.md)<br><sub>⚠️ são demonstrações: dependem de chave de API e não trazem contenção nem tratamento de produção</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* 🛠 [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto. `MIT` ★★★☆☆ [análise](achados/2026-08-31-rome-o-so-agentico-que-persiste-software-nao-so-conversa.md)<br><sub>⚠️ preview em evolução ativa; exige Docker e a nuvem própria ainda está fechada</sub>

### Outros

* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## Infraestrutura e DevOps

### Ferramentas

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails. `MIT` ★★★★☆ [análise](achados/2026-09-01-portkey-ai-gateway-gateway-de-llm-com-guardrails-e-observabi.md)<br><sub>⚠️ open core: cache semântico, otimização de provedor e templates ficam na versão paga</sub>

### Projetos

* 🛠 [Huly](https://github.com/hcengineering/platform) - Suíte de trabalho auto-hospedável num app só: gestão de projetos, chat, CRM, RH e recrutamento — alternativa a Jira, Linear, Slack e Notion. `EPL-2.0` ★★★★☆ [análise](achados/2026-08-29-huly-platform-alternativa-self-hosted-a-jira-linear-slack-e.md)<br><sub>⚠️ o serviço hospedado foi descontinuado; agora é auto-hospedar, e a stack (Mongo, Elastic, MinIO) é pesada</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

### Outros

* 🔗 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Catálogo de 1.255 softwares livres para hospedar você mesmo, com licença e stack declaradas e os projetos abandonados sinalizados. `CC-BY-SA-3.0` ★★★★★ [análise](achados/2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)<br><sub>⚠️ 305 dos projetos são AGPL ou equivalente — decisivo se a ideia for produto fechado</sub>

## Design

### Ferramentas

* ⚙️ [archify](https://github.com/tt-a1i/archify) - Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só. `MIT` ★★★★☆ [análise](achados/2026-08-28-archify-diagramas-de-arquitetura-deterministicos-a-partir-de.md)<br><sub>⚠️ sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [OpenDesign](https://github.com/nexu-io/open-design) - Faz o agente entregar protótipo, deck, dashboard, imagem e vídeo em vez de só código — com 151 design systems e exportação real. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)<br><sub>⚠️ telemetria ligada por padrão; imagem e vídeo consomem API paga por conta própria, e ainda está em 0.10</sub>
* ⚙️ [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar. `própria (serviço web)` ★★★★☆ [análise](achados/2026-08-29-shoogle-buscador-de-componentes-e-blocos-shadcn-ui.md)<br><sub>⚠️ o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes</sub>

### Outros

* 🔗 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara. `própria (coleção)` ★★★★☆ [análise](achados/2026-09-01-awesome-design-md-73-arquivos-design-md-de-produtos-conhecid.md)<br><sub>⚠️ replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém</sub>
* 🔗 [SaaSUI](https://www.saasui.design/) - Galeria de referência com capturas reais de produtos SaaS, organizada por padrão de interface — dashboards, onboarding, preços, formulários. `própria (site)` ★★★☆☆ [análise](achados/2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)<br><sub>⚠️ não consegui abrir o site nesta sessão; resumo baseado em busca externa, não em leitura direta</sub>

## Negócios

* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-09-02-openreply-comentario-do-instagram-vira-dm-automatico-self-ho.md)<br><sub>⚠️ só Instagram; exige app Meta configurado e respeita o teto de 750 DMs/hora e a janela da Meta</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* 🛠 [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat. `MIT` ★★★☆☆ [análise](achados/2026-09-02-zernflow-construtor-visual-de-chatbots-multicanal-alternativ.md)<br><sub>⚠️ depende da API paga da Zernio para mensagens, e o WhatsApp esbarra na janela de 24h da Meta</sub>

## Segurança

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* ⚙️ [red-team](https://www.skills.sh/alirezarezvani/claude-skills/red-team) - Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada. `MIT` ★★★☆☆ [análise](achados/2026-08-28-red-team-skill-de-planejamento-de-simulacao-adversarial-mitr.md)<br><sub>⚠️ uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized</sub>

## Finanças

* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
<!-- FIM:LISTA -->

## Adicionados recentemente

<!-- INICIO:RECENTES -->
* `2026-09-02` [ZernFlow](https://github.com/zernio-dev/zernflow) - Construtor visual de chatbots self-hosted para 7 redes, com CRM, disparo, gotejamento e nó de IA — alternativa aberta ao ManyChat.
* `2026-09-02` [OpenReply](https://github.com/diwenne/openreply) - Alternativa self-hosted ao ManyChat focada num truque só: comentar uma palavra-chave num post dispara um DM automático, via API oficial da Meta.
* `2026-09-01` [Portkey Gateway](https://github.com/portkey-ai/gateway) - Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails.
* `2026-09-01` [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara.
* `2026-08-31` [Rome](https://github.com/rome-os/rome) - Ambiente auto-hospedável onde agentes constroem apps, ações e skills que persistem entre tarefas — memória de software, não só de texto.
* `2026-08-31` [apify-mcp-server](https://github.com/apify/apify-mcp-server) - Servidor MCP oficial da Apify que expõe milhares de scrapers prontos (Actors) ao agente — busca, executa e traz o dado, cobrando por uso.
* `2026-08-30` [agent-reach](https://github.com/Panniantong/agent-reach) - CLI unificada que deixa o agente ler e buscar em Twitter, Reddit, YouTube, GitHub e outras plataformas sem taxa de API — só leitura, nunca posta.
* `2026-08-29` [Shoogle](https://shoogle.dev/) - Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar.
<!-- FIM:RECENTES -->

## Como isto funciona

Mando um link, o Claude lê a página, escreve a análise em português, classifica, cruza com
o que já está aqui e regenera esta lista. O detalhe do fluxo está em
[`CLAUDE.md`](CLAUDE.md).

**Mandar um link novo:** cole a URL em [`INBOX.md`](INBOX.md) e peça *"processa a inbox"*,
ou mande direto na conversa.

**Registrar à mão:**

```bash
python3 scripts/novo.py https://exemplo.com/artigo \
  --titulo "Título" --nome "nome-curto" \
  --tldr "O que é e para que serve, em uma frase." \
  --tipo ferramenta --categorias ia --tags rag,python --nota 4
python3 scripts/indexar.py
```

**Procurar depois:**

```bash
python3 scripts/buscar.py rag --detalhe
python3 scripts/buscar.py --tag python --tipo projeto --nota-min 4
python3 scripts/buscar.py --tags          # todas as tags existentes
```

Veja também [`TAGS.md`](TAGS.md) (mapa de tags) e [`IDEIAS.md`](IDEIAS.md) — projetos que
só existem cruzando mais de um achado.

**Coleções derivadas.** Quando um único achado traz dezenas ou centenas de projetos dentro
dele, o catálogo vai para arquivo próprio, com documento de ideias ao lado:

| Coleção | Catálogo | Ideias |
| --- | --- | --- |
| 115 aplicações de LLM prontas | [`LLM-APPS.md`](LLM-APPS.md) | [`IDEIAS-LLM-APPS.md`](IDEIAS-LLM-APPS.md) |
| 1.255 softwares para auto-hospedar | [`SELFHOSTED.md`](SELFHOSTED.md) | [`IDEIAS-SELFHOSTED.md`](IDEIAS-SELFHOSTED.md) |
| 73 arquivos DESIGN.md de produtos reais | [`DESIGN-MD.md`](DESIGN-MD.md) | [`IDEIAS-DESIGN-MD.md`](IDEIAS-DESIGN-MD.md) |

| Caminho | O que é |
| --- | --- |
| [`achados/`](achados/) | Um Markdown por achado — a fonte da verdade |
| [`INBOX.md`](INBOX.md) | Caixa de entrada para links crus |
| [`IDEIAS.md`](IDEIAS.md) | Ideias que cruzam vários achados |
| [`TAGS.md`](TAGS.md) | Mapa de tags — **gerado** |
| [`scripts/`](scripts/) | `novo.py`, `indexar.py`, `buscar.py` (Python puro, sem deps) |
| [`LLM-APPS.md`](LLM-APPS.md) · [`SELFHOSTED.md`](SELFHOSTED.md) · [`DESIGN-MD.md`](DESIGN-MD.md) | Catálogos das coleções derivadas — **gerados** |
| [`IDEIAS-LLM-APPS.md`](IDEIAS-LLM-APPS.md) · [`IDEIAS-SELFHOSTED.md`](IDEIAS-SELFHOSTED.md) · [`IDEIAS-DESIGN-MD.md`](IDEIAS-DESIGN-MD.md) | Ideias de cada coleção derivada |
| [`dados/`](dados/) | Fontes tabulares das coleções derivadas |
| [`modelos/`](modelos/) | Template de achado e workflow de CI opcional |

---

<sub>Esta página é gerada por `scripts/indexar.py` a partir de `achados/` — edite os
achados, não os blocos entre marcadores. Conteúdo sob CC BY 4.0; cada projeto listado
mantém a própria licença.</sub>

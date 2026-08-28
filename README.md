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
**15** achados · **8** categorias · **48** tags · atualizado em 2026-08-28

| tipo | qtd. |  | status | qtd. |
| --- | ---: | --- | --- | ---: |
| ferramenta | 8 |  | novo | 15 |
| projeto | 6 |  |  |  |
| outro | 1 |  |  |  |

Categorias: `design` · `devops` · `engenharia` · `financas` · `ia` · `negocios` · `seguranca` · `web`
<!-- FIM:ESTATISTICAS -->

## Conteúdo

<!-- INICIO:SUMARIO -->
- [Inteligência artificial](#inteligência-artificial) <sub>13</sub>
    - [Ferramentas](#ferramentas) <sub>8</sub>
    - [Projetos](#projetos) <sub>4</sub>
    - [Outros](#outros) <sub>1</sub>
- [Infraestrutura e DevOps](#infraestrutura-e-devops) <sub>4</sub>
- [Engenharia de software](#engenharia-de-software) <sub>4</sub>
- [Web](#web) <sub>4</sub>
- [Negócios](#negócios) <sub>2</sub>
- [Design](#design) <sub>1</sub>
- [Finanças](#finanças) <sub>1</sub>
- [Segurança](#segurança) <sub>1</sub>
<!-- FIM:SUMARIO -->

- [Adicionados recentemente](#adicionados-recentemente)
- [Como isto funciona](#como-isto-funciona)

<!-- INICIO:LISTA -->
## Inteligência artificial

### Ferramentas

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

### Projetos

* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

### Outros

* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## Infraestrutura e DevOps

* ⚙️ [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)<br><sub>⚠️ modelo open core: cluster e recursos avançados ficam na edição paga</sub>
* ⚙️ [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só. `MIT` ★★★★☆ [análise](achados/2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)<br><sub>⚠️ alpha declarado; troque as credenciais padrão antes de expor na rede</sub>
* ⚙️ [OmniRoute](https://github.com/diegosouzapw/OmniRoute) - Gateway local que expõe um endpoint OpenAI para centenas de provedores de LLM, com fallback automático quando a cota grátis acaba. `MIT` ★★★★☆ [análise](achados/2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md)<br><sub>⚠️ parte dos tiers gratuitos é marcada como sensível a termos de uso</sub>
* 🛠 [sub2api](https://github.com/Wei-Shaw/sub2api) - Gateway em Go que revende acesso a assinaturas de IA como chaves de API, com cobrança e painel — o próprio README avisa que viola termos de uso. `LGPL-3.0` ★★☆☆☆ [análise](achados/2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md)<br><sub>⚠️ o próprio README avisa que o uso pode violar os termos dos provedores</sub>

## Engenharia de software

* ⚙️ [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - 24 skills que cobrem o ciclo inteiro — spec, plano, TDD, review, segurança, performance e deploy — com 8 comandos e provas obrigatórias. `MIT` ★★★★★ [análise](achados/2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)<br><sub>⚠️ instalar skill avulsa não traz as checklists de `references/`</sub>
* ⚙️ [mattpocock/skills](https://github.com/mattpocock/skills) - Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review. `MIT` ★★★★★ [análise](achados/2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
* 🛠 [munder-difflin](https://github.com/chaitanyagiri/munder-difflin) - App de desktop que roda vários CLIs de agente como um escritório: memória compartilhada, roteamento de tarefas e kanban, com avatares em pixel art. `MIT` ★★★☆☆ [análise](achados/2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)<br><sub>⚠️ protótipo; a arte em pixel tem licença própria com exigência de crédito</sub>
* 🔗 [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar. `GPL-3.0 declarada` ★★★☆☆ [análise](achados/2026-08-23-system-prompts-and-models-of-ai-tools-coletanea-de-prompts-d.md)<br><sub>⚠️ conteúdo de terceiros sem origem informada; não reutilize os textos</sub>

## Web

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
* 🛠 [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais. `própria` ★★★☆☆ [análise](achados/2026-08-27-lobehub-plataforma-de-orquestracao-de-agentes-de-ia.md)<br><sub>⚠️ LobeHub Community License, com restrições de uso comercial</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>
* ⚙️ [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados. `MIT` ★★☆☆☆ [análise](achados/2026-08-28-camofox-browser-navegador-anti-deteccao-como-servidor-para-a.md)<br><sub>⚠️ contornar proteção anti-bot costuma violar os termos do site; envia telemetria por padrão</sub>

## Negócios

* ⚙️ [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório. `MIT` ★★★☆☆ [análise](achados/2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md)<br><sub>⚠️ não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada</sub>
* 🛠 [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta. `MIT` ★★★☆☆ [análise](achados/2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md)<br><sub>⚠️ depende de conta aprovada na WhatsApp Business API, com custo por conversa</sub>

## Design

* ⚙️ [impeccable](https://github.com/pbakaus/impeccable) - Ensina agentes de código a fazer interfaces com cara decidida: 23 comandos e 59 detectores de anti-padrões visuais. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)

## Finanças

* 🛠 [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria. `MIT` ★★★☆☆ [análise](achados/2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)<br><sub>⚠️ executa ordens reais com dinheiro seu, por decisão de LLM — comece e permaneça em papel até provar o contrário</sub>

## Segurança

* 🛠 [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) - Boilerplate Next.js de SaaS B2B com autenticação, SSO/SAML, times, convites, audit log e webhooks já prontos. `Apache-2.0` ★★★★☆ [análise](achados/2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)<br><sub>⚠️ webhooks, audit log e cobrança dependem de serviços externos pagos</sub>
<!-- FIM:LISTA -->

## Adicionados recentemente

<!-- INICIO:RECENTES -->
* `2026-08-28` [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Agente de IA que pesquisa, faz backtest e envia ordens reais em 13+ corretoras, com kill-switch, limites e trilha de auditoria.
* `2026-08-28` [claude-ads](https://github.com/AgriciDaniel/claude-ads) - Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório.
* `2026-08-28` [camofox-browser](https://github.com/jo-inc/camofox-browser) - Servidor REST de navegador headless com fingerprint falsificado no nível do Firefox, feito para agentes navegarem sem serem barrados.
* `2026-08-27` [lobehub](https://github.com/lobehub/lobehub) - Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais.
* `2026-08-27` [bifrost](https://github.com/maximhq/bifrost) - Gateway Apache 2.0 em Go: um endpoint OpenAI para 23+ provedores, com chaves virtuais, limite de gasto, cache semântico e métricas Prometheus.
* `2026-08-23` [system-prompts](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Coletânea de prompts de sistema de mais de 30 ferramentas de IA comerciais — valiosa para estudar padrões, arriscada para copiar.
* `2026-08-23` [mission-control](https://github.com/builderz-labs/mission-control) - Painel self-hosted para operar agentes: despacho de tarefas, sessões, custo por execução, auditoria, cron e webhooks num lugar só.
* `2026-08-22` [wacrm](https://github.com/ArnasDon/wacrm) - CRM auto-hospedável para WhatsApp: caixa de entrada compartilhada, funil kanban, disparos e automações sobre a API oficial da Meta.
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

| Caminho | O que é |
| --- | --- |
| [`achados/`](achados/) | Um Markdown por achado — a fonte da verdade |
| [`INBOX.md`](INBOX.md) | Caixa de entrada para links crus |
| [`IDEIAS.md`](IDEIAS.md) | Ideias que cruzam vários achados |
| [`TAGS.md`](TAGS.md) | Mapa de tags — **gerado** |
| [`scripts/`](scripts/) | `novo.py`, `indexar.py`, `buscar.py` (Python puro, sem deps) |
| [`modelos/`](modelos/) | Template de achado e workflow de CI opcional |

---

<sub>Esta página é gerada por `scripts/indexar.py` a partir de `achados/` — edite os
achados, não os blocos entre marcadores. Conteúdo sob CC BY 4.0; cada projeto listado
mantém a própria licença.</sub>

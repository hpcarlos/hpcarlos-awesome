Aplicações de LLM prontas
===

Catálogo das aplicações que vivem dentro do
[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps), de Shubham Saboo —
agentes, times de agentes, RAG, memória, voz e interfaces geradas, todos com código
completo e executável. Cada item aponta direto para a pasta do projeto.

> **Como ler esta lista.** Ela é diferente do [README](README.md): lá, cada item passou por
> análise individual, com pontos-chave, ressalvas e ideias próprias. Aqui são 115 aplicações
> de um repositório só, catalogadas em bloco — as descrições vêm do nome e da categoria de
> cada uma, **não de leitura do código de cada pasta**. Trate como mapa para achar o
> exemplo certo, não como avaliação de qualidade individual.

**Licença e origem**

Tudo aqui é Apache-2.0 e mora no mesmo repositório, mantido por Shubham Saboo. As
aplicações usam modelos variados (Claude, GPT, Gemini, DeepSeek, Llama, Qwen) e boa parte
depende de chave de API — algumas rodam local. O único item externo está marcado como tal.

<!-- INICIO:ESTATISTICAS -->
**115** aplicações em **15** categorias · todas sob Apache-2.0, no mesmo repositório · atualizado em 2026-08-28
<!-- FIM:ESTATISTICAS -->

## Conteúdo

<!-- INICIO:SUMARIO -->
- [Skills de agente](#-skills-de-agente) <sub>6</sub>
- [Agentes para começar](#-agentes-para-começar) <sub>12</sub>
- [Agentes avançados](#-agentes-avançados) <sub>22</sub>
- [Agentes sempre ativos](#️-agentes-sempre-ativos) <sub>2</sub>
- [Times de agentes](#-times-de-agentes) <sub>13</sub>
- [Agentes de voz](#️-agentes-de-voz) <sub>5</sub>
- [Interfaces geradas por agente](#️-interfaces-geradas-por-agente) <sub>7</sub>
- [Agentes que jogam](#-agentes-que-jogam) <sub>3</sub>
- [Agentes com MCP](#️-agentes-com-mcp) <sub>6</sub>
- [RAG](#-rag) <sub>21</sub>
- [Aplicações com memória](#-aplicações-com-memória) <sub>6</sub>
- [Conversar com…](#-conversar-com) <sub>6</sub>
- [Otimização de contexto e token](#-otimização-de-contexto-e-token) <sub>2</sub>
- [Ajuste fino de modelo](#-ajuste-fino-de-modelo) <sub>2</sub>
- [Cursos rápidos de framework](#-cursos-rápidos-de-framework) <sub>2</sub>
<!-- FIM:SUMARIO -->

- [Como usar isto](#como-usar-isto)

<!-- INICIO:LISTA -->
## 🧩 Skills de agente

* [Project Graveyard](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard) - Skill que registra e analisa projetos abandonados, para entender por que morreram.
* [Scope Creep Detector](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/scope-creep-detector) - Skill que detecta quando o escopo de uma tarefa está inchando além do combinado.
* [Commit Archaeologist](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/commit-archaeologist) - Skill que escava o histórico de commits para explicar por que o código chegou onde chegou.
* [Dependency Doctor](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/dependency-doctor) - Skill que diagnostica a árvore de dependências: o que está obsoleto, duplicado ou sobrando.
* [Advisor Orchestrator Worker](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/advisor-orchestrator-worker) - Skill que implementa o padrão conselheiro-orquestrador-executor entre agentes.
* [Self-Improving Agent Skills](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/self-improving-agent-skills) - Skills que se reescrevem a partir do resultado das próprias execuções.

## 🌱 Agentes para começar

* [AI Blog to Podcast Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_blog_to_podcast_agent) - Converte um post de blog em episódio de podcast narrado.
* [AI Breakup Recovery Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_breakup_recovery_agent) - Agente de apoio conversacional para término de relacionamento.
* [AI Data Analysis Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_data_analysis_agent) - Analisa um conjunto de dados e responde perguntas sobre ele em linguagem natural.
* [AI Medical Imaging Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_medical_imaging_agent) - Interpreta imagens médicas — demonstração de visão, não ferramenta clínica.
* [AI Meme Generator Agent (Browser)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_meme_generator_agent_browseruse) - Gera memes controlando o navegador, com browser-use.
* [AI Music Generator Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_music_generator_agent) - Gera trechos musicais a partir de descrição em texto.
* [AI Travel Agent (Local & Cloud)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_travel_agent) - Monta roteiro de viagem, com versão local e versão em nuvem.
* [Gemini Multimodal Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/multimodal_ai_agent) - Agente multimodal com Gemini, combinando texto e imagem.
* [Mixture of Agents](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/mixture_of_agents) - Combina respostas de vários modelos para produzir uma resposta melhor.
* [xAI Finance Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/xai_finance_agent) - Agente de análise financeira usando modelos da xAI.
* [OpenAI Research Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/openai_research_agent) - Agente de pesquisa construído sobre o SDK da OpenAI.
* [Web Scraping AI Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/web_scraping_ai_agent) - Extrai dados de páginas web guiado por instrução em linguagem natural.

## 🚀 Agentes avançados

* [AI Home Renovation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent) - Planeja reforma doméstica com geração de imagem do resultado.
* [DevPulse AI](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/devpulse_ai) - Inteligência de sinais para times de desenvolvimento, com vários agentes.
* [AI Deep Research Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_deep_research_agent) - Pesquisa profunda sobre um tema, com várias rodadas de busca e síntese.
* [AI VC Due Diligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team) - Time de agentes que faz diligência de investimento sobre uma empresa.
* [AI Research Planner & Executor](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api) - Separa o planejamento da pesquisa da sua execução, com a API do Gemini.
* [AI Consultant Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_consultant_agent) - Agente que responde como consultor de negócios sobre um problema apresentado.
* [AI System Architect Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_system_architect_r1) - Propõe arquitetura de sistema a partir de requisitos, usando modelo de raciocínio.
* [AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent) - Orientação financeira pessoal a partir da situação descrita pelo usuário.
* [AI Movie Production Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_movie_production_agent) - Desenvolve conceito de filme: roteiro, elenco e produção.
* [AI Investment Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_investment_agent) - Compara ações e monta tese de investimento.
* [Earnings Call Analyst Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent) - Analisa teleconferência de resultados e extrai o que importa.
* [AI Health & Fitness Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_health_fitness_agent) - Monta plano de treino e alimentação a partir do perfil informado.
* [AI Product Launch Intelligence Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/product_launch_intelligence_agent) - Analisa lançamentos de produto de concorrentes.
* [AI Fraud Investigation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent) - Investiga indícios de fraude em transações e documentos.
* [AI Journalist Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_journalist_agent) - Apura e escreve matéria jornalística sobre um tema.
* [AI Mental Wellbeing Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_mental_wellbeing_agent) - Time de agentes de apoio ao bem-estar mental — demonstração, não terapia.
* [AI Meeting Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_meeting_agent) - Prepara pauta e material de apoio para uma reunião.
* [AI Self-Evolving Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_self_evolving_agent) - Agente que ajusta as próprias instruções conforme os resultados.
* [AI Sales Intelligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team) - Time que pesquisa prospects e prepara abordagem comercial.
* [AI Social Media News and Podcast Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agents) - Acompanha notícias e transforma em conteúdo para redes e podcast.
* [Openwork - Open Browser Automation Agent](https://github.com/accomplish-ai/openwork) - Automação de navegador de código aberto — projeto externo, ligado a partir da lista. <sub>projeto externo</sub>
* [Trust-Gated Multi-Agent Research Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/trust_gated_agent_team) - Time de pesquisa em que cada passo passa por uma trava de confiança.

## 🛰️ Agentes sempre ativos

* [Always-on Hacker News Briefing Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/always_on_agents/always_on_hn_briefing_agent) - Agente que roda continuamente e entrega resumo do Hacker News.
* [Release Radar Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/always_on_agents/release_radar_agent) - Monitora lançamentos de projetos e avisa o que mudou.

## 🤝 Times de agentes

* [AI Competitor Intelligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_competitor_intelligence_agent_team) - Time que monitora e compara concorrentes.
* [AI Finance Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team) - Time de agentes para análise financeira dividida por especialidade.
* [AI Game Design Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_game_design_agent_team) - Time que desenvolve conceito de jogo: mecânica, narrativa e arte.
* [AG2 Adaptive Research Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ag2_adaptive_research_team) - Time de pesquisa que adapta a própria composição, com o framework AG2.
* [AI Legal Agent Team (Cloud & Local)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_legal_agent_team) - Time que analisa documento jurídico, com versão local e em nuvem.
* [AI Recruitment Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_recruitment_agent_team) - Time que triagem currículos e prepara entrevista.
* [AI Real Estate Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_real_estate_agent_team) - Time que pesquisa imóveis e compara oportunidades.
* [AI Services Agency (CrewAI)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_services_agency) - Simula uma agência de serviços inteira com CrewAI.
* [AI Teaching Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_teaching_agent_team) - Time que monta trilha de estudo e ensina um assunto.
* [Multimodal Coding Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_coding_agent_team) - Time de programação que aceita imagem além de texto como entrada.
* [Multimodal Design Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_design_agent_team) - Time de design que trabalha a partir de referências visuais.
* [Multimodal UI/UX Feedback Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team) - Time que critica interface a partir de captura de tela.
* [AI Travel Planner Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_travel_planner_agent_team) - Time que planeja viagem dividindo voo, hospedagem e roteiro.

## 🗣️ Agentes de voz

* [AI Audio Tour Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/ai_audio_tour_agent) - Gera narração de audioguia para um lugar ou museu.
* [Customer Support Voice Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/customer_support_voice_agent) - Atendimento ao cliente por voz, com resposta falada.
* [Insurance Claim Live Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/insurance_claim_live_agent_team) - Time que conduz abertura de sinistro por voz, ao vivo.
* [Voice RAG Agent (OpenAI SDK)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents/voice_rag_openaisdk) - RAG com entrada e saída por voz, sobre o SDK da OpenAI.
* [OpenSource Voice Dictation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/voice_ai_agents) - Ditado por voz com modelos abertos.

## 🖼️ Interfaces geradas por agente

* [Generative UI Starter Project](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/generative-ui-starter-project) - Ponto de partida para interface gerada pelo agente em tempo de execução.
* [AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-financial-coach-agent) - Orientação financeira com interface montada pelo próprio agente.
* [AI Dashboard Canvas Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-dashboard-canvas-agent) - Agente que monta painel de dados como tela editável.
* [AI MCP App Builder](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-mcp-app-builder) - Constrói aplicação a partir de servidores MCP disponíveis.
* [MCP Apps Generative UI Showcase](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/mcp-apps-generative-ui-showcase) - Vitrine de interfaces geradas a partir de aplicações MCP.
* [AI Shadcn Component Generator](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-shadcn-component-generator) - Gera componentes shadcn/ui a partir de descrição.
* [AI Deep Research Agent (UI)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/generative_ui_agents/ai-deep-research-agent) - Pesquisa profunda com interface gerada para acompanhar o processo.

## 🎮 Agentes que jogam

* [AI 3D Pygame Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1) - Agente que programa jogo 3D em Pygame com modelo de raciocínio.
* [AI Chess Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_chess_agent) - Dois agentes jogando xadrez um contra o outro.
* [AI Tic-Tac-Toe Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent) - Agentes disputando jogo da velha — exemplo mínimo de confronto.

## ♾️ Agentes com MCP

* [Browser MCP Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/browser_mcp_agent) - Agente que controla o navegador através de servidor MCP.
* [GitHub MCP Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/github_mcp_agent) - Agente que opera repositórios do GitHub via MCP.
* [Notion MCP Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/notion_mcp_agent) - Agente que lê e escreve no Notion via MCP.
* [AI Travel Planner MCP Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/ai_travel_planner_mcp_agent_team) - Time de planejamento de viagem consumindo várias ferramentas MCP.
* [Multi-MCP Agent Router](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/multi_mcp_agent_router) - Roteia a tarefa para o servidor MCP certo entre vários disponíveis.
* [OpenAI Remote MCP Tool Bridge](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/mcp_ai_agents/openai_remote_mcp_bridge) - Ponte que expõe ferramentas MCP remotas para a API da OpenAI.

## 📀 RAG

* [Agentic RAG with Embedding Gemma](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/agentic_rag_embedding_gemma) - RAG com agente usando o modelo de embedding Gemma.
* [Agentic RAG with Reasoning](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/agentic_rag_with_reasoning) - RAG em que o agente raciocina sobre o que buscar antes de responder.
* [AI Blog Search (RAG)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/ai_blog_search) - Busca semântica sobre uma coleção de posts de blog.
* [Autonomous RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/autonomous_rag) - RAG que decide sozinho quando e o que recuperar.
* [Contextual AI RAG Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/contextualai_rag_agent) - RAG sobre a plataforma da Contextual AI.
* [Corrective RAG (CRAG)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/corrective_rag) - RAG que avalia e corrige a própria recuperação quando ela vem ruim.
* [Typed Agentic RAG with Pydantic AI](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/agentic_typed_rag_pydanticai) - RAG com saída tipada e validada, usando Pydantic AI.
* [Deepseek Local RAG Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/deepseek_local_rag_agent) - RAG rodando inteiramente local com modelos DeepSeek.
* [Gemini Agentic RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/gemini_agentic_rag) - RAG com agente usando modelos Gemini.
* [Hybrid Search RAG (Cloud)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/hybrid_search_rag) - Combina busca por palavra-chave e por vetor, em nuvem.
* [Llama 3.1 Local RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/llama3.1_local_rag) - RAG local com Llama 3.1.
* [Local Hybrid Search RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/local_hybrid_search_rag) - Busca híbrida rodando na própria máquina, sem serviço externo.
* [Multimodal Agentic RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/multimodal_agentic_rag) - RAG que recupera e raciocina sobre texto e imagem.
* [Local RAG Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/local_rag_agent) - Agente de RAG local, sem depender de API paga.
* [RAG-as-a-Service](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag-as-a-service) - RAG empacotado como serviço consumível por API.
* [RAG Agent with Cohere](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_agent_cohere) - RAG usando os modelos e o reranker da Cohere.
* [Basic RAG Chain](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_chain) - A cadeia mínima de RAG — o ponto de partida para entender o resto.
* [RAG with Database Routing](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_database_routing) - Escolhe entre várias bases qual consultar para cada pergunta.
* [Vision RAG](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/vision_rag) - Recuperação sobre imagens, respondendo perguntas visuais.
* [RAG Failure Diagnostics Clinic](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/rag_failure_diagnostics_clinic) - Diagnostica por que um RAG está respondendo errado.
* [Knowledge Graph RAG with Citations](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/rag_tutorials/knowledge_graph_rag_citations) - RAG sobre grafo de conhecimento, com citação da fonte de cada afirmação.

## 💾 Aplicações com memória

* [AI ArXiv Agent with Memory](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/ai_arxiv_agent_memory) - Agente de leitura de artigos que lembra o que já foi lido.
* [AI Travel Agent with Memory](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/ai_travel_agent_memory) - Planejador de viagem que retém preferências entre conversas.
* [Llama3 Stateful Chat](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/llama3_stateful_chat) - Conversa com estado persistente sobre Llama 3.
* [LLM App with Personalized Memory](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/llm_app_personalized_memory) - Aplicação que constrói memória personalizada por usuário.
* [Local ChatGPT Clone with Memory](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/local_chatgpt_with_memory) - Clone local de chat com memória, sem enviar dado para fora.
* [Multi-LLM Application with Shared Memory](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_apps_with_memory_tutorials/multi_llm_memory) - Vários modelos compartilhando a mesma memória.

## 💬 Conversar com…

* [Chat with GitHub (GPT & Llama3)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_github) - Conversa com um repositório do GitHub.
* [Chat with Gmail](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_gmail) - Conversa com a própria caixa de e-mail.
* [Chat with PDF (GPT & Llama3)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_pdf) - Conversa com um PDF — o exemplo canônico de RAG.
* [Chat with Research Papers (ArXiv)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_research_papers) - Conversa com artigos científicos do arXiv.
* [Chat with Substack](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_substack) - Conversa com o arquivo de uma newsletter do Substack.
* [Chat with YouTube Videos](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/chat_with_X_tutorials/chat_with_youtube_videos) - Conversa com a transcrição de vídeos do YouTube.

## 🎯 Otimização de contexto e token

* [Toonify Token Optimization](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_optimization_tools/toonify_token_optimization) - Reduz o consumo de token de uma aplicação.
* [Headroom Context Optimization](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_optimization_tools/headroom_context_optimization) - Gerencia a folga da janela de contexto para não estourar o limite.

## 🔧 Ajuste fino de modelo

* [Gemma 3 Fine-tuning](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning) - Ajuste fino do Gemma 3 para uma tarefa específica.
* [Llama 3.2 Fine-tuning](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/llm_finetuning_tutorials/llama3.2_finetuning) - Ajuste fino do Llama 3.2, com Unsloth.

## 🧑‍🏫 Cursos rápidos de framework

* [Google ADK Crash Course](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course) - Curso rápido do Agent Development Kit do Google.
* [OpenAI Agents SDK Crash Course](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/openai_sdk_crash_course) - Curso rápido do SDK de agentes da OpenAI.
<!-- FIM:LISTA -->

## Como usar isto

As ideias de projeto a partir destas aplicações estão em
[`IDEIAS-LLM-APPS.md`](IDEIAS-LLM-APPS.md) — inclusive as que cruzam com os achados da
lista principal.

Para encontrar algo aqui, a busca do repositório não cobre este arquivo (ela lê `achados/`);
use a busca do próprio GitHub ou `grep`:

```bash
grep -i "rag" LLM-APPS.md
grep -i "voz\|voice" LLM-APPS.md
```

Para regenerar a lista depois de editar `dados/llm-apps.tsv`:

```bash
python3 scripts/indexar_llm_apps.py
python3 scripts/indexar_llm_apps.py --conferir   # só verifica
```

---

<sub>Lista gerada por `scripts/indexar_llm_apps.py` a partir de `dados/llm-apps.tsv`. O
conteúdo original é do awesome-llm-apps (Apache-2.0); as descrições em português são
deste repositório.</sub>

Software para hospedar você mesmo
===

Catálogo do [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted):
software livre que você roda no seu próprio servidor em vez de assinar como serviço. De
CMS a CRM, de streaming a monitoramento, de e-mail a painel de casa inteligente.

> **Como ler esta lista.** Ela é diferente do [README](README.md), onde cada item passou por
> análise individual. Aqui são 1.255 projetos importados em bloco: os títulos das categorias
> estão em português, mas **as descrições permanecem no original em inglês** — traduzir mais
> de mil frases à mão levaria semanas, e reescrevê-las sem ler cada projeto seria inventar.
> O que interessa mais nesta lista já vem estruturado: **licença**, **stack** e o aviso de
> projeto abandonado. Trate como mapa para achar candidato, não como avaliação individual.

**Legenda**

`MIT` `AGPL-3.0` — licença declarada pelo projeto; <sub>Docker/Go</sub> — o que é preciso
para rodar; ⚠️ — projeto que a fonte marca como **não mantido**, ou de **copyleft forte**
(AGPL e afins), em que oferecer o software como serviço em rede obriga a disponibilizar o
código-fonte das suas modificações. Isso não é problema para uso próprio — é decisivo se a
ideia for construir produto fechado em cima.

<!-- INICIO:ESTATISTICAS -->
**1255** projetos em **84** categorias · atualizado em 2026-08-30

Licenças mais comuns: `MIT` 353 · `AGPL-3.0` 299 · `GPL-3.0` 223 · `Apache-2.0` 133 · `GPL-2.0` 101 · `BSD-3-Clause` 36

⚠️ **66** marcados pela fonte como não mantidos · **305** sob copyleft forte (AGPL e afins)
<!-- FIM:ESTATISTICAS -->

## Conteúdo

<!-- INICIO:SUMARIO -->
- [Acesso remoto](#acesso-remoto) <sub>9</sub>
- [Administração de banco de dados](#administração-de-banco-de-dados) <sub>16</sub>
- [Agenda e contatos](#agenda-e-contatos) <sub>8</sub>
- [Agendamento e reservas](#agendamento-e-reservas) <sub>8</sub>
- [Agricultura comunitária](#agricultura-comunitária) <sub>8</sub>
- [Analytics e métricas de uso](#analytics-e-métricas-de-uso) <sub>32</sub>
- [Arquivamento e preservação digital](#arquivamento-e-preservação-digital) <sub>14</sub>
- [Arquivos — armazenamento de objetos](#arquivos--armazenamento-de-objetos) <sub>5</sub>
- [Arquivos — compartilhamento P2P](#arquivos--compartilhamento-p2p) <sub>7</sub>
- [Arquivos — gerenciadores web](#arquivos--gerenciadores-web) <sub>16</sub>
- [Arquivos — upload rápido](#arquivos--upload-rápido) <sub>29</sub>
- [Automação](#automação) <sub>28</sub>
- [Buscadores](#buscadores) <sub>14</sub>
- [CRM](#crm) <sub>7</sub>
- [Chamados e suporte](#chamados-e-suporte) <sub>12</sub>
- [Comunicação — IRC](#comunicação--irc) <sub>11</sub>
- [Comunicação — SIP e telefonia](#comunicação--sip-e-telefonia) <sub>12</sub>
- [Comunicação — sistemas de mensagem](#comunicação--sistemas-de-mensagem) <sub>37</sub>
- [Comércio eletrônico](#comércio-eletrônico) <sub>21</sub>
- [Controle de estoque](#controle-de-estoque) <sub>9</sub>
- [Controle de tempo](#controle-de-tempo) <sub>10</sub>
- [DNS](#dns) <sub>6</sub>
- [Desenvolvimento — IDEs e ferramentas](#desenvolvimento--ides-e-ferramentas) <sub>12</sub>
- [Desenvolvimento — feature flags](#desenvolvimento--feature-flags) <sub>4</sub>
- [Desenvolvimento — gestão de APIs](#desenvolvimento--gestão-de-apis) <sub>13</sub>
- [Desenvolvimento — gestão de projetos](#desenvolvimento--gestão-de-projetos) <sub>36</sub>
- [Desenvolvimento — localização e tradução](#desenvolvimento--localização-e-tradução) <sub>4</sub>
- [Desenvolvimento — low code](#desenvolvimento--low-code) <sub>9</sub>
- [Desenvolvimento — testes](#desenvolvimento--testes) <sub>3</sub>
- [Diversos](#diversos) <sub>74</sub>
- [Documentos — e-books](#documentos--e-books) <sub>13</sub>
- [Documentos — repositórios e bibliotecas digitais](#documentos--repositórios-e-bibliotecas-digitais) <sub>6</sub>
- [Documentos — sistemas de biblioteca](#documentos--sistemas-de-biblioteca) <sub>3</sub>
- [E-mail — clientes web](#e-mail--clientes-web) <sub>4</sub>
- [E-mail — entrega (MDA)](#e-mail--entrega-mda) <sub>3</sub>
- [E-mail — listas e newsletters](#e-mail--listas-e-newsletters) <sub>10</sub>
- [E-mail — soluções completas](#e-mail--soluções-completas) <sub>17</sub>
- [E-mail — transporte (MTA)](#e-mail--transporte-mta) <sub>9</sub>
- [Encurtadores de URL](#encurtadores-de-url) <sub>9</sub>
- [Enquetes e eventos](#enquetes-e-eventos) <sub>19</sub>
- [Ensino e cursos](#ensino-e-cursos) <sub>15</sub>
- [Favoritos e compartilhamento de links](#favoritos-e-compartilhamento-de-links) <sub>17</sub>
- [Finanças pessoais e orçamento](#finanças-pessoais-e-orçamento) <sub>37</sub>
- [Galerias de fotos](#galerias-de-fotos) <sub>21</sub>
- [Genealogia](#genealogia) <sub>5</sub>
- [Gerenciadores de conteúdo (CMS)](#gerenciadores-de-conteúdo-cms) <sub>41</sub>
- [Gerenciadores de senha](#gerenciadores-de-senha) <sub>7</sub>
- [Gestão de conhecimento](#gestão-de-conhecimento) <sub>7</sub>
- [Gestão de documentos](#gestão-de-documentos) <sub>17</sub>
- [Gestão de eventos e conferências](#gestão-de-eventos-e-conferências) <sub>5</sub>
- [Gestão de mídia](#gestão-de-mídia) <sub>28</sub>
- [Gestão de pessoas (RH)](#gestão-de-pessoas-rh) <sub>3</sub>
- [Groupware](#groupware) <sub>13</sub>
- [IA generativa](#ia-generativa) <sub>13</sub>
- [Internet das coisas (IoT)](#internet-das-coisas-iot) <sub>20</sub>
- [Jogos](#jogos) <sub>19</sub>
- [Jogos — painéis e administração](#jogos--painéis-e-administração) <sub>19</sub>
- [Leitores de feed](#leitores-de-feed) <sub>24</sub>
- [Manufatura](#manufatura) <sub>6</sub>
- [Mapas e GPS](#mapas-e-gps) <sub>17</sub>
- [Notas e editores](#notas-e-editores) <sub>20</sub>
- [Painéis pessoais](#painéis-pessoais) <sub>18</sub>
- [Pastebins](#pastebins) <sub>21</sub>
- [Planejamento de recursos (ERP)](#planejamento-de-recursos-erp) <sub>8</sub>
- [Plataformas de auto-hospedagem](#plataformas-de-auto-hospedagem) <sub>21</sub>
- [Plataformas de blog](#plataformas-de-blog) <sub>15</sub>
- [Proxy](#proxy) <sub>10</sub>
- [Receitas culinárias](#receitas-culinárias) <sub>10</sub>
- [Redes sociais e fóruns](#redes-sociais-e-fóruns) <sub>40</sub>
- [Saúde e exercício](#saúde-e-exercício) <sub>6</sub>
- [Servidores web](#servidores-web) <sub>19</sub>
- [Streaming — multimídia](#streaming--multimídia) <sub>16</sub>
- [Streaming — vídeo](#streaming--vídeo) <sub>14</sub>
- [Streaming — áudio](#streaming--áudio) <sub>27</sub>
- [Suítes de escritório](#suítes-de-escritório) <sub>6</sub>
- [Tarefas e listas](#tarefas-e-listas) <sub>23</sub>
- [Transferência e sincronização de arquivos](#transferência-e-sincronização-de-arquivos) <sub>16</sub>
- [Utilitários de rede](#utilitários-de-rede) <sub>12</sub>
- [Viagens](#viagens) <sub>1</sub>
- [Videoconferência](#videoconferência) <sub>9</sub>
- [Vigilância por vídeo](#vigilância-por-vídeo) <sub>8</sub>
- [Wikis](#wikis) <sub>25</sub>
- [XMPP — clientes web](#xmpp--clientes-web) <sub>3</sub>
- [XMPP — servidores](#xmpp--servidores) <sub>6</sub>
<!-- FIM:SUMARIO -->

- [Como usar isto](#como-usar-isto)

<!-- INICIO:LISTA -->
## Acesso remoto

* [Cardea](https://github.com/hectorm/cardea) - SSH bastion server with access control, session recording, and optional TPM-backed key protection. `EUPL-1.2` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>
* [Engity's Bifröst](https://bifroest.engity.org/) - Highly customizable SSH server with several ways to authorize a user and options where and how to execute a user's session. `Apache-2.0` <sub>Go/Docker</sub>
* [Firezone](https://www.firezone.dev/) - Secure remote access gateway that supports the WireGuard protocol. It offers a Web GUI, 1-line install script, multi-factor auth (MFA), and SSO. `Apache-2.0` <sub>Elixir/Docker</sub>
* [Guacamole](https://guacamole.apache.org) - Clientless remote desktop gateway supporting standard protocols like VNC and RDP. `Apache-2.0` <sub>Java/C</sub>
* [MeshCentral](https://meshcentral.com/) - Run your own web server to remotely manage and control computers on a local network or anywhere on the internet. `Apache-2.0` <sub>Nodejs</sub>
* [ShellHub](https://www.shellhub.io) - Modern SSH server for remotely accessing linux devices via command line (using any SSH client) or web-based user interface (alternative to sshd). `Apache-2.0` <sub>Docker</sub>
* [Sshwifty](https://github.com/nirui/sshwifty) - Sshwifty is a SSH and Telnet connector made for the Web. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Termix](https://docs.termix.site/) - Clientless web-based server management platform with SSH terminal, tunneling, and file editing capabilities. `Apache-2.0` <sub>Docker</sub>
* [Warpgate](https://github.com/warp-tech/warpgate) - Fully transparent SSH, HTTPS, Kubernetes, MySQL and Postgres bastion/PAM that doesn't need additional client-side software. `Apache-2.0` <sub>Rust/Docker</sub>

## Administração de banco de dados

* [Adminer](https://www.adminer.org/) - Database management in a single PHP file. Available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others. `Apache-2.0/GPL-2.0` <sub>PHP</sub>
* [Azimutt](https://azimutt.app) - Visual database exploration made for real world databases (big and messy). Explore your database schema as well as data, document them, extend them and even get analysis and guidelines. `MIT` <sub>Elixir/Nodejs/Docker</sub>
* [Baserow](https://baserow.io/) - Create your own database without technical experience (alternative to Airtable). `MIT` <sub>Docker</sub>
* [Bytebase](https://www.bytebase.com/) - Safe database schema change and version control for DevOps teams, supports MySQL, PostgreSQL, TiDB, ClickHouse, and Snowflake. `MIT` <sub>Docker/K8S/Go</sub>
* [Chartbrew](https://chartbrew.com) - Connect directly to databases and APIs and use the data to create beautiful charts. `MIT` <sub>Nodejs/Docker</sub>
* [ChartDB](https://chartdb.io/) - Database diagrams editor that allows you to visualize and design your DB with a single query. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [CloudBeaver](https://dbeaver.com/) - Manage databases, supports PostgreSQL, MySQL, SQLite and more. A web/hosted version of DBeaver. `Apache-2.0` <sub>Docker</sub>
* [d9](https://d9.webcapsule.io) - Turn SQL databases into secure APIs through an intuitive admin interface. Data platform and headless CMS (fork of Directus). `GPL-3.0` <sub>Nodejs</sub>
* [Databunker](https://databunker.org/) - Network-based, self-hosted, GDPR compliant, secure database for personal data or PII. `MIT` <sub>Docker</sub>
* [Datasette](https://datasette.io/) - Explore and publish data with easy import and export and database management. `Apache-2.0` <sub>Python/Docker</sub>
* [Evidence](https://evidence.dev) - Code-based BI tool. Write reports using SQL and markdown and they render as a website. `MIT` <sub>Nodejs</sub>
* [LibreDB Studio](https://libredb.org) - Browser-based SQL IDE for PostgreSQL, MySQL, Oracle, SQL Server, SQLite, MongoDB and Redis, with an optional AI assistant that writes SQL from natural language (alternative to DataGrip, DBeaver). `MIT` <sub>Docker/K8S</sub>
* [Limbas](https://www.limbas.com/en/) - Database framework for creating database-driven business applications. As a graphical database frontend, it enables the efficient processing of data stocks and the flexible development of comfortable database applications. `GPL-2.0` <sub>PHP</sub>
* [Mathesar](https://mathesar.org/) - Intuitive UI to manage data collaboratively, for users of all technical skill levels. Built on Postgres – connect an existing DB or set up a new one. `GPL-3.0` <sub>Docker/Python</sub>
* [OrcaQ](https://orca-q.com) - Modern database client and IDE for managing, querying, and exploring multiple database types with built-in AI assistant. `MIT` <sub>Nodejs/deb/Docker</sub>
* [StackRender](https://stackrender.io/) - Database schema design and SQL migration generator supporting PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, and Oracle. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Agenda e contatos

* [Baïkal](https://sabre.io/baikal/) - Lightweight CalDAV and CardDAV server based on sabre/dav. `GPL-3.0` <sub>PHP</sub>
* [DAViCal](https://www.davical.org/) - Server for calendar sharing (CalDAV) that uses a PostgreSQL database as a data store. `GPL-2.0` <sub>PHP/deb</sub>
* [Davis](https://github.com/tchapi/davis) - A simple, dockerizable and fully translatable admin interface for sabre/dav based on Symfony 5 and Bootstrap 4, largely inspired by Baïkal. `MIT` <sub>PHP</sub>
* [Keeper.sh](https://keeper.sh/) - Calendar syncing tool that pulls and pushes events between calendar sources and destinations via iCal/ICS or OAuth, with support for anonymized busy/free events. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Manage My Damn Life](https://intri.in/manage-my-damn-life/) - Manage my Damn Life (MMDL) is a self-hosted front end for managing your CalDAV tasks and calendars. `GPL-3.0` <sub>Nodejs/Docker</sub>
* [Radicale](https://radicale.org/) - Simple calendar and contact server with extremely low administrative overhead. `GPL-3.0` <sub>Python/deb</sub>
* [SabreDAV](https://sabre.io/) - Open source CardDAV, CalDAV, and WebDAV framework and server. `MIT` <sub>PHP</sub>
* [Xandikos](https://github.com/jelmer/xandikos) - Open source CardDAV and CalDAV server with minimal administrative overhead, backed by a Git repository. `GPL-3.0` <sub>Python/deb</sub>

## Agendamento e reservas

* [Alf.io](https://alf.io/) - Ticket reservation system. `GPL-3.0` <sub>Java</sub>
* [Cal.diy](https://cal.diy/) - Online appointment scheduling system. `MIT` <sub>Nodejs</sub>
* [Easy!Appointments](https://easyappointments.org/) - Allows your customers to book appointments with you via the web. `GPL-3.0` <sub>PHP</sub>
* [Hi.Events](https://hi.events) - Event management and ticketing platform for conferences, concerts, and more. Offering customizable event pages and embeddable ticket widgets. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LibreBooking](https://librebooking.readthedocs.io/) - Resource scheduling solution offering a flexible, mobile-friendly, and extensible interface for organizations to manage resource reservations. `GPL-3.0` <sub>PHP/Docker</sub>
* [QloApps](https://qloapps.com/) - Customizable and intuitive web-based hotel reservation system and a booking engine. `OSL-3.0` <sub>PHP/Nodejs</sub>
* [Rallly](https://rallly.co) - Create polls to vote on dates and times (alternative to Doodle). `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Seatsurfing](https://seatsurfing.app/) - Webbased app to book seats, desks and rooms for offices. `GPL-3.0` <sub>Docker</sub>

## Agricultura comunitária

* [ACP Admin](https://acp-admin.ch/) - CSA administration. Manage members, subscriptions, deliveries, drop-off locations, member participation, invoices and emails (documentation in French). `MIT` <sub>Ruby</sub>
* [FoodCoopShop](https://www.foodcoopshop.com/) - User-friendly software for food-coops. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Foodsoft](https://foodcoops.net/) - Manage a non-profit food coop (product catalog, ordering, accounting, job scheduling). `AGPL-3.0` <sub>Docker/Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Hive-Pal](https://hivepal.app) - Mobile-first beekeeping management app for tracking hives, inspections, queen records, and equipment with streamlined data entry optimized for field use. `MIT` <sub>Nodejs/Docker</sub>
* [juntagrico](https://juntagrico.org/) - Management platform for community gardens and vegetable cooperatives. `LGPL-3.0` <sub>Python</sub>
* [Open Food Network](https://www.openfoodnetwork.org/) - Online marketplace for local food. It enables a network of independent online food stores that connect farmers and food hubs with individuals and local businesses. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpenOlitor](https://openolitor.org/) - Administration platform for Community Supported Agriculture groups. `AGPL-3.0` <sub>Scala</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [teikei](https://github.com/teikei/teikei) - A web application that maps out community-supported agriculture based on crowdsourced data. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Analytics e métricas de uso

* [ANALOG](https://github.com/orangecoloured/analog) - A minimal analytics tool. Tracks events in a span of 10-30 days. `MIT` <sub>Nodejs/Docker</sub>
* [Aptabase](https://aptabase.com/) - Privacy first and simple analytics for mobile and desktop apps. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [AWStats](http://www.awstats.org/) - Generate statistics from web, streaming, ftp or mail server logfiles. `GPL-3.0` <sub>Perl</sub>
* [Countly Community Edition](https://count.ly) - Real time mobile and web analytics, crash reporting and push notifications platform. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [d8a.tech](https://d8a.tech) - A data collection service that works with your existing Google Analytics setup to capture user activity and send it straight to your own private database. `MIT` <sub>Go/Docker</sub>
* [Daily Stars Explorer](https://emanuelef.github.io/daily-stars-explorer) - Track GitHub repo trends with daily star insights to see growth and community interest over time. `MIT` <sub>Go/Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Druid](https://druid.apache.org) - Distributed, column-oriented, real-time analytics data store. `Apache-2.0` <sub>Java/Docker</sub>
* [EDA](https://github.com/jortilles/EDA) - Web application for data analysis and visualization. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [GoAccess](http://goaccess.io/) - Real-time web log analyzer and interactive viewer that runs in a terminal. `GPL-2.0` <sub>C</sub>
* [GoatCounter](https://www.goatcounter.com) - Easy web statistics without tracking of personal data. `EUPL-1.2` <sub>Go</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>
* [HitKeep](https://hitkeep.com/) - Privacy-first web analytics with goals, funnels, ecommerce tracking, and team management in a single binary with embedded DuckDB (alternative to Google Analytics, Plausible, Umami). `MIT` <sub>Go/Docker</sub>
* [Litlyx](https://litlyx.com) - All-in-one Analytics Solution. Setup in 30 seconds. Display all your data on an AI-powered dashboard. Fully self-hostable and GDPR compliant. `Apache-2.0` <sub>Docker</sub>
* [Liwan](https://liwan.dev/) - Privacy-first web analytics. `Apache-2.0` <sub>Rust/Docker</sub>
* [Matomo](https://matomo.org/) - Web analytics that protects your data and your customers' privacy (alternative to Google Analytics). `GPL-3.0` <sub>PHP</sub>
* [Medama Analytics](https://oss.medama.io) - Privacy-first website analytics. Tiny, simple, and cookie-free. `Apache-2.0/MIT` <sub>Docker/Go</sub>
* [Metabase](https://metabase.com/) - Easy way for everyone in your company to ask questions and learn from data. `AGPL-3.0` <sub>Java/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Middleware](https://middlewarehq.com/) - Tool designed to help engineering leaders measure and analyze the effectiveness of their teams using the DORA metrics. `Apache-2.0` <sub>Docker/Python/Nodejs</sub>
* [Netron](https://netron.app/) - Visualizer for neural network and machine learning models. `MIT` <sub>Python/Nodejs</sub>
* [Offen](https://www.offen.dev/) - Fair, lightweight and open web analytics tool. Gain insights while your users have full access to their data. `Apache-2.0` <sub>Go/Docker</sub>
* [Plausible Analytics](https://plausible.io/) - Simple, lightweight (< 1 KB) and privacy-friendly web analytics. `AGPL-3.0` <sub>Elixir</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PostHog](https://posthog.com) - Product analytics, session recording, feature flagging and a/b testing that you can self-host (alternative to Mixpanel, Amplitude, Heap, HotJar, Optimizely). `MIT` <sub>Python</sub>
* [Postiz](https://postiz.com) - Schedule posts, track the performance of your content, and manage all your social media accounts in one place (Alternative to Buffer, Hootsuite, Sprout Social). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Prisme Analytics](https://www.prismeanalytics.com) - Privacy-focused and progressive analytics service based on Grafana. `AGPL-3.0/MIT` <sub>Docker</sub>
* [Redash](http://redash.io) - Connect and query your data sources, build dashboards to visualize data and share them with your company. `BSD-2-Clause` <sub>Docker</sub>
* [Rybbit](https://rybbit.com/) - Web and products analytics that is easy to setup and more intuitive (alternative to Google Analytics). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Shaper](https://taleshape.com/shaper/docs) - Build Data Dashboards all in SQL. Powered by DuckDB. `MPL-2.0` <sub>Docker/Nodejs/Python/Go</sub>
* [Socioboard](https://github.com/socioboard/Socioboard-5.0) - Social media management, analytics, and reporting platform supporting nine social media networks out-of-the-box. `GPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Statistics for Strava](https://github.com/robiningelbrecht/statistics-for-strava) - Statistics dashboard generated from Strava data. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Superset](http://superset.apache.org/) - Modern data exploration and visualization platform. `Apache-2.0` <sub>Python</sub>
* [Swetrix](https://swetrix.com/) - Ultimate, open-source web analytics to satisfy all your needs. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Umami](https://umami.is/) - Simple, fast, privacy-focused alternative to Google Analytics. `MIT` <sub>Nodejs/Docker</sub>
* [Vince](https://www.vinceanalytics.com/) - Web analytics and dashboard (alternative to Google Analytics). `AGPL-3.0` <sub>Go/Docker/K8S/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Arquivamento e preservação digital

* [ArchiveBox](https://archivebox.io/) - Create HTML & screenshot archives of sites from your bookmarks, browsing history, RSS feeds, or other sources (alternative to Wayback Machine). `MIT` <sub>Python/Docker</sub>
* [ArchivesSpace](https://archivesspace.org/) - Archives information management application for managing and providing Web access to archives, manuscripts and digital objects. `ECL-2.0` <sub>Ruby</sub>
* [Bichon](https://github.com/rustmailer/bichon) - Email archiving server that syncs from IMAP accounts, indexes emails for full-text search, and provides a REST API. No external database required, includes WebUI with multi-account support. `AGPL-3.0` <sub>Rust/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [bitmagnet](https://bitmagnet.io) - BitTorrent indexer, DHT crawler, content classifier and torrent search engine with web UI, GraphQL API and Servarr stack integration. `MIT` <sub>Go/Docker</sub>
* [CKAN](https://ckan.org) - Make open data websites. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Collective Access - Providence](https://collectiveaccess.org/) - Highly configurable Web-based framework for management, description, and discovery of digital and physical collections supporting a variety of metadata standards, data types, and media formats. `GPL-3.0` <sub>PHP</sub>
* [Eonvelope](https://dacid99.gitlab.io/eonvelope) - Email archiving software that allows you to preserve your emails for an indefinite long period of time. `AGPL-3.0` <sub>K8S/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Ganymede](https://github.com/Zibbp/ganymede) - Twitch VOD and live stream archiving platform. Includes a rendered chat for each archive. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [mail-archiver](https://github.com/s1t5/mail-archiver) - Web application for archiving, searching, and exporting emails from multiple accounts (IMAP, M365 or Import). Featuring folder sync, attachment support, mailbox migration and a dashboard. `GPL-3.0` <sub>Docker</sub>
* [Omeka S](https://omeka.org/s/) - Next-generation web publishing platform for institutions interested in connecting digital cultural heritage collections with other resources online. `GPL-3.0` <sub>Nodejs</sub>
* [Open Archiver](https://openarchiver.com/) - Email archiving solution with full-text search and eDiscovery search features. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Piler](https://www.mailpiler.org/) - Feature-rich email archiving solution. `GPL-3.0` <sub>C/Docker/deb</sub>
* [Wallabag](https://www.wallabag.org) - Wallabag, formerly Poche, is a web application allowing you to save articles to read them later with improved readability. `MIT` <sub>PHP</sub>
* [Wayback](https://github.com/wabarc/wayback) - A self-hosted toolkit for archiving webpages to the Internet Archive, archive.today, IPFS, and local file systems. `GPL-3.0` <sub>Go</sub>

## Arquivos — armazenamento de objetos

* [GarageHQ](https://garagehq.deuxfleurs.fr/) - Geo-distributed, S3‑compatible storage service that can fulfill many needs. `AGPL-3.0` <sub>Docker/Rust</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Harbor](https://goharbor.io/) - Cloud native image registry that stores, signs, and scans content. `Apache-2.0` <sub>Docker/K8S</sub>
* [SeaweedFS](https://github.com/seaweedfs/seaweedfs) - SeaweedFS is an open source distributed file system supporting WebDAV, S3 API, FUSE mount, HDFS, etc, optimized for lots of small files, and easy to add capacity. `Apache-2.0` <sub>Go</sub>
* [Zenko CloudServer](https://www.zenko.io/cloudserver) - Zenko CloudServer, an open-source implementation of a server handling the Amazon S3 protocol. `Apache-2.0` <sub>Docker/Nodejs</sub>
* [ZOT OCI Registry](https://zotregistry.dev) - A production-ready vendor-neutral OCI-native container image registry. `Apache-2.0` <sub>Go/Docker</sub>

## Arquivos — compartilhamento P2P

* [bittorrent-tracker](https://webtorrent.io/) - Simple, robust, BitTorrent tracker (client and server) implementation. `MIT` <sub>Nodejs</sub>
* [Deluge](https://deluge-torrent.org/) - Lightweight, cross-platform BitTorrent client. `GPL-3.0` <sub>Python/deb</sub>
* [PrivyDrop](https://www.privydrop.app) - Simple and user-friendly, breakpoint-resumable peer-to-peer text, image, and file transfer tool based on WebRTC. `MIT` <sub>Docker/Nodejs</sub>
* [qBittorrent](https://www.qbittorrent.org/) - Free cross-platform bittorrent client with a feature rich Web UI for remote access. `GPL-2.0` <sub>C++</sub>
* [slskd](https://github.com/slskd/slskd) - A modern client-server application for the Soulseek file sharing network. `AGPL-3.0` <sub>Docker/C#</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Transmission](https://transmissionbt.com/) - Fast, easy, free Bittorrent client. `GPL-3.0` <sub>C++/deb</sub>
* [Webtor](https://github.com/webtor-io/self-hosted) - Web-based torrent client with instant audio/video streaming. `MIT` <sub>Docker</sub>

## Arquivos — gerenciadores web

* [Apaxy](https://oupala.github.io/apaxy/) - Theme built to enhance the experience of browsing web directories, using the mod_autoindex Apache module and some CSS to override the default style of a directory listing. `GPL-3.0` <sub>Javascript</sub>
* [ClyoCloud](https://clyo.cloud/) - A personal, self-hosted cloud storage and media management application built for privacy, efficiency, and aesthetics. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [copyparty](https://github.com/9001/copyparty) - Portable file server with accelerated resumable uploads, deduplication, WebDAV, FTP, zeroconf, media indexer, video thumbnails, audio transcoding, and write-only folders, in a single file with no mandatory dependencies. `MIT` <sub>Python</sub>
* [Directory Lister](https://www.directorylister.com/) - Simple PHP based directory lister that lists a directory and all its sub-directories and allows you to navigate there within. `MIT` <sub>PHP/Docker</sub>
* [filebrowser](https://filebrowser.org/) - Web File Browser with a Material Design web interface. `Apache-2.0` <sub>Go</sub>
* [FileGator](https://filegator.io/) - FileGator is a powerful multi-user file manager with a single page front-end. `MIT` <sub>PHP/Docker</sub>
* [FileRise](https://github.com/error311/FileRise) - Web file manager with uploads, tagging, share links, gallery/table views, and an in-browser editor. `MIT` <sub>Docker/PHP</sub>
* [Filestash](https://www.filestash.app/) - Web file manager that lets you manage your data anywhere it is located: FTP, SFTP, WebDAV, Git, S3, Minio, Dropbox, or Google Drive. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [IFM](https://github.com/misterunknown/ifm) - Single script file manager. `MIT` <sub>PHP</sub>
* [mikochi](https://github.com/zer0tonin/Mikochi) - Browse remote folders, upload files, delete, rename, download and stream files to VLC/mpv. `MIT` <sub>Go/Docker/K8S</sub>
* [miniserve](https://github.com/svenstaro/miniserve) - CLI tool to serve files and dirs over HTTP. `MIT` <sub>Rust</sub>
* [ResourceSpace](https://www.resourcespace.com) - Simple, fast, and free way to organise your digital assets. `BSD-4-Clause` <sub>PHP</sub>
* [slcl](https://codeberg.org/xavidcr/slcl) - Simple and lightweight web cloud storage. `AGPL-3.0` <sub>C</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Surfer](https://git.cloudron.io/cloudron/surfer) - Simple static file server with webui to manage files. `MIT` <sub>Nodejs</sub>
* [TagSpaces](https://www.tagspaces.org/) - TagSpaces is an offline, cross-platform file manager and organiser that also can function as a note taking app. The WebDAV version of the application can be installed on top of a WebDAV servers such as Nextcloud or ownCloud. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Tiny File Manager](https://tinyfilemanager.github.io) - Web based File Manager in PHP, simple, fast and small file manager with a single file. `GPL-3.0` <sub>PHP</sub>

## Arquivos — upload rápido

* [015](https://send.fudaoyuan.icu) - A temporary file sharing platform. Focused on providing one-time, temporary file and text upload, processing, and sharing services. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Chibisafe](https://chibisafe.app) - File uploader service that aims to to be easy to use and set up. It accepts files, photos, documents, anything you imagine and gives you back a shareable link for you to send to others. `MIT` <sub>Docker/Nodejs</sub>
* [Digirecord](https://ladigitale.dev/digirecord/) - Record and share audio files (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [elixire](https://gitlab.com/elixire/elixire) - Simple yet advanced screenshot uploading and link shortening service. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Files Sharing](https://github.com/axeloz/filesharing) - File sharing application based on unique and temporary links. `GPL-3.0` <sub>PHP/Docker</sub>
* [Flare](https://github.com/FlintSH/Flare) - A nonbloated, modern, and highly configurable file/screenshot vault server with support for ShareX, Flameshot, and Spectacle. Offers OCR search and more. `MIT` <sub>Docker/Nodejs</sub>
* [Gokapi](https://github.com/Forceu/gokapi) - Lightweight server to share files, which expire after a set amount of downloads or days. Similar to the discontinued Firefox Send, with the difference that only the admin is allowed to upload files. `GPL-3.0` <sub>Go/Docker</sub>
* [goploader](https://depado.github.io/goploader/) - Easy file sharing with server-side encryption, curl/httpie/wget compliant. `MIT` <sub>Go</sub>
* [GoSƐ](https://codeberg.org/stv0g/gose) - Modern file-uploader focusing on scalability and simplicity. It only depends on a S3 storage backend and hence scales horizontally without the need for additional databases or caches. `Apache-2.0` <sub>Go/Docker</sub>
* [Jirafeau](https://gitlab.com/jirafeau/Jirafeau) - One-click-fileshare project. Select your file, upload, and share a link. That's it. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OnionShare](https://github.com/onionshare/onionshare) - Securely and anonymously share a file of any size. `GPL-3.0` <sub>Python/deb</sub>
* [PicoShare](https://github.com/mtlynch/picoshare) - Minimalist, easy-to-host service for sharing images and other files. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Picsur](https://github.com/CaramelFur/Picsur) - Simple imaging hosting platform that allows you to easily host, edit, and share images. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PictShare](https://www.pictshare.net/) - Multi lingual image hosting service with a simple resizing and upload API. `Apache-2.0` <sub>PHP/Docker</sub>
* [Pingvin Share X](https://github.com/smp46/pingvin-share-x) - File sharing platform with support for logins, reverse shares, share expiry, S3 Buckets, advanced authentication, ClamAV for security scans and more (fork of Pingvin Share). `BSD-2-Clause` <sub>Docker/Nodejs</sub>
* [Plik](https://github.com/root-gg/plik) - Scalable and friendly temporary file upload system. `MIT` <sub>Go/Docker</sub>
* [ProjectSend](https://www.projectsend.org/) - Upload files and assign them to specific clients you create. Give access to those files to your clients. `GPL-2.0` <sub>PHP</sub>
* [PsiTransfer](https://github.com/psi-4ward/psitransfer) - Simple file sharing solution with robust up-/download-resume and password protection. `BSD-2-Clause` <sub>Nodejs</sub>
* [QuickShare](https://ihexxa.github.io/quickshare.site/) - Quick and simple file sharing between different devices. `LGPL-3.0` <sub>Docker/Go</sub>
* [Safebucket](https://docs.safebucket.io/) - File sharing platform with pluggable infrastructure, where uploads and downloads go directly between clients and S3-compatible storage. `Apache-2.0` <sub>Go/Docker</sub>
* [sE2EEnd](https://github.com/sE2EEnd/sE2EEnd) - End-to-end encrypted file sharing with password protection, download limits, and auto-expiration, integrated with Keycloak for authentication. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Sharry](https://github.com/eikek/sharry) - Share files easily over the internet between authenticated and anonymous users (both ways) with resumable up- and downloads. `GPL-3.0` <sub>Scala/Java/deb/Docker</sub>
* [Shifter](https://github.com/TobySuch/Shifter) - A simple, self-hosted file-sharing web app, powered by Django. `MIT` <sub>Docker</sub>
* [Slink](https://docs.slinkapp.io/) - Image sharing platform designed to give users complete control over their media sharing experience. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [snowshare](https://github.com/TuroYT/snowshare) - File and link sharing platform with URL shortening, code snippet sharing, and file uploads, featuring customizable expiration, privacy settings, and QR codes. `CC0-1.0` <sub>Nodejs/Docker</sub>
* [transfer.sh](https://github.com/dutchcoders/transfer.sh) - Easy file sharing from the command line. `MIT` <sub>Go</sub>
* [Uguu](https://github.com/nokonoko/uguu) - Stores files and deletes after X amount of time. `MIT` <sub>PHP</sub>
* [XBackBone](https://xbackbone.app/) - A simple, fast and lightweight file manager with instant sharing tools integration, like ShareX (a free and open-source screenshot utility for Windows). `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Zipline](https://github.com/diced/zipline) - A lightweight, fast and reliable file sharing server that is commonly used with ShareX, offering a react-based Web UI and fast API. `MIT` <sub>Docker/Nodejs</sub>

## Automação

* [Activepieces](https://www.activepieces.com) - No-code business automation tool like Zapier or Tray. For example, you can send a Slack notification for each new Trello card. `MIT` <sub>Docker</sub>
* [Apache Airflow](https://airflow.apache.org/) - Platform to programmatically author, schedule, and monitor workflows. `Apache-2.0` <sub>Python/Docker</sub>
* [Automatisch](https://automatisch.io) - Business automation tool that lets you connect different services like Twitter, Slack, and more to automate your business processes (alternative to Zapier). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [BookBounty](https://github.com/TheWicklowWolf/BookBounty) - Retrieve missing Readarr books from Library Genesis. `MPL-2.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [changedetection.io](https://changedetection.io/) - Stay up-to-date with web-site content changes. `Apache-2.0` <sub>Python/Docker</sub>
* [ChiefOnboarding](https://chiefonboarding.com) - Employee onboarding platform that allows you to provision user accounts and create sequences with todo items, resources, text/email/Slack messages, and more! Available as a web portal and Slack bot. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Cronicle](https://cronicle.net/) - Simple, distributed task scheduler and runner with a web based UI. `MIT` <sub>Nodejs</sub>
* [Cronmaster](https://github.com/fccview/cronmaster) - Cronjob management UI with human readable syntax, live logging and log history for your cronjobs. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Dagu](https://docs.dagu.cloud/) - Powerful Cron alternative with a Web UI. It allows you to define dependencies between commands as a Directed Acyclic Graph (DAG) in a declarative YAML format. `GPL-3.0` <sub>Go/Docker</sub>
* [Discount Bandit](https://discount-bandit.cybrarist.com/) - Track pricing, stock status of products across multiple stores such as Amazon, Ebay, Walmart, etc. `GPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Dittofeed](https://www.dittofeed.com) - Omni-channel customer engagement and messaging automation platform (alternative to Braze, Customer.io, Iterable). `MIT` <sub>Docker</sub>
* [feedmixer](https://github.com/cristoper/feedmixer) - Micro web service which takes a list of feed URLs and returns a new feed consisting of the most recent n entries from each given feed (returns Atom, RSS, or JSON). `WTFPL` <sub>Python</sub>
* [flowctl](https://flowctl.net) - Self-service workflow execution platform with approvals, remote execution and scheduling. `Apache-2.0` <sub>Go/Docker</sub>
* [Fredy](https://fredy.orange-coding.net/) - Searches for new apartments, houses, and flats in Germany on platforms like ImmoScout24, Immowelt, and others, and instantly delivers the results to you via Slack, Telegram, and more. `Apache-2.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [gocron](https://github.com/flohoss/gocron) - Task scheduler that allows users to specify recurring jobs via a simple YAML configuration file. `MIT` <sub>Docker</sub>
* [HandBrake Web](https://github.com/TheNickOfTime/handbrake-web) - Use one or more instances of HandBrake video transcoder on a headless device via a web interface. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Healthchecks](https://healthchecks.io/) - Listen for pings and sends alerts when pings are late. `BSD-3-Clause` <sub>Python/Docker</sub>
* [Huginn](https://github.com/huginn/huginn) - Build agents that monitor and act on your behalf. `MIT` <sub>Ruby</sub>
* [Kestra](https://kestra.io) - Event-driven, language-agnostic platform to create, schedule, and monitor workflows. In code. Coordinate data pipelines and tasks such as ETL and ELT. `Apache-2.0` <sub>Docker</sub>
* [Kibitzr](https://kibitzr.github.io) - Lightweight personal web assistant with powerful integrations. `MIT` <sub>Python</sub>
* [LazyLibrarian](https://gitlab.com/LazyLibrarian/LazyLibrarian) - Follow authors and grab metadata for all your digital reading needs. It uses a combination of Goodreads, Librarything and optionally GoogleBooks as sources for author info and book info. `GPL-3.0` <sub>Python</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Leon](https://getleon.ai) - Personal assistant who can live on your server. `MIT` <sub>Nodejs</sub>
* [Matchering](https://github.com/sergree/matchering) - Automated music mastering (alternative to LANDR, eMastered and MajorDecibel). `GPL-3.0` <sub>Docker</sub>
* [Mylar3](https://mylar.nerdfirehurricane.com/) - Automated Comic Book (cbr/cbz) downloader program for use with NZB and torrents. `GPL-3.0` <sub>Python/Docker</sub>
* [OliveTin](https://www.olivetin.app/) - Web interface for running Linux shell commands. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [pyLoad](https://pyload.net/) - Lightweight, customizable and remotely manageable downloader for 1-click-hosting sites like rapidshare.com or uploaded.to. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [StackStorm](https://stackstorm.com) - StackStorm (aka _IFTTT for Ops_) is event-driven automation for auto-remediation, security responses, troubleshooting, deployments, and more. Includes rules engine, workflow, 160 integration packs with 6000+ actions and ChatOps. `Apache-2.0` <sub>Python</sub>
* [µTask](https://github.com/ovh/utask) - Automation engine that models and executes business processes declared in yaml. `BSD-3-Clause` <sub>Go/Docker</sub>

## Buscadores

* [Aleph](https://aleph.occrp.org/) - Tool for indexing large amounts of both documents (PDF, Word, HTML) and structured (CSV, XLS, SQL) data for easy browsing and search. It is built with investigative reporting as a primary use case. `MIT` <sub>Docker/K8S</sub>
* [Amgix](https://amgix.io) - Open-source hybrid search engine built for flexible deployment and real-world messy data. `AGPL-3.0` <sub>Docker/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Apache Solr](https://lucene.apache.org/solr/) - Enterprise search platform featuring full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, and rich document (e.g., Word, PDF) handling. `Apache-2.0` <sub>Java/Docker/K8S</sub>
* [Fess](https://fess.codelibs.org/) - Powerful and easily deployable Enterprise Search Server. `Apache-2.0` <sub>Java/Docker</sub>
* [Hister](https://hister.org/) - Personal web search engine with automatic indexing of visited websites. Supports offline local result previews, local files, multi-user handling and optional semantic search. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Manticore Search](https://github.com/manticoresoftware/manticoresearch/) - Full-text search and data analytics, with fast response time for small, medium and big data (alternative to Elasticsearch). `GPL-3.0` <sub>Docker/deb/C++/K8S</sub>
* [MeiliSearch](https://www.meilisearch.com) - Ultra relevant, instant and typo-tolerant full-text search API. `MIT` <sub>Rust/Docker/deb</sub>
* [Meme Search](https://github.com/neonwatty/meme-search) - AI-powered meme search engine. Automatically extracts descriptions from images using vision-language models, then indexes with vector embeddings for semantic and keyword search. `Apache-2.0` <sub>Docker</sub>
* [OpenSearch](https://opensearch.org) - Distributed and RESTful search engine. `Apache-2.0` <sub>Java/Docker/K8S/deb</sub>
* [SearXNG](https://docs.searxng.org/) - Internet metasearch engine which aggregates results from various search services and databases (Fork of Searx). `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Sosse](https://sosse.readthedocs.io/en/stable/) - Selenium based search engine and crawler with offline archiving. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Typesense](https://typesense.org) - Blazing fast, typo-tolerant open source search engine optimized for developer happiness and ease of use. `GPL-3.0` <sub>C++/Docker/K8S/deb</sub>
* [Websurfx](https://github.com/neon-mmd/websurfx) - Aggregate results from other search engines (metasearch engine) without ads while keeping privacy and security in mind. It is extremely fast and provides a high level of customization (alternative to SearX). `AGPL-3.0` <sub>Rust/Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Yacy](https://yacy.net/en/index.html) - Peer based, decentralized search engine server. `GPL-2.0` <sub>Java/Docker/K8S</sub>

## CRM

* [Corteza](https://docs.cortezaproject.org) - CRM including a unified workspace, enterprise messaging and a low code environment for rapidly and securely delivering records-based management solutions. `Apache-2.0` <sub>Go</sub>
* [Django-CRM](https://DjangoCRM.github.io/info/) - Analytical CRM with tasks management, email marketing and many more. Django CRM is built for individual use, businesses of any size or freelancers and is designed to provide easy customization and quick development. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [EspoCRM](https://www.espocrm.com/) - CRM with a frontend designed as a single page application, and a REST API. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Krayin](https://krayincrm.com/) - CRM solution for SMEs and Enterprises for complete customer lifecycle management. `MIT` <sub>PHP</sub>
* [Monica](https://monicahq.com/) - Personal relationship manager, and a new kind of CRM to organize interactions with your friends and family. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SuiteCRM](https://suitecrm.com) - The award-winning, enterprise-class open source CRM. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Twenty](https://twenty.com) - A modern CRM offering the flexibility of open source, advanced features, and a sleek design. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Chamados e suporte

* [BugPin](https://bugpin.io) - Visual bug reporting and ticketing tool for web applications. `AGPL-3.0/MIT` <sub>Docker</sub>
* [Bugzilla](https://www.bugzilla.org/) - General-purpose bugtracker and testing tool originally developed and used by the Mozilla project. `MPL-2.0` <sub>Perl</sub>
* [Frappe Helpdesk](https://frappe.io/helpdesk) - Helpdesk software which helps you streamline your company's support, offers an easy setup, clean user interface, and automation tools to resolve customer queries efficiently. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [FreeScout](https://freescout.net/) - Email-based customer support application, help desk and shared mailbox (alternative to Zendesk and Help Scout). `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [GlitchTip](https://glitchtip.com) - Error tracking app to collect errors reported by your app. `MIT` <sub>Python/Docker/K8S</sub>
* [ITFlow](https://itflow.org) - Client IT documentation, ticketing, invoicing and accounting for MSPs (Managed Service Providers). `GPL-3.0` <sub>PHP</sub>
* [Libredesk](https://libredesk.io/) - Modern omnichannel customer support desk. Live chat, email, and more in a single binary. `AGPL-3.0` <sub>Docker/Go/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MantisBT](https://www.mantisbt.org/) - Bug tracker, fits best for software development. `GPL-2.0` <sub>PHP</sub>
* [OTOBO](https://otobo.io/en/) - Flexible web-based ticketing system used for customer service, help desk, IT service management. `GPL-3.0` <sub>Perl/Docker</sub>
* [Request Tracker](https://www.bestpractical.com/rt/) - Enterprise-grade issue tracking system. `GPL-2.0` <sub>Perl</sub>
* [Roundup Issue Tracker](https://www.roundup-tracker.org/) - Simple-to-use and -install issue tracking system with command-line, web, REST, XML-RPC, and e-mail interfaces. Designed with flexibility in mind - not just another bug tracker. `MIT/ZPL-2.0` <sub>Python/Docker</sub>
* [Zammad](https://zammad.org/) - Easy to use but powerful open-source support and ticketing system. `AGPL-3.0` <sub>Ruby/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Comunicação — IRC

* [Ergo](https://ergo.chat/) - Modern IRCv3 server written in Go, combining the features of an ircd, a services framework, and a bouncer. `MIT` <sub>Go/Docker</sub>
* [Glowing Bear](https://github.com/glowing-bear/glowing-bear) - A web frontend for WeeChat. `GPL-3.0` <sub>Nodejs</sub>
* [InspIRCd](https://www.inspircd.org/) - Modular IRC server written in C++ for Linux, BSD, Windows, and macOS. `GPL-2.0` <sub>C++/Docker</sub>
* [Kiwi IRC](https://kiwiirc.com/) - Responsive web IRC client with theming support. `Apache-2.0` <sub>Nodejs</sub>
* [ngircd](https://ngircd.barton.de/) - Portable and lightweight Internet Relay Chat server for small or private networks. `GPL-2.0` <sub>C/deb</sub>
* [Quassel IRC](https://quassel-irc.org/) - Distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core. `GPL-2.0` <sub>C++</sub>
* [Robust IRC](https://robustirc.net/) - IRC without netsplits. Distributed IRC server, based on RobustSession protocol. `BSD-3-Clause` <sub>Go</sub>
* [The Lounge](https://thelounge.chat/) - Self-hosted web IRC client. `MIT` <sub>Nodejs/Docker</sub>
* [UnrealIRCd](https://www.unrealircd.org/) - Modular, advanced and highly configurable IRC server written in C for Linux, BSD, Windows, and macOS. `GPL-2.0` <sub>C</sub>
* [Weechat](https://weechat.org/) - Fast, light and extensible chat client. `GPL-3.0` <sub>C/Docker/deb</sub>
* [ZNC](https://wiki.znc.in/ZNC) - Advanced IRC bouncer. `Apache-2.0` <sub>C++/deb</sub>

## Comunicação — SIP e telefonia

* [Asterisk](https://www.asterisk.org/) - Easy to use but advanced IP PBX system, VoIP gateway and conference server. `GPL-2.0` <sub>C/deb</sub>
* [Flexisip](https://www.linphone.org/en/flexisip-sip-server/) - Complete, modular and scalable SIP server, includes a push gateway, to deliver SIP incoming calls or text messages on mobile device platforms where push notifications are required to receive information when the app is not active in the foreground. `AGPL-3.0` <sub>C/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Freepbx](https://www.freepbx.org) - Web-based open source GUI that controls and manages Asterisk. `GPL-2.0` <sub>PHP</sub>
* [FreeSWITCH](https://freeswitch.org/) - Scalable open source cross-platform telephony platform. `MPL-2.0` <sub>C</sub>
* [FusionPBX](https://www.fusionpbx.com/) - Web interface for multi-platform voice switch called FreeSWITCH. `MPL-1.1` <sub>PHP</sub>
* [Kamailio](https://www.kamailio.org/w/) - Modular SIP server (registrar/proxy/router/etc). `GPL-2.0` <sub>C/deb</sub>
* [openSIPS](https://opensips.org/) - SIP proxy/server for voice, video, IM, presence and any other SIP extensions. `GPL-2.0` <sub>C</sub>
* [Routr](https://routr.io) - Lightweight SIP proxy, location server, and registrar for a reliable and scalable SIP infrastructure. `MIT` <sub>Docker/K8S</sub>
* [SIP3](https://sip3.io/) - VoIP troubleshooting and monitoring platform. `Apache-2.0` <sub>Java</sub>
* [SIPCAPTURE Homer](https://www.sipcapture.org/) - Troubleshooting and monitoring VoIP calls. `AGPL-3.0` <sub>Nodejs/Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Wazo](https://wazo-platform.org/) - Full-featured IPBX solution built atop Asterisk with integrated Web administration interface and REST-ful API. `GPL-3.0` <sub>Python</sub>
* [Yeti-Switch](https://yeti-switch.org/) - Transit class4 softswitch(SBC) with integrated billing and routing engine and REST API. `GPL-2.0` <sub>C++/Ruby</sub>

## Comunicação — sistemas de mensagem

* [AnyCable](https://anycable.io/) - Realtime server for reliable two-way communication over WebSockets, Server-sent events, etc. `MIT` <sub>Go/Docker</sub>
* [Apprise](https://github.com/caronc/apprise) - Apprise allows you to send a notification to almost all of the most popular notification services available to us today such as: Telegram, Discord, Slack, Amazon SNS, Gotify, etc. `MIT` <sub>Python/Docker/deb</sub>
* [Centrifugo](https://centrifugal.dev/) - Language-agnostic real-time messaging (Websocket or SockJS) server. `MIT` <sub>Go/Docker/K8S</sub>
* [Chitchatter](https://chitchatter.im/) - Peer-to-peer chat app that is serverless, decentralized, and ephemeral. `GPL-2.0` <sub>Nodejs</sub>
* [Conduit](https://conduit.rs/) - A simple, fast, and reliable chat server powered by Matrix. `Apache-2.0` <sub>Rust</sub>
* [Continuwuity](https://continuwuity.org/) - Community-driven Matrix homeserver, the continuation of conduwuit focusing on user experience and new features (fork of Conduit). `Apache-2.0` <sub>Rust/Docker/K8S/deb</sub>
* [Databag](https://github.com/balzack/databag) - Federated, end-to-end encrypted messaging service for the web, iOS, and Android, supporting text, photos, video, and WebRTC video and audio calls. `Apache-2.0` <sub>Docker</sub>
* [Element](https://element.io) - Fully-featured Matrix client for Web, iOS & Android. `Apache-2.0` <sub>Nodejs</sub>
* [GlobaLeaks](https://www.globaleaks.org/) - Whistleblowing software enabling anyone to easily set up and maintain a secure reporting platform. `AGPL-3.0` <sub>Python/deb/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [GNUnet](https://gnunet.org/) - Software framework for decentralized, peer-to-peer networking. `GPL-3.0` <sub>C</sub>
* [Gotify](https://gotify.net/) - Notification server with Android and CLI clients (alternative to PushBullet). `MIT` <sub>Go/Docker</sub>
* [Hyphanet](https://hyphanet.org/) - Anonymously share files, browse and publish _freesites_ (web sites accessible only through Hyphanet) and chat on forums. `GPL-2.0` <sub>Java</sub>
* [Jami](https://jami.net/) - Universal communication platform which preserves the user's privacy and freedoms. `GPL-3.0` <sub>C++</sub>
* [Live Helper Chat](https://livehelperchat.com/) - Live Support chat for your website. `Apache-2.0` <sub>PHP</sub>
* [Mumble](https://wiki.mumble.info/wiki/Main_Page) - Low-latency, high quality voice/text chat software. `BSD-3-Clause` <sub>C++/deb</sub>
* [Notifo](https://github.com/notifo-io/notifo) - Multichannel notification server with support for Email, Mobile Push, Web Push, SMS, messaging and a javascript plugin. `MIT` <sub>C#</sub>
* [Novu](https://novu.co/) - Notification infrastructure for developers. `MIT` <sub>Docker/Nodejs</sub>
* [ntfy](https://ntfy.sh/) - Push notifications to phone or desktop using HTTP PUT/POST, with Android app, CLI and web app, similar to Pushover and Gotify. `Apache-2.0/GPL-2.0` <sub>Go/Docker/K8S</sub>
* [One Time Secret](https://docs.onetimesecret.com) - Share sensitive information securely with self-destructing links that are only viewable once. `MIT` <sub>Docker/Ruby/Nodejs</sub>
* [OTS](https://ots.fyi/) - One-Time-Secret sharing platform with a symmetric 256bit AES encryption in the browser. `Apache-2.0` <sub>Go</sub>
* [PushBits](https://github.com/pushbits/server) - Notification server for relaying push notifications via Matrix, similar to PushBullet and Gotify. `ISC` <sub>Go</sub>
* [RetroShare](https://retroshare.cc) - Secured and decentralized communication system. Offers decentralized chat, forums, messaging, file transfer. `GPL-2.0` <sub>C++</sub>
* [Rocket.Chat](https://rocket.chat/) - Communications platform that puts data protection first (alternative to Gitter.im and Slack). `MIT` <sub>Nodejs/Docker/K8S</sub>
* [SAMA](https://samacloud.io) - Next-Gen self-hosted chat server and clients. `GPL-3.0` <sub>Nodejs/Docker</sub>
* [Screego](https://screego.net) - Screego is a simple tool to quickly share your screen to one or multiple people via web browser. `GPL-3.0` <sub>Docker/Go</sub>
* [Shhh](https://github.com/smallwat3r/shhh) - Keep secrets out of emails or chat logs, share them using secure links with passphrase and expiration dates. `MIT` <sub>Python</sub>
* [SimpleX Chat](https://github.com/simplex-chat/simplex-chat) - The most private and secure chat and applications platform - now with double ratchet E2E encryption. `AGPL-3.0` <sub>Haskell</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Spectrum 2](https://spectrum.im/) - Spectrum 2 is an open source instant messaging transport.  It allows users to chat together even when they are using different IM networks. `GPL-3.0` <sub>C++</sub>
* [Stoat](https://stoat.chat/) - Stoat is a user-first chat platform built with modern web technologies. `AGPL-3.0/MIT` <sub>Rust</sub>
* [Synapse](https://element-hq.github.io/synapse/latest/index.html) - Server for [Matrix](https://matrix.org/), an open standard for decentralized persistent communication. `Apache-2.0` <sub>Python/deb</sub>
* [Tiledesk](https://tiledesk.com) - All-in-one customer engagement platform from lead-gen to post-sales, from WhatsApp to your website. With omni-channel live agents and AI-powered chatbots (alternative to Intercom, Zendesk, Tawk.to and Tidio). `MIT` <sub>Docker/K8S</sub>
* [Tinode](https://github.com/tinode) - Instant messaging platform. Backend in Go. Clients: Swift iOS, Java Android, JS webapp, scriptable command line; chatbots. `GPL-3.0` <sub>Go</sub>
* [Tox](https://tox.chat/) - Distributed, secure messenger with audio and video chat capabilities. `GPL-3.0` <sub>C</sub>
* [Tuwunel](https://tuwunel.chat) - High-performance and feature-rich chat server for Matrix, and the successor to conduwuit (fork of Conduit). `Apache-2.0` <sub>deb/Docker/Nix/Rust</sub>
* [Typebot](https://typebot.io) - Conversational app builder (alternative to Typeform and Landbot). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [WBO](https://github.com/lovasoa/whitebophir) - Web Whiteboard to collaborate in real-time on schemas, drawings, and notes. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Zulip](https://zulip.org) - Zulip is a powerful, open source group chat application. `Apache-2.0` <sub>Python</sub>

## Comércio eletrônico

* [Aimeos](https://aimeos.org/) - E-commerce framework for building custom online shops, market places and complex B2B applications scaling to billions of items with Laravel. `LGPL-3.0/MIT` <sub>PHP</sub>
* [Bagisto](https://bagisto.com/en/) - Leading Laravel open source e-commerce framework with multi-inventory sources, taxation, localization, dropshipping and more exciting features. `MIT` <sub>PHP</sub>
* [CoreShop](https://www.coreshop.org) - E-commerce plugin for Pimcore. `GPL-3.0` <sub>PHP</sub>
* [Drupal Commerce](https://drupalcommerce.org) - Popular e-commerce module for Drupal CMS, with support for dozens of payment, shipping, and shopping related modules. `GPL-2.0` <sub>PHP</sub>
* [EverShop](https://evershop.io/) - E-commerce platform with essential commerce features. Modular architecture and fully customizable. `GPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Magento Open Source](https://business.adobe.com/products/magento/magento-commerce.html) - Leading provider of open omnichannel innovation. `OSL-3.0` <sub>PHP</sub>
* [MedusaJs](https://medusajs.com/) - Headless commerce engine that enables developers to create amazing digital commerce experiences. `MIT` <sub>Nodejs</sub>
* [myCart](https://github.com/shurco/mycart) - Shopping cart in 1 file (with support for payment by card or cryptocurrency). `MIT` <sub>Go/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Open Source POS](https://github.com/opensourcepos/opensourcepos) - Open Source Point of Sale is a web based point of sale system. `MIT` <sub>PHP</sub>
* [OpenCart](https://www.opencart.com) - Shopping cart solution. `GPL-3.0` <sub>PHP</sub>
* [PrestaShop](https://www.prestashop.com/) - Fully scalable e-commerce solution. `OSL-3.0` <sub>PHP</sub>
* [Pretix](https://pretix.eu/) - Ticket sales platform for events. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [s-cart](https://s-cart.org/) - E-commerce website for individuals and businesses, built on top of Laravel Framework. `MIT` <sub>PHP</sub>
* [Saleor](https://saleor.io) - Django based open-sourced e-commerce storefront. `BSD-3-Clause` <sub>Docker/Python</sub>
* [Shopware Community Edition](https://www.shopware.com/en/community/community-edition/) - PHP based open source e-commerce software made in Germany. `MIT` <sub>PHP</sub>
* [Solidus](https://solidus.io/) - A free, open-source ecommerce platform that gives you complete control over your store. `BSD-3-Clause` <sub>Ruby/Docker</sub>
* [Spree Commerce](https://spreecommerce.org) - Spree is a complete, modular & API-driven open source e-commerce solution for Ruby on Rails. `BSD-3-Clause` <sub>Ruby</sub>
* [Sylius](https://sylius.com) - Symfony2 powered open source full-stack platform for eCommerce. `MIT` <sub>PHP</sub>
* [Thelia](https://thelia.net/) - Thelia is an open source and flexible e-commerce solution. `LGPL-3.0` <sub>PHP</sub>
* [Vendure](https://www.vendure.io) - A headless commerce framework. `MIT` <sub>Nodejs</sub>
* [WooCommerce](https://woocommerce.com/) - WordPress based e-commerce solution. `GPL-3.0` <sub>PHP</sub>

## Controle de estoque

* [Cannery](https://cannery.app) - Firearm and ammunition tracker app. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [DVinyl](https://github.com/Kyonew/DVinyl) - Modern collection manager for physical media (vinyls, CDs, cassettes, books, movies, and video games). `MIT` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [HomeBox (SysAdminsMedia)](https://homebox.software/) - Inventory and organization system built for the home user. `AGPL-3.0` <sub>Docker/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Inventaire](https://inventaire.io/welcome) - Collaborative resources mapper project, while yet only focused on exploring books mapping with wikidata and ISBNs. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Inventree](https://docs.inventree.org/en/latest/) - Inventory management system which provides intuitive parts management and stock control. `MIT` <sub>Python</sub>
* [Open QuarterMaster](https://openquartermaster.com/) - Powerful inventory management system, designed to be flexible and scalable. `GPL-3.0` <sub>deb/Docker</sub>
* [Part-DB](https://docs.part-db.de/) - Inventory management system for your electronic components. `AGPL-3.0` <sub>Docker/PHP/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Shelf](https://www.shelf.nu) - Asset and equipment tracking software used by teams who value clarity. Shelf is an asset database and QR asset label generator that lets you create, manage and overview your assets across locations. Unlimited assets, free forever. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Spoolman](https://github.com/Donkie/Spoolman) - Keep track of your inventory of 3D-printer filament spools. `MIT` <sub>Docker/Python</sub>

## Controle de tempo

* [ActivityWatch](https://activitywatch.net) - Automatically track how you spend time on your devices. `MPL-2.0` <sub>Python</sub>
* [Beaver Habit Tracker](https://github.com/daya0576/beaverhabits) - Habit tracking app to save your precious moments in your fleeting life. `BSD-3-Clause` <sub>Docker</sub>
* [Ever Gauzy](https://gauzy.co) - Open business management platform for collaborative, on-demand and sharing economies (ERP/CRM/HRM/ATS/PM). `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kimai](https://www.kimai.org/) - Track work time and print out a summary of your activities on demand. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [solidtime](https://www.solidtime.io) - Modern time tracking application for freelancers and agencies. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [TimeTagger](https://timetagger.app) - An open source time-tracker based on an interactive timeline and powerful reporting. `GPL-3.0` <sub>Python</sub>
* [TimeTracker](https://timetracker.drytrix.com/) - Track time across projects and clients, with timers, kanban tasks, CRM, expense tracking, multi-currency invoicing (PDF, Peppol/ZugFerd e-invoicing), reports, OIDC/SSO, and a REST API. `GPL-3.0` <sub>Docker</sub>
* [Traggo](https://traggo.net/) - Traggo is a tag-based time tracking tool. In Traggo there are no tasks, only tagged time spans. `GPL-3.0` <sub>Docker/Go</sub>
* [Wakapi](https://wakapi.dev/) - Tracking tool for coding statistics, compatible with WakaTime. `GPL-3.0` <sub>Go/Docker</sub>
* [Ziit](https://ziit.app) - The Swiss army knife of code time tracking (alternative to WakaTime). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## DNS

* [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) - User-friendly ads & trackers blocking DNS server. `GPL-3.0` <sub>Docker</sub>
* [blocky](https://0xerr0r.github.io/blocky/latest/) - Fast and lightweight DNS proxy as ad-blocker for local network with many features (alternative to Pi-hole). `Apache-2.0` <sub>Go/Docker</sub>
* [Maza ad blocking](https://maza-ad-blocking.andros.dev/) - Local ad blocker. Like Pi-hole but local and using your operating system. `Apache-2.0` <sub>Shell</sub>
* [Numa](https://numa.rs/) - Ad-blocking DNS resolver with DNSSEC-validating recursive resolution, DoH/DoT/Oblivious DoH, ephemeral overrides, and local service domains, in a single Rust binary (alternative to Pi-hole, AdGuard Home, NextDNS). `MIT` <sub>Rust/Docker/Nix</sub>
* [Pi-hole](https://pi-hole.net/) - Blackhole for Internet advertisements with a GUI for management and monitoring. `EUPL-1.2` <sub>Shell/PHP/Docker</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>
* [Technitium DNS Server](https://technitium.com/dns/) - Authoritative/recursive DNS server with ad blocking functionality. `GPL-3.0` <sub>Docker/C#</sub>

## Desenvolvimento — IDEs e ferramentas

* [Atheos](https://www.atheos.io) - Web-based IDE framework with a small footprint and minimal requirements, continued from Codiad. `MIT` <sub>PHP/Docker</sub>
* [code-server](https://github.com/coder/code-server) - VS Code in the browser, hosted on a remote server. `MIT` <sub>Nodejs/Docker</sub>
* [Coder](https://coder.com/) - Remote development machines on your own infrastructure. `AGPL-3.0` <sub>Go/Docker/K8S/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Eclipse Che](https://www.eclipse.org/che/) - Open source workspace server and cloud IDE. `EPL-1.0` <sub>Docker/Java</sub>
* [Hopp](https://gethopp.app) - Remote pair programming app with low-latency 4K screen sharing, drawing, and remote control, with clients for macOS and Windows (alternative to Tuple, Pop, Drovio, Coscreen). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Judge0 CE](https://judge0.com) - API to compile and run source code. `GPL-3.0` <sub>Docker</sub>
* [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) - Web-based environment for interactive and reproducible computing. `BSD-3-Clause` <sub>Python/Docker</sub>
* [Langfuse](https://langfuse.com) - LLM engineering platform for model tracing, prompt management, and application evaluation. Langfuse helps teams collaboratively debug, analyze, and iterate on their LLM applications such as chatbots or AI agents. `MIT` <sub>Docker</sub>
* [LiveCodes](https://livecodes.io/docs/features/self-hosting) - Feature-rich client-side code playground for React, Vue, Svelte, Solid, Typescript, Python, Go, Ruby, PHP and 90+ other languages. `MIT` <sub>Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Lowdefy](https://www.lowdefy.com/) - Build internal tools, BI dashboards, admin panels, CRUD apps and workflows in minutes using YAML / JSON on an self-hosted, open-source platform. Connect to your data sources, host via Serverless, Netlify or Docker. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [RapidForge](https://rapidforge.io/) - Lightweight platform for building webhooks, scheduled tasks and pages. Implement your logic with Bash or Lua. `Apache-2.0` <sub>Go/Nodejs</sub>
* [RStudio Server](https://www.rstudio.com/products/rstudio/#Server) - Web browser based IDE for R. `AGPL-3.0` <sub>Java/C++</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Desenvolvimento — feature flags

* [Featbit](https://www.featbit.co/) - Enterprise-grade feature flag platform that you can self-host. `MIT` <sub>Docker/K8S</sub>
* [Flagsmith](https://flagsmith.com) - Dashboard, API and SDKs for adding Feature Flags to your applications (alternative to LaunchDarkly). `BSD-3-Clause` <sub>Docker/K8S</sub>
* [Flipt](https://flipt.io) - Feature flag solution with support for multiple data backends (alternative to LaunchDarkly). `GPL-3.0` <sub>Docker/K8S/Go</sub>
* [GO Feature Flag](https://gofeatureflag.org) - Simple, complete, and lightweight feature flag solution (alternative to LaunchDarkly). `MIT` <sub>Go</sub>

## Desenvolvimento — gestão de APIs

* [Aastro](https://starwalkn.github.io/aastro-docs) - Extensible API Gateway written in Go. `Apache-2.0` <sub>Go/Docker</sub>
* [DreamFactory](https://www.dreamfactory.com/) - Turns any SQL/NoSQL/Structured data into Restful API. `Apache-2.0` <sub>PHP/Docker/K8S</sub>
* [form.io](https://form.io) - A REST API building platform that utilizes a drag & drop form builder, and is application framework agnostic. Contains open source and enterprise version. `MIT` <sub>Nodejs/Docker</sub>
* [Fusio](https://www.fusio-project.org/) - Open-source API management platform which helps to build and manage REST APIs. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Graphweaver](https://graphweaver.com/) - Turn multiple data sources into a single GraphQL API. `MIT` <sub>Nodejs</sub>
* [Hasura](https://hasura.io) - Fast, instant realtime GraphQL APIs on Postgres with fine grained access control, also trigger webhooks on database events. `Apache-2.0` <sub>Haskell/Docker/K8S</sub>
* [Hoppscotch Community Edition](https://hoppscotch.io) - Fast and beautiful API request builder. `MIT` <sub>Nodejs/Docker</sub>
* [Kong](https://konghq.com/kong/) - Microservice API Gateway and Platform. `Apache-2.0` <sub>Lua/Docker/K8S/deb</sub>
* [Lura](https://luraproject.org/) - High-performance API Gateway. `Apache-2.0` <sub>Go</sub>
* [Opik](https://www.comet.com/site/products/opik/) - Evaluate, test, and ship LLM applications with a suite of observability tools to calibrate language model outputs across your dev and production lifecycle. `Apache-2.0` <sub>Docker/Python</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Para](https://paraio.org) - Flexible and modular backend framework/server for object persistence, API development and authentication. `Apache-2.0` <sub>Java/Docker</sub>
* [Svix](https://svix.com) - Open-source webhooks as a service that makes it super easy for API providers to send webhooks. `MIT` <sub>Docker/Rust</sub>
* [Tyk](https://tyk.io) - Fast and scalable open source API Gateway. Out of the box, Tyk offers an API Management Platform with an API Gateway, API Analytics, Developer Portal and API Management Dashboard. `MPL-2.0` <sub>Go/Docker/K8S</sub>

## Desenvolvimento — gestão de projetos

* [Cgit](https://git.zx2c4.com/cgit/about/) - Fast lightweight web interface for git repositories. `GPL-2.0` <sub>C</sub>
* [Forgejo](https://forgejo.org) - A lightweight software forge focused on scaling, federation, and privacy (fork of Gitea). `MIT` <sub>Docker/Go</sub>
* [Fossil](https://www.fossil-scm.org/index.html/doc/trunk/www/index.wiki) - Distributed version control system featuring wiki and bug tracker. `BSD-2-Clause-FreeBSD` <sub>C</sub>
* [Gerrit](https://www.gerritcodereview.com/) - Code review and project management tool for Git-based projects. `Apache-2.0` <sub>Java/Docker</sub>
* [gitbucket](https://gitbucket.github.io/) - Git platform powered with easy installation, high extensibility & GitHub API compatibility (alternative to GitHub). `Apache-2.0` <sub>Scala/Java</sub>
* [Gitea](https://gitea.com) - Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD. `MIT` <sub>Go/Docker/K8S</sub>
* [GitLab](https://about.gitlab.com) - Self Hosted Git repository management, code reviews, issue tracking, activity feeds and wikis. `MIT` <sub>Ruby/deb/Docker/K8S</sub>
* [Gogs](https://gogs.io/) - Painless self-hosted Git Service written in Go. `MIT` <sub>Go</sub>
* [Huly](https://huly.io) - All-in-one project management platform (alternative to Linear, Jira, Slack, Notion, Motion). `EPL-2.0` <sub>Docker/K8S/Nodejs</sub>
* [Ideon](https://www.theideon.com) - Project workspace built around an infinite canvas; embed GitHub, GitLab, Gitea, and Forgejo repositories alongside notes, links, and tasks, with real-time collaboration. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kaneo](https://kaneo.app/) - Project management platform focused on simplicity and efficiency. `MIT` <sub>K8S/Docker</sub>
* [Leantime](https://leantime.io) - Lean project management system for small teams and startups helping to manage projects from ideation through delivery. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Mindwendel](https://www.mindwendel.com/) - Brainstorm and upvote ideas and thoughts within your team. `AGPL-3.0` <sub>Docker/Elixir</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [minimal-git-server](https://github.com/mcarbonne/minimal-git-server) - Lightweight git server with a basic CLI to manage repositories, supporting multiple accounts and running in a container. `MIT` <sub>Docker</sub>
* [Octobox](https://octobox.io/) - Take back control of your GitHub Notifications. `AGPL-3.0` <sub>Ruby/Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OneDev](https://onedev.io/) - All-In-One DevOps Platform. With Git Management, Issue Tracking, and CI/CD. Simple yet Powerful. `MIT` <sub>Java/Docker/K8S</sub>
* [OpenProject](https://www.openproject.org) - Manage your projects, tasks and goals. Collaborate via work packages and link them to your pull requests on Github. `GPL-3.0` <sub>Ruby/deb/Docker</sub>
* [Pagure](https://pagure.io/pagure) - Lightweight, powerful, and flexible git-centric forge with features laying the foundation for federated and decentralized development. `GPL-2.0` <sub>Docker/Python/deb</sub>
* [Phorge](https://we.phorge.it/) - Community-driven platform for collaborating, managing, organizing and reviewing software development projects. `Apache-2.0` <sub>PHP</sub>
* [Plane](https://plane.so) - Track issues, epics, and product roadmaps in the simplest way possible (alternative to JIRA, Linear and Height). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [ProjeQtOr](https://www.projeqtor.org/) - Complete, mature, multi-user project management system with extensive functionality for all phases of a project. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Redmine](https://www.redmine.org/) - Flexible project management web application. `GPL-2.0` <sub>Ruby</sub>
* [Review Board](https://www.reviewboard.org/) - Extensible and friendly code review tool for projects and companies of all sizes. `MIT` <sub>Python/Docker</sub>
* [RhodeCode](https://rhodecode.com/) - Unify and simplify repository management for Git, Subversion, and Mercurial. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Rukovoditel](https://www.rukovoditel.net/) - Configurable open source project management, web-based application. `GPL-2.0` <sub>PHP</sub>
* [SCM Manager](https://www.scm-manager.org/) - The easiest way to share and manage your Git, Mercurial and Subversion repositories over http. `BSD-3-Clause` <sub>Java/deb/Docker/K8S</sub>
* [ShipShipShip](https://shipshipship.io) - Changelog and roadmap platform that bridges project management and customer communication. `Apache-2.0` <sub>Docker</sub>
* [Smederee](https://smeder.ee) - A frugal platform which is dedicated to help people build great software together leveraging the power of the Darcs version control system. `AGPL-3.0` <sub>Scala</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Sourcehut](https://sourcehut.org/) - A full web git interface with no javascript. `GPL-2.0` <sub>Go</sub>
* [Taiga](https://www.taiga.io/) - Agile Project Management Tool based on the Kanban and Scrum methods. `MPL-2.0` <sub>Docker/Python/Nodejs</sub>
* [Titra](https://titra.io/) - Time-tracking solution for freelancers and small teams. `GPL-3.0` <sub>Javascript/Docker</sub>
* [Trac](https://trac.edgewall.org/) - Trac is an enhanced wiki and issue tracking system for software development projects. `BSD-3-Clause` <sub>Python/deb</sub>
* [Traq](https://traq.io/) - Project management and issue tracking system written in PHP. `GPL-3.0` <sub>PHP/Nodejs</sub>
* [Tuleap](https://www.tuleap.org/) - Tuleap is a libre suite to plan, track, code and collaborate on software projects. `GPL-2.0` <sub>PHP</sub>
* [UVDesk](https://www.uvdesk.com/) - UVDesk community is a service oriented, event driven extensible opensource helpdesk system that can be used by your organization to provide efficient support to your clients effortlessly whichever way you imagine. `MIT` <sub>PHP</sub>
* [ZenTao](https://www.zentao.pm/) - An agile(scrum) project management system/tool. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Desenvolvimento — localização e tradução

* [Accent](https://www.accent.reviews/) - Developer-oriented translation tool. `BSD-3-Clause` <sub>Elixir/Docker</sub>
* [Tolgee](https://tolgee.io) - Developer & translator friendly web-based localization platform enabling users to translate directly in the app they develop. `Apache-2.0` <sub>Docker/Java</sub>
* [Traduora](https://traduora.co) - Translation management platform for teams. `AGPL-3.0` <sub>Docker/K8S/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Weblate](https://weblate.org) - Web-based translation tool with tight version control integration. `GPL-3.0` <sub>Python/Docker/K8S</sub>

## Desenvolvimento — low code

* [Appsmith](https://www.appsmith.com/) - Build admin panels, CRUD apps and workflows. Build everything you need, 10x faster. `Apache-2.0` <sub>Java/Docker/K8S</sub>
* [Appwrite](https://appwrite.io) - End to end backend server for web, native, and mobile developers 🚀. `BSD-3-Clause` <sub>Docker</sub>
* [Halo](https://www.halo.run) - A powerful and easy-to-use website building tool (documentation in Chinese). `GPL-3.0` <sub>Java/Docker</sub>
* [Manifest](https://manifest.build) - Complete backend that fits into 1 YAML file. `MIT` <sub>Nodejs</sub>
* [PocketBase](https://pocketbase.io/) - Backend for your next SaaS and Mobile app in one file. `MIT` <sub>Go/Docker</sub>
* [Saltcorn](https://saltcorn.com/) - No-code database application builder for web and mobile applications. One platform for user interface, data backend, durable workflows, email, PDF generation, and AI applications. `MIT` <sub>Docker/Nodejs</sub>
* [SQLPage](https://sql-page.com) - SQL-only dynamic website builder. `MIT` <sub>Rust/Docker</sub>
* [ToolJet](https://tooljet.io/) - Low-code framework to build & deploy internal tools with minimal engineering effort (alternative to Retool and Mendix). `GPL-3.0` <sub>Nodejs/Docker/K8S</sub>
* [TrailBase](https://trailbase.io/) - Open, sub-millisecond, single-executable FireBase alternative with type-safe REST & realtime APIs, built-in JS/TS runtime, auth & admin UI. `OSL-3.0` <sub>Rust/Docker</sub>

## Desenvolvimento — testes

* [Bencher](https://bencher.dev/) - Suite of continuous benchmarking tools designed to catch performance regressions in CI. `MIT/Apache-2.0` <sub>Rust</sub>
* [Request Inbox](https://request-inbox.com/) - Collect and inspect HTTP requests for testing and debugging. Create and manage inboxes, capture detailed request data, configure custom responses. `Apache-2.0` <sub>Docker</sub>
* [WebHook Tester](https://github.com/tarampampam/webhook-tester) - Powerful tool for testing WebHooks and more. `MIT` <sub>Docker/Go/deb/K8S</sub>

## Diversos

* [2FAuth](https://github.com/Bubka/2FAuth) - Manage your Two-Factor Authentication (2FA) accounts and generate their security codes. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Anchr](https://anchr.io) - Toolbox for tiny tasks on the internet, including bookmark collections, URL shortening and (encrypted) image uploads. `GPL-3.0` <sub>Nodejs</sub>
* [Anubis](https://anubis.techaro.lol/) - Web AI firewall utility which protects upstream resources from scraper bots. `MIT` <sub>Docker/deb/Go</sub>
* [asciinema](https://asciinema.org/) - Web app for hosting asciicasts. `Apache-2.0` <sub>Elixir/Docker</sub>
* [Baby Buddy](https://github.com/babybuddy/babybuddy) - Helps caregivers track baby sleep, feedings, diaper changes, and tummy time. `BSD-2-Clause` <sub>Python</sub>
* [ClipCascade](https://github.com/Sathvik-Rao/ClipCascade) - Syncs your clipboard across multiple devices instantly, without any button press. Available on Windows, macOS, Linux, and Android, it provides seamless and secure clipboard sharing with end-to-end data encryption. `GPL-3.0` <sub>Java/Docker</sub>
* [Cloudlog](https://magicbug.co.uk/cloudlog/) - Log your amateur radio contacts anywhere. `MIT` <sub>PHP/Docker</sub>
* [ConvertX](https://github.com/C4illin/ConvertX) - Online file converter which supports over a thousand different formats. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [CUPS](https://www.cups.org/) - The Common Unix Print System uses Internet Printing Protocol (IPP) to support printing to local and network printers. `GPL-2.0` <sub>C</sub>
* [CyberChef](https://github.com/gchq/CyberChef) - Perform all manner of operations within a web browser such as AES, DES and Blowfish encryption and decryption, creating hexdumps, calculating hashes, and much more. `Apache-2.0` <sub>Javascript</sub>
* [Digiboard](https://digiboard.app/) - Create collaborative whiteboards (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digicard](https://codeberg.org/ladigitale/digicard) - Create simple graphic compositions (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digicut](https://ladigitale.dev/digicut/) - Cut audio and video files using FFMPEG.wasm (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiface](https://ladigitale.dev/digiface/) - Create avatars using the Avataaars library (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiflashcards](https://ladigitale.dev/digiflashcards/) - An online application to create flashcards (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digimerge](https://ladigitale.dev/digimerge/) - Assemble audio and video files directly in your browser (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiquiz](https://ladigitale.dev/digiquiz/) - An online application to publish content created with H5P (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiread](https://ladigitale.dev/digiread/) - Clean up online pages and articles using Mozilla's Readability (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digisteps](https://ladigitale.dev/digisteps/) - A simple application for creating online educational paths (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digitranscode](https://ladigitale.dev/digitranscode) - Convert audio files and videos directly in the browser (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiview](https://ladigitale.dev/digiview/) - View YouTube videos in a distraction-free interface (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiwords](https://ladigitale.dev/digiwords/) - A simple online application for creating word clouds (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [DOCAT](https://github.com/docat-org/docat) - Host your docs. Simple. Versioned. Fancy. `MIT` <sub>Python/Docker</sub>
* [Domain Locker](https://domain-locker.com) - Domain name portfolio management and tracker. `MIT` <sub>Deno/Docker</sub>
* [DOMJudge](https://www.domjudge.org/) - System for running a programming contest, like the ICPC regional and world championship programming contests. `GPL-2.0/BSD-3-Clause/MIT` <sub>PHP</sub>
* [ESMira](https://esmira.kl.ac.at) - Run longitudinal studies (ESM, AA, EMA) with data collection and communication with participants being completely anonymous. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [F-Droid](https://f-droid.org) - Server tools for maintaining an F-Droid repository system. `AGPL-3.0` <sub>Python/Docker/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Flyimg](https://flyimg.io) - Resize and crop images on the fly. Get optimised images with MozJPEG, WebP or PNG using ImageMagick, with an efficient caching system. `MIT` <sub>Docker</sub>
* [Garlic-Hub](https://garlic-signage.com/garlic-hub/) - Digital signage device and content management system with SMIL playlist support and scheduling. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Geeftlist](https://codeberg.org/nanawel/geeftlist) - Collaborative platform for managing, sharing and reserving gifts between friends and family. `GPL-3.0` <sub>Docker</sub>
* [google-webfonts-helper](https://github.com/majodev/google-webfonts-helper) - Hassle-Free Way to Self-Host Google Fonts. Get eot, ttf, svg, woff and woff2 files + CSS snippets. `MIT` <sub>Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Habitica](https://habitica.com/) - Habit tracker app which treats your goals like a Role Playing Game. `GPL-3.0/CC-BY-SA-3.0` <sub>Nodejs/Docker</sub>
* [HortusFox](https://hortusfox.github.io) - Collaborative plant management and tracking system for plant enthusiasts. `MIT` <sub>PHP/Docker</sub>
* [ImgCompress](https://imgcompress.karimzouine.com) - Image processing tool that runs entirely in Docker. Compress, convert, resize, batch-process images, and remove backgrounds using local AI without cloud dependencies. `GPL-3.0` <sub>Docker</sub>
* [Infisical Community Edition](https://infisical.com/) - Platform for secrets, certificates, and privileged access management. `MIT` <sub>Docker/K8S/deb</sub>
* [iSponsorBlockTV](https://github.com/dmunozv04/iSponsorBlockTV) - Block and skip sponsors, while also muting and skipping ads on YouTube. `GPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [IT-Tools by sharevb](https://github.com/sharevb/it-tools) - Collection of handy online tools for developers (fork of [it-tools](https://github.com/CorentinTh/it-tools)). `GPL-3.0` <sub>Docker</sub>
* [Jelu](https://bayang.github.io/jelu-web) - Read and to-read list book tracker. `MIT` <sub>Java/Docker</sub>
* [jetlog](https://github.com/pbogre/jetlog) - Personal flight tracker and viewer. `GPL-2.0` <sub>Docker</sub>
* [Kasm Workspaces](https://kasmweb.com/) - Streaming containerized apps and desktops to end-users. Examples include Ubuntu in your browser, or simply single apps such as Chrome, OpenOffice, Gimp, Filezilla etc. `GPL-3.0` <sub>Docker</sub>
* [Koillection](https://koillection.github.io/) - Koillection is a service allowing users to manage any kind of collections. `MIT` <sub>Docker/PHP</sub>
* [LanguageTool](https://languagetool.org/) - Proofread more than 20 languages. It finds many errors that a simple spell checker cannot detect. `LGPL-2.1` <sub>Java/Docker</sub>
* [Libre Translate](https://libretranslate.com/) - Machine Translation API. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LubeLogger](https://lubelogger.com) - Web-based vehicle maintenance and fuel mileage tracker. `MIT` <sub>Docker/K8S/C#</sub>
* [Mirumoji](https://svdc1.github.io/mirumoji/docs) - Japanese immersion toolkit providing clickable, tokenized subtitles with dictionary lookups and transcription generation. `MIT` <sub>Docker/Python</sub>
* [mosparo](https://mosparo.io/) - The modern spam protection tool. It replaces other captcha methods with a simple and easy to use spam protection solution. `MIT` <sub>PHP</sub>
* [Movary](https://github.com/leepeuker/movary) - Web app to track and rate your watched movies. `MIT` <sub>Docker/PHP</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Neko](https://neko.m1k1o.net) - Virtual browser that runs in docker and uses WebRTC. `Apache-2.0` <sub>Docker/Go</sub>
* [OmniTools](https://omnitools.app/) - Collection of powerful web-based tools for everyday tasks (coding, manipulating images/videos, PDFs or crunching numbers...). `MIT` <sub>Docker</sub>
* [Open-Meteo](https://open-meteo.com/) - Weather API with open-data forecasts, historical and climate data from all major national weather services. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpenReader](https://openreader.richardr.dev/) - EPUB, PDF, DOCX, MD, and TXT file text to speech document reader. Read documents in realtime with high-quality TTS; or extract audiobooks. `MIT` <sub>Docker</sub>
* [OpenZiti](https://openziti.io/) - Fully-featured, zero trust, full mesh overlay network. Includes a 2FA support out of the box, clients for all major desktop/mobile OS'es. `Apache-2.0` <sub>Go</sub>
* [Operational.co](https://operational.co) - Receive alerts in a live timeline from your product. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [penpot](https://penpot.app/) - Web-based design and prototyping platform meant for cross-domain teams. `MPL-2.0` <sub>Docker</sub>
* [POMjs](https://password.oppetmoln.se/) - Random password generator. `GPL-2.0` <sub>Javascript</sub>
* [Pønskelisten](https://github.com/aunefyren/poenskelisten) - Sharing wishlists and collaborating on gifts and presents. `GPL-3.0` <sub>Docker/Go</sub>
* [re:Director](https://re-director.github.io/) - Simple domain redirection management tool. `Apache-2.0` <sub>Java/Docker</sub>
* [Reactive Resume](https://rxresu.me/) - One-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable, portable, open-source and free forever. `MIT` <sub>Docker/Nodejs</sub>
* [revealjs](https://revealjs.com) - Framework for easily creating beautiful presentations using HTML. `MIT` <sub>Javascript</sub>
* [Revive Adserver](https://www.revive-adserver.com/) - Ad serving system. Formerly known as OpenX Adserver and phpAdsNew. `GPL-2.0` <sub>PHP</sub>
* [SANE Network Scanning](http://sane-project.org/) - Allow remote clients to access image acquisition devices (scanners) available on the local host. `GPL-2.0` <sub>C</sub>
* [string.is](https://string.is/) - An open-source, privacy-friendly online string toolkit for developers. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Teleport](https://goteleport.com/) - Certificate authority and access plane for SSH, Kubernetes, web applications, and databases. `Apache-2.0` <sub>Go/Docker/K8S</sub>
* [TeslaMate](https://github.com/teslamate-org/teslamate) - A powerful data logger for Tesla vehicles. `MIT` <sub>Elixir/Docker</sub>
* [Transmute](https://transmute.sh) - File converter for images, video, audio, json, excel and more. Supports over 2,000 conversions!. `MIT` <sub>Docker</sub>
* [URL-to-PNG](https://github.com/jasonraimondi/url-to-png) - URL to PNG utility featuring parallel rendering using Playwright for screenshots and with storage caching via Local, S3, or CouchDB. `MIT` <sub>Nodejs/Docker</sub>
* [Usertour](https://www.usertour.io/) - User onboarding platform allowing you to create in-app product tours, checklists, and surveys in minutes effortlessly. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Warracker](https://warracker.com) - Warranty tracker that lets you monitor expiry dates, upload receipts/files, and get alerts before warranties expire. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Wavelog](https://www.wavelog.org) - Webbased Logging Software for Radio Amateurs. Enhanced QSO logging, statistics and maps for your browser. `MIT` <sub>PHP/Docker</sub>
* [WeeWX](https://weewx.com/) - Open source software for your weather station. `GPL-3.0` <sub>Python/deb</sub>
* [WeTTY](https://butlerx.github.io/wetty/#/) - Terminal in browser over http/https. `MIT` <sub>Docker/Nodejs</sub>
* [Wishlist](https://github.com/cmintey/wishlist) - Wishlist application that you can share with your friends and family. `MIT` <sub>Docker/K8S</sub>
* [Yamtrack](https://github.com/FuzzyGrim/Yamtrack) - Media tracker for movies, tv shows, anime, manga, video games and books. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Zero-TOTP](https://zero-totp.com) - Complete, reliable, secure and zero-trust webapp based on zero-knowledge encryption to store your TOTP codes. `GPL-3.0` <sub>Docker</sub>

## Documentos — e-books

* [Atsumeru](https://atsumeru.xyz) - Manga/comic/light novel media server with clients for Windows, Linux, macOS and Android. `MIT` <sub>Java/Docker</sub>
* [Bindery](https://github.com/jarynclouatre/bindery) - Folder-watching converter for e-books and comics. EPUB to Kobo KEPUB via kepubify, CBZ/CBR/PDF via Kindle Comic Converter, with per-device profiles, ComicInfo.xml naming, chapter-to-volume bundling and a web UI. `MIT` <sub>Docker</sub>
* [BookLogr](https://github.com/Mozzo1000/booklogr) - Manage your personal book library with ease. `Apache-2.0` <sub>Docker</sub>
* [Calibre](https://calibre-ebook.com/) - E-book library manager that can view, convert, and catalog e-books in most of the major e-book formats and provides a built-in Web server for remote clients. `GPL-3.0` <sub>Python/deb</sub>
* [Calibre Web](https://github.com/janeczku/calibre-web) - Browse, read and download eBooks using an existing Calibre database. `GPL-3.0` <sub>Python</sub>
* [Calibre Web Automated](https://github.com/crocodilestick/Calibre-Web-Automated) - All-in-one solution, combining the modern lightweight web UI from Calibre-Web with the robust, versatile feature set of Calibre (fork of Calibre Web). `GPL-3.0` <sub>Docker</sub>
* [Inkheart](https://gitlab.com/Nystik/inkheart) - Lightweight PDF library and reader. `Apache-2.0` <sub>Docker</sub>
* [Kapowarr](https://casvt.github.io/Kapowarr/) - Build and manage a comic book library. Download, rename, move and convert issues of the volume to your liking. `GPL-3.0` <sub>Docker/Python</sub>
* [Kavita](https://www.kavitareader.com/) - Cross-platform e-book/manga/comic/pdf server and web reader with user management, ratings and reviews, and metadata support. `GPL-3.0` <sub>.NET/Docker</sub>
* [kiwix-serve](https://github.com/kiwix/kiwix-tools) - HTTP daemon for serving wikis from ZIM files. `GPL-3.0` <sub>C++</sub>
* [Komga](https://komga.org) - Media server for comics/mangas/BDs with API and OPDS support, a modern web interface for exploring your libraries, as well as a web reader. `MIT` <sub>Java/Docker</sub>
* [MyMangaDB](https://github.com/FabianRolfMatthiasNoll/MyMangaDB) - Manga collection manager with automatic metadata, MyAnimeList import and detailed collection statistics. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Stump](https://www.stumpapp.dev) - A fast, free and open source comics, manga and digital book server with OPDS support. `MIT` <sub>Rust</sub>

## Documentos — repositórios e bibliotecas digitais

* [DSpace](http://www.dspace.org/) - Turnkey repository application providing durable access to digital resources. `BSD-3-Clause` <sub>Java</sub>
* [EPrints](https://www.eprints.org/) - Digital document management system with a flexible metadata and workflow model primarily aimed at academic institutions. `GPL-3.0` <sub>Perl</sub>
* [Fedora Commons Repository](https://wiki.lyrasis.org/display/FF/Fedora+Repository+Home) - Robust and modular repository system for the management and dissemination of digital content especially suited for digital libraries and archives, both for access and preservation. `Apache-2.0` <sub>Java</sub>
* [InvenioRDM](https://inveniordm.docs.cern.ch/) - Highly scalable turn-key research data management platform with a beautiful user experience. `MIT` <sub>Python</sub>
* [Islandora](https://www.islandora.ca/) - Drupal module for browsing and managing Fedora-based digital repositories. `GPL-3.0` <sub>PHP</sub>
* [Samvera Hyrax](https://samvera.org/) - Front-end for the Samvera framework, which itself is a Ruby on Rails application for browsing and managing Fedora-based digital repositories. `Apache-2.0` <sub>Ruby</sub>

## Documentos — sistemas de biblioteca

* [Evergreen](https://evergreen-ils.org) - Highly-scalable software for libraries that helps library patrons find library materials, and helps libraries manage, catalog, and circulate those materials. `GPL-2.0` <sub>PLpgSQL</sub>
* [Koha](https://koha-community.org/) - Enterprise-class ILS with modules for acquisitions, circulation, cataloging, label printing, offline circulation for when Internet access is not available, and much more. `GPL-3.0` <sub>Perl</sub>
* [RERO ILS](https://rero21.ch/) - Large-scale ILS that can be run as a service with consortial features, intended primarily for library networks. Includes most standard modules (circulation, acquisitions, cataloging,...) and a web-based public and professional interface. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## E-mail — clientes web

* [Cypht](https://cypht.org) - Feed reader for your email accounts. `LGPL-2.1` <sub>PHP</sub>
* [Roundcube](https://roundcube.net) - Browser-based IMAP client with an application-like user interface. `GPL-3.0` <sub>PHP/deb</sub>
* [SnappyMail](https://github.com/the-djmaze/snappymail) - Simple, modern, lightweight & fast web-based email client (fork of RainLoop). `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SquirrelMail](https://squirrelmail.org) - Another browser-based IMAP client. `GPL-2.0` <sub>PHP</sub>

## E-mail — entrega (MDA)

* [Cyrus IMAP](https://www.cyrusimap.org/) - Email (IMAP/POP3), contacts and calendar server. `BSD-3-Clause-Attribution` <sub>C</sub>
* [DavMail](https://davmail.sourceforge.net/) - POP/IMAP/SMTP/Caldav/Carddav/LDAP exchange gateway allowing users to use any mail/calendar client with an Exchange server, even from the internet or behind a firewall through Outlook Web Access. `GPL-2.0` <sub>Java</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Dovecot](https://www.dovecot.org/) - IMAP and POP3 server written primarily with security in mind. `MIT/LGPL-2.1` <sub>C/deb</sub>

## E-mail — listas e newsletters

* [HyperKitty](https://wiki.list.org/HyperKitty) - Access GNU Mailman v3 archives. `GPL-3.0` <sub>Python</sub>
* [Keila](https://www.keila.io) - Reliable and easy-to-use newsletter tool (alternative to Mailchimp and Sendinblue). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Listmonk](https://listmonk.app/) - High performance, self-hosted newsletter and mailing list manager with a modern dashboard. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Mailman](https://www.list.org/) - Manage electronic mail discussion and e-newsletter lists. `GPL-3.0` <sub>Python</sub>
* [Mautic](https://www.mautic.org/) - Marketing automation software (email, social and more). `GPL-3.0` <sub>PHP</sub>
* [mlmmj](https://mlmmj.org/) - Mailing list management made joyful. `MIT` <sub>C</sub>
* [phpList](https://www.phplist.org) - Newsletter and email marketing with advanced management of subscribers, bounces, and plugins. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Postorius](https://docs.mailman3.org/projects/postorius/en/latest/) - Web user interface to access GNU Mailman. `GPL-3.0` <sub>Python</sub>
* [Schleuder](https://schleuder.nadir.org/) - GPG-enabled mailing list manager with resending-capabilities. `GPL-3.0` <sub>Ruby</sub>
* [Sympa](https://www.sympa.community/) - Mailing list manager. `GPL-2.0` <sub>Perl</sub>

## E-mail — soluções completas

* [AnonAddy](https://anonaddy.com) - Email forwarding service for creating aliases. `MIT` <sub>PHP/Docker</sub>
* [b1gMail](https://www.b1gmail.eu) - Complete email solution that runs on any webspace with PHP and MariaDB. It supports POP3 catchall mailboxes and can also integrate with Postfix or b1gMailServer if you're running your own server. `GPL-2.0` <sub>PHP</sub>
* [DebOps](https://docs.debops.org/) - Your Debian-based data center in a box. A set of general-purpose Ansible roles that can be used to manage Debian or Ubuntu hosts. `GPL-3.0` <sub>Ansible/Python</sub>
* [docker-mailserver](https://docker-mailserver.github.io/docker-mailserver/edge/) - Production-ready fullstack but simple mail server (SMTP, IMAP, LDAP, Antispam, Antivirus, etc.) running inside a container. Only configuration files, no SQL database. `MIT` <sub>Docker</sub>
* [Inboxen](https://inboxen.org) - Lets you have an infinite number of unique inboxes. `GPL-3.0` <sub>Python</sub>
* [iRedMail](https://www.iredmail.org/) - Full-featured mail server solution based on Postfix and Dovecot. `GPL-3.0` <sub>Shell</sub>
* [Maddy Mail Server](https://maddy.email/) - All-in-one mail server that implements SMTP (both MTA and MX) and IMAP. Replaces Postfix, Dovecot, OpenDKIM, OpenSPF, OpenDMARC with single daemon. `GPL-3.0` <sub>Go</sub>
* [Mail-in-a-Box](https://mailinabox.email/) - Turns any Ubuntu server into a fully functional mail server with one command. `CC0-1.0` <sub>Shell</sub>
* [Mailcow](https://mailcow.email/) - Mail server suite based on Dovecot, Postfix and other open source software, that provides a modern Web UI for administration. `GPL-3.0` <sub>Docker/PHP</sub>
* [Mailu](https://mailu.io/) - Simple yet full-featured mail server as a set of Docker images. `MIT` <sub>Docker/Python</sub>
* [Modoboa](https://modoboa.org/en/) - Mail hosting and management platform including a modern and simplified web user interface. `ISC` <sub>Python</sub>
* [Mox](https://www.xmox.nl/) - Complete e-mail solution with IMAP4, SMTP, SPF, DKIM, DMARC, MTA-STS, DANE and DNSSEC, reputation-based and content-based junk filtering, Internationalization (IDNA), automatic TLS with ACME and Let's Encrypt, account autoconfiguration, and webmail. `MIT` <sub>Go</sub>
* [Postal](https://docs.postalserver.io/) - Complete and fully featured mail server for use by websites & web servers. `MIT` <sub>Docker/Ruby</sub>
* [Simple NixOS Mailserver](https://gitlab.com/simple-nixos-mailserver/nixos-mailserver) - Complete mailserver solution leveraging the Nix Ecosystem. `GPL-3.0` <sub>Nix</sub>
* [SimpleLogin](https://simplelogin.io) - Open source email alias solution to protect your email address. Comes with browser extensions and mobile apps. `MIT` <sub>Docker/Python</sub>
* [Stalwart Mail Server](https://stalw.art) - All-in-one mail server with JMAP, IMAP4, and SMTP support and a wide range of modern features. `AGPL-3.0` <sub>Rust/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [wildduck](https://wildduck.email/) - Scalable no-SPOF IMAP/POP3 mail server. `EUPL-1.2` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>

## E-mail — transporte (MTA)

* [chasquid](https://blitiri.com.ar/p/chasquid/) - SMTP (email) server with a focus on simplicity, security, and ease of operation. `Apache-2.0` <sub>Go</sub>
* [Courier MTA](https://www.courier-mta.org/) - Fast, scalable, enterprise mail/groupware server providing ESMTP, IMAP, POP3, webmail, mailing list, basic web-based calendaring and scheduling services. `GPL-3.0` <sub>C/deb</sub>
* [DragonFly](https://github.com/corecode/dma) - A small MTA for home and office use. Works on Linux and FreeBSD. `BSD-3-Clause` <sub>C</sub>
* [EmailRelay](https://emailrelay.sourceforge.net/) - A small and easy to configure SMTP and POP3 server for Windows and Linux. `GPL-3.0` <sub>C++</sub>
* [Exim](https://www.exim.org/) - Message transfer agent (MTA) developed at the University of Cambridge. `GPL-3.0` <sub>C/deb</sub>
* [Haraka](https://haraka.github.io/) - Fast, highly extensible, and event driven SMTP server. `MIT` <sub>Nodejs</sub>
* [OpenSMTPD](https://opensmtpd.org/) - Secure SMTP server implementation from the OpenBSD project. `ISC` <sub>C/deb</sub>
* [Postfix](http://www.postfix.org/) - Fast, easy to administer, and secure Sendmail replacement. `IPL-1.0` <sub>C/deb</sub>
* [Sendmail](https://www.proofpoint.com/us/products/email-protection/open-source-email-solution) - Message transfer agent (MTA). `Sendmail` <sub>C/deb</sub>

## Encurtadores de URL

* [bit](https://github.com/sjdonado/bit) - Fast, lightweight, resource-efficient, compiled URL shortener. `MIT` <sub>Docker/Crystal</sub>
* [Chhoto URL](https://chhoto.link) - Simple, lightning-fast URL shortener with no bloat (fork of simply-shorten). `MIT` <sub>Rust/Docker</sub>
* [clink](https://git.crueter.xyz/crueter/clink) - A super-minimal link shortening service written in pure C, focusing on small executable size, portability, and ease of configuration. `AGPL-3.0` <sub>C</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Flink](https://gitlab.com/rtraceio/web/flink) - Create QR Codes, embeddable link previews for your website and crawls/scrapes metadata. `MIT` <sub>Docker</sub>
* [Kutt](https://kutt.to) - Modern URL shortener with support for custom domains and custom URLs. `MIT` <sub>Nodejs/Docker</sub>
* [rs-short](https://git.42l.fr/42l/rs-short) - Lightweight link shortener written in Rust, with features such as caching, spambot protection and phishing detection. `MPL-2.0` <sub>Rust</sub>
* [Shlink](https://shlink.io) - URL shortener with REST API and command line interface. Includes official progressive web application and docker images. `MIT` <sub>PHP/Docker</sub>
* [Simple-URL-Shortener](https://github.com/azlux/Simple-URL-Shortener) - KISS URL shortener, public or private (with account). Minimalist and lightweight. No dependencies. `MIT` <sub>PHP</sub>
* [YOURLS](https://yourls.org/) - YOURLS is a set of PHP scripts that will allow you to run Your Own URL Shortener. Features include password protection, URL customization, bookmarklets, statistics, API, plugins, jsonp. `MIT` <sub>PHP</sub>

## Enquetes e eventos

* [Bitpoll](https://github.com/fsinfuhh/Bitpoll) - Conduct polls about dates, times or general questions. `GPL-3.0` <sub>Docker/Python</sub>
* [Bracket](https://docs.bracketapp.nl/) - Flexible tournament system to build a tournament setup, add teams, schedule matches, keep track of scores and present ranking live to the public. `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Christmas Community](https://github.com/Wingysam/Christmas-Community) - Create a simple place for your entire family to use to find gifts that people want, and to avoid double-gifting. `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Claper](https://claper.co/) - The ultimate tool to interact with your audience (alternative to Slido, AhaSlides and Mentimeter). `GPL-3.0` <sub>Elixir/Docker</sub>
* [ClearFlask](https://clearflask.com) - Community-feedback tool for managing incoming feedback and prioritizing a public roadmap (alternative to Canny, UserVoice, Upvoty). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [docassemble](https://docassemble.org/) - A free, open-source expert system for guided interviews and document assembly, based on Python, YAML, and Markdown. `MIT` <sub>Docker/Python</sub>
* [EventSchedule](https://eventschedule.com/) - Share events, sell tickets, and bring communities together. `AAL` <sub>PHP/Docker</sub>
* [Fider](https://fider.io) - Open platform to collect and prioritize feedback (alternative to UserVoice). `MIT` <sub>Docker</sub>
* [Formbricks](https://formbricks.com) - Experience Management Suite built on the largest open source survey stack worldwide. Gracefully gather feedback at every step of the customer journey to know what your customers need. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Framadate](https://framadate.org/abc/) - Online service for planning an appointment or make a decision quickly and easily: Make a poll, Define dates or subjects to choose, Send the poll link to your friends or colleagues, Discuss and make a decision. `CECILL-B` <sub>PHP</sub>
* [Gancio](https://gancio.org/) - Local community event and agenda sharing. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [gathio](https://docs.gath.io/) - Self-destructing, shareable, no-registration event pages. `GPL-3.0` <sub>Nodejs/Docker</sub>
* [HeyForm](https://heyform.net) - Form builder that allows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [hitobito](https://hitobito.com) - Manage complex group hierarchies with members, events and a lot more. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LimeSurvey](https://www.limesurvey.org) - Feature-rich web-based polling software. Supports extensive survey logic. `GPL-2.0` <sub>PHP</sub>
* [Meetable](https://events.indieweb.org) - Minimal events aggregator. `MIT` <sub>PHP</sub>
* [Mobilizon](https://mobilizon.org) - Federated tool that helps you find, create and organise events and groups. `AGPL-3.0` <sub>Elixir/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpnForm](https://opnform.com) - Beautiful open-source form builder. `AGPL-3.0` <sub>PHP/Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Revel](https://www.letsrevel.io) - Community-focused event management and ticketing platform. `MIT` <sub>Python/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>

## Ensino e cursos

* [Canvas LMS](https://www.instructure.com/canvas/) - Learning management system (LMS) that is revolutionizing the way we educate. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Chamilo LMS](https://chamilo.org/) - Create a virtual campus for the provision of online or semi-online training. `GPL-3.0` <sub>PHP</sub>
* [Digiscreen](https://ladigitale.dev/digiscreen/) - Interactive whiteboard/wallpaper for the classroom, in person or remotely (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digitools](https://ladigitale.dev/digitools) - A set of simple tools to accompany the animation of courses in person or remotely. (documentation in French). `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [edX](https://www.edx.org/) - The Open edX platform is open-source code that powers edX.org. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Gibbon](https://gibbonedu.org/) - Flexible school management platform designed to make life better for teachers, students, parents and leaders. `GPL-3.0` <sub>PHP</sub>
* [Helium](https://www.heliumedu.com) - Color-coded student planner for classes, homework, grades, and notes with smart notifications and multi-device sync. `MIT` <sub>Python/Docker</sub>
* [ILIAS](https://www.ilias.de) - Learning management system that can cope with anything you throw at it. `GPL-3.0` <sub>PHP</sub>
* [INGInious](https://inginious.org/?lang=en) - Intelligent grader that allows secured and automated testing of code made by students. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Moodle](https://moodle.org/) - Learning and courses platform with one of the largest open source communities worldwide. `GPL-3.0` <sub>PHP</sub>
* [Open eClass](https://www.openeclass.org/) - Open eClass is an advanced e-learning solution that can enhance the teaching and learning process. `GPL-2.0` <sub>PHP</sub>
* [OpenOLAT](https://www.openolat.com/?lang=en) - Learning management system for teaching, education, assessment and communication. `Apache-2.0` <sub>Java</sub>
* [QST](https://qstonline.org) - Online assessment software. From a quick quiz on your phone to large scale, high stakes, proctored desktop testing, easy, secure and economical. `GPL-2.0` <sub>Perl</sub>
* [RELATE](https://documen.tician.de/relate/) - Courseware package that includes features such as: flexible rules, statistics, multi-course support, class calendar. `MIT` <sub>Python</sub>
* [RosarioSIS](https://www.rosariosis.org/) - Student Information System for school management. Features students demographics, grades, scheduling, attendance, student billing, discipline & food service modules. `GPL-2.0` <sub>PHP</sub>

## Favoritos e compartilhamento de links

* [Betula](https://joinbetula.org) - Single-user federated bookmark manager with Fediverse support and archives. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Buku](https://github.com/jarun/Buku) - Powerful bookmark manager and a personal textual mini-web. `GPL-3.0` <sub>Python/deb</sub>
* [Digibunch](https://ladigitale.dev/digibunch/#/) - Create bunches of links to share with your learners or colleagues. `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Espial](https://github.com/jonschoning/espial) - An open-source, web-based bookmarking server. `AGPL-3.0` <sub>Haskell</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Faved](https://faved.to/) - Handcrafted bookmark manager combining powerful tagging, instant search, and a clean, distraction-free interface. Built for large collections and advanced workflows, optimized for efficiency and ease-of-use. `MIT` <sub>Docker</sub>
* [Firefox Account Server](https://mozilla-services.readthedocs.io/en/latest/howtos/run-fxa.html) - Host your own Firefox accounts server. `MPL-2.0` <sub>Nodejs/Java</sub>
* [Karakeep](https://karakeep.app/) - Bookmark-everything app with a touch of AI for the data hoarders out there. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LinkAce](https://www.linkace.org/) - Bookmark archive with automatic backups to the Internet Archive, link monitoring, and a full REST API. Installation is done via Docker, or as a simple PHP application. `GPL-3.0` <sub>Docker/PHP</sub>
* [linkding](https://linkding.link/) - Minimal bookmark management with a fast and clean UI. Simple installation through Docker and can run on your Raspberry Pi. `MIT` <sub>Docker</sub>
* [LinkWarden](https://linkwarden.app/) - Bookmark and archive manager to store your useful links. `MIT` <sub>Docker/Nodejs</sub>
* [NeonLink](https://github.com/AlexSciFier/neonlink) - Bookmark service with unique design and simple installation with Docker. `MIT` <sub>Docker</sub>
* [Readeck](https://readeck.org/en/) - Save the precious readable content of web pages you like and want to keep forever. See it as a bookmark manager and a read later tool. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Servas](https://github.com/beromir/Servas) - A self-hosted bookmark management tool. It allows organization with tags, groups, and a list specifically for later access. It supports multiple users with 2FA. Companion browser extensions are available for Firefox and Chrome. `GPL-3.0` <sub>Docker/Nodejs/PHP</sub>
* [Shaarli](https://github.com/shaarli/Shaarli) - Personal, minimalist, super-fast, no-database bookmarking and link sharing platform. `Zlib` <sub>PHP/deb</sub>
* [Shiori](https://github.com/go-shiori/shiori) - Simple bookmark manager built with Go. `MIT` <sub>Go/Docker</sub>
* [Slash](https://github.com/yourselfhosted/slash) - An open source, self-hosted bookmarks and link sharing platform. `GPL-3.0` <sub>Docker</sub>
* [SyncMarks](https://codeberg.org/Offerel/SyncMarks-Webapp) - Sync and manage your browser bookmarks from Edge, Firefox and Chromium. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Finanças pessoais e orçamento

* [Actual](https://actualbudget.org) - Local-first personal finance tool based on zero-sum budgeting, supporting synchronization across devices, custom rules, manual transaction importing (from QIF, OFX, and QFX files), and optional automatic synchronization with many banks. `MIT` <sub>Nodejs/Docker</sub>
* [Bigcapital](https://bigcapital.app/) - Financial accounting and inventory management software for small to medium businesses. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Bitcart](https://bitcart.ai) - Cryptocurrencies payment processor and development platform. `MIT` <sub>Docker/Python/Nodejs</sub>
* [BTCPay Server](https://btcpayserver.org/) - Bitcoin and other cryptocurrencies payment processor. `MIT` <sub>C#</sub>
* [Budget Board](https://budgetboard.net/) - Simple app for tracking monthly spending and working towards financial goals. `GPL-3.0` <sub>Docker</sub>
* [DePay](https://depay.com) - Accept Web3 Payments directly into your wallet. Peer-to-peer, free, self-hosted & open-source. `MIT` <sub>Nodejs</sub>
* [Econumo](https://econumo.com) - Budgeting application for managing personal and family finances, supporting multiple currencies, joint accounts, and budgets. `MIT` <sub>Docker</sub>
* [ExpenseOwl](https://github.com/tanq16/expenseowl) - Extremely simple expense tracker with a beautiful UI. `MIT` <sub>Go/Docker/K8S</sub>
* [ezbookkeeping](https://ezbookkeeping.mayswind.net/) - A lightweight personal bookkeeping app hosted by yourself. `MIT` <sub>Go/Docker</sub>
* [Family Accounting Tool](https://github.com/nymanjens/facto) - Web-based finance management tool for partners with partially shared expenses. `Apache-2.0` <sub>Scala</sub>
* [Fava](https://beancount.github.io/fava/) - Web frontend of Beancount, a text based double-entry accounting system. `MIT` <sub>Python</sub>
* [Firefly III](https://firefly-iii.org/) - Firefly III is a modern financial manager. It helps you to keep track of your money and make budget forecasts. It supports credit cards, has an advanced rule engine and can import data from many banks. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [FOSSBilling](https://fossbilling.org/) - Hosting and billing automation. Integrates with WHM, CWP, cPanel and HestiaCP. Full API and easily extensible. `Apache-2.0` <sub>PHP/Docker</sub>
* [Galette](https://galette.eu/) - Membership management web application aimed towards non profit organizations. `GPL-3.0` <sub>PHP</sub>
* [Ghostfolio](https://ghostfol.io/) - Wealth management software to keep track of stocks, ETFs and cryptocurrencies. `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [GRR](https://grr.devome.com/?lang=en) - Assets management and booking for small/medium companies. `GPL-2.0` <sub>PHP</sub>
* [HyperSwitch](https://hyperswitch.io/) - Payment switch to make payments fast, reliable and affordable. Connect with multiple payment processors and route traffic effortlessly, all with a single API integration. `Apache-2.0` <sub>Docker/Rust</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [IHateMoney](https://ihatemoney.org/) - Manage your shared expenses, easily. `BSD-3-Clause` <sub>Docker/Python</sub>
* [InvoicePlane](https://www.invoiceplane.com/) - Manage quotes, invoices, payments and customers for your small business. `MIT` <sub>PHP</sub>
* [InvoiceShelf](https://invoiceshelf.com/) - Track expenses, payments & create professional invoices & estimates (fork of Crater). `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kill Bill](https://killbill.io/) - Subscription billing & payments platform. Have access to real-time analytics and financial reports. `Apache-2.0` <sub>Java/Docker</sub>
* [Kresus](https://kresus.org/) - Personal finance manager. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Lago](https://www.getlago.com/) - Metering and usage-based billing. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Mybucks.online](https://mybucks.online) - Secure, browser-based, password-only self-custodial cryptocurrency wallet. `MIT` <sub>Nodejs</sub>
* [MyFin Budget](https://myfinbudget.com) - Personal finances platform (web + REST API + Android) that'll help you budget, keep track of your income/spending and forecast your financial future. `GPL-3.0` <sub>Nodejs/Docker</sub>
* [OctoBot](https://www.octobot.cloud/) - Cryptocurrency trading bot. `GPL-3.0` <sub>Python/Docker</sub>
* [Ocular](https://simonwep.github.io/ocular/) - Simplistic and straightforward budgeting app to track your budget across months and years. `MIT` <sub>Docker</sub>
* [OpenBudgeteer](https://github.com/TheAxelander/OpenBudgeteer) - Budgeting app based on the Bucket Budgeting Principle. `AGPL-3.0` <sub>Docker/C#</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Receipt Wrangler](https://receiptwrangler.io) - Easy-to-use receipt manager, powered by AI. Allows users to create receipts effortlessly and quickly, categorize and more. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [REI3](https://rei3.de/home_en/) - Manage tasks, time, assets and much more within your business. `MIT` <sub>Go</sub>
* [SHKeeper](https://shkeeper.io/) - Cryptocurrency payment processor with the unique combination of gateway and merchant allowing you to accept payments in multiple cryptocurrencies without fees and intermediaries. `GPL-3.0` <sub>Python</sub>
* [SolidInvoice](https://solidinvoice.co) - Open source invoicing and quote application. `MIT` <sub>PHP</sub>
* [Sure](https://github.com/we-promise/sure) - Personal finance application for everyone (fork of Maybe). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [VoucherVault](https://github.com/l4rm4nd/VoucherVault) - Store and manage vouchers, coupons, loyalty and gift cards digitally. Supports expiry notifications, transaction histories, file uploads and OIDC SSO. `GPL-3.0` <sub>Docker</sub>
* [Wallos](https://wallosapp.com) - Lightweight personal subscription tracker with statistics and optional notifications. `GPL-3.0` <sub>PHP/Docker</sub>
* [WYGIWYH](https://github.com/eitchtee/WYGIWYH) - Simple and powerful finance tracker. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [YAFFA](https://www.yaffa.cc) - Personal finance web application, that can be used to keep track of your money, expenses, budgets, and investments. It also helps with long-term financial planning. `MIT` <sub>PHP</sub>

## Galerias de fotos

* [Chevereto](https://chevereto.com/) - Ultimate image sharing software. Create your very own personal image hosting website in just minutes. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [ChronoFrame](https://chronoframe.bh8.ga/) - Personal gallery application with online photo management, supporting Live/Motion Photos, and explore map. `MIT` <sub>Nodejs/Docker</sub>
* [Damselfly](https://damselfly.info) - Fast server-based photo management system for large collections of images. Includes face detection, face & object recognition, powerful search, and EXIF Keyword tagging. Runs on Linux, MacOS and Windows. `GPL-3.0` <sub>Docker/C#/.NET</sub>
* [Ente](https://ente.com/) - An end-to-end encrypted photo-sharing platform (alternative to Google Photos, Apple Photos). `AGPL-3.0` <sub>Docker/Nodejs/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [HomeGallery](https://home-gallery.org) - Browse personal photos and videos featuring tagging, mobile-friendly, and AI powered image discovery. `MIT` <sub>Nodejs/Docker</sub>
* [Immich](https://immich.app/) - Photo and video backup solution directly from your mobile phone (alternative to Google Photos). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Immich Kiosk](https://github.com/damongolding/immich-kiosk) - Lightweight slideshow for running on kiosk devices and browsers that uses Immich as a data source. `GPL-3.0` <sub>Docker/Go</sub>
* [LibrePhotos](https://github.com/LibrePhotos/librephotos) - Photo management service with a slight focus on cool graphs (alternative to Google Photos). `MIT` <sub>Python/Docker</sub>
* [Lychee](https://lycheeorg.github.io/) - Grid and album based photo-management-system. `MIT` <sub>PHP/Docker</sub>
* [Mediagoblin](https://mediagoblin.org) - Media publishing platform that anyone can run (alternative to Flickr, YouTube, SoundCloud). `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Memtly](https://docs.memtly.com/) - Event photo sharing platform and gallery with slideshow that allows guests to view and share memories via a QR code. `GPL-3.0` <sub>C#/Docker</sub>
* [Nextcloud Memories](https://memories.gallery/) - Fast, modern and advanced photo management suite. Runs as a Nextcloud app. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Photofield](https://github.com/SmilyOrg/photofield) - Experimental fast photo viewer. `MIT` <sub>Docker/Go</sub>
* [PhotoPrism](https://photoprism.org) - Personal photo management powered by Go and Google TensorFlow.  Browse, organize, and share your personal photo collection, using the latest technologies to automatically tag and find pictures. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Photoview](https://photoview.github.io/) - Simple and user-friendly photo gallery for personal servers. It is made for photographers and aims to provide an easy and fast way to navigate directories, with thousands of high resolution photos. `GPL-3.0` <sub>Go/Docker</sub>
* [PiGallery 2](https://bpatrik.github.io/pigallery2/) - Directory-first photo gallery website, with a rich UI, optimised for running on low resource servers. `MIT` <sub>Docker/Nodejs</sub>
* [Piwigo](https://piwigo.org/) - Photo gallery software for the web, built by an active community of users and developers. `GPL-2.0` <sub>PHP</sub>
* [SPIS](https://github.com/gbbirkisson/spis) - A simple, lightweight and fast media server with decent mobile support. `GPL-3.0` <sub>Docker/Rust</sub>
* [This week in past](https://github.com/RouHim/this-week-in-past) - Aggregates images taken this week, from previous years and presents them on a web page with a simple slideshow. `MIT` <sub>Docker/Rust</sub>
* [Thumbor](http://thumbor.org/) - A smart imaging service and enables on-demand cropping, resizing, applying filters and optimizing images. `MIT` <sub>Python/Docker</sub>
* [Zenphoto](https://www.zenphoto.org/) - Open-source gallery and CMS project. `GPL-2.0` <sub>PHP</sub>

## Genealogia

* [Genea.app](https://www.genea.app/) - Genealogy tool designed with privacy in mind that anyone can use to author or edit their family tree. Data is stored in the GEDCOM format and all processing is done in the browser. `MIT` <sub>Javascript</sub>
* [Genealogy](https://genealogy.kreaweb.be/) - Record family members and their relationships and build a family tree. `MIT` <sub>PHP</sub>
* [GeneWeb](https://github.com/geneweb/geneweb/wiki) - Genealogy software that can be used offline or as a Web service. `GPL-2.0` <sub>OCaml</sub>
* [Gramps Web](https://www.grampsweb.org/) - Web app for collaborative genealogy, based on and interoperable with Gramps, the open source genealogy desktop application. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [webtrees](https://www.webtrees.net) - Webtrees is the web's leading online collaborative genealogy application. `GPL-3.0` <sub>PHP</sub>

## Gerenciadores de conteúdo (CMS)

* [Alfresco Community Edition](https://www.alfresco.com/products/community/download) - The open source Enterprise Content Management software that handles any type of content, allowing users to easily share and collaborate on content. `LGPL-3.0` <sub>Java</sub>
* [Apostrophe](https://apostrophecms.com/) - CMS with a focus on extensible in-context editing tools. `MIT` <sub>Nodejs</sub>
* [Automad](https://automad.org/) - Flat-file content management system and template engine. `MIT` <sub>PHP/Docker</sub>
* [Backdrop CMS](https://backdropcms.org/) - Comprehensive CMS for small to medium sized businesses and non-profits. `GPL-2.0` <sub>PHP</sub>
* [Bludit](https://www.bludit.com/) - Build a site or blog in seconds. Bludit uses flat-files (text files in JSON format) to store posts and pages. `MIT` <sub>PHP</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Bolt CMS](https://boltcms.io/) - Content Management Tool, which strives to be as simple and straightforward as possible. `MIT` <sub>PHP</sub>
* [CMS Made Simple](https://www.cmsmadesimple.org/) - Faster and easier management of website contents, scalable for small businesses to large corporations. `GPL-2.0` <sub>PHP</sub>
* [Cockpit](https://getcockpit.com) - Simple content platform to manage any structured content. `MIT` <sub>PHP</sub>
* [Concrete 5 CMS](https://www.concretecms.com) - Open source content management system. `MIT` <sub>PHP</sub>
* [Contao](https://contao.org/) - Powerful CMS that allows you to create professional websites and scalable web applications. `LGPL-3.0` <sub>PHP</sub>
* [CouchCMS](https://www.couchcms.com/) - CMS for designers. `CPAL-1.0` <sub>PHP</sub>
* [Drupal](https://www.drupal.org/) - Advanced open source content management platform. `GPL-2.0` <sub>PHP</sub>
* [eLabFTW](https://www.elabftw.net) - Online lab notebook for research labs. Store experiments, use a database to find reagents or protocols, use trusted timestamping to legally timestamp an experiment, export as pdf or zip archive, share with collaborators…. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Expressa](https://github.com/thomas4019/expressa) - Content Management System for powering database driven websites using JSON schemas. Provides permission management and automatic REST APIs. `MIT` <sub>Nodejs</sub>
* [Joomla!](https://www.joomla.org/) - Advanced Content Management System (CMS). `GPL-2.0` <sub>PHP</sub>
* [KeystoneJS](https://keystonejs.com/) - CMS and web application platform. `MIT` <sub>Nodejs</sub>
* [Localess](https://localess.org/home) - Powerful translation management and content management system. Manage and translate your website or app content into multiple languages, using AI to translate faster. `MIT` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [MODX](https://modx.com/) - Advanced content management and publishing platform. The current version is called 'Revolution'. `GPL-2.0` <sub>PHP</sub>
* [Neos](https://www.neos.io) - Neos or TYPO3 Neos (for version 1) is a modern, open source CMS. `GPL-3.0` <sub>PHP</sub>
* [Noosfero](https://gitlab.com/noosfero/noosfero) - Platform for social and solidarity economy networks with blog, e-Portfolios, CMS, RSS, thematic discussion, events agenda and collective intelligence for solidarity economy in the same system. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Omeka](https://omeka.org) - Create complex narratives and share rich collections, adhering to Dublin Core standards with Omeka on your server, designed for scholars, museums, libraries, archives, and enthusiasts. `GPL-3.0` <sub>PHP</sub>
* [Payload CMS](https://payloadcms.com/) - Developer-first headless CMS and application framework. `MIT` <sub>Nodejs</sub>
* [Pimcore](http://www.pimcore.com/) - Multi-channel experience and engagement management platform. `GPL-3.0` <sub>PHP/Docker</sub>
* [Plone](https://plone.org/) - Powerful open-source CMS system. `ZPL-2.0` <sub>Python/Docker</sub>
* [Publify](https://publify.github.io/) - Simple but full featured web publishing software. `MIT` <sub>Ruby</sub>
* [Pushword](https://pushword.piedweb.com) - Content management system built on Symfony, where pages are Markdown and themes are Twig, with optional Git-based flat-file storage. `MIT` <sub>PHP</sub>
* [REDAXO](https://www.redaxo.org) - Simple, flexible and useful content management system (documentation in German). `MIT` <sub>PHP/Docker</sub>
* [SilverStripe](https://www.silverstripe.org) - Easy to use CMS with powerful MVC framework underlying. `BSD-3-Clause` <sub>PHP</sub>
* [SPIP](https://www.spip.net/fr) - Publication system for the Internet aimed at collaborative work, multilingual environments, and simplicity of use for web authors. `GPL-3.0` <sub>PHP</sub>
* [Squidex](https://squidex.io) - Headless CMS, based on MongoDB, CQRS and Event Sourcing. `MIT` <sub>.NET</sub>
* [Strapi](https://strapi.io/) - The most advanced open-source Content Management Framework (headless-CMS) to build powerful API with no effort. `MIT` <sub>Nodejs</sub>
* [Superdesk](https://superdesk.org/) - End-to-end news creation, production, curation, distribution, and publishing platform. `AGPL-3.0` <sub>Docker/Python/PHP</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Textpattern](https://textpattern.com/) - Flexible, elegant and easy-to-use CMS. `GPL-2.0` <sub>PHP</sub>
* [Typemill](https://typemill.net/) - Author-friendly flat-file-cms with a visual markdown editor based on vue.js. `MIT` <sub>PHP</sub>
* [TYPO3](https://typo3.org/) - Powerful and advanced CMS with a large community. `GPL-2.0` <sub>PHP</sub>
* [Umbraco](https://umbraco.com/) - The friendly CMS. Free and open source with an amazing community. `MIT` <sub>.NET</sub>
* [Vvveb CMS](https://www.vvveb.com) - Powerful and easy to use CMS to build websites, blogs or e-commerce stores. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Wagtail](https://wagtail.io/) - Django content management system focused on flexibility and user experience. `BSD-3-Clause` <sub>Python</sub>
* [WinterCMS](https://wintercms.com/) - Speedy and secure content management system built on the Laravel PHP framework. `MIT` <sub>PHP</sub>
* [WonderCMS](https://www.wondercms.com) - WonderCMS is the smallest flat file CMS since 2008. `MIT` <sub>PHP</sub>
* [WordPress](https://wordpress.org/) - World's most-used blogging and CMS engine. `GPL-2.0` <sub>PHP</sub>

## Gerenciadores de senha

* [AliasVault](https://www.aliasvault.net) - End-to-end encrypted password manager with a built-in email alias generator and server. `MIT` <sub>Docker</sub>
* [Bitwarden](https://bitwarden.com/) - Password manager with a webapp, browser extension, and mobile app. `AGPL-3.0` <sub>Docker/C#</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Passbolt](https://www.passbolt.com/) - Collaborative password manager. `AGPL-3.0` <sub>PHP/deb/K8S/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PassIt](https://passit.io/) - Simple password manage with sharing features by group and user, but no administration interface. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Psono](https://psono.com/) - Password manager for companies. `Apache-2.0` <sub>Python</sub>
* [Teampass](https://teampass.net/) - Password manager dedicated for managing passwords in a collaborative way. One symmetric key is used to encrypt all shared/team passwords and stored server side in a file and the database. works on any server Apache, MySQL and PHP. `GPL-3.0` <sub>PHP</sub>
* [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - Lightweight Bitwarden server API implementation written in Rust. `GPL-3.0` <sub>Rust/Docker</sub>

## Gestão de conhecimento

* [AFFiNE Community Edition](https://affine.pro/) - Next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, customizable and ready to use (alternative to Notion and Miro). `MIT/AGPL-3.0` <sub>Docker</sub>
* [Atomic Server](https://atomicserver.eu/) - Knowledge graph database with documents (similar to Notion), tables, search, and a powerful linked data API. Lightweight, very fast and no runtime dependencies. `MIT` <sub>Docker/Rust</sub>
* [Digimindmap](https://ladigitale.dev/digimindmap/#/) - Create simple mindmaps (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LibreKB](https://librekb.com/) - Web-based knowledge base solution. A simple web app, it runs on pretty much any web server or hosting provider with PHP and MySQL. `GPL-3.0` <sub>PHP</sub>
* [memEx](https://codeberg.org/shibao/memEx) - Structured personal knowledge base, inspired by zettlekasten and org-mode. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SiYuan](https://b3log.org/siyuan/) - A privacy-first personal knowledge management software, written in typescript and golang. `AGPL-3.0` <sub>Docker/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [TeamMapper](https://github.com/b310-digital/teammapper) - Host and create your own mindmaps. Share your mindmap sessions with your team and collaborate live on mindmaps. `MIT` <sub>Docker/Nodejs</sub>

## Gestão de documentos

* [BentoPDF](https://bentopdf.com) - Powerful, privacy-first, client-side PDF toolkit that allows you to manipulate, edit, merge, and process PDF files directly in your browser. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Docspell](https://docspell.org) - Auto-tagging document organizer and archive. `GPL-3.0` <sub>Scala/Java/Docker</sub>
* [Documenso](https://documenso.com) - Digital document signing platform (alternative to DocuSign). `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Docuseal](https://www.docuseal.co) - Create, fill, and sign digital documents (alternative to DocuSign). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [EveryDocs](https://github.com/jonashellmann/everydocs-core) - Simple Document Management System for private use with basic functionality to organize your documents digitally. `GPL-3.0` <sub>Docker/Ruby</sub>
* [Gotenberg](https://gotenberg.dev) - Developer-friendly API to interact with powerful tools like Chromium and LibreOffice for converting numerous document formats (HTML, Markdown, Word, Excel, etc.) into PDF files, and more. `MIT` <sub>Docker</sub>
* [I, Librarian](https://i-librarian.net) - Organize PDF papers and office documents. It provides a lot of extra features for students and research groups both in industry and academia. `GPL-3.0` <sub>PHP</sub>
* [Mayan EDMS](https://www.mayan-edms.com) - Electronic document management system for your documents with preview generation, OCR, and automatic categorization among other features. `GPL-2.0` <sub>Docker/K8S</sub>
* [OpenSign](https://www.opensignlabs.com) - Document signing software (alternative to DocuSign). `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Paperless-ngx](https://docs.paperless-ngx.com/) - Scan, index, and archive all of your paper documents with an improved interface (fork of Paperless). `GPL-3.0` <sub>Python/Docker</sub>
* [Papermerge](https://papermerge.com) - Document management system focused on scanned documents (electronic archives). Features file browsing in similar way to dropbox/google drive. OCR, full text search, text overlay/selection. `Apache-2.0` <sub>Docker/K8S</sub>
* [Papra](https://papra.app) - Minimalist document storage, management and archiving platform designed to be simple to use and accessible to everyone. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PdfDing](https://www.pdfding.com) - PDF manager, viewer and editor offering a seamless user experience on multiple devices. It's designed to be minimal, fast, and easy to set up using Docker. `AGPL-3.0` <sub>Docker/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SeedDMS](https://www.seeddms.org) - Document Management System with workflows, access rights, fulltext search, and more. `GPL-2.0` <sub>PHP</sub>
* [Signature PDF](https://github.com/24eme/signaturepdf) - Sign and manipulate PDFs with collaboration, organization, compression and metadata editing. `AGPL-3.0` <sub>PHP/deb/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SimpleDMS](https://simpledms.eu) - Easy-to-use, metadata-driven, open-source document management system (DMS) for small businesses that sorts documents almost by itself. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) - Local hosted web application that allows you to perform various operations on PDF files, such as merging, splitting, file conversions and OCR. `Apache-2.0` <sub>Docker/Java</sub>

## Gestão de eventos e conferências

* [indico](https://getindico.io/) - Feature-rich event management system, made @ CERN, the place where the Web was born. `MIT` <sub>Python</sub>
* [motion.tools (Antragsgrün)](https://motion.tools/) - Manage motions and amendments for (political) conventions. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpenSlides](https://openslides.com/) - Presentation and assembly system for managing and projecting agenda, motions and elections of an assembly. `MIT` <sub>Docker</sub>
* [osem](https://osem.io/) - Event management tailored to free Software conferences. `MIT` <sub>Ruby/Docker</sub>
* [pretalx](https://pretalx.org) - Web-based event management, including running a Call for Papers, reviewing submissions, and scheduling talks. Exports and imports for various related tools. `Apache-2.0` <sub>Python</sub>

## Gestão de mídia

* [ChannelTube](https://github.com/TheWicklowWolf/ChannelTube) - Download video or audio from YouTube channels on a schedule via yt-dlp. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Deleterr](https://github.com/rfsbraz/deleterr) - Automated media cleanup tool that removes watched and stale content from Plex, Sonarr, and Radarr based on configurable rules. `MIT` <sub>Docker</sub>
* [Downtify](https://downtify.henriquesebastiao.com) - Download Spotify music with album art and metadata. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Lidarr](https://lidarr.audio/) - Music collection manager for Usenet and BitTorrent users. `GPL-3.0` <sub>C#/Docker</sub>
* [LidaTube](https://github.com/TheWicklowWolf/LidaTube) - Finding and fetch missing Lidarr albums via yt-dlp. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Lidify](https://github.com/TheWicklowWolf/Lidify) - Music discovery tool that provides recommendations based on selected Lidarr artists, using Spotify or LastFM. `MIT` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Lingarr](https://lingarr.com) - Automatically translate subtitle files in your Radarr and Sonarr media libraries, using LibreTranslate, local AI models, or SaaS translation services. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Medusa](https://github.com/pymedusa/Medusa) - Automatic Video library manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic. `GPL-3.0` <sub>Python</sub>
* [MeTube](https://github.com/alexta69/metube) - Web GUI for youtube-dl, with playlist support. Allows downloading videos from dozens of websites. `AGPL-3.0` <sub>Python/Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MKVPriority](https://github.com/kennethsible/mkvpriority) - Selects preferred audio and subtitle tracks using configurable priority scores and sets the appropriate default and forced flags. `MIT` <sub>Python/Docker</sub>
* [MyTube](https://github.com/franklioxygen/MyTube) - Downloader and player for yt-dlp-supported sites with channel subscriptions, cloud upload support, and local library organization. `MIT` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [nefarious](https://lardbit.github.io/nefarious/) - Automate downloading Movies and TV Shows. `GPL-3.0` <sub>Python</sub>
* [Ombi](https://ombi.io/) - Content request system for Plex/Emby, connects to SickRage, CouchPotato, Sonarr, with a growing feature set. `GPL-2.0` <sub>C#/deb</sub>
* [Pinchflat](https://github.com/kieraneglin/pinchflat) - Download YouTube content built using yt-dlp. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PodFetch](https://samtv12345.github.io/PodFetch) - Sleek and efficient podcast downloader. `Apache-2.0` <sub>Docker/Rust</sub>
* [Radarr](https://radarr.video/) - Automatically download movies via Usenet and BitTorrent (fork of Sonarr). `GPL-3.0` <sub>C#/Docker</sub>
* [Ratelog](https://ratelog.org) - Movie tracker and rating app (alternative to Letterboxd). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Reaparr](https://www.reaparr.rocks/) - Cross-platform Plex media downloader that seamlessly adds media from other Plex servers to your own. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Seerr](https://github.com/seerr-team/seerr) - Manage requests for your media library, supports Plex, Jellyfin and Emby media servers (fork of Overseerr). `MIT` <sub>Docker/Nodejs</sub>
* [Sonarr](https://sonarr.tv/) - Automatic TV Shows downloader and manager for Usenet and BitTorrent. It can grab, sort and rename new episodes and automatically upgrade the quality of files already downloaded when a better quality format becomes available. `GPL-3.0` <sub>C#/Docker</sub>
* [TrackWatch](https://trackwatch.emlopezr.com) - Automated music release tracker for Spotify with email notifications, discography generator, and ghost track cleaner (alternative to Release Radar). `MIT` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [tubesync](https://github.com/meeb/tubesync) - Syncs YouTube channels and playlists to a locally hosted media server. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Watcharr](https://github.com/sbondCo/Watcharr) - Add and track all the shows and movies you are watching. Comes with user authentication, modern and clean UI and a very simple setup. `MIT` <sub>Docker</sub>
* [ydl_api_ng](https://github.com/Totonyus/ydl_api_ng) - Simple youtube-dl REST API to launch downloads on a distant server. `GPL-3.0` <sub>Python</sub>
* [Youtarr](https://github.com/DialmasterOrg/Youtarr) - Download videos from YouTube channels on a schedule via yt-dlp, with a web UI to browse and selectively download videos. Integrates with Plex Media Server and generates NFO metadata for Jellyfin, Kodi, and Emby. `ISC` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [youtube-dl-nas](https://hyeonsangjeon.github.io/youtube-dl-nas/) - Authenticated yt-dlp download queue for video, audio and subtitles, with history, mobile sharing and NAS file management (fork of youtube-dl-server). `MIT` <sub>Python/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [YoutubeDL-Server](https://github.com/nbr23/youtube-dl-server) - Web and REST interface to Youtube-DL for downloading videos onto a server. `MIT` <sub>Python/Docker</sub>
* [yt-dlp Web UI](https://github.com/marcopiovanello/yt-dlp-web-ui) - Web GUI for yt-dlp. `MPL-2.0` <sub>Docker/Go/Nodejs</sub>

## Gestão de pessoas (RH)

* [admidio](https://www.admidio.org/) - User management system for websites of organizations and groups. The system has a flexible role model so that it’s possible to reflect the structure and permissions of your organization. `GPL-2.0` <sub>PHP/Docker</sub>
* [Frappe HR](https://frappe.io/hr) - Complete HRMS solution with over 13 different modules right from employee management, onboarding, leaves, to payroll, taxation, and more. `GPL-3.0` <sub>Docker/Python/Nodejs</sub>
* [MintHCM](https://minthcm.org/) - Tool for Human Capital Management based on two popular, well-known business applications SugarCRM Community Edition and SuiteCRM. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Groupware

* [Citadel](https://www.citadel.org/) - Groupware including email, calendar/scheduling, address books, forums, mailing lists, IM, wiki and blog engines, RSS aggregation and more. `GPL-3.0` <sub>C/Docker/Shell</sub>
* [Colanode](https://colanode.com) - Collaboration suite with real-time messaging, rich text pages, file management, and dynamic databases - built for offline work (alternative to Slack, Notion). `Apache-2.0` <sub>K8S/Docker</sub>
* [Cozy Cloud](https://cozy.io/) - Personal cloud where you can manage and sync your files, notes, contacts, passwords, and documents. `GPL-3.0` <sub>Nodejs</sub>
* [Digipad](https://digipad.app/) - An online self-hosted application for creating collaborative digital notepads (Documentation in french). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digistorm](https://digistorm.app/) - Create collaborative surveys, quizzes, brainstorms, and word clouds (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digiwall](https://digiwall.app/) - Create multimedia collaborative walls for in-person or remote work (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [egroupware](https://www.egroupware.org/) - Software suite including calendars, address books, notepad, project management tools, client relationship management tools (CRM), knowledge management tools, a wiki and a CMS. `GPL-2.0` <sub>PHP</sub>
* [Group Office](https://www.group-office.com) - Enterprise CRM and groupware tool. Share projects, calendars, files and e-mail online with co-workers and clients. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Openmeetings](https://openmeetings.apache.org/index.html) - Video conferencing, instant messaging, whiteboard, collaborative document editing and other groupware tools using API functions of the Red5 Streaming Server for Remoting and Streaming. `Apache-2.0` <sub>Java</sub>
* [SOGo](https://www.sogo.nu/) - SOGo offers multiple ways to access the calendaring and messaging data. CalDAV, CardDAV, GroupDAV, as well as ActiveSync, including native Outlook compatibility and Web interface. `LGPL-2.1` <sub>Objective-C</sub>
* [Tine](https://www.tine-groupware.de/) - Software for digital collaboration in companies and organizations. From powerful groupware functionalities to clever add-ons, tine combines everything to make daily team collaboration easier. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Tracim](https://github.com/tracim/tracim) - Collaborative Platform for team collaboration: file,threads,notes,agenda,etc. `AGPL-3.0/LGPL-3.0/MIT` <sub>Python</sub>
* [Zimbra Collaboration](https://www.zimbra.com/) - Email, calendar, collaboration server with Web interface and lots of integrations. `GPL-2.0/CPAL-1.0` <sub>Java</sub>

## IA generativa

* [Agenta](https://agenta.ai/) - LLMOps platform for prompt management, LLM evaluation, and observability. Build, evaluate, and monitor production-grade LLM applications with collaborative prompt engineering. `MIT` <sub>Docker</sub>
* [AnythingLLM](https://anythingllm.com/) - All-in-one desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility, and more. `MIT` <sub>Nodejs/Docker</sub>
* [GoModel](https://gomodel.enterpilot.io/) - AI gateway written in Go with a unified OpenAI-compatible API for multiple LLM providers, USD cost tracking, budgets, usage analytics, guardrails, caching, and an admin dashboard. `MIT` <sub>Go/Docker</sub>
* [Khoj](https://khoj.dev/) - Your AI second brain. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LibreChat](https://www.librechat.ai) - Enhanced ChatGPT-compatible AI chat interface supporting multiple AI providers, with multi-user auth, message search, and plugin support. `MIT` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [LLM Harbor](https://github.com/av/harbor) - Containerized LLM toolkit. Run LLM backends, APIs, frontends, and additional services via a concise CLI. `Apache-2.0` <sub>Docker/Shell</sub>
* [LLMKube](https://llmkube.com) - Kubernetes operator for self-hosted LLM inference with pluggable runtimes (llama.cpp, vLLM, TGI, Ollama, vllm-swift), multi-GPU sharding, NVIDIA CUDA + Apple Silicon Metal support, and OpenAI-compatible API. `Apache-2.0` <sub>Go/Docker/K8S</sub>
* [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) - AI-powered deep research tool with multi-source search (arXiv, PubMed, web), PDF text extraction, and encrypted local storage. `MIT` <sub>Docker/Python</sub>
* [LocalAI](https://localai.io/) - Run your AI models locally and generate images and audio (alternative to OpenAI and Claude). `MIT` <sub>Docker/K8S</sub>
* [Ollama](https://ollama.com/) - Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 3, and other large language models. `MIT` <sub>Docker/Python</sub>
* [Onyx Community Edition](https://onyx.app) - Chat UI that works with any LLM. It comes loaded with advanced features like agents, web search, RAG, MCP, deep research, Connectors to 40+ knowledge sources, and more. `MIT` <sub>Docker/K8S</sub>
* [Open-WebUI](https://openwebui.com) - User-friendly AI Interface, supports Ollama, OpenAI API. `BSD-3-Clause` <sub>Docker/Python</sub>
* [Vane](https://github.com/ItzCrazyKns/Vane) - AI-powered search engine (alternative to Perplexity AI). `MIT` <sub>Docker</sub>

## Internet das coisas (IoT)

* [Domoticz](https://www.domoticz.com/) - Home Automation System that lets you monitor and configure various devices like: Lights, Switches, various sensors/meters like Temperature, Rain, Wind, UV, Electra, Gas, Water and much more. `GPL-3.0` <sub>C/C++/Docker/Shell</sub>
* [EMQX](https://www.emqx.com/) - Scalable MQTT broker. Connect 100M+ IoT devices in one single cluster, move and process real-time IoT data with 1M msg/s throughput at 1ms latency. `Apache-2.0` <sub>Docker/Erlang</sub>
* [evcc](https://evcc.io/) - Extensible Electric Vehicle Charge Controller and home energy management system. `MIT` <sub>deb/Docker/Go</sub>
* [FHEM](https://fhem.de/fhem.html) - Automate common tasks in the household like switching lamps and heating. It can also be used to log events like temperature or power consumption. You can control it via web or smartphone frontends, telnet or TCP/IP directly. `GPL-3.0` <sub>Perl</sub>
* [FlowForge](https://flowforge.com/) - Deploy Node-RED applications in a reliable, scalable and secure manner. The FlowForge platform provides DevOps capabilities for Node-RED development teams. `Apache-2.0` <sub>Nodejs/Docker/K8S</sub>
* [FMD Server](https://fmd-foss.org) - A server to communicate with the FMD (Find My Device) Android app, to locate and control your devices. `GPL-3.0` <sub>Docker/Go</sub>
* [Gladys](https://gladysassistant.com/) - Privacy-first home assistant. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [Home Assistant](https://home-assistant.io/) - Home automation platform. `Apache-2.0` <sub>Python/Docker</sub>
* [ioBroker](https://www.iobroker.net/) - Integration platform for the Internet of Things, focused on building automation, smart metering, ambient assisted living, process automation, visualization and data logging. `MIT` <sub>Nodejs</sub>
* [LHA](https://github.com/javalikescript/lha) - Light Home Automation application that is fully extensible using Blockly, HTML or Lua. It includes extensions such as ConBee, Philips Hue or Z-Wave JS. `MIT` <sub>Lua</sub>
* [Node RED](https://nodered.org/) - Browser-based flow editor that helps you wiring hardware devices, APIs and online services to create IoT solutions. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [Onloc](https://onloc.app) - Track and share your location in real time. Control and lock stolen or lost phones. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [openHAB](https://www.openhab.org) - Vendor and technology agnostic open source software for home automation. `EPL-2.0` <sub>Java</sub>
* [OpenRemote](https://openremote.io) - IoT Asset management, Flow Rules and WHEN-THEN rules, Data visualization, Edge Gateway. `AGPL-3.0` <sub>Java</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [polluSensWeb](https://wespeakenglish.github.io/polluSensWeb/) - Web-based serial interface and charting tool for visualizing and logging data from UART pollution sensors (PM2.5, VOC, etc). Features live data acquisition, dynamic charts, CSV export, and webhook integration. `MIT` <sub>Javascript</sub>
* [SIP Irrigation Control](https://dan-in-ca.github.io/SIP/) - Open source software for sprinkler/irrigation control. `GPL-3.0` <sub>Python</sub>
* [SOLECTRUS](https://solectrus.de) - Photovoltaic dashboard that displays energy production and consumption with cost and savings calculations. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Tasmota](https://tasmota.com) - Open source firmware for ESP devices. Total local control with quick setup and updates. Control using MQTT, Web UI, HTTP or serial. Automate using timers, rules or scripts. Integration with home automation solutions. `GPL-3.0` <sub>C/C++</sub>
* [Thingsboard](https://thingsboard.io/) - Open-source IoT Platform - Device management, data collection, processing and visualization. `Apache-2.0` <sub>Java/Docker/K8S</sub>
* [WebThings Gateway](https://webthings.io/gateway/) - WebThings is an open source implementation of the Web of Things, including the WebThings Gateway and the WebThings Framework. `MPL-2.0` <sub>Nodejs</sub>

## Jogos

* [0 A.D.](https://play0ad.com/) - Cross-platform real-time strategy game of ancient warfare. `MIT/GPL-2.0/Zlib` <sub>C++/C/deb</sub>
* [A Dark Room](https://github.com/doublespeakgames/adarkroom) - Minimalist text adventure game for your browser. `MPL-2.0` <sub>Javascript</sub>
* [DDraceNetwork](https://ddnet.org/) - Cooperative platformer version of DDRace, a Teeworlds modification featuring unique cooperative gameplay. `Zlib` <sub>C++</sub>
* [Digibuzzer](https://digibuzzer.app/) - Create a virtual game room around a connected buzzer (documentation in French). `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Hypersomnia](https://github.com/TeamHypersomnia/Hypersomnia) - Competitive top-down shooter blending Counter-Strike with Hotline Miami. Runs on Linux, Windows, MacOS and the Web. `AGPL-3.0` <sub>C++/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Lila](https://lichess.org/) - Ad-less chess server powering lichess.org, with official iOS and Android client apps. `AGPL-3.0` <sub>Scala</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Luanti](https://www.luanti.org/) - Voxel game engine (formerly Minetest). Play one of our many games, mod a game to your liking, make your own game, or play on a multiplayer server. `LGPL-2.1/MIT/Zlib` <sub>C++/Lua/deb</sub>
* [Mindustry](https://mindustrygame.github.io/) - Factorio-like tower defense game. Build production chains to gather more resources, and build complex facilities. `GPL-3.0` <sub>Java</sub>
* [MTA:SA](https://multitheftauto.com/) - Add network play functionality to Rockstar North's Grand Theft Auto game series, in which this functionality is not originally found. `GPL-3.0` <sub>C++</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [OpenTTD](https://www.openttd.org/) - Transport tycoon simulation game. `GPL-2.0` <sub>C++/Docker</sub>
* [piqueserver](https://github.com/piqueserver/piqueserver) - Server for openspades, the first-person shooter in a destructible voxel world. `GPL-3.0` <sub>Python/C++</sub>
* [Posio](https://github.com/abrenaut/posio) - Geography multiplayer game. `MIT` <sub>Python</sub>
* [Razzia](https://github.com/Ralex91/Razzia) - Quiz game platform, designed for smaller self-hosted events (alternative to Kahoot!). `MIT` <sub>Nodejs/Docker</sub>
* [Red Eclipse 2](https://www.redeclipse.net/) - Arena first-person shooter similar to Unreal Tournament. `Zlib/MIT/CC-BY-SA-4.0` <sub>C/C++/deb</sub>
* [Scribble.rs](https://github.com/scribble-rs/scribble.rs) - A web-based pictionary game. `BSD-3-Clause` <sub>Go/Docker</sub>
* [Suroi](https://suroi.io/) - An open-source 2D battle royale game inspired by surviv.io. `GPL-3.0` <sub>Nodejs</sub>
* [The Battle for Wesnoth](https://github.com/wesnoth/wesnoth) - The Battle for Wesnoth is an Open Source, turn-based tactical strategy game with a high fantasy theme, featuring both singleplayer and online/hotseat multiplayer combat. `GPL-2.0` <sub>C++/deb</sub>
* [Veloren](https://veloren.net/) - Multiplayer RPG. Open-source game inspired by Cube World, Legend of Zelda, Dwarf Fortress and Minecraft. `GPL-3.0` <sub>Rust</sub>
* [Zero-K](https://zero-k.info/) - Open Source on Springrts engine. Zero-K is a traditional real time strategy game with a focus on player creativity through terrain manipulation, physics, and a large roster of unique units - all while being balanced to support competitive play. `GPL-2.0` <sub>Lua</sub>

## Jogos — painéis e administração

* [auto-mcs](https://www.auto-mcs.com) - Cross-platform Minecraft server manager. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Calagopus](https://calagopus.com) - Modern game server management panel. Deploy, monitor, and manage Minecraft, Hytale, and other game servers with industry-leading performance. `MIT` <sub>Rust/Docker/deb</sub>
* [Crafty Controller](https://craftycontrol.com/) - Minecraft launcher and manager that allows users to start and administer Minecraft servers from a user-friendly interface. `GPL-3.0` <sub>Docker/Python</sub>
* [Drop](https://droposs.org) - Game distribution platform, designed for distributing and sharing DRM-free games efficiently (alternative to Steam, GameVault). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [EasyWI](https://easy-wi.com) - Easy-Wi is a Web-interface that allows you to manage server daemons like gameservers. In addition it provides you with a CMS which includes a fully automated game- and voiceserver lending service. `GPL-3.0` <sub>PHP/Shell</sub>
* [GameAP](https://gameap.com/) - Game Administration Panel for managing game servers on Linux and Windows. `MIT` <sub>Go/Docker</sub>
* [Gameyfin](https://gameyfin.org) - Video game library manager with automatic scanning, web access, downloads, and plugin support. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Gaseous Server](https://github.com/gaseous-project/gaseous-server) - Game ROM manager with a built-in web-based emulator using multiple sources to identify and provide metadata. `AGPL-3.0` <sub>Docker/.NET</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Lancache](https://lancache.net) - LAN Party game caching made easy. `MIT` <sub>Docker/Shell</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [LinuxGSM](https://linuxgsm.com/) - CLI tool for deployment and management of dedicated game servers on Linux: more than 120 games are supported. `MIT` <sub>Shell</sub>
* [Minus Games](https://accessory.github.io/minus_games_user_guide) - Sync games and save files across multiple devices. `MIT` <sub>Rust</sub>
* [Ownfoil](https://github.com/a1ex4/ownfoil) - Nintendo Switch library manager, with automated management tasks (file identification and organization, missing updates/DLC), serving your library to multiple supported clients on your Switch, with shop customization and multi user authentication. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Pelican Panel](https://pelican.dev/) - Web application for easy management of game servers, offering a user-friendly interface for deploying, configuring, and managing servers, server monitoring tools, and extensive customization options (fork of Pterodactyl). `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Pterodactyl](https://pterodactyl.io/) - Management panel for game servers, with an intuitive UI for end users. `MIT` <sub>PHP</sub>
* [PufferPanel](https://www.pufferpanel.com/) - Game server management panel designed for both small networks and game server providers. `Apache-2.0` <sub>Go</sub>
* [Retrom](https://github.com/JMBeresford/retrom) - Private cloud game library distribution server + frontend/launcher. `GPL-3.0` <sub>Docker/Rust</sub>
* [RomM](https://romm.app/) - ROM manager for organizing, enriching, and playing retro games, with support for 400+ platforms. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SourceBans++](https://sbpp.github.io/) - Admin, ban, and communication management system for games running on the Source engine. `CC-BY-SA-4.0` <sub>PHP</sub>
* [Sunshine](https://app.lizardbyte.dev/Sunshine/) - Remote game stream host for Moonlight with support up to 120 frames per second and 4K resolution. `GPL-3.0` <sub>C++/deb/Docker</sub>

## Leitores de feed

* [Bubo Reader](https://github.com/georgemandis/bubo-rss) - Irrationally minimal RSS feed reader. `MIT` <sub>Nodejs</sub>
* [CommaFeed](https://www.commafeed.com/) - Google Reader inspired self-hosted RSS reader. `Apache-2.0` <sub>Java/Docker</sub>
* [Feeds Fun](https://feeds.fun/) - News reader with tags, scoring, and AI. `BSD-3-Clause` <sub>Python</sub>
* [FreshRSS](https://freshrss.org/) - Self-hostable RSS feed aggregator. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Fusion](https://github.com/0x2E/fusion) - Lightweight RSS aggregator and reader. `MIT` <sub>Go/Docker</sub>
* [Goeland](https://github.com/slurdge/goeland) - Turns any RSS/Atom feed into a beautiful email digest. `MIT` <sub>Go/Docker</sub>
* [JARR](https://1pxsolidblack.pl/jarr-en.html) - JARR (Just Another RSS Reader) is a web-based news aggregator and reader (fork of Newspipe). `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kriss Feed](https://github.com/tontof/kriss_feed) - Simple and smart (or stupid) feed reader. `CC0-1.0` <sub>PHP</sub>
* [Leed](https://github.com/LeedRSS/Leed) - Leed (for Light Feed) is a Free and minimalist RSS aggregator. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Miniflux](https://miniflux.app/) - Minimalist news reader. `Apache-2.0` <sub>Go/deb/Docker</sub>
* [NewsBlur](https://www.newsblur.com/) - Personal news reader that brings people together to talk about the world. A new sound of an old instrument. `MIT` <sub>Python</sub>
* [Newspipe](https://git.sr.ht/~cedric/newspipe) - Web news reader. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [reader](https://github.com/lemon24/reader) - Feed reader web app and library (so you can use it to build your own), with only standard library and pure-Python dependencies. `BSD-3-Clause` <sub>Python</sub>
* [Readflow](https://readflow.app) - Lightweight news reader with modern interface and features: full-text search, automatic categorization, archiving, offline support, notifications. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [RSS Monster](https://github.com/pietheinstrengholt/rssmonster) - Easy to use web-based RSS aggregator and reader compatible with the Fever API (alternative to Google Reader). `MIT` <sub>PHP</sub>
* [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge) - Generate RSS/ATOM feeds for websites which don't have one. `Unlicense` <sub>PHP/Docker</sub>
* [RSS2EMail](https://github.com/rss2email/rss2email) - Fetches RSS/Atom-feeds and pushes new content to any email-receiver, supports OPML. `GPL-2.0` <sub>Python/deb</sub>
* [RSSHub](https://docs.rsshub.app) - Easy to use, and extensible RSS feed aggregator capable of generating RSS feeds from pretty much everything ranging from social media to university departments. `MIT` <sub>Nodejs/Docker</sub>
* [Selfoss](https://selfoss.aditu.de/) - New multipurpose rss reader, live stream, mashup, aggregation web application. `GPL-3.0` <sub>PHP</sub>
* [Stringer](https://github.com/stringer-rss/stringer) - Work-in-progress self-hosted, anti-social RSS reader. `MIT` <sub>Ruby</sub>
* [Tiny Tiny RSS](https://tt-rss.org) - Web-based news feed (RSS/Atom) reader and aggregator. `GPL-3.0` <sub>Docker/PHP</sub>
* [TinyFeed](https://feed.lovergne.dev/) - Generate a static HTML page from a collection of feeds with a simple CLI. `MIT` <sub>Go/Docker</sub>
* [Upvote RSS](https://www.upvote-rss.com/) - Generate rich RSS feeds from Reddit, Hacker News, Lemmy, Mbin, and more. `MIT` <sub>Docker/PHP</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Yarr](https://github.com/nkanaev/yarr) - Yarr (yet another rss reader) is a web-based feed aggregator which can be used both as a desktop application and a personal self-hosted server. `MIT` <sub>Go</sub>

## Manufatura

* [CNCjs](https://cnc.js.org/) - Web interface for CNC milling controllers running Grbl, Smoothieware, or TinyG. `MIT` <sub>Nodejs</sub>
* [Fluidd](https://docs.fluidd.xyz/) - Lightweight & responsive user interface for Klipper, the 3D printer firmware. `GPL-3.0` <sub>Docker/Nodejs</sub>
* [LinuxCNC](https://www.linuxcnc.org/) - Linux based CNC machine controller. It can drive milling machines, lathes, 3D printers, laser cutters, plasma cutters, robot arms, hexapods, and more. `GPL-2.0/LGPL-3.0` <sub>C/deb</sub>
* [Mainsail](https://docs.mainsail.xyz/) - Modern and responsive user interface for the Klipper 3D printer firmware. Control and monitor your printer from everywhere, from any device. `GPL-3.0` <sub>Docker/Python</sub>
* [Manyfold](https://manyfold.app) - Digital asset manager for 3d print files; STL, OBJ, 3MF and more. `MIT` <sub>Docker</sub>
* [Octoprint](https://octoprint.org/) - Snappy web interface for controlling consumer 3D printers. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Mapas e GPS

* [AdventureLog](https://adventurelog.app) - Travel tracker and trip planner. `GPL-3.0` <sub>Docker</sub>
* [AirTrail](https://airtrail.johan.ohly.dk) - Personal flight tracking system. `GPL-3.0` <sub>Docker/Nodejs</sub>
* [Bicimon](https://github.com/knrdl/bicimon) - Bike Speedometer as Progressive Web App. `MIT` <sub>Javascript</sub>
* [Dawarich](https://dawarich.app/) - Visualize your location history, track your movements, and analyze your travel patterns with complete privacy and control (alternative to Google Timeline a.k.a. Google Location History). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Geo2tz](https://github.com/noandrea/geo2tz) - Get the timezone from geo coordinates (lat, lon). `MIT` <sub>Go/Docker</sub>
* [GraphHopper](https://graphhopper.com/) - Fast routing library and server using OpenStreetMap. `Apache-2.0` <sub>Java</sub>
* [NextGIS Web](https://nextgis.com/nextgis-web/) - Web GIS server for geospatial data management, web map publishing, and QGIS-centered collaborative workflows. `GPL-3.0` <sub>Docker</sub>
* [Nominatim](https://nominatim.org/) - Server application for geocoding (address -> coordinates) and reverse geocoding (coordinates -> address) on OpenStreetMap data. `GPL-2.0` <sub>C</sub>
* [Open Source Routing Machine (OSRM)](http://project-osrm.org/) - High performance routing engine designed to run on OpenStreetMap data and offering an HTTP API, C++ library interface, and Nodejs wrapper. `BSD-2-Clause` <sub>C++</sub>
* [OpenRouteService](https://openrouteservice.org/) - Route service with directions, isochrones, time-distance matrix, route optimization, etc. `GPL-3.0` <sub>Docker/Java</sub>
* [OpenStreetMap](https://www.openstreetmap.org/) - Collaborative project to create a free editable map of the world. `GPL-2.0` <sub>Ruby</sub>
* [OpenTripPlanner](https://www.opentripplanner.org/) - Multimodal trip planning software based on OpenStreetMap data and consuming published GTFS-formatted data to suggest routes using local public transit systems. `LGPL-3.0` <sub>Java/Javascript</sub>
* [OwnTracks Recorder](https://github.com/owntracks/recorder) - Store and access data published by [OwnTracks](https://owntracks.org/) location tracking apps. `GPL-2.0` <sub>C/Lua/deb/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [TileServer GL](https://tileserver.readthedocs.io/) - Vector and raster maps with GL styles. Server side rendering by Mapbox GL Native. Map tile server for Mapbox GL JS, Android, iOS, Leaflet, OpenLayers, GIS via WMTS, etc. `BSD-2-Clause` <sub>Nodejs/Docker</sub>
* [Traccar](https://www.traccar.org/) - Java application to track GPS positions. Supports loads of tracking devices and protocols, has an Android and iOS App. Has a web interface to view your trips. `Apache-2.0` <sub>Java</sub>
* [TRIP](https://itskovacs-trip.netlify.app/) - Minimalist POI Map tracker and Trip planner. `MIT` <sub>Docker</sub>
* [wanderer](https://github.com/open-wanderer/wanderer) - Trail database where you can upload your recorded tracks or create new ones and add various metadata to build an easily searchable catalogue. `AGPL-3.0` <sub>Docker/Go/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Notas e editores

* [Blinko](https://blinko.space/) - A personal note tool with AI features. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [DailyTxT](https://github.com/PhiTux/DailyTxT) - Encrypted diary Web application to save your personal memories of each day. Includes a search function and encrypted file upload. `MIT` <sub>Docker</sub>
* [Docs](https://docs.numerique.gouv.fr/) - Collaborative note taking, wiki and documentation platform that scales. `MIT` <sub>K8S</sub>
* [draw.io](https://draw.io) - Diagram software for making flowcharts, process diagrams, org charts, UML, ER and network diagrams. `Apache-2.0` <sub>Javascript/Docker</sub>
* [flatnotes](https://github.com/dullage/flatnotes) - Database-less note-taking web app that utilises a flat folder of markdown files for storage. `MIT` <sub>Docker</sub>
* [HedgeDoc](https://hedgedoc.org/) - Realtime collaborative markdown notes on all platforms, formerly known as CodiMD and HackMD CE. `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Joplin](https://joplinapp.org/) - Note taking application with markdown editor and encryption support for mobile and desktop platforms. Runs client-side and syncs through a self hosted Nextcloud instance or similar (alternative to Evernote). `MIT` <sub>Nodejs</sub>
* [Jotty](https://jotty.page) - Lightweight but powerful alternative for managing your personal, file based, notes and checklists. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Livebook](https://livebook.dev) - Realtime collaborative notebook app based on Markdown that supports running Elixir code snippets, TeX and Mermaid Diagrams. Easily deployed using Docker or Elixir. `Apache-2.0` <sub>Elixir/Docker</sub>
* [Many Notes](https://github.com/brufdev/many-notes) - Markdown note-taking web application designed for simplicity. `MIT` <sub>Docker</sub>
* [Memos](https://usememos.com/) - Knowledge base that works with a SQLite db file. `MIT` <sub>Docker/Go</sub>
* [Note Mark](https://notemark.docs.enchantedcode.co.uk/) - Minimal web-based Markdown notes app. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Overleaf](https://www.overleaf.com/) - Web-based collaborative LaTeX editor. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Plainpad](https://alextselegidis.com/get/plainpad/) - Modern note taking application for the cloud, utilizing the best features of progressive web apps technology. `GPL-3.0` <sub>PHP</sub>
* [plumio](https://plumio.app/) - Markdown notes taking app with live preview, document encryption, multi-user support, multi-organization capabilities and more. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SilverBullet](https://silverbullet.md/) - Note-taking application optimized for people with a hacker mindset. `MIT` <sub>Docker/Deno</sub>
* [Standard Notes](https://docs.standardnotes.com/self-hosting/getting-started) - Simple and private notes app. Protect your privacy while getting more done. That's Standard Notes. `GPL-3.0` <sub>Ruby</sub>
* [TriliumNext Notes](https://github.com/TriliumNext/Trilium) - Cross-platform hierarchical note taking application with focus on building large personal knowledge bases (fork of Trilium Notes). `AGPL-3.0` <sub>Nodejs/Docker/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Turtl](https://turtl.it/) - Totally private personal database and note taking app. `GPL-3.0` <sub>CommonLisp</sub>
* [Writing](https://josephernest.github.io/writing/) - Lightweight distraction-free text editor, in the browser (Markdown and LaTeX supported). No lag when writing. `MIT` <sub>Javascript</sub>

## Painéis pessoais

* [Dashy](https://dashy.to/) - Feature-rich homepage for your homelab, with easy YAML configuration. `MIT` <sub>Nodejs/Docker</sub>
* [Glance](https://github.com/glanceapp/glance) - Highly customizable dashboard that puts all your feeds in one place. `AGPL-3.0` <sub>Docker/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [gobookmarks](https://github.com/arran4/gobookmarks) - Landing page to display bookmarks stored in GitHub, GitLab or local Git. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Heimdall](https://heimdall.site/) - Elegant solution to organise all your web applications. `MIT` <sub>PHP</sub>
* [Homarr](https://homarr.dev) - Sleek, modern dashboard with many integrations and web-based config. `MIT` <sub>Docker/Nodejs</sub>
* [Homepage by gethomepage](https://github.com/gethomepage/homepage) - Highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations. `GPL-3.0` <sub>Docker/Nodejs</sub>
* [Homepage by tomershvueli](https://github.com/tomershvueli/homepage) - Simple, standalone, self-hosted PHP page that is your window to your server and the web. `MIT` <sub>PHP</sub>
* [Homer](https://github.com/bastienwirtz/homer) - Dead simple static homepage to expose your server services, with an easy yaml configuration and connectivity check. `Apache-2.0` <sub>Docker/K8S/Nodejs</sub>
* [Hubleys](https://github.com/knrdl/hubleys-dashboard) - Personal dashboards to organize links for multiple users via a central yaml config. `MIT` <sub>Docker</sub>
* [LinkStack](https://linkstack.org/) - Link all your social media platforms easily accessible on one page, customizable through an intuitive, easy to use user/admin interface (alternative to Linktree and Manylink). `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LittleLink](https://littlelink.io/) - Simplistic approach for links in bio with 100+ branded buttons (alternative to Linktree). `MIT` <sub>Javascript</sub>
* [Mafl](https://mafl.hywax.space/) - Minimalistic flexible homepage. `MIT` <sub>Docker/Nodejs</sub>
* [Nimbus](https://nimbus.turboot.com/) - Modern drag-and-drop homelab dashboard with visual editor and simple configuration. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Personal Management System](https://volmarg.github.io/) - Organize the essentials of everyday life, everything from a simple to-do list, and notes up to payments, and schedules. `MIT` <sub>Docker</sub>
* [portkey](https://portkey.page) - Simple web portal that serves as a startup page, displaying a compilation of links and URLs, while also allowing the addition of custom pages, all managed through a single configuration file. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [ryot](https://github.com/ignisda/ryot) - Track various facets of your life - media, fitness, etc. `GPL-3.0` <sub>Docker</sub>
* [Starbase 80](https://github.com/notclickable-jordan/starbase-80) - A simple homepage with an iPad-style application grid, for mobile and desktop. One JSON configuration file. `MIT` <sub>Docker</sub>
* [Your Spotify](https://github.com/Yooooomi/your_spotify) - Allows you to record your Spotify listening activity and have statistics about them served through a Web application. `MIT` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>

## Pastebins

* [1time](https://1time.io) - Zero-knowledge one-time secret sharing. Create a one-time link for a password, API key, or file. Encrypted client-side in the browser, never reaches the server in plaintext, self-destructs after the allowed number of views (one by default). `MIT` <sub>Docker</sub>
* [BinPastes](https://github.com/querwurzel/BinPastes) - Minimal pastebin supporting client-side encryption, fulltext search, one-time messages. Intended for one to few users looking for a simple pastebin deployment. `Apache-2.0` <sub>Java</sub>
* [ByteStash](https://github.com/jordan-dalby/ByteStash) - Pastebin and file storage service with a simple web interface. Supports syntax highlighting, optional user authentication and public sharing. `GPL-3.0` <sub>Docker</sub>
* [Chiyogami](https://github.com/rhee876527/chiyogami) - Pastebin with API, client-side encryption, user accounts, syntax highlighting, markdown rendering, and more. `BSD-3-Clause` <sub>Docker</sub>
* [dpaste](https://dpaste.org/) - Simple pastebin with multiple text and code option, with short url result easy to remember. `MIT` <sub>Docker/Python</sub>
* [Hemmelig](https://hemmelig.app) - Share encrypted secrets cross organizations, or as private persons. `MIT` <sub>Docker/Nodejs</sub>
* [lesma](https://lesma.eu) - Simple paste app friendly with browser and command line. `GPL-3.0` <sub>Rust/Docker</sub>
* [Local Content Share](https://github.com/Tanq16/local-content-share) - Store and share text snippets and files within your local network. `MIT` <sub>Docker/Go</sub>
* [not-th.re](https://not-th.re) - Simple paste sharing platform, with client side encryption, featuring the monaco browser-based code editor. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Opengist](https://opengist.io) - Pastebin powered by Git. `AGPL-3.0` <sub>Docker/Go/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [paaster](https://paaster.io) - End-to-end encrypted pastebin built with the objective of simplicity. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [pacebin](https://git.crueter.xyz/crueter/pacebin) - Super-minimal pastebin and file upload service focusing on small executable size, portability, and ease of configuration. `AGPL-3.0` <sub>C</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Password Pusher](https://pwpush.com) - Dead-simple application to securely communicate passwords (or text) over the web. Passwords automatically expire after a certain number of views and/or time has passed. `Apache-2.0` <sub>Docker/K8S/Ruby</sub>
* [Pastefy](https://pastefy.app/) - Beautiful, simple and easy to deploy Pastebin with optional client encryption, multitab pastes, an API, a highlighted editor and more. `MIT` <sub>Docker/K8S/Java</sub>
* [PrivateBin](https://privatebin.info/) - Minimalist pastebin/discussion board where the server has zero knowledge of hosted data. `Zlib` <sub>PHP</sub>
* [rustypaste](https://github.com/orhun/rustypaste) - Minimal file upload/pastebin service. `MIT` <sub>Rust</sub>
* [Snipo](https://github.com/MohamedElashri/snipo) - Lightweight, self‑hosted snippet manager for saving and organizing code and text snippets with folders, tags, API, and GitHub Gist sync. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SnyPy](https://snypy.com) - Open source on-prem code snippet manager. `MIT` <sub>Docker</sub>
* [Sup3rS3cretMes5age](https://github.com/algolia/sup3rS3cretMes5age) - Very simple (to deploy and to use) secret message service using Hashicorp Vault as a secrets storage. `MIT` <sub>Go</sub>
* [Wastebin](https://github.com/matze/wastebin) - Lightweight, minimal and fast pastebin with an SQLite backend. `MIT` <sub>Rust/Docker</sub>
* [Yopass](https://github.com/jhaals/yopass) - Secure sharing of secrets, passwords and files. `Apache-2.0` <sub>Go/Docker</sub>

## Planejamento de recursos (ERP)

* [Dolibarr](https://www.dolibarr.org/) - Modern CRM software package to manage your company or foundation activity (contacts, suppliers, invoices, orders, stocks, agenda, accounting, ...). `GPL-3.0` <sub>PHP/deb</sub>
* [ERPNext](https://frappe.io/erpnext) - ERP system to help you run your business. `GPL-3.0` <sub>Python/Docker</sub>
* [farmOS](https://farmos.org/) - Web-based farm record keeping application. `GPL-2.0` <sub>PHP/Docker</sub>
* [grocy](https://grocy.info/) - ERP beyond your fridge. Groceries & household management solution for your home. `MIT` <sub>PHP/Docker</sub>
* [LedgerSMB](https://ledgersmb.org/) - Integrated accounting and ERP system for small and midsize businesses, with double entry accounting, budgeting, invoicing, quotations, projects, orders and inventory management, shipping and more. `GPL-2.0` <sub>Docker/Perl</sub>
* [Odoo](https://www.odoo.com) - Free open source ERP system. `LGPL-3.0` <sub>Python/deb/Docker</sub>
* [OFBiz](https://ofbiz.apache.org/) - Enterprise Resource Planning system with a suite of business applications flexible enough to be used across any industry. `Apache-2.0` <sub>Java</sub>
* [Tryton](https://www.tryton.org/) - Free open source business solution. `GPL-3.0` <sub>Python</sub>

## Plataformas de auto-hospedagem

* [DietPi](https://dietpi.com/) - Minimal Debian OS optimized for single-board computers, which allows you to easily install and manage several services for selfhosting at home. `GPL-2.0` <sub>Shell</sub>
* [DockSTARTer](https://dockstarter.com/) - DockSTARTer helps you get started with home server apps running in Docker. `MIT` <sub>Shell</sub>
* [Dropserver](https://dropserver.org) - An application platform for your personal web services. `Apache-2.0` <sub>Go/Deno</sub>
* [FreedomBox](https://freedombox.org/) - Community project to develop, design and promote personal servers running free software for private, personal, communications. `AGPL-3.0` <sub>Python/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [HomeButler](https://homebutler.dev) - Installs and manages a curated catalog of applications via Docker Compose, maps containers and exposed ports, verifies backups restore, and reports what changed since the last run with CLI, JSON, web and MCP interfaces. `MIT` <sub>Docker/Go</sub>
* [HomelabOS](https://homelabos.com) - Offline privacy-centric data-center. Deploy over 100 services with a few commands. `MIT` <sub>Docker</sub>
* [HomeServerHQ](https://www.homeserverhq.com/) - All-in-one home server infrastructure and installer. Have a fully configured email server, VPN, and public website(s) set up in less than an hour, even behind CGNAT. `GPL-3.0` <sub>Shell</sub>
* [LibreServer](https://libreserver.org/) - Home server configuration based on Debian. `AGPL-3.0` <sub>Shell</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [NextCloudPi](https://github.com/nextcloud/nextcloudpi) - Nextcloud preinstalled and preconfigured, with a text and web management interface and all the tools needed to self host private data. With installation images for Raspberry Pi, Odroid, Rock64, Docker, and a curl installer for Armbian/Debian. `GPL-2.0` <sub>Shell/PHP</sub>
* [Nirvati](https://nirvati.org) - Easily 1-click spin up popular self-hosted apps from a convenient web interface. `AGPL-3.0` <sub>Rust/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpenMediaVault](https://www.openmediavault.org/) - Network attached storage (NAS) solution based on Debian Linux. It contains services like SSH, (S)FTP, SMB/CIFS, DAAP media server, RSync, BitTorrent client and many more. `GPL-3.0` <sub>PHP</sub>
* [Sandstorm](https://sandstorm.io/) - Personal server for running self-hosted apps easily and securely. `Apache-2.0` <sub>C++/Shell</sub>
* [Self Host Blocks](https://github.com/ibizaman/selfhostblocks) - Modular server management based on NixOS modules and focused on best practices. `AGPL-3.0` <sub>Nix</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [StartOS](https://start9.com) - Browser-based, graphical Operating System (OS) that makes running a personal server as easy as running a personal computer. `MIT` <sub>Rust</sub>
* [Syncloud](https://syncloud.org/) - Your own online file storage, social network or email server. `GPL-3.0` <sub>Go/Shell</sub>
* [Tipi](https://runtipi.io/) - Homeserver manager. One command setup, one click installs for your favorites self-hosted apps. `GPL-3.0` <sub>Shell</sub>
* [UBOS](https://ubos.net/) - Linux distro that runs on indie boxes (personal servers and IoT devices). Single-command installation and management of apps - Jenkins, Mediawiki, Owncloud, WordPress, etc., and other features. `GPL-3.0` <sub>Perl</sub>
* [Websoft9](https://www.websoft9.com) - GitOps-driven, multi-application hosting for cloud servers and home servers, one-click deployment of 200+ open source apps. `LGPL-3.0` <sub>Shell/Python</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [WikiSuite](https://wikisuite.org) - The most comprehensive and integrated Free / Libre / Open Source enterprise software suite. `GPL-3.0/LGPL-2.1/Apache-2.0/MPL-2.0/MPL-1.1/MIT/AGPL-3.0` <sub>Shell/Perl/deb</sub>
* [xsrv](https://xsrv.readthedocs.io/) - Install and manage self-hosted services/applications, on your own server(s). `GPL-3.0` <sub>Ansible/Shell</sub>
* [YunoHost](https://yunohost.org/) - Server operating system aiming to make self-hosting accessible to everyone. `AGPL-3.0` <sub>Python/Shell</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Plataformas de blog

* [Antville](https://antville.org) - Free, open source project aimed at the development of a high performance, feature rich weblog hosting software. `Apache-2.0` <sub>Javascript</sub>
* [Castopod](https://castopod.org) - Podcast management hosting platform that includes the latest podcast 2.0 standards, an automated Fediverse feed, analytics, an embeddable player, and more. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Chyrp Lite](https://chyrplite.net) - Extra-awesome, extra-lightweight blog engine. `BSD-3-Clause` <sub>PHP</sub>
* [Dotclear](https://git.dotclear.org/dev/dotclear) - Take control over your blog. `GPL-2.0` <sub>PHP</sub>
* [Ech0](https://ech0.app/) - Lightweight federated publishing platform focused on personal idea sharing (documentation in Chinese). `AGPL-3.0` <sub>Docker/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [FlatPress](https://flatpress.org/) - A lightweight, easy-to-set-up flat-file blogging engine. `GPL-2.0` <sub>PHP</sub>
* [fx](https://github.com/rikhuijzer/fx) - Micro-blog tool offering built-in syntax highlighting, mobile publishing and more (alternative to Twitter, Bluesky). `MIT` <sub>Docker</sub>
* [Ghost](https://ghost.org/) - Just a blogging platform. `MIT` <sub>Nodejs</sub>
* [Haven](https://havenweb.org/) - Private blogging system with markdown editing and built in RSS reader. `MIT` <sub>Ruby</sub>
* [HTMLy](https://www.htmly.com/) - Databaseless PHP blogging platform. A flat-file CMS that allows you to create a fast, secure, and powerful website or blog in seconds. `GPL-2.0` <sub>PHP</sub>
* [Known](https://withknown.com/) - Collaborative social publishing platform. `Apache-2.0` <sub>PHP</sub>
* [Mataroa](https://mataroa.blog/) - Naked blogging platform for minimalists. `MIT` <sub>Python</sub>
* [PluXml](https://pluxml.org) - XML-based blog/CMS platform. `GPL-3.0` <sub>PHP</sub>
* [Serendipity](https://docs.s9y.org/) - Serendipity (s9y) is a highly extensible and customizable PHP blog engine using Smarty templating. `BSD-3-Clause` <sub>PHP</sub>
* [WriteFreely](https://writefreely.org) - Writing software for starting a minimalist, federated blog — or an entire community. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Proxy

* [g3proxy](https://g3-project.readthedocs.io/projects/g3proxy/en/latest/) - Forward proxy server supporting proxy chaining, protocol inspection, MITM Interception, ICAP adaptation and transparent proxy. `Apache-2.0` <sub>Rust/deb</sub>
* [GitProxy](https://git-proxy.finos.org/) - Proxy for Git that applies rules and workflows to all outgoing git push operations and ensures they are compliant. It supports both HTTP/HTTPS and SSH protocols with security scanning and validation. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [imgproxy](https://imgproxy.net/) - Fast and secure standalone server for resizing and converting remote images. `MIT` <sub>Go/Docker/K8S</sub>
* [iodine](https://code.kryo.se/iodine/) - IPv4 over DNS tunnel solution, enabling you to start up a socks5 proxy listener. `ISC` <sub>C/deb</sub>
* [Outline Server](https://getoutline.org/) - A proxy server that runs a Shadowsocks instance for each access key and a REST API to manage the access keys. `Apache-2.0` <sub>Docker/Nodejs</sub>
* [Privoxy](https://www.privoxy.org) - Non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk. `GPL-2.0` <sub>C/deb</sub>
* [sish](https://github.com/antoniomika/sish) - HTTP(S)/WS(S)/TCP tunnels to localhost using only SSH (serveo/ngrok alternative). `MIT` <sub>Go/Docker</sub>
* [socks5-proxy-server](https://github.com/nskondratev/socks5-proxy-server) - SOCKS5 proxy server with built-in authentication and Telegram-bot for user management and user statistics on data spent (handy when you pay per GB of data). It is dockerised and simple to install. `Apache-2.0` <sub>Docker</sub>
* [Squid](http://www.squid-cache.org/) - Caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. `GPL-2.0` <sub>C/deb</sub>
* [Tinyproxy](https://tinyproxy.github.io/) - Light-weight HTTP/HTTPS proxy daemon. `GPL-2.0` <sub>C/deb</sub>

## Receitas culinárias

* [Bar Assistant](https://barassistant.app/) - Manage your home bar while adding your ingredients, searching for cocktails and creating custom cocktail recipes. `MIT` <sub>PHP/Docker</sub>
* [CookCLI](https://cooklang.org) - Command-line tool for automating meal planning and shopping with Cooklang recipes, scriptable for UNIX workflows, includes web server. `MIT` <sub>Rust</sub>
* [Fork Recipes](https://mikebgrep.github.io/forkapi/latest/clients/) - Manage your food recipes with simplicity. `BSD-3-Clause` <sub>Docker</sub>
* [ManageMeals](https://managemeals.com/) - Manage recipes, import recipes by URL and organize them without any ads or unnecessary text. `GPL-3.0` <sub>Docker</sub>
* [Mealie](https://nightly.mealie.io/) - Material design inspired recipe manager with category and tag management, shopping-lists, meal-planner, and site customizations. Mealie is focused on simple user interactions to keep the whole family using the app. `MIT` <sub>Python</sub>
* [RecipeSage](https://github.com/julianpoy/recipesage) - A recipe keeper, meal plan organizer, and shopping list manager that can import recipes directly from any URL. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Recipya](https://recipes.musicavis.ca) - Clean, simple and powerful recipe manager your whole family will enjoy. `GPL-3.0` <sub>Docker/Go</sub>
* [Tamari](https://tamariapp.com) - Recipe manager web app with a built-in collection of recipes. Organize by favorites and categories, create shopping lists, and plan meals. `GPL-3.0` <sub>Docker/Python</sub>
* [Vanilla Cookbook](https://vanilla-cookbook.readthedocs.io/en/) - Recipe manager designed with complexity under the hood, keeping the user experience as uncluttered, simply vanilla as possible. `GPL-3.0` <sub>Docker/Nodejs</sub>
* [What To Cook?](https://github.com/kassner/whattocook) - Get a recipe to cook today, based on the ingredients you have at home. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Redes sociais e fóruns

* [Akkoma](https://akkoma.social/) - Federated microblogging server with Mastodon, GNU social, and ActivityPub compatibility. `AGPL-3.0` <sub>Elixir/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Answer](https://answer.apache.org) - Knowledge-based community software. You can use it to quickly build your Q&A community for product technical support, customer support, user communication, and more. `Apache-2.0` <sub>Docker/Go</sub>
* [Artalk](https://artalk.js.org/) - Comment system built in Golang, providing a lightweight and highly customizable solution for adding comments to your website. `MIT` <sub>Go/Docker</sub>
* [AsmBB](https://board.asm32.info) - Fast, SQLite-powered forum engine written in ASM. `EUPL-1.2` <sub>Assembly</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>
* [BuddyPress](https://buddypress.org/about/) - Powerful plugin that takes your WordPress.org powered site beyond the blog with social-network features like user profiles, activity streams, user groups, and more. `GPL-2.0` <sub>PHP</sub>
* [Coral](https://coralproject.net/) - A better commenting experience from Vox Media. `Apache-2.0` <sub>Docker/Nodejs</sub>
* [diaspora*](https://diasporafoundation.org/) - Distributed social networking server. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Discourse](https://www.discourse.org/) - Advanced forum / community solution based on Ruby and JS. `GPL-2.0` <sub>Docker</sub>
* [Elgg](https://elgg.org/) - Powerful open source social networking engine. `GPL-2.0` <sub>PHP</sub>
* [Enigma 1/2 BBS](https://nuskooler.github.io/enigma-bbs/) - Enigma 1/2 is a modern, multi-platform BBS engine with unlimited "callers" and legacy DOS door game support. `BSD-2-Clause` <sub>Shell/Docker/Nodejs</sub>
* [Flarum](https://flarum.org) - Delightfully simple forums. Flarum is the next-generation forum software that makes online discussion fun again. `MIT` <sub>PHP</sub>
* [Friendica](https://friendi.ca/) - Social Communication Server. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [GoToSocial](https://docs.gotosocial.org/en/latest/) - ActivityPub federated social network server implementing the Mastodon client API. `AGPL-3.0` <sub>Docker/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Habitat](https://gethabitat.org/) - A Platform for Local Communities. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Hatsu](https://hatsu.cli.rs/) - Bridge that interacts with Fediverse on behalf of your static site. `AGPL-3.0` <sub>Docker/Rust</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Hubzilla](https://hubzilla.org) - Decentralized identity, privacy, publishing, sharing, cloud storage, and communications/social platform. `MIT` <sub>PHP</sub>
* [HumHub](https://www.humhub.org/) - Flexible kit for private social networks. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Iceshrimp.NET](https://iceshrimp.net) - Federated microblogging server that communicates over ActivityPub. `EUPL-1.2` <sub>.NET/C#/Docker</sub><br><sub>⚠️ copyleft forte (`EUPL-1.2`): serviço em rede exige abrir o código</sub>
* [Isso](https://isso-comments.de/) - Lightweight commenting server written in Python and Javascript. It aims to be a drop-in replacement for Disqus. `MIT` <sub>Python/Docker</sub>
* [Lemmy](https://join-lemmy.org/) - Link aggregator for the fediverse (alternative to Reddit). `AGPL-3.0` <sub>Docker/Rust</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Loomio](https://www.loomio.org/) - Collaborative decision-making tool that makes it easy for anyone to participate in decisions which affect them. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Mastodon](https://joinmastodon.org/) - Federated microblogging server. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Misago](https://misago-project.org/) - Fully featured modern forum application that is fast, scalable and responsive. `GPL-2.0` <sub>Docker</sub>
* [Misskey](https://misskey.io/) - Decentralized app-like microblogging server/SNS for the Fediverse, using the ActivityPub protocol like GNU social and Mastodon. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Movim](https://movim.eu/) - Modern, federated social network based on XMPP, with a fully featured group-chat, subscriptions and microblogging. `AGPL-3.0` <sub>PHP/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MyBB](https://mybb.com/) - Free, extensible forum software package. `LGPL-3.0` <sub>PHP</sub>
* [NodeBB](https://nodebb.org/) - Forum software built for the modern web. `GPL-3.0` <sub>Nodejs/Docker</sub>
* [OSSN](https://www.opensource-socialnetwork.org/) - Social networking software that allows you to make a social networking website and helps your members build social relationships, with people who share similar professional or personal interests. `CAL-1.0` <sub>PHP</sub>
* [phpBB](https://www.phpbb.com/) - Flat-forum bulletin board software solution that can be used to stay in touch with a group of people or can power your entire website. `GPL-2.0` <sub>PHP</sub>
* [PieFed](https://join.piefed.social) - A link aggregator / reddit clone for the fediverse (alternative to Reddit). `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [PixelFed](https://pixelfed.social) - Ethical photo sharing platform, powered by ActivityPub federation (alternative to Instagram). `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Pleroma](https://pleroma.social) - Federated microblogging server, Mastodon, GNU social, & ActivityPub compatible. `AGPL-3.0` <sub>Elixir</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [qpixel](https://codidact.com/) - Q&A-based community knowledge-sharing software. `AGPL-3.0` <sub>Ruby</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Redlib](https://github.com/redlib-org/redlib) - An alternative private front-end to Reddit, with its origins in Libreddit. `AGPL-3.0` <sub>Rust</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [remark42](https://remark42.com/) - Lightweight and simple comment engine, which doesn't spy on users. It can be embedded into blogs, articles or any other place where readers add comments. `MIT` <sub>Docker/Go</sub>
* [Scoold](https://scoold.com) - Stack Overflow in a JAR. An enterprise-ready Q&A platform with full-text search, SAML, LDAP integration and social login support. `Apache-2.0` <sub>Java/Docker/K8S</sub>
* [Simple Machines Forum](https://www.simplemachines.org/) - Free, professional grade software package that allows you to set up your own online community within minutes. `BSD-3-Clause` <sub>PHP</sub>
* [Socialhome](https://socialhome.network) - Federated and decentralized profile builder and social network engine. `AGPL-3.0` <sub>Docker/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Talkyard](https://www.talkyard.io/) - Create a community, where your users can suggest ideas and get questions answered. And have friendly open-ended discussions and chat (Slack/StackOverflow/Discourse/Reddit/Disqus hybrid). `AGPL-3.0` <sub>Docker/Scala</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [yarn.social](https://yarn.social) - Self-Hosted, Twitter™-like Decentralised micro-logging platform. No ads, no tracking, your content, your data. `MIT` <sub>Go</sub>

## Saúde e exercício

* [Endurain](https://docs.endurain.com/) - Fitness tracking service designed to give users full control over their data and hosting environment. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [FitTrackee](https://docs.fittrackee.org/) - Simple workout/activity tracker. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Mere Medical](https://meremedical.co/) - Manage all of your medical records from Epic MyChart, Cerner, and OnPatient patient portals in one place. Privacy-focused, self-hosted, and offline-first. `GPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [OpenELIS Global](https://openelis-global.org) - Laboratory information system (LIS/LIMS) for clinical, public health, environmental and vector surveillance labs. FHIR-native, with analyzer integration (ASTM/HL7), quality control and national-scale reporting. `MPL-2.0` <sub>Java/Docker</sub>
* [OpenEMR](https://www.open-emr.org/) - Electronic health records and medical practice management solution. `GPL-3.0` <sub>PHP/Docker</sub>
* [wger](https://wger.de/) - Web-based personal workout, fitness and weight logger/tracker. It can also be used as a simple gym management utility and offers a full REST API as well. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Servidores web

* [Algernon](https://algernon.roboticoverlords.org/) - Small self-contained pure-Go web server with Lua, Markdown, HTTP/2, QUIC, Redis and PostgreSQL support. `BSD-3-Clause` <sub>Go/Docker</sub>
* [Apache HTTP Server](https://httpd.apache.org/) - Secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards. `Apache-2.0` <sub>C/deb/Docker</sub>
* [BunkerWeb](https://www.bunkerweb.io) - Next-gen Web Application Firewall (WAF) that will protect your web services. `AGPL-3.0` <sub>deb/Docker/K8S/Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Caddy](https://caddyserver.com/) - Powerful, enterprise-ready, open source web server with automatic HTTPS. `Apache-2.0` <sub>Go/deb/Docker</sub>
* [Ferron](https://ferron.sh/) - Fast, memory-safe web server written in Rust. `MIT` <sub>Rust/Docker/deb</sub>
* [go-doxy](https://github.com/yusing/godoxy) - Lightweight, simple, and  performant reverse proxy with WebUI, Docker integration, automatic shutdown/startup for container based on traffic. `MIT` <sub>Docker/Go</sub>
* [HAProxy](https://www.haproxy.org/) - Very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. `GPL-2.0` <sub>C/deb/Docker</sub>
* [Lighttpd](https://www.lighttpd.net/) - Secure, fast, compliant, and very flexible web server that has been optimized for high-performance environments. `BSD-3-Clause` <sub>C/deb/Docker</sub>
* [NGINX](https://nginx.org/en/) - HTTP and reverse proxy server, mail proxy server, and generic TCP/UDP proxy server. `BSD-2-Clause` <sub>C/deb/Docker</sub>
* [Nginx Proxy Manager](https://nginxproxymanager.com/) - Docker container for managing Nginx proxy hosts with a simple, powerful interface. `MIT` <sub>Docker</sub>
* [Pangolin](https://digpangolin.com/) - Identity-aware tunneled reverse proxy with dashboard UI, access control, and WireGuard-based tunnels (alternative to Cloudflare Tunnel, Tailscale). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Pomerium](https://www.pomerium.io) - Identity-aware reverse proxy, successor to now obsolete oauth_proxy. It inserts an OAuth step before proxying your request to the backend, so that you can safely expose your self-hosted websites to public Internet. `Apache-2.0` <sub>Go/Docker</sub>
* [SafeLine](https://waf.chaitin.com/) - Web application firewall / reverse proxy to protect your web apps from attacks and exploits. `GPL-3.0` <sub>Docker</sub>
* [Static Web Server](https://static-web-server.net/) - Cross-platform, high-performance, and asynchronous web server for static file serving. `Apache-2.0/MIT` <sub>Rust/Docker</sub>
* [SWAG (Secure Web Application Gateway)](https://github.com/linuxserver/docker-swag) - Nginx webserver and reverse proxy with PHP support, built-in Certbot (Let's Encrypt) client and fail2ban integration. `GPL-3.0` <sub>Docker</sub>
* [Traefik](https://traefik.io/) - HTTP reverse proxy and load balancer that makes deploying microservices easy. `MIT` <sub>Go/Docker</sub>
* [UUSEC WAF](https://waf.uusec.com/) - Industry-leading high-performance, AI and semantic technology web application firewall and API security gateway (fork of nginx). `GPL-3.0` <sub>C/Lua/Docker</sub>
* [Vinyl Cache](https://vinyl-cache.org/) - Web application accelerator/caching HTTP reverse proxy (formerly Varnish). `BSD-2-Clause` <sub>Go/deb/Docker</sub>
* [Zoraxy](https://zoraxy.aroz.org/) - General purpose HTTP reverse proxy and forwarding tool. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Streaming — multimídia

* [ClipBucket](https://clipbucket.fr/) - Start your own video sharing website (YouTube/Netflix Clone) in a matter of minutes. `AAL` <sub>Docker/PHP</sub>
* [cmyflix](https://github.com/farfalleflickan/cmyflix) - Minimalist Plex/Jellyfin alternative to stream video. `AGPL-3.0` <sub>C/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Gerbera](https://gerbera.io/) - UPnP Media Server, which allows you to stream your digital media throughout your home network and listen to/watch it on a variety of UPnP compatible devices. `GPL-2.0` <sub>Docker/deb/C++</sub>
* [Icecast 2](https://icecast.org) - Streaming audio/video server which can be used to create an Internet radio station or a privately running jukebox and many things in between. `GPL-2.0` <sub>C</sub>
* [Jellyfin](https://jellyfin.org) - Media server for audio, video, books, comics, and photos with a sleek interface and robust transcoding capabilities. Almost all modern platforms have clients, including Roku, Android TV, iOS, and Kodi. `GPL-2.0` <sub>C#/deb/Docker</sub>
* [Karaoke Eternal](https://www.karaoke-eternal.com) - Host awesome karaoke parties where everyone can easily find and queue songs from their phone's browser. The player is also fully browser-based with support for MP3+G, MP4 and WebGL visualizations. `ISC` <sub>Docker/Nodejs</sub>
* [Kodi](https://kodi.tv/) - Multimedia/Entertainment center, formerly known as XBMC. Runs on Android, BSD, Linux, macOS, iOS and Windows. `GPL-2.0` <sub>C++/deb</sub>
* [Kyoo](https://github.com/zoriya/kyoo) - Innovative media browser designed for seamless streaming of anime, series and movies, offering advanced features like dynamic transcoding, auto watch history and intelligent metadata retrieval. `GPL-3.0` <sub>Docker</sub>
* [MediaMTX](https://mediamtx.org) - Ready-to-use, zero-dependency real-time media server and proxy to publish, read, record, playback and route video/audio streams over SRT, WebRTC, RTSP, RTMP, HLS, MPEG-TS, RTP. `MIT` <sub>Go/Docker</sub>
* [Meelo](https://github.com/Arthi-chaud/Meelo) - Personal Music Server, designed for collectors and music maniacs. `GPL-3.0` <sub>Docker</sub>
* [MistServer](https://mistserver.org/) - Public domain streaming media server that works with any device and any format. `Unlicense` <sub>C++</sub>
* [NymphCast](http://nyanko.ws/nymphcast.php) - Turn your choice of Linux-capable hardware into an audio and video source for a television or powered speakers (alternative to Chromecast). `BSD-3-Clause` <sub>C++</sub>
* [Rygel](https://gnome.pages.gitlab.gnome.org/rygel/) - UPnP AV MediaServer that allows you to easily share audio, video, and pictures. Media player software may use Rygel to become a MediaRenderer that may be controlled remotely by a UPnP or DLNA Controller. `LGPL-2.1` <sub>C</sub>
* [Stash](https://stashapp.cc) - A web-based library organizer and player for your adult media stash, with auto-tagging and metadata scraping support. `AGPL-3.0` <sub>Docker/Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [µStreamer](https://github.com/pikvm/ustreamer) - Lightweight and very quick server to stream MJPEG video from any V4L2 device to the net. `GPL-3.0` <sub>C/deb</sub>
* [üWave](https://u-wave.net/) - Self-hosted collaborative listening platform. Users take turns playing media—songs, talks, gameplay videos, or anything else—from a variety of media sources like YouTube and SoundCloud. `MIT` <sub>Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>

## Streaming — vídeo

* [CyTube](https://github.com/calzoneman/sync) - Synchronize media, chat, and more for an arbitrary number of channels. `MIT` <sub>Nodejs</sub>
* [Invidious](https://github.com/iv-org/invidious) - Alternative YouTube front-end. `AGPL-3.0` <sub>Docker/Crystal</sub><br><sub>⚠️ não mantido pelos autores · copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MediaCMS](https://mediacms.io) - Modern, fully featured open source video and media CMS, written in Python/Django/React, featuring a REST API. `AGPL-3.0` <sub>Python/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OvenMediaEngine](https://github.com/OvenMediaLabs/OvenMediaEngine) - Streaming Server with Sub-Second Latency. `AGPL-3.0` <sub>C++/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Owncast](https://owncast.online/) - Decentralized single-user live video streaming and chat server for running your own live streams similar in style to the large mainstream options. `MIT` <sub>Go</sub>
* [PeerTube](https://joinpeertube.org/en/) - Decentralized video streaming platform using P2P (BitTorrent) directly in the web browser. `AGPL-3.0` <sub>Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Rapidbay](https://github.com/hauxir/rapidbay/) - Videostreaming service/torrent client that allows searching and playing videos from torrents in the browser or from a Chromecast/AppleTV/Smart TV. `MIT` <sub>Python/Docker</sub>
* [Restreamer](https://datarhei.github.io/restreamer/) - Access H.264 real-time video streaming on your website without a streaming provider. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [SRS](https://ossrs.io/) - A simple, high efficiency and real-time video server, supports RTMP, WebRTC, HLS, HTTP-FLV and SRT. `MIT` <sub>Docker/C++</sub>
* [SyncTube](https://github.com/RblSb/SyncTube) - Lightweight and very simple to setup CyTube alternative to watch videos with friends and chat. `MIT` <sub>Nodejs/Haxe</sub>
* [Tiramisu](https://github.com/MrRobotoGit/tiramisu) - BitTorrent engine with a FUSE virtual filesystem that streams torrents live to Plex/Jellyfin without downloading (alternative to Real-Debrid). `GPL-2.0` <sub>Go/Docker</sub>
* [Tube](https://git.mills.io/prologic/tube) - Youtube-like (_without censorship and features you don't need!_) video sharing app written in Go which also supports automatic transcoding to MP4 H.265 AAC, multiple collections and RSS feed. `MIT` <sub>Go</sub>
* [Tube Archivist](https://tubearchivist.com/) - Organize, search, and enjoy your YouTube collection. Subscribe, download, and track viewed content with metadata indexing and a user-friendly interface. `GPL-3.0` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [VideoLAN Client (VLC)](https://www.videolan.org/) - Cross-platform multimedia player client and server supporting most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols. `GPL-2.0` <sub>C/deb</sub>

## Streaming — áudio

* [Ampache](https://ampache.org/) - Web based audio/video streaming application. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Audiobookshelf](https://www.audiobookshelf.org/) - Audiobook and podcast server. It streams all audio formats, keeps and syncs progress across devices. Comes with open-source apps for Android and iOS. `GPL-3.0` <sub>Docker/deb/Nodejs</sub>
* [Audioserve](https://github.com/izderadicka/audioserve) - Simple personal server to serve audio files from directories (audiobooks, music, podcasts...). Focused on simplicity and supports sync of play position between clients. `MIT` <sub>Rust</sub>
* [AzuraCast](https://www.azuracast.com/) - Modern and accessible web radio management suite. `Apache-2.0` <sub>Docker</sub>
* [Beets](https://beets.io/) - Music library manager and MusicBrainz tagger (command-line and Web interface). `MIT` <sub>Python/deb</sub>
* [Black Candy](https://github.com/blackcandy-org/blackcandy) - Music streaming server. `MIT` <sub>Docker/Ruby</sub>
* [BotWave](https://botwave.dpip.lol) - FM broadcasting system with server-client architecture for managing multiple Raspberry Pi transmitters remotely. `GPL-3.0` <sub>Python</sub>
* [Funkwhale](https://dev.funkwhale.audio/funkwhale) - Modern, web-based, convivial, multi-user and free music server. `BSD-3-Clause` <sub>Python</sub>
* [gonic](https://github.com/sentriz/gonic) - Lightweight music streaming server. Subsonic compatible. `GPL-3.0` <sub>Go/Docker</sub>
* [koel](https://koel.dev/) - Personal music streaming server that works. `MIT` <sub>PHP</sub>
* [LibreTime](https://libretime.org) - Broadcast streaming radio on the web (fork of [Airtime](https://github.com/sourcefabric/Airtime)). `AGPL-3.0` <sub>Docker/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [LMS](https://github.com/epoupon/lms) - Access your self-hosted music using a web interface. `GPL-3.0` <sub>Docker/deb/C++</sub>
* [Lyrion Music Server](https://lyrion.org/) - Server software which controls a wide range of Squeezebox/Slim Devices audio players and compatible hardware (formerly Logitech Media Server). `GPL-2.0` <sub>deb/Docker/Perl</sub>
* [moOde Audio](https://moodeaudio.org/) - Audiophile-quality music playback for the wonderful Raspberry Pi family of single board computers. `GPL-3.0` <sub>PHP</sub>
* [Mopidy](https://docs.mopidy.com/) - Extensible music server. Offers a superset of the mpd API, as well as integration with 3rd party services like Spotify, SoundCloud etc. `Apache-2.0` <sub>Python/deb</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [mpd](https://www.musicpd.org/) - Daemon to remotely play music, stream music, handle and organize playlists. Many clients available. `GPL-2.0` <sub>C++</sub>
* [mStream](https://mstream.io/) - Music streaming server with GUI management tools. Runs on Mac, Windows, and Linux. `GPL-3.0` <sub>Nodejs</sub>
* [multi-scrobbler](https://foxxmd.github.io/multi-scrobbler) - Scrobble plays from multiple sources to multiple scrobbling services. `MIT` <sub>Nodejs/Docker</sub>
* [musikcube](https://github.com/clangen/musikcube) - Streaming audio server with Linux/macOS/Windows/Android clients. `BSD-3-Clause` <sub>C++/deb</sub>
* [Navidrome Music Server](https://www.navidrome.org) - Modern Music Server and Streamer, compatible with Subsonic/Airsonic. `GPL-3.0` <sub>Docker/Go</sub>
* [Pinepods](https://www.pinepods.online/) - Podcast management system with multi-user support. Pinepods utilizes a central database so aspects like listen time and themes follow from device to device. `GPL-3.0` <sub>Docker</sub>
* [Polaris](https://github.com/agersant/polaris) - Music browsing and streaming application optimized for large music collections, ease of use and high performance. `MIT` <sub>Rust/Docker</sub>
* [Snapcast](https://github.com/snapcast/snapcast) - Synchronous multiroom audio server. `GPL-3.0` <sub>C++/deb</sub>
* [Stretto](https://github.com/benkaiser/stretto) - Music player with Youtube/Soundcloud import and iTunes/Spotify discovery. `MIT` <sub>Nodejs</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Supysonic](https://github.com/spl0k/supysonic) - Python implementation of the Subsonic server API. `AGPL-3.0` <sub>Python/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [SwingMusic](https://swingmusic.vercel.app/) - Swing Music is a beautiful, self-hosted music player and streaming server for your local audio files. Like a cooler Spotify ... but bring your own music. `MIT` <sub>Python/Docker</sub>
* [vod2pod-rss](https://github.com/madiele/vod2pod-rss) - Convert YouTube and Twitch channels to podcasts, no storage required. Transcodes VoDs to MP3 192k on the fly, generates an RSS feed to use in podcast clients. `MIT` <sub>Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>

## Suítes de escritório

* [Collabora Online Development Edition](https://www.collaboraoffice.com/code) - Collabora Online Development Edition (CODE) is a powerful LibreOffice-based online office that supports all major document, spreadsheet and presentation file formats, which you can integrate in your own infrastructure. `MPL-2.0` <sub>C++</sub>
* [CryptPad](https://cryptpad.org) - Collaboration suite built to enable collaboration, synchronizing changes to documents in real time. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Digislides](https://ladigitale.dev/digislides/) - Create multimedia presentations in a quick and easy way. (documentation in French). `AGPL-3.0` <sub>Nodejs/PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Etherpad](https://etherpad.org/) - Highly customizable online editor providing collaborative editing in real-time. `Apache-2.0` <sub>Nodejs/Docker</sub>
* [Grist](https://getgrist.com/) - Next-generation spreadsheet with relational structure, formula-based access control, and a portable, self-contained format (alternative to Airtable). `Apache-2.0` <sub>Nodejs/Python/Docker</sub>
* [ONLYOFFICE](https://helpcenter.onlyoffice.com/faq/server-opensource.aspx) - Office suite that enables you to manage documents, projects, team and customer relations in one place. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Tarefas e listas

* [4ga Boards](https://4gaboards.com) - Straightforward realtime kanban boards management for intuitive task tracking. Featuring an elegant dark mode, collapsible todo lists, and multitasking tools to supercharge your team's productivity. `MIT` <sub>Nodejs/Docker/K8S</sub>
* [AppFlowy](https://appflowy.io/) - Build detailed lists of to-do’s for different projects while tracking the status of each one. Open Source Notion Alternative. `AGPL-3.0` <sub>Rust/Dart/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [dayGLANCE](https://dayglance.app) - Day planner with drag-and-drop time blocking, inbox, recurring tasks, habits, routines, goals, projects and Pomodoro focus mode, plus iCal and CalDAV calendar sync. Data stays in the browser, with optional WebDAV or GLANCEvault sync. `MIT` <sub>Javascript/Docker</sub>
* [Donetick](https://donetick.com) - Task and chore management tool for personal and family use, with advanced scheduling, flexible assignment, and group sharing capabilities, detailed history, automation via API, simple and modern design. `AGPL-3.0` <sub>Go/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Focus Flow](https://github.com/francesco-gaglione/focus_flow_cloud) - Complete ecosystem for time management using the Pomodoro technique. `MIT` <sub>Docker/K8S</sub>
* [HamsterBase Tasks](https://tasks.hamsterbase.com) - A tool to help organize ideas and build great things. Plan, organize, build and ship. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kan](https://kan.bn/) - Flexible kanban app that helps you organise work, track progress, and deliver results (alternative to Trello). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Kanboard](https://kanboard.org/) - Simple visual task board. `MIT` <sub>PHP</sub>
* [Listaway](https://github.com/jeffrpowell/listaway/) - List management app for creating and publicly sharing lists of items. Supports auth, admin tools, item notes and priorities, and opt-in public read-only links with randomized URLs (alternative to Amazon Lists). `MIT` <sub>Docker</sub>
* [myTinyTodo](https://www.mytinytodo.net/) - Simple way to manage your todo list in AJAX style. Uses PHP, jQuery, SQLite/MySQL. GTD compliant. `GPL-2.0` <sub>PHP</sub>
* [Nullboard](https://github.com/apankrat/nullboard) - Single-page minimalist kanban board; compact, highly readable and quick to use. `BSD-2-Clause` <sub>Javascript</sub>
* [OpenHabitTracker](https://openhabittracker.net) - Track habits, tasks and notes with time tracking, calendar view and completion statistics. `GPL-3.0` <sub>Docker</sub>
* [Our Shopping List](https://codeberg.org/nanawel/our-shopping-list) - Simple shared list application including shopping lists and any other small todo-list that needs to be used collaboratively. `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Super Productivity](https://super-productivity.com) - Advanced todo list app with integrated timeboxing and time tracking capabilities. Integrates with Jira, GitHub, GitLab, Redmine and OpenProject. `MIT` <sub>Docker</sub>
* [Task Keeper](https://github.com/nymanjens/piga) - List editor for power users, backed by a self-hosted server. `Apache-2.0` <sub>Scala</sub>
* [Tasks.md](https://github.com/BaldissaraMatheus/Tasks.md) - A self-hosted, file based task management board that supports Markdown syntax. `MIT` <sub>Docker</sub>
* [Taskwarrior](https://taskwarrior.org/) - Taskwarrior is Free and Open Source Software that manages your TODO list from your command line. It is flexible, fast, efficient, and unobtrusive. It does its job then gets out of your way. `MIT` <sub>C++</sub>
* [Tellor](https://tellor.cc/) - Minimalist single-user kanban todo app. Clean, simplified, and compact UI. Can import boards from Trello. `MIT` <sub>PHP</sub>
* [Tracks](https://www.getontracks.org/) - Web-based application to help you implement David Allen’s [Getting Things Done™](https://en.wikipedia.org/wiki/Getting_Things_Done) methodology. `GPL-2.0` <sub>Ruby</sub>
* [tududi](https://tududi.com/) - Task management tool with hierarchical structure, smart recurring tasks, and seamless Telegram integration. `MIT` <sub>Docker</sub>
* [Vikunja](https://vikunja.io/) - The to-do app to organize your life. `AGPL-3.0/GPL-3.0` <sub>Go</sub>
* [Wekan](https://wekan.github.io/) - Open-source Trello-like kanban. `MIT` <sub>Nodejs</sub>
* [Will Be Done](https://will-be-done.app/) - Offline-first task manager with weekly planning, project boards, real-time sync, Vim keybindings, desktop quick add, and import from popular task managers (alternative to TickTick, Todoist). `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## Transferência e sincronização de arquivos

* [bewCloud](https://bewcloud.com) - File sharing + sync, notes, and photos (alternative to Nextcloud and ownCloud's RSS reader). `AGPL-3.0` <sub>Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Cloudreve](https://cloudreve.org/) - File management and sharing system, supports multiple storage providers. `GPL-3.0` <sub>Docker/Go</sub>
* [Git Annex](https://git-annex.branchable.com/) - File synchronization between computers, servers, external drives. `GPL-3.0` <sub>Haskell</sub>
* [Kinto](https://kinto.readthedocs.org) - Minimalist JSON storage service with synchronisation and sharing abilities. `Apache-2.0` <sub>Python</sub>
* [Nextcloud](https://nextcloud.com/) - Access and share your files, calendars, contacts, mail and [more](https://apps.nextcloud.com/) from any device, on your terms. `AGPL-3.0` <sub>PHP/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [OpenCloud](https://docs.opencloud.eu/) - File Sharing and Collaboration Platform. `Apache-2.0` <sub>Docker/Go/Nodejs</sub>
* [OpenSSH SFTP server](https://www.openssh.com/) - Secure File Transfer Program. `BSD-2-Clause` <sub>C/deb</sub>
* [ownCloud](https://owncloud.org/) - All-in-one solution for saving, synchronizing, viewing, editing and sharing files, calendars, address books and more. `AGPL-3.0` <sub>PHP/Docker/deb</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Peergos](https://peergos.org) - Secure and private space online where you can store, share and view your photos, videos, music and documents. Also includes a calendar, news feed, task lists, chat and email client. `AGPL-3.0` <sub>Java</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Puter](https://puter.com/) - Web-based operating system designed to be feature-rich, exceptionally fast, and highly extensible. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Pydio](https://pydio.com/) - Turn any web server into a powerful file management system and an alternative to mainstream cloud storage providers. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Samba](https://www.samba.org/) - Samba is the standard Windows interoperability suite of programs for Linux and Unix. It provides secure, stable and fast file and print services for all clients using the SMB/CIFS protocol. `GPL-3.0` <sub>C</sub>
* [Seafile](https://www.seafile.com/en/home/) - File hosting and sharing solution primary for teams and organizations. `GPL-2.0/GPL-3.0/AGPL-3.0/Apache-2.0` <sub>C</sub>
* [Sync-in](https://sync-in.com) - File storage, syncing, sharing, and collaboration with real-time editing, permission management, and desktop/CLI clients. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Syncthing](https://syncthing.net/) - Syncthing is an open source peer-to-peer file synchronisation tool. `MPL-2.0` <sub>Go/Docker/deb</sub>
* [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - Unison is a file-synchronization tool for OSX, Unix, and Windows. `GPL-3.0` <sub>deb/OCaml</sub>

## Utilitários de rede

* [beelzebub](https://beelzebub-honeypot.com/) - Honeypot framework designed to provide a highly secure environment for detecting and analyzing cyber attacks. `MIT` <sub>Docker/K8S/Go</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [Canary Tokens](https://canarytokens.org) - Generates lightweight, embedded honeypot triggers called canary tokens for detecting unauthorized access. `BSD-3-Clause` <sub>Docker/Python</sub>
* [MyIP](https://ipcheck.ing) - All in one IP Toolbox. Easy to check what's your IPs, IP geolocation, check for DNS leaks, examine WebRTC connections, speed test, ping test, MTR test, check website availability and more. `MIT` <sub>Nodejs/Docker</sub><br><sub>⚠️ não mantido pelos autores</sub>
* [MySpeed](https://myspeed.dev/) - Speed test analysis software that shows your internet speed for up to 30 days. `MIT` <sub>Docker/Nodejs</sub>
* [NetAlertX](https://netalertx.com/) - Network intruder and presence detector. Scans for devices connected to your network and alerts you if new and unknown devices are found. `GPL-3.0` <sub>Docker</sub>
* [PlugNPiN](https://deepspace2.github.io/PlugNPiN) - Automatically scrapes containers with specific labels and creates local DNS/CNAME entries in Pi-Hole/AdGuard Home and proxy hosts in Nginx Proxy Manager. `GPL-3.0` <sub>Docker</sub>
* [Speed Test by OpenSpeedTest™](https://openspeedtest.com/) - Free & Open-Source HTML5 Network Performance Estimation Tool. `MIT` <sub>Docker</sub>
* [Speedtest Tracker](https://docs.speedtest-tracker.dev/) - Monitor the performance and uptime of your internet connection. `MIT` <sub>Docker/K8S</sub>
* [Upsnap](https://github.com/seriousm4x/UpSnap) - A simple Wake on LAN (WOL) dashboard app. Wake up devices on your network and see current status. `MIT` <sub>Go/Docker</sub>
* [Wakupator](https://github.com/Gibus21250/Wakupator) - Wake On LAN Machine Manager based on network traffic. `MIT` <sub>C</sub>
* [WatchYourLAN](https://github.com/aceberg/WatchYourLAN) - Lightweight network IP scanner with notifications, history, export to Grafana. `MIT` <sub>Docker/Go/deb</sub>
* [whois](https://github.com/KincaidYang/whois) - WHOIS/RDAP query API for domains, IP addresses, CIDR prefixes and ASNs, with unified JSON output, caching, API key authentication, batch queries and MCP support for AI assistants. `MIT` <sub>Go/Docker</sub>

## Viagens

* [Surmai](https://surmai.app/) - Collaborative personal and family travel organizer. `MIT` <sub>Docker</sub>

## Videoconferência

* [BigBlueButton](https://bigbluebutton.org/) - Supports real-time sharing of audio, video, slides (with whiteboard controls), chat, and the screen. Instructors can engage remote students with polling, emojis, and breakout rooms. `LGPL-3.0` <sub>Java</sub>
* [Galene](https://galene.org/) - Video conferencing server that is easy to deploy and that requires moderate server resources. `MIT` <sub>Go</sub>
* [Janus](https://janus.conf.meetecho.com/) - General-purpose, lightweight, minimalist WebRTC Server. `GPL-3.0` <sub>C</sub>
* [Jitsi Meet](https://jitsi.org/Projects/JitsiMeet) - WebRTC application that uses Jitsi Videobridge to provide high quality, scalable video conferences. `Apache-2.0` <sub>Nodejs/Docker/deb</sub>
* [Jitsi Video Bridge](https://jitsi.org/Projects/JitsiVideobridge) - WebRTC compatible Selective Forwarding Unit (SFU) that allows for multiuser video communication. `Apache-2.0` <sub>Java/deb</sub>
* [MiroTalk C2C](https://c2c.mirotalk.com) - Real-time cam-2-cam video calls & screen sharing, end-to-end encrypted, to embed in any website with a simple iframe. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MiroTalk P2P](https://p2p.mirotalk.com) - Simple, secure, fast real-time video conferences up to 4k and 60fps, compatible with all browsers and platforms. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [MiroTalk SFU](https://sfu.mirotalk.com) - Simple, secure, scalable real-time video conferences up to 4k, compatible with all browsers and platforms. `AGPL-3.0` <sub>Nodejs/Docker</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [plugNmeet](https://www.plugnmeet.org/) - Scalable and high performance web conferencing system. `MIT` <sub>Docker/Go</sub>

## Vigilância por vídeo

* [Bluecherry](https://github.com/bluecherrydvr/bluecherry-apps) - Closed-circuit television (CCTV) software application which supports IP and Analog cameras. `GPL-2.0` <sub>PHP</sub>
* [Frigate](https://frigate.video/) - Monitor your security cameras with locally processed AI. `MIT` <sub>Docker/Python/Nodejs</sub>
* [motionEye](https://github.com/motioneye-project/motioneye) - Online interface for the software Motion, a video surveillance program with motion detection. `GPL-3.0` <sub>Python/Docker</sub>
* [Secluso](https://secluso.com) - Private DIY home security camera system for Raspberry Pi, with end-to-end encrypted remote access and mobile apps for live video, alerts, and recording playback. `GPL-3.0` <sub>Rust</sub>
* [SentryShot](https://codeberg.org/SentryShot/sentryshot) - Video surveillance management system. `GPL-2.0` <sub>Docker/Rust</sub>
* [Strix](https://github.com/eduard256/Strix) - Auto-discovers working stream URLs for IP cameras and generates ready-to-use Frigate and go2rtc configs. `MIT` <sub>Go/Docker</sub>
* [Viseron](https://viseron.netlify.app/) - Self-hosted, local-only NVR and AI Computer Vision software. With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor. `MIT` <sub>Docker</sub>
* [Zoneminder](https://www.zoneminder.com/) - Closed-circuit television (CCTV) software application which supports IP, USB and Analog cameras. `GPL-2.0` <sub>PHP/deb</sub>

## Wikis

* [AmuseWiki](https://amusewiki.org/) - Amusewiki is based on the Emacs Muse markup, remaining mostly compatible with the original implementation. It can work as a read-only site, as a moderated wiki, or as a fully open wiki or even as a private site. `GPL-1.0` <sub>Perl/Docker</sub>
* [BookStack](https://www.bookstackapp.com/) - Organize and store information. Stores documentation in a book like fashion. `MIT` <sub>PHP/Docker</sub>
* [django-wiki](https://github.com/django-wiki/django-wiki) - Wiki system with complex functionality for simple integration and a superb interface. Store your knowledge with style: Use django models. `GPL-3.0` <sub>Python</sub>
* [docmost Community Edition](https://docmost.com/) - Collaborative wiki and documentation software (alternative to Confluence, Notion). `AGPL-3.0` <sub>Docker/Nodejs</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Documize](https://documize.com) - Modern Docs + Wiki software with built-in workflow, single binary executable, just bring MySQL/Percona. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Dokuwiki](https://www.dokuwiki.org/DokuWiki) - Easy to use, lightweight, standards-compliant wiki engine with a simple syntax allowing reading the data outside the wiki. All data is stored in plain text files, therefore no database is required. `GPL-2.0` <sub>PHP</sub>
* [Feather Wiki](https://feather.wiki) - A lightning fast and infinitely extensible tool for creating personal non-linear notebooks, databases, and wikis that is entirely self-contained, runs in your browser, and is only 58 kilobytes in size. `AGPL-3.0` <sub>Javascript</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Gitit](https://github.com/jgm/gitit) - Wiki program that stores pages and uploaded files in a git repository, which can then be modified using the VCS command line tools or the wiki's web interface. `GPL-2.0` <sub>Haskell</sub>
* [Gollum](https://github.com/gollum/gollum) - Simple, Git-powered wiki with a sweet API and local frontend. `MIT` <sub>Ruby</sub>
* [LeafWiki](https://github.com/perber/leafwiki) - A fast wiki for people who think in folders, not feeds. Fast editing. Tree navigation. Markdown on disk. `MIT` <sub>Docker/Go</sub>
* [Mediawiki](https://www.mediawiki.org/wiki/MediaWiki) - Wiki software package that powers Wikipedia and all other Wikimedia projects, serving hundreds of millions of users each month. `GPL-2.0` <sub>PHP</sub>
* [Mycorrhiza Wiki](https://mycorrhiza.wiki/) - Filesystem and git-based wiki engine written in Go using Mycomarkup as its primary markup language. `AGPL-3.0` <sub>Go</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Otter Wiki](https://otterwiki.com/) - Simple, easy to use wiki software using markdown. `MIT` <sub>Docker</sub>
* [PmWiki](https://www.pmwiki.org) - Wiki-based system for collaborative creation and maintenance of websites. `GPL-3.0` <sub>PHP</sub>
* [Raneto](https://raneto.com/) - Knowledgebase platform that uses static Markdown files. `MIT` <sub>Nodejs</sub>
* [TiddlyWiki](https://tiddlywiki.com/) - Reusable non-linear personal web notebook. `BSD-3-Clause` <sub>Nodejs</sub>
* [Tiki](https://tiki.org/HomePage) - Wiki CMS Groupware with the most built-in features. `LGPL-2.1` <sub>PHP</sub>
* [W](https://w.club1.fr) - Lightweight, mutli-user, flat-file-database Wiki engine. Create pages quickly and edit them in your Web browser using Mardown/HTML/CSS/JS. The main difference with other wiki is that you are encouraged to customize each page style individually. `AGPL-3.0` <sub>PHP</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [WackoWiki](https://wackowiki.org/) - WackoWiki is a light and easy to install multilingual Wiki-engine. `BSD-3-Clause` <sub>PHP</sub>
* [Wiki-Go](https://leomoon.com/downloads/web-apps/wiki-go/) - A modern, feature-rich, databaseless flat-file wiki platform. `GPL-3.0` <sub>Go/Docker</sub>
* [Wiki.js](https://js.wiki/) - Modern, lightweight and powerful wiki app using Git and Markdown. `AGPL-3.0` <sub>Nodejs/Docker/K8S</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [WikiDocs](https://www.wikidocs.app/) - A databaseless markdown flat-file wiki engine. `MIT` <sub>PHP/Docker</sub>
* [WiKiss](https://wikiss.tuxfamily.org/) - Wiki, simple to use and install. `GPL-2.0` <sub>PHP</sub>
* [XWiki](https://www.xwiki.org) - Second generation wiki that allows the user to extend its functionalities with a powerful extension-based architecture. `LGPL-2.1` <sub>Java/Docker/deb</sub>
* [Zim](https://zim-wiki.org/) - Graphical text editor used to maintain a collection of wiki pages. Each page can contain links to other pages, simple formatting and images. `GPL-2.0` <sub>Python/deb</sub>

## XMPP — clientes web

* [Converse.js](https://conversejs.org/) - XMPP chat client in your browser. `MPL-2.0` <sub>Javascript</sub>
* [Libervia](https://repos.goffi.org/libervia-web) - Web frontend from Salut à Toi. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>
* [Salut à Toi](https://www.salut-a-toi.org/) - Multipurpose, multi frontend, libre and decentralized communication tool. `AGPL-3.0` <sub>Python</sub><br><sub>⚠️ copyleft forte (`AGPL-3.0`): serviço em rede exige abrir o código</sub>

## XMPP — servidores

* [ejabberd](https://www.ejabberd.im/) - XMPP instant messaging server. `GPL-2.0` <sub>Erlang/Docker</sub>
* [MongooseIM](https://www.erlang-solutions.com/products/mongooseim.html) - Mobile messaging platform with a focus on performance and scalability. `GPL-2.0` <sub>Erlang/Docker/K8S</sub>
* [Openfire](https://www.igniterealtime.org/projects/openfire/) - Real time collaboration (RTC) server. `Apache-2.0` <sub>Java</sub>
* [Prosody IM](https://prosody.im/) - Feature-rich and easy to configure XMPP server. `MIT` <sub>Lua</sub>
* [Snikket](https://snikket.org/) - All-in-one Dockerized easy XMPP solution, including web admin and clients. `Apache-2.0` <sub>Docker</sub>
* [Tigase](https://tigase.net/xmpp-server) - XMPP server implementation in Java. `GPL-3.0` <sub>Java</sub>
<!-- FIM:LISTA -->

## Como usar isto

Ideias de projeto a partir destes softwares, inclusive cruzando com os achados da lista
principal: [`IDEIAS-SELFHOSTED.md`](IDEIAS-SELFHOSTED.md).

Para procurar aqui, a busca do repositório não cobre este arquivo (ela lê `achados/`) — use
`grep` sobre a fonte, que é tabular e responde melhor:

```bash
grep -i "kanban"      dados/selfhosted.tsv | cut -f1,2,4
awk -F'\t' '$4=="MIT" && $1 ~ /CRM/' dados/selfhosted.tsv | cut -f2,3
awk -F'\t' '$6=="sim"' dados/selfhosted.tsv | wc -l      # quantos estão abandonados
```

Para atualizar a coleção quando a fonte mudar:

```bash
curl -sSL -o /tmp/ash.md \
  https://raw.githubusercontent.com/awesome-selfhosted/awesome-selfhosted/master/README.md
python3 scripts/importar_selfhosted.py /tmp/ash.md
python3 scripts/indexar_selfhosted.py
```

---

<sub>Lista gerada por `scripts/indexar_selfhosted.py` a partir de `dados/selfhosted.tsv`,
importado do awesome-selfhosted. O conteúdo original é da comunidade daquele projeto
(CC-BY-SA-3.0); cada software listado mantém a própria licença.</sub>

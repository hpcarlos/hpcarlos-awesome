---
titulo: "lobehub — plataforma de orquestração de agentes de IA"
nome: lobehub
tldr: "Plataforma para operar equipes de agentes — grupos, agendamento, memória editável e plugins MCP — sob licença própria com restrições comerciais."
url: https://github.com/lobehub/lobehub
tipo: projeto
categorias: [ia, web]
tags: [agentes, self-hosted, nextjs, mcp, chat, typescript]
status: novo
nota: 3
adicionado: 2026-08-27
fonte: enviado pelo hpcarlos
relacionados: [2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md, 2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md]
---

# lobehub — plataforma de orquestração de agentes de IA

## Resumo

Plataforma que se posiciona como "operador-chefe de agentes": em vez de uma janela de chat,
propõe contratar, agendar e monitorar equipes de agentes rodando o tempo todo. Traz
construtor de agentes por configuração, grupos que colaboram entre si com páginas
compartilhadas, agendamento de tarefas, memória pessoal estruturada e editável, e
integração com um catálogo grande de ferramentas via plugins MCP. Monorepo em pnpm com
Next.js e React, publicando também pacotes próprios de UI, ícones e TTS. Existe versão
hospedada pelos mantenedores.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o terceiro projeto da coleção a atacar o mesmo problema — operar vários agentes —
e o mais maduro em termos de produto acabado. Vale como referência de interface e de
recursos, mesmo que a licença atrapalhe o uso.

## Pontos-chave

- **⚠️ A licença é o ponto decisivo, e não é permissiva.** O projeto usa a *LobeHub
  Community License*, uma licença própria com restrições de uso comercial — não é MIT,
  Apache nem AGPL. **Leia os termos antes de qualquer plano** que envolva cliente,
  produto ou revenda; é a diferença entre "posso usar isso no trabalho" e "não posso".
  Trate esta linha como pendência aberta: eu não li o texto da licença, apenas registrei
  que ela existe e é própria.
- **Comparado aos outros dois da coleção:** o
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  é governança sóbria (custo, auditoria, RBAC) sob MIT; o
  [munder-difflin](2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)
  é experimento visual sob MIT; o lobehub é o produto mais completo dos três e o único com
  licença restritiva. A escolha é entre acabamento e liberdade.
- **Memória editável** é o recurso mais interessante: memória que o usuário pode abrir e
  corrigir, em vez de um histórico opaco. É o tipo de decisão de produto que vale copiar
  como ideia, independentemente do código.
- **Stack:** monorepo pnpm com Next.js, React, Zustand, Drizzle ORM, Docker e deploy em um
  clique em várias nuvens. Há modo SPA separado para rodar só o frontend.
- **Requer chave de provedor** (a documentação parte de `OPENAI_API_KEY`), com suporte a
  proxy customizado — o que abre a porta para apontá-lo a um gateway próprio.
- **Números não verificados** (API do GitHub bloqueada nesta sessão), embora o volume de
  commits e o monorepo indiquem projeto grande e ativo.

## Ideias de projeto

- **Ler a licença antes de qualquer outra coisa** — se ela permitir o seu caso de uso, o
  projeto entra na disputa; se não, ele vira apenas referência visual e o
  [mission-control](2026-08-23-mission-control-plano-de-controle-self-hosted-para-operar-ag.md)
  fica como escolha prática. É uma hora de leitura que decide o resto. _Esforço: baixo._
- **Apontar para um gateway próprio** — como aceita URL de proxy, dá para rodá-lo sobre o
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) ou o
  [OmniRoute](2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md),
  ganhando controle de custo e log sem depender do que a plataforma oferece.
  _Esforço: baixo._
- **Copiar a ideia da memória editável** — implementar memória que o usuário revisa e
  corrige em qualquer projeto seu de agente. É desenho de produto, não código: a lição
  transfere para o [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) ou para
  qualquer assistente que você venha a montar. _Esforço: médio._
- **Estudar o monorepo como referência de organização** — separar `apps/`, `packages/` e
  `plugins/` com pnpm workspaces, publicando UI e ícones como pacotes próprios, é um
  padrão bem executado aqui e reaproveitável em projeto seu. _Esforço: baixo._

## Notas

```bash
# docker (caminho recomendado)
mkdir lobehub-db && cd lobehub-db
bash <(curl -fsSL https://lobe.li/setup.sh)
docker compose up -d

# desenvolvimento
git clone https://github.com/lobehub/lobehub.git
cd lobehub && pnpm install
pnpm dev             # full-stack
pnpm run dev:spa     # só o frontend, porta 9876
```

- O script de instalação é baixado e executado direto do site do projeto — leia antes de
  rodar, como sempre.
- Versão hospedada pelos mantenedores em app.lobehub.com, útil para avaliar a interface
  sem instalar nada.
- **Pendência registrada:** conferir os termos exatos da *LobeHub Community License* e
  anotar aqui o veredito para uso comercial.

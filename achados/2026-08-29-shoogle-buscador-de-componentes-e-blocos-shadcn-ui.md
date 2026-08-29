---
titulo: "Shoogle — buscador de componentes e blocos shadcn/ui"
nome: Shoogle
tldr: "Buscador único de componentes e blocos shadcn/ui: varre milhares de páginas de mais de 100 bibliotecas, com preview e código para copiar."
licenca: "própria (serviço web)"
alerta: "o código-fonte é fechado; o repo público é só para feedback, e há um servidor MCP para agentes"
url: https://shoogle.dev/
tipo: ferramenta
categorias: [web, design]
tags: [shadcn, react, componentes, ui, busca, frontend]
status: novo
nota: 4
adicionado: 2026-08-29
fonte: enviado pelo hpcarlos
relacionados: [2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md, 2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md]
---

# Shoogle — buscador de componentes e blocos shadcn/ui

> ⚠️ O site em si (shoogle.dev) está bloqueado pelo proxy desta sessão; o que descreve a
> interface veio de busca externa. Mas o repositório enviado
> ([alibey-10/shoogle](https://github.com/alibey-10/shoogle)) foi lido, e é dele que sai o
> ponto abaixo sobre código fechado e servidor MCP.

## Resumo

Motor de busca dedicado a componentes e blocos no estilo shadcn/ui: em vez de pular entre
os sites de cada biblioteca, você procura num lugar só. O projeto anuncia mais de 10.000
blocos indexados e, além da interface web, expõe um **servidor MCP** — o que permite que um
agente de código consulte e traga o componente certo direto na sessão. A busca web mostra
preview com código para copiar, com tema claro e escuro. Resolve uma dor concreta de quem
usa shadcn: achar o bloco certo (uma tabela, um formulário de login, uma seção de preços)
sem abrir dez documentações. Acesso gratuito em shoogle.dev.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a peça que faltava no lado do **código** de interface. O
[SaaSUI](2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md) mostra
como a tela deveria parecer; o Shoogle entrega o componente pronto para montá-la, na stack
que boa parte dos achados desta coleção usa (React + Tailwind + shadcn).

## Pontos-chave

- **Servidor MCP é o diferencial que importa aqui.** Além de site para humano, ele se
  instala como ferramenta de agente (guia em shoogle.dev/mcp-install): o agente busca o
  bloco shadcn e recebe o código, em vez de inventá-lo. Coloca o Shoogle no mesmo grupo de
  achados que viram capacidade do agente, não só página para abrir.
- **Agrega, não hospeda.** Indexa componentes espalhados por muitos registries e os coloca
  sob a mesma busca — anuncia mais de 10.000 blocos. O ganho é de tempo e de descoberta:
  você encontra bloco de biblioteca que nem sabia que existia.
- **⚠️ O código é fechado.** O repositório público enviado serve só para feedback e issues; a
  aplicação em si é privada, e o autor diz que *pode ou não* ser aberta um dia. Ou seja: é um
  serviço gratuito, não um projeto que você hospeda ou audita. Depender dele é depender de um
  serviço de terceiro que pode mudar de modelo — registre isso antes de embutir no seu fluxo.
- **shadcn/ui é o alvo certo.** É o padrão de componente mais usado no ecossistema
  React/Next hoje, e o mesmo que o
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
  e o gerador de componentes do
  [OpenDesign](2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)
  já assumem. Cai como luva em quem trabalha nessa base.
- **Copia código, não instala pacote** — o modelo shadcn é justamente esse: o componente
  entra no seu projeto como código seu, editável, sem virar dependência. O Shoogle acelera o
  passo de achar; o de adaptar continua com você.
- **Repositório novo e pequeno** (poucas estrelas, pouco mais de uma dezena de commits) —
  é o canal de feedback, não o produto. O produto é o serviço, e a saúde dele não se mede
  pelo repo.
- **⚠️ Licença dos componentes é de cada origem.** O buscador reúne blocos de muitos
  registries, e copiar código herda a licença de quem o publicou, não a do Shoogle. Não há
  aviso sobre isso no repositório — a responsabilidade de checar fica com quem copia.

## Ideias de projeto

- **A esteira completa de interface** — quatro achados agora cobrem o ciclo inteiro:
  [SaaSUI](2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md) para
  ver o padrão, **Shoogle** para achar o componente, o
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md) para
  garantir que o código não re-renderiza à toa e o
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md) para
  tirar a cara de template. Ver → achar → montar → auditar → polir. _Esforço: baixo._
- **Fonte de componente para o agente, via MCP** — plugar o servidor MCP do Shoogle no
  Claude Code e deixar o agente buscar o bloco shadcn sozinho, recebendo o código pronto em
  vez de inventar o componente do zero. É o uso mais direto, e o que aproveita o diferencial
  do projeto. _Esforço: baixo._
- **Montar a vitrine dos achados com blocos prontos** — a ideia antiga da vitrine web
  (`IDEIAS.md`) fica mais barata se a interface for montada com blocos shadcn achados aqui,
  em vez de desenhada do zero. Combina com o gerador do OpenDesign. _Esforço: médio._

## Notas

- Público-alvo: quem já usa shadcn/ui em React/Next e quer achar bloco mais rápido, e
  designers explorando o que o estilo permite.
- **Servidor MCP:** guia de instalação em shoogle.dev/mcp-install — é o caminho para plugar
  no Claude Code e deixar o agente buscar componente sozinho.
- **Repositório de feedback:** <https://github.com/alibey-10/shoogle> — abra issue ali se
  quiser reportar algo; o código da aplicação não está lá.
- Interface descrita como painel dividido: resultados de um lado, preview e código do outro.
- **Ao usar:** o bloco copiado carrega a licença da biblioteca de origem. Para produto,
  confira a licença de cada componente antes de embutir.

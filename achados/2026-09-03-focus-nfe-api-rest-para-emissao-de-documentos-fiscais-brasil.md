---
titulo: "Focus NFe — API REST para emissão de documentos fiscais brasileiros"
nome: Focus NFe
tldr: "API REST que emite NF-e, NFC-e, NFS-e, MDF-e, NFCom e DC-e, com integração ativa em mais de três mil municípios e sem contrato mínimo."
licenca: "própria (SaaS)"
alerta: "serviço pago; preço não apurado nesta sessão, e município novo tem taxa fixa de integração"
url: https://focusnfe.com.br/
tipo: ferramenta
categorias: [negocios, web]
tags: [nota-fiscal, brasil, api, fiscal, saas, integracao]
status: novo
nota: 4
adicionado: 2026-09-03
fonte: enviado pelo hpcarlos
relacionados: [2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md, 2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md]
---

# Focus NFe — API REST para emissão de documentos fiscais brasileiros

> ⚠️ Não consegui acessar o site (o domínio está bloqueado pelo proxy desta sessão). O
> resumo vem de busca externa e das páginas públicas do serviço, não de leitura direta —
> confirme preço e limites ao abrir.

## Resumo

Conjunto de APIs REST para emitir e receber documentos fiscais brasileiros. A cobertura é a
mais ampla dos emissores catalogados: NF-e (venda entre empresas), NFC-e (varejo ao
consumidor), NFS-e (serviço, junto às prefeituras), MDF-e (manifesto de transporte), NFCom
(telecomunicações) e DC-e (declaração de conteúdo). Anuncia integração ativa com mais de
três mil municípios e se compromete a integrar município novo por uma taxa fixa em prazo
determinado. Sem tempo mínimo de contrato.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o terceiro caminho para o mesmo problema, e o que mais cobre documento. Com ele, a
decisão fiscal da coleção deixa de ser binária (SaaS ou biblioteca) e passa a ter opções
reais dentro de cada lado.

## Os três caminhos para emitir nota

| | modelo | cobertura | força |
| --- | --- | --- | --- |
| **Focus NFe** | API REST paga | NF-e, NFC-e, NFS-e, MDF-e, NFCom, DC-e | amplitude de documento e de município |
| [**Spedy**](2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md) | SaaS pago | NF-e, NFS-e, NFC-e | automação a partir das vendas, 70+ integrações |
| [**ACBr**](2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md) | biblioteca LGPL | ampla, inclusive equipamentos | custo zero de licença |

- **Focus e Spedy resolvem problemas diferentes**, apesar de ambos serem API paga: a Spedy
  se vende como automação ponta a ponta (conecta à plataforma de pagamento e emite sozinha);
  o Focus se vende como infraestrutura de emissão — você chama, ele emite. Se o seu sistema
  já sabe quando emitir, o Focus basta; se você quer que alguém descubra isso a partir das
  vendas, a Spedy faz mais.
- **O ACBr continua sendo a saída sem mensalidade**, cobrando em trabalho.

## Pontos-chave

- **A NFS-e é onde a amplitude vale dinheiro.** Cada município tem seu próprio padrão, e é
  aí que qualquer emissor sofre. Integração ativa em milhares de municípios, com compromisso
  de prazo e **taxa fixa** para município novo, é uma resposta concreta ao problema mais
  chato do fiscal brasileiro — e algo que quem usa o
  [ACBr](2026-09-03-projeto-acbr-componentes-livres-de-automacao-comercial-e-fis.md) teria de
  resolver sozinho.
- **Cobertura de documento acima da média:** além do trio comum, cobre MDF-e (relevante para
  quem movimenta carga), NFCom e DC-e. Se o negócio precisar de um desses, a escolha
  praticamente se decide sozinha.
- **Sem contrato mínimo e com cancelamento livre**, segundo o material — reduz o risco de
  experimentar, o que importa quando a alternativa é integrar uma biblioteca por conta própria.
- **⚠️ Preço não apurado.** Há planos com nomes distintos, mas os valores não apareceram na
  busca. Como em toda escolha por volume, o número é o que decide — é a primeira coisa a
  levantar, junto com o da [Spedy](2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md).
- **Mesma dependência estrutural dos outros SaaS fiscais:** a obrigação legal de emitir
  continua sendo sua. Confirme como exportar histórico e o que acontece com as notas se você
  sair — vale para os três serviços pagos catalogados.
- **Nada verificado além do que a busca trouxe** — o site está bloqueado nesta sessão.

## Ideias de projeto

- **A planilha que decide** — três colunas (Focus, Spedy, ACBr), quatro linhas (custo por nota
  no seu volume, documentos de que você precisa, municípios envolvidos, tempo de integração).
  Com os três catalogados, essa comparação é de uma tarde e resolve uma decisão que costuma
  se arrastar. _Esforço: baixo, e é o próximo passo natural._
- **Emissão no micro-SaaS brasileiro** — com o
  [saas-starter-kit](2026-08-22-boxyhq-saas-starter-kit-boilerplate-next-js-para-saas-b2b.md)
  nas contas e o Focus na emissão, o produto fecha o ciclo fiscal com uma chamada REST. É a
  integração mais direta dos três, porque o Focus não presume nada sobre de onde vem a venda.
  _Esforço: médio._
- **Sandbox antes de decidir** — testar a emissão em ambiente de homologação com uma nota
  real do seu caso (produto ou serviço, no seu município) responde mais que qualquer tabela
  comparativa. _Esforço: baixo._

## Notas

- Há documentação de API pública com exemplos em várias linguagens — bom sinal para quem vai
  integrar de um backend Node ou Python.
- **Primeiro passo ao abrir:** a página de preços e a de produtos. Levante o custo por nota,
  se há mínimo mensal, e confirme se o seu município está na lista de integração ativa (ou
  qual o prazo e a taxa se não estiver).
- Quinto achado de infraestrutura brasileira em sequência, e o terceiro emissor fiscal.
  A coleção agora cobre bem esse espaço: dois SaaS com focos diferentes e uma biblioteca livre.

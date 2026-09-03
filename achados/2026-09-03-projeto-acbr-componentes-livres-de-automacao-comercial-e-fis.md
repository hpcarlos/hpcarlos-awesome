---
titulo: "Projeto ACBr — componentes livres de automação comercial e fiscal brasileira"
nome: ACBr
tldr: "Biblioteca livre brasileira para NF-e, NFS-e, SAT, boleto, PIX e impressoras fiscais — a alternativa a pagar por nota emitida."
licenca: "LGPL-2.1+"
alerta: "nativo em Delphi/Lazarus; outras linguagens só via ACBrLib, e emitir por conta própria exige lidar com certificado e SEFAZ"
url: https://www.projetoacbr.com.br/
tipo: biblioteca
categorias: [negocios, engenharia]
tags: [nota-fiscal, brasil, delphi, lazarus, fiscal, automacao-comercial, lgpl]
status: novo
nota: 4
adicionado: 2026-09-03
fonte: enviado pelo hpcarlos
relacionados: [2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md, 2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md]
---

# Projeto ACBr — componentes livres de automação comercial e fiscal brasileira

> ⚠️ Não consegui acessar o site (o domínio está bloqueado pelo proxy desta sessão). O
> resumo vem de busca externa, do código público no GitHub e de material técnico sobre o
> projeto — não de leitura direta da página. Confirme escopo e detalhes ao abrir.

## Resumo

Projeto brasileiro veterano que mantém uma paleta de componentes livres para automação
comercial e obrigações fiscais: emissão de documentos eletrônicos (NF-e, NFS-e e a família
DFe), comunicação com equipamentos (impressoras, balanças, SAT, TEF) e integrações
financeiras (boleto, PIX). Nasceu para Delphi e Lazarus, funcionando em Windows e Linux
**sem depender das DLLs dos fabricantes** — e hoje expõe a mesma capacidade para outras
linguagens através da ACBrLib, uma camada em biblioteca dinâmica. Licença LGPL, com
comunidade e fórum ativos há muitos anos.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o contraponto livre exato da
[Spedy](2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md). Lá o
achado registrava: "se o custo por nota não fechar, o emissor gratuito resolve com mais
trabalho manual". O ACBr **é** esse caminho — e não é gambiarra, é a base sobre a qual boa
parte do software comercial brasileiro foi construída nas últimas duas décadas.

## Spedy × ACBr: a decisão

| | modelo | custo | trabalho seu |
| --- | --- | --- | --- |
| [**Spedy**](2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md) | SaaS com API | por nota emitida | integrar uma API |
| **ACBr** | biblioteca livre (LGPL) | zero de licença | certificado, SEFAZ, layout, atualização de regra |

- **A conta não é só de dinheiro.** O que você economiza em taxa por nota, paga em tempo:
  gestão de certificado digital A1/A3, comunicação com a SEFAZ de cada estado, contingência
  quando o serviço da Receita cai, e acompanhamento das mudanças de layout — que acontecem.
  O ACBr resolve a parte técnica; a operação continua sua.
- **Regra prática:** volume baixo e produto simples → SaaS, porque o custo por nota é menor
  que o seu tempo. Volume alto, ou necessidade de controle total do processo → ACBr.

## Pontos-chave

- **⚠️ O stack nativo é Delphi/Lazarus** — Object Pascal, que não é o mundo de quase nenhum
  outro achado desta coleção. A ponte é a **ACBrLib**: os componentes empacotados como
  DLL/SO, chamáveis de C#, Java, Python, PHP e afins. Se você for usar de um backend Node ou
  Python, é por aí, e vale conferir o esforço dessa camada antes de contar com ela.
- **Licença LGPL** — livre para uso comercial, inclusive em produto fechado, desde que
  alterações na própria biblioteca sejam compartilhadas. Bem mais confortável que AGPL para
  quem constrói software proprietário.
- **Escopo enorme e específico do Brasil:** documentos fiscais, SAT, TEF, impressora fiscal,
  boleto, PIX, e a integração com as particularidades de cada estado e município. Isso é
  conhecimento acumulado que não existe em biblioteca estrangeira nenhuma.
- **Longevidade é o maior ativo.** É um projeto de muitos anos, com fórum ativo e uso
  disseminado no mercado brasileiro. Em obrigação fiscal, que muda de regra com frequência,
  isso vale mais que qualquer recurso: o que importa é alguém acompanhar a mudança.
- **Referência mesmo sem usar.** O código é uma documentação viva de como o fisco brasileiro
  funciona na prática — útil para entender o problema antes de decidir comprar ou construir.
- **Nada verificado além do que a busca e o código público mostraram** — o site está
  bloqueado nesta sessão.

## Ideias de projeto

- **Decidir emissor por aritmética, não por gosto** — pegar o volume mensal estimado de notas
  e comparar o custo da [Spedy](2026-09-03-spedy-emissao-automatica-de-nota-fiscal-para-negocios-digita.md)
  com o tempo estimado de integrar e manter o ACBr. É a mesma conta sugerida no achado da
  Spedy, agora com os dois lados catalogados. _Esforço: baixo, e é o primeiro passo._
- **Serviço de emissão próprio, via ACBrLib** — expor o ACBr como um pequeno serviço HTTP
  interno e chamar dele o backend do seu produto (Node, Python, o que for). Você reconstrói,
  em pequeno, o que a Spedy vende — e fica dono do processo. Faz sentido se houver volume ou
  necessidade de controle. _Esforço: alto._
- **Entender o problema antes de escolher fornecedor** — ler o que o ACBr precisa tratar
  (certificado, contingência, layout por estado) mostra o que qualquer SaaS fiscal está
  abstraindo por você. Faz avaliar preço com critério em vez de comparar tabelas.
  _Esforço: baixo._
- **A infraestrutura brasileira, versão livre** — junto com o que o
  [awesome-selfhosted](2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md)
  oferece de ERP e gestão, dá para montar uma operação inteira sem SaaS. Trocando mensalidade
  por trabalho de manutenção, que é a conta que precisa fechar. _Esforço: alto._

## Notas

- O código está espelhado no GitHub (há vários forks públicos com a árvore completa:
  `Fontes/`, `Pacotes/`, `Exemplos/` e `Projetos/ACBrLib`) — bom ponto de partida para ver o
  escopo real sem instalar nada.
- **ACBrLib** é o caminho para linguagens fora do Object Pascal: os componentes viram
  biblioteca dinâmica com API em C.
- **Primeiro passo ao abrir:** confirmar o estado atual da ACBrLib para a sua linguagem e se
  há suporte ao documento fiscal que você precisa (NF-e, NFS-e do seu município, NFC-e).
- Quarto achado de infraestrutura brasileira em sequência, e o primeiro **livre** do grupo —
  os outros três (Spedy, Polp, Malvo) são serviços pagos.

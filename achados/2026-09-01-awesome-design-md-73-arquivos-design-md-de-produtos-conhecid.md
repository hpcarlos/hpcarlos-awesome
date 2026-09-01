---
titulo: "awesome-design-md — 73 arquivos DESIGN.md de produtos conhecidos"
nome: awesome-design-md
tldr: "Coleção de 73 arquivos DESIGN.md que replicam a linguagem visual de produtos reais — cole um e peça ao agente uma tela com aquela cara."
licenca: "própria (coleção)"
alerta: "replicam a identidade de marcas reais; use a estrutura, não copie a cara de ninguém"
url: https://github.com/VoltAgent/awesome-design-md
tipo: outro
categorias: [design, ia]
tags: [design, design-md, ui, referencia, agentes, frontend]
status: novo
nota: 4
adicionado: 2026-09-01
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md, 2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md]
---

# awesome-design-md — 73 arquivos DESIGN.md de produtos conhecidos

## Resumo

Coleção curada, da VoltAgent, de 73 arquivos `DESIGN.md` — documentos em Markdown que
codificam a linguagem visual de produtos conhecidos (Claude, Linear, Stripe, Vercel,
Mistral e outros), em 10 categorias. A proposta é usar cada um como instrução de estilo
para um agente de código: você copia o `DESIGN.md` para o projeto, pede "uma página com esta
cara", e o resultado sai coerente com aquela identidade. Cada item aponta para o arquivo
correspondente em getdesign.md.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque fecha a peça que faltava na esteira de interface da coleção: o **estilo de partida**.
Já havia como ver o padrão, achar o componente, gerar, auditar e polir — mas a "cara" que o
agente deveria seguir vinha do vácuo. Estes arquivos são essa entrada, prontos e por marca.

## Pontos-chave

- **`DESIGN.md` é o formato que atravessa a coleção.** Aparece como conceito central no
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md) (que
  gera um por entrevista) e no
  [OpenDesign](2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)
  (que traz 151 embutidos). Esta é a terceira fonte, e a mais fácil de garimpar por produto
  específico. Ter as três mostra que "estilo como arquivo versionável" virou padrão de fato.
- **⚠️ A ressalva é de marca, não de licença.** Cada `DESIGN.md` replica a identidade visual
  de uma empresa real. Estudar como o Stripe organiza cor e tipografia é uma coisa; entregar
  um produto seu com a cara do Stripe é problema de marca registrada. Use a **estrutura** do
  documento — quais campos, como descrever tom e paleta —, não a identidade copiada.
- **O valor real é comparativo.** Ler quatro ou cinco lado a lado ensina como marcas
  diferentes codificam a mesma coisa, e isso alimenta o `/impeccable init` a produzir o
  **seu** DESIGN.md — melhor que partir da folha em branco.
- **Curadoria pequena e navegável** (73 itens, contra os 151 do OpenDesign), organizada por
  setor — de plataformas de IA a fintech, e-commerce e até uma seção de web retrô. O tamanho
  modesto é vantagem: dá para varrer inteiro.
- **⚠️ A qualidade de cada arquivo não foi verificada.** O catálogo derivado descreve o
  estilo pela frase que a fonte traz, não por leitura de cada `DESIGN.md`. Trate como índice
  de referências, não como aval.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

As ideias completas estão em **[`IDEIAS-DESIGN-MD.md`](../IDEIAS-DESIGN-MD.md)**. As duas que
valem começar por:

- **Completar a esteira de interface** — o `DESIGN.md` é o estilo de partida entre ver
  ([SaaSUI](2026-08-29-saasui-biblioteca-de-padroes-de-interface-de-produtos-saas-r.md)) e
  gerar ([OpenDesign](2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md)).
  Escolher um, copiar para o projeto, mandar gerar a primeira tela seguindo-o. _Esforço:
  baixo._
- **Escrever o DESIGN.md da própria vitrine** — a vitrine web da coleção precisa de
  identidade; inspirar-se nestes arquivos para produzir um próprio, sóbrio e editorial, e
  usá-lo como entrada única para gerar todas as páginas com coerência. _Esforço: médio._

## Notas

- Catálogo completo, com títulos de categoria em português:
  [`DESIGN-MD.md`](../DESIGN-MD.md), gerado por `scripts/indexar_design_md.py` a partir de
  `dados/design-md.tsv`.
- As descrições de estilo de cada item continuam em inglês, como na fonte — são frases
  curtas ("Warm terracotta accent, clean editorial layout"), não valeu traduzir uma a uma.
- A importação é reprodutível: `scripts/importar_design_md.py` lê o Markdown de origem.
- **Antes de usar em produto:** a estrutura do DESIGN.md é reaproveitável; a identidade de
  uma marca específica não. Gere a sua a partir do padrão, não do clone.

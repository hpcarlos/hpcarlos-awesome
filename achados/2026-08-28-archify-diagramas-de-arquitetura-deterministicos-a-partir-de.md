---
titulo: "archify — diagramas de arquitetura determinísticos a partir de JSON"
nome: archify
tldr: "Skill que transforma JSON tipado em diagrama de arquitetura, fluxo, sequência ou ciclo de vida, com layout determinístico e saída num arquivo só."
licenca: "MIT"
alerta: "sem auto-layout, editor visual ou import de Mermaid — o agente precisa escrever o JSON tipado"
url: https://github.com/tt-a1i/archify
tipo: ferramenta
categorias: [engenharia, design]
tags: [diagramas, arquitetura, documentacao, claude-code, skills, nodejs, mcp]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md, 2026-08-28-opendesign-gerador-de-artefatos-de-design-dirigido-por-agent.md]
---

# archify — diagramas de arquitetura determinísticos a partir de JSON

## Resumo

Skill de agente que recebe um JSON tipado e devolve diagrama interativo em HTML/SVG, em
cinco formatos: arquitetura de componentes, fluxo de trabalho, sequência de chamadas,
fluxo de dados e ciclo de vida de estado. O layout é **determinístico** — mesmo JSON, mesmo
desenho, sem o resultado embaralhado a cada geração que caracteriza auto-layout genérico.
A saída é um arquivo HTML autossuficiente, com busca, rastreio de rota, alcance a montante
e a jusante, temas, modo apresentação e URLs estáveis para focar num nó. Exporta também
PNG, WebM e card social. Node.js, MIT, instala como skill em Cursor, Claude Code, Codex e
outros.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a peça que faltava entre entender e mostrar. O
[graphify](2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)
extrai a estrutura real do código; este desenha algo que uma pessoa consegue ler numa
reunião. Um é análise, o outro é comunicação — e a segunda é onde a maioria dos projetos
falha.

## Pontos-chave

- **Determinístico por escolha, e isso é o diferencial.** O projeto rejeita explicitamente
  auto-layout genérico: o desenho é estável entre execuções, o que torna o diagrama
  versionável em git e comparável entre commits. Diagrama que muda sozinho a cada geração
  não serve para acompanhar evolução.
- **Não usa LLM por dentro.** A divisão é limpa: o agente escreve o JSON, o archify valida
  e renderiza. Mais uma entrada no padrão determinístico que já domina a coleção — detecção
  e renderização por código, modelo só na parte interpretativa.
- **⚠️ O que ele não faz, e está declarado:** não importa Mermaid, não tem auto-layout, não
  tem editor visual e não hospeda nada. Se a expectativa era colar um diagrama pronto e ver
  o resultado, não é aqui.
- **Validação com recibo de falha em JSON** — quando o desenho não sai, ele diz o que
  faltou de forma estruturada, o que permite o agente corrigir sozinho em vez de tentar de
  novo às cegas.
- **Comparação antes/depois** entre duas versões da arquitetura é o recurso mais original:
  mostra o que mudou na estrutura, não só o estado atual.
- **Um arquivo HTML como entrega** resolve o problema chato de compartilhar diagrama: sem
  servidor, sem link que expira, sem conta em serviço.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Pipeline de documentação de arquitetura** — o
  [graphify](2026-08-28-graphify-transforma-um-repositorio-em-grafo-de-conhecimento.md)
  extrai o grafo do código com AST, o agente converte o recorte relevante no JSON do
  archify, e sai um diagrama versionado. Com o gancho de git do graphify, isso se atualiza
  sozinho a cada commit. É a documentação que ninguém mantém, mantida por construção.
  _Esforço: médio._
- **Diagramar as bases antes de escolher** — junto com a auditoria já planejada no
  `IDEIAS.md`: o react-doctor diz se a base é sadia, o graphify mostra a estrutura e o
  archify transforma isso em algo que dá para comparar lado a lado. _Esforço: baixo._
- **Desenhar o fluxo deste repositório** — `INBOX.md` → `novo.py` → achado → `indexar.py` →
  `README.md` é um diagrama de fluxo de trabalho de cinco nós, e serve de teste honesto da
  ferramenta em algo que você conhece bem. Se o resultado ficar bom, entra no próprio
  README. _Esforço: baixo._
- **Cards para compartilhar** — a exportação em 1200×630 é feita para post e apresentação.
  Se você publicar algo sobre os projetos que construir a partir desta coleção, o diagrama
  já sai pronto para acompanhar o texto. _Esforço: baixo._

## Notas

```bash
npx skills add tt-a1i/archify -g                       # instala a skill globalmente
npx skills use tt-a1i/archify@archify --agent codex    # uso pontual

# direto no repositório
node bin/archify.mjs doctor
node bin/archify.mjs validate workflow exemplo.json --quality showcase --json
node bin/archify.mjs preview workflow exemplo.json /tmp/saida.html --quality showcase
node bin/archify.mjs deliver workflow exemplo.json /tmp/saida.html --open --json
```

- O uso natural é conversacional: "usa o archify para desenhar isto" dentro do agente.
- `doctor` confere o ambiente antes de gerar — bom primeiro comando quando algo falha.
- Os URLs estáveis (`#focus`, `#route`, `#lens`) permitem mandar para alguém um link já
  apontando para o pedaço do diagrama que interessa.

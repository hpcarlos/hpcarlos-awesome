---
titulo: "mattpocock/skills — skills de engenharia para agentes de código"
nome: mattpocock/skills
tldr: "Coleção de skills pequenas e componíveis que dão método de engenharia ao agente: triagem, spec, TDD, diagnóstico de bug e code review."
url: https://github.com/mattpocock/skills
tipo: ferramenta
categorias: [ia, engenharia]
tags: [claude-code, skills, agentes, workflow, tdd, code-review]
status: novo
nota: 5
adicionado: 2026-08-22
fonte: enviado pelo hpcarlos
relacionados: [2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md, 2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md]
---

# mattpocock/skills — skills de engenharia para agentes de código

## Resumo

Coleção de skills que o Matt Pocock usa no dia a dia para fazer engenharia de verdade com
agente — a definição dele, no README, é "não vibe coding". São dezenas de skills
pequenas e independentes que cobrem o ciclo inteiro: `triage` para classificar issues,
`to-spec` e `to-tickets` para transformar conversa em trabalho definido, `implement`,
`tdd`, `diagnosing-bugs` (um laço disciplinado de diagnóstico), `code-review`,
`resolving-merge-conflicts` e `improve-codebase-architecture`. Há também um bloco de
produtividade, com destaque para as skills de *grilling*: entrevistas insistentes que
furam plano mal pensado antes de virar código. Licença MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é a peça que falta nos outros achados do repositório: o
[impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
cuida de como a interface fica, e este aqui cuida de como o trabalho é conduzido — do
issue mal escrito até o code review. Como você usa Claude Code, é o achado de retorno
mais imediato da coleção até agora.

## Pontos-chave

- **A tese do projeto é o oposto da dos frameworks grandes.** O README critica
  explicitamente GSD, BMAD e Spec-Kit por tirarem o controle do desenvolvedor, e aposta
  em skills pequenas, componíveis e feitas para você editar. Isso importa na prática: o
  custo de adotar é baixo e o de abandonar também.
- **Duas famílias de skill:** as *user-invoked*, que você chama (`/triage`, `/to-spec`,
  `/grill-me`), e as *model-invoked*, que o agente aciona sozinho quando reconhece a
  situação (`tdd`, `diagnosing-bugs`, `research`).
- **Precisa de uma configuração por repositório:** rodar `/setup-matt-pocock-skills` uma
  vez para dizer onde ficam as issues (GitHub, Linear ou arquivos locais), que rótulos de
  triagem usar e onde vive a documentação.
- **Não é exclusivo do Claude Code** — instala em Codex e outros agentes via `npx skills`,
  ainda que o caminho mais liso seja o marketplace de plugins.
- **Fundamentação declarada:** o README cita *The Pragmatic Programmer* e
  Domain-Driven Design. É opinativo por escolha, não por acidente — se você discorda do
  método, as skills vão atritar.
- **Números não verificados:** a leitura devolveu uma contagem de estrelas
  implausivelmente alta (na casa das centenas de milhares, o que colocaria o projeto entre
  os maiores do GitHub). Quase certamente é erro de leitura, e a API do GitHub está
  bloqueada nesta sessão. Ignore o número; avalie pelo conteúdo.

## Ideias de projeto

- **Adotar `triage` + `to-spec` neste repositório de achados** — as ideias do
  `IDEIAS.md` são hoje texto solto; passá-las por `to-spec` e `to-tickets` as transforma
  em trabalho executável, e o `wayfinder` ajuda a escolher por onde começar. É usar a
  ferramenta na primeira coisa que estiver à mão. _Esforço: baixo._
- **Um `grill-me` antes de cada achado virar projeto** — a skill de entrevista serve
  exatamente para furar plano bonito. Rodar sobre as ideias do `IDEIAS.md` deve matar
  metade delas, o que é o resultado desejado. _Esforço: baixo._
- **Sua própria coleção de skills, no formato dele** — ler `writing-for-agents` e
  `wizard` para entender a estrutura, e escrever skills para as tarefas que você repete
  (organizar achados, revisar PR de um jeito específico, publicar). O repositório vira
  ponto de partida em vez de dependência. _Esforço: médio._
- **Bake-off contra o [addyosmani/agent-skills](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)** — as duas coleções resolvem o
  mesmo problema por filosofias opostas: aqui, peças pequenas que você compõe; lá, um
  sistema de 24 skills com portões de verificação. Rodar a mesma tarefa nas duas e
  anotar tempo, retrabalho e custo responde a pergunta de uma vez. _Esforço: médio._
- **Combinar com o [munder-difflin](2026-08-22-munder-difflin-escritorio-de-agentes-de-ia-num-app-de-deskto.md)**
  — se a ideia for orquestrar vários agentes, vale dar a eles um método comum em vez de
  cada um improvisar. As skills são o método; o outro projeto é o palco. _Esforço: médio._

## Notas

```bash
# Claude Code (caminho mais curto)
claude plugins install mattpocock-skills
# ou, dentro da sessão:
/plugin install mattpocock-skills

# outros agentes, ou para editar os arquivos à mão
npx skills@latest add mattpocock/skills
npx skills update

# uma vez por repositório
/setup-matt-pocock-skills
```

- `ask-matt` funciona como roteador: quando não souber qual skill serve, comece por ela.
- As skills de *grilling* (`grill-me`, `grill-with-docs`, `grilling`) são a parte mais
  original da coleção — vale ler o texto delas mesmo sem instalar nada.
- Como são arquivos Markdown, dá para ler o conteúdo direto no GitHub antes de decidir.

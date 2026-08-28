---
titulo: "ponytail — skill que faz o agente escrever menos código"
nome: ponytail
tldr: "Skill sempre ativa que obriga o agente a percorrer uma escada de decisão antes de escrever código, cortando solução inflada."
licenca: "MIT"
alerta: "os ganhos anunciados vêm de benchmark do próprio projeto; o efeito é quase nulo onde o código já é enxuto"
url: https://github.com/DietrichGebert/ponytail
tipo: ferramenta
categorias: [ia, engenharia]
tags: [claude-code, skills, agentes, yagni, custos, nodejs]
status: novo
nota: 4
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md]
---

# ponytail — skill que faz o agente escrever menos código

## Resumo

Skill que instala um sistema de valores no agente em vez de um processo: antes de escrever
qualquer coisa, ele precisa descer uma escada de decisão — este código precisa existir? já
existe algo assim na base? a biblioteca padrão resolve? é recurso nativo da plataforma? uma
dependência já instalada dá conta? cabe em uma linha? Só depois vem a solução mínima. Fica
sempre ativa, com intensidade regulável (`lite`, `full`, `ultra`, `off`), e traz comandos
para auditar diff, varrer o repositório inteiro, listar atalhos adiados e mostrar o impacto
acumulado. MIT, instalável em mais de vinte agentes diferentes.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque ataca o defeito mais caro de programar com agente: ele quase nunca escreve de menos.
Cada abstração desnecessária vira código para manter, revisar e pagar em token — e é o tipo
de excesso que passa em revisão porque parece competente.

## Pontos-chave

- **É comportamento, não processo.** As duas coleções de skills que você já tem —
  [mattpocock](2026-08-22-mattpocock-skills-skills-de-engenharia-para-agentes-de-codig.md)
  e [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md)
  — organizam *como o trabalho anda*. Esta decide *quanto código sai*. São ortogonais:
  instalar o ponytail junto de uma delas não é escolher entre as duas.
- **⚠️ Os números são do próprio projeto.** Cerca de 54% menos código, 20% mais barato e
  27% mais rápido em doze tarefas, contra uma linha de base sem a skill. A metodologia está
  publicada e datada, o que é mais do que a maioria oferece — mas continua sendo o autor
  medindo a si mesmo. Vale reproduzir antes de repetir o número.
- **⚠️ Honestidade sobre o limite:** o próprio projeto diz que o ganho é grande onde há
  armadilha de excesso (cita 94% de redução num seletor de data) e **próximo de zero onde o
  código já é minimalista**. Também admite que modelos que raciocinam muito podem gastar
  mais token deliberando — o ganho em código pode virar custo em pensamento.
- **Sobreposição a mapear:** as skills do Addy já trazem `code-simplification`. Aqui a
  diferença é ser sempre ativa e anterior à escrita, em vez de uma limpeza depois. Vale
  testar se somam ou se atritam.
- **`/ponytail-debt` é o comando mais interessante:** junta os atalhos que foram adiados
  conscientemente, transformando "depois eu arrumo" em lista, não em esquecimento.
- **Funciona sem plugin**, copiando o arquivo de regras para `.cursor/rules/`,
  `.clinerules/`, `.github/copilot-instructions.md` e afins — o que o torna aproveitável
  mesmo em ferramenta sem marketplace.
- **Números de adoção não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **A medição própria que a coleção ainda não tem** — a metodologia do benchmark está
  publicada. Escolher duas tarefas suas de verdade, rodar com e sem a skill, e anotar
  linhas de código, tokens e tempo. Você passa a ter um número seu em vez de repetir o de
  alguém, e isso vira achado deste repositório. _Esforço: médio._
- **Combinar com a rede de segurança** — o ponytail reduz o que é escrito; o
  [react-doctor](2026-08-28-react-doctor-auditoria-deterministica-de-codigo-react.md) e o
  [impeccable](2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md)
  pegam o que passou. Menos código gerado significa menos achado para revisar depois — dá
  para medir esse efeito em cascata. _Esforço: baixo._
- **`/ponytail-audit` nos scripts deste repositório** — `indexar.py`, `buscar.py` e
  `lib_achados.py` foram escritos por agente e nunca passaram por uma revisão de excesso.
  É a menor tarefa possível para testar a ferramenta em código que você conhece.
  _Esforço: baixo._
- **Reduzir custo antes de rotear** — o [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
  baixa o preço por token; este baixa a quantidade de token. As duas alavancas se
  multiplicam, e esta é a mais barata de acionar. _Esforço: baixo._

## Notas

```
# Claude Code
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail

# comandos
/ponytail [lite|full|ultra|off]   # intensidade
/ponytail-review                  # audita o diff atual
/ponytail-audit                   # varre o repositório
/ponytail-debt                    # atalhos adiados
/ponytail-gain                    # impacto acumulado
```

- Também instala em Codex, Copilot CLI e OpenCode (`@dietrichgebert/ponytail` no npm);
  nos demais, é copiar o arquivo de regras.
- Precisa de Node no `PATH` para os ganchos de ciclo de vida.
- O projeto cita o Caveman como complementar: aquele reduz a prosa do agente, este reduz o
  código. Vale saber que existem os dois eixos.
- **Sugestão de uso:** começar em `lite` num projeto real por uma semana antes de subir
  para `full`. Skill sempre ativa que discorda de você o tempo todo cansa rápido se a
  intensidade estiver errada.

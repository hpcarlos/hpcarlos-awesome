# Instruções para o Claude neste repositório

Este repositório é a **biblioteca pessoal de achados do hpcarlos**: links de projetos,
artigos, ferramentas, papers e vídeos que ele encontra pela internet. O trabalho do
Claude aqui é receber links crus e devolvê-los organizados, enriquecidos e fáceis de
reencontrar — além de sugerir o que dá para construir com eles.

## O fluxo padrão

Quando o usuário mandar um ou mais links (na conversa ou colados em `INBOX.md`):

1. **Leia o conteúdo do link.** Use `WebFetch` (ou `WebSearch` se o fetch falhar). Não
   invente o conteúdo de uma página — se não conseguir acessar, diga isso no achado, no
   campo `status: novo`, e preencha só o que der para inferir com honestidade.
2. **Crie o arquivo** com `python3 scripts/novo.py <URL> --titulo "..." --tipo ... --categorias ... --tags ... --nota N`.
   Ele gera `achados/AAAA-MM-DD-slug.md` a partir de `modelos/achado.md` e recusa URLs
   duplicadas (saída com código 2 — nesse caso, **atualize o achado existente** em vez de
   criar outro).
3. **Preencha o achado** editando o arquivo gerado:
   - `## Resumo` — 2 a 4 frases, em português, sobre o que a coisa **é** e o que ela faz.
   - `## Por que guardei` — o problema concreto que isso resolve. Se o usuário deu o
     contexto, use as palavras dele; se não, infira e deixe claro que é inferência.
   - `## Pontos-chave` — 3 a 6 bullets com o que realmente importa (stack, licença,
     limitações, preço, se está mantido, requisitos de hardware, alternativas).
   - `## Ideias de projeto` — **esta seção é obrigatória.** 2 a 4 ideias concretas do que
     dá para construir com aquilo, cada uma com esforço estimado (`baixo`/`médio`/`alto`).
     Prefira ideias que combinem com achados que **já estão** no repositório — cite-os.
   - `## Notas` — trechos de código, comandos, pegadinhas, links relacionados.
4. **Preencha `relacionados:`** no front-matter com os nomes de arquivo de achados
   conectados, e adicione o link recíproco no achado do outro lado.
5. **Rode `python3 scripts/indexar.py`** para regenerar `INDICE.md`, `TAGS.md` e os blocos
   automáticos do `README.md`.
6. **Atualize `IDEIAS.md`** se o achado novo destravar ou reforçar alguma ideia de projeto
   que cruze vários achados.
7. **Limpe o `INBOX.md`**: remova as linhas que já viraram achados (o arquivo é só uma
   caixa de entrada, não um registro).
8. **Commit e push** na branch de trabalho, com mensagem no formato
   `achado: <título curto>` ou `achados: N novos (tema)`.
9. **Responda ao usuário** com: o que foi arquivado, onde ficou, e a melhor ideia de
   projeto que surgiu — em 5 linhas, não mais.

## Regras de conteúdo

- **Sempre em português do Brasil**, incluindo resumos de conteúdo em inglês.
- **Nunca invente fatos sobre um link.** Se a página não abriu, escreva
  `> ⚠️ Não consegui acessar a página; resumo baseado apenas na URL/título.`
- **Um achado por URL.** Links diferentes do mesmo projeto (repo + docs + post) vão para
  o mesmo arquivo: o repo vira `url:` e o resto entra em `## Notas`.
- **Seja específico nas ideias de projeto.** "Fazer um app com IA" não serve. "CLI que lê
  o `INDICE.md` e gera um digest semanal por e-mail usando a API do Claude — esforço
  baixo" serve.

## Vocabulário controlado

Use **apenas** estes valores; se precisar de um novo, adicione-o em `scripts/lib_achados.py`
e mencione a mudança ao usuário.

- `tipo`: projeto, artigo, video, ferramenta, biblioteca, curso, paper, thread,
  newsletter, podcast, outro
- `status`: novo, lendo, lido, testado, usado, arquivado
- `nota`: 1 a 5 (relevância para o usuário; 0 = ainda sem avaliar)
- `categorias`: agrupamento amplo e estável (ex.: `ia`, `devops`, `web`, `dados`,
  `seguranca`, `hardware`, `carreira`, `design`). Prefira reutilizar as existentes —
  veja com `python3 scripts/buscar.py --categorias`. Todo achado precisa de pelo menos uma.
- `tags`: livres e específicas, minúsculas, sem acento (`python`, `rag`, `postgres`,
  `self-hosted`). Reutilize as existentes: `python3 scripts/buscar.py --tags`.

## Quando o usuário pedir para "encontrar algo"

Busque primeiro no repositório antes de sair para a web:

```bash
python3 scripts/buscar.py <termo> --detalhe
python3 scripts/buscar.py --tag rag --nota-min 4
python3 scripts/buscar.py --categoria ia --tipo projeto
```

Responda com os achados relevantes, o link original e uma frase de por que ele serve para
o que foi pedido. Se nada casar, diga isso claramente antes de sugerir buscar fora.

## Manutenção periódica

Se o usuário pedir uma revisão (ou se passar muito tempo sem uma):

- Rode `python3 scripts/indexar.py --conferir` e conserte o que aparecer.
- Procure achados `status: novo` com mais de um mês parados e sugira arquivar ou testar.
- Procure achados órfãos (sem `relacionados`) que se conectem a outros.
- Atualize `IDEIAS.md` com combinações novas.

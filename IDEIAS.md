# 💡 Ideias de projeto

Projetos que dá para construir **cruzando** os achados deste repositório. Cada achado tem
sua própria seção "Ideias de projeto"; aqui ficam as ideias que combinam dois ou mais.

Formato de cada ideia: o que é, quais achados alimentam, esforço estimado e o primeiro
passo concreto.

<!-- O Claude atualiza este arquivo sempre que um achado novo destrava ou reforça uma ideia. -->

## Em aberto

### Vitrine web dos achados

Site estático gerado a partir do front-matter de `achados/`: cartões por categoria,
filtro por tag e por nota, busca no cliente. A parte de dados é trivial — os scripts já
leem tudo. O que costuma sair feio é a interface, e é aí que entra o
[impeccable](achados/2026-08-21-impeccable-design-language-e-skill-para-agentes-de-codigo.md):
`shape` para planejar, `craft` para construir, `audit` e `polish` para tirar a cara de
template. Publicável no GitHub Pages.

- **Alimenta:** impeccable
- **Esforço:** médio
- **Primeiro passo:** `scripts/exportar.py` que despeja todos os achados num `dados.json`
  (o `lib_achados.py` já entrega os objetos prontos) — o site consome isso.
- **Bônus:** é um projeto frontend real para testar o impeccable de verdade, em vez de
  avaliar a ferramenta por captura de tela.

### Digest do que entrou

CLI que lê os achados adicionados na última semana e monta um resumo — por e-mail, ou
como issue no próprio repositório. Reaproveita `scripts/buscar.py --desde`, que já
filtra por data. Vale mais quando houver volume; fica anotado para depois.

- **Alimenta:** (nenhum achado específico ainda)
- **Esforço:** baixo
- **Primeiro passo:** `python3 scripts/buscar.py --desde $(date -d '7 days ago' +%F)`

## Em andamento

_(mova para cá quando começar a construir)_

## Feitas ou descartadas

_(com uma linha dizendo o que aconteceu — descartar com motivo também é resultado)_

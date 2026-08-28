---
titulo: "claude-ads — operação de mídia paga como plugin de agente"
nome: claude-ads
tldr: "Plugin de agente para operar mídia paga em 12 plataformas: auditoria com evidência datada, plano, criação, monitoramento e relatório."
licenca: "MIT"
alerta: "não é produto oficial da Anthropic; opera contas de anúncios reais quando a escrita é liberada"
url: https://github.com/AgriciDaniel/claude-ads
tipo: ferramenta
categorias: [ia, negocios]
tags: [claude-code, skills, marketing, anuncios, python, automacao]
status: novo
nota: 3
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md]
---

# claude-ads — operação de mídia paga como plugin de agente

## Resumo

Plugin que ensina o agente a operar mídia paga do jeito que uma agência opera: audita a
conta e apresenta achados com **evidência datada e nível de confiança explícito**, monta
plano de canal e orçamento, gera briefing de texto, imagem e vídeo, acompanha ritmo de
entrega e rastreamento, e fecha relatório em JSON, Markdown, HTML ou PDF. Cobre doze
plataformas — Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Reddit, Snapchat, X,
Apple, Amazon e Pinterest. Python 3.11/3.12, licença MIT, instalável pelo marketplace de
plugins do Claude Code ou por script, e também compatível com Codex, Gemini, Cursor e
Windsurf.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o segundo achado seguido em que um agente encosta em dinheiro real, e o segundo
que resolve isso com contenção em vez de confiança. Se você atende cliente ou roda campanha
própria, o ganho é direto; se não, ele ainda vale como estudo de um agente que precisa
provar o que afirma.

## Pontos-chave

- **⚠️ Não é produto da Anthropic.** Usa "Claude" no nome porque é otimizado para o Claude
  Code, mas está no espaço pessoal de um mantenedor independente e não vi declaração de
  afiliação oficial. Não trate como software chancelado por ninguém.
- **⚠️ Ele lê e, quando autorizado, escreve em contas de anúncios reais.** O padrão é
  somente leitura, mudanças saem como rascunho (`/ads launch --draft`) e a escrita exige
  passar por várias travas — mas a partir do momento em que você entrega credencial de
  Google Ads ou Meta Ads, há orçamento de verdade do outro lado.
- **A ideia mais valiosa está no rigor da evidência:** cada achado vem com data e grau de
  confiança, e a auditoria calcula a própria **cobertura de evidência** — abaixo de 60%,
  ela se declara insuficiente em vez de fingir conclusão. Isso é o oposto do relatório de
  agente que soa convincente e não se sustenta.
- **Mesmo padrão de contenção do
  [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md):**
  leitura por padrão, escrita atrás de aprovação, idempotência e verificação. Dois projetos
  de domínios completamente diferentes chegando ao mesmo desenho é um sinal forte de que
  esse é *o* jeito de deixar agente agir.
- **Antes de usar em conta de cliente:** confira os termos de uso da API de cada
  plataforma. Automatizar operação costuma ser permitido, mas há regras sobre limite de
  chamada, uso de dado e atribuição que variam entre elas.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Copiar o conceito de cobertura de evidência** — fazer o agente declarar quanto do que
  ele precisava olhar ele realmente olhou, e recusar conclusão abaixo de um limiar, resolve
  o problema mais comum de relatório gerado por IA. Vale em auditoria de código, revisão de
  contrato ou qualquer análise. Combina com as skills do
  [addyosmani](2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md),
  cuja regra é "verificação inegociável". _Esforço: médio._
- **Auditoria de conta própria, sem escrita** — rodar `/ads audit` com credencial somente
  de leitura numa campanha sua e comparar o que ele acha com o que você já sabe. É o teste
  barato que diz se a ferramenta entende do assunto. _Esforço: baixo._
- **Serviço de diagnóstico para pequeno negócio** — auditoria mais relatório em PDF é um
  produto vendável por si só, sem tocar na conta do cliente. Casa com o
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md) para quem atende comércio
  local: um cuida do atendimento, o outro da mídia. _Esforço: médio._
- **Ler o modelo de gates como referência** — aprovação, idempotência e verificação em
  cascata é um padrão reaproveitável para qualquer integração que escreva em sistema de
  terceiro, de ERP a CMS. _Esforço: baixo._

## Notas

```bash
# dentro do Claude Code
/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@ai-marketing-hub-claude-ads

# instalação local
git clone https://github.com/AgriciDaniel/claude-ads.git
cd claude-ads && bash install.sh --source=local

# comandos
/ads setup      /ads audit [all|plataforma|escopo]      /ads plan
/ads create     /ads launch --draft                     /ads monitor    /ads report
```

- Credenciais em variáveis de ambiente ou no chaveiro do sistema.
- Usa Playwright para captura de tela e WeasyPrint/Pango para gerar PDF — dependências
  pesadas, vale conferir antes de instalar em máquina apertada.
- Documentação separada por host (`CLAUDE.md`, `CODEX.md`, `GEMINI.md`), o que ajuda quem
  não usa Claude Code.

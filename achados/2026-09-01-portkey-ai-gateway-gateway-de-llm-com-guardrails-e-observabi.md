---
titulo: "Portkey AI Gateway — gateway de LLM com guardrails e observabilidade"
nome: Portkey Gateway
tldr: "Gateway de LLM enxuto e testado em produção: um endpoint para 45+ provedores, com fallback, load balancing, cache e mais de 50 guardrails."
licenca: "MIT"
alerta: "open core: cache semântico, otimização de provedor e templates ficam na versão paga"
url: https://github.com/portkey-ai/gateway
tipo: ferramenta
categorias: [ia, devops]
tags: [gateway, llm, openai-api, guardrails, observabilidade, self-hosted]
status: novo
nota: 4
adicionado: 2026-09-01
fonte: enviado pelo hpcarlos
relacionados: [2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md, 2026-08-21-omniroute-gateway-de-ia-com-um-endpoint-para-centenas-de-pro.md, 2026-08-22-sub2api-gateway-que-distribui-quotas-de-assinaturas-de-ia.md]
---

# Portkey AI Gateway — gateway de LLM com guardrails e observabilidade

## Resumo

Gateway de IA da Portkey que expõe um endpoint único para mais de 45 provedores (e, segundo
eles, 1.600+ modelos), com o pacote de confiabilidade que se espera da categoria — fallback
automático, retry com backoff, load balancing por peso entre chaves — e um diferencial: mais
de 50 *guardrails* prontos que validam entrada e saída, além de observabilidade centralizada.
O código é enxuto (o README fala em 122 kb de footprint e menos de 1 ms de latência
adicionada) e roda em Docker, Node, Kubernetes ou Cloudflare Workers. TypeScript, licença
MIT no núcleo, com nuvem e edição enterprise pagas por cima.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Porque é o quarto gateway da coleção, e o segundo que dá para adotar sem ressalva jurídica —
o que muda a disputa. Onde o [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md)
brilha em governança e velocidade, este traz os *guardrails* como peça de primeira classe, o
que interessa a quem coloca LLM na frente de usuário e precisa filtrar o que entra e sai.

## Onde ele entra na disputa de gateways

Agora são quatro. A tabela do achado do bifrost ganha uma linha:

| | licença | de onde vem o acesso | diferencial | quando escolher |
| --- | --- | --- | --- | --- |
| **bifrost** | Apache-2.0 | suas chaves | Go, governança, Prometheus | produto sério, foco em custo e velocidade |
| **Portkey** | MIT (open core) | suas chaves | 50+ guardrails, multimodal | produto com LLM na frente de usuário |
| **OmniRoute** | MIT | tiers gratuitos | fallback entre gratuitos | experimento pessoal |
| **sub2api** | LGPL-3.0 | assinaturas alheias | — | nenhum: só leitura |

- **bifrost vs Portkey** é a escolha real hoje: os dois são permissivos e rodam sobre suas
  chaves. Portkey ganha em guardrails e maturidade de mercado (SOC2, HIPAA, uso em escala);
  bifrost ganha em ser inteiramente aberto e em não empurrar para a nuvem paga. Medir os dois
  com o seu tráfego é a única forma honesta de decidir.

## Pontos-chave

- **Guardrails são o argumento.** Mais de 50 validações prontas de entrada e saída — o pedaço
  que falta na maioria dos gateways e que vira obrigatório quando há usuário do outro lado
  (filtrar PII, bloquear conteúdo, validar formato). É o que o justifica sobre o bifrost em
  produto voltado ao público.
- **⚠️ Modelo open core, e a linha de corte importa:** o próprio README diz que cache
  semântico, otimização de provedor e gestão de templates de prompt ficam nas versões
  hospedada e enterprise. O núcleo MIT é forte, mas os recursos que mais reduzem custo estão
  do lado pago. Saber disso antes evita a surpresa de "o que eu quero é o que se paga".
- **Enxuto e testado em produção:** 122 kb, menos de 1 ms de sobrecarga, e a alegação de
  bilhões de tokens por dia. Como sempre com número de README, é do fabricante — mas o
  footprint pequeno é verificável e conta a favor de embutir o gateway na própria aplicação.
- **Multimodal de fábrica** (visão, áudio, geração de imagem), o que nem todo gateway cobre e
  passa a importar conforme os modelos deixam de ser só texto.
- **Roda em Cloudflare Workers**, além de Docker e Node — útil para quem quer o gateway na
  borda, perto do usuário, sem servidor dedicado.
- **⚠️ A conta é sua.** Como bifrost e OmniRoute, ele roteia; o custo dos tokens continua no
  seu provedor. Vale o mesmo teto de gasto e a mesma medição de sempre.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Bake-off de gateway com o seu tráfego** — subir Portkey e
  [bifrost](2026-08-27-bifrost-gateway-de-ia-em-go-com-governanca-e-observabilidade.md) lado a
  lado, apontar uma aplicação real para cada um por uma semana e comparar latência, esforço de
  operação e o que cada um cobra para liberar o recurso que você precisa. É a decisão de
  infraestrutura mais reutilizável da coleção, e ela tem que ser sua. _Esforço: médio._
- **Guardrail na frente do que vai a usuário** — se qualquer produto seu (o
  [wacrm](2026-08-22-wacrm-crm-auto-hospedavel-para-whatsapp.md), um bot de atendimento)
  expõe LLM ao público, os guardrails do Portkey filtram PII e conteúdo impróprio sem você
  escrever a validação. É o caso de uso que o distingue. _Esforço: médio._
- **Gateway na borda com Cloudflare Workers** — rodar o Portkey como Worker coloca o
  roteamento perto do usuário e dispensa servidor. Combina com aplicação já hospedada na
  Cloudflare. _Esforço: médio._
- **Fechar a conta, de novo** — as métricas dele somam à ideia recorrente de painel de custo
  de agentes (`IDEIAS.md`), agora com um quarto candidato a fonte de dado. A pergunta segue
  sendo qual gateway fica, não quantos. _Esforço: médio._

## Notas

```bash
# sobe em segundos
npx @portkey-ai/gateway
# Gateway em http://localhost:8787/v1 e console em http://localhost:8787/public/
```

- Deploy também por Docker, Kubernetes, Cloudflare Workers e Replit; enterprise em AWS,
  Azure e GCP.
- Versão 2.0 em pré-lançamento no branch `2.0.0` — vale conferir o que muda antes de fixar em
  produção.
- **Antes de adotar:** listar quais recursos você realmente vai usar e checar quais estão no
  núcleo MIT e quais exigem a nuvem paga. Em open core, essa é a pergunta que decide.
- Certificações citadas (SOC2, HIPAA, GDPR, CCPA) valem para quem precisa de conformidade —
  raro num projeto aberto, e um argumento real em ambiente regulado.

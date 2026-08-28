---
titulo: "red-team — skill de planejamento de simulação adversarial (MITRE ATT&CK)"
nome: red-team
tldr: "Skill que monta plano de red team a partir de técnicas MITRE ATT&CK, pontuando esforço e risco de detecção — só com autorização assinada."
licenca: "MIT"
alerta: "uso sem autorização escrita é crime (CFAA e equivalentes); a ferramenta exige a flag --authorized"
url: https://www.skills.sh/alirezarezvani/claude-skills/red-team
tipo: ferramenta
categorias: [seguranca, ia]
tags: [red-team, seguranca-ofensiva, mitre-attack, claude-code, skills, pentest]
status: novo
nota: 3
adicionado: 2026-08-28
fonte: enviado pelo hpcarlos
relacionados: [2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md, 2026-08-22-addyosmani-agent-skills-24-skills-que-impoem-disciplina-de-e.md]
---

# red-team — skill de planejamento de simulação adversarial (MITRE ATT&CK)

## Resumo

Skill de agente para **planejar exercícios de red team autorizados**: a partir de um
conjunto de técnicas do MITRE ATT&CK, do nível de acesso e dos alvos críticos, ela monta um
plano de ataque ordenado por fase da kill-chain, pontuando cada técnica por esforço e por
risco de detecção, apontando pontos de estrangulamento e sinalizando riscos de OPSEC. É
explícita sobre o que **não** é: não é varredura de vulnerabilidade nem resposta a
incidente — é simulação estruturada de adversário para testar a capacidade de detecção e
resposta de uma organização. Vem com um `engagement_planner.py` e é distribuída pela
plataforma skills.sh, dentro de uma coleção de 388 skills de Alireza Rezvani, sob MIT.

## Por que guardei

> ⚠️ Contexto inferido — o link veio sem comentário.

Como a primeira entrada de segurança ofensiva da coleção, e um exemplo de dual-use bem
tratado: a mesma metodologia que um atacante usaria, embrulhada num processo que exige
autorização e serve à defesa. É estudo legítimo de como um ataque é planejado — que é
metade do trabalho de saber se defender.

## Pontos-chave

- **⚠️ Isto só é legal com autorização escrita.** A própria skill diz, e repete: exige um
  documento de Regras de Engajamento assinado, escopo definido e aprovação executiva. Usar
  as técnicas contra sistema que você não possui ou não tem permissão explícita para testar
  é crime — a skill cita CFAA, Computer Misuse Act e equivalentes. A ferramenta se recusa a
  gerar plano sem a flag `--authorized`, e o próprio texto avisa que marcar a flag sem RoE
  real não torna o uso legítimo.
- **Não é ferramenta de ataque, é de planejamento.** Ela não explora nada nem executa
  técnica — monta e pontua o plano. O `engagement_planner.py` produz um roteiro; a execução,
  quando autorizada, é feita por outras mãos e outras ferramentas.
- **O valor defensivo é real:** entender kill-chain, pontos de estrangulamento e exposição
  de detecção é exatamente o que a equipe de defesa precisa saber. Um dos anti-padrões que a
  skill lista é "evitar toda técnica detectável" — porque isso produz um exercício
  irrealista que não valida a detecção. É a mentalidade certa.
- **Alinhada com a postura do resto da coleção:** exige autorização antes de agir, como o
  desenho de contenção do
  [Vibe-Trading](2026-08-28-vibe-trading-agente-de-ia-para-pesquisa-e-execucao-de-ordens.md)
  e a leitura-por-padrão do
  [claude-ads](2026-08-28-claude-ads-operacao-de-midia-paga-como-plugin-de-agente.md). Aqui
  a barreira é legal, não técnica, mas a lógica é a mesma: poder de ação atrás de um portão.
- **Faz parte de uma coleção grande** (388 skills, 118 agentes, sob MIT). Se o tema
  interessar, o repositório inteiro merece uma olhada — mas com o mesmo cuidado de sempre
  com coleção grande: nem toda skill ali foi feita com o mesmo rigor desta.
- **⚠️ A fonte é a plataforma skills.sh**, que não abriu nesta sessão (bloqueada pelo proxy);
  li o conteúdo direto do repositório de origem no GitHub
  (`alirezarezvani/claude-skills`). O link do achado aponta para a plataforma, como veio.
- **Números não verificados** — a API do GitHub está bloqueada nesta sessão.

## Ideias de projeto

- **Estudar o modelo de defesa lendo o de ataque** — mesmo sem nunca conduzir um red team,
  ler como a skill ordena a kill-chain e pontua risco de detecção ensina o que monitorar do
  lado defensivo. É o uso mais seguro e provavelmente o mais útil para a maioria das pessoas.
  _Esforço: baixo._
- **Endurecer o que você já hospeda** — cruzar com o
  [awesome-selfhosted](2026-08-28-awesome-selfhosted-1255-softwares-livres-para-rodar-no-seu-s.md):
  antes de expor um serviço auto-hospedado à internet, pensar como um adversário pensaria
  sobre ele. Os alvos críticos e pontos de estrangulamento da metodologia viram um checklist
  de o que proteger primeiro. _Esforço: médio._
- **Autorização como padrão de projeto** — a forma como esta skill trava a saída atrás de
  uma flag de autorização, e recusa fingimento, é um padrão reutilizável para qualquer
  ferramenta sua que faça algo perigoso. Junta-se ao cinto de segurança já registrado no
  `IDEIAS.md`. _Esforço: baixo._

## Notas

- A skill vive dentro do repositório `alirezarezvani/claude-skills`, em
  `engineering-team/skills/red-team/`, e é publicada também via plataforma skills.sh (um
  diretório de skills de agente). O SKILL.md é o conteúdo; `scripts/engagement_planner.py`
  é a ferramenta.
- Exemplo de uso, direto do SKILL.md:

  ```bash
  python3 scripts/engagement_planner.py \
    --techniques T1059,T1078,T1003 --access-level external \
    --authorized --json
  ```

- **Distinção que a própria skill faz:** `red-team` é simulação de adversário;
  `security-pen-testing` é descoberta de vulnerabilidade; `threat-detection` é caça a
  atividade de atacante; `incident-response` é resposta a incidente confirmado. Não confunda
  os quatro.
- **Recomendação:** para uso pessoal, tratar como leitura de estudo. Conduzir engajamento
  real exige contrato, escopo e autorização — nada disso é opcional, e a skill é a primeira
  a dizer.

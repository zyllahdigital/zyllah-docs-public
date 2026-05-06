# ZYLLAH DIGITAL — VAULT DO PROJETO
## Memória operacional · Atualizado em 05 de maio de 2026

---

## IDENTIDADE DO PROJETO

**Empresa:** Zyllah Digital  
**Fundador:** Guilherme Caetano  
**Nicho:** Presença digital para profissionais de saúde (médicos, dentistas, psicólogos)  
**Localização:** Nova Friburgo, RJ — opera remotamente  
**Fase atual:** Pré-receita · Prospectando clientes · Hub operacional funcional  
**Marco (04/05/2026):** Base operacional da agência construída em ~2 meses — brand, hub, contratos, sistema de 7 papéis, conteúdo, infraestrutura técnica. Fundação sólida, ainda a ser aprimorada.  
**Email:** zyllah.digital@gmail.com  
**Site:** zyllah.com.br (index.html com GA4 + Meta Pixel instalado)  
**Instagram:** @zyllahdigital (18 seguidores em 24/04/2026)  
**LinkedIn:** Guilherme Caetano  
**GitHub público:** https://zyllahdigital.github.io/zyllah-docs-public/  
**Claude Pro:** Sonnet 4.6 como agente principal  
**Plano Claude:** Pro — 1 conta Pro + 7 contas gratuitas  
**Diretriz de uso Claude:** Pro reservada para trabalho **estratégico, pontual, não funcional** — análise, arquitetura, contratos, decisões de negócio, sessões de construção. Tarefas funcionais e repetitivas vão para contas gratuitas ou Haiku.  

---

## ESTRUTURA DE DIRETÓRIOS

```
ZYLLAH/
├── 01_MARCA/
│   ├── BRANDBOOK/           → zyllah_brandbook.html
│   ├── DOCS/                → guia_sessao_cliente.html, index.html (site), relatório mar–abr
│   ├── FONTES/              → Cinzel, Cormorant Garamond, Fraunces, Jost
│   ├── FOTOS_PERFIL/        → Fotos de 31/03/2026 (4 JPGs) + referências
│   ├── LOGOTIPOS/           → Z, PALAVRA ZYLLAH, PALAVRAS, TOTAL, HORIZONTAL (.svg/.png)
│   └── REFERENCIAS_VISUAIS/
│       ├── ASSETS TELA/     → asset_tela_comparativo.html
│       ├── CONTEÚDO/        → calendário, conteúdo IG/LI, docs produção
│       ├── ESTRATÉGIA/      → hub inicial, raciocínio, concorrência, FAQ, jornada, mapa processos, stack técnico, modelo remoto
│       ├── FERRAMENTAS/     → gerador apresentação, gerador prompt, plano produção, prompts Gemini
│       ├── JURÍDICO/        → contratos, mapa riscos contratuais
│       ├── ONBOARDING_CLIENTE/ → briefing, formulário, msg pré-sessão, msg 48h
│       ├── OUTROS/          → Script Página web Hub Operacional.txt, carrossel, frames, semana 30mar
│       ├── PRODUTO/         → flow rascunho, nexa ads, produto perpétuo, vendedor indicação
│       ├── TREINAMENTO/     → quiz conselhos CFM, quiz vendas
│       └── VENDAS/          → checklist IG, imersão laboratório, briefing Mônica, Thayara
│
├── 02_ESTRATEGIA/
│   ├── ANALISES/            → 9 análises estratégicas, ZYLLAH_LINKS.md, métricas semanais (Cowork), Script Hub Operacional.txt, relatório performance 07abr
│   ├── CLAUDE/              → Relatórios de sessão 1–19, infraestrutura automação, contexto consolidado
│   ├── PROCESSOS/           → zyllah_hub.html ★, script_conector_hub.gs ★, sistema_operacional_semanal.md, manual_hub_21_abril.docx, Zyllah Hub Operacional.xlsx, briefing_rápido, schema_gatilhos, prospeccao_25leads
│   └── RELATORIOS/          → Relatório LinkedIn Company Page 31/03
│
├── 03_VENDAS/
│   ├── MATERIAIS/           → apresentacao.html, material_visita.html, objecoes.html
│   ├── PROSPECCAO/          → prompt_pesquisa_prospect, Ana Livia, roleplay script (txt)
│   └── SCRIPTS/             → script_reuniao.html, prospeccao_nova_friburgo.html, roleplay (txt)
│
├── 04_CONTEUDO/
│   ├── ARTES/               → Cards animados, imagens de marca, artes posts
│   ├── PLANEJAMENTO/        → Calendário abril s2/s3, protocolo_gravacao_oneday.md, mapa_gravacao_3dias.md, script_dia_de_gravacao.html
│   ├── POSTS/               → 7 séries (E1–E7) em 16:9 e 9:16, planer.html
│   ├── REFERENCIAS/         → Imagens referência, prints, capas de reel
│   ├── SERIES/              → ZyllahStudio (app.html + servidor.py), rev_09 (fotos)
│   └── zyllah_producao.html
│
├── 08_TECNICO/
│   ├── INFRAESTRUTURA/hub_index_upload_seguro/ → hub como index.html para deploy Cloudflare
│   └── FLOW/                → prompt_agente_medico_v1.md, n8n_workflow_zyllah_flow_v1.json, docker-compose.yml, .env.example, README.md
│
└── 05_PRODUCAO_AV/
    ├── ASSETS/CAPAS_THUMBNAILS/ → Thumbnails YouTube (V1–V5, S2 Ep01–03), capa canal
    ├── ASSETS/FOTOS_IA/         → 17 fotos Gemini geradas
    ├── EDITADO/REELS/           → 4 Reels editados + WAV
    ├── EDITADO/YOUTUBE_SERIE2/  → 5 cenas croma + cena final geral
    └── FERRAMENTAS/
        ├── zyllah_motion/       → Projeto Remotion (node_modules instalado)
        └── Transcrição o-peso-da-saude (json + txt)
```

---

## HUB OPERACIONAL — ESTADO ATUAL

### Dois hubs: distinção importante

| | Hub Inicial (Ideia) | Hub Operacional (Real) |
|---|---|---|
| **Arquivo** | `01_MARCA/REFERENCIAS_VISUAIS/ESTRATÉGIA/zyllah_ideia_inicial_de_hub.html` | `02_ESTRATEGIA/PROCESSOS/zyllah_hub.html` ★ |
| **Natureza** | Conceito visual original — vitrine da ideia | Ferramenta real de operação diária |
| **Integração** | Nenhuma | Google Sheets via Apps Script (JSONP) |
| **Senha** | — | Zhub |
| **Deploy** | — | Cloudflare Pages · `npx wrangler pages deploy . --project-name=zyllah-hub` |
| **Proteção** | — | Login Google (Gmail Zyllah) via Cloudflare Access |
| **Pasta deploy** | — | `08_TECNICO/INFRAESTRUTURA/hub_index_upload_seguro/` (hub como index.html) |

### Hub Operacional v10 — arquitetura técnica (05/05/2026)

**Script URL (Apps Script Web App v3):**
```
https://script.google.com/macros/s/AKfycbxXdfQFOWFb3xjBaQnc6Bk9sWfXAsx2cdidVXiV0TNfSmHirwpySJdeRpIXNtVF019TSg/exec
```

**Protocolo de comunicação:** GET + JSONP (sem POST, sem doPost — resolvido definitivamente na Sessão 19)

**Arquitetura:**
- `?action=listar` → retorna clientes e ritual
- `?action=salvar&data=JSON_ENCODED&callback=FUNC` → salva cliente
- `?action=remover&data=...` → remove cliente
- `?action=ritual&data=...` → salva checklist de segunda
- `?action=getRitual` → lê checklist
- `?action=gerarComentarioYT&data=...` → gera comentário YouTube via Haiku (⚠️ pendente de implantar)
- `?action=gerarPauta&data=...` → gera 5 sugestões de pauta via Haiku

**Planilha Google Sheets — abas operacionais (case-sensitive, criadas por `setupPlanilha()`):**
- `Clientes` — id, nome, esp, plano, tipo, inicio, vencimento, valor, pagamento, entregas, marcos, reuniao, proxPag, notas, data_ultimo_alerta, status_financeiro
- `Prospects` — funil (Kelly, Cleonicio, Fabricia, Mônica e novos) — 21 colunas incluindo nota_presenca, doctoralia, gap_principal
- `Pauta` — pendências de produção de conteúdo (hoje só em localStorage; pendência ativa: persistir via `_seedPauta()` no GAS)
- `Financeiro` — entradas/saídas e tracker MEI
- `Demandas` — follow-ups automáticos D+3/D+7/D+14 e tarefas avulsas
- `EventosCalendar` — IDs de eventos criados no Google Calendar "Zyllah Hub"

**Abas de contexto (criadas por `setupContexto()`):** `CTX_Permanente`, `CTX_Evolutivo`, `CTX_Transitorio`, `CTX_Arquivo`.

**Ritual NÃO é aba** — vive em `PropertiesService.getScriptProperties().getProperty('RITUAL_DATA')` como JSON.

**ID da planilha:** `PropertiesService.getScriptProperties().getProperty('PLANILHA_ID')`. Trocar a planilha exige atualizar essa propriedade e reimplantar a Web App.

**Setup inicial (rodar uma vez no editor do Apps Script):** `setupPlanilha()` → `setupContexto()` → opcional `semearDemandas()`. Todos idempotentes.

**Módulos no hub:**
1. Cards de clientes (máx. 4) com entregas, marcos, status pagamento
2. Alertas automáticos (pagamento, entrega urgente, reunião próxima)
3. Ritual de segunda-feira (7 checkboxes)
4. Calendário semanal operacional
5. Modal de edição de cliente
6. **YouTube module** — busca vídeos por 9 termos, gera comentário via Haiku (chave Anthropic via Apps Script, nunca no navegador)

**Segurança de chaves:**
- Chave Anthropic → `PropertiesService.getScriptProperties()` no Apps Script (NUNCA no HTML)
- Google YouTube API Key → pode ficar no hub, desde que restrita por referrer no Console
- **Incidente registrado (16/04):** chave `sk-ant-api03-Zf2...xgAA` commitada no repo público e auto-revogada. Nova chave gerada. Regra permanente: zero credenciais em repos públicos.

---

## SISTEMA OPERACIONAL — 7 PAPÉIS

| Papel | Frequência | Agente principal |
|---|---|---|
| 1. Prospector | 3x/semana · 20 min | ✋ + ⚡ Haiku |
| 2. Vendedor | Sob demanda · 48h antes reunião | 🧠 Sonnet |
| 3. Produtor | Ter+Qua produção · Qui revisão · Sex publicação | ✋ + 🖥️ Cowork |
| 4. Gestor de Cliente | Diário 5 min + reunião mensal | ✋ + 🖥️ Cowork |
| 5. Financeiro | Semanal 5 min + vencimentos | ✋ + ⚡ Haiku |
| 6. Jurídico | Sob demanda · antes de contratos | 🧠 Sonnet |
| 7. Parceiro | Sob demanda · após 2º cliente | ✋ |

**Legenda de agentes:**
- 🧠 **Sonnet** — estratégia, copywriting, análise, documentos ricos
- ⚡ **Haiku** — classificação, legendas, CFM, tarefas estruturadas
- 🖥️ **Cowork** — pastas, relatórios locais, tarefas repetitivas no desktop
- 💻 **Código** — Apps Script, n8n, HTML/JS
- 🤖 **n8n** — automações recorrentes (pós-validação)
- ✋ **Manual** — contato humano, aprovações, assinaturas

---

## PRODUTOS / PLANOS

| Plano | Duração | Público |
|---|---|---|
| Essencial | 6 meses | Profissionais em início de presença |
| Presença Completa | 6 meses | Presença estruturada, mais canais |
| Autoridade | 12 meses | Liderança de nicho, conteúdo premium |

**Outros produtos (horizonte):**
- Nexa Ads — Google/Meta/LinkedIn Ads (add-on)
- Zyllah Flow — automação WhatsApp + Agenda + CRM (rascunho — NÃO apresentar ainda)
- Produto perpétuo (pós 2 cases)
- Parceria Cloudia (SaaS atendimento)

---

## REGRAS INEGOCIÁVEIS

**Prospecção:**
- NUNCA revelar o gap digital na DM — só na reunião presencial
- NUNCA mencionar a Zyllah nos comentários de aquecimento
- SEMPRE pesquisar antes de qualquer contato
- Aguardar 2–3 dias entre comentário e DM

**Conteúdo / CFM:**
- Verificar toda peça pela Resolução CFM 2.336/2023
- Proibido: antes/depois, preço de procedimento, depoimento identificado com nome e foto
- Permitido: informativo, educativo, presença institucional

**Segurança técnica:**
- Chaves de API NUNCA em HTML que vai para repositórios públicos
- Chave Anthropic SEMPRE via PropertiesService no Apps Script
- Google API Key do YouTube: OK no hub se restrita por referrer no Console

**Jurídico:**
- Todo novo cliente: Contrato Base + Anexo I do plano + Adendo Piloto (se aplicável)
- Validação obrigatória por advogado antes do primeiro contrato real (pendente)
- LGPD/DPA obrigatório para dados sensíveis de saúde

**Operação:**
- Máximo 4 clientes ativos no hub (fase atual)
- Ritual de segunda-feira: 30 minutos, 7 checkboxes
- Por sessão com Sonnet: declarar hora + foco único ao abrir

---

## PARCERIA CLOUDIA

- **Status:** Credenciado em 09/04/2026
- **Decisão (05/05/2026):** Comissionamento não é prioridade no início. Não indicar o lead só compromete o comissionamento — a parceria em si permanece. Prazo passou sem pressão. Retomar quando fizer sentido.
- **Link de indicação:** digital.cloudia.com.br/cloudia-indicacao-do-parceiro?agncia=zyllah
- **Regra:** manter 1 lead por trimestre para manter comissionamento (opcional por ora)
- **NF Zyllah:** emitir em abril, julho, outubro, janeiro (CNPJ obrigatório — quando MEI estiver regularizado)

---

## PROSPECTS ATIVOS (em 05/05/2026 — atualizar após cada contato)

| Nome | Status | Próxima ação |
|---|---|---|
| Kelly Purger | A cadastrar no hub | Iniciar aquecimento IG |
| Cleonicio Cordeiro | A cadastrar no hub | Comentar no IG |
| Fabricia Corbett | A cadastrar no hub | Comentar no IG |
| Mônica (psicóloga) | DM diagnóstica enviada | Aguardar resposta |

---

## MÉTRICAS (última semana disponível: 17–23/04/2026)

| Canal | Métrica | Valor | Variação |
|---|---|---|---|
| Instagram | Visualizações | 22 | — |
| Instagram | Alcance | 3 contas | — |
| Instagram | Seguidores | 18 | 0% crescimento |
| Instagram | Posts publicados | 0 | Semana sem publicação |
| LinkedIn | Impressões | 0 | — |
| LinkedIn | Seguidores novos | 0 | — |
| YouTube | Visualizações | 1 | -86% vs semana anterior |

**Semana anterior (10–16/04):** Instagram 68 views / LinkedIn +27,9% impressões (193) / YouTube 7 views

**Diagnóstico:** queda reflete ausência de publicações. Retomar rotina de conteúdo é urgente.

---

## PENDÊNCIAS — CONSOLIDADO (Sessão 25/04/2026)

> Última revisão: 25/04/2026 · Para marcar como feito: trocar `[ ]` por `[x]`

---

### ✅ Resolvido em 05/05/2026 (Sessão 23 — longa)
- [x] **Hub v10:** layout corrigido (grid `1.6fr 1fr 1fr`, overflow-x, width:0 removido)
- [x] **Hub:** botão `✦ Comentar` em cada card de prospect + modal com skill calibrada
- [x] **GAS:** função `gerarComentarioProspect` + skills `SKILL_VOZ_GAS` e `SKILL_COMENTARIO_GAS` embutidas — registrada no `doGet`
- [x] **Pipeline prospectar.py** criado em `ZyllahOS/` — Qwen → txt → inbox → Haiku + skills → comentários em `inbox/saidas/`
- [x] **ZyllahOS/04-SKILLS:** criadas `emergency_mode.md`, `checklist_prospeccao.md`
- [x] **ZyllahOS/05-PROJECTS:** criadas `hub_proxima_iteracao.md`, `sprint_gravacao_e_runway.md`
- [x] **Cloudia:** prazo removido da urgente. Comissionamento não é prioridade. Parceria mantida.
- [x] **Instagram/LinkedIn auditados:** 17 posts, 20 seguidores. Posts sobre dor do médico superam posts sobre Zyllah. Audiência SP já orgânica. Ratio seguindo/seguidores corrigir (parar follow-for-follow).
- [x] **Huashu Design** classificado: 🟡 médio prazo, pós-sprint gravação, para apresentações interativas.
- [x] **CLAUDE.md e MEMORY.md** atualizados com marco dos 2 meses + estrutura 1 Pro / 7 gratuitas.
- [x] **sprint_gravacao_e_runway.md:** 20 roteiros por figurino (A/B/C), plano de 6 meses de conteúdo, estratégia de volume sem anúncios, válvulas de runway.

### ✅ Resolvido em 25/04/2026 (Sessão anterior)
- [x] Hub Fase 1: CFM Gate, Follow-up D+3/D+7/D+14, Auto-score, MEI tracker
- [x] PROD_STEPS por formato (vídeo/post/motion separados)
- [x] Seed de 30 itens de pauta no hub
- [x] Bug corrigido: botão "Para cliente" no gerador de pauta (função `pgenSetAlvo` estava faltando)
- [x] Contrato v2.4 revisado e pronto para advogado (email corrigido, Cláusula 20 assinatura eletrônica, 9 pontos para o advogado, campo testemunhas)
- [x] Manual do hub criado (`manual_hub_completo.html`)
- [x] Calendário de produção completo + sprint 4 dias (`zyllah_calendario_producao_completo.html`)
- [x] CRM Encantarys v2 com paradigma timeline (`crm_encantarys_v2.html`)
- [x] Voz da Fernanda documentada (`voz_fernanda_ia.md`)
- [x] Template de relatório periódico para clientes (`zyllah_relatorio_cliente.html`)
- [x] Novos formatos na pauta: youtube, motion, tela, bastidor

---

### 🔴 Urgente — tem prazo ou bloqueia operação

- [x] **Cloudia — pressão de prazo resolvida (05/05/2026):** Confirmado via chat que não indicar o lead só compromete o comissionamento, não a parceria em si. Decisão: comissionamento não é prioridade neste início — menos uma pressão. Parceria mantida sem urgência de indicação.
- [ ] **Cloudia — opcional:** confirmar por email os termos de re-credenciamento futuros quando fizer sentido retomar.
- [ ] **Abrir MEI com CNAE correto — ou mudar CNAE se já aberto errado** (27/04) — CNPJ necessário para: NF Cloudia, contratos com clientes, Stripe. CNAE provável: 7319-0/04 (consultoria em publicidade) ou 6204-0/00 (consultoria em TI). Confirmar com contador antes de abrir/alterar — escolha errada bloqueia emissão de NF para o tipo de serviço Zyllah.
- [ ] **Deploy do hub v3 atualizado no Cloudflare** — copiar `zyllah_hub.html` → `08_TECNICO/INFRAESTRUTURA/hub_index_upload_seguro/index.html` → `npx wrangler pages deploy . --project-name=zyllah-hub`
- [ ] **Ativar proteção no Cloudflare** — hub está em `https://zyllah-hub.pages.dev/` sem senha. Cloudflare Zero Trust → Access → Applications → email `zyllah.digital@gmail.com`
- [ ] **Retomar publicação:** publicar Reel "Médico cansado" hoje — é o primeiro conteúdo da retomada

**Zyllah Flow — construir pra valer (decisão tomada em 26/04/2026):**
> Caminho A escolhido. WhatsApp Cloud API bloqueada até MEI sair → usar Waha ou Evolution API por enquanto. Prazo-alvo: 2 semanas.
> **VPS Hostinger não tem fidelidade tipo operadora**: paga adiantado por período (mensal mais caro ~R$80, 12m ~R$44/mês = R$528 adiantado, 24m ~R$38/mês). Reembolso pro-rata só nos primeiros 30 dias; depois disso o pago não volta. Recomendação: começar com mensal pra testar 1–2 meses; se rodar estável, migra para 12m.
- [ ] **Z1.** Contratar VPS Hostinger 8GB, região Brasil, template n8n pré-instalado. Cupom `MAESTROS10` da pesquisa pode dar 10% off em planos 12/24m. Senha 12+ chars com símbolos.
- [ ] **Z2.** Acessar n8n via painel Hostinger; criar usuário admin; ativar chave de licença enviada por email (menu Usage and Plan).
- [ ] **Z3.** Decidir número WhatsApp dedicado — chip novo ou número existente. Recomendação: chip novo, pra isolar risco de bloqueio.
- [ ] **Z4.** Escolher entre **Waha** (self-hosted, gratuito, mais controle) e **Evolution API** (mais usada no Brasil, comunidade ativa). Daniel é contato pra Evolution/Z-API se precisar de setup pago.
- [ ] **Z5.** Conectar número WhatsApp na API escolhida e testar envio/recepção básico.
- [ ] **Z6.** Adaptar `voz_fernanda_ia.md` → prompt de sistema para agente médico (eu faço, próxima sessão dedicada). Personagem: triagem de paciente médico, tom Zyllah (clínico, direto), filtro CFM embutido.
- [ ] **Z7.** Montar fluxo n8n: webhook recebe mensagem → node Wait 8s para buffer/fila (junta mensagens picotadas) → AI Agent (Sonnet via Anthropic API) → resposta → log em planilha.
- [ ] **Z8.** Definir critérios de hand-off pra humano (palavras-gatilho, intenção de marcar consulta, dúvida fora do escopo).
- [ ] **Z9.** Bateria de testes com número-amigo: 20 conversas simuladas (cordial, irritado, pressa, dúvida fora do escopo, tentativa de jailbreak).
- [ ] **Z10.** Documentar fluxo final em `zyllah_flow_v1.md` para que o cliente futuro saiba o que está contratando.
- [ ] **Z11.** Só depois de Z10: reincluir WhatsApp 24h no `zyllah_script_reuniao.html` e no Anexo I do plano Presença Completa.

> **Pré-requisito para eu começar Z6/Z7:** Z1 a Z5 prontos. Me chame quando o n8n estiver acessível e o número estiver conectado.

**Z6/Z7 entregues em 26/04/2026** — pacote em `08_TECNICO/FLOW/`:
- `prompt_agente_medico_v1.md` — Helena (concierge 24/7), avisos LGPD + IA, ACTION JSON pattern
- `n8n_workflow_zyllah_flow_v1.json` — webhook → buffer → Calendar slots → Sonnet → parse → Waha → Switch ACTION → Calendar create/update/delete
- `docker-compose.yml`, `.env.example`, `README.md` atualizados

**Auditoria contratual (Cláusula 11 + Anexo I-B Zyllah Flow) — 3 gaps a fechar antes de cobrar 1º cliente:**
- [ ] **Z12.** Workflow de **lembrete D-1 automático** (Schedule trigger lendo Google Calendar) — contrato promete confirmação 24h antes. Em `08_TECNICO/FLOW/` como segundo workflow `n8n_workflow_lembrete_d1_v1.json`.
- [ ] **Z13.** **Outros canais (Instagram Direct, email, chat site)** prometidos em até 45 dias úteis após ativação do WhatsApp. Roadmap interno; documentar caminho de implementação.
- [ ] **Z14.** **Trocar credencial Anthropic do piloto pela do cliente** antes de cobrar — contrato exige que o cliente pague API direto em platform.anthropic.com (cartão dele). No piloto está usando sua chave. Procedimento de onboarding deve incluir esse passo.

---

### 🟡 Alta prioridade — esta semana

**Brain dump 27/04 — adicionado nesta sessão:**

- [ ] **(27/04) Refatorar contrato v2.4 — eliminar linguagem de "nota de advogado"** — Filipe estranhou e perguntou se foi advogado de verdade que escreveu. Resolver os 9 pontos no que for resolvível por mim mesmo (linguagem, redundância, formatação). Para o que sobrar genuinamente em aberto, **NÃO usar palavra "advogado" nem "verificar com legal"** — substituir por marcador discreto: asterisco + palavra simples "incerteza" em azul (`<span style="color:#2563eb">*incerteza</span>`). Entrega: contrato pronto pra parecer auto-redigido, com pontos abertos sinalizados de forma neutra.
- [x] **(27/04) Sistema escalável de engajamento nas redes dos prospects** — `ZyllahOS/prospectar.py` + `prospectar.bat`. Fluxo: gravar tela navegando pelos prospects → jogar no Qwen (descreve posts) → salvar .txt em `inbox/` → duplo clique no .bat → comentários prontos em `inbox/saidas/`. Usa Haiku (conta gratuita). Skills: `zyllah-voz` + `zyllah-comentario-publico`. Localizado em 05/05/2026. — hoje é manual (entrar no IG, escolher post, comentar). Precisa de: lista mestre de prospects + handles + última-vez-comentado, rotação semanal sem repetir o mesmo prospect 2x na mesma semana, biblioteca de comentários-tipo (não-genéricos, ancorados em algo específico do post), regra dos 2-3 dias antes da DM. Fica numa aba do hub ou doc próprio. **Lembrete operacional:** comentário > DM frio (já é regra), e nunca mencionar Zyllah no aquecimento.
- [x] **(27/04) Protocolo de gravação one-day** — entregue em `04_CONTEUDO/PLANEJAMENTO/protocolo_gravacao_oneday.md` e `mapa_gravacao_3dias.md`. Script completo com todas as falas por figurino em `script_dia_de_gravacao.html`.
- [ ] **Sprint de gravação — AMANHÃ 06/05/2026** — Roupas chegaram (Shein, não Shopee). Cabelo cortado em 05/05. Plano detalhado em `ZyllahOS/05-PROJECTS/sprint_gravacao_e_runway.md`. Figurinos: (A) tudo preto — autoridade, (B) polo azul marinho — consultivo, (C) suéter cinza + café — humanizado. Meta: 20 clipes × 4 formatos = 80 peças = ~26 semanas de conteúdo. Script com todas as falas em `04_CONTEUDO/PLANEJAMENTO/script_dia_de_gravacao.html`.
- [ ] **(27/04) Apresentações personalizadas pré-feitas para os 4 prospects ativos** — Kelly Purger, Cleonicio Cordeiro, Fabricia Corbett, Mônica. Caso algum confirme reunião com 48h de antecedência (ou menos), apresentação tem que estar pronta. Base: `zyllah_apresentacao.html`. Conteúdo por prospect: gap digital identificado, especialidade, plano sugerido, números do mercado dele.
- [ ] **(27/04) Programa de treino de roleplay + repertório de objeções IA-relacionadas + plano de postura física** — Guilherme pediu "a melhor forma de treinar". Componentes: (a) método (memorização vs debate vs simulação vs extremos), (b) cadência (frequência semanal, duração de cada sessão), (c) repertório escrito de respostas para objeções recorrentes — em especial as IA-relacionadas: "que IA você usa?", "isso é rapidinho", "tem equipe? com IA sai rápido, né?", e o vetor de menosprezo geral; (d) plano de postura física (mãos, voz, contato visual, ritmo de fala, o que fazer ao ouvir uma objeção que machuca). **Contexto importante (memória):** autoestima de vendedor está em construção — não é treino motivacional, é treino mecânico de respostas concretas.
- [ ] **(27/04) Manual do gestor para relatórios + tradução em linguagem cliente** — gestor precisa saber (a) como ler os números, (b) como ajustar estratégia a partir deles. Cliente precisa receber a mesma informação em linguagem da área dele (médico/dentista/psicólogo). Entregável: `manual_gestor_relatorio.md` (interno) + atualização do `zyllah_relatorio_cliente.html` com camada de tradução. Critério: se o cliente lê e entende a decisão sem te chamar, está bom.

**Pré-existente:**

- [ ] **Colar `gerarComentarioYT` no Apps Script e reimplantar** — função está no hub, falta no GAS. Ver `script_conector_hub.gs` e ZYLLAH_LINKS.
- [ ] **Testar sync do hub** — Chrome Console: `gs({action:'listar'}).then(d=>console.log(d))`
- [ ] **Contratar advogado especialista em contratos de prestação de serviço** — Filipe declinou (especialidade dele é societário, não contratos de serviço). Pediu indicação a ele; provável que seja pago. Aguardar nome indicado e orçar. Contrato v2.4 está pronto para enviar quando achar o profissional certo.
- [ ] **Criar email `juridico@zyllah.com.br`** — descobrir onde o DNS do domínio está (Registro.br? Hostinger? Cloudflare?) — a caixa é criada lá, não no Brevo
- [ ] **Cadastrar Kelly, Cleonicio e Fabricia no hub** — aba Prospects, dados já no seed
- [ ] **Iniciar aquecimento IG:** Dr. Cleonicio e Dra. Fabricia — comentar em 2 posts antes de DM
- [ ] **Converter `CRM Encantarys.xlsx` para Google Sheets** — abrir no Drive → Arquivo → Salvar como Google Planilhas
- [ ] **Subir backup do hub inicial no GitHub e Drive** — `zyllah_ideia_inicial_de_hub.html` → repo público como `zyllah_hub_conceito.html` + cópia no Drive. É só vitrine da ideia original (não é ferramenta operacional). Backup histórico, não tem outro fim.
- [ ] **Documentar regra GPT Image 2 vs Nano Banana 2 no `zyllah_producao.html`** — GPT Image 2 para carrosséis com texto, infográficos, mockups, recibos, QR codes funcionais (precisão tipográfica + acentuação PT). Nano Banana 2 para retratos fotográficos puros / avatar (fotorrealismo de pele e olhar). Fonte: pesquisa "Análise de Fidelidade GPT Image 2 vs Nano Banana".

---

### 🔵 Médio prazo — próximas 2–4 semanas

**Produção de conteúdo:**
- [ ] **Sprint Dia 1** — gravações de tela: V1 (Google), V3 (CFM), V5 (feeds), cards E1–E7
- [ ] **Sprint Dia 2** — câmera: chroma Série 2 (B1–B5) + V2 + V4 + partes V5 + bastidores
- [ ] **Sprint Dia 3** — edição: V1–V5 completos + Manifesto Série 2 + Reels derivados
- [ ] **Sprint Dia 4** — legendas (Haiku) + upload YouTube + Buffer (3 semanas)
- [ ] FAQ 01–08 no Remotion (motion, sem câmera)
- [ ] Bastidor: tour pelo hub (screen recording)

**Técnico — Hub:**
- [ ] Configurar triggers no Apps Script: `verificacaoDiaria()` às 07h, `resumoSemanal()` domingo 20h
- [ ] Implantar `gerarComentarioYT` no Apps Script (doGet + função)
- [ ] Fazer `_seedPauta()` persistir no GAS (atualmente só no localStorage)
- [ ] Gap G3: adicionar campo "link do Buffer" na pauta
- [ ] Gap G7: criar atalho `.bat` para abrir Remotion Studio com duplo clique

**Técnico — Canva:**
- [ ] Completar Brand Kit: Cabeçalho (Jost, 20pt), Subcabeçalho (Jost, 14pt), Corpo (Jost Light, 13pt), Labels (Jost, 9pt)
- [ ] Criar templates Zyllah: 1 template de feed, 1 de Reel, 1 de LinkedIn (definir se para Zyllah ou para clientes primeiro)

**Gráfica — material de visita:**
- [ ] Definir gráfica online (Guilherme tem uma "muito boa" em mente — pesquisar e escolher)
- [ ] Levantar specs técnicas da gráfica escolhida: formato/peça, sangria, margem segurança, resolução, cor (CMYK/Pantone), formato de arquivo (PDF/X-1a, etc.), acabamento (couché 250g? verniz?), quantidade
- [ ] Reformatar `material_visita.html` para gerar PDF dentro das specs — quando specs estiverem na mão, me chamar pra reescrever o HTML/CSS com `@page` size, sangria e CMYK

**Técnico — CapCut/Remotion:**
- [ ] Sessão dedicada para criar scripts batch no Remotion/CapCut que automatizem produção de FAQ e cards
- [ ] **Técnicas CapCut Batch Edit para Reels derivados (Sprint Dia 4):** método "Delete + Ctrl+Z" (deletar tudo que não é o Short atual, exportar, desfazer, repetir) — mais rápido que sobreposição em track superior. Compound Clips (Alt+G) para aplicar efeitos em lote. Fonte: pesquisa "Guia Definitivo da Edição de Vídeo com IA".
- [ ] **Huashu Design** (05/05/2026) — open-source alternativo ao Claude Design. Gera UI/protótipos interativos, apresentações (Swiss Grid Tech, Dark Future, Editorial Brutalist) e **vídeos MP4 de 15s a partir de HTML** via Playwright + FFMPEG. Compatível com Claude Code. Casos de uso para Zyllah: (1) apresentações personalizadas por prospect em formato interativo, (2) motion graphics curtos sem Remotion. **Gatilho:** pós-sprint de gravação. **Dependência:** instalar FFMPEG. Fonte: PESQUISA DE FEATURES.txt 05/05.

**Zyllah Flow:**
- [ ] Definir número de WhatsApp para piloto do Zyllah Flow
- [ ] Criar prompt de sistema adaptado (base: `voz_fernanda_ia.md` adaptada para médico)
- [ ] Montar fluxo no n8n + Waha para o plano Presença Completa
- [ ] Testar com o número disponível antes de apresentar a clientes

**Jurídico:**
- [ ] Enviar contrato v2.4 para advogado com instrução dos 9 pontos
- [ ] Validação obrigatória antes de assinar qualquer contrato real

**Docs estratégicos (reorganização pendente):**
- [ ] Revisar e aglutinar: `zyllah_jornada_cliente_ramos.html`, `zyllah_mapa_processos_arquitetura.html`, `zyllah_stack_tecnico_7_papeis.html`, `zyllah_faq_estrategico.html`, `plano_producao.html`, `gerador_prompt.html` — critério: "isso muda minha ação hoje?"

---

### ⚪ Backlog — sem prazo crítico

- [ ] Migrar tarefas do Cowork (prospector, tendências) para Apps Script
- [ ] Configurar Daniel — Z-API/Evolution para WhatsApp Flow (aguardar validação do Flow primeiro)
- [ ] Roleplay de vendas semanal com Claude
- [ ] Vídeos Cloudia — arquivados (não produzir até rever a parceria)
- [ ] Executar `testarExportacao()` para gerar 3 arquivos de contexto no Drive
- [ ] Colar links do Drive nas instruções do projeto (camadas 1, 2, 3)
- [ ] Produto perpétuo — só após 2 cases confirmados
- [ ] Parceria Vendedor Externo — só após 2º cliente ativo
- [ ] **Fábrica de conteúdo com avatar IA (n8n + HeyGen + Tavily + Metricool + 11Labs)** — pipeline: Tavily pesquisa tendência → Gemini 3 Pro (via OpenRouter) gera roteiro com `\n\n` para pacing → HTTP POST HeyGen com Avatar ID + Voice ID 11Labs (720x1280) → loop GET+IF+Wait 30s até `status:completed` → Metricool agenda IG/TikTok/YT + backup Google Drive. Infra: VPS Hostinger 8GB (~R$44/mês). **Só implementar após 1º cliente pagante** — antes disso é over-engineering. Fonte: 3 textos sobre "Fábrica de Conteúdo / Content Factory".
- [ ] **Modelo "agência de 1 pessoa" (Marcela AI / Maven OS) — reavaliar com 3 clientes ativos.** Stack: Easy Panel + n8n + Chatwoot self-hosted + WhatsApp Cloud API oficial (Graph API, não Z-API). Substitui PandaDoc, ClickUp e triador humano. Economia projetada: ~R$72k/ano. Não fazer agora: hub v3 já cobre, onboarding da WhatsApp Cloud API é chato e exige CNPJ. Fonte: "A Agência de Uma Pessoa e a Era da Alavancagem por IA".
- [ ] **Antigravity (IDE Google com Claude Code)** — arquivado. Você já roda Claude Code direto, sem ganho operacional. Reavaliar só se aparecer feature exclusiva.
- [ ] **HeyGen avatar substituindo a sua imagem na Zyllah** — não fazer. Anti-marca: posicionamento Zyllah é presença humana clínica, não persona sintética. Pode ser oferta futura para clientes médicos, nunca para o canal Zyllah.
- [ ] **Refatorar CLAUDE.md em arquitetura de Skills (Progressive Disclosure)** — gatilho: após 2º cliente ativo. Antes disso é meta-trabalho — organizar o sistema em vez de usar. Vault carrega ~14k tokens/sessão; refatoração economizaria 60–80%, mas isso não muda decisão de negócio em pré-receita. Mover 7 papéis para skills (`prospector.md`, `vendedor.md`, etc.) e deixar CLAUDE.md como índice.
- [ ] **Pipeline de edição IA (Dscript + AutoEdit + Whisper + Remotion)** — gatilho: quando edição virar gargalo real (você reclamando "edito demais"). Hoje o gargalo é publicar, não editar. CapCut puro resolve. Fonte: "Guia Definitivo da Edição de Vídeo com IA".

---

### 📦 Encantarys — pendências paralelas

- [ ] Fernanda: ativar CRM v2 (`crm_encantarys_v2.html`) — testar no celular primeiro
- [ ] Colar `CRM - APPS SCRIPT v2.txt` no Google Apps Script do Encantarys e reimplantar
- [ ] Separar planilha Encantarys como Google Sheets (mesma conversão manual acima)
- [ ] Fernanda: revisar e completar `voz_fernanda_ia.md` com expressões próprias que faltam
- [ ] Ativar calendário T+1/T+90/T+330 para clientes existentes (Nicoly, Nicole, Naiara) — não têm eventos criados ainda

---

## HISTÓRICO DE SESSÕES

| Sessão | Data | Tema principal |
|---|---|---|
| 1 | mar/2026 | Fundação da Zyllah, identidade, estratégia inicial |
| 4 | 04/mar | Brandbook, posicionamento |
| 8 | 08/mar | Primeiros documentos operacionais |
| 16 | 16/mar | Estratégia editorial, calendário |
| 17 | 17/mar | — |
| 19 | 19/mar | — |
| 20 | 24/mar | — |
| 20 (noite) | 24/mar | — |
| — | 28/mar | Múltiplas sessões: operação, docs |
| — | 31/mar | Fim/início de ciclo |
| — | 01/abr | Pós-março |
| — | 03/abr | Contratos, onboarding |
| **17** | **08–09/abr** | **FAQ completo, cards série 2, hub+Sheets inicial** |
| — | 16/abr | Sessão Opus (análise planejamento) |
| **19** | **16/abr** | **Hub v3 (CORS resolvido), YouTube module, incidente chave API, sistema 7 papéis** |
| — | 24/abr | Vault + Hub Fase 1 + CRM Encantarys v2 |
| **20** | **25/abr** | **Contrato v2.4, hub fixes (PROD_STEPS, seed pauta, bug pgenSetAlvo), calendário produção completo, manual hub, template relatório** |
| **21** | **27/abr** | **Brain dump matinal: 6 frentes novas adicionadas ao vault (CNAE MEI, engajamento escalável, contrato sem "advogado", protocolo gravação one-day, apresentações pré-feitas, roleplay+objeções IA, manual gestor)** |
| **22** | **04/mai** | **Classificação features, skills em ZyllahOS, pipeline prospectar.py, arquitetura 7 contas Claude, ✦ Comentar no hub, GAS gerarComentarioProspect, layout hub v10** |
| **23** | **05/mai** | **Sessão longa: Cloudia sem pressão, checklist_prospeccao, hub_proxima_iteracao, sprint_gravacao_e_runway (20 roteiros), emergency_mode, audit Instagram/LinkedIn, estratégia de volume e runway** |
| **22** | **05/mai** | **Auditoria vault · Roupas chegaram (Shein) · Cabelo cortado · Grava amanhã · Pipeline Qwen+Python localizado (`ZyllahOS/prospectar.py`) · Análise IG/LinkedIn · sprint_gravacao_e_runway.md criado · estratégia runway + prospecção volume** |

---

## PESQUISA DE FEATURES
> Guilherme cola pesquisas em `C:\Users\Guilherme\Documents\ZyllahOS\fundador\PESQUISA DE FEATURES.txt`. Eu leio no início de cada sessão e classifico nas pendências se for acionável.

**Histórico de classificações:**

- **26/04/2026** · Lote inicial (8 blocos): Antigravity, Avatar IA n8n+HeyGen, Skills/Progressive Disclosure, GPT Image 2 vs Nano Banana, Edição IA AutoEdit/Remotion, Agência de 1 pessoa Maven OS, CapCut Batch. Após autocrítica, reordenado:
  - 🟡 Alta (única): documentar regra GPT Image 2 vs Nano Banana no `zyllah_producao.html`
  - 🔵 Médio: técnicas CapCut Batch para Sprint Dia 4 (Delete+Ctrl+Z, Compound Clips)
  - ⚪ Backlog (com gatilhos explícitos): fábrica avatar IA (após 1º cliente pagante) · Maven OS self-hosted (após 3 clientes) · refatorar Skills (após 2º cliente) · pipeline edição IA (quando edição virar gargalo) · Antigravity arquivado · HeyGen na marca Zyllah descartado

*(novas entradas abaixo — formato: data · nome · fonte · uma linha · urgência)*

---

## DOCUMENTOS CRÍTICOS (ordem de consulta)

| Prioridade | Arquivo | Localização |
|---|---|---|
| ★★★ | `zyllah_hub.html` | `02_ESTRATEGIA/PROCESSOS/` — também em Cloudflare Pages |
| ★★★ | `script_conector_hub.gs` | `02_ESTRATEGIA/PROCESSOS/` |
| ★★★ | `zyllah_sistema_operacional_semanal.md` | `02_ESTRATEGIA/PROCESSOS/` |
| ★★★ | `ZYLLAH_LINKS.md` | `02_ESTRATEGIA/ANALISES/` |
| ★★ | `zyllah_brandbook.html` | `01_MARCA/BRANDBOOK/` |
| ★★ | `zyllah_raciocinio.html` | GitHub público |
| ★★ | `relatorio_sessao_16abr.md` | `02_ESTRATEGIA/CLAUDE/` |
| ★★ | `zyllah_mapa_riscos_contratuais.html` | `01_MARCA/REFERENCIAS_VISUAIS/JURÍDICO/` |
| ★ | `zyllah_faq_estrategico.html` | `01_MARCA/REFERENCIAS_VISUAIS/ESTRATÉGIA/` |

---

## IDENTIDADE VISUAL (referência rápida)

| Elemento | Valor |
|---|---|
| Cor principal | `#B8976A` (gold) |
| Cor fundo | `#1A1714` (ink) |
| Cor clara | `#FAF7F2` (cream) |
| Tipografia editorial | Cormorant Garamond (serif) |
| Tipografia funcional | Jost (sans-serif) |
| Tom de voz | Clínico, direto, sem excessos — nunca genérico |

---

## EQUIPAMENTO / SETUP

| Item | Detalhe |
|---|---|
| Desktop | i5-9600KF · 32GB RAM · RTX 3050 · SSD 466GB |
| Celular | Samsung A52S (usado em sessões mobile e gravação) |
| Captação | A52S + gimbal + iluminação básica |
| Edição vídeo | CapCut |
| Agendamento | Buffer |
| Contratos | PandaDoc (5 docs/mês grátis) |
| Pagamentos | PagSeguro (PF) / Stripe (CNPJ) / Asaas (candidato — avaliar) |
| Cobrança recorrente | Stripe configurado (conta Inter PJ vinculada em 27/04/2026) |
| MEI | CNPJ ativo · CNAE pendente de atualização · Alvará na prefeitura pendente |

---

## COMO INICIAR UMA SESSÃO

```
São [HORA]. Foco desta sessão: [UMA FRASE].
```

Seguir protocolo:
1. Declarar hora + foco único
2. Um entregável principal por sessão
3. Não mandar print a menos que seja imprescindível
4. Perguntas agrupadas — não uma por mensagem
5. Ao final: produzir relatório de sessão e salvar em `02_ESTRATEGIA/CLAUDE/`

---

---

## HUB — FASE 1 IMPLEMENTADA (24/04/2026)

Quatro Quick Wins aplicados diretamente no `zyllah_hub.html`:

| # | Feature | O que faz |
|---|---|---|
| QW1 | **CFM Gate automático** | `salvarPa()` escaneia tema+notas contra 25 termos proibidos CFM 2.336/2023. Auto-popula campo `cfm_ok`. Bloqueia aprovação com CFM: Não (com confirmação). |
| QW2 | **Auto Follow-up D+3/D+7/D+14** | Ao mudar prospect para `DM enviada`, cria 3 demandas automaticamente com datas e instruções. Toast confirmativo. |
| QW3 | **Auto-score de presença** | Botão "Auto ↺" no modal de prospect calcula nota 0–10 a partir de: site (+2), GMN (+2), seguidores IG (0/1/2/3), LinkedIn (+1), Doctoralia com avaliações (+2). |
| QW4 | **MEI Limite tracker** | Barra de progresso no painel Financeiro mostra projeção anual vs. R$81.000 limite MEI. Alerta no strip quando >70%. |

**Fase 2 (próxima):** triggers Apps Script (verificação diária, resumo semanal, exportação de contexto segunda 07h). WhatsApp via n8n + Waha (única parte que não cabe no Apps Script).

---

## APRESENTAÇÃO PERSONALIZADA POR PROSPECT

`zyllah_apresentacao.html` = base template para apresentações individuais.  
**Fluxo pretendido:** hub detecta reunião confirmada → botão "Gerar apresentação" no card do prospect → Apps Script chama Sonnet com dados do prospect (gaps, especialidade, plano sugerido) → gera HTML personalizado.  
Status: botão `apres-gen-btn` já existe no hub v3. Apps Script precisa do handler `gerarApresentacaoProspect` expandido com o template da apresentação base.

---

## GITHUB — REGRAS DE USO

- **Função:** backup apenas — não é fonte de verdade, não precisa de index
- **Repo público:** `zyllahdigital/zyllah-docs-public` — documentos de referência sem senha
- **Repo privado:** hub, contratos, scripts — nunca subir com chaves de API
- **Convenção de nome:** curto, sem espaços, sem data no nome (ex: `zyllah_brandbook.html`)

---

## DOCS ESTRATÉGICOS — REORGANIZAÇÃO PENDENTE

Os arquivos abaixo precisam ser aglutinados/divididos/renomeados para otimizar como material de apoio real (não apenas referência):

- `zyllah_jornada_cliente_ramos.html`
- `zyllah_mapa_processos_arquitetura.html`
- `zyllah_stack_tecnico_7_papeis.html`
- `zyllah_mapa_riscos_contratuais.html`
- `zyllah_faq_estrategico.html`
- `plano_producao.html`
- `gerador_prompt.html`

**Critério de reorganização:** pergunta "isso muda minha ação hoje?" — se sim, fica como está ou consolida; se não, arquiva ou apaga.

---

*Vault atualizado em 05 de maio de 2026 — Sessão 22 · Estado: pré-receita · sprint de gravação amanhã (06/05) · pipeline de prospecção operacional · runway apertado, plano B mapeado*  
*Próxima atualização: após sprint de gravação ou primeiro cliente ativo*

---

## INTELIGÊNCIA COMPETITIVA

### Grupo Pierre (mapeado em 27/04/2026)
- **Fundador:** Miguel Pierre — criador de conteúdo YouTube/IG sobre gestão de clínicas
- **Modelo:** Ecossistema (marketing + BPO + contabilidade + gestão + tecnologia + educação)
- **Método:** SOMMA (5 pilares: marketing, vendas, gestão pacientes, financeiro, equipe)
- **Cases:** +150%, +300%, +500% de faturamento prometidos
- **Preços:** não listados — consultivo
- **Escala:** contratando Growth Operations Manager R$5–7,5k PJ → operação em volume
- **Relação com Zyllah:** não competição direta — eles são generalistas/consultoria ampla, Zyllah é especializada em presença digital. CFM/CFO/CFP não declarado por eles.
- **Lição:** modelo de autoridade via conteúdo → agência é exatamente o caminho que Guilherme está construindo

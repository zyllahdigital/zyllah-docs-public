# Relatório de Sessão — 04 de maio de 2026

## Foco da sessão
Classificação de features (PESQUISA DE FEATURES.txt) + reflexão sobre arquitetura do sistema + registros de contexto.

---

## Marcos registrados nesta sessão

### 1. Base da agência construída em ~2 meses
A Zyllah Digital tem, em 04/05/2026, uma fundação operacional completa construída em aproximadamente 2 meses:
- Brand (brandbook, identidade visual, tom de voz)
- Hub operacional v3 (Cloudflare + Apps Script + Google Sheets)
- Sistema de 7 papéis (Prospector, Vendedor, Produtor, Gestor, Financeiro, Jurídico, Parceiro)
- Contrato v2.4 (20 cláusulas, 3 anexos de escopo, adendo piloto)
- Infraestrutura técnica (CNPJ, Stripe, Buffer, PandaDoc)
- Zyllah Flow parcialmente construído (Helena, n8n, prompt)
- 25 prospects mapeados
- Conteúdo planejado (sprint de 4 dias pós-chegada de roupas)

Ainda a aprimorar — mas a fundação existe.

### 2. Estrutura de contas Claude
- **1 conta Pro** (Claude Code + Sonnet 4.6)
- **7 contas gratuitas**
- **Diretriz:** Pro reservada para trabalho estratégico, pontual, não funcional. Tarefas funcionais e repetitivas usam contas gratuitas ou Haiku.

---

## Classificação de features (PESQUISA DE FEATURES.txt)

### Úteis agora
| Feature | Ação |
|---|---|
| CapCut Batch Edit (Delete+Ctrl+Z, Compound Clips) | Documentar em `zyllah_producao.html` para sprint de gravação |
| GPT Image 2 vs Nano Banana 2 | Documentar regra de uso em `zyllah_producao.html` (pendência já existia) |
| Claude Design | Usar para apresentações personalizadas por prospect + Design System com brandbook |
| Claude Code + CapCut rough cut (JSON) | Aplicar no Dia 3 do sprint (edição) |
| Adobe Podcast | Usar em todo material gravado pelo A52S |

### Backlog com gatilho
| Feature | Gatilho |
|---|---|
| Fábrica de conteúdo com HeyGen (avatar IA) | Após 1º cliente pagante |
| Maven OS / Chatwoot self-hosted | Após 3 clientes ativos |
| Pipeline edição IA (AutoEdit + Whisper) | Quando edição virar gargalo |
| Skills / Progressive Disclosure no CLAUDE.md | Após 2º cliente ativo |

### Descartados
- Antigravity (já usa Claude Code direto)
- Front Zap (Zyllah Flow já em construção)
- Base 44 (constrói HTML direto)
- Abacus AI (tem Claude Pro)
- GSD (meta-prompting para SaaS, não agência)
- Elementos 3D / loop infinito (não é e-commerce)
- "Empresa no piloto automático" (glossário aspiracional sem aplicação imediata)

---

## Decisões arquiteturais

### Fluxo de prospecção (comentários)
- **Post com texto legível:** copiar legenda diretamente → Claude com contexto do prospect → gerar comentários. Sem gravação, sem Qwen.
- **Story/Reel/TikTok sem legenda:** gravar tela (20–30s) → Qwen → Claude. Fluxo atual está correto para este caso.

### Contexto por prospect
- Criar `prospect_[nome].md` no vault antes de qualquer contato — campos mínimos: gap, último toque, próximo passo, tom preferido, o que não dizer ainda.
- Toda conversa Claude sobre aquele prospect começa com esse arquivo como contexto.

---

## Pendências abertas (mantidas do vault)
Ver CLAUDE.md seção "PENDÊNCIAS — CONSOLIDADO" — nenhuma pendência nova adicionada nesta sessão.

---

*Zyllah Digital · Sessão 22 · 04 de maio de 2026*

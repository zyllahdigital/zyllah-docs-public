# Mapa de Backup — Zyllah Digital

> Onde cada coisa vai. Seguir este mapa antes de criar ou mover qualquer arquivo.

---

## GitHub — Dois repos

### Repo 1: `zyllahdigital/zyllah-docs-public` (PÚBLICO)
O que vai: documentos de referência sem dados pessoais nem chaves.

| Pasta local | O que commitar |
|---|---|
| `01_MARCA/BRANDBOOK/` | `zyllah_brandbook.html` |
| `01_MARCA/LOGOTIPOS/` | SVGs e PNGs das logos |
| `02_ESTRATEGIA/ANALISES/` | Análises estratégicas, ZYLLAH_LINKS.md |
| `03_VENDAS/MATERIAIS/` | Apresentação, material de visita, objeções |
| `03_VENDAS/SCRIPTS/` | Scripts de reunião e prospecção |
| `04_CONTEUDO/` | PRODUCAO.md, planer.html, calendários |
| `ZyllahOS/03-CONTEXT/` | icp.md, tom-de-voz.md, estrategia.md |
| `ZyllahOS/04-SKILLS/` | Todas as skills (sem dados pessoais) |
| `ZyllahOS/README.md` | — |
| `README.md`, `CLAUDE.md` | — |

**Nunca commitar:** nomes de clientes/prospects reais, dados financeiros, contratos assinados, chaves de API.

---

### Repo 2: `zyllahdigital/zyllah-ops` (PRIVADO — criar)
O que vai: ferramentas operacionais e infraestrutura.

| Pasta local | O que commitar |
|---|---|
| `02_ESTRATEGIA/PROCESSOS/zyllah_hub.html` | Hub operacional |
| `02_ESTRATEGIA/PROCESSOS/script_conector_hub.gs` | GAS backend |
| `02_ESTRATEGIA/PROCESSOS/manual_hub_v10.html` | Manual do hub |
| `08_TECNICO/FLOW/` | n8n workflow, docker-compose, README |
| `08_TECNICO/INFRAESTRUTURA/hub_index_upload_seguro/index.html` | Deploy Cloudflare |
| `ZyllahOS/prospectar.py` | Pipeline de prospecção |
| `ZyllahOS/prospectar.bat` | Launcher |

**Nunca commitar:** `.env`, `.claude/`, dados de clientes reais, planilha com prospects.

---

## Google Drive — Backup completo

Pasta raiz: `Drive/Zyllah Digital/`

```
Zyllah Digital/
  📁 ZYLLAH_ZYLLAH/          ← Espelho de C:\Users\Guilherme\Desktop\ZYLLAH\ZYLLAH\
      01_MARCA/
      02_ESTRATEGIA/
      03_VENDAS/
      04_CONTEUDO/
      05_PRODUCAO_AV/        ← Inclui vídeos (Drive aguenta, GitHub não)
      06_CLIENTES/
      07_ONBOARDING/
      08_TECNICO/
      09_FINANCEIRO/
      10_JURIDICO/
  
  📁 ZyllahOS/               ← Espelho de C:\Users\Guilherme\Documents\ZyllahOS\
      03-CONTEXT/
      04-SKILLS/
      05-PROJECTS/
      fundador/
```

**O que NÃO vai para Drive:** `.env`, `.claude/`, `node_modules/`, arquivos de cache.

---

## Frequência de backup

| Quando | O quê | Para onde |
|---|---|---|
| Após cada sessão Claude longa | CLAUDE.md + relatório da sessão | Git commit + Drive |
| Após cada sprint de produção | Vídeos editados + posts finalizados | Drive |
| Semanalmente (domingo) | Tudo que mudou | Drive sync manual |
| Após mudança crítica no hub | hub.html + script_conector_hub.gs | Git (ops) + Drive |

---

## Convenções globais

**Nomes de arquivo:**
- Sem espaços → usar underline: `script_conector_hub.gs`
- Sem acentos em nomes de PASTA → usar sem acento: `10_JURIDICO/`
- Prefixo `zyllah_` em documentos operacionais HTML: `zyllah_hub.html`
- Versão só quando necessário: `_v2`, `_v10` — não usar data no nome

**Nomes de commit Git:**
- Primeira linha: ação + contexto (máx 72 chars)
- Tipo: `feat:`, `fix:`, `docs:`, `refactor:`
- Exemplo: `feat: botão Comentar no card de prospect + modal com skills`

---

*Criado em 05/05/2026 · Revisar quando um novo repo for criado ou a estrutura mudar*

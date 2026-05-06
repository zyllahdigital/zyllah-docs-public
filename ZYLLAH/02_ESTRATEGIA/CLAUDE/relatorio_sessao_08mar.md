# Relatório de Sessão — Zyllah Digital
**Data:** Domingo, 08 de março de 2026
**Operador:** Guilherme Caetano

---

## ✅ Concluído nesta sessão

### Automação n8n — CRM com IA
Construído do zero um fluxo completo de automação:

**Webhook → HTTP Request (Claude IA) → Edit Fields (Set) → Google Sheets**

#### O que o fluxo faz:
1. Recebe dados de um lead via webhook (nome, telefone, mensagem)
2. Envia a mensagem para a API da Anthropic (Claude Haiku)
3. A IA classifica o lead como **alto, médio ou baixo** interesse
4. A IA gera uma **resposta sugerida** personalizada
5. Salva tudo automaticamente no Google Sheets — 5 colunas: nome, telefone, mensagem, classificacao, resposta_sugerida

#### Infraestrutura configurada:
- **n8n** instalado permanentemente via `npm install -g n8n`
- **Google Cloud Console** configurado — projeto Zyllah n8n
- **Google Sheets API** e **Google Drive API** ativadas
- **OAuth2** configurado e autenticado
- **Planilha Zyllah Leads** criada no Google Sheets
- **API Anthropic** conectada — $5 de créditos adicionados
- **Avast** desativado — estava bloqueando porta 443

#### Problemas resolvidos:
- Erro de certificado SSL no Windows — resolvido desativando Avast
- Campos com `=` sendo interpretados como fórmula no Sheets — resolvido com nó Edit Fields (Set) + referências simples `$json.campo`
- Webhook expirando em modo teste — resolvido publicando o workflow

---

### Estratégia de Prospecção
- Identificados primeiros prospects: **Thayara** (fisioterapeuta) e **Mônica** (psicóloga)
- Decisão: abordar via **pastor Lucas** (marido da Thayara) — relação mais natural
- Proposta: projeto piloto gratuito/simbólico em troca de depoimento e indicações
- Arquivo `zyllah_thayara.html` revisitado — mensagens de abordagem prontas

### LinkedIn — Métricas
Post publicado há 4 dias:
- **127 impressões**
- **50 usuários alcançados**
- Público predominante: São Paulo (22,8%) + Rio (21,1%), nível sênior (35%)

### Postagens programadas confirmadas
| Data | Horário | Canal | Conteúdo |
|------|---------|-------|----------|
| Sex 06/03 | 18h10 | Instagram | Post apresentação Zyllah |
| Seg 09/03 | 12h00 | Instagram | Bastidores — foto abas de pesquisa |
| Ter 10/03 | 18h00 | LinkedIn pessoal | Post ciclo do médico |
| Qua 11/03 | — | Instagram | Carrossel 3 sinais |

---

## 📁 Infraestrutura ativa
- **n8n:** `n8n start` no CMD → localhost:5678
- **Webhook URL produção:** `http://localhost:5678/webhook/zyllah-lead`
- **Planilha:** Google Sheets — Zyllah Leads
- **API:** Anthropic Claude Haiku — $5 créditos

---

## ⏳ Pendente
- Abordar pastor Lucas sobre Thayara
- Conectar webhook a um formulário real no site ou WhatsApp
- Configurar n8n para iniciar automaticamente com o Windows
- Stories — estratégia de produção otimizada (pendente de discussão)
- Upload do `index.html` e `zyllah_material_visita.html` no GitHub

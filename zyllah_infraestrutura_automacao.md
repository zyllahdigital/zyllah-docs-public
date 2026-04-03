# Infraestrutura de Automação Zyllah Digital
## Documento Técnico de Referência
**Versão 1.0 · Março 2026 · Guilherme Caetano**

---

## Visão Geral

Este documento descreve a arquitetura, o método de construção e as decisões técnicas da infraestrutura de automação da Zyllah Digital. Foi construída do zero em uma única sessão e serve como base para replicar ou expandir o sistema para novos clientes.

O objetivo do sistema é: **receber uma mensagem de lead, analisá-la com IA e salvar os dados classificados automaticamente em uma planilha — sem intervenção humana.**

---

## Arquitetura do Fluxo

```
[Lead envia mensagem]
        ↓
   [Webhook n8n]
        ↓
 [HTTP Request → API Anthropic]
        ↓
   [Edit Fields (Set)]
        ↓
   [Google Sheets]
```

### Descrição de cada nó

**1. Webhook**
- Tipo: `n8n-nodes-base.webhook`
- Método: POST
- Path: `zyllah-lead`
- URL de produção: `http://localhost:5678/webhook/zyllah-lead`
- Recebe: `nome`, `telefone`, `mensagem`

**2. HTTP Request (Claude IA)**
- Tipo: `n8n-nodes-base.httpRequest`
- URL: `https://api.anthropic.com/v1/messages`
- Método: POST
- Headers (JSON):
```json
{
  "x-api-key": "SUA_CHAVE_SK-ANT",
  "anthropic-version": "2023-06-01",
  "content-type": "application/json"
}
```
- Body (JSON com expressão):
```json
={
  "model": "claude-haiku-4-5-20251001",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Você é um assistente da Zyllah Digital, agência de presença digital para profissionais de saúde. Analise a mensagem abaixo de um lead e retorne APENAS um JSON com dois campos: 'classificacao' (alto, medio ou baixo) e 'resposta_sugerida' (mensagem curta para enviar ao lead). Mensagem: {{ $('Webhook').item.json.body.mensagem }}"
    }
  ]
}
```

**3. Edit Fields (Set)**
- Tipo: `n8n-nodes-base.set`
- Finalidade: processar e limpar os dados antes de gravar no Sheets
- Todos os campos como tipo **String**
- Campos configurados:

| Campo | Expressão |
|-------|-----------|
| nome | `{{ $('Webhook').item.json.body.nome }}` |
| telefone | `{{ $('Webhook').item.json.body.telefone }}` |
| mensagem | `{{ $('Webhook').item.json.body.mensagem }}` |
| classificacao | `={{ $('HTTP Request').item.json.content[0].text.replace(/```json\n?\|\n?```/g, '').trim().match(/"classificacao":\s*"([^"]+)"/)[1] }}` |
| resposta_sugerida | `={{ $('HTTP Request').item.json.content[0].text.replace(/```json\n?\|\n?```/g, '').trim().match(/"resposta_sugerida":\s*"([^"]+)"/)[1] }}` |

**4. Google Sheets (Append Row)**
- Tipo: `n8n-nodes-base.googleSheets`
- Operação: `append`
- Mapping: defineBelow (manual)
- Campos no modo **Expression** com referências simples:

| Campo Sheets | Expressão n8n |
|-------------|---------------|
| nome | `={{ $json.nome }}` |
| telefone | `={{ $json.telefone }}` |
| mensagem | `={{ $json.mensagem }}` |
| classificacao | `={{ $json.classificacao }}` |
| resposta_sugerida | `={{ $json.resposta_sugerida }}` |

> ⚠️ **Importante:** Sempre usar o nó Set antes do Sheets. Expressões com funções longas (`.replace()`, `.match()`) aplicadas diretamente no Sheets causam o erro de `=` sendo interpretado como fórmula.

---

## Infraestrutura de Suporte

### n8n
- **Instalação:** `npm install -g n8n`
- **Inicialização:** `n8n start` no CMD
- **Interface:** `http://localhost:5678`
- **Modo:** Self-hosted no Windows

### Google Cloud
- **Projeto:** Zyllah n8n
- **APIs ativadas:** Google Sheets API + Google Drive API
- **Autenticação:** OAuth2
- **Tela de consentimento:** Externo, com email do operador como usuário de teste

### Anthropic API
- **Modelo:** claude-haiku-4-5-20251001 (mais barato, ideal para classificação)
- **Chave:** criada em console.anthropic.com → API Keys
- **Créditos:** mínimo $5 para começar
- **Custo estimado:** frações de centavo por interação

---

## Problemas Encontrados e Soluções

| Problema | Causa | Solução |
|----------|-------|---------|
| Webhook não registrado | Modo teste expira rápido | Publicar o workflow antes de testar |
| `curl: Failed to connect port 443` | Avast bloqueando HTTPS | Desativar proteção web do Avast |
| `Error 403: access_denied` | Email não autorizado no OAuth | Adicionar email em Público-alvo → Usuários de teste no Google Cloud |
| `Column names were updated` | Nome de coluna mudado após setup | Deletar e recriar o nó Google Sheets do zero |
| `=valor` interpretado como fórmula no Sheets | n8n adiciona `=` em expressões longas | Usar nó Set intermediário + referências simples `$json.campo` no Sheets |
| IA retorna JSON com ```json ``` | Comportamento padrão do modelo | Usar `.replace()` + `.match()` para extrair valores |

---

## Como Replicar para um Novo Cliente

1. **Criar planilha** no Google Sheets com colunas: `nome`, `telefone`, `mensagem`, `classificacao`, `resposta_sugerida`
2. **Duplicar o workflow** no n8n — botão "Duplicate" no menu do workflow
3. **Atualizar o path do webhook** para o nome do cliente (ex: `cliente-joao`)
4. **Atualizar o prompt** no HTTP Request com o contexto do cliente
5. **Reconectar o Google Sheets** para apontar para a nova planilha
6. **Publicar** o workflow
7. **Testar** com curl usando a nova URL de produção

---

## Como Testar o Fluxo

```bash
curl -X POST http://localhost:5678/webhook/zyllah-lead \
  -H "Content-Type: application/json" \
  -d "{\"nome\": \"Dr. João Silva\", \"telefone\": \"22999999999\", \"mensagem\": \"Quero saber mais sobre os serviços\"}"
```

Resposta esperada: `{"message":"Workflow was started"}`

---

## Próximas Evoluções

- **Notificação por email** — quando lead alto chegar, enviar alerta imediato
- **Integração WhatsApp** — via Z-API ou Evolution API (~R$50/mês)
- **Formulário no site** — substituir o curl por formulário real em `zyllah.com.br`
- **n8n no boot** — configurar para iniciar automaticamente com o Windows
- **Dashboard** — Google Sheets com gráficos de leads por classificação e período

---

*Zyllah Digital · Documento interno · Uso operacional*

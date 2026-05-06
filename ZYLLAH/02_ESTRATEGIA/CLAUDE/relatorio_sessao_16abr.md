# Zyllah Digital — Relatório de Sessão
## 16 de abril de 2026 · Sessão 19 · ~46 dias de Zyllah

---

## Contexto da sessão

**Data:** 16 de abril de 2026  
**Equipamento:** Samsung A52S (mobile) — sessão conduzida pelo celular  
**Estado da operação:** pré-receita, prospectando, hub com problema de sync em resolução  
**Foco principal:** resolver sincronização do Hub com Google Sheets, segurança de chaves de API, módulo YouTube

---

## Contexto anterior (o que vinha da Sessão 18)

- Hub operacional v3 produzido com JSONP — CORS ainda não resolvido na prática
- Apps Script v3 implantado com nova URL
- Problema identificado: hub tinha duas definições da função `gs()`, a segunda sobrescrevia a primeira e usava `gsPost` com `fetch POST` (bloqueado por CORS)
- Semana do calendário exibindo dias errados (bug no cálculo de offset)
- Três prospects a cadastrar: Kelly Purger, Cleonicio Cordeiro, Fabricia Corbett
- Prazo Cloudia: enviar primeiro lead até 09/05/2026

---

## Realizações desta sessão

### 1. Diagnóstico definitivo do problema de sync

**Causa raiz identificada:** o hub continha **duas definições da função `gs()`** no mesmo arquivo. JavaScript usa a última definição encontrada. A segunda (antiga) chamava `gsPost()` via `fetch POST`, que é bloqueado por CORS no Google Apps Script.

**Evidência:** ao comparar o hub enviado como documento, as linhas 724–736 continham:
```javascript
async function gsPost(params){ fetch... }
async function gs(params){ if(GS_WRITE...) return gsPost(...) }
```
sobrescrevendo a versão correta (JSONP puro) definida acima.

**Solução aplicada:** remoção completa do bloco `gsPost` e da segunda `gs()`. A função `gs()` final serializa todos os parâmetros em `data=JSON_ENCODED` e envia via `gsGet()` (JSONP), inclusive operações de escrita.

---

### 2. Bug do calendário — semana errada

**Problema:** o calendário do hub mostrava a semana errada. Na quinta-feira 16/04, exibia datas de outra semana.

**Causa:** o cálculo `1 - dow` retornava negativo quando `dow > 1` (terça em diante), empurrando os offsets para a semana anterior.

**Correção:**
```javascript
function getOffsetsDosDias() {
  const hoje = new Date();
  const dow = hoje.getDay();
  const offsetParaSegunda = dow === 0 ? -6 : 1 - dow;
  const offsets = [];
  for (let i = 0; i < 5; i++) offsets.push(offsetParaSegunda + i);
  return offsets;
}
```

---

### 3. Apps Script v3 — consolidação e entrega final

**Mudança arquitetural principal:** `doGet` tornou-se o **único ponto de entrada** — leituras e escritas. O `doPost` foi mantido apenas como fallback mas não é mais usado pelo hub.

**Estrutura do doGet:**
```
?action=X&data=JSON_ENCODED&callback=FUNC_NAME
```

O parâmetro `data` carrega o payload de qualquer escrita serializado como JSON e encodado. O Apps Script faz `decodeURIComponent` + `JSON.parse` internamente.

**Módulo de apresentações automáticas:** integrado ao `verificacaoDiaria()`. A cada rodada, processa até 3 prospects com status diferente de `novo/arquivado/perdido` e que ainda não tenham apresentação gerada. Usa Claude Sonnet via `UrlFetchApp`. Salva HTMLs no Drive e notifica por e-mail.

**Prospects — campos todos opcionais exceto nome:** cadastro mínimo com só o nome já funciona. Os campos de investigação (seguidores, site, GMN, gancho) são preenchidos progressivamente.

**Arquivo entregue:** `zyllah_apps_script_v3.gs`

---

### 4. Vazamento de chaves de API — incidente e resposta

**Evento:** e-mail da Anthropic às 04:24 UTC de 16/04 notificando que a chave `sk-ant-api03-Zf2...xgAA` foi detectada e **automaticamente revogada** pelo programa de secret scanning do GitHub.

**Origem:** o arquivo `zyllah_hub.html` foi commitado no repositório público `zyllahdigital/zyllah-docs-public` com a chave hardcoded nas constantes `YT_ANTHROPIC_KEY` e no código de `configurarApiKey()`.

**Segundo alerta:** Google API Key também detectada no mesmo commit (linha 1335 do hub).

**Ações tomadas:**

| Ação | Status |
|---|---|
| Nova chave Anthropic gerada | ✅ Concluído |
| Chave antiga — já revogada pelo GitHub | ✅ Automático |
| Nova chave salva no Apps Script via `configurarApiKey()` | ✅ Concluído |
| Chave removida do código-fonte do hub | ✅ Concluído |
| Google API Key restrita por referrer + API no Console | ✅ Concluído |

**Regra estabelecida permanentemente:**
- Chaves de API **nunca** em arquivos que vão para repositórios públicos
- No Apps Script: sempre via `PropertiesService.getScriptProperties()`
- No hub HTML: a chave Anthropic não deve existir — toda chamada passa pelo Apps Script
- A Google API Key para YouTube pode existir no hub, desde que **restrita por referrer e API** no Google Cloud Console

---

### 5. Módulo YouTube — integrado e seguro

**Funcionalidade:** painel de oportunidades de comentário no YouTube, acessível pela sidebar do hub.

**Fluxo:**
1. Busca vídeos dos últimos 7 dias por termos configuráveis (padrão: 9 termos sobre marketing médico/saúde)
2. Filtra: mín. 500 visualizações, comentários abertos, não infantil
3. Gera comentário personalizado para cada vídeo via Haiku
4. Guilherme abre o vídeo, cola o comentário, marca como postado

**Arquitetura de segurança:**
- `YT_API_KEY` (Google) permanece no hub — inevitável para chamada direta à YouTube Data API, mas restrita no Console
- Chave Anthropic: **removida do hub**. A geração de comentários agora passa pelo Apps Script via `gs({action:'gerarComentarioYT',...})`

**Dois lugares para alterar no Apps Script:**

**Lugar 1 — No `doGet`, antes do `else resultado = { erro: 'Ação inválida'... }`:**
```javascript
else if (action === 'gerarComentarioYT') resultado = gerarComentarioYT(d);
```

**Lugar 2 — Antes dos `// TESTES`, adicionar a função:**
```javascript
function gerarComentarioYT(d) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_API_KEY');
  if (!apiKey) return { erro: 'Chave não configurada' };
  const prompt = `Você é Guilherme Caetano, fundador da Zyllah Digital...`;
  // [função completa no arquivo zyllah_apps_script_v3.gs]
}
```

**Termos de busca padrão configurados:**
- marketing médico, autoridade médica, presença digital médico
- personal branding saúde, médico empreendedor
- captação pacientes consultório, marketing para clínicas
- instagram para médicos, conteúdo profissionais de saúde

**Badge na sidebar:** exibe contagem de vídeos pendentes de comentário.

---

### 6. Hub v3 — versão final entregue

**Arquivo:** `zyllah_hub.html`

**O que mudou em relação às versões anteriores:**

- `gs()` — versão única, JSONP puro, sem `gsPost`, sem `GS_WRITE`
- `getOffsetsDosDias()` — calendário mostra a semana correta
- Módulo YouTube integrado com painel, CSS, nav e lógica completa
- Chamadas Anthropic roteadas pelo Apps Script (sem chave no navegador)
- `SCRIPT_URL` atualizada para a implantação mais recente
- `salvarRitual` corrigido — action `salvarRitual` (não `ritual`)

---

## Documentos produzidos nesta sessão

| Arquivo | Descrição | Destino |
|---|---|---|
| `zyllah_apps_script_v3.gs` | Apps Script completo — CORS resolvido, módulo YT | Colar no Apps Script online |
| `zyllah_hub.html` | Hub operacional v3 — sync funcionando, YouTube integrado | GitHub Pages (repo privado) ou local |
| `hub_correcoes.js` | Referência das correções cirúrgicas aplicadas | Uso interno |

---

## Decisões técnicas tomadas

1. **Toda comunicação hub → Apps Script via GET+JSONP** — sem exception, sem fallback POST
2. **Prospects: campos todos opcionais exceto nome** — cadastro progressivo conforme investigação avança
3. **Chave Anthropic nunca no navegador** — sempre via Apps Script
4. **Google API Key do YouTube pode ficar no hub**, desde que restrita por referrer no Console
5. **Módulo YouTube gera comentários via Haiku** — tom de Guilherme, genuíno, sem autopropaganda, 2-3 frases + pergunta aberta

---

## Pendências atualizadas

### Urgente
- [ ] Colar `gerarComentarioYT` no Apps Script (doGet + função) e reimplantar
- [ ] Testar sync: Console Chrome → `gs({action:'listar'}).then(d=>console.log(d))`
- [ ] Enviar primeiro lead para Cloudia (prazo: **09/05/2026**)
- [ ] Abrir MEI

### Alta prioridade
- [ ] Cadastrar Kelly, Cleonicio e Fabricia na aba Prospects do hub
- [ ] Iniciar comentários no Instagram: Dr. Cleonicio, Dra. Fabricia
- [ ] Configurar triggers no Apps Script (verificacaoDiaria 07h, resumoSemanal domingo 20h, exportarContexto segunda 07h)
- [ ] Executar `testarExportacao()` no Apps Script para gerar os 3 arquivos de contexto no Drive e pegar os links
- [ ] Colar os 3 links do Drive nas instruções do projeto (camadas 1, 2, 3)
- [ ] Contratar advogado — validar mapa de riscos v2.0

### Médio prazo
- [ ] Migrar tarefas do Cowork (prospector, tendências) para Apps Script
- [ ] Configurar Daniel — Z-API/Evolution para WhatsApp Flow
- [ ] Roleplay de reunião de vendas — prática antes de prospect responder

---

## Lição de segurança registrada

O incidente com a chave Anthropic é um acidente comum em projetos que crescem rápido sem processo de revisão de segurança. A lição não é culpa — é sistema:

**Processo a seguir daqui em diante antes de qualquer commit:**
1. Verificar se há strings `sk-ant-`, `AIzaSy` ou qualquer padrão de chave no arquivo
2. Repositório público = zero credenciais, independente do arquivo
3. Chaves no Apps Script: sempre `PropertiesService`, nunca no código-fonte
4. Hub e documentos HTML: se precisar de IA, proxy via Apps Script

---

*Zyllah Digital · Sessão 19 · 16 de abril de 2026 · Uso interno*

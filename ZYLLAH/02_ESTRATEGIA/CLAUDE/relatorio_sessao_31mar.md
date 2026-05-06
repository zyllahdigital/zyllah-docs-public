# Zyllah Digital — Relatório de Sessão
## 31 de março de 2026 — Sessão 12

---

## Situação geral

Guilherme em Nova Friburgo. Sessão de alta produção — foco total em conteúdo audiovisual, assets YouTube/TikTok e planejamento de produção em série. Três prospects (@dralidiamagliano, @drfabricioayres, @dramarinasampaio) em silêncio desde 25/03. Aguardando resposta orgânica.

---

## O que foi produzido nesta sessão

### Assets YouTube — versão final corrigida

| Arquivo | Descrição |
|---|---|
| `yt_thumb_01_google.html` | Miniatura Ep. 01 — logo limpa, mockups maiores |
| `yt_thumb_02_criador.html` | Miniatura Ep. 02 — split screen câmera |
| `yt_thumb_03_cfm.html` | Miniatura Ep. 03 — fundo médica profissional, selo CFM legível |
| `yt_thumb_04_filtro.html` | Miniatura Ep. 04 — fundo mais escuro, mais contraste |
| `yt_thumb_05_agencias.html` | Miniatura Ep. 05 — foto Guilherme, logo limpa |
| `yt_capa_canal.html` | Capa do canal YouTube 2048×1152 — logo sem retângulo |
| `capa_playlist_serie1.html` | Capa playlist Série Zyllah 1280×720 |
| `capa_playlist_serie2.html` | Capa playlist Análise Crítica 1280×720 — tom vermelho |

**Correção principal:** logo extraída com canal alpha (fundo preto removido via Python), bordas brancas cortadas. Logo agora flutua limpa sobre qualquer fundo.

### Roteiros YouTube — série completa

| Arquivo | Vídeo | Formato | Câmera |
|---|---|---|---|
| `roteiro_youtube_v1.html` | V1 — O que o Google encontra | Voz over + tela | Não |
| `roteiro_youtube_v2.html` | V2 — Por que médico não precisa virar criador | Câmera | Sim |
| `roteiro_youtube_v3.html` | V3 — O que o CFM proíbe | Voz over + tela | Não |
| `roteiro_youtube_v4.html` | V4 — Presença que filtra paciente | Câmera | Sim |
| `roteiro_youtube_v5.html` | V5 — Por que agências entregam o mesmo | Câmera + tela | Sim |

### Série 2 — Análise Crítica

| Arquivo | Descrição |
|---|---|
| `yt_s2_thumb_01_cfm.html` | Miniatura S2 Ep. 01 — post fictício com carimbo PROIBIDO |
| `yt_s2_thumb_02_feed.html` | Miniatura S2 Ep. 02 — dois feeds idênticos com símbolo = |
| `yt_s2_thumb_03_seguidores.html` | Miniatura S2 Ep. 03 — 10k seguidores / 0 pacientes |

**Temas aprovados:**
- S2 #01 — O post que violou o CFM (e ninguém percebeu)
- S2 #02 — Por que esse feed parece de qualquer um
- S2 #03 — O perfil com 10k seguidores e 0 pacientes novos
- S2 #04 e #05 — em fila (A bio que afasta o paciente certo / O site que não aparece no Google)

### Assets de tela — para gravação

| Arquivo | Uso |
|---|---|
| `asset_tela_feeds_genericos.html` | V5 — dois feeds idênticos lado a lado |
| `asset_tela_erros_cfm.html` | V3 e S2#01 — posts proibidos + corretos com infração identificada |
| `asset_tela_comparativo.html` | V3 e V5 — feed ruim vs. feed bom com diagnóstico |

### Plano de produção em série

**Arquivo:** `plano_producao_serie.html`

6 setups organizados para uma sessão de 2h+:

| Setup | Tipo | Conteúdo | Tempo |
|---|---|---|---|
| A | Voz over (off) | V1 + V3 + S2#01 | ~35 min |
| B | Câmera Roupa 1 | V2 + V4 | ~45 min |
| C | Câmera Roupa 2 | V5 + Shorts autônomos | ~35 min |
| D | Tela gravada | Cenas V1 + V3 + V5 + S2 | ~30 min |
| E | Texto animado | 6 Shorts sem voz | ~20 min |
| F | B-roll | Imagens geradas (fora da sessão) | — |

**28 falas catalogadas** com marcação de recorte para Short/Reel em cada uma.
**20+ Shorts/Reels derivados** identificados com plataforma prioritária.

### TikTok — assets de perfil

| Arquivo | Dimensão |
|---|---|
| `tiktok_foto_perfil.html` | 200×200px — foto Guilherme |
| `tiktok_capa_perfil.html` | 1080×1920px — banner vertical, mesmo padrão YouTube |

**Handle:** @zyllahdigital

### Ferramenta interna

**Arquivo:** `gerador_prompt.html`

Gerador interativo de metadados. 4 campos + checkboxes de plataforma → prompt completo para o Gemini. Gera de uma vez: título YouTube, descrição, tags, legenda Instagram, hashtags, legenda LinkedIn, legenda TikTok, legenda Shorts. Já inclui todas as regras CFM e posicionamento Zyllah.

**8 vídeos para preencher** (termos já extraídos dos roteiros):
- V1 a V5 da Série 1
- S2 #01, #02, #03 da Série 2

---

## Decisões estratégicas

### Duas séries no canal YouTube
- **Série 1 — "Série Zyllah"** (5 vídeos): educativa, autoridade progressiva
- **Série 2 — "Análise Crítica"** (começa com 3): polêmica controlada, perfis fictícios, formato diagnóstico

### ElevenLabs e HeyGen
- **ElevenLabs (~$22/mês):** recomendado — clona voz para todos os vídeos de voz over. Vale para o volume desta produção.
- **HeyGen (~$29/mês):** condicional — só se câmera for gargalo real. Caso contrário, gravar ao vivo é mais autêntico.

### Organização de arquivos — estrutura definida
```
ZYLLAH_PRODUCAO_2026/
  RAW/ → A_OFF / B_CAMERA_ROUPA1 / C_CAMERA_ROUPA2 / D_TELA / E_TEXTO
  EDITADO/ → YOUTUBE_SERIE1 / YOUTUBE_SERIE2 / REELS / SHORTS / LINKEDIN
  ASSETS/ → CAPAS_THUMBNAILS / LOGOS / TRILHAS
```
Nomenclatura de arquivo raw: **setup + número da fala + vídeo destino + take**
Ex: `B2_V2_ciclo_abandono_take1.mp4`

Controle de status: Google Sheets simples com colunas Gravado / Editado / Publicado / Plataforma / Link.

---

## Trilhas definidas por setup

| Setup | Trilha | Fonte |
|---|---|---|
| A (off) + D (tela) | Dark academia ambient — piano + strings suave | YouTube Audio Library: "Contemplative" |
| B + C (câmera) | Instrumental minimalista — guitar ou piano solo (pós-edição) | YouTube Audio Library: "Corporate Minimal" |
| E (texto animado) | Dark academia ambient — volume mais alto sem voz competindo | Mesma família do Setup A |

---

## Pendências carregadas (alta prioridade)

- [ ] **Roleplay da reunião de vendas** — gargalo principal, ainda não realizado
- [ ] Postar reel "O Peso da Saúde" — pendente desde 28/03
- [ ] Subir arquivos no GitHub
- [ ] Instalar assinatura de e-mail no Gmail
- [ ] Adicionar logo como foto principal no Google Meu Negócio
- [ ] Atualizar site zyllah.com.br

## Pendências desta sessão

- [ ] Gravar cena 04 do reel "O Peso da Saúde" (consultório — refazer com prompt Gemini)
- [ ] Criar conta TikTok @zyllahdigital e configurar perfil com assets gerados
- [ ] Avaliar compra ElevenLabs por 1 mês
- [ ] Subir no projeto: todos os roteiros V2–V5, assets de tela, plano de produção, gerador de metadados, assets TikTok
- [ ] Iniciar planilha de controle de produção no Google Sheets

---

## Nota sobre perda de contexto

Houve perda de conteúdo de conversa anterior. Informações sobre AnaLívia e Mônica (além do registro de Mônica como psicóloga/prospect em 08/03) não foram recuperadas. E-mail enviado ao suporte Anthropic. Manter hábito de salvar relatório ao final de cada sessão produtiva.

---

*Zyllah Digital · Uso interno · 31 de março de 2026*

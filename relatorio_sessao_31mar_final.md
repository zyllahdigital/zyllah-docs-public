# Zyllah Digital — Relatório de Sessão
## 31 de março de 2026 — Sessão 12 (continuação)

---

## Contexto

Sessão longa de alta produção. Foco total em planejamento audiovisual, assets visuais e ferramentas de suporte ao editor. Nenhuma gravação realizada — tudo planejado e documentado para execução nos próximos 3 dias.

---

## Decisões estratégicas desta sessão

### Ferramentas — decisão final
- **ElevenLabs:** descartado. Guilherme grava a voz ao vivo.
- **HeyGen:** descartado. Guilherme aparece em câmera ao vivo.
- **Custo de produção: R$ 0.** Stack: Samsung A52S + CapCut + OBS + Gemini gratuito.

### Estrutura do vídeo longo YouTube (padrão para todos os 8 vídeos)
```
[3s câmera abertura] → [conteúdo: tela/cards/voz over] → [20s end screen limpo] → [3s câmera CTA]
```
- End screen 20s: fundo escuro limpo — YouTube sobrepõe cards automaticamente
- Duas timelines por vídeo: 16:9 YouTube + 9:16 Reels via CapCut Auto Reframe
- PiP descartado — substituído por cards animados e B-roll

### HeyGen — cancelado após análise de risco
- 15 créditos era margem insuficiente para 8 vídeos longos com PiP
- Decisão mais econômica e autêntica: câmera ao vivo

### Cards animados — decisão de fonte
- Barlow Condensed aprovado para títulos de impacto
- Argumento: legibilidade superior em vídeo curto no celular vs. Cormorant Garamond
- Cormorant e Jost mantidos para elementos secundários (fiel ao brandbook)

### Cards — problema de F11 identificado e corrigido
- Arquivo único com navegação: F11 mostraria nav + labels + fundo
- Solução: cada card virou arquivo HTML individual isolado
- Versões 16:9 e 9:16 separadas — sem conversão forçada, sem barras pretas

### Dimensões por plataforma
| Formato | Dimensão | Plataforma |
|---|---|---|
| Vertical | 1080×1920 (9:16) | Reels, TikTok, Shorts, Stories |
| Quadrado | 1080×1080 (1:1) | LinkedIn feed, Instagram estático |
| Horizontal | 1920×1080 (16:9) | YouTube vídeo longo, tela gravada |

### Cross-promotion — implementado
- Site atualizado com 4 redes no footer: Instagram, TikTok, YouTube, LinkedIn
- Links reais com target="_blank"
- Bloco fixo de links para descrição de todos os vídeos YouTube definido

---

## Arquivos produzidos nesta sessão

### Planos de produção
| Arquivo | Versão | Descrição |
|---|---|---|
| `plano_producao_v3_final.html` | v3 — Final | Sem HeyGen/ElevenLabs. 5 setups, 45+ peças, R$0 custo |

### Cards animados — 14 arquivos individuais
| Arquivo | Fundo | Duração |
|---|---|---|
| `card_E1_seguidores_16x9.html` + `_9x16.html` | Ink | 8s |
| `card_E2_consistencia_16x9.html` + `_9x16.html` | Ink | 12s |
| `card_E3_cfm_sancao_16x9.html` + `_9x16.html` | **Verde croma** | 12s |
| `card_E4_ciclo_16x9.html` + `_9x16.html` | **Verde croma** | 20s |
| `card_E5_cfm_resolucao_16x9.html` + `_9x16.html` | Ink | 8s |
| `card_E6_presenca_16x9.html` + `_9x16.html` | **Verde croma** | 12s |
| `card_E7_curtidas_16x9.html` + `_9x16.html` | Ink | 8s |

**Como usar:** abrir no Chrome → F11 → gravar com OBS. Cards verdes: editor aplica chroma key e coloca B-roll por trás.

### Prompts Gemini
| Arquivo | Conteúdo |
|---|---|
| `prompts_gemini.html` | 12 prompts com botão Copiar — Instagram (5), Google (3), LinkedIn (2), B-roll (6) |

### Gerador de metadados
| Arquivo | Conteúdo |
|---|---|
| `gerador_prompt.html` | 4 campos + checkboxes de plataforma → prompt completo para Gemini |

**8 vídeos para preencher:**
- V1 a V5 — Série Zyllah
- S2 #01, #02, #03 — Análise Crítica

### Site
| Arquivo | Alteração |
|---|---|
| `index.html` | Footer atualizado: coluna "Redes" com Instagram, TikTok, YouTube, LinkedIn com links reais |

### TikTok — assets de perfil
| Arquivo | Dimensão |
|---|---|
| `tiktok_foto_perfil.html` | 200×200px |
| `tiktok_capa_perfil.html` | 1080×1920px |

### Roteiros YouTube — recriados
| Arquivo | Vídeo |
|---|---|
| `roteiro_youtube_v2.html` | Por que médico não precisa virar criador |
| `roteiro_youtube_v3.html` | O que o CFM proíbe |
| `roteiro_youtube_v4.html` | Presença que filtra paciente |
| `roteiro_youtube_v5.html` | Por que agências entregam o mesmo |

### Thumbnails e capas
| Arquivo | Descrição |
|---|---|
| `capa_playlist_serie1.html` | Playlist Série Zyllah — ink/ouro |
| `capa_playlist_serie2.html` | Playlist Análise Crítica — vermelho |
| `yt_s2_thumb_01_cfm.html` | Miniatura S2 Ep.01 |
| `yt_s2_thumb_02_feed.html` | Miniatura S2 Ep.02 |
| `yt_s2_thumb_03_seguidores.html` | Miniatura S2 Ep.03 |

### Assets de tela (para Setup D)
| Arquivo | Uso |
|---|---|
| `asset_tela_feeds_genericos.html` | V5 — dois feeds idênticos |
| `asset_tela_erros_cfm.html` | V3 e S2#01 — posts proibidos + corretos |
| `asset_tela_comparativo.html` | V3 e V5 — feed ruim vs. bom |

---

## Plano de produção v3 — 3 dias, 5 setups

| Dia | Setups | Conteúdo |
|---|---|---|
| Dia 1 | A + B | Voz over (7 falas) + câmera Roupa 1 (V2 + V4 + aberturas/encerramentos) |
| Dia 2 | C + D | Câmera Roupa 2 (V5 + 4 séries de Shorts) + tela gravada (5 cenas) |
| Dia 3 | E + edição | Cards animados (7 × 2 formatos) + montar vídeos |

**Novas séries de Shorts gravadas ao vivo (Setup C):**
- C3: "Médico me perguntou" — 10 takes de 10s
- C4: "Mito ou verdade" — 5 takes de 12s
- C5: "Em 20 anos de audiovisual" — 5 takes de 15s
- C6: "Antes de contratar uma agência" — 5 takes de 15s

---

## Bloco fixo de links para descrição YouTube

```
📍 Siga a Zyllah Digital:
Instagram → instagram.com/zyllahdigital
TikTok → tiktok.com/@zyllahdigital
LinkedIn → linkedin.com/company/zyllah-digital
Site → zyllah.com.br
```

---

## Pendências carregadas

**Alta prioridade:**
- [ ] **Roleplay da reunião de vendas** — gargalo principal desde sessões anteriores
- [ ] Postar reel "O Peso da Saúde" — pendente desde 28/03
- [ ] Subir todos os arquivos desta sessão no GitHub
- [ ] Substituir index.html no projeto (footer atualizado)
- [ ] Instalar assinatura de e-mail no Gmail
- [ ] Adicionar logo como foto principal no Google Meu Negócio
- [ ] Criar conta TikTok @zyllahdigital

**Desta sessão:**
- [ ] Gerar simulacros no Gemini com os 12 prompts antes de editar os vídeos
- [ ] Iniciar planilha de controle de produção no Google Sheets
- [ ] Preencher gerador de metadados para os 8 vídeos

---

*Zyllah Digital · Uso interno · 31 de março de 2026*

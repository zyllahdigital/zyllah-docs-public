# Zyllah Digital — Vault Operacional

Agência de presença digital para profissionais de saúde.
Fundador: Guilherme Caetano · Nova Friburgo, RJ · zyllah.com.br

---

## Filosofia de organização

Este repositório tem **viés operacional** — contém o que é usado, entregue e mostrado.

O contexto estratégico (ICP, tom de voz, skills de execução) vive no vault Obsidian em `ZyllahOS/` (local, não versionado aqui).

**Regra de criação:** ao criar um arquivo novo, perguntar:
- É algo que uso ou entrego? → entra aqui
- É contexto ou instrução de como pensar? → vai para `ZyllahOS/`

---

## Estrutura

```
01_MARCA/          Identidade visual, brandbook, logotipos, fotos de perfil
02_ESTRATEGIA/     Hub operacional, GAS, análises, relatórios de sessão Claude
03_VENDAS/         Materiais de reunião, scripts de prospecção, apresentações
04_CONTEUDO/       Produção de conteúdo: planejamento, artes, posts, séries
05_PRODUCAO_AV/    Vídeos (referências e thumbnails — brutos/editados no Drive)
07_ONBOARDING/     Documentos de entrada do cliente
08_TECNICO/        Infraestrutura: deploy, Cloudflare, Zyllah Flow, site
10_JURÍDICO/       Contratos e documentos legais (privado — não vai ao repo público)
```

---

## Convenções de nomenclatura

| Tipo | Padrão | Exemplo |
|---|---|---|
| Documento HTML operacional | `zyllah_[nome].html` | `zyllah_hub.html` |
| Script Apps Script | `script_[função].gs` | `script_conector_hub.gs` |
| Documento markdown | `[nome_descritivo].md` | `PRODUCAO.md` |
| Arte/imagem | `[tipo]_[descricao]_[versao]` | `card_medico_cansado_v1` |
| Vídeo editado | `[serie]_[ep]_[plataforma]` | `S2_E01_reel` |

**Sem espaços em nomes de arquivo. Sem acentos em nomes de pasta.**

---

## O que NÃO vai para este repo

- Vídeos brutos e editados (Drive)
- Dados de clientes e financeiro (local)
- Chaves de API (`.env`, `.claude/`)
- Dependências (`node_modules/`)

---

## Arquivos-chave

| Arquivo | Função |
|---|---|
| `CLAUDE.md` | Memória operacional do projeto — contexto para sessões Claude |
| `02_ESTRATEGIA/PROCESSOS/zyllah_hub.html` | Hub operacional central |
| `02_ESTRATEGIA/PROCESSOS/script_conector_hub.gs` | Backend GAS |
| `04_CONTEUDO/PRODUCAO.md` | Fluxo completo: gravação → edição → postagem |
| `03_VENDAS/SCRIPTS/script_reuniao.html` | Script de reunião com prospect |

---

## Vault de contexto (ZyllahOS — local)

```
ZyllahOS/
  03-CONTEXT/    ICP, tom de voz, estratégia, evolutivo, contratos
  04-SKILLS/     Skills de execução: comentário, DM, legenda, emergência
  05-PROJECTS/   Projetos ativos: sprint de gravação, hub próxima iteração
  inbox/         Entrada do pipeline prospectar.py
```

---

*Zyllah Digital · Iniciado em março de 2026 · Fundador solo*

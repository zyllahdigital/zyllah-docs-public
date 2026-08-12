# Zyllah Digital

Presença digital para profissionais de saúde.  
Fundador: Guilherme Caetano · Nova Friburgo, RJ · [zyllah.com.br](https://zyllah.com.br)

---

## ⚠️ Este repositório é PÚBLICO

**Tudo aqui é legível por qualquer pessoa da internet**, pelo GitHub e pelo `raw.githubusercontent`,
com ou sem link. Não existe "não indexado" que proteja: quem descobre o nome do repositório lê tudo.

**Ele NÃO serve o site.** `zyllah.com.br` é servido pelo repositório `zyllahdigital`.
Aqui ficam apenas documentos de compartilhamento com parceiros e colaboradores.

## O que está publicado, e para quem

| Arquivo | Para quem | Por quê |
|---|---|---|
| `ZYLLAH/brandbook.html` | colaboradores visuais | precisam do padrão para produzir |
| `ZYLLAH/contratos.html` | parceiros jurídicos | pacote contratual **v2.0**, versão de revisão jurídica |
| `ZYLLAH/mapa_riscos.html` | parceiros jurídicos | leitura dos riscos do contrato |
| `roteiro_youtube_v1..v5.html` | editor/colaborador de vídeo | viram vídeo público de qualquer forma |

## ⛔ O que NUNCA entra aqui

- **Operacional:** hub de vendas, painéis, scripts de reunião, banco de objeções, materiais de venda.
- **Dado de cliente ou de lead:** relatório, diagnóstico, dossiê, nome, telefone, endereço.
- **Credencial de qualquer espécie**, inclusive senha de tela de acesso dentro do HTML.
- **Financeiro** e qualquer arquivo marcado "uso interno".

> **Regra de decisão, e ela é o inverso da intuição:** a pergunta não é *"tem problema isto ser
> público?"*. É *"eu escolhi publicar isto, para uma pessoa específica, por um motivo escrito?"*
> **Se não houver linha na tabela acima, não sobe.**

## Histórico de saneamento

**12/08/2026 — removidos dois arquivos que contrariavam a regra deste próprio README:**
- `ZYLLAH/hub_vendas_zyllah.html` — o hub é operacional, e a versão anterior deste arquivo já dizia
  que operacional fica em repositório privado. Continha a mensalidade de dois planos e o CNPJ.
- `encantarys-relatorio-validacao-zyllah.html` — **relatório de um cliente real**, que nunca esteve
  em nenhuma tabela de "para quem".

⚠️ **Remoção não apaga o passado:** os dois seguem legíveis no histórico de commits deste
repositório, que é público. Fechar isso exige reescrever o histórico.

**12/08/2026 — `ZYLLAH/contratos.html` substituído pela versão de revisão jurídica.**
A anterior trazia `var SENHA = '2026'` **no próprio código-fonte**, o que tornava a tela de acesso
decorativa, e carimbava "Uso interno" num documento que ia para terceiro. Pior: **declarava a versão
`v2.7`, que nunca existiu** — um número fantasma que o vault já havia corrigido internamente e que
tinha sobrevivido aqui fora.

A nova é derivada do contrato vivo por `08_TECNICO/gerar_contrato_para_advogado.py`, e o script
confere sozinho antes de entregar: **v2.0 · sem bloco de senha · sem tela de senha · sem carimbo de
uso interno · 5 documentos · 20 cláusulas · divs balanceadas.**

> ⛔ **Não editar este arquivo à mão.** Mudou o contrato, rode o script de novo e substitua.
> Editar aqui recria a cópia que envelhece, que é a doença que este saneamento veio curar.

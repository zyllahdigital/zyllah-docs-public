# Zyllah Digital — Relatório de Sessão
## 3 de abril de 2026 — Sessão 15

---

## Contexto

Continuação da sessão anterior. Guilherme ainda em recuperação do resfriado. Sessão focada em infraestrutura, organização de arquivos, prospecção e validação de posicionamento.

---

## Realizações desta sessão

### GitHub Pages — repositório público ativado

URL: `https://zyllahdigital.github.io/zyllah-docs-public/`

Todos os arquivos públicos hospedados e validados. Arquivos `.htm` corrigidos para renderizar como HTML. Senhas removidas dos documentos públicos. Documentos sensíveis movidos para repositório privado.

**Validação de acesso via web_fetch confirmada:** Claude consegue acessar os documentos do GitHub Pages quando as URLs são fornecidas na conversa. O fluxo ZYLLAH_LINKS.md funciona como planejado.

### Arquitetura final de documentos definida

| Local | O que vai lá |
|---|---|
| GitHub Pages público | Documentos sem informação sensível — cards, roteiros, briefings, ferramentas, prompts |
| GitHub privado | Hub, script de reunião, contratos, vendas, quiz de vendas, catálogo de senhas, flow |
| Projeto Claude | INSTRUCOES_PROJETO_v2.md + ZYLLAH_LINKS.md + relatório recente |

### ZYLLAH_LINKS.md criado

Índice completo de todos os documentos com URLs do GitHub Pages. Fica no projeto Claude. Claude acessa os documentos via web_fetch quando necessário — sem precisar que Guilherme cole o conteúdo manualmente.

### Teste de posicionamento com Manus

Guilherme simulou ser um dentista e pediu ao Manus que pesquisasse a Zyllah. Resultado:

- **Nota atribuída:** 9.5 / 10
- Manus chegou aos mesmos argumentos do script de vendas de forma orgânica
- Validou que o posicionamento público já vende antes da reunião

Documento gerado: `validacao_posicionamento_manus.md`

**Vulnerabilidades identificadas:**
- Zyllah Flow vendido como argumento central — ainda não validado com Encantarys
- Claude Pro mencionado como "motor invisível" — reforça regra de não mencionar em reuniões

### Prospecção — Dra. Kelly Purger

Manus analisou o Instagram da Dra. Kelly e selecionou dois posts estratégicos:
- Post 1: Ozempic e Botox — interação medicamentosa (nov/2025)
- Post 2: Menos tendência, mais ciência (3 dias atrás)

Comentários corrigidos — versões sem mencionar a Zyllah. Guilherme comentou em ambos os posts.

### Prompt anti-alucinação para Gemini e Manus

Criado prompt de sistema que força separação entre VERIFICADO / NÃO VERIFICADO / INTERPRETAÇÃO com nível de confiança ao final. Versão completa e versão curta.

### Pesquisa empírica — 10 prospects Nova Friburgo

Pesquisa via Google completa para todos os 10 prospects da lista do Manus:

| Prospect | Risco | Observação |
|---|---|---|
| Dra. Kelly Purger | 🟢 Baixo | 2 avaliações Google, Instagram difícil de encontrar |
| Dr. Cleonicio Cordeiro | 🟢 Baixo | Presença digital praticamente inexistente |
| Dra. Fabricia Corbett | 🟢 Baixo | 29 anos experiência, @fabriciacorbett2 no Instagram |
| Dr. Thiago Ribeiro | 🟡 Médio | 7.6k seguidores, 47 posts — verificar data |
| Dr. Bernardo Daflon | 🟡 Médio | Site existe, @daflonfriburgo a confirmar |
| Dra. Carolina Monnerat | 🟡 Médio | Gmail como contato profissional da clínica |
| Dr. Marcelo Rosa | 🟡 Médio | 5.6k seguidores, sem site |
| Dr. Augusto Pedretti | 🟡 Médio | Site + Instagram existem |
| Dra. Isabela Saleme | 🔴 Alto | Ecossistema completo — pode ter agência |
| Dr. Richard Robadey | 🔴 Alto | Apareceu no Lady Night, presença robusta |

### Prompt de pesquisa de prospect para Gemini

Criado prompt estruturado para Gemini pesquisar qualquer prospect e retornar relatório padronizado em 6 seções. Versão detalhada e versão em lote. Claude faz o diagnóstico estratégico com base no relatório.

### Decisões estratégicas

**Diagnóstico Digital como etapa zero:** toda abordagem precisa de pesquisa prévia. Mensagem usa reconhecimento do prospect como gancho — nunca o gap digital (risco de entregar ouro ao concorrente). Gap fica para a apresentação personalizada na reunião.

**Apresentação personalizada na reunião:** slides com dados reais do prospect — avaliações Google, posição nas buscas, feed do Instagram. Visto presencialmente, não pode ser gravado. Diferencial que nenhuma agência local faz.

**Cobrança automática:** Stripe ou PagSeguro Recorrente — resolver antes do primeiro contrato.

**Política de revisões:** incluir no contrato — número de rodadas incluídas, prazo de aprovação, escopo preciso.

**Arquitetura dos 5 motores:**
- Entrada — Diagnóstico + Prospecção
- Conversão — Vendas
- Entrega — Produção
- Retenção — Gestão de Clientes
- Passivo — Produto Perpétuo

**Aba Ideias na planilha:** Motor / Quando (Agora / Pós 1º cliente / Pós 2º cliente)

### Documentos produzidos nesta sessão

| Arquivo | Descrição |
|---|---|
| `validacao_posicionamento_manus.md` | Teste com IA independente — nota 9.5/10 |
| `prompt_sistema_gemini_manus.md` | Prompt anti-alucinação para Gemini e Manus |
| `prompt_pesquisa_prospect.html` | Prompt estruturado para pesquisa de prospects |
| `ZYLLAH_LINKS.md` | Índice completo de documentos com URLs |
| `manual_tarefas_pendentes.html` | Checklist passo a passo para criança de 10 anos |
| `relatorio_sessao_03abr.md` | Este relatório |

---

## Pendências atualizadas

**Urgente:**
- [ ] Ativar GitHub Pages no repositório privado (não ativar — deve ficar inacessível)
- [ ] Popular planilha Zyllah Pendências com CSV (via computador)
- [ ] Criar estrutura de pastas de produção no computador
- [ ] Subir index.html com Meta Pixel no repositório do site

**Alta prioridade:**
- [ ] Roleplay da reunião de vendas — gargalo principal
- [ ] Verificar Instagrams dos prospects de risco médio antes de abordar
- [ ] Incluir cláusula de revisões e cobrança automática no contrato
- [ ] Adicionar aba Ideias na planilha de pendências
- [ ] Comentar em 2º post da Dra. Kelly Purger antes de enviar DM

**Prospecção:**
- [ ] Iniciar comentários nos prospects de risco baixo: Dr. Cleonicio Cordeiro, Dra. Fabricia Corbett
- [ ] Verificar @daflonfriburgo — confirmar se é o Dr. Bernardo Daflon

**Pós-recuperação:**
- [ ] Gravar Setups A, B, C, D, E
- [ ] Postar reel O Peso da Saúde — pendente desde 28/03

---

*Zyllah Digital · Uso interno · 3 de abril de 2026*

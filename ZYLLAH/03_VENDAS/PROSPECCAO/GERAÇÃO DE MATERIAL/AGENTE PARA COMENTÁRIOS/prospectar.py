#!/usr/bin/env python3
"""
Zyllah Prospectar — Pipeline unificado
Gera COMENTÁRIOS para prospects E INSPIRAÇÃO EDITORIAL a partir da mesma
descrição do Qwen sobre a gravação de tela.

Fluxo:
  1. Grave a tela navegando pelos posts dos prospects/criadores do nicho
  2. Jogue o vídeo no Qwen → peça descrição detalhada de cada post visto
  3. Salve o texto do Qwen como arquivo .txt em:
       .../AGENTE PARA COMENTÁRIOS/inbox/
  4. Duplo clique em prospectar.bat
  5. Resultados em inbox/saidas/
       → AAAMMDD_comentarios.md   (comentários para publicar)
       → AAAMMDD_editorial.md     (inspiração para o conteúdo da Zyllah)

Modelo: Haiku (tarefa funcional — não usa conta Pro)
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent
INBOX        = SCRIPT_DIR / "inbox"
SAIDAS       = INBOX / "saidas"
PROCESSADOS  = INBOX / "processados"

# Skills e contexto vivem no ZyllahOS (vault de referência)
ZYLLAHOS = Path(r"C:\Users\Guilherme\Documents\ZyllahOS")
SKILLS   = ZYLLAHOS / "04-SKILLS"
CONTEXT  = ZYLLAHOS / "03-CONTEXT"

# ── Helpers ────────────────────────────────────────────────────────────────
def load_file(path: Path) -> str:
    for variant in [path, path.with_suffix(".md"), path.with_name(path.name + ".md")]:
        if variant.exists():
            return variant.read_text(encoding="utf-8")
    return f"[NÃO ENCONTRADO: {path}]"

def load_skill(name: str) -> str:
    skill_dir = SKILLS / name
    for candidate in ["SKILL.md", "SKILL.md.md"]:
        f = skill_dir / candidate
        if f.exists():
            return f.read_text(encoding="utf-8")
    return f"[SKILL {name} não encontrada em {skill_dir}]"

# ── Prompts ────────────────────────────────────────────────────────────────
def build_prompt_comentarios() -> str:
    return f"""Você é o assistente operacional de prospecção da Zyllah Digital —
agência de presença digital para profissionais de saúde em Nova Friburgo, RJ.

{load_skill("zyllah-voz")}

{load_skill("zyllah-comentario-publico")}

ICP — PERFIL DO CLIENTE IDEAL:
{load_file(CONTEXT / "icp.md")}

TOM DE VOZ:
{load_file(CONTEXT / "tom-de-voz.md")}

SUA TAREFA: analisar a descrição de posts vistos na gravação de tela.
Selecionar máximo 5 com potencial real de comentário. Para cada um, gerar 2 opções.

SELECIONAR: post mostra DECISÃO do médico, tem espaço para observação de nicho,
deixa porta aberta, não é polêmico nem arriscado para CFM.
DESCARTAR: antes/depois, promoção de preço, post de clínica (não do médico),
polêmico, comentário pareceria oportunista.

FORMATO DE SAÍDA para cada post selecionado:
---
## [N]. [Nome/Especialidade] · [Canal]
**Post:** [1-2 frases]
**Por que vale:** [1 frase]
**Opção A:** [máx 2 frases — nomeia decisão como verdade universal]
**Opção B:** [máx 3 frases — adiciona camada]
**Raciocínio:** [onde A/B funcionam, onde pode falhar]
---

Ao final: ## Posts descartados (lista com motivo em 1 linha cada)

CRÍTICO: elogiar sempre a DECISÃO do médico, nunca a execução do conteúdo."""

def build_prompt_editorial() -> str:
    return f"""Você é o assistente de planejamento editorial da Zyllah Digital —
agência de presença digital especializada em profissionais de saúde.

{load_skill("zyllah-voz")}

TOM DE VOZ:
{load_file(CONTEXT / "tom-de-voz.md")}

ICP:
{load_file(CONTEXT / "icp.md")}

SUA TAREFA: analisar os posts vistos na gravação de tela e extrair
INSPIRAÇÃO EDITORIAL para o conteúdo da PRÓPRIA Zyllah.

Não é para comentar nesses posts. É para identificar:
1. Temas que estão em alta no nicho de saúde/medicina digital
2. Ângulos que ninguém está abordando com profundidade
3. Dores ou tensões que a Zyllah pode explorar no próprio conteúdo
4. Formatos que estão performando bem e que fazem sentido para a Zyllah

FORMATO DE SAÍDA:

## Tendências identificadas
[3-5 temas que aparecem com frequência ou destaque nos posts vistos]

## Oportunidades editoriais para a Zyllah
Para cada oportunidade:
---
**Tema:** [nome do tema]
**Ângulo Zyllah:** [como a Zyllah abordaria — específico, com o tom da marca]
**Formato sugerido:** [reel / carrossel / texto longo / vídeo educativo]
**Gancho:** [primeira frase ou ideia de abertura]
**Por que agora:** [por que esse tema é relevante neste momento]
---

## O que NÃO fazer (baseado no que está saturado)
[2-3 abordagens que aparecem demais e que a Zyllah deve evitar por serem genéricas]

## Sugestão de pauta para a semana
[3 temas concretos com formato e gancho, prontos para virar roteiro]

Calibrar tudo pelo tom da Zyllah: clínico, direto, sem rodeios morais.
Nunca sugerir conteúdo que o CFM proibiria."""

# ── Processamento ──────────────────────────────────────────────────────────
def process_file(txt_file: Path, modo: str) -> tuple[str, str]:
    """
    Processa um arquivo .txt com a descrição do Qwen.
    modo: 'ambos' | 'comentarios' | 'editorial'
    Retorna (resultado_comentarios, resultado_editorial) — vazio se não solicitado.
    """
    import anthropic
    client = anthropic.Anthropic()

    description = txt_file.read_text(encoding="utf-8")
    if not description.strip():
        return "Arquivo vazio.", ""

    def chamar(system: str, task_label: str) -> str:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=4096,
            system=system,
            messages=[{"role": "user", "content":
                f"Descrição da gravação ({txt_file.name}):\n\n{description}"}]
        )
        return msg.content[0].text

    res_comentarios = ""
    res_editorial   = ""

    if modo in ("ambos", "comentarios"):
        print("    → Gerando comentários...", end="", flush=True)
        res_comentarios = chamar(build_prompt_comentarios(), "comentarios")
        print(" OK")

    if modo in ("ambos", "editorial"):
        print("    → Gerando inspiração editorial...", end="", flush=True)
        res_editorial = chamar(build_prompt_editorial(), "editorial")
        print(" OK")

    return res_comentarios, res_editorial

def save_results(res_com: str, res_ed: str, source_name: str) -> list[Path]:
    SAIDAS.mkdir(parents=True, exist_ok=True)
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    saved = []

    header = lambda tipo: f"""# {tipo} — {hora}
> Fonte: `{source_name}` · Modelo: Haiku · Skills: zyllah-voz + {
    "zyllah-comentario-publico" if "Comentário" in tipo else "editorial"
}

---

"""

    if res_com:
        path = SAIDAS / f"{ts}_comentarios.md"
        note = """> **Antes de publicar:** leia em voz alta.
> Teste: *"Se o médico visse isso, pensaria 'é com esses que quero trabalhar'?"*

---

"""
        path.write_text(header("Sugestões de Comentário") + note + res_com, encoding="utf-8")
        saved.append(path)

    if res_ed:
        path = SAIDAS / f"{ts}_editorial.md"
        path.write_text(header("Inspiração Editorial") + res_ed, encoding="utf-8")
        saved.append(path)

    return saved

def archive_input(txt_file: Path):
    PROCESSADOS.mkdir(parents=True, exist_ok=True)
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = PROCESSADOS / f"{ts}_{txt_file.name}"
    txt_file.rename(dest)

# ── API Key ────────────────────────────────────────────────────────────────
def check_api_key() -> bool:
    if os.environ.get("ANTHROPIC_API_KEY"):
        return True
    # Procura .env em múltiplos locais
    candidates = [
        SCRIPT_DIR / ".env",
        ZYLLAHOS / ".env",
        Path.home() / ".env",
    ]
    for env_file in candidates:
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY=") and not line.startswith("#"):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if key and "COLE" not in key:
                        os.environ["ANTHROPIC_API_KEY"] = key
                        return True
    return False

# ── Menu ───────────────────────────────────────────────────────────────────
def escolher_modo() -> str:
    print("\nO que gerar?")
    print("  [1] Comentários para prospects")
    print("  [2] Inspiração editorial")
    print("  [3] Ambos (recomendado)")
    while True:
        op = input("\nOpção (1/2/3): ").strip()
        if op == "1": return "comentarios"
        if op == "2": return "editorial"
        if op == "3" or op == "": return "ambos"
        print("  → Digite 1, 2 ou 3.")

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    print("=" * 52)
    print("  Zyllah Prospectar — Comentários + Editorial")
    print("=" * 52)

    if not check_api_key():
        print("\nERRO: Chave Anthropic não encontrada ou sem créditos.")
        print("  → Acesse console.anthropic.com → Billing → Add credits")
        print("  → Ative auto-reload para não interromper de novo")
        print(f"\n  Crie {ZYLLAHOS / '.env'} com:")
        print("  ANTHROPIC_API_KEY=sk-ant-...")
        input("\nEnter para sair...")
        sys.exit(1)

    INBOX.mkdir(exist_ok=True)
    txt_files = list(INBOX.glob("*.txt"))

    if not txt_files:
        print(f"\nNenhum .txt em: {INBOX}")
        print("\nFluxo:")
        print("  1. Grave a tela navegando pelos perfis dos prospects")
        print("  2. Qwen: 'Descreva cada post: quem postou, canal, conteúdo, tom'")
        print("  3. Salve o texto como .txt nesta pasta inbox/")
        print("  4. Rode novamente")
        input("\nEnter para sair...")
        return

    print(f"\n{len(txt_files)} arquivo(s) em inbox:\n")
    for f in txt_files:
        print(f"  · {f.name}")

    modo = escolher_modo()

    for txt_file in txt_files:
        print(f"\n▸ Processando: {txt_file.name}")
        try:
            res_com, res_ed = process_file(txt_file, modo)
            saved           = save_results(res_com, res_ed, txt_file.name)
            archive_input(txt_file)
            for s in saved:
                print(f"  ✓ {s.name}")
        except Exception as e:
            print(f"  ✗ Erro: {e}")

    print(f"\n{'=' * 52}")
    print("  Pronto. Abra inbox/saidas/ para ver os resultados.")
    print(f"{'=' * 52}")
    input("\nEnter para sair...")

if __name__ == "__main__":
    main()

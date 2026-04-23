#senha-tela { position: fixed; inset: 0; z-index: 99999; background: #1A1714; display: flex; align-items: center; justify-content: center; }
.senha-box { width: 100%; max-width: 400px; padding: 48px; display: flex; flex-direction: column; gap: 20px; }
.senha-logo { font-family: ‘Cormorant Garamond’, serif; font-size: 13px; color: rgba(184,151,106,0.5); letter-spacing: 0.3em; }
.senha-titulo { font-family: ‘Cormorant Garamond’, serif; font-size: 32px; font-weight: 300; color: white; line-height: 1.1; }
.senha-titulo em { font-style: italic; color: #D4B896; }
.senha-input { width: 100%; background: transparent; border: none; border-bottom: 1px solid rgba(184,151,106,0.35); padding: 14px 0; font-family: ‘Jost’, sans-serif; font-size: 18px; color: white; outline: none; letter-spacing: 0.1em; }
.senha-input::placeholder { color:rgba(255,255,255,0.55); font-size: 14px; letter-spacing: 0.2em; }
.senha-btn { background: #B8976A; color: #1A1714; border: none; padding: 14px 32px; font-family: ‘Jost’, sans-serif; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; cursor: pointer; align-self: flex-start; }
.senha-erro { font-size: 13px; color: rgba(210,100,100,0.9); min-height: 18px; }

.header { background: var(–ink); padding: 56px 80px 48px; }
.header-tag { font-size: 11px; letter-spacing: 0.5em; text-transform: uppercase; color: var(–gold); margin-bottom: 16px; display: block; }
.header-titulo { font-family: ‘Cormorant Garamond’, serif; font-size: clamp(36px, 5vw, 56px); font-weight: 300; color: white; line-height: 1.05; margin-bottom: 12px; }
.header-titulo em { font-style: italic; color: var(–gold-light); }
.header-sub { font-size: 15px; color:rgba(255,255,255,0.55); max-width: 560px; line-height: 1.85; }

.corpo { max-width: 960px; margin: 0 auto; padding: 64px 60px 100px; }

.semana { margin-bottom: 56px; }
.semana-header { background: var(–ink); padding: 18px 28px; display: flex; align-items: center; justify-content: space-between; }
.semana-titulo { font-family: ‘Cormorant Garamond’, serif; font-size: 22px; color: white; font-weight: 300; }
.semana-tema { font-size: 11px; letter-spacing: 0.25em; text-transform: uppercase; color: var(–gold); }

.post { background: white; border: 1px solid rgba(184,151,106,0.12); border-left: 4px solid transparent; margin-top: 2px; }
.post.li { border-left-color: var(–li); }
.post.ig { border-left-color: var(–ig); }
.post.li-emp { border-left-color: var(–li-emp); }
.post.ambos { border-left-color: var(–gold); }

.post-header { padding: 16px 24px 0; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.post-dia { font-size: 13px; font-weight: 500; color: var(–ink); min-width: 60px; }
.post-canal { font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; padding: 3px 10px; }
.post-canal.li { background: rgba(10,102,194,0.08); color: var(–li); }
.post-canal.ig { background: rgba(193,53,132,0.08); color: var(–ig); }
.post-canal.li-emp { background: rgba(0,160,220,0.08); color: var(–li-emp); }
.post-canal.ambos { background: rgba(184,151,106,0.1); color: var(–gold-dark); }
.post-formato { font-size: 11px; color:rgba(61,56,48,0.65); letter-spacing: 0.1em; }

.post-body { padding: 12px 24px 20px; }
.post-titulo { font-size: 15px; font-weight: 500; color: var(–ink); margin-bottom: 10px; }

.bloco { margin-bottom: 14px; }
.bloco-label { font-size: 10px; letter-spacing: 0.35em; text-transform: uppercase; color: var(–gold-dark); margin-bottom: 6px; display: block; }

.visual-box { background: rgba(184,151,106,0.05); border: 1px dashed rgba(184,151,106,0.3); padding: 12px 16px; font-size: 13px; color: var(–ink-soft); line-height: 1.7; }
.visual-box em { color: var(–ink); font-style: normal; font-weight: 400; }

.texto-box { background: rgba(61,56,48,0.03); border-left: 2px solid rgba(184,151,106,0.3); padding: 14px 18px; font-size: 14px; color: var(–ink-soft); line-height: 1.85; white-space: pre-wrap; }
.texto-box strong { color: var(–ink); font-weight: 400; }

.nota-box { font-size: 12px; color: var(–gold-dark); font-style: italic; margin-top: 8px; }

.secao-tag { font-size: 11px; letter-spacing: 0.45em; text-transform: uppercase; color: var(–gold); margin-bottom: 12px; margin-top: 56px; display: flex; align-items: center; gap: 12px; }
.secao-tag::after { content: ‘’; flex: 1; height: 1px; background: rgba(184,151,106,0.2); }
.secao-titulo { font-family: ‘Cormorant Garamond’, serif; font-size: 32px; font-weight: 300; color: var(–ink); margin-bottom: 28px; }
.secao-titulo em { font-style: italic; color: var(–gold); }

.regra { background: var(–ink); padding: 24px 32px; margin: 32px 0; }
.regra p { font-size: 14px; color: rgba(255,255,255,0.6); line-height: 1.85; }
.regra p strong { color: white; font-weight: 400; }
.regra p em { color: var(–gold-light); font-style: italic; }

@media (max-width: 640px) {
.header { padding: 40px 24px; }
.corpo { padding: 40px 20px 80px; }
.semana-header { flex-direction: column; align-items: flex-start; gap: 6px; }
}

Zyllah Digital
Acesso
restrito
Entrar →
Estratégia de Conteúdo · Uso interno
Calendário
de conteúdo
LinkedIn pessoal · LinkedIn empresa · Instagram. Textos prontos, visual descrito, cadência sustentável para 2-3 horas por semana.

Como usar este documento: cada post tem três blocos — Visual (o que produzir no Canva ou fotografar), Texto (pronto para adaptar e publicar), e quando necessário uma nota de execução. Adapte o texto com sua voz antes de publicar — não publique palavra por palavra sem ler em voz alta primeiro.

Semana 1
Apresentação — quem sou, o que faço, por que importa
Terça
LinkedIn Pessoal
Texto longo · já publicado
Os 16 anos — post de estreia
Status
Post já publicado e no ar. Monitore os comentários e responda todos nas primeiras 2 horas — isso sinaliza ao algoritmo que o post gera conversa.
Quarta
Instagram
Foto + texto
Apresentação da Zyllah
Visual
Foto sua trabalhando — pode ser você olhando para tela do computador, de lado ou de costas (não precisa aparecer o rosto se não quiser). Luz natural preferencial. Fundo neutro ou escritório. Alternativamente: o logo da Zyllah centralizado em fundo ink (#1A1714), com tagline embaixo em dourado — feito no Canva, tamanho 1080×1080px.
Texto
Comecei a Zyllah Digital porque vi um padrão se repetindo.
Profissionais de saúde brilhantes — médicos, dentistas, psicólogos — com uma presença digital que não representa nem um pouco o trabalho que entregam.

Não é descuido. É que eles foram formados para cuidar de pessoas, não para criar conteúdo.

A Zyllah Digital existe pra resolver exatamente isso.

Se você é profissional de saúde, ou conhece alguém que é: me segue por aqui. Vou compartilhar o que aprendo nessa jornada. 🌿

#ZyllahDigital #PresençaDigital #Saúde


Quinta
LinkedIn Pessoal
Texto médio
Por que saúde?
Visual
Posts de texto no LinkedIn não precisam de imagem — o algoritmo distribui texto puro muito bem. Se quiser adicionar: foto sua de perfil profissional (não selfie), ou deixe sem imagem mesmo.
Texto
Tem um paradoxo curioso no mercado de saúde.
Os profissionais mais qualificados — os que mais estudaram, os que mais investiram na formação — costumam ter a presença digital mais fraca.

Não é coincidência.

É que a formação médica, odontológica, psicológica é longa e absortiva. Quando terminam, já têm 30 anos, um consultório pra montar e pacientes pra atender. Aprender marketing não estava no plano.

Resultado: o Instagram some por meses. O site continua com foto de 2018. A indicação boca a boca ainda é a única fonte de novos pacientes.

Escolhi esse nicho porque o problema é real, recorrente e — principalmente — porque existe um gap enorme entre a qualidade do trabalho que esses profissionais entregam e como eles se apresentam para o mundo.

Esse gap é onde a Zyllah Digital trabalha.

Você já percebeu esse padrão em algum profissional de saúde que conhece?


Quinta
LinkedIn Empresa
Post de estreia da página
Apresentação da página Zyllah Digital
Visual
Logo da Zyllah em fundo ink, tamanho 1200×627px. No Canva: fundo #1A1714, logo centralizado (LOGO_TOTAL.svg), tagline abaixo em Jost 300, cor #B8976A: "Presença Digital para Saúde". URL zyllah.com.br no canto inferior direito em tamanho menor.
Texto
A Zyllah Digital começa hoje.
Somos especializados em presença digital para profissionais e clínicas de saúde — médicos, dentistas, psicólogos e outros que entregam excelência no consultório mas ainda não encontraram a forma certa de mostrar isso para o mundo.

Nosso trabalho: construir identidade, conteúdo e posicionamento digital que representam, de verdade, a qualidade do serviço que você já presta.

Siga a página para acompanhar nossa jornada.

🌐 zyllah.com.br


Depois de publicar na página, compartilhe do perfil pessoal com uma frase curta: “A página da Zyllah Digital está no ar — me segue lá também.”

Sexta
Instagram
Carrossel · 5 slides
3 sinais de que sua presença digital não representa seu trabalho
Visual — descrição slide a slide
Slide 1 (capa): Fundo ink (#1A1714). Texto em branco, fonte Cormorant Garamond: "3 sinais de que sua presença digital não representa seu trabalho". Logo pequeno no canto inferior. Tamanho 1080×1080px.
Slides 2, 3, 4 (um sinal por slide): Fundo creme (#FAF7F2). Número grande em dourado (1, 2, 3) no canto superior esquerdo em Cormorant. Título do sinal em marrom escuro, fonte Jost. Descrição curta abaixo.

Slide 5 (CTA): Fundo ink. Texto em branco: “Reconheceu algum desses sinais?” Linha dourada. Abaixo: “Me manda uma mensagem. 🌿 @zyllahdigital”




Conteúdo dos slides
Slide 2: Sinal 1 — Você some por semanas
Seu perfil fica sem post por 30, 60, 90 dias. Não por falta de vontade — por falta de método.
Slide 3: Sinal 2 — Suas redes não mostram sua especialidade
Quem visita seu perfil não consegue entender em 5 segundos o que você faz e para quem.

Slide 4: Sinal 3 — Você depende 100% de indicação
Novos pacientes chegam só por indicação. O digital não gera nenhum contato novo.



Legenda
Se você reconheceu 1 ou mais desses sinais — você não está sozinho.
A maioria dos profissionais de saúde que conheço passa por pelo menos um deles.

Salva esse post. E se quiser conversar sobre como está a sua presença digital hoje, me manda mensagem. 🌿

#PresençaDigital #ProfissionalDeSaúde #MarketingParaSaúde #ZyllahDigital


Semana 2
O problema do profissional de saúde
Segunda
Instagram
Foto bastidor
Bastidor — como você pesquisa um nicho
Visual
Foto da tela do computador com abas abertas de pesquisa — perfis de saúde, referências de comunicação, anotações. Pode ser desfocada levemente para não revelar dados. Ou: caderno aberto com anotações manuscritas sobre o nicho saúde. Luz natural, fundo neutro. Não precisa aparecer seu rosto.
Legenda
Antes de qualquer projeto, pesquiso.
Perfis de referência, linguagem do nicho, o que funciona, o que não funciona, o que está sendo dito demais e o que está faltando.

No caso de saúde: falta muita coisa. 👀

Mais sobre isso nos próximos posts.

#ZyllahDigital #BastidorDeAgência


Terça
LinkedIn Pessoal
Texto longo
O médico que some do Instagram por meses
Texto
Existe um padrão que vejo se repetir.
O médico posta durante 2 semanas. Com energia, com cuidado, com conteúdo bom.

Aí vem uma semana pesada no consultório. Depois um plantão. Depois uma emergência familiar.

E o Instagram fica parado por 40, 60, 90 dias.

Quando ele volta, sente que precisa se justificar. Escreve um post de “voltei!”. Posta mais uma semana. E o ciclo recomeça.

Não é falta de comprometimento.

É que o modelo que ele está tentando seguir — criar conteúdo de improviso, sem método, sem calendário — não foi feito para a rotina de quem trabalha com saúde.

O que funciona é diferente: conteúdo planejado com antecedência, em blocos, com temas definidos. Assim você produz tudo numa tarde e programa para o mês inteiro.

Parece simples. E é — quando alguém organiza isso por você.

Você conhece algum profissional de saúde que vive nesse ciclo?


Quarta
Instagram
Carrossel · 6 slides
Por que profissionais de saúde têm dificuldade com conteúdo
Visual — slide a slide
Slide 1 (capa): Fundo ink. Título em branco: "Por que profissionais de saúde têm dificuldade com conteúdo" — fonte Cormorant, tamanho grande. Logo no canto.
Slides 2–5: Fundo creme. Número + título do motivo em destaque (Cormorant, dourado). Texto explicativo abaixo (Jost 300, marrom). Linha fina dourada separando número do texto.

Slide 6: Fundo ink. Texto em branco: “Nenhum desses motivos é falta de vontade.” Abaixo em dourado menor: “É falta de método. E isso tem solução.”




Conteúdo dos slides
Motivo 1: Tempo
A rotina de saúde não tem margem. Entre consultas, plantões e formação continuada, sobra pouco espaço para pensar em conteúdo.
Motivo 2: Restrições do CFM e CFO
Médicos e dentistas não podem prometer resultados nem usar antes/depois de procedimentos. Isso limita e gera insegurança sobre o que pode e o que não pode ser publicado.

Motivo 3: Não saber o que dizer
“Minha rotina é muito técnica, ninguém vai se interessar.” — Essa frase aparece toda semana. E está errada.

Motivo 4: Medo de parecer vendedor
Profissional de saúde tem pudor. Parece que falar do próprio trabalho é vanglória. Não é — é informação que o paciente precisa para te encontrar.



Legenda
Já ouvi essas quatro frases dezenas de vezes.
Todas têm solução. Nenhuma delas significa que conteúdo não funciona para saúde — significa que o método precisa ser diferente.

Salva esse carrossel. E me conta nos comentários: qual desses você mais se identifica? 👇

#ProfissionalDeSaúde #MarketingMédico #PresençaDigital #ZyllahDigital


Quinta
LinkedIn Pessoal
Texto médio
A diferença entre visibilidade e autoridade
Texto
Muita gente confunde as duas. E a diferença importa muito — especialmente em saúde.
Visibilidade é ser visto.
Autoridade é ser procurado.

Você pode ter visibilidade e não ter autoridade: um perfil com muitos seguidores mas sem posição clara. As pessoas veem, mas não sabem exatamente por que deveriam te contratar.

Você pode ter autoridade sem visibilidade: o especialista que todo mundo no meio conhece, mas que não aparece para quem está pesquisando online.

O ideal — e o que constrói negócio de verdade — é ter os dois.

Para profissionais de saúde, a autoridade geralmente já existe. O conhecimento está lá. O que falta é a visibilidade que traduz esse conhecimento para quem ainda não te conhece.

Essa tradução é o que a comunicação faz quando é feita com intenção.


Quinta
LinkedIn Empresa
Texto curto + imagem
Reforço de posicionamento
Visual
Arte no Canva 1200×627px, fundo creme (#FAF7F2). Frase em destaque no centro, fonte Cormorant Garamond itálico, cor ink: "Visibilidade é ser visto. Autoridade é ser procurado." Linha fina dourada abaixo da frase. Logo Zyllah pequeno no canto inferior direito.
Texto
Profissionais de saúde geralmente já têm autoridade.
O que falta é a visibilidade que traduz essa autoridade para quem ainda não os conhece.

Esse é o trabalho da Zyllah Digital.

🌐 zyllah.com.br


Sexta
Instagram
Arte · frase da semana
Quote da semana
Visual
Arte 1080×1080px no Canva. Fundo ink (#1A1714). Frase centralizada em fonte Cormorant Garamond itálico, cor branco: "Visibilidade é ser visto. Autoridade é ser procurado." Linha fina dourada acima e abaixo da frase. Logo Zyllah pequeno no canto inferior.
Legenda
Qual dos dois você precisa construir agora?
👇 Me conta nos comentários.

#ZyllahDigital #PresençaDigital #MarketingParaSaúde


Semana 3
Como a Zyllah trabalha — método e processo
Segunda
Instagram
Vídeo curto · 30–60s
30 segundos: o que a Zyllah faz
Visual
Você enquadrado da cintura para cima, fundo neutro ou parede limpa. Câmera na altura dos olhos. Luz natural de frente ou lateral. Sem edição elaborada — autenticidade supera produção aqui. Pode gravar 2-3 takes e usar o melhor. Duração: 30 a 60 segundos.
Roteiro (fale com suas palavras)
Oi, eu sou o Guilherme, fundador da Zyllah Digital.
A Zyllah existe pra resolver um problema específico: profissionais de saúde que entregam excelência no consultório mas têm uma presença digital que não representa esse trabalho.

A gente constrói identidade visual, estratégia de conteúdo e posicionamento digital — feito pra quem não tem tempo de aprender marketing, mas quer ser encontrado pelas pessoas certas.

Se isso faz sentido pra você ou pra alguém que você conhece, me manda mensagem. O link está na bio.


Terça
LinkedIn Pessoal
Texto longo
O briefing como proteção
Texto
Todo retrabalho que já vi na vida tem a mesma origem.
Alguém começou sem entender o suficiente.

Não é falta de competência técnica. É falta de informação na hora certa. O cliente pediu uma coisa, o profissional entendeu outra, e só na entrega ficou claro que o caminho estava errado desde o início.

Por isso, todo projeto na Zyllah começa com briefing.

Não é burocracia. É proteção — minha e do cliente.

Quando eu entendo exatamente quem ele atende, o que ele quer transmitir, o que já tentou antes e o que não funcionou — a entrega acerta da primeira vez. Menos retrabalho, menos estresse, mais resultado.

Tem outro benefício que as pessoas não percebem de imediato: o briefing qualifica o cliente. Quem não tem disposição para responder 15 perguntas sobre o próprio negócio geralmente também não tem disposição para dar feedback claro ou respeitar prazos.

Descobrir isso antes de assinar contrato poupa muita energia dos dois lados.

Você usa algum processo de alinhamento antes de começar um projeto?


Quarta
Instagram
Carrossel · 6 slides
Do briefing ao resultado: como funciona um projeto Zyllah
Visual — slide a slide
Slide 1 (capa): Fundo ink. Título em branco Cormorant: "Do briefing ao resultado" — subtítulo menor em dourado Jost: "Como funciona um projeto Zyllah Digital".
Slides 2–5 (etapas): Fundo creme. Número da etapa grande em dourado (Cormorant). Nome da etapa em negrito (Jost 500). Descrição curta abaixo (Jost 300).

Slide 6: Fundo ink. Texto: “Resultado: uma presença digital que representa o trabalho que você já entrega.” Logo no canto.




Conteúdo das etapas
Etapa 1 — Briefing: Você responde perguntas sobre seu negócio, seus clientes e seus objetivos. Isso define tudo que vem depois.
Etapa 2 — Diagnóstico: Analisamos sua presença digital atual — o que está faltando, o que precisa de ajuste, o que já está bom.

Etapa 3 — Construção: Identidade visual, textos, estratégia de conteúdo — tudo alinhado com o que foi levantado no briefing.

Etapa 4 — Entrega e ajustes: Você recebe os materiais, revisa, e a gente ajusta até estar certo. Até 2 rodadas incluídas.



Legenda
Processo claro, sem surpresas.
Cada etapa existe por um motivo. E cada entrega é baseada no que você disse que precisa — não no que a gente acha bonito.

Curioso sobre como seria um projeto para o seu perfil? Me manda mensagem. 🌿

#ZyllahDigital #ProcessoCriativo #PresençaDigital


Quinta
LinkedIn Pessoal
Texto médio
O que você perde sem presença digital consistente
Texto
Um dado que ninguém fala com clareza suficiente:
Quando um paciente recebe indicação do seu nome, a primeira coisa que ele faz é pesquisar você online.

Se o que ele encontra não convence — perfil desatualizado, poucas fotos, bio genérica, último post de seis meses atrás — ele continua a busca.

Não necessariamente vai para o concorrente. Mas hesita.

E na hesitação, você perde.

Não é questão de estar o tempo todo nas redes. É questão de, quando alguém te procura, o que ele encontra estar à altura do que você entrega.

Isso é o que uma presença digital consistente faz: converte a curiosidade em consulta.


Quinta
LinkedIn Empresa
Texto + arte
O processo Zyllah em uma frase
Visual
Arte 1200×627px no Canva. Fundo creme. Frase centralizada em Cormorant itálico: "Briefing. Diagnóstico. Construção. Entrega." Cada palavra separada por linha fina dourada vertical. Logo Zyllah no canto inferior direito.
Texto
Cada projeto Zyllah segue quatro etapas.
Briefing — para entender de verdade o negócio e o cliente.
Diagnóstico — para identificar o que falta e o que já está bom.
Construção — identidade, conteúdo e posicionamento alinhados.
Entrega — com revisão até estar certo.

Sem surpresas. Sem escopo aberto. Sem retrabalho desnecessário.

🌐 zyllah.com.br


Sexta
Instagram
Foto bastidor
Bastidor — criando material para cliente
Visual
Tela do Canva ou computador com um projeto aberto — pode ser borrado ou parcialmente ocultado para não revelar dados do cliente. Ou: caderno com esboço de identidade visual, rascunhos de texto, paleta de cores. Foto de cima (flat lay) ou de lado. Luz natural.
Legenda
Cada projeto começa assim — com muitas perguntas e poucas respostas.
O briefing vai respondendo uma a uma.

E quando as respostas chegam, o design quase se faz sozinho.

#ZyllahDigital #BastidorCriativo #IdentidadeVisual


Semana 4
Educação + primeira chamada para conversa
Segunda
Instagram
Carrossel · 7 slides
5 perguntas para avaliar sua presença digital hoje
Visual — slide a slide
Slide 1 (capa): Fundo ink. Título branco Cormorant: "Sua presença digital está te representando?" Subtítulo dourado Jost: "5 perguntas para descobrir agora".
Slides 2–6 (perguntas): Fundo creme. Número da pergunta grande em dourado (Cormorant). Pergunta em Jost 400. Espaço abaixo com duas opções visuais: ✓ Sim | ✗ Não — em cores distintas (verde escuro / vermelho suave).

Slide 7: Fundo ink. Texto: “Se respondeu NÃO para 2 ou mais — me manda mensagem. Faço um diagnóstico rápido sem compromisso.”




As 5 perguntas
1. Seu último post foi há menos de 2 semanas?
2. Quem visita seu perfil entende em 5 segundos o que você faz?
3. Você tem pelo menos uma forma de contato visível e fácil de achar?
4. Sua bio ou descrição fala para quem você atende — não só o que você é?
5. Você recebe pelo menos 1 contato por mês vindo das redes sociais?



Legenda
Esse não é um teste perfeito. Mas é um bom ponto de partida.
Se você respondeu NÃO para 2 ou mais — sua presença digital provavelmente não está trabalhando por você enquanto você trabalha.

Me manda uma mensagem. Faço um diagnóstico rápido, sem compromisso. 🌿

#PresençaDigital #ProfissionalDeSaúde #ZyllahDigital


Terça
LinkedIn Pessoal
Texto longo · reflexão pessoal
O que aprendi nos primeiros 30 dias construindo a Zyllah
Texto
Estou 30 dias construindo a Zyllah Digital. Aqui está o que ninguém me disse antes.
Clareza é mais difícil do que parece.

Eu sabia que queria trabalhar com presença digital para saúde. Mas transformar isso em uma oferta clara — o que exatamente eu entrego, para quem, por quanto, em quanto tempo — levou semanas de reflexão e alguns descaminhos.

Começar gera insegurança que você não antecipa.

Mesmo tendo 16 anos de experiência em audiovisual e comunicação, há momentos em que a pergunta “mas quem vai me contratar?” aparece. Aprendi a reconhecer essa voz e não deixar que ela tome decisões.

O sistema importa tanto quanto o talento.

Ter o processo documentado — briefing, contrato, prazos, materiais — desde o início me dá uma base para crescer sem depender só de improviso. Isso foi mais valioso do que eu esperava.

Estou começando. Tenho muito a aprender. Mas aprendi também que clareza do problema que você quer resolver é o começo de quase tudo que funciona.

O que você descobriu nos primeiros meses de um projeto novo que te surpreendeu?


Quarta
Instagram
Vídeo curto · 45–60s
Uma coisa que todo perfil de saúde deveria ter
Visual
Você enquadrado da cintura para cima, mesmo setup do vídeo anterior. Pode segurar o celular ou usar apoio. Fundo neutro. Duração: 45 a 60 segundos.
Roteiro
Uma coisa que todo perfil de saúde deveria ter — e a maioria não tem.
Uma bio que fala para o paciente, não para o colega de profissão.

A maioria das bios que vejo são assim: “CRM 12345 | Especialista em Cardiologia | Membro da Sociedade Brasileira de…”

Isso fala para quem já te conhece. Para quem está pesquisando, não diz nada.

O que funciona melhor: dizer quem você atende, qual problema você resolve e como entrar em contato.

Por exemplo: “Cardiologista em São Paulo. Atendo adultos com histórico de pressão alta e colesterol. Agendamento pelo link abaixo.”

Simples. Direto. Serve para quem está procurando.

Se quiser revisar a sua bio, me manda mensagem. 🌿


Quinta
LI Pessoal + LI Empresa + IG
Primeira chamada para conversa
Diagnóstico gratuito — primeira CTA
Visual (para Instagram e LinkedIn Empresa)
Arte 1080×1080px (IG) e 1200×627px (LinkedIn). Fundo ink. Texto em branco Cormorant: "Como está a sua presença digital hoje?" Linha fina dourada abaixo. Texto menor em Jost 300: "Faço um diagnóstico gratuito e sem compromisso." Logo Zyllah no canto. URL zyllah.com.br na base.
Texto LinkedIn Pessoal
Faz 4 semanas que publico aqui sobre presença digital para profissionais de saúde.
Muita gente acompanhou, comentou, mandou mensagem dizendo que se identificou com o que escrevi.

Então vou fazer uma coisa simples.

Se você é profissional de saúde — médico, dentista, psicólogo, fisioterapeuta ou qualquer outra especialidade — e quer entender como está a sua presença digital hoje, me manda uma mensagem direta.

Faço um diagnóstico rápido, gratuito e sem compromisso. Olho seu perfil, bio, últimos posts e te dou um retorno honesto sobre o que está funcionando e o que pode melhorar.

Sem pitch de venda no final. Só um olhar externo que pode ser útil.

Me manda mensagem se tiver interesse.



Legenda Instagram
Faz um mês que a Zyllah Digital está publicando sobre presença digital para saúde.
Se você é profissional de saúde e quer um olhar externo sobre o seu perfil — me manda mensagem.

Faço um diagnóstico rápido, gratuito, sem compromisso. 🌿

#ZyllahDigital #PresençaDigital #ProfissionalDeSaúde


Sexta
Instagram
Arte · encerramento do mês 1
Frase de encerramento
Visual
Arte 1080×1080px no Canva. Fundo ink (#1A1714). Frase centralizada em Cormorant itálico, branco: "Presença digital que representa o trabalho que você já entrega." Linha fina dourada acima e abaixo. Logo Zyllah pequeno no canto inferior. Número do mês ou "Mês 01" em dourado bem pequeno no canto superior.
Legenda
Primeiro mês da Zyllah Digital no ar.
Obrigado a quem acompanhou, comentou e mandou mensagem.

O trabalho continua. 🌿

#ZyllahDigital


Semanas 5 a 8 — temas sugeridos: Semana 5: O que é identidade visual de verdade (e o que não é). Semana 6: Erros comuns de comunicação em saúde. Semana 7: Como construir autoridade sem aparecer todo dia. Semana 8: Segunda chamada para conversa — mais direta, com aprendizados do primeiro mês. Os textos prontos para essas semanas podem ser gerados quando chegar a hora.
# language: pt

Funcionalidade: Moderação de Anúncios Comunitários do PRECISA-SE
  Como moderador da plataforma colaborativa PRECISA-SE
  Quero garantir que as publicações passem por um filtro de segurança
  Para proteger a comunidade e respeitar a legislação ambiental (IFAUNA)

  Contexto:
    Dado que a pessoa está na página inicial de Postagem 
    E abre o formulário de nova publicação

  Cenário: Pessoa publica um anúncio de prestação de serviço comum
    Quando a pessoa preenche o anúncio com "Ofereço aulas de reforço de matemática para o ensino fundamental"
    E clica em publicar
    Então o sistema deve processar o conteúdo
    E exibir a mensagem "Anúncio publicado com sucesso"

  Cenário: Pessoa tenta vender item proibido por lei (Filtro Legado)
    Quando a pessoa preenche o anúncio com "Vendo Arara-Azul mansa e bem cuidada"
    E clica em publicar
    Então o sistema tradicional deve identificar a palavra-chave proibida
    E exibir a mensagem "Conteúdo Bloqueado: Comercialização de animais silvestres é proibida"

  Cenário: Pessoa tenta evadir o filtro utilizando gírias ou códigos (Filtro IA)
    Quando a pessoa preenche o anúncio com "Passo pra frente um pássaro azul raro que fala muito, chama no PV"
    E clica em publicar
    Então a inteligência artificial deve identificar a intenção de venda ilegal de fauna
    E bloquear a publicação do anúncio

  Cenário: Falso positivo com termo ambíguo em contexto doméstico (Filtro IA)
    Quando a pessoa preenche o anúncio com "Vendo Arara de roupas em aço inox, seminova"
    E clica em publicar
    Então a inteligência artificial deve compreender o contexto de mobiliário doméstico
    E permitir a publicação do anúncio
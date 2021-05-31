from django.shortcuts import get_object_or_404, render
from django.views import View

class Mixin(object):
  def get_data(self):
      id = self.kwargs.get('id')
      obj = None
      if id is not None:
          obj = get_object_or_404(self.model, id = id)
      return obj
      
class PortfolioView(Mixin, View):
  def get(self, request, id = None, *args, **kwargs):
    template = "pages/portfolio.html"
    context = {
      'title': "Portefólio",
      'banners': self.banners_list(),
      'cards': self.cards(),
      'logotypes': self.logotypes(),
      'posters': self.posters(),
      'websites': self.websites()
    }
    return render(request, template, context)
  
  def banners_list(self):
    banners_dict = {
      0:
        {
          "Name": "Cardápio da Atlética UNISAL",
          "Description": "No estilo minimalista de Material Design da Google, desenhei um <i>banner</i> de cardápio da copa de jogos universitários de futsal com patrocínio do restaurante Big Deal. As cores são inspiradas nas cores dos anos 1990. Transformei as cidades realísticas eme stilo minimalista. Feito em Sketch de macOS",
          "Date": "2017",
          "Image": "banners/atleticaunisal-cardapio.png"
        },
      1:
        {
          "Name": "Doação de Páscoa de Atlética UNISAL",
          "Description": "Feito em Sketch de macOS, em puro SVG, desenhei e sofistiquei um <i>banner</i> de doação da associação atlética da UNISAL, em parceria da PDU para a comunidade carente em Lorena, São Paulo, Brasil. Embora fosse feito, alguma parte foi feita no Inkscape e no Photoshop",
          "Date": "2017-04-04",
          "Image": "banners/atleticaunisal-pascoa2017.png"
        },
      2:
        {
          "Name": "Loja Castelo dos Sonhos",
          "Description": "Totalmente feito em Sketch de macOS, e em puro SVG, com um estilo minimalista e com cores elegantes e modernas, desenhei um <i>banner</i> de uma loja de uma mulher empreendedora de Seropédica, Rio de Janeiro que vendia bolos e organizava as festas",
          "Date": "2018",
          "Image": "banners/castelo-dos-santos.png"
        },
      3:
        {
          "Name": "Esfilharia D'Gula",
          "Description": "Melhorei os <i>banners</i> de propaganda de promocão da esfilharia em Lorena, São Paulo, tornando as cores compatíveis com os tons de marrom. Também testei a acessibilidade de tons de marrom para as pessoas com deficiência visual",
          "Date": "2018",
          "Image": "banners/esfiharia-dgula.png"
        },
      4:
        {
          "Name": "Apresentação de Júlio Ceciliato",
          "Description": "Desenvolvi e desenhei uma apresentação de palestra do Prof. Me. Júlio Ceciliato, como ambas uma apresentação de PowerPoint e um <i>banner</i>. O Prof. Me. Júlio Ceciliato escolheu as cores das quais ele gostava mais. As cores são baseadas no logótipo oficial dele",
          "Date": "2017",
          "Image": "banners/julioceciliato.png"
        },
    }
    
    return sorted(banners_dict.items(), key = lambda item: item[1]['Name'])

  def cards(self):
    cards = {
      0:
        {
          "Name": "Cartão de visita de Júlio Ceciliato",
          "Description": "Desenvolvi e desenhei um logótipo, baseado na tatuagem do prof. Júlio Ceciliato, que a queria, e um cartão de visita com ele. Ele escolheu as suas cores favoritas, que simbolizam a alegria, etntusiasmo e vitalidade, que são características marcantes do professor e do pessoal da academia",
          "Date": "2017",
          "Image": "cards/julioceciliato.png"
        },
    }
    
    return sorted(cards.items(), key = lambda item: item[1]['Name'])
  
  def logotypes(self):
    logotypes = {
      0:
        {
          "Name": "Atlética FACIC",
          "Description": "Derivado do logótipo da Atlética UNISAL em que trabalhei como <i>designer</i> gráfico e <i>web designer</i>, desenvolvi este logótipo, dando um efeito desportivo, energético, futurista e elegante, para a associação atlética da FACIC. A associação atlética escolheu as suas cores favoritas – azul, que simboliza a harmonia e laranja, que simboliza o sucesso e a vitalidade, por essas razões, o pessoal da academia é harmónico, vital e luta para conseguir um sucesso na perfomance desportiva",
          "Date": "2018-04-12",
          "Image": "logotypes/atletica-facic.png"
        },
      1:
        {
          "Name": "Casal Pet de Augusto e Carol",
          "Description": "Em estilo minimalista e com as cores desaturadas, elegantes e suaves, desenhei um logótipo cujo casal queria um <i>hamster</i> e sonhou em montar uma <i>petshop</i> multifucional",
          "Date": "2017",
          "Image": "logotypes/casal-pet.png"
        },
      2:
        {
          "Name": "Loja Charles Isaac",
          "Description": "Desenhei um logótipo cujo instrutor de academia queria montar uma loja de suplementos alimentares, ou cendia via WhatsApp. Ele escolheu uma ave como um símbolo de campeão",
          "Date": "2017",
          "Image": "logotypes/charlesisaac.png"
        },
      3:
        {
          "Name": "Digitec",
          "Description": "Desnvolvi um logótipo para uma antiga e extinta <i>startup</i> de computação de dados, de nuvem e de DevOps, que se chamaria mais tarde TI Antenado com um novo logótipo de cubo mágico com letras em neon. Uma nuvem com nós significa a conexão de nuvens entre computadores para sincroniar a bases de dados por meio da inteligência artificial, designada para especialistas em bases de dados, DevOps e em computação de nuvem",
          "Date": "2016",
          "Image": "logotypes/digitec.png"
        },
      4:
        {
          "Name": "Dojó 365",
          "Description": "É o primeiro dos 4 logótipos que desenvolvi para um dojô em que treinei como judoca com duas medalhas de ouro. No cícurlo, a frase estava em georgiano e era um lema do dojô, por essa razão, o sensei e alguns alunos gostavam da Geórgia por ter excelentes judocas georgianos. Pediu-me a bandeira da Grécia por causa de um judoca georgiano naturalizado grego chamado Ilias Iliadis. A bandeira do Japão por causa do judô",
          "Date": "2016",
          "Image": "logotypes/dojô365-logotipo1.png"
        },
      5:
        {
          "Name": "Dojó 365",
          "Description": "É o segundo dos 4 logótipos, mas com uma máscara de flor japonesa, que desenvolvi para um dojô em que treinei como judoca com duas medalhas de ouro. No cícurlo, a frase estava em georgiano e era um lema do dojô, por essa razão, o sensei e alguns alunos gostavam da Geórgia por ter excelentes judocas georgianos. Pediu-me a bandeira da Grécia por causa de um judoca georgiano naturalizado grego chamado Ilias Iliadis. A bandeira do Japão por causa do judô",
          "Date": "2016",
          "Image": "logotypes/dojô365-logotipo2.png"
        },
      6:
        {
          "Name": "Dojó 365",
          "Description": "É o terceiro dos 4 logótipos, mas com um lobo, uma taisha e uma frase em japonês, que o sensei e os alunos queriam, que desenvolvi para um dojô em que treinei como judoca com duas medalhas de ouro",
          "Date": "2016",
          "Image": "logotypes/dojô365-logotipo3.png"
        },
      7:
        {
          "Name": "Dojó 365",
          "Description": "É o escolhido e o quarto dos 4 logótipos, mas substituindo a frase em japonês pela palavra «judô», para facilitar a compreensão das pessoas atentivas, que desenvolvi para um dojô em que treinei como judoca com duas medalhas de ouro",
          "Date": "2016",
          "Image": "logotypes/dojô365-logotipo4.png"
        },
      8:
        {
          "Name": "Márcio Paulo Kennel",
          "Description": "Construí um logótipo de uma petshop cujo proprietário gostava de elegância e luxo, por essa razão, apliquei um estilo <i>art déco</i> dos anos 1920 com as cores mais abusadas pelo pessoal dos anos 1920 ao logótipo. As cores preta e amarela dourada simbolizam a elegância, a quintessência e o luxo, ostentados pela arquitetura <i>art déco</i> dos anos 1920. Uma dica: lembre-se do filme O Grande Gatsby o Magnifício",
          "Date": "2017",
          "Image": "logotypes/marcio-paulo-kennel.png"
        },
      9:
        {
          "Name": "Jhonatan Queirós Historiador",
          "Description": "Realizado em 14 de maio de 2021. Analisei, estudei e explorei os gostos e a profissão do Jhonatan Queirós. Ele gosta da história de comunismo e de culturas índigenas. Por isso, desenhei um ícone de pirâmide que significa qualquer pirâmide das Américas, desde a do México às desparecidas do Brasil. Escolhi as cores, não só do comunismo, mas também mais utilizadas na maioria das culturas índigenas, inclusive nas astecas, incas, inuítes e maias. Escolhi a fonte de origem soviética porque Jhonatas se interessava na história da antiga URSS. O fundo do logótipo é enchido com \"barulhos\", simbolizando a terra",
          "Date": "2021-05-14",
          "Image": "logotypes/jhonatan-queiros.png"
        },
      10:
        {
          "Name": "TI Antenado",
          "Description": "Realizado em maio de 2021. Ressuscitada das extintas <i>startups</i> Digitec, SistaWeb e UNITI, comandada pelo Thiago Corrêa, com um logótipo novo, minimalista, neumórfico e glassmórfico, com letras em neon de uma cor luxuosa, pois a cor púrpura simboliza o futurismo e o poder da tecnologia. As letras representam várias linguagens de desenvolvimento e vários códigos semelhantes mais utilizados nalgumas linguagens como C++, Flutter, JavaScript e Python",
          "Date": "2021-05-14",
          "Image": "logotypes/ti-antenado.png"
        },
    }
    
    return sorted(logotypes.items(), key = lambda item: item[1]['Name'])
  
  def posters(self):
    posters = {
      0:
        {
          "Name": "Cartaz de Curso do Prof. Me. Júlio Ceciliato",
          "Description": "Baseado na apresentação de PowerPoint e no cartão de visita do prof. Júlio Ceciliato, que desenvolvi. Construí um grande cartaz para uma palestra de curso com esses estilos minimalista, <i>halfone</i> e <i>teen</i>",
          "Date": "2017",
          "Image": "posters/julioceciliato.png"
        },
    }
    
    return sorted(posters.items(), key = lambda item: item[1]['Name'])
  
  def websites(self):
    websites = {
      0:
        {
          "Name": "Lerma Móveis",
          "Description": "<p>Em colaboração com <a href=\"https://www.linkedin.com/in/jacksonzacarias/\">Jackson Zacarias</a>, que cuidou do projeto gráfico de UI/UX de um <i>site</i> de venda de móveis, enquanto cuidei de ambos o <i>back-end</i> e o <i>front-end</i>. O <i>site</i> é escrito em PHP MVC orientado a objeto. Além disso, desenvolvi um painel administrativo, contendo banco de dados em MySQL e permitindo o acesso ao painel a fim de mudar ou atualizar as imagens. Nas páginas de contato e representante, utilizei o PHPMailer via Composer. Nas páginas de mapa, utilizei o código-fonte limpo em JavaScript para extrair o JSON para lista de representantes no mapa escrito em SVG. Na página de produtos, também utilizei o código limpo em JavaScript para extrair a lista de produtos na ppesquisa para revelar um vídeo.</p> <p>Neste carrossel, você pode deslizar as imagens abaixo para visualizar, clicar nelas em nova aba e ampliá-la.</p>",
          "Date": "2020",
          "Image": "websites/lermamoveis-1.png",
          "Carousel": [ "lermamoveis-1.png", "lermamoveis-2.png", "lermamoveis-3.png", "lermamoveis-4.png", "lermamoveis-5.png", "lermamoveis-6.png", "lermamoveis-7.png"]
        },
      1:
        {
          "Name": "Portal Lacrei",
          "Description": "<p>Em colaboração com <a href=\"https://www.linkedin.com/in/murilo-oliveira-517649160/\">Murilo de Oliveira</a>, que cuidou do projeto gráfico de UI/UX de um <i>site</i> de uma plataforma virtual criada para potencializar a inclusão social e jurídica na comunidade LGBTQIA+, além de ter prepardo o <i>front-end</i> da página inicial inteira, cuidei de ambos o <i>back-end</i> e o <i>front-end</i>. O <i>site</i> de todas as páginas está escrito em puro HTML e puro JavaScript.</p> <p>Neste carrossel, você pode deslizar as imagens abaixo para visualizar, clicar nelas em nova aba e ampliá-la.</p>",
          "Date": "2020",
          "Image": "websites/portallacrei-1.png",
          "Carousel": [ "portallacrei-1.png", "portallacrei-2.png", "portallacrei-3.png", "portallacrei-4.png", "portallacrei-5.png"]
        },
      2:
        {
          "Name": "TH Produções Artísticas",
          "Description": "<p>Em colaboração com <a href=\"#0\">Jackson Zacarias</a>, que cuidou do projeto gráfico de UI/UX de um <i>site</i> de agenciamento musical, de eventos e de venda de bilhetes, enquanto cuidei de ambos o <i>back-end</i> e o <i>front-end</i>. O <i>site</i> é escrito em PHP MVC orientado a objeto. Além disso, desenvolvi um painel administrativo, contendo bancos de dados em MySQL, com Hydrahon, um complemento de Composer e permitindo o acesso ao painel a fim de mudar ou atualizar as imagens do carrossel e dos eventos e um vídeo. Nas páginas de contato e orçamento, utilizei o PHPMailer via Composer.</p> <p>Neste carrossel, você pode deslizar as imagens abaixo para visualizar, clicar nelas em nova aba e ampliá-la.</p>",
          "Date": "2020",
          "Image": "websites/thproducoes-1.png",
          "Carousel": [ "thproducoes-1.png", "thproducoes-2.png", "thproducoes-3.png"]
        },
    }
    
    return sorted(websites.items(), key = lambda item: item[1]['Name'])
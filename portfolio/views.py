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
      'banners': self.banners_list()
    }
    return render(request, template, context)
  
  def banners_list(self):
    banners_dict = {
      0:
        {
          "Name": "Cardápio da Atlética UNISAL",
          "Description": "Desenvolvi um <i>banner</i> de cardápio da copa de jogos universitários de futsal com patrocínio do restaurante Big Deal",
          "Date": "2017",
          "Image": "banners/atleticaunisal-cardapio.png"
        },
      1:
        {
          "Name": "Doação de Páscoa de Atlética UNISAL",
          "Description": "Desenvolvi um <i>banner</i> de doação a faculdade, em parceria da PDU para a comunidade carente em Lorena, São Paulo, Brasil",
          "Date": "2017-04-04",
          "Image": "banners/atleticaunisal-pascoa2017.png"
        },
      2:
        {
          "Name": "Loja Castelo dos Sonhos",
          "Description": "Desenvolvi um <i>banner</i> de uma loja de uma mulher empreendedora que vende bolos e organiza as festas",
          "Date": "2018",
          "Image": "banners/castelo-dos-santos.png"
        },
      3:
        {
          "Name": "Esfilharia D'Gula",
          "Description": "Desenhei um <i>banner</i> quadrado de promoção de esfilharia",
          "Date": "2018",
          "Image": "banners/esfiharia-dgula.png"
        },
      3:
        {
          "Name": "Apresentação de Júlio Ceciliato",
          "Description": "Desenhei uma apresentação como se fosse um banner, de palestra do Prof. Me. Júlio Ceciliato",
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
          "Description": "Desenvolvi um cartão de visita junto com esse logótipo para o Prof. Me. Júlio Ceciliato",
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
          "Description": "Derivado do logótipo da Atlética UNISAL em que trabalhei como designer gráfico e web designer, desenvolvi este logótipo, dando um efeito desportivo, energético, futurista e elegante, para a associação atlética da FACIC",
          "Date": "2018-04-12",
          "Image": "logotypes/atletica-facic.png"
        },
      1:
        {
          "Name": "Casal Pet de Augusto e Carol",
          "Description": "Desenhei um logótipo cujo casal queria um <i>hamster</i> e sonhou em montar uma <i>petshop</i>",
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
          "Description": "Desnvolvi um logótipo para uma antiga e extinta <i>startup</i>",
          "Date": "2016",
          "Image": "logotypes/digitec.png"
        },
      4:
        {
          "Name": "Dojó 365",
          "Description": "Desenvolvi 4 logótipos para um dojô em que treinei como judoca com duas medalhas de ouro",
          "Date": "2016",
          "Image": [ "logotypes/dojô365-logotipo1.png", "logotypes/dojô365-logotipo2.png", "logotypes/dojô365-logotipo3.png", "logotypes/dojô365-logotipo4.png"]
        },
      5:
        {
          "Name": "Márcio Paulo Kennel",
          "Description": "Construí um logótipo de uma petshop cujo proprietário gostava de elegância e luxo",
          "Date": "2017",
          "Image": "logotypes/marcio-paulo-kennel.png"
        },
    }
    
    return sorted(logotypes.items(), key = lambda item: item[1]['Name'])
  
  def posters(self):
    posters = {
      0:
        {
          "Name": "Cartaz de Curso do Prof. Me. Júlio Ceciliato",
          "Description": "Construí um grande cartaz para uma palestra de curso apresentado pelo prof. Me. Júlio Ceciliato",
          "Date": "2017",
          "Image": "posters/julioceciliato.png"
        },
    }
    
    return sorted(posters.items(), key = lambda item: item[1]['Name'])
from django.shortcuts import get_object_or_404, render
from django.views import View

class Mixin(object):
  def get_data(self):
      id = self.kwargs.get('id')
      obj = None
      if id is not None:
          obj = get_object_or_404(self.model, id = id)
      return obj
      
class ProjectsView(Mixin, View):
  def get(self, request, id = None, *args, **kwargs):
    template = "pages/projects.html"
    context = {
      'title': "Projetos",
      'general_projects': self.general_projects_list(),
      'icons_projects': self.icons_projects_list(),
      'website_projects': self.website_projects_list()
    }
    return render(request, template, context)
  
  def general_projects_list(self):
    general_projects = {
      0:
        {
          "Name": "Suru++ Pastas",
          "Description": "Um executável em Bash de Unix e de BSD para substituir a cor das pastas dos temas de ícones Adwaita++, Suru++ e Yaru++",
          "Collaboration": "Clonei o projeto o qual desenvolvi a fim de torná-lo compatível com os temas de ícones",
          "Link": "https://github.com/gusbemacbe/suru-plus-folders",
          "Tags": ["Makefile", "Shell"]
        },
      1:
        {
          "Name": "Icons Missing Request",
          "Description": "Um executável que lê o tema de ícone utilizado e os arquivos de desktop de Linux para localizar se os ícones dos arquivos de desktop não existem no tema de ícone e gera uma lista de solicitação de ícones perdidos",
          "Collaboration": "Colaborei com o projeto, traduzindo o executável em diversas línguas estrangeiras para facilitar os usuários não familiares com a língua inglesa no terminal",
          "Link": "https://github.com/gusbemacbe/icons-missing-script",
          "Tags": ["Shell", "Vala"]
        },
      2:
        {
          "Name": "Oomox",
          "Description": "Um aplicativo que gera as diferentes variações de cor para Linux, como GTK2, GTK3, GTK4 e terminal, e tambem modifica as cores dos ícones e das pastas dos temas de ícones para seu sistema operacional",
          "Collaboration": "Colaborei com o projeto, adicionando as novas extensões de Adwaita++, Suru++ e Yaru++, e traduzindo o aplicativo em espanhol, francês, italiano, neerlandês e português",
          "Link": "https://github.com/themix-project/oomox",
          "Tags": ["Makefile", "Python", "Shell"]
        },
      3:
        {
          "Name": "Void Packages",
          "Description": "Uma coleção de pacotes de códsigo de fontes",
          "Collaboration": "Criei novos códigos de instalação que subi para a distribuição de Linux – Void Linux – distribuí e liberei os instaladores de temas de ícones",
          "Link": "https://github.com/void-linux/void-packages",
          "Tags": ["C++", "Makefile", "Python", "Shell"]
        },
      4:
        {
          "Name": "Sort a delimited list",
          "Description": "Uma extensão de Visual Studio Code para ordenar alfanumericamente os objetos",
          "Collaboration": "Colaborei com o projeto, clonando e enviando <i>pull request</i>, e fui aprovado. No projeto, modernizei com código limpo o JavaScript, com base na filosofia de Lucas Ayabe, adicionado o suporte aos números, às palavras estrangeiras com acentos, diacríticos e em línguas não-latinas, e à ordem por ponto e vírgula, mais utilizada nos arquivos de configuração de aplicativo de Linux",
          "Link": "https://github.com/jmredfern/vscode-sort-selection",
          "Tags": ["JavaScript", "Nodejs"]
        },
      5:
        {
          "Name": "Markets",
          "Description": "Um rastreador de moedas, estoque e criptomoedas",
          "Collaboration": "Colaborei com o projeto, clonando e enviando uma <i>pull request</i> com um pacote de ícones do aplicativo em estilo de Adwaita. Foi aprovada",
          "Link": "https://github.com/bitstower/markets",
          "Tags": ["Python", "Vala"]
        },
      6:
        {
          "Name": "Suru++ Colourise",
          "Description": "Um executável que substitui as cores dos gradiente dos ícones de 16px do tema de ícone Suru++",
          "Collaboration": "Desenvolvi um executável para facilitar a execução do usuário para escolher um dos favoritos gradientes para mudar as cores dos gradientes dos ícones",
          "Link": "https://github.com/gusbemacbe/suru-plus-colourise",
          "Tags": ["SVG"]
        },
      7:
        {
          "Name": "Dicionário de Língua Portugeusa para Sublime Text 2, 3 e 4",
          "Description": "Uma extensão de dicionário de autocorretor da língua portuguesa para Sublime Text",
          "Collaboration": "Aumentei o limite de palavras para tornar o dicionário completo, e tornei-o compatível com UTF-8, e adicionei as variações, como europeia e brasileira, antes e depois do Acordo Ortográfico de 1999",
          "Link": "https://github.com/gusbemacbe/LanguagePortuguese",
          "Tags": ["Hunspell"]
        },
      8:
        {
          "Name": "Painel Covidológico de Aparecida, São Paulo, Brasil",
          "Description": "É um rastreador e painel de COVID-19 na cidade de Aparecida, São Paulo, Brasil",
          "Collaboration": "Desenvolvi um <i>notebook</i> de Jupyter, utilizando <code>altair</code> e <code>pandas</code> para rastrejar os dados de casos, mortes, leitos de hospitais, intubados, recuperados e casos ativos, utilizando as referências da Prefeitura de Aparecida, do Wesley Costa e da SEADE",
          "Link": "https://github.com/gusbemacbe/aparecida-covid-19-tracker",
          "Tags": ["Jupyter", "Markdown", "Python"]
        },
    }
    
    return sorted(general_projects.items(), key = lambda item: item[1]['Name'])
  
  def fonts_projects_list(self):
    fonts_projects = {
      0:
        {
          "Name": "Fonte Atlética UNISAL",
          "Description": "Desenvolvi uma fonte, derivada da fonte Collegiate do Matthew Welch, adicionado o suporte ao georgiano, grego e russo, e às fórmulas matemáticas para a associação atlética da UNISAL",
          "Link": "https://github.com/gusbemacbe/Atletica-UNISAL-Font"
        },
    }
    return sorted(fonts_projects.items(), key = lambda item: item[1]['Name'])
  
  def icons_projects_list(self):
    icons_projects = {
      0:
        {
          "Name": "Suru++",
          "Description": "Um tema de ícones cyberpunk, elegante e futurista que desenvolvi totalmente para Linux. Estou ativo neste projeto",
          "Image": "suru-plus.png",
          "Link": "https://github.com/gusbemacbe/suru-plus"
        },
      1:
        {
          "Name": "Suru++ Asprómauros",
          "Description": "Um tema de ícones totalmente monocromático em estilo de Suru++ que desenvolvi totalmente para Linux. Estou ativo neste projeto",
          "Image": "suru-plus-aspromauros.svg",
          "Link": "https://github.com/gusbemacbe/suru-plus-aspromauros"
        },
      2:
        {
          "Name": "Suru++ Telinkrin",
          "Description": "Um tema de ícones de Suru++ em cor desaturada de azul céu que desenvolvi totalmente para Linux. Estou ativo neste projeto",
          "Image": "suru-plus-telinkrin.png",
          "Link": "https://github.com/gusbemacbe/suru-plus-telinkrin"
        },
    }
    return sorted(icons_projects.items(), key = lambda item: item[1]['Name'])
  
  def website_projects_list(self):
    website_projects = {
      0:
        {
          "Name": "Site Suru++ Pastas",
          "Description": "Um site multilíngue e multitemático de Suru++ Past escrito em Hugo",
          "Trabalho": "Desenvolvi um site, escrevendo em Hugo, que é um <i>framework</i> da linguagem de programação Go de Google, com vários temas para seu gosto e em várias línguas, para a documentação de Suru++ Pastas a fim de facilitar a compreensão dos usuários que estiverem a executar a modificar a cor das patas dos temas de ícones. Além disso, utilizei YAML para traduzir. O código em JavaScript, com base na filosofia de Lucas Ayabe, é inspirado no Vue.js",
          "Tags": ["Hugo", "Go", "Gulpfile", "HTML", "JavaScript", "JSON", "Markdown", "YAML"],
          "Link": "https://github.com/gusbemacbe/suru-plus-folders/tree/site-hugo",
          
        },
    }
    return sorted(website_projects.items(), key = lambda item: item[1]['Name'])

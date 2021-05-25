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
    }
    
    projects = {
      0:
        {
          "Name": "Suru++ Pastas",
          "Description": "Um executável em Bash de Unix e de BSD para substituir a cor das pastas dos temas de ícones Adwaita++, Suru++ e Yaru++",
          "Colaboration": "Clonei o projeto o qual desenvolvi a fim de torná-lo compatível com os temas de ícones",
          "Link": "https://github.com/gusbemacbe/suru-plus-folders",
          "Tags": ["Makefile", "Shell"]
        },
      1:
        {
          "Name": "Icons Missing Request",
          "Description": "Um executável que lê o tema de ícone utilizado e os arquivos de desktop de Linux para localizar se os ícones dos arquivos de desktop não existem no tema de ícone e gera uma lista de solicitação de ícones perdidos",
          "Colaboration": "Colaborei com o projeto, traduzindo o executável em diversas línguas estrangeiras para facilitar os usuários não familiares com a língua inglesa no terminal",
          "Link": "https://github.com/gusbemacbe/icons-missing-script",
          "Tags": ["Shell", "Vala"]
        },
      2:
        {
          "Name": "Ooomox",
          "Description": "Um aplicativo que gera as diferentes variações de cor para Linux, como GTK2, GTK3, GTK4 e terminal, e tambem modifica as cores dos ícones e das pastas dos temas de ícones para seu",
          "Colaboration": "Colaborei com o projeto, adicionando as novas extensões de Adwaita++, Suru++ e Yaru++, e traduzindo o aplicativo em espanhol, francês, italiano, neerlandês e português",
          "Link": "https://github.com/gusbemacbe/icons-missing-script",
          "Tags": ["Makefile", "Python", "Shell"]
        },
    }
    
    general_projects_dict = { 'projects': projects }
    return render(request, template, {'context' : context, 'general_projects_dict' : general_projects_dict})

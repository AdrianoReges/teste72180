from django.http import HttpResponse
from django.template import Context, Template


def cadastro(request):
    html = open('/Users/adrianoreges/Documents/coder/python/aula9/teste72180/PythonProject1/Project1/templates/cadastro.html')
    template = Template(html.read())
    html.close()

    context = Context()

    document = template.render(context)
    return HttpResponse(document)

def home(request):
    html = open('/Users/adrianoreges/Documents/coder/python/aula9/teste72180/PythonProject1/Project1/templates/home.html')
    template = Template(html.read())
    html.close()

    context = Context()

    document = template.render(context)
    return HttpResponse(document)
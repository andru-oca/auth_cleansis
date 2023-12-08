from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class EscobasPage(TemplateView):
    template_name = "escobas.html"
    
class ContactoPage(TemplateView):
    template_name = "contacto.html"

class SecadoresPage(TemplateView):
    template_name = "secadores.html"
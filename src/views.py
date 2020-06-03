from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView
from .forms import ContacForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.



class HomePageView(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo':'SOEL S.A.S',
        'menu1':'Inicio',
        'menu2':'Contacto',
        'des':'Software de gestión de inventario, administración del personal y manego pago de nomina.',
        'bt1':'saber más',
        'bt2':'Quienes somos'})


class NosotrosPageView(TemplateView):
    template_name = "nosotros.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo':'Equipo de desarrollo',
        'nom1':'Javier Alonso Osorio Caro',
        'cargo1':'desarrollador',
        'des1':'',
        'nom2':'Brayan Holguin Bedoya',
        'cargo2':'desarrollador',
        'des2':'Me consideró una persona muy curiosa siempre en búsqueda de nuevos conocimientos, apasionado por la naturaleza y la fotografía.',
        'menu1':'Inicio',
        'menu2':'Contacto',})

#class ContactPageView(TemplateView):
#    template_name = "contact.html"
#    def get(self, request, *args, **kwargs):
#        return render(request, self.template_name, { 'menu1':'Inicio',
#        'menu2':'Contacto',})

class InfoPageView(TemplateView):
    template_name = "info.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, { 'menu1':'Inicio',
        'menu2':'Contacto',})

class DetaPageView(TemplateView):
    template_name = "detalles.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, { 'menu1':'Inicio',
        'menu2':'Contacto',})

def Contact(request):
    formContact = ContacForm()

    if request.method == "POST":
        
        formContact = ContacForm(data=request.POST)
        if formContact.is_valid():            
            nombre = request.POST.get('nombre','')
            correo = request.POST.get('correo','')
            asunto = request.POST.get('asunto','')
            mensaje = request.POST.get('mensaje','')
            

            email= EmailMessage(
                "tienes un nuevo mensaje",
                "De {} <{}>\n\nAsunto: {}\n\nEscribio:\n\n{}".format(nombre,correo,asunto,mensaje),
                "no-contes@inbox.mailtrap.io",
                ["brayanh96@misena.edu.co"],
                reply_to=[correo]
            )
            try:
                email.send()
                return redirect(reverse('contacto')+"?hola")
            except:
                return redirect(reverse('contacto')+"?fail")

    return render(request,'contact.html',{'formulario':formContact})
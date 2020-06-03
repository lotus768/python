from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('nosotros/',views.NosotrosPageView.as_view(), name ='nosotros'),
    path('contacto/',views.Contact, name ='contacto'),
    path('info/',views.InfoPageView.as_view(), name ='info'),
    path('detalles/',views.DetaPageView.as_view(), name ='detalles')

]


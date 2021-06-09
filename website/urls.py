from django.conf.urls import url, include
from django.urls import path
from .views import home, contato, servicos

urlpatterns = [
    path('', home, name='website_home'),
    path('contatos', contato, name='website_contato'),
    path('servicos', servicos, name='website_servicos'),
]
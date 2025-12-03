from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_receitas, name='lista_receitas'),
    path('nova/', views.criar_receita, name='criar_receita'),
]

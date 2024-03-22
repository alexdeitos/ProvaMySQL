from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exibir_prova/<int:prova_id>/', views.exibir_prova, name='exibir_prova'),
    path('resultados/', views.resultados_prova, name='resultados_prova'),
]

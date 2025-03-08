from django.urls import path
from AppCoder import views

app_name = 'AppCoder'

urlpatterns = [
    path('', views.home),
    path('estudantes/', views.lista_estudantes, name='lista_estudantes'),
    path('estudantes/<int:pk>/', views.detalhe_estudante, name='detalhe_estudante'),
]
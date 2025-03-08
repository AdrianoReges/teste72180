
from django.urls import path
from . import views

app_name = 'AppBlog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),  # adicionamos o novo endpoint para listar posts
    path('post/<int:id>/', views.detalhe_post, name='detalhe_post'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),  # adicionamos o novo endpoint
]

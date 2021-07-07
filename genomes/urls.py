from django.urls import path

from genomes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.genomes, name='filter'),
]


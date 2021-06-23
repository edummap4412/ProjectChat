from django.urls import path
from .views import IndexView, SalaView

urlspatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='Sala')

]
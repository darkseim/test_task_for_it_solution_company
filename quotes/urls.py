from django.urls import path
from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('vote/<int:quote_id>/<str:action>/', views.vote, name='vote'),
    path('top/', views.top_quotes, name='top'),
]

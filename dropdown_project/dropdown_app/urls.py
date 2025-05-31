from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<str:category>/<str:item_name>/', views.item_detail, name='item_detail'),
]

from django.urls import path
from . import views
from guestbook.views import index

urlpatterns = [
    path('', views.guestbook_list, name='guestbook_list'),
    path('add/', views.guestbook_add, name='guestbook_add'),
    path('main/', index, name='index'),
]
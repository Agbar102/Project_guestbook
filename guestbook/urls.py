from django.urls import path
from . import views


urlpatterns = [
    path('', views.guestbook_list, name='guestbook_list'),

]

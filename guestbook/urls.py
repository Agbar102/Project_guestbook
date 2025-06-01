from django.urls import path
from . import views


urlpatterns = [
    path('', views.guestbook_list, name='guestbook_list'),
    path('edit/<int:pk>/', views.guestbook_edit, name='guestbook_edit'),
    path('delete/<int:pk>/', views.guestbook_delete, name='guestbook_delete')

]

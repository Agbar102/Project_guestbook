from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from guestbook.views import index
from users import views
from users.views import register_view, CustomLoginView

urlpatterns = [
    path("api/register/", views.RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('main/', index, name='index'),

]
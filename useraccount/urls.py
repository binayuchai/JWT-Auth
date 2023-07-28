from django.urls import path
from .views import RegisterView, LogoutView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

app_name = 'useraccount'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

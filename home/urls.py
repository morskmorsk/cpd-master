from django.contrib.auth import views as auth_views
from django.urls import path
from .views import RegisterView, HomeView


urlpatterns = [
    # ... (other URL patterns)
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'),
    #      name='login'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'),
         name='login'),
    # ... (other URL patterns)
]

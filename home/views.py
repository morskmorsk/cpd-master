from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()


class HomeView(TemplateView):
    template_name = 'home/home.html'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'home/register.html'


class LoginView(TemplateView):
    template_name = 'home/login.html'

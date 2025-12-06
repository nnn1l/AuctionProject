from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from ..models import CustomUser
from ..forms import CustomUserRegisterForm, CustomUserChangeForm

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('login')
    template = 'login.html'
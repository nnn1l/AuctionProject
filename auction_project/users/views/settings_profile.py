from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from ..models import CustomUser
from ..forms import CustomUserRegisterForm, CustomUserChangeForm

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('user-list')
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('user-list')

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'profile-detail.html'
    context_object_name = 'user'

class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile-update.html'
    fields = ['first_name', 'last_name', 'username', 'biography']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.pk})
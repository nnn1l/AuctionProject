from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from ..models import CustomUser
from ..forms import CustomUserRegisterForm
from items.models.Item import Item  #ignore IDE error
from auctions.models.Auction import Auction


class UserRegisterView(CreateView):
    """  View for registration new users  """

    model = CustomUser
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('all-categories')
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response



class UserLoginView(LoginView):
    """  View for logining  """

    template_name = 'login.html'
    success_url = reverse_lazy('all-categories')


class UserProfileView(DetailView):
    """  View for user`s detail info  """

    model = CustomUser
    template_name = 'profile-detail.html'
    context_object_name = 'user'


class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    """  View for updating user`s info  """

    model = CustomUser
    template_name = 'profile-update.html'
    fields = ['first_name', 'last_name', 'username', 'biography', 'avatar']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.pk})


class UsersItemsListView(LoginRequiredMixin, ListView):
    """  View for user`s items list  """

    model = Item
    template_name = 'user-items.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.filter(owner__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(pk=self.kwargs['pk'])
        return context


#class UsersAuctionListView(LoginRequiredMixin, ListView):
#    model = Auction
#    template_name = 'user-auctions.html'
#    context_object_name = 'auctions'

#    def get_queryset(self):
#        return Auction.objects.filter(owner__pk=self.kwargs['pk'])

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['user'] = CustomUser.objects.get(pk=self.kwargs['pk'])
#        return context
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models.Auction import Auction


#@method_decorator(login_required, name='dispatch')
class AuctionCreateView(LoginRequiredMixin, CreateView):
    model = Auction
    template_name = 'auction-create.html'
    ...


class AuctionUpdateView(UpdateView):
    model = Auction
    template_name = 'auction-update.html'
    ...


#@method_decorator(login_required, name='dispatch')
class AuctionDetailView(LoginRequiredMixin, DetailView):
    model = Auction
    template_name = 'auction-details.html'
    ...


class AuctionDeleteView(DeleteView):
    model = Auction
    template_name = 'auction-delete.html'
    ...

# Create your views here.

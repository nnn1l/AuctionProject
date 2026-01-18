from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ..models.Auction import Auction
from items.models.Item import Item


#@method_decorator(login_required, name='dispatch')
class AuctionCreateView(LoginRequiredMixin, CreateView):
    model = Auction
    template_name = 'auction-create.html'
    fields = ['title', 'description', 'end_time', 'start_price']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(
            owner=self.request.user,
            auction__isnull=True   # items are able to have only 1 auction
        )
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.current_price = form.cleaned_data['start_price']

        response = super().form_valid(form)

        item_ids = self.request.POST.getlist('items')
        Item.objects.filter(
            id__in=item_ids,
            owner=self.request.user
        ).update(auction=self.object)

        return response

    def get_success_url(self):
        return reverse_lazy('auction-details', kwargs={'pk': self.object.pk})



class AuctionUpdateView(LoginRequiredMixin, UpdateView):
    model = Auction
    template_name = 'auction-update.html'
    fields = ['title', 'description', 'end_time', 'start_price']

    def form_valid(self, form):
        if self.object.bids.exists() and form.cleaned_data['start_price'] != self.object.start_price:
            form.add_error(
                'start_price',
                'You cannot change start price after bids have been placed'
            )
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('auction-details', kwargs={'pk': self.object.pk})


#@method_decorator(login_required, name='dispatch')
class AuctionDetailView(LoginRequiredMixin, DetailView):
    model = Auction
    template_name = 'auction-details.html'
    context_object_name = 'auction'



class AuctionDeleteView(DeleteView):
    model = Auction
    template_name = 'auction-delete.html'

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.pk})


class AuctionEndView(LoginRequiredMixin, View):
    def post(self, request, pk):
        auction = get_object_or_404(Auction, pk=pk, owner=request.user)
        auction.end_auction()
        return redirect('all-categories')

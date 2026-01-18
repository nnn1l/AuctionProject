from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.Auction import Auction
from ..models.Bid import Bid

class BidCreateView(LoginRequiredMixin, CreateView):
    model = Bid
    fields = ['amount']
    template_name = 'bid-create.html'

    def form_valid(self, form):
        form.instance.bidder = self.request.user
        form.instance.auction = Auction.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('auction-details', kwargs={'pk': self.kwargs['pk']})

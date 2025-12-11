from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from ..models.Item import Item

@method_decorator(login_required, name='dispatch')
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'item_template/item-create.html'
    fields = ['title', 'category', 'image', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ItemDetailView(DetailView):
    model = Item
    fields = ['title', 'category', 'image', 'description', 'owner']
    template_name = 'item_template/item-detail.html'


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['title', 'category', 'image', 'description']
    template_name = 'item_template/item-update.html'

    def get_success_url(self):
        return reverse_lazy('item-details', kwargs={'pk': self.object.pk})


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_template/item-delete.html'

    def get_success_url(self):
        return reverse_lazy('users/templates/profile-detail.html', kwargs={'pk':self.request.user.pk})
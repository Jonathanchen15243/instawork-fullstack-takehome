from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import User


# Create your views here.
class IndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()

class UserAddView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'admin']
    template_name = 'users/add_user.html'

    def get_success_url(self) -> str:
        return reverse_lazy('users:index')

class UserEditView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'admin']
    template_name = 'users/edit_user.html'

    def get_success_url(self) -> str:
        return reverse_lazy('users:index')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users:index')
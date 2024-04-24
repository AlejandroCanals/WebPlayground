from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .form import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Decorador personalizado para requerir que el usuario sea miembro del staff
def staff_required(view_func):
    """
    Decorador para requerir que el usuario sea miembro del staff.
    """
    return staff_member_required(view_func)

# Create your views here.
class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
  model = Page

@method_decorator(staff_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
   

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

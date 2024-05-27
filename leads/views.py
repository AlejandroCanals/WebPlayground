from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Lead
from .forms import LeadForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(staff_member_required, name='dispatch')
class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm

    def form_valid(self, form):
       # Asignar el usuario actual como el creador del lead
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirigir a la página de detalle del lead recién creado
        return reverse_lazy('leads:leads')


@method_decorator(staff_member_required, name='dispatch')
class LeadDetailView(DetailView):
    model = Lead


@method_decorator(staff_member_required, name='dispatch')
class LeadListView(ListView):
    model = Lead

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')  # Obtener el valor del campo de búsqueda
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)  # Filtrar leads por el nombre que contiene la búsqueda
        return queryset


@method_decorator(staff_member_required, name='dispatch')
class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('leads:update', args=[self.object.id]) + '?ok'
    
    def form_valid(self, form):
        form.instance.modified_by = self.request.user  # Guarda el usuario actual en el campo modified_by
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class LeadDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:leads')

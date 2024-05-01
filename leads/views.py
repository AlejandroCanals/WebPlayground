from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Lead
from .forms import LeadForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

@method_decorator(login_required, name='dispatch')
class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_form.html'

    def form_valid(self,form):
       # Asignar el usuario actual como el creador del lead
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirigir a la página de detalle del lead recién creado
        return reverse_lazy('lead_detail', kwargs={'pk': self.object.pk})
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator  # Necesario para aplicar decoradores a clases



# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):

    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile_detail'


    def get_object(self):
            username = self.kwargs.get('username')  # Obtener el username de los parámetros de la URL
            return get_object_or_404(Profile, user__username=username)  # Recuperar el perfil basado en el username
from django.urls import path
from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView

lead_patterns = ([
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    # Otras URLs relacionadas con leads...
], 'leads')

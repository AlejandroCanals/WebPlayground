from django.urls import path
from .views import  LeadCreateView, LeadListView, LeadDetailView  , LeadUpdateView

lead_patterns = ([
    path('', LeadListView.as_view(), name='leads'),
    path('<int:pk>/<slug:slug>/', LeadDetailView.as_view(), name='lead'),

    path('create/', LeadCreateView.as_view(), name='create'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='update'),

 

], 'leads')

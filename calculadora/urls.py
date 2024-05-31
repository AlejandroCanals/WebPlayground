from django.urls import path
from .views import Calculadora

calculador_patterns = ([
    path('', Calculadora.as_view(), name='calculadora'), 
], 'calculadora')


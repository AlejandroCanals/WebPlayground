from django.urls import path
from .views import GenerateQrCode

qr_generator_patterns = ([
    path('', GenerateQrCode.as_view(), name='qr_generate'), 
], 'qr_generator')


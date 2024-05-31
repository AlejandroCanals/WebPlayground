from django.shortcuts import render
from django.views import View
import qrcode 
from django.http import HttpResponse
import io
import base64


# Create your views here.


class GenerateQrCode(View):

    def get(self,request):
        return render(request, template_name="qr_generator/qr_generator.html")
    
    def post(self,request):
        data = request.POST.get('data')
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)   

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = io.BytesIO()

        img.save(buffer,format='PNG')

        encoded_image = base64.b64encode(buffer.getvalue()).decode()


        return render(request,"qr_generator/qr_result.html",{"qr_image":encoded_image})





    """
    def post(self,request):
        data = data
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

        qr.add_data('Some data')
        qr.make(fit=True)   

        img = qr.make_image(fill_color="black", back_color="white")

    """


from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Calculadora(View):
    def get(self, request):
        return render(request, 'calculadora/calculadora.html') 

    def post(self, request):
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        opcion = request.POST.get('opcion')

        if opcion == '+':
            res = num1 + num2
        elif opcion == '-':
            res = num1 - num2
        elif opcion == '*':
            res = num1 * num2
        elif opcion == '/':
            if num2 == 0:
                return HttpResponse("Error: No se puede dividir entre cero.")
            else:
                res = num1 / num2
        elif opcion == '**':
            res = num1 ** num2
        else:
            return HttpResponse("Opción no válida.")

        return render(request, 'calculadora/calculadora_resultado.html', {'num1': num1, 'num2': num2, 'opcion': opcion, 'resultado': res})

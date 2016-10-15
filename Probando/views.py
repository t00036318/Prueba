from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import Calculadora


@csrf_exempt
def RequestsHandler(request):
    if len(request.GET) != 0:
        return HttpResponse("Get request must be empty.")
    elif request.method == "POST":
        if len(request.POST) > 3:
            return HttpResponse("Extra data!")
        try:
            a = request.POST["a"]
            b = request.POST["b"]
            operacion = request.POST["op"]
        except Exception:
            return HttpResponse("Missing data!")

        try:
            a = float(a)
            b = float(b)
            operacion = float(operacion)
        except Exception:
            return HttpResponse("Everything must be a number")

        CalculadoraObjeto = Calculadora.Calculadora(operacion, a, b)

        if CalculadoraObjeto.op == 1.0:
            return HttpResponse(CalculadoraObjeto.suma())
        elif CalculadoraObjeto.op == 2.0:
            return HttpResponse(CalculadoraObjeto.resta())
        elif CalculadoraObjeto.op == 3.0:
            return HttpResponse(CalculadoraObjeto.multiplicacion())
        elif CalculadoraObjeto.op == 4.0:
            if CalculadoraObjeto.num2 == 0.0:
                return HttpResponse("Divition by 0 not defined")
            return HttpResponse(CalculadoraObjeto.division())
        else:
            return HttpResponse("Operation undefined")
    else:
        return HttpResponse ("Http request method error")


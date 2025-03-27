from django.shortcuts import render, redirect

# Create your views here.
class Registro:
    def __init__(self, fecha, descripcion, saldo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.saldo = saldo

class RegistroIngreso(Registro):
    def __init__(self, fecha, descripcion, saldo, ingreso):
        super().__init__(fecha, descripcion, saldo)
        self.ingreso = ingreso
    
    def sumar_ingreso(self):
        sumaingreso = self.ingreso + self.saldo
        return f'El saldo actual es: {sumaingreso}'


class RegistroEgreso(Registro):
    def __init__(self, fecha, descripcion, saldo, egreso):
        super().__init__(fecha, descripcion, saldo)
        self.egreso = egreso
        pass



def inicio(request):
    objeto = Registro("hoy", "esto es un registro", 5000)

    fecha_reg = objeto.fecha
    descripcion_reg = objeto.descripcion
    saldo_reg = objeto.saldo
    ingreso_reg = int(input("Ingrese el ingreso: "))

    objeto_ingreso = RegistroIngreso(fecha_reg, descripcion_reg, saldo_reg, ingreso_reg)

    print(objeto_ingreso.sumar_ingreso())
    return render(request, 'inicio.html')

def agregar_registro(request):
    if request.method == "POST":
        descripcion = request.POST["descripcion"]
        ingreso = float(request.POST.get("ingreso", 0))
        egreso = float(request.POST.get("egreso", 0))

        ultimo_registro = Registro.objects.last()
        saldo_actual = ultimo_registro.saldo if ultimo_registro else 0

        nuevo_saldo = saldo_actual + ingreso - egreso
        if nuevo_saldo < 0:
            return render(request, "index.html", {"error": "Saldo insuficiente"})


        Registro.objects.create(
            descripcion = descripcion,
            ingreso = ingreso,
            egreso = egreso,
            saldo = nuevo_saldo
        )

        return redirect("index")
    
    return redirect(request, "index.html")


# def inicio(request):
#     objeto = Registro("hoy", "esto es un registro", 5000)

#     fecha_reg = objeto.fecha
#     descripcion_reg = objeto.descripcion
#     saldo_reg = objeto.saldo
#     ingreso_reg = int(input("Ingrese el ingreso: "))

#     objeto_ingreso = RegistroIngreso(fecha_reg, descripcion_reg, saldo_reg, ingreso_reg)

#     print(objeto_ingreso.sumar_ingreso())
#     return render(request, 'inicio.html')
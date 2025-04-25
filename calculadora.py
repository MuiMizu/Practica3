
def Cambio_Divisa(Monto, tasa_cambio):
    return Monto / tasa_cambio

Monto = float(input("Ingresa la cantidad de su moneda: "))
Ratio = float(input("Ingresa atio de conversion: "))

MontoConvertido = str(Cambio_Divisa(Monto,Ratio))


print("Ahora tiene" + MontoConvertido + " de la moneda local")
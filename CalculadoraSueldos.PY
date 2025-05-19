# Fabian Lorenzo 5to A Informatica
# CONSTANTES
TSS_TOTAL = 0.0591  # 5.91% del salario sin calcular
PORCENTAJE_BONIFICACION = 0.10  # 10% de los beneficios netos/Sueldo neto

def calcular_ISR(sueldo_anual):

    #Calcula la retención Segun el sueldo anual
    if sueldo_anual <= 416220:
        return 0
    elif sueldo_anual <= 624329:
        excedente = sueldo_anual - 416220
        return excedente * 0.15
    elif sueldo_anual <= 867123:
        excedente = sueldo_anual - 624329
        return 31216 + excedente * 0.20
    else:
        excedente = sueldo_anual - 867123
        return 79776 + excedente * 0.25

def main():
    try:
        sueldo_bruto_mensual = float(input("Ingrese el sueldo bruto mensual: "))
        otros_descuentos = float(input("Ingrese otros descuentos mensuales: "))
        aplica_bonificacion = input("¿Aplica bonificación? (s/n): ").strip().lower()

        if sueldo_bruto_mensual <= 0:
            print("El sueldo bruto debe ser un valor positivo.")
            return

        # Cálculos generales
        descuento_tss = sueldo_bruto_mensual * TSS_TOTAL
        sueldo_mensual_antes_ISR = sueldo_bruto_mensual - descuento_tss
        sueldo_anual = sueldo_mensual_antes_ISR * 12
        retencion_isr_anual = calcular_ISR(sueldo_anual)
        retencion_isr_mensual = retencion_isr_anual / 12

        # Cálculo de bonificación
        bonificacion = sueldo_bruto_mensual * PORCENTAJE_BONIFICACION if aplica_bonificacion == 's' else 0

        # Cálculo del sueldo despues de calculos
        sueldo_neto = sueldo_bruto_mensual - descuento_tss - retencion_isr_mensual - otros_descuentos + bonificacion


        print("\n--- Detalle del Cálculo ---")
        print(f"Sueldo Bruto Mensual: RD${sueldo_bruto_mensual:.2f}")
        print(f"Descuento por Seguridad Social (TSS): RD${descuento_tss:.2f}")
        print(f"Retención ISR Mensual: RD${retencion_isr_mensual:.2f}")
        print(f"Otros Descuentos: RD${otros_descuentos:.2f}")
        print(f"Bonificación: RD${bonificacion:.2f}")
        print(f"Sueldo Neto Mensual: RD${sueldo_neto:.2f}")
        print("Eso es todo amigos")

    except ValueError:
        print("Use numeros validos.")


if __name__ == "__main__":
    main()



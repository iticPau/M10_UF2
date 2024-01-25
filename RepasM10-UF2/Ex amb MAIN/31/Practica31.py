def calcular_iva(sin_iva, iva_porcentaje=21):
    Iva = sin_iva * (iva_porcentaje / 100)
    Total_con_iva = sin_iva + Iva

    print(f"Valor sin IVA : {sin_iva}")
    print(f"IVA ({iva_porcentaje}): {Iva}")
    print(f"Total con IVA : {Total_con_iva}")
    return Total_con_iva
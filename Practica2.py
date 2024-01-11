euros = float(input("Introduce euros: "))
porcentaje = float(input("Introduce el IVA (4%, 10% o 21%): "))
final = euros * (1 + porcentaje / 100)
print(f"Valor introducido: €{euros:.2f}, IVA introducido: {porcentaje}% y valor final con IVA: €{final:.2f}")

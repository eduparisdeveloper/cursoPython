nombre = input("Cual es tu nombres: ")
ventas = int(input("Cuanto has tenido de ventas: "))

comision = round(ventas*0.13,2)

print(f"{nombre} has pagado {comision}€ en comisiones y has tenido {round(ventas - comision,2)}€ de beneficio")
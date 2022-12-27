def total():
    monto = float(input("Ingrese el valor del producto que estás pagando: "))
    iva = int(input("Ingrese el valor del IVA: "))
    
    if iva !=0:
        if iva > 0:
            totalPagar = (monto*iva)/100 + monto
            return totalPagar
        else:
            return "El monto de IVA es negativo. No podemos avanzar"

    else:
        totalPagar = (monto*1.21)
        return totalPagar   

print("El total de su monto es: ", total())

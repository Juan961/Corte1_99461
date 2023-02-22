def n3():
    # Inicio

    try:
        # Definir IVA porcentaje
        IVA_PERCENTAGE = 0.19

        # Leer precio_producto
        product_price = float(input("Enter the final product value: "))

        # Si el precio es menor o igual a 0 erro 
        if product_price <= 0: raise Exception("Price cannot be 0 or less")

        # Calcular el precio agregado por IVA
        iva = product_price * IVA_PERCENTAGE

        # Imprimir el IVA calculado
        print(f"The IVA of the product is: {iva}")

        # Imprimir el precio del producto sin el IVA        
        print(f"Product price without IVA: {product_price - iva}")

    except Exception as e:
        print(e)

    # Fin

if __name__ == "__main__":
    n3()

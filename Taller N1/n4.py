def n4():
    # Inicio

    try:
        # Leer distancia viajada en kilometros anualmente
        total_distance = float(input("Enter the total annual distance traveled (km): "))
        
        # Leer el consumo de conbustible (L) anual por cada 100km 
        anual_fuel_consumption = float(input("Enter the annual fuel consumption (L/100Km): "))
        
        # Leer el costo promedio del combustible por litros conducidos
        average_anual_cost_of_fuel = float(input("Enter the average annual cost of fuel per liters driven ($/L): "))

        # Leer distancia viajada en kilometros anualmente
        fuel_cost = ( total_distance * ( anual_fuel_consumption / 100 ) ) * average_anual_cost_of_fuel

        # Imprimir el costo del consumo del combustible
        print(f"Annual cost of fuel consumption: {fuel_cost}")

    except Exception as e:
        print(e)

    # Fin

if __name__ == "__main__":
    n4()

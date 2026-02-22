def unit_converter():
    print("--- ⚖️ Universal Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("Type 'exit' to quit")

    while True:
        choice = input("\nChoose option (1/2/3) or 'exit': ").lower()

        if choice == 'exit':
            print("Shutting down converter. Goodbye!")
            break

        if choice in ['1', '2', '3']:
            try:
                val = float(input("Enter value: "))
                if choice == '1':
                    print(f"{val} KM = {round(val * 0.621371, 2)} Miles")
                elif choice == '2':
                    print(f"{val}°C = {round((val * 9/5) + 32, 2)}°F")
                elif choice == '3':
                    print(f"{val} KG = {round(val * 2.20462, 2)} Lbs")
            except ValueError:
                print("Error: Please enter a valid number.")
        else:
            print("Invalid input. Try again.")

unit_converter()

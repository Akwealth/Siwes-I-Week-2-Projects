# Unit Converter App

def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Select conversion (1 or 2): ")

    if choice == "1":
        km_input = input("Enter length in Kilometers: ")
        try:
            km = float(km_input)
            miles = km * 0.621371
            print(f"{km} km = {miles:.2f} miles")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    elif choice == "2":
        miles_input = input("Enter length in Miles: ")
        try:
            miles = float(miles_input)
            km = miles / 0.621371
            print(f"{miles} miles = {km:.2f} km")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    else:
        print("Invalid conversion choice!")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Select conversion (1 or 2): ")

    if choice == "1":
        kg_input = input("Enter weight in Kilograms: ")
        try:
            kg = float(kg_input)
            lbs = kg * 2.20462
            print(f"{kg} kg = {lbs:.2f} lbs")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    elif choice == "2":
        lbs_input = input("Enter weight in Pounds: ")
        try:
            lbs = float(lbs_input)
            kg = lbs / 2.20462
            print(f"{lbs} lbs = {kg:.2f} kg")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    else:
        print("Invalid conversion choice!")


def main():
    print("Welcome to the Unit Converter App")
    print("1. Length (Kilometers ↔ Miles)")
    print("2. Weight (Kilograms ↔ Pounds)")
    
    choice = input("Choose a category (1 or 2): ")

    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    else:
        print("Invalid selection! Please enter 1 or 2.")


if __name__ == "__main__":
    main()
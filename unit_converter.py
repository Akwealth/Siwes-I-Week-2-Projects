# Unit Converter Application
# This CLI app converts measurement values between standard units (Length and Weight).

def length_converter():
    # Handles distance and length unit conversions between Kilometers and Miles.
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

    # Prompt the user to select the conversion direction
    choice = input("Select conversion (1 or 2): ")

    if choice == "1":
        km_input = input("Enter length in Kilometers: ")
        try:
            # Cast user string input to float for arithmetic operations
            km = float(km_input)
            # Conversion formula: 1 Kilometer = 0.621371 Miles
            miles = km * 0.621371
            # Print output formatted to 2 decimal places
            print(f"{km} km = {miles:.2f} miles")
        except ValueError:
            # Error guard: Triggered if user types non-numeric characters
            print("Invalid input! Please enter a numerical value.")
    elif choice == "2":
        miles_input = input("Enter length in Miles: ")
        try:
            miles = float(miles_input)
            # Conversion formula: Miles divided by conversion factor
            km = miles / 0.621371
            print(f"{miles} miles = {km:.2f} km")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    else:
        # Fallback response for choices outside option 1 or 2
        print("Invalid conversion choice!")


def weight_converter():
    #Handles mass and weight unit conversions between Kilograms and Pounds.
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Select conversion (1 or 2): ")

    if choice == "1":
        kg_input = input("Enter weight in Kilograms: ")
        try:
            kg = float(kg_input)
            # Conversion formula: 1 Kilogram = 2.20462 Pounds
            lbs = kg * 2.20462
            print(f"{kg} kg = {lbs:.2f} lbs")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    elif choice == "2":
        lbs_input = input("Enter weight in Pounds: ")
        try:
            lbs = float(lbs_input)
            # Conversion formula: Pounds divided by conversion factor
            kg = lbs / 2.20462
            print(f"{lbs} lbs = {kg:.2f} kg")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    else:
        print("Invalid conversion choice!")


def main():
    # Primary execution loop and main menu routing.
    print("Welcome to the Unit Converter App")
    print("1. Length (Kilometers ↔ Miles)")
    print("2. Weight (Kilograms ↔ Pounds)")
    
    choice = input("Choose a category (1 or 2): ")

    # Route program flow based on main menu choice
    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    else:
        print("Invalid selection! Please enter 1 or 2.")

# Standard Python boilerplate to ensure main() executes when run directly
if __name__ == "__main__":
    main()
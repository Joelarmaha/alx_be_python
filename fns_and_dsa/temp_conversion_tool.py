# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

try:
    temperature = float(input("Enter a temperature: "))
    specify_unit = input("Specify whether it’s in Celsius or Fahrenheit (Celsius/Fahrenheit): ").strip()

    if specify_unit == "Celsius":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")

    elif specify_unit == "Fahrenheit":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")

    else:
        print("This is not valid. Please enter either 'Celsius' or 'Fahrenheit'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

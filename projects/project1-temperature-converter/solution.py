# Project 1 — Temperature Converter
# Author: Muhammed Nur Celil
# Branch: MNC06-project1

# Ask the user which conversion they want
choice = input("Convert: (1) Celsius → Fahrenheit  (2) Fahrenheit → Celsius\nChoice: ")

# Option 1 — Celsius to Fahrenheit
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# Option 2 — Fahrenheit to Celsius
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")

# Invalid choice
else:
    print("Invalid choice. Please run the program again and select 1 or 2.")

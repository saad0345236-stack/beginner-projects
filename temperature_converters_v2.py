# Temperature Converter V2:
def temperature_converter():
    pick = input("Celsius or Fahrenheit (c/f): ").lower()
    try:
        if pick == 'f':
            c = int(input("What's C? "))
            return f"Temperature is {((c * 9/5) + 32):.1f}°F"
        
        elif pick == 'c':
            f = int(input("What's F? "))
            return f"Temperature is {((f - 32) * 5/9):.1f}°C"
                
        else:
            return "Invalid unit."
    
    except ValueError:
        print("You can only enter integers.")

print(temperature_converter())
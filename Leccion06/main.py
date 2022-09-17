def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9


fahrenheit = float(input("Introduce los grados Fahrenheit: "))
print(fahrenheit_celsius(fahrenheit))

celsius = float(input("Introduce los grados celsius: "))

print(celsius_fahrenheit(celsius))



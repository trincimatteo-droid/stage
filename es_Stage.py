print("Benvenuto al convertitore di temperatura")

while True:
    num1 = input("Inserisci un temperatura: ")
    if num1.isdecimal():
        num1 = float(num1)
        break
    else:
        print("Inserisci una temeperatura valida")

print(
    "Inserisci 1 per convertire il numero in Celsius di default, 2 per convertire il numero in Fahrenheit di default"
)
num2 = str(input("Inserisci °C o °F:"))
num4 = 1
while num2 == "°C" and num4 != 0:
    num1 = input("Inserisci un numero: ")
    num1 = float(num1)
    print("Il numero in Celsius è:", int((num1 - 32) * 5 / 9), "°C"  "🌡️")
    num4 = int(input("Inserisci 0 per uscire, un altro numero per continuare: "))
while num2 == "°F" and num4 != 0:
    num1 = input("Inserisci un numero: ")
    num1 = float(num1)
    print("Il numero in Fahrenheit è:", int(num1 * 9.0 / 5.0) + 32, "°F"  "🌡️")
    num4 = int(input("Inserisci 0 per uscire, un altro numero per continuare: "))
    

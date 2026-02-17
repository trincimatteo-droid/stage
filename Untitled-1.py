
while True:
    num1 = input("Inserisci un numero: ")
    if num1.isdecimal():
        num1 = float(num1)
        break
    else:
        print("Inserisci un numero valido")

print("Inserissci 1 per convertire da Fahrenheit a Celsius, 2 per convertire da Celsius a Fahrenheit")
num2 = str(input("Inserisci 1 o 2:"))
if num2 == "1":
        print("Il numero in Celsius è:", int((num1 - 32) * 5/9))
elif num2 == "2":
        print("Il numero in Fahrenheit è:", int(num1 * 9.0/5.0) + 32)
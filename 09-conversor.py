#Ejercicio conversor de temperatura
temperatura = float(input("Ingrese temperatura: "))
escala = input("¿Es Fahrenheit(F) o es Celcius(C)?: ").lower()

if escala == "f":
  celcius = (temperatura -32) * 5 /9
  print( temperatura,"°F en Grados Celcius son: ",celcius,"°C")
elif escala == "c":
  fahrenheit = temperatura * 1.8 +32
  print(temperatura,"°C en Grados Fahrenheit son: ", fahrenheit,"°F")
else:
  print("Escasla incorrecta")




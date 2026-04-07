print("\nConversão de temperatura")

#Quando digitar o valor da temperatura, no lugar da vírgula use um ponto 
tc = float(input("Digite a temperatura em Graus Celcius: "))

tf = ((1.8 * tc) + 32)
tk = (tc + 273)

print("\nResultado da Conversão")
print(f"Fahrenheit: {tf:.2f}")
print(f"Kelvin: {tk:.2f}\n")
print("\nCálculo da Cotação do Dólar")

#Quando digitar o valor da cotação no lugar da vírgula de centavos use um ponto 
cotacao = float(input("Digite a cotação atual do dólar: R$ "))
dolar = float(input("Digite o valor em dólar para converter: $"))

#Cálculo de conversão (Cotação atual em R$ 5,26)
conversao = (cotacao * dolar)

print("\nResultado da conversão para Real")
print(f"R$ {conversao:.2f}\n")
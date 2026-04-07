print("\nComanda - Restaurante ComaBem")

#Quando digitar o valor gasto, no lugar da vírgula de centavos use um ponto 
entrada = float(input("Digite o valor gasto no prato de entrada R$ "))
principal = float(input("Digite o valor gasto no prato principal R$ "))
bebida = float(input("Digite o valor gasto em bebidas R$ "))
sobremesa = float(input("Digite o valor gasto em sobremesa R$ "))

soma = (entrada + principal + bebida + sobremesa)
gorjeta = (soma * 0.10)
total = (soma + gorjeta)

print("\nTotal a pagar:")
print(f"R$ {total:.2f}\n")
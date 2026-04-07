print("\nCálculo de acréscimo de 5% em seu salário.")

#Quando digitar o valor do salário, no lugar da vírgula de centavos use um ponto 
x = float(input("\nDigite o seu salário - R$ "))
comissao = (x * 0.05)
total = (comissao + x)

print(f"Seu salário total com comissão é: R$ {total:.2f}\n")
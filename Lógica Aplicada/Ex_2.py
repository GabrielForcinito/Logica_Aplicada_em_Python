print("\nCálculo da Velocidade Média de um carro entre duas cidades.")

d = float(input("\nDigite a distância entre as duas cidades (Km/h): "))
t = float(input("Digite o tempo de viagem entre as duas cidades (Horas): "))
vmedia = (d / t)

print(f"A velociade média da viagem é: {vmedia:.2f} km/h\n")
#Ao usar o f no inicio e colocar entre chaves a váriavel: .2f, vai me gerar na resposta final duas casas depois da virgula
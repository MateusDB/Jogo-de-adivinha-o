import random

numero_secreto = random.randint(0, 100)

print("Adivinhe o número entre 0 e 100")
tentativas = 0
tentativas_maximas = 10

while True:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto: 
        print(f"Você acertou em {tentativas} tentativas!")  
    elif palpite > 100 or palpite < 0:
        print("Número inválido, digite um número entre 0 e 100")
    elif palpite > numero_secreto:
        print("Você errou! O número é menor.")
    else:  
        print("Errado! O número é maior.")
        
    if tentativas >= tentativas_maximas:
        print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")
        break

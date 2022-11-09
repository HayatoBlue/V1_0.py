def troca(a, b, vetor):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

def organizando(vetor):
    for i in range(0, len(vetor)-1):
        for j in range(0, len(vetor)-1):
            if vetor[j] > vetor[j + 1]:
                troca(j, j+1, vetor)


def linha():
    print("-----------------------------------------")

def inicializando():
    print("Escolha uma opção:")
    print("1 - criar lista\n2 - organizar lista\n3 - apagar lista\n4 - visualizar a lista\n0 - finalizar programa")

#vetor = [4, 1, 7, 2]
#print(vetor)
#organizando(vetor)
#print(vetor)

linha()
linha()
print("Olá, sou um programa para criar e organizar listas!")
linha()

print("vamos começar!")
linha()
vet = []
i = 0
nm = 9999999999999

while nm != 0:
    inicializando()   
    x = int(input())
    if x == 1:
        tam = int(input("Qual o tamanho da lista:\n"))
        vet = [i] * tam
        for j in range(tam):
            y = int(input("Digite: "))
            vet[i] = y
            i = i + 1
            y = 0
    elif x == 2:
        print("Vmaos organizar essa lista!")
        organizando(vet)
    elif x == 3:
        vet = vet[y] * tam
    elif x == 4:
        print(vet)
    else:
        break



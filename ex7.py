def matriz_diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j and matriz[i][j] != 0:
                return False
    return True

def main():
    matrizA = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar): ")
        if linha == "":
            break
        matrizA.append([int(num) for num in linha.split()])

    print(matriz_diagonal(matrizA))

main()
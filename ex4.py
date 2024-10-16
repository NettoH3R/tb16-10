def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def main():
    matrizA = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar): ")
        if linha == "":
            break
        matrizA.append([int(num) for num in linha.split()])

    print(transposta(matrizA))

main()
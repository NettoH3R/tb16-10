def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def main():
    matrizA = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar): ")
        if linha == "":
            break
        matrizA.append([int(num) for num in linha.split()])

    print(imprimir_matriz(matrizA))

main()
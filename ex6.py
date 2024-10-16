def multiplicar_matrizes(A, B):
    if len(A[0]) != len(B):
        return []
    
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def main():
    matrizA = []
    matrizB = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar) para a Matriz A: ")
        if linha == "":
            break
        matrizA.append([int(num) for num in linha.split()])

    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar) para a Matriz B: ")
        if linha == "":
            break
        matrizB.append([int(num) for num in linha.split()])

    print(multiplicar_matrizes(matrizA, matrizB))

main()
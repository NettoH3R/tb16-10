def verificar_matriz(matriz):
    if not matriz or not isinstance(matriz, list) or not all(isinstance(linha, list) for linha in matriz):
        return ()
    
    colunas = len(matriz[0])
    if all(len(linha) == colunas for linha in matriz):
        return (len(matriz), colunas)
        
def soma_matrizes(A, B):
    if verificar_matriz(A) != verificar_matriz(B):
        return []
    
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

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

    print(soma_matrizes(matrizA, matrizB))

main()
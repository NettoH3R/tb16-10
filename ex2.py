def verificar_matriz(matriz):
    if not matriz or not isinstance(matriz, list) or not all(isinstance(linha, list) for linha in matriz):
        return ()
    
    colunas = len(matriz[0])
    if all(len(linha) == colunas for linha in matriz):
        return (len(matriz), colunas)


def main():
    matrizA = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar): ")
        if linha == "":
            break
        matrizA.append([int(num) for num in linha.split()])

    print(verificar_matriz(matrizA))
    

main()
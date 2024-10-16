def main():
    matriz = []
    while True:
        linha = input("Digite uma linha de números inteiros separados por espaços (ou deixe em branco para parar): ")
        if linha == "":
            break
        matriz.append([int(num) for num in linha.split()])
        print(f"\n\nSua matriz é: {matriz}")

main()
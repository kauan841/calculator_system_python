import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from funcoes.soma import soma
from funcoes.subtracao import subtracao
from funcoes.multiplicacao import multiplicacao
from funcoes.dividir import dividir
from funcoes.potencia import potencia
from funcoes.raiz import raiz



while True:
    print("\nseja bem vindo a calculadora")
    print("escolha a operação que deseja realizar:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
     try:   
         num1 = float(input("Digite o primeiro número: "))
         num2 = float(input("Digite o segundo número: "))
         print(f"Resultado: {soma(num1, num2)}")
     except ValueError :
        print(f"digite apenas números, tente novamente. ")

    elif escolha == '2':
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {subtracao(num1, num2)}")
        except ValueError :
            print(f"digite apenas números, tente novamente. ")

    elif escolha == '3':
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {multiplicacao(num1, num2)}")
        except ValueError :
            print(f"digite apenas números, tente novamente. ")

    elif escolha == '4':

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {dividir(num1, num2)}")
        
        except ValueError:
            print(f"digite apenas números, tente novamente.")

    elif escolha == '5':
        
        try:
            num1 = float(input("Digite a base: "))
            num2 = float(input("Digite o expoente: "))
            print(f"Resultado: {potencia(num1, num2)}")

        except ValueError:
            print(f"digite apenas números, tente novamente. ")

    elif escolha == '6':

        try:
            num1 = float(input("Digite o número: "))
            print(f"Resultado: {raiz(num1)}")
        except ValueError:
            print(f"digite apenas números, tente novamente. ")

    elif escolha == '7':
        print("Encerrando a calculadora. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
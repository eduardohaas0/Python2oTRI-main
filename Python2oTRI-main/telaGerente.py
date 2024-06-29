import csv
from conta import Conta

def escreveArquivo(numero, senha, titular, saldo, limite):
    with open('contas.csv', 'a', newline='') as csvfile:
        escreve_conta = csv.writer(csvfile, delimiter=',')
        escreve_conta.writerow([numero, senha, titular, saldo, limite])
        print("### USUÁRIO ", titular, "adicionado com sucesso! ###")

contas = []
print("### BEM VINDO A TELA DE CADASTRO DE CONTAS ###")
while(True):
    print("\nNOVO USUÁRIO:")
    numero = int(input("Digite o número da conta do cliente: \n"))
    senha = int(input("Solicite uma nova senha ao cliente: \n"))
    titular = input("Digite o nome completo do cliente: \n")
    saldo = 0.0
    limite = 100.0
    novaConta = Conta(numero, senha, titular, saldo, limite)
    
    escreveArquivo(numero, senha, titular, saldo, limite)
    contas.append(novaConta)
    # TESTE PARA VER SE O SISTEMA FUNCIONA:
    for conta in contas:
        print(conta.limite, " - ")


    


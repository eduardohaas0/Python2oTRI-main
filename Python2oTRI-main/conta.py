class Conta:
    # Método construtor
    def __init__(self, numero, senha, titular, saldo, limite):
        # ATRIBUTOS DA CLASSE CONTA
        self.__numero = numero
        self.__senha = senha
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    # Métodos gerais
    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        print("Saque efetuado! __saldo atual: ", self.__saldo)
    
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        print("Depósito efetuado! Saldo atual: ", self.__saldo)

    def extrato(self):
        print("Saldo atual: ", self.__saldo)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor








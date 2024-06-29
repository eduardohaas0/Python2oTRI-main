# ARMAZENAMENTO CHAVE-VALOR (dictionary em Python)

def criaCarro(marca, modelo, ano, placa):
    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "placa": placa
    }
    return carro
uno = criaCarro("Fiat", "Uno", 2002, "AAA-0000")
#print(uno)
print("A marca do carro é", uno["marca"], ", modelo ", uno["modelo"], "ano", uno["ano"])
# CRIAR UM NOVO CARRO: MARCA VW, MODELO GOL, ANO 2010, PLACA ABC-1010. Mostrar o texto com marca, modelo e ano.
gol = criaCarro("VW", "GOL", 2010, "ABC-1010")
print("A marca do carro é", gol["marca"], ", modelo ", gol["modelo"], "ano", gol["ano"])




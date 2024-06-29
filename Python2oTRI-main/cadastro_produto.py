import json

class Produto:
    def __init__(self, codigo, nome, descricao, preco, quantidade, categoria):
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._quantidade = quantidade
        self._categoria = categoria
    

    def get_codigo(self):
        return self._codigo
    
    def get_nome(self):
        return self._nome
    
    def get_descricao(self):
        return self._descricao
    
    def get_preco(self):
        return self._preco
    
    def get_quantidade(self):
        return self._quantidade
    
    def get_categoria(self):
        return self._categoria
    


    def set_codigo(self, codigo):
        self._codigo = codigo
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_descricao(self, descricao):
        self._descricao = descricao
    
    def set_preco(self, preco):
        self._preco = preco
    
    def set_quantidade(self, quantidade):
        self._quantidade = quantidade
    
    def set_categoria(self, categoria):
        self._categoria = categoria


produtos = []


def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    categoria = input("Categoria do produto: ")
    
    produto = Produto(codigo, nome, descricao, preco, quantidade, categoria)
    produtos.append(produto)
    
    with open('produtos.json', 'a') as file:
        json.dump(produto.__dict__, file)
        file.write('\n')
    
    print(f"Produto {nome} cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("\nLista de Produtos Cadastrados:")
    for produto in produtos:
        print(f"Código: {produto.get_codigo()}, Nome: {produto.get_nome()}, Descrição: {produto.get_descricao()}, Preço: {produto.get_preco()}, Quantidade: {produto.get_quantidade()}, Categoria: {produto.get_categoria()}")

def menu():
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            cadastrar_produto()
            listar_produtos()
        elif opcao == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()


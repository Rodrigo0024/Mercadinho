# models/produto.py
class Produto: #está sendo criada a classe produto 
    def __init__(self, id=None, nome="", preco=0.0, descricao=""):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def to_tuple(self):
        return (self.nome, self.preco, self.descricao) #Está sendo criada uma tupla para passar os dados separadamente pro mysql, ajuda tornar as coisas mais seguras

    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco})"
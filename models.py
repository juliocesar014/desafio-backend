class Produto:
    def __init__(self,nome,preco,categoria,desc,quantidade):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.desc = desc
        self.quantidade = quantidade
    
    def toDBCollection(self):
        return {
            'nome': self.nome,
            'preco': self.preco,
            'categoria': self.categoria,
            'desc': self.desc,
            'quantidade': self.quantidade
        }
    

        
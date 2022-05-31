from app.model.acervo import listadelivros, listadeexemplares, listadeassuntos
from app.model.bibliotecario import Bibliotecario


class Emprestimo(Bibliotecario):
    def __init__(self, nome):
        super().__init__(nome)
        
        
    def cadastrarEmprestimo(self, nomePesquisa):
        self.nomePesquisa = nomePesquisa
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.nomePesquisa)
            if x['Livro'] == self.nomePesquisa:
                confirmaEmprestimo = input("Deseja emprestar o livro? (S/N) ")
                if confirmaEmprestimo == "S":
                    self.emprestimo = input("Digite a data de emprestimo: EX: 27/04/2022 ")
                    x['Emprestimo'] = self.emprestimo
                    return listadelivros
                else:
                    return "Livro não emprestado"
            else:
                return "Livro não encontrado"

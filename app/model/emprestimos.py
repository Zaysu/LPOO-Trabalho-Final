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
            
            
    def pesquisarData(self, data):
        self.data = data
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Emprestimo'] == self.data)
            if x['Emprestimo'] == self.data:
                return listadelivros
            else:
                return "Livro não encontrado"
                
    def gerarRelatorio(self, dataInicial, dataFinal):
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Emprestimo'] == self.dataInicial)
            if x['Emprestimo'] == self.dataInicial:
                return listadelivros
            else:
                return "Nenhum livro cadastrado nesse periodo"

    def cancelarEmprestimo(self, nomePesquisa):
        self.nomePesquisa = nomePesquisa
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.nomePesquisa)
            if x['Livro'] == self.nomePesquisa:
                confirmaCancelamento = input("Deseja cancelar o emprestimo? (S/N) ")
                if confirmaCancelamento == "S":
                    self.emprestimo = "00/00/0000"
                    x['Emprestimo'] = self.emprestimo
                    return listadelivros
                else:
                    return "Livro não cancelado"
            else:
                return "Livro não encontrado"
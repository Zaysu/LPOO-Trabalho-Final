from ast import Break
from app.model.acervo import listadelivros, listadeexemplares, listadeassuntos, usuarios
from app.model.bibliotecario import Bibliotecario
from datetime import date, datetime


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
                    User = input("Quem Deseja Alugar?: ")
                    x['Usuario'] = User
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
                
    def gerarRelatorio(self, Nomelivro, dataInicial, dataFinal):
        self.Nomelivro = Nomelivro
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.Nomelivro)
            if x['Livro'] == self.Nomelivro:
                self.dataInicial = datetime.strptime(self.dataInicial, '%Y-%m-%d ')
                self.dataFinal = datetime.strptime(self.dataFinal, '%Y-%m-%d')
                if self.dataInicial <= x['Emprestimo'] <= self.dataFinal:
                #if x['Emprestimo'] <= self.dataInicial.strftime("%Y-%m-%d") and x['Emprestimo'] >= self.dataFinal.strftime("%Y-%m-%d"):
                    return listadelivros
                else:
                    return "Nenhum livro cadastrado nesse periodo"
            else:
                return "Livro não encontrado"
            
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
        
    def verificaUsuario(self, login, senha):
        self.login = login
        self.senha = senha
        for x in usuarios:
            x = next(x for x in usuarios if x['Nome'] == self.login)
            if x['Nome'] == self.login and x['Senha'] == self.senha:
                return "Usuario logado"
            else:
                return Break 

from datetime import *
from app.model.acervo import listadelivros, listadeexemplares, listadeassuntos

'''listadelivros = [{'Livro' : 'Senhor Dos Aneis', 'Autor' : 'J.R.R. Tolkien', 'ISBN' : '123456789', 'Edicao' : '1', 'Editora' : 'DarkSide','Emprestimo':'jan'},]
#listadelivros = [{'Livro' : 'Senhor', 'Autor' : 'J.R.R. Tolkien', 'ISBN' : '123456789', 'Edicao' : '1', 'Editora' : 'Side','Emprestimo':'abril'},]
listadeexemplares = [{'Nome' : 'Senhor Dos Aneis', 'Quantidade' : '2'},]
listadeassuntos = [{'Assunto' : 'Aventura'},]'''


class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome
        
class Cadastrar_livro(Bibliotecario):
    def __init__(self, nome, livro, ISBN, autor, edicao, editora, emprestimo):
        super().__init__(nome)
        self.livro = livro
        self.ISBN = ISBN
        self.autor = autor
        self.edicao = edicao
        self.editora = editora
        self.emprestimo = emprestimo
     def get_livro(self):
        return self.livro
     def get_isbn(self):
        return self.ISBN
     def get_autor(self):
        return self.autor
     def get_edicao(self):
        return self.edicao
     def get_editora(self):
        return self.editora
     def get_emprestimo(self):
        return self.emprestimo
Lista = [
Cadastrar_livro(nome='marcelo',livro='o livro', ISBN='2828', autor='marcelo', edicao='1998', editora='atlanta', emprestimo='27/03/2022',
Cadastrar_livro(nome='marcelo2',livro='o livro2', ISBN='2828', autor='marcelo', edicao='1998', editora='atlanta', emprestimo='27/03/2022'
]
###################---------------CadastroLivroFechou--------------###############################    
    def incluirNovoLivro(self):
        self.listafinal = {'Livro' : self.livro, 'ISBN' : self.ISBN , 'Autor': self.autor, 'Edição' : self.edicao, 'Editora' : self.editora}
        listadelivros.append(self.listafinal)
        return listadelivros
    
####################-------------FECHOU Alterando livro na lista ###############################     
    def alterarLivro(self, nomePesquisa):
        self.nomePesquisa = nomePesquisa
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.nomePesquisa)
            if x['Livro'] == self.nomePesquisa:
                confirmaAlteracao = input("Deseja alterar o livro? (S/N) ")
                if confirmaAlteracao == "S":
                    self.novoLivro = input("Digite o novo livro: ")
                    x['Livro'] = self.novoLivro
                    return listadelivros
                else:
                    return "Livro não alterado"
        
########################## Fechou Excluir livro #########################   
    def excluirLivro(self, nomeExcluir):
        self.nomeExcluir = nomeExcluir
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.nomeExcluir)
            if x['Livro'] == self.nomeExcluir:
                confirmeExluir = input("Deseja excluir o livro? (S/N) ")
                if confirmeExluir == "S":
                    listadelivros.remove(x)
                return listadelivros
            else:
                return "Livro não excluido"    
        else:
            return "Nenhum Livro não encontrado"
           
########################## ''''''''''''' Consulta de Livros #########################
    def consultarLivros(self, NomeLivro):
        self.NomeLivro = NomeLivro
        for x in listadelivros:
            x = next(x for x in listadelivros if x['Livro'] == self.NomeLivro)
            if x['Livro'] == self.NomeLivro:
                return x
            else:
                return "Nenhum Livro não encontrado"
    def consultarLivrosPeriodo(self, PeriodoInicio,PeriodoFinal):
        self.periodo_inicio = PeriodoInicio
        self.periodo_fim = PeriodoFinal
        for x in listadelivros:
           if x['emprestimo'] <=  self.periodo_inicio and x['emprestimo'] >= self.periodo_fim:
               return x
           else:
               return "Nenhum Livro não encontrado"
      

############# Cadastrando EXEMPLAR  ###############                 
class Cadastrar_Exemplar(Bibliotecario):
    def __init__(self, livro, exemplar):
        super().__init__(livro)
        self.exemplar = exemplar
        
        
#--------- FECHOU Cadastrando EXEMPLAR -------------#
    def incluirNovoExemplar(self, nomeExemplar, qtdExemplar):
        self.qtdeExemplar = qtdExemplar
        self.exemplar = nomeExemplar
        if (self.exemplar in listadelivros):
            #self.listafinal = [self.qtdeExemplar]
            self.listafinal = {'Nome' : self.exemplar , 'Quantidade' : self.qtdeExemplar}
            listadeexemplares.append(self.listafinal)
            return listadeexemplares
        else:
            return "Livro não encontrado"
        
#-----------------------Concluido Exemplares -----------------#        
    def consultaExemplares(self, nomeExemplar):
        self.nomeExemplar = nomeExemplar
        for x in listadeexemplares: 
            x = next(x for x in listadeexemplares if x['Nome'] == self.nomeExemplar)
            if x['Nome'] == self.nomeExemplar:
                return x 
            else:
                return "Exemplar não encontrado"  
               
#-----------------------Excluindo Exemplares -----------------#
    def excluirExemplares(self, nomeExemplarExcluir):
        self.nomeExemplarExcluir = nomeExemplarExcluir
        for x in listadeexemplares:
            x = next( x for x in listadeexemplares if x['Nome'] == self.nomeExemplarExcluir)
            if x['Nome'] == self.nomeExemplarExcluir:
                confirmarExcluir = input("Deseja excluir o exemplar? (S/N) ")
                if confirmarExcluir == "S":
                    listadeexemplares.remove(x)
                    return listadeexemplares
                else:
                    return "Exemplar não excluido"
            else:
                return "Exemplar não encontrado"

#-----------------------Alterando Exemplares -----------------#

    def alterarExemplares(self, nomeExemplarAlterar):
        self.nomeExemplarAlterar = nomeExemplarAlterar
        for x in listadeexemplares:
            x = next(x for x in listadeexemplares if x['Nome'] == self.nomeExemplarAlterar)
            if x['Nome'] == self.nomeExemplarAlterar:
                self.novoNomeExemplar = input("Digite o novo nome do exemplar: ")
                x['Nome'] = self.novoNomeExemplar
                return listadeexemplares
            else:
                return "Exemplar não encontrado"



############ Cadastrando Assunto ###############
class Cadastrar_assunto(Bibliotecario):
    def __init__(self, nome, categoria):
        super().__init__(nome)
        self.categoria = categoria
    
    def incluirNovoAssunto(self, nomeAssunto):
        self.nomeAssunto = nomeAssunto
        for x in listadeassuntos:
            x = next(x for x in listadeassuntos if x['Nome'] == self.nomeAssunto)                 
            confirmaAssunto = input("Deseja incluir o assunto? (S/N) ")
            if confirmaAssunto == "S":
                self.listafinalassunto = {'Assunto' : self.nomeAssunto}
                listadeassuntos.append(self.listafinalassunto)
                return listadeassuntos
            else:
                return "Assunto não incluido"

    
    def consultarAssunto(self, nomeAssunto):
        self.nomeAssunto = nomeAssunto
        for x in listadeassuntos:
            x = next(x for x in listadeassuntos if x['Assunto'] == self.nomeAssunto)
            if x['Assunto'] == self.nomeAssunto:
                return x
            else:
                return "Assunto não encontrado"
    
    def excluirAssunto(self, nomeAssuntoExcluir):
        self.nomeAssuntoExcluir = nomeAssuntoExcluir
        for x in listadeassuntos:
            x = next(x for x in listadeassuntos if x['Assunto'] == self.nomeAssuntoExcluir)
            if x['Assunto'] == self.nomeAssuntoExcluir:
                confirmarExcluir = input("Deseja excluir o assunto? (S/N) ")
                if confirmarExcluir == "S":
                    listadeassuntos.remove(x)
                    return listadeassuntos
                else:
                    return "Assunto não excluido"
            else:
                return "Assunto não encontrado"
    
    def alterarAssunto(self, nomeAssuntoAlterar):
        self.nomeAssuntoAlterar = nomeAssuntoAlterar
        for x in listadeassuntos:
            x = next(x for x in listadeassuntos if x['Assunto'] == self.nomeAssuntoAlterar)
            if x['Assunto'] == self.nomeAssuntoAlterar:
                self.novoNomeAssunto = input("Digite o novo nome do assunto: ")
                x['Assunto'] = self.novoNomeAssunto
                return listadeassuntos
            else:
                return "Assunto não encontrado"

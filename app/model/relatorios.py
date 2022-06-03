from app.model.acervo import statuslivros,  listadeexemplares, usuarios

class GerarRelatorio:
    
    def gerarRelat(self, nomePesquisa):
    
        self.nomePesquisa = nomePesquisa
        
        for x in statuslivros:
            x = next(x for x in statuslivros if x['Livro'] == self.nomePesquisa)
            if x['Livro'] == self.nomePesquisa:
                if x['Status'] == "Disponivel":
                    return self.livrosDisponiveis
                elif x['Status'] == "Emprestado":
                    return self.livrosEmprestados
                elif x['Status'] == "Reservado":
                    return self.livrosReservados
                else:
                    return "Livro não encontrado"
            else:
                return "Livro não encontrado"
            
    def todosLivrosEmprestados(self):
        for x in statuslivros:
            x = next(x for x in statuslivros if x['Status'] == "Emprestado")
            if x['Status'] == "Emprestado":
                livro = x['Livro']
                return livro
            else:
                return "Nenhum livro emprestado"
            
    def todosLivrosReservados(self):
        for x in statuslivros:
            x = next(x for x in statuslivros if x['Status'] == "Reservado")
            if x['Status'] == "Reservado":
                livro = x['Livro']
                return livro
            else:
                return "Nenhum livro reservado"
    
    def emAtraso(self):
        for x in statuslivros:
            x = next(x for x in statuslivros if x['Status'] == "Atraso")
            if x['Status'] == "Atraso":
                livro = x['Livro']
                return livro
            else:
                return "Nenhum livro em Atraso"
    
    def TodosExemplares(self):
        for x in listadeexemplares:
            return listadeexemplares
        
    def TodosUsuarios(self):
        for x in usuarios:
            return usuarios
            
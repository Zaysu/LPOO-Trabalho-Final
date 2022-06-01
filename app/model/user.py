from app.model.acervo import usuarios

class Usuario:
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo
    
    def get_nome(self):
        return self.nome
    
    def get_senha(self):
        return self.senha
    
    def get_tipo(self):
        return self.tipo
    
    def cadUser(self):
        self.listafinal = {'Nome' : self.nome, 'Senha' : self.senha, 'tipo' : self.tipo, 'aluguel': '' }
        usuarios.append(self.listafinal)
        return usuarios
    
    '''for x in usuarios:
            x = next(x for x in usuarios if x['Nome'] == self.nome)
            if x['Nome'] == self.nome:
                return "Usuario ja cadastrado"
            else:
                usuarios.append(self.listafinal)
                return usuarios'''
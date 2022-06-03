from app.model.bibliotecario import Bibliotecario, Cadastrar_livro, Cadastrar_Exemplar, Cadastrar_assunto
from app.model.emprestimos import Emprestimo
from app.model.user import Usuario
from app.model.relatorios import GerarRelatorio

login = input("Senha para execultar o sistema: ")

if login == 'Admin':
    opcao = 0
    while opcao != 6:
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        conferelogin = Emprestimo('')
        print(f"{conferelogin.verificaUsuario(login, senha)}")
        print('''Opções:
            ________________LIVROS______________________
            1 - Cadastrar livro
                11 - Alterar livro
                12 - Excluir livro
                13 - Consultar Livros
             ___________________________________________
                 
            ________________EXEMPLARES__________________
            2 - Cadastrar exemplar
                22 - Alterar exemplar
                23 - Consultar exemplares
                24 - Excluir exemplar
            _____________________________________________
                 
            ____________CATEGORIAS_______________________
            3 - Cadastrar Categoria
                33 - Consultar Categoria
                34 - Alterar Categoria 
                35 - Excluir Categoria
            _____________________________________________
                 
            ______________EMPRESTIMOS_____________________
            4 - Periodo Emprestimo
                41 - Emprestimos de Livros
                42 - Livros emprestados
                43 - Cancelar Emprestimo
                44 - Pesquisar por data
            _____________________________________________
                 
            _______________RELATORIO______________________
            5 - Relatorio
                51 -  Emprestados
                52 -  Reservados
                53 -  Atraso
                54 -  Todos Livros
 
           _______________RELATORIO______________________ 
            7 - Registrar Usuario
                777 - Todos Usuarios
           ______________________________________________
           ______________________________________________
            6 - SAIR
            ''','')
        opcao = int(input('Digite o Numero da opção: '))
        
        # ------------------ Cadastrar Livro ------------------
        if opcao == 1:
            nomeMain = input("Digite o nome do bibliotecario: ")
            livroMain = input("Digite o nome do livro: ")
            ISBNMain = input("Digite o ISBN do livro: ")
            autorMain = input("Digite o autor do livro: ")
            edicaoMain = input("Digite a edicao do livro: ")
            editoraMain = input("Digite a editora do livro: ")

            livro = Cadastrar_livro(nomeMain, livroMain, ISBNMain, autorMain, edicaoMain, editoraMain)

            print(f"Livro Cadastrado {livro.incluirNovoLivro()}")
            
        # ------------------- Alterar Livro -------------------
        if opcao == 11:
            pesquisaLivrvo = input("Digite o nome do livro para pesquisar: ")
            livexemplo = Cadastrar_livro('', '', '', '', '', '','')
            print(f"{livexemplo.alterarLivro(pesquisaLivrvo)}")
            
        # ------------------- Excluir Livro -------------------
        if opcao == 12:
            excluindoLivro = input("Digite o nome do livro para excluir: ")
            livexemplo = Cadastrar_livro('', '', '', '', '', '','')
            print(f"{livexemplo.excluirLivro(excluindoLivro)}")
        
        # ------------------- Consulta Livro ------------------- 
        if opcao == 13:
            livexemplo2 = Cadastrar_livro('', '', '', '', '', '','')
            DigiteNomeLivro = input("Digite o nome do livro para consulta: ")
            print(f"Livro  {livexemplo2.consultarLivros(DigiteNomeLivro)}")
            
    #__________________________________FECHOU EXEMPLAR____________________________________________________________#

    
    # ------------------ Cadastrar Exemplar ------------------
        if opcao == 2:
            pesquisaLivro = input("Digite o nome do livro para pesquisar: ")
            qtdExemplar = int(input("Digite a quantidade de exemplares: "))
            livexemplo3  = Cadastrar_Exemplar(pesquisaLivro, qtdExemplar)
            print(f"{livexemplo3.incluirNovoExemplar(pesquisaLivro, qtdExemplar)}") 
            
        # ------------------- Pesquisando Exemplar -------------------
        if opcao == 23:
            PesquisaExemplar = input("Digite o nome do livro para pesquisar: ")
            buscaExemplar =  Cadastrar_Exemplar('', '','')
            buscaExemplar2 = buscaExemplar.consultaExemplares(PesquisaExemplar)
            print(f"{buscaExemplar2}")
            
        # ------------------- Alterar Exemplar -------------------
        if opcao == 22:
            PesquisaExemplar = input("Digite o nome do livro para Alteração: ")
            AlteraExemplar23 =  Cadastrar_Exemplar('', '','')
            print(f"{AlteraExemplar23.alterarExemplares(PesquisaExemplar)}")
            
            
        # ------------------- Excluir Exemplar -------------------    
        if opcao == 24:
            excluindoExemplar = input("Digite o nome do livro para excluir: ")
            livexemplo4 = Cadastrar_Exemplar('', '','')
            print(f"{livexemplo4.excluirExemplares(excluindoExemplar)}")
            
    #__________________________________FECHOU Exemplar ____________________________________________________________#


        # ------------------ Cadastrar Categoria ------------------
        if opcao == 3:
            cadCategoria = input("Digite o nome da categoria: ")
            categoria = Cadastrar_assunto('', cadCategoria)
            
            print(f"{categoria.incluirNovoAssunto(cadCategoria)}")
        
        # ------------------- Consultar Categoria -------------------
        if opcao == 33:
            pesqcateg = input("Digite o nome da categoria para pesquisar: ")
            pescategoria = Cadastrar_assunto('', '','')
            
            print(f"{pescategoria.consultarAssunto(pesqcateg)}")
                
        # ------------------- Alterar Categoria -------------------
        if opcao == 34:
            pesquisaCategoria = input("Digite o nome da categoria para Alterar: ")
            categoria = Cadastrar_assunto('', '','')
            print(f"{categoria.alterarAssunto(pesquisaCategoria)}")
        
        # ------------------- Excluir Categoria -------------------
        if opcao == 35:
            excateCategoria = input("Digite o nome da categoria para excluir: ")
            categoriaExcluir = Cadastrar_assunto('', '','')
            
            print(f"{categoriaExcluir.excluirAssunto(excateCategoria)}")
        #__________________________________FECHOU Categorias ____________________________________________________________#
  
        # ------------------- Cadastrando Emprestimo -------------------
        
        if opcao == 4: 
            nomeLivro = input("Digite o nome do livro: ")
            datainical = input("Digite a data inicial do emprestimo: ")
            datafinal = input("Digite a data final do emprestimo: ")
            livroEmprestimo4 = Emprestimo('')
            print(f"{livroEmprestimo4.gerarRelatorio(nomeLivro, datainical, datafinal)}")
        
        if opcao == 41:
            livroEmprestimo = input("Digite o nome do livro para emprestimo: ")
            livroEmprestimo2 = Emprestimo(livroEmprestimo)
            print(f"{livroEmprestimo2.cadastrarEmprestimo(livroEmprestimo)}")
            
        if opcao == 43:
            dataCancelamento = input("Digite nome do livro para cancelar emprestimo: ")
            livroEmprestimo43 = Emprestimo('')
            print(f"{livroEmprestimo43.cancelarEmprestimo(dataCancelamento)}")
               
        if opcao == 44:
            dataPesquisa = input("Digite a data para pesquisa: ")
            dataEmprestimo = Emprestimo('')
            print(f"{dataEmprestimo.pesquisarData(dataPesquisa)}")
            
        if opcao == 7:
            cadUsuario = input("Digite o nome do usuario: ")
            cadSenha = input("Digite a senha do usuario: ")
            cadTipo = input("Digite o tipo de usuario: ")
            cadastroUsuario = Usuario(cadUsuario, cadSenha, cadTipo)
            print(f"{cadastroUsuario.cadUser()}")
            
            
            
            
        #_________________________________-relatorios____________________________________________________________#
        
        if opcao == 51:
            LivrosEmprestados = GerarRelatorio()
            print(f"Livros Emprestados: {LivrosEmprestados.todosLivrosEmprestados()}")

        if opcao == 52:
            LivrosReservado = GerarRelatorio()
            print(f"{LivrosReservado.todosLivrosReservados()}")
            
        if opcao == 53:
            LivroEmAtraso = GerarRelatorio()
            print(f"{LivroEmAtraso.emAtraso()}")
                
        if opcao == 54:
            TodosLivros = GerarRelatorio()
            print(f"{TodosLivros.TodosExemplares()}")
        
        if opcao == 777:
            TodosUsers = GerarRelatorio()
            print(f'{TodosUsers.TodosUsuarios()}')
        
else:
    print('Verificação Inválida')


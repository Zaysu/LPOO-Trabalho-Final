from bibliotecario import Bibliotecario, Cadastrar_livro, Cadastrar_Exemplar, Cadastrar_assunto
from datetime import datetime

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if senha == 'Admin' and login == 'Admin':
    opcao = 0
    while opcao != 5:
        print('''Opções:
            _____________________________________
            1 - Cadastrar livro
                11 - Alterar livro
                12 - Excluir livro
                13 - Consultar Livros
            _____________________________________
            2 - Cadastrar exemplar
                22 - Alterar exemplar
                23 - Consultar exemplares
                24 - Excluir exemplar
            _____________________________________
            3 - Cadastrar Categoria
                33 - Consultar Categoria
                34 - Alterar Categoria 
                35 - Excluir Categoria
            4 - Relatorios 
           
            _________________________________________
            _____________________________________
            5 - Sair
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

       # ------------------ Cadastrar Categoria ------------------
        if opcao == 4:
            
            PeriodoInicio = input("Digite a data inicial passada, ex:. 30/03/2022 ")
            PeriodoFinal = input("Digite a data final , ex:. 30/04/2022 ")

            livexemplo2 = Cadastrar_livro('', '', '', '', '', '','')
            print(f"Livro  {livexemplo2.consultarLivrosPeriodo(PeriodoInicio,PeriodoFinal)}")
           
            


else:
    print('Usuário ou senha incorretos')

# Sistema de Cadastro de Livros

import matplotlib.pyplot as plt

# Lista que armazenará os livros cadastrados

livros = [
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'genero': 'Romance'},
    {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula'},
    {'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K. Rowling', 'genero': 'Fantasia'},
    {'titulo': '1984', 'autor': 'George Orwell', 'genero': 'Ficção científica'},
    {'titulo': 'Capitães da Areia', 'autor': 'Jorge Amado', 'genero': 'Drama social'},
    {'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell', 'genero': 'Fábula'},
    {'titulo': 'Memórias Póstumas de Brás Cubas', 'autor': 'Machado de Assis', 'genero': 'Romance'},
    {'titulo': 'O Hobbit', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'},
    {'titulo': 'Ensaio sobre a Cegueira', 'autor': 'José Saramago', 'genero': 'Drama social'},
    {'titulo': 'O Alquimista', 'autor': 'Paulo Coelho', 'genero': 'Fábula'}
]

# Função que retorna uma saudação com base na hora informada pelo usuário

def saudacao():
    hora = int(input("Digite a hora atual (0-23): "))
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
# Função para adicionar um novo livro à lista

def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    genero = input("Gênero do livro:+ ")
    livros.append({'titulo': titulo, 'autor': autor, 'genero': genero})
    print("Livro adicionado com sucesso!")

# Função para listar todos os livros cadastrados

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("Lista de Livros:")
        for i, livro in enumerate(livros, start=1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['genero']})")


# Função para gerar gráfico de quantidade de livros por gênero

def gerar_grafico_por_genero():
    if not livros:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return
    
    # Daods para o gráfico

    contagem_generos = {}
    for livro in livros:
        genero = livro['genero']
        contagem_generos[genero] = contagem_generos.get(genero, 0) + 1

    # Dados para o gráfico

    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())

    # Gera o gráfico de barras

    plt.bar(generos, quantidades, color = 'skyblue')
    plt.title("Quantidade de Livros por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.xticks(rotation = 45, fontsize = 10) # Rotaciona os nomes em 45 graus
    plt.tight_layout()
    plt.show()

# Função principal que exibe o menu e controla o fluxo do programa

def menu():
    print(saudacao())
    print("Bem-vindo ao sistema de cadastro de livros!")

    while True:
        print("\nMenu:")
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Gerar gráfico por gênero")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            gerar_grafico_por_genero()
        elif opcao == '4':
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa

menu()

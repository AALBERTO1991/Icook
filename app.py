import os

restaurant = []

def logo():
    print(""" 
    ███████████████████████████
    █▄─▄█─▄▄▄─█─▄▄─█─▄▄─█▄─█─▄█
    ██─██─███▀█─██─█─██─██─▄▀██
    ▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀
    """)

def options():
    print('1 - Cadastrar restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair do App\n')

def exit():
    os.system('cls') #limpa toda a tela do terminal
    logo()
    print('Icook agradece seu contato!\n')

def invalid_value():
    print('Oh oh - Opção errada')
    input('Digite algo para voltar ao menu principal')
    main()

def register():
    os.system('cls')
    print('Olá, Bem vindo ao cadastro de restaurantes do ICOOK\n')
    print('Vamos começar o Cadastro!')
    name = input('Nome do Restaurante: ')
    restaurant.append(name)
    print(f'o Restaurante {name} foi cadastrado com sucesso!\n')
    input('Aperte Enter para voltar ao menu principal: ')
    main()

def choise():
    try:
        choise_option = int(input('Escolha uma das opções: '))
        match choise_option:
            case 1:
                register()
            case 2:
                print('Lista de Restaurante!\n')
            case 3:
                print('Restaurante Ativo!\n')
            case 4:
                exit()
            case _:
                invalid_value()
    except:
        invalid_value()

def main():
    os.system('cls')
    logo()
    options()
    choise()

if __name__ == '__main__':
    main()

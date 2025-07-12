def exibir_menu():
    print("=== Sistema de Cadastro ===")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Sair")

def cadastrar_usuario(usuarios):
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    idade = input("Digite a idade: ")
    usuario = {"nome": nome, "email": email, "idade": idade}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("=== Lista de Usuários ===")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")

def main():
    usuarios = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
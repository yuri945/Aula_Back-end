
tarefas = []

def adicionar_tarefa():
    
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas.append(nova_tarefa)
    print("✨ Tarefa adicionada com sucesso!\n")

def listar_tarefas():
    
    if not tarefas:
        print("📭 A lista de tarefas está vazia.\n")
        return False 
    
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t}")
    print() 
    return True 

def atualizar_tarefa():
    
    if listar_tarefas():
        try:
            indice = int(input("Digite o número da tarefa a ser atualizada: ")) - 1
            if 0 <= indice < len(tarefas):
                nova_tarefa = input("Digite o novo texto da tarefa: ")
                tarefas[indice] = nova_tarefa
                print("🔄 Tarefa atualizada com sucesso!\n")
            else:
                print("❌ Número inválido. Essa tarefa não existe.\n")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro.\n")


while True:
    print("--- Menu de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    print() 

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        print("Saindo do programa... Até logo! 👋")
        break
    else:
        print("❌ Opção inválida. Tente novamente.\n")

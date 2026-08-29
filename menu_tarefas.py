tarefas = []

while True:
    print("\n1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação de uma tarefa")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()

        if titulo == "":
            print("O título não pode estar vazio.")
            continue

        prioridade = input("Digite a prioridade (baixa, média ou alta): ").strip().lower()

        if prioridade not in ["baixa", "média", "alta"]:
            print("Prioridade inválida.")
            continue

        tarefa = {
            "titulo": titulo,
            "prioridade": prioridade,
            "situacao": "pendente"
        }

        tarefas.append(tarefa)

        print("Tarefa cadastrada com sucesso.")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTAREFAS")

            for indice, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{indice} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            continue

        numero = input("Digite o número da tarefa: ")

        if not numero.isdigit():
            print("Número inválido.")
            continue

        indice = int(numero) - 1

        if indice >= 0 and indice < len(tarefas):
            tarefas[indice]["situacao"] = "concluída"
            print("Tarefa concluída com sucesso.")
        else:
            print("Tarefa inexistente.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")
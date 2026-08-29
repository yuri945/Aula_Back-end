chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Computador não liga",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "hardware"
    },
    {
        "id": 4,
        "titulo": "Erro ao acessar o e-mail",
        "prioridade": "média",
        "situacao": "fechado",
        "categoria": "acesso"
    },
    {
        "id": 5,
        "titulo": "Sistema apresentando lentidão",
        "prioridade": "baixa",
        "situacao": "em atendimento",
        "categoria": "sistema"
    }
]

print("TODOS OS CHAMADOS")
print()

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("------------------------------")

situacao_desejada = "aberto"
encontrou_chamado = False

print()
print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print()

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("------------------------------")
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado.")

situacao_desejada = "cancelado"
encontrou_chamado = False

print()
print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print()

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("------------------------------")
        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado.")

id_chamado = 1
nova_situacao = "fechado"
chamado_encontrado = False

print()
print("ATUALIZAÇÃO DE CHAMADO")
print()

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        print(f"Chamado {id_chamado} atualizado com sucesso.")
        print(f"Nova situação: {nova_situacao}")
        chamado_encontrado = True
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")

id_chamado = 10
nova_situacao = "fechado"
chamado_encontrado = False

print()

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao
        print(f"Chamado {id_chamado} atualizado com sucesso.")
        chamado_encontrado = True
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")

categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print()
print("CATEGORIAS")
print()

for categoria in categorias:
    print(categoria)
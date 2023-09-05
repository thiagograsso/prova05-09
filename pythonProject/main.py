def produtoCartesiano(sem_duplicados, sem_duplicados2):
    produtoCartesiano = [(x, y) for x in sem_duplicados for y in sem_duplicados2]
    return produtoCartesiano

sem_duplicados = []
sem_duplicados2 = []
contador = 0
user = int(input("Número de elementos para 1: "))
lista = []
while contador < user:
    contador += 1
    dados = input("Digite um elemento: ")
    lista.append(dados)
sem_duplicados = set(lista)

contador2 = 0
user2 = int(input("Número de elementos para 2: "))
lista2 = []
while contador2 < user2:
    contador2 += 1
    dados2 = input("Digite um elemento: ")
    lista2.append(dados2)
sem_duplicados2 = set(lista2)

operation = str(input("Entre com a operação desejada (I = interseção, U = união, D = diferença e C = produto cartesiano): "))
if operation.upper() == "I":
    print(sem_duplicados.intersection(sem_duplicados2))
elif operation.upper() == "U":
    print(sem_duplicados.union(sem_duplicados2))
elif operation.upper() == "D":
    print(sem_duplicados.difference(sem_duplicados2))
elif operation.upper() == "C":
    print(produtoCartesiano(sem_duplicados, sem_duplicados2))
else:
    print("Operação inválida.")

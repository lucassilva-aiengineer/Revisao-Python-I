# Tuplas 

# As tuplas são estruturas de dados ordenadas declaradas entre parênteses onde cada elemento 
# é associado a um índice, são muito parecidas com as listas, aceitam uma quantidade indeterminada 
# de elementos de diferentes tipos de dados e aceitam elementos duplicados, porém não são 
# alteráveis. 

nomes = ("Lucas", "João", "Jonas", "Jorge", "John", "Marcos", "Mateus", "Tiago")


# Acessando elementos 

def acessando_elementos()-> None:

    global nomes

    print(nomes[0])
    print(nomes[-1])


    # Acessando elementos por um índice específico 

    if "Tiago" in nomes: 
        print(nomes.index("Tiago"))


    # Função len 

    print("Contagem: " + " " + str(len(nomes)))


    # Fatiamento 

    print(nomes[0: 5])
    print(nomes[:2])
    print(nomes[5:])
    print(nomes[-2])


    # Alterando uma tupla 

    lista_nomes = list(nomes)

    lista_nomes.remove("Tiago")

    nomes = tuple(lista_nomes) 

    print(nomes)


def main():

    acessando_elementos()


if __name__ == '__main__':
    main()
from typing import List

# Conjuntos

# São uma estrutura de dados, baseada nas propriedades da teoria dos conjuntos, 
# não permite elementos duplicados, e não são ordenadas, mas aceitam uma quantidade
# indeterminada de elementos de diferentes tipos e\ou estruturas de dados, além de aceitar operações matemáticas 
# presentes da teoria matemática de conjuntos, como intercessão e união. 


conjunto_1 = {"Mateus", "Mateus", "João", "Lucas", "Marcos", "Carlos"}
conjunto_2 = {"João", "José"}


def teste_1()-> None:

    """
        Os conjuntos não são ordenados
    """

    for _ in range(3):
        print(conjunto_1)


def intercecao()-> set:

    """
        Interceção o que está tanto no conjunto B quanto no conjunto A 
    """

    return conjunto_1 & conjunto_2 


# União 

def uniao()-> set:

    """
        União o que faz parte do conjunto B ou faz parte do conjunto A
    """

    return conjunto_1 | conjunto_2


# A diferença de conjuntos 

def diferenca()-> set:

    """
        Diferença de conjuntos: 
        O que o conjunto A possui que o conjunto B não possui

    """
    return conjunto_1 - conjunto_2

# Operações de comparação 

def comparacao()-> None:

    # if conjunto_1 > conjunto_2:
    #     print("O conjunto A é maior que o conjunto B")
    #     # return True

    # elif conjunto_1 < conjunto_2: 
    #     print("O conjunto A é menor que o conjunto B")

    # else: 
    #     print("Os dois conjuntos possuem a mesma quantidade de elementos.")

    print(conjunto_1 > conjunto_2)


def busca()-> None:

    print("Marcos" in conjunto_1)

def lista_elementos()-> List[str]:

    return list(conjunto_1)

def main()-> None:

    # print(intercecao())
    # print(uniao()) 
    # print(diferenca())
    # comparacao()
    # busca()

    print(lista_elementos())


if __name__ == '__main__':
    main()
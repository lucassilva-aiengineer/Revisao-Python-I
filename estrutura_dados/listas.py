import random 
# Listas 

# Listas são estruturas de dados unidimensionais 
# capazes de admitir  indeterminados elementos de váriados tipos de dados, duplicados, 
# ordenados, e cada um, associado por um índice. 

def introducao():


    def oque_sao_listas()-> None:
        class Pessoa: 
            ... 

        pessoa1 = Pessoa()
        pessoa1.nome = "Marcos"

        print(pessoa1.nome)

        lista_1 =   [False, "nome1", 5, True, 20, 20.5, pessoa1, None]


    def verificar_elementos()-> None:

        if "João" in ["Mateus", "Jonas", "João", "José", "Jordan", "Marcos"]:
            print("João está na lista!")

        else: 
            print("João não está na lista!")



    def acessando_elementos():

        """ 
            Acessando elementos em uma lista 
        """

        lista = ["Mateus", "João", "Lucas", "Marcos", "José", "Pedro"]

        for i in range(len(lista)):
            print(lista[i])


        # Acessando elementos 

        # As listas são ciclicas 
        #           0    1    2
        #          -3    -2    -1

        # lista = ["a", "b", "c"]

        print(lista[0])  # Primeiro item 
        print(lista[1])  # Segundo item   
        print(lista[-1]) # Útimo item  
        print(lista[-2]) # Penúltimo item. 

        # Trocando elementos 
        lista[0] = "zero"
        lista[-1] = "menos um"

        for a in lista:
            print(a)

        # Adicionando vinte elementos. 

        elementos_adicionados, elementos_adicionar = 0, 20 
        while elementos_adicionados <= elementos_adicionar: 

            # lista[len(lista)]

            lista.append(random.randint(0, 1000))
            elementos_adicionados += 1 

        for elemento in lista:
            print(elemento)


    def fatiamento():

        lista = [10, 20, "Lucas", "Marcos", "Mateus", "João", "José"]

        print(lista[0: 4]) # Do índice 0 até o índice anterior ao quatro. 
        print(lista[0: 2])

        print(lista[0: ]) # Indo até o índice final 
        print(lista[: 5]) # Indo até o índice 5, do início até o 4. 


    def juntando_listas()-> None:

        lista_1 = [10, 20, 30, 40]
        lista_1.extend([50, 60, 70, 80, dict(nome= "Lucas"), set()])

        print(lista_1)


        # Utilizando o operador += 

        def operador()-> None:

            lista_2 = [1, 2, 3, 4, 5]

            lista_2 += [10, 20, 30, 40]

            print(lista_2)

        operador()

    def removendo_elementos():

        lista_3 = [10, 40, True, dict(idade= 20, nome= "Mateus"), list([1, 2, 3, 4, 5])]
    # Executando funções 
    # verificar_elementos()
    # acessando_elementos() 

        lista_3.remove(10)

        print(lista_3)


    # juntando_listas()
    # fatiamento()
    removendo_elementos()

def main():

    introducao()
    




if __name__ == '__main__':
    main()
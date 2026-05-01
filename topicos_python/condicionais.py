
# Estruturas de condicionais 
from faker import Faker
import random



def gerar_nomes()-> None:
# faker = Faker('pt_BR')
    faker = Faker('pt_BR')


    lista_nomes = [faker.name() for a in range(1000)]




    marcos = 0 

    for nome in lista_nomes:
        if "marcos" in nome.lower(): 

            marcos += 1 

    print(f"A quantidade de pessoas com o nome Marcos: {marcos}/1000.")


    if len(lista_nomes) > 1000:
        print("Caso a condição A seja cumprida nós executamos o código.")
        print("Nós temos mais que mil nomes anotados.")

    elif len(lista_nomes) > 500: 
        print("Caso A condição anterior não tenha sido cumprida.")
        print("Tente esta aqui!")

        print("Nós temos algo entre quinhentos e mil nomes.")

    else:

        print("Caso nenhuma das condições anteriores se cumpra execute esta.")




def condicionais_2()-> None:

    numeros = [random.randint(0, 10000) for _ in range(1000)] 


    if 100 in numeros:
        
        print("O número cem está nesta lista!")

    else: 
        print("O número cem não faz parte desta lista.")
        
        numeros += [100]


    if 100 in numeros: 
        print("Agora o número 100 está na lista!")




def main():

    # gerar_nomes() 

    condicionais_2()


if __name__ == '__main__':
    main()
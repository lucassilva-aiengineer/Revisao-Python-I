from typing import List
import time 
from faker import Faker

# Loop for

# O loop for se trata de um iterador, ele executa um bloco de código, um bloco de 
# execução um número predeterminado de vezes, ele também pode percorrer estruturas 
# de dados executando blocos de códigos e acessando valores. 




def imprimir_lista()-> None:

    numeros = [1, 10, 15, 12, 14, 13, 25, 24, 32, 100]

    cumprimento_lista = len(numeros)

    for i in range(cumprimento_lista):
        print(numeros[i])




def preencher_lista()-> None:

    lista_alunos: List[tuple] = []

    quantidade = int(input("Indique a quantidade de alunos: "))

    for a in range(quantidade):

        nome = input("Indique o nome aluno: ")
        idade = int(input("Indique a idade do aluno: "))

        nota_1 = float(input("Indique a nota da primeira avaliação: "))
        nota_2 = float(input("Indique a nota da segunda prova: "))


        notas = {"av_1": nota_1,
                "av_2": nota_2}        

        pessoa = (nome, idade, notas)

        lista_alunos.append(pessoa)

        opcao = input("Para para sair digite s: ")

        if opcao.lower() == "s":

            # Assim podemos para o código antes de termos todas as iterações. 
            print("Saindo...")
            time.sleep(2)
            break


    for aluno in lista_alunos: 
        print(f"""Nome: {aluno[0]}
Idade aluno: {aluno[1]}
Nota avaliação 1: {aluno[2]['av_1']}
Nota avaliação 2: {aluno[2]['av_2']}

Média Aritmética: {(aluno[2]['av_1'] + aluno[2]['av_2']) / 2}""")



def modificando_valores()-> None:
    numeros = [10, 25, 22, 23, 30, 42, 45, 44]


    for numero in numeros:
        # numeros.append(numero + 1)

        nv_numero = numero + 10 
        numeros.remove(numero)
        numeros.append(nv_numero)

    print(numeros)


class Produto:

    def __init__(self, nome: str= "", marca: str= "", preco: float= 0.0):

        self.nome = nome 
        self.marca = marca 
        self.preco = preco 


def prencher_lista(): 

    pessoas: List[Produto] = []

    faker = Faker('pt_BR')

    pessoas_adicionar = 10 
    pessoas_adicionadas = 0


    produtos = ["Arroz", "Feijão", "Leite-Condensado", "Creme de leite"]

    while pessoas_adicionadas < pessoas_adicionar:

        nome = random.choice(produtos)
        marca = faker.company()
        preco = random.unifform(1, 2)

        pessoa = Produto(nome, marca, preco)
        pessoas.append(pessoa)


        pessoas_adicionadas += 1


    # Construindo um csv 
    # Construindo um csv DataFrame 

### REVISAR CADA TÓPICO ESPECÍFICO ###

def teste():

    faker = Faker('pt_BR')

    print(faker.company())

def main():
    # imprimir_lista()
    # preencher_lista()
    # modificando_valores()

    # teste()
    ... 


if __name__ == '__main__':
    main()
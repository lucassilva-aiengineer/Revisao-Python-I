from typing import List
import time 
from faker import Faker
from typing import List, Optional, Tuple, Union
import random

# Optional, ou um tipo de dados específico ou None 
# Union, um dos tipos de dados indicados. Exemplo: int, str, bool, float

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


def topicos()-> None:



    # def contratar(candidato, contratados: List[Tuple[str, int]]= [])-> None:

        # contratados.append(candidato)

        # return contratados 

        # contratados 

    candidatos = [("João", 100), ("Jonas", 80), ("Joaquim", 15)]


    lista_contratatados: List[Tuple[str, int]] = []
    def contratar(candidato: Tuple[str, int], lista_candidatos: List[Tuple[str, int]]):
        lista_candidatos.append(candidato)



    for candidato in candidatos:

        """
            Caso o candidato tenha uma pontuação 
        """
        if candidato[1] <= 80:
            continue
        contratar(candidato, lista_contratatados)


    def exibir_contratados(contratados_list: List[Tuple[str, int]]):

        # O enumerate transforma um lista de itens em uma lista de tuplas 
        # onde o índice 0 se trata do índice do valor e o índice 1 se trata 
        # do item. 

        print("Exibição 1: ")
        for index, candidato in enumerate(contratados_list):

            print(f"Nome candidato n° {index + 1}: {candidato[0]}")
            print(f"Pontuação condidato: {candidato[1]}") 

        print("Exibição 2: ")
        indice = 1
        for nome, nota in contratados_list:
            print(f"Índice: {indice}")
            print(f"Nome: {nome}")
            print(f"Nota: {nota}")



    def encontrar_valor()-> None:

        # a palavra chave break interrompe a execução 
        # do laço de repetição. 

        tentativas = 0
        for a in range(0, 101):
            numero = random.randint(0, 9)

            print(numero)
            if numero == 9:
                print("Número 9 encontrado!")
                tentativas += 1
                break 


            tentativas += 1 
        print(f"Foram necessárias {tentativas} tentativas.")

    # exibir_contratados(lista_contratatados)

    
    encontrar_valor()
def teste1():

    for a in range(10):
        if a == 1:
            print("Número Igual a A 1")
            continue # Pulamos esta interação para a próxima.

        print(a)






def main():
    # imprimir_lista()
    # preencher_lista()
    # modificando_valores()

    # teste()
    
    # teste1()
    topicos()

if __name__ == '__main__':
    main()
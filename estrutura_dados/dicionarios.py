# Dicionários 
# Os dicionários são uma das estruturas de dados das mais legais dentro da linguagem python 
# é uma estrutura ordenada formada seguindo uma estrutura de chave valor, onde a chave se trata 
# de um tipo de dado imutável, como um inteiro ou string, que tem a si associado qualquer tipo 
# de valor, de qualquer tipo e\ou estrutura de dados, é uma estrutura ordenada que pemite alterações. 



pessoa = {"nome": "Mateus", "idade": 20, "casado": True}


def acessando_valores():

    # Alterando valor pela chave 

    if "nome" in pessoa:
        print(True)

        pessoa["nome"] = "João"

    print(pessoa["nome"])   # Engraçado, parece que conseguimos alterar o dicionário como 
    # se este fosse uma variável global. 


    # Acessando um valor no dicionário 

    # get(), o método get() retorna um valor padrão caso a chave buscada não seja encontrada. 

    print(pessoa.get("sobrenome", "Chave não encontrada"))


def removendo_valores():

    # Indicamos o dicionário como sendo uma variável global, tornando-a passível de 
    # alteração pela fução. 

    global pessoa   

    # Utilizando o método pop para remover a chave nome. 

    print(pessoa.pop("nome"))

    # print(pessoa["nome"])

    print(pessoa.get("nome", "Nome não encontrado"))


def acessando_termos()-> None:

    # Acessando as chaves

    print(list(pessoa.keys())) 

    # Acessando valores 

    print(pessoa.values())

    valores_dicionario = pessoa.values()

    for valor in valores_dicionario:
        print(valor)

    # Acessando uma lista de tuplas contendo cada par chave-valor.

    for chave, valor in pessoa.items():
        print("Chave: ", chave, "Valor: ", valor)


def alteracoes()-> None:

    quantidade_pares = len(pessoa)
    print(quantidade_pares)

    pessoa["cidade_origem"] = "Goiânia"

    print(pessoa["cidade_origem"])

    # Deletando chave 

    print(pessoa.keys())

    del pessoa["idade"]

    print(pessoa.get("idade", "chave não encontrada!"))

    # Criando uma cópia do dicionário 

    copia_dicionario = pessoa.copy()

    print(copia_dicionario["nome"])

    print(copia_dicionario.items())



def main():

    # acessando_valores()
    # removendo_valores()
    # acessando_termos() 
    alteracoes()



if __name__ == '__main__':
    main()
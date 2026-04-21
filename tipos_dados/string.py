from typing import Tuple

# Strings 

# As strings se trata de um tipo de dado que se resume nas 
# cadeias de carcteres, portando, um tipo de dado textual. 


def strings()-> Tuple[str, str]: 

    string_a = 'Mateus'
    string_b = "José"

    return string_a, string_b



def concatenando_string()-> str:

    """
        Concatenando, juntando strings. 
    """ 

    nome = "Mateus" 
    frase = "O nome dele é " + nome + ". Ele possui" + " " + str(20) + " anos"

    return frase


def concatenando_strings_2()-> str:

    """
        Utilizando o operador += para juntar 
        diferentes strings. 
    """

    frase_1 = "Lucas possui uma BMW 320i grafite, um "
    substantivo = "carro"

    frase_2 = " muito legal e confortável."

    frase_1 += substantivo 

    frase_1 += frase_2 

    frase_1 += " \nEle tem apenas " + str(22) + " anos de idade."

    return frase_1 


def string_multline()-> str:

    """
        As strings podem ter várias linhas 
    """

    return  """
                Mateus gosta de carros feitos pela 
                mercedez bens.
        """


def metodos_string():

    nome = "Marcos"

    # Todas as letras maiúsculas
    print(nome.upper())
    print("Mateus".upper())

    # Todas as letras minúsculas
    print(nome.lower())
    print("Mateus".lower())


    # A letras inícial maiúscula, enquanto as outras são minúsculas. 
    print("mAteuS juNIoR".title())


    # Verificando se todas as letras são minúsculas 
    print("mateus".islower())

    # Verificando se todas as letras são minúsculas 
    print("MATEUS".isupper())


    # Verifica se a palavra inícia com a letra M
    print("Mateus".startswith("M"))


    # Verifica se a palavra termina com a letra s. 
    print("Mateus".endswith("s"))

    # Trocando partes de uma string por outras 
    print("Lucas gosta de comer pizza".replace("pizza", "chocolate"))


    # Criando uma lista de palavras seguindo um caracter específico como limitador ou separador. 

    texto = "Um dois três quatro cinco"
    lista_palavras = texto.split(" ")

    for palavra in lista_palavras:
        print(palavra)


    # Removendo caracteres de espaço sobressalentes, antes e depois da string. 

    print("  nome@servidor.com  ".strip())


    # Juntando uma lista de palavra em uma única string 

    palavras = ["O", "garoto", "joga", "bola", "nas", "manhãs", "de", "quinta"]
    nova_frase = "|".join(palavras)

    print(nova_frase)


def find_a(texto, palavra):

    """
        Retornando o índice de uma palavra encontrada. 
    """
    return texto.find(palavra)
    

def verificar_elemento(texto, valor_buscado):

    return valor_buscado in texto 


def fatiamento():

    string = "Marcos"

    print(string[0])
    print(string[2:])
    print(string[:4])


def main():

    # minha_string = strings()

    # print(minha_string[0], minha_string[1])

    # minha_string = concatenando_string()
    # print(minha_string)

    # minha_string = concatenando_strings_2() 
    # print(minha_string)

    # minha_string = string_multline()
    # print(minha_string)

    # metodos_string() 

    print(find_a("Eu gosto de comer pizza", "pizza"))

    print(verificar_elemento("A rua 12345 é uma das ruas mais importantes da cidade", "rua")) 
    fatiamento()


if __name__ == '__main__':
    main()
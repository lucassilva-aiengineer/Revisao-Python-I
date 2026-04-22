# Boleanos 

# Valores boleanos são valores ligados a lógica boleana que é por natureza bivalente, 
# assumindo apenas a existência de dois valores logicos possíveis True e False de acordo com 
# os princípios da lógica. 



def boleano(variavel):

    if variavel:
        print("Sim, choveu!")

    else: 
        print("Não, Choveu!")


# Algumas representações 

def representacoes(valor):

    if valor: 
        print("Verdadeiro")

    else: 
        print("Falso")



def alguns_testes():

    
    chover = False 

    boleano(chover)


    string_vazia = ""
    string_nao_vazia = "texto"
    representacoes(string_vazia)

    valor_a = 0 
    valor_b = 100 

    representacoes(valor_a)
    representacoes(valor_b)


    print(type(True) == bool)
    print(type("texto") == str)


def algumas_funcoes_globais():

    # A função any() retorna True caso ao menos algum valor seja verdadeiro. 
    print(any([True, False, False]))
    print(any([False, False, False]))


    # A função all() retorna verdadeiro somente quando todos os valores forem 
    # verdadeiros. 


    print(all([True, True, True]))
    print(all([False, False, False]))

def main():

    algumas_funcoes_globais()




if __name__ == '__main__':
    main()
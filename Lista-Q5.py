class node:
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

class ListDuplaEnc:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insert(self, dado):
        no = node(dado)
        #primeira inserção na lista
        if self.head is None:
            self.head = no
            self.tail = no
        else:
            no.prev = self.tail
            no.next = None
            self.tail.next = no
            self.tail = no
        self._size += 1

    #Retorna o tamanho da lista
    def __len__(self):
        return self._size

    def __str__(self):
        aux = self.head
        prim = ''
        while aux:
            prim += str(aux.info) + " ; "
            aux = aux.next
        return prim

#Função interativa
def ehPalindromo(data):
    #Verifica se é inteiro ou não
    if type(data) == int:
        data = str(data)
    lista = ListDuplaEnc()
    #Insere os caracteres na lista
    for i in data:
        lista.insert(i)

    if verifyPalindromo(lista):
        print(f"{data} É palindromo")
    else:
        print(f"{data} Não é palindromo")

#Função recursiva
def ehPalRec(data):
    #Verifica se é inteiro ou não
    if type(data) == int:
        data = str(data)
    lista = ListDuplaEnc()
    #Insere os caracteres na lista
    for i in data:
        lista.insert(i)
    if len(lista) < 2:
        print(f"{data} Não é palindromo")
    elif verifyPalRec(lista.head, lista.tail):
        print(f"{data} É palindromo")
    else:
        print(f"{data} Não é palindromo")

#Função de comparação das extremidades
def verifyPalindromo(lista):
    init = lista.head
    end = lista.tail
    tam = len(lista)
    if tam < 2:
        return False
    #Irá percorrer até chegar na metade da palavra ou numero
    while tam//2 > 0:
        if init.info != end.info:
            return False
        else:
            init = init.next
            end = end.prev
            tam -=1
    return True

#Função recursiva, percorre a palavra inteira, até head e tail forem nulos
def verifyPalRec(no1, no2):
    if no1 is None and no2 is None:
        return True
    elif no1.info == no2.info:
        return verifyPalRec(no1.next, no2.prev)
    else:
        return False

#Main
if __name__ == '__main__':

    a = 13232
    ehPalindromo(a)

    b = 2222
    ehPalRec(b)

    c = 'osso'
    ehPalindromo(c)
    
    d = 'ovo'
    ehPalRec(d)

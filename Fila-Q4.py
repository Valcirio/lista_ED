#Classe da Fila
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, dado):
        no = Node(dado)

        if self.head is None:
            self.head = no
        if self.tail is None:
            self.tail = no
        else:
            self.tail.prox = no
            self.tail = no
            

    def dequeue(self):
        if self.head is None:
            print("Fila vazia!")
            return
        else:
            aux = self.head.dado
            self.head = self.head.prox
            return aux
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self) -> str:
        prim = ''
        aux = self.head
        while aux:
            prim += str(aux.dado) + '-> '
            aux = aux.prox
        return prim




#Função que verifica se o número é primo
def verifPrimo(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


def mmc(valor, queue):
    #O programa irá dividir o numero pelo maior numero primo possivel em cada rodada
    d = valor
    while True:
        if valor == 1:
            return queue
        elif d == 2:
            queue.enqueue(d)
            valor = valor//d
        #Se o numero é primo e o valor é divisível sem deixar resto
        elif verifPrimo(d) and valor%d == 0:
            queue.enqueue(d)
            valor = valor//d
        #Condição que vai diminuindo o valor do divisor até achar um número primo
        else:
            d -= 1

#Main
if __name__ == "__main__":

    #cria fila
    queue = Fila()

    #Printa a fila em ordem decrescente
    print(mmc(3960, queue))
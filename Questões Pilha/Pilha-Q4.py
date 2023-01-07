import random

class PilhaStatic:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

    def isFull(self):
        if self.capacity == self.size:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Pilha Cheia!")
            return
        else:
            self.storage[self.size] = data
            self.size +=1

    def pop(self):
        if self.size == 0:
            print("Pilha vazia!")
            return
        else:
            aux = self.storage[(self.size)-1]
            self.size -= 1
            return aux
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self) -> str:
        prim = ''
        aux = self.storage
        for i in range(0, self.size):
            prim += str(self.storage[i]) + ' ; '
        return prim

#Função que distibui aleatoriamente valores de um vetor para n vetores usando random.choice.
def orderTo3Decks(stacks, deck):
    while deck.size != 0:
        stackChosen = random.choice(stacks)
        if stackChosen.isFull() is False:
            stackChosen.push(deck.pop())
    return stacks

#Função que distibui aleatoriamente valores de n vetores para um vetor usando random.choice.
def organizeToOne(stacks, mainStack):
    while mainStack.isFull() is False:
        stackChosen = random.choice(stacks)
        if stackChosen.size != 0:
            mainStack.push(stackChosen.pop())
    return mainStack

#Main
if __name__ == "__main__":

    #Baralho Inicial sem estar ordenado, indo sequencialmente: copas, ouros, espadas, paus
    Baralho = PilhaStatic(52)

    for count in range(0,13):
        Baralho.push('C'+str(count))
        
    for count in range(0,13):
        Baralho.push('O'+str(count))

    for count in range(0,13):
        Baralho.push('E'+str(count))

    for count in range(0,13):
        Baralho.push('P'+str(count))

    # Cria as três pilhas para adicionar as cartas 
    pilha = [0]*3
    pilha[0] = PilhaStatic(16)
    pilha[1] = PilhaStatic(16)
    pilha[2] = PilhaStatic(20)

    #Passa as cartas do baralho de 52 utilizando random.choice, para as três pilhas
    pilha = orderTo3Decks(pilha, Baralho)

    mainStack = PilhaStatic(52)

    #Passa as cartas das três pilhas utilizando random.choice, para um novo pilha de 52
    maintack = organizeToOne(pilha, mainStack)

    # Print do primeiro embaralhamento
    print(f"{mainStack} tamanho: {mainStack.size}\n\n\n")

    #Repetindo o processo: distribuindo as cartas do deck ja embaralhado e ...
    # depois passando das três pilhas aleatoriamente para a pilha de 52 novamente
    pilha = orderTo3Decks(pilha, mainStack)
    maintack = organizeToOne(pilha, mainStack)

    # Print do segundo embaralhamento
    print(f"{mainStack} tamanho: {mainStack.size}")

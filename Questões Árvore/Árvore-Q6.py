import random

class node:
    def __init__(self, info):
        self.info = info
        self.next = None

class Lista:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, dado):
        #primeira inserção na lista
        if self.root is None:
            self.root = node(dado)
        
        else:
            no = self.root
            while no.next:
                no = no.next
            no.next = node(dado)
        self.size +=1

    def __str__(self):
        return self.__repr__()

    def __repr__(self) -> str:
        prim = ''
        aux = self.root
        while aux:
            prim +=  str(aux.info) + ' -> '
            aux = aux.next
        return prim

class Heap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [0]*capacity
        self.maxHeap = None
        self.minHeap = None
        self.size = 0


    #Método de inserção da Lista para o storage da classe Heap
    def insertArray(self, pointer):
        no = pointer
        while no:
            self.insert(no.info)
            no = no.next

 # Métodos de procura de index dos pais e dos filhos
 
    def fatherIndex(self, index):
        return (index-1)//2

    def leftChildIndex(self, index):
        return 2*index + 1

    def rightChildIndex(self, index):
        return 2*index + 2

# Métodos para verificar a existência dos pais e dos filhos

    def hasFather(self, index):
        return self.fatherIndex(index) >=0

    def hasLeft(self, index):
        return self.leftChildIndex(index) < self.size

    def hasRight(self, index):
        return self.rightChildIndex(index) < self.size

# Métodos para definir as folhas

    def father(self, index):
        return self.storage[self.fatherIndex(index)]

    def leftChild(self, index):
        return self.storage[self.leftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.rightChildIndex(index)]

    # Verifica se está cheio
    def isFull(self):
        return self.size == self.capacity
    
    # Método de inserção
    def insert(self, data):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1

    # Método de verificação do storage
    def verifyHeap(self, index):
        #Verifica se existe filho à esquerda, e chama o metodo com o índice do filho à esquerda
        if self.hasLeft(index):
            print(index)
            self.verifyHeap(self.leftChildIndex(index))

        #Verifica se existe filho à direita, e chama o metodo com o índice do filho à direita
        if self.hasRight(index):
            self.verifyHeap(self.rightChildIndex(index))
        
        #Se o índice tem pai, inicia a comparação, o pai sendo maior, é maxHeap, caso contrário, minHeap. 
        if self.hasFather(index):
            if self.father(index) > self.storage[index]:
                self.maxHeap = True
            else:
                self.minHeap = True

    def __str__(self):
        aux = self.storage
        prim = ''
        for i in aux:
            prim += str(i) + '; '
        return prim

#Função para verificar se é um heap, sendo ele, maxHeap ou minHeap
def ehHeap(raiz):
    #cria o Heap do tamanho da lista
    possivelHeap = Heap(raiz.size)

    #Insere a lista no storage para a comparação
    possivelHeap.insertArray(raiz.root)

    #inicia a comparação sempre no índice 0
    possivelHeap.verifyHeap(0)

    #Se tanto o maxHeap == True, quanto o minHeap, então a lista não é um Heap
    if possivelHeap.maxHeap == True and possivelHeap.minHeap == True:
        return 0
    if possivelHeap.maxHeap == None:
        return -1
    else:
        return 1

if __name__ == "__main__":
    
    #Criação das Listas
    listMin = Lista()
    listMax = Lista()
    normalList = Lista()

    #Adicionando os valores, ordem crescente
    for i in range(0, 7):
        listMin.append(i)

    #Adicionando os valores, ordem decrescente
    for i in range(0, 7):
        listMax.append(7 - i)

    #Adicionando os valores, aleatórios
    for i in range(0, 7):
        normalList.append(random.randint(0,15))

    print("Resultados: 0 não é heap; -1 minHeap; 1 maxHeap\n")
    print(f"A lista: {listMin} = {ehHeap(listMin)}")
    print(f"A lista: {listMax} = {ehHeap(listMax)}")
    print(f"A lista: {normalList} = {ehHeap(normalList)}")
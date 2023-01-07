import random

class Heap:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

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

# Método de troca
    def swap(self, index1, index2):
        aux = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = aux
    
# Método de inserção
    def insert(self, data, type):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1
        if type == 1:
            self.upMinHeap(self.size -1)
        else:
            self.upMaxHeap(self.size -1)

# Organiza o Heap de baixo para cima
    def upMinHeap(self, index):
        while(self.hasFather(index) and self.father(index) > self.storage[index]):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)

    def upMaxHeap(self, index):
        while(self.hasFather(index) and self.father(index) < self.storage[index]):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)


    def downMinHeap(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index] < self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def downMaxHeap(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index] < self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
    
    def __str__(self):
        aux = self.storage
        prim = ''
        for i in aux:
            prim += str(i) + '; '
        return prim

#Main
if __name__ == "__main__":
    #Função para adicionar um vetor, podendo ser organizado em minHeap ou maxHeap
    def HeapiFy(array, size, type):
        heap = Heap(size)
        for i in array:
            heap.insert(i, type)
        return heap

    tamanhoVetor = int(input("Adicione um tamanho de vetor que deseja:"))
    vetor = []
    #Adiciona numeros aleatorios para o vetor
    for i in range(0, tamanhoVetor):
        vetor.append(random.randint(0, 30))

    print(f"Vetor à ser Ordenado: {vetor}\n")

    minHeap = HeapiFy(vetor, len(vetor), 1)

    maxHeap = HeapiFy(vetor, len(vetor), 2)

    print(f"minHeap: {minHeap}\n")
    print(f"maxHeap: {maxHeap}\n")


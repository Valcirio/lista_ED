import random

class Pessoa:
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return self.__repr__()

    def __repr__(self) -> str:
        return str(self.matricula)+";"+self.nome+";"+str(self.nota)

#Selection Sort
def selectionSort(lista, type):
    tamanho = len(lista)
    if type == 1:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].matricula < lista[minIndex].matricula:
                    minIndex = j
            if lista[i].matricula > lista[minIndex].matricula:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]
    elif type == 2:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].nome < lista[minIndex].nome:
                    minIndex = j
            if lista[i].nome > lista[minIndex].nome:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]
    else:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].nota < lista[minIndex].nota:
                    minIndex = j
            if lista[i].nota > lista[minIndex].nota:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]

#Insertion Sort
def insertionSort(lista, type):
    tamanho = len(lista)
    if type == 1:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].matricula > key.matricula:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key
    elif type == 2:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].nome > key.nome:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key
    else:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].nota > key.nota:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key

#Merge Sort
def mergeSort(lista, type, init=0, end=None):
    if end is None:
        end = len(lista)
    if (end-init) > 1:
        middle = (end+init)//2
        mergeSort(lista, type, init, middle)
        mergeSort(lista, type, middle, end)
        merge(lista, type, init, middle, end)

def merge(lista, type, init, middle, end):
    leftList = lista[init:middle]
    rightList = lista[middle:end]
    topLeft, topRight = 0, 0
    if type == 1:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].matricula < rightList[topRight].matricula:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1
    elif type == 2:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].nome < rightList[topRight].nome:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1
    else:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].nota < rightList[topRight].nota:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1

#Quick Sort
def quickSort(lista, type, init=0, end=None):
    if end is None:
        end = len(lista)-1
    if init < end:
        pivot = partition(lista, type, init, end)
        quickSort(lista, type, init, pivot-1)
        quickSort(lista, type, pivot+1, end)

def partition(lista, type, init, end):
    pivot = lista[end]
    index = init
    if type == 1:
        for j in range(init, end):
            if lista[j].matricula <= pivot.matricula:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index
    elif type == 2:
        for j in range(init, end):
            if lista[j].nome <= pivot.nome:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index
    else:
        for j in range(init, end):
            if lista[j].nota <= pivot.nota:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index

#Main
if __name__ == "__main__":

    pessoa = [0]*8

    pessoa[0] = Pessoa(211, 'joao', 7.5)
    pessoa[1] = Pessoa(221, 'mateus', 7.0)
    pessoa[2] = Pessoa(111, 'vitor', 8.1)
    pessoa[3] = Pessoa(210, 'ricardo', 6.2)
    pessoa[4] = Pessoa(220, 'isaac', 4.5)
    pessoa[5] = Pessoa(310, 'enzo', 7.0)
    pessoa[6] = Pessoa(400, 'Raquel', 9.0)
    pessoa[7] = Pessoa(320, 'Debora', 8.0)
    
    lista = []
    for i in range(8):
        lista.append(pessoa[i])

    #Quando type recebe 1, a função compara a matricula;
    #Quando recebe o 2, compara o nome; ultimo caso a nota, que está em um else
    print(lista)
    selectionSort(lista, 1)
    print(lista)



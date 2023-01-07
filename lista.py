class node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None

class Lista:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, dado):
        #primeira inserção na lista
        if self.root is None:
            self.root = node(dado)
        
        else:
            no = self.root
            while no.next:
                no = no.next
            no.next = node(dado)
        self._size += 1

    def __getitem__(self, index):
        no = self.root
        for i in range(index):
            if no:
                no = no.next
            else:
                print("Não existe esse índice")
        if no:
            return no.info  
        print("Não existe esse índice")

    def __setitem__(self, index, data):
        no = self.root
        for i in range(index):
            if no:
                no = no.next
            else:
                print("Não existe esse índice")
        if no:
            no.info = data
        else:
            print("Não existe esse índice")

    def search(self, data):
        no = self.root
        i = 0
        while no:
            if no.info == data:
                return i
            no = no.next
            i += 1
        print("Elemento não está na lista")
        
    def __len__(self):
        return self._size

    def __str__(self):
        aux = self.root
        prim = ''
        while aux:
            prim += str(aux.info) + " ; "
            aux = aux.next
        return prim

list = Lista()

list.insert(12)
list.insert(2)
list.insert(9)

print(len(list))
print(list[2])

print(list.search(2))

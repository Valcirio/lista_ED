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


#Main
if __name__ == "__main__":
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.colchete = 0
        self.chaves = 0
        self.parenteses = 0

    def push(self, data):
        no = Node(data)
        #Verica o dado inserido no novo nó à ser inserido na pilha
        if no.data == '(':
            self.parenteses = self.parenteses + 1
        elif no.data == ')':
            self.parenteses = (1 - self.parenteses)*(-1)
        elif no.data == '[':
            self.colchete = self.colchete +1
        elif no.data == ']':
            self.colchete = (1 - self.colchete)*(-1)
        elif no.data == '{':
            self.chaves = self.chaves + 1
        elif no.data == '}':
            self.chaves = (1 - self.chaves)*(-1)
            

        no.prox = self.topo
        self.topo = no

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return
        else:
            aux = self.topo.data
            self.topo = self.topo.prox
            return aux

    def __str__(self):
        prim = ''
        aux = self.topo
        while aux:
            prim +=  str(aux.data) + ' -> '
            aux = aux.prox
        return prim



def ehValido(expression):
    pilha = Pilha()
    #Percorre toda a expressão, inserido cada caractere na pilha
    for i in expression:
        pilha.push(i)
    #Verifica o estado de cada combinação validada ou invalidada dentro da pilha
    if pilha.parenteses != 0:
        print(f"A Expressão {expression} é Inválida!\n")
        return
    elif pilha.chaves != 0:
        print(f"A Expressão {expression} é Inválida!\n")
        return
    elif pilha.colchete != 0:
        print(f"A Expressão {expression} é Inválida!\n")
        return
    else:
        print(f"A Expressão {expression} é válida\n")
        return

#Main
if __name__ == "__main__":
    
    calc1 = '{[(5 × 7)/5] × 4 - [(5 × 7) × 2]} /(3 × 6)'

    ehValido(calc1)

    calc2 = '{2 + [(16 + 2 ∧ 3) - 4)} × 3'

    ehValido(calc2)
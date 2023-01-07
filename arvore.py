import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None

    def __str__(self):
        return str(self.data)
     

class TreeBinarySearch:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def insertNode(self, data):
        treeTemp = Node(data) 
        return treeTemp

    def insert(self, value, node=None):

        father = None
        aux = self.root
        #Antes de inserir o valor, ele percorre até encontrar um folha
        while(aux):
            father = aux
            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if father is None:
            self.root = self.insertNode(value)
        elif value < father.data:
            father.left = self.insertNode(value)
        else:
            father.right = self.insertNode(value)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return node 
        if node.data == value:
            return TreeBinarySearch(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node)
        if node.right:
            self.inorder(node.right)

    def posorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.posorder(node.left)
        if node.right:
            self.posorder(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        leftH = 0
        rightH = 0
        if node.left:
            leftH = self.height(node.left)
        if node.right:
            rightH = self.height(node.right)
        if rightH > leftH:
            return rightH + 1
        else:
            return leftH + 1

if __name__ == "__main__":
    arv = TreeBinarySearch(15)
    lista = [6, 20, 3, 8, 18, 22, 7]
    for i in lista:
        arv.insert(i)

    print(arv.height())


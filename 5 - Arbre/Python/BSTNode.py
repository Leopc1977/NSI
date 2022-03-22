from arbreBinaire import Node
class BST(Node):
    def __init__(s,key):
        Node.__init__(s,key)    
    def printAll(s):
        print("Current Node: ", s.key)
        if not s.isLeaf():
            print("Left: ",s.left)
            print("Right: ",s.right)
            if s.left:  
                s.left.printAll()
            if s.right: 
                s.right.printAll() 
        return
    def search(s,v):
        if s.key == v:
            return True
        elif s.isLeaf():
            return False
        nextNode = None
        if s.key<=v:
            nextNode = s.left
        else: 
            nextNode = s.right
        return nextNode.search(v)
    def insert(s,v):
        if v <= s.key:
            if s.left:
                s.left.insert(v)
            else:
                s.left = BST(v)
        else:
            if s.right:
                s.right.insert(v)
            else:
                s.right = BST(v)
    def inOrderTraversal(s):
        lst = []
        if s.left:
            if s.left.isLeaf():
                lst.append(s.key)
            else:
                lst.append(s.left.inOrderTraversal())
        lst.append(s.key)
        if s.right:
            if s.right.isLeaf():
                lst.append(s.right.key)
            else:
                lst.append(s.right.inOrderTraversal())
        return lst
    def getFatherofMax(s):
        if s.right:
            if s.right.isLeaf():
                return s
            else:
                return s.right.getFatherofMax()
        return None
    def getMaxNode(s):
        n = s.getFatherofMax()
        if n:
            return n.right
        return None        
    def getFather(s,v):
        if v <= s.key:
            if s.left:
                if s.left.key == v:
                    return s
                else: 
                    return s.left.getFather(v)
        else: 
            if s.right:
                if s.right.key == v:
                    return s
                else:
                    return s.right.getFather(v)
        return None
    #def remove(s,v):
        

def lstToBST(lst):
    node = BST(lst[0])
    for i in range(1,len(lst)-1):
        node.insert(lst[i])
    return node
from random import randint
lst = [randint(0,10) for i in range(10)]
print(lst)
n= lstToBST(lst)
#n.printAll()
print(n.inOrderTraversal())
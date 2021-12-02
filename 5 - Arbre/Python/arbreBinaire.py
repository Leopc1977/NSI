class Node: 
    def __init__(s, value=None, left=None, right=None):
        s.key = value
        s.left = left
        s.right = right
    def __str__(s):
        return str(s.key)
    def print(s):
        if not s.left and not s.right:
            print(f"Node: {s.key} is a leaf;")
            return
        res = f"Node: {s.key};\n"
        if s.left and type(s.left)==Node:
            res = res+ f"Left child: {s.left.key};\n"
        if s.right and type(s.right)==Node:
            res = res + f"Right child: {s.right.key};"
        print(res)
    def getSize(s,node,size):
        if not node.left and not node.right: #is a leaf
            return size
        sizeLeft,sizeRight = 0,0
        if node.left:
            sizeLeft = s.getSize(node.left,size)
        if node.right:
            sizeRight = s.getSize(node.right,size)
        return size+sizeLeft+sizeRight

a = Node(3)
b = Node(2,a)
c = Node(0)
d = Node(1,c,b)
print(d.getSize(d,1))

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
            return 1
        sizeLeft,sizeRight = 0,0
        if node.left:
            sizeLeft = s.getSize(node.left,size)
        if node.right:
            sizeRight = s.getSize(node.right,size)
        return size+sizeLeft+sizeRight
    def getTree(s,node,lstTree): #to finish
        if not node.left and not node.right: #is a leaf
            return node.key

        currentBranch = [node.key]
        branchsToAppend = [] 

        if node.left:
            treeLeft = s.getTree(node.left,lstTree)
            branchsToAppend.append(treeLeft)
        if node.right:
            treeRight = s.getTree(node.right, lstTree)
            branchsToAppend.append(treeRight)
        else: 
            branchsToAppend.append(None)
        currentBranch.append(branchsToAppend)

        if s !=node:
            lstTree.append(currentBranch)
            
        return lstTree
    def isLeaf(s):
        return not s.left and not s.right
    def isInTree(s,keySearched):
        print(s.key)

        if s.key == keySearched:
            return True
        if s.isLeaf():
            return False
    
        left,right=False,False
        if s.left:
            left = s.left.isInTree(keySearched)
        if s.right:
            right = s.right.isInTree(keySearched)
        if left==True or right==True:   
            return True
    def getLeaves(s,lstLeaves):
        if s.isLeaf():
            return lstLeaves.append(s.key)
        else:
            left,right=[],[]
            if s.left:
                left = s.left.getLeaves(lstLeaves)
            if s.right:
                right = s.right.getLeaves(lstLeaves)
            if type(left)==list:
                if len(left)>0:
                    lstLeaves.append(left)
            if type(right)==list:
                if len(right)>0:
                    lstLeaves.append(right)
        return lstLeaves        
def createBT(lstOfKeys):
    lstNode = [Node() for i in range(len(lstOfKeys)//2)]
    for k in range(len(lstOfKeys)):
        try:
            lstNode[k].key = lstOfKeys[k]
            if lstOfKeys[2*k+1]:
                lstNode[k].left = Node(lstOfKeys[k*2+1])
            if lstOfKeys[2*k+2]:
                lstNode[k].right = Node(lstOfKeys[k*2+2])
        except:
            pass
    node = lstNode[0]
    for n in lstNode :
        n.print()
    return node

a = Node(4,Node(5),Node(6))
b = Node(3,Node(8))
e = Node(2,a,b)
f = Node (1,e)

tree = f.getTree(f,[f.key])
leaves = f.getLeaves([])

lst = [0,1,2,3,4,5,6]
node = createBT(lst)
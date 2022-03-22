class Cell:
    def __init__(s,pHead=None,pNext=None):
        s.head = pHead 
        s.next = pNext

class Liste:
    def __init__(s,pCell):
        s.cell = pCell

    def pprint(s):
        if s.cell.head == None:
            print(" ")
        else:
            print(s.cell.head)
            if s.cell.next != None:
                s.getTail().pprint()
        
    def get_head(s):
        return s.cell.head
    def getTail(s):
        return Liste(Cell(s.cell.next.head, s.cell.next.next))

    def ajouter_en_tete(s,pHead):
        s.cell = Cell(pHead,s.cell)

    def est_vide(s):
        return s.cell.head==None and s.cell.next==None

    def getLast(s):
        if s.cell.next==None:
            return s.cell
        else:
            return s.getnext().getLast()

    def length(s):
        if s.cell.next==None:
            return 1
        return 1+s.getnext().count()

    def supprimer_en_tete(s):
        s.cell = Cell(s.cell.next.head,s.cell.next.next)

    def cons(s,pCell):
        return Liste(Cell(pCell,s.cell))

    def find(s,v):
        if s.cell.head ==v:
            return 0
        if s.cell.next==None:
            return -1
        n = s.getnext().find(v)
        if n != -1: 
            return 1+n

    def insert(s,value,index,n=0):
        if n==index:
            return Cell(value, s.cell)    
        if s.cell.next!=None:
            next = s.getTail()
            s.cell.next = next.insert(value,index,n+1)
            return Cell(s.cell.head,s.cell.next)

    def insertIter(s,val,index):
        cel1 = s.cell
        for _ in range(index-1):
            cel1 = cel1.next
        cel2 = Cell(val,cel1.next)
        cel1.next = cel2

    def concat(s,list2):
        if s.cell.next == None:
            return Cell(list2.cell.head,list2.cell.next)
        next = s.getTail()
        s.cell.next = next.concat(list2)
        return Cell(s.cell.head, s.cell.next)

cell_vide = Cell()
cell1 = Cell(1,None)
cell2 = Cell(2,cell1)
cell3 = Cell(3,cell2)
cell4 = Cell(4,None)
cell5 = Cell(5,cell4)
cell6 = Cell(6,cell5)
print("=============================")

lst = Liste(cell3)
lst2 = Liste(cell6)
"""
lst.insert(99,1,0 x) #3|99|2|1|
print("====")
lst.insert(100,2,0) #3|99|100|2|1|
print("=========")
lst.pprint()
"""
lst.concat(lst2)
lst.pprint()
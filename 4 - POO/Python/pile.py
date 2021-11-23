class Stack():
    def __init__(s):
        s.items = []
    def push(s,item):  s.items.append(item)
    def pop(s):        return s.items.pop(-1)
    def isEmpty(s):    return s.items == []
    def getPeek(s):    return s.items[-1]
    def getSize(s):    return len(s.items)
    def print(s):      print(s.items)
    def getMax(s):
        save = Stack()
        max = s.pop()
        save.push(max)
        indiceMax = 1
        cnt = 1

        while not s.isEmpty():
            peek = s.pop()
            cnt=cnt+1
            if peek>max:
                max = peek
                indiceMax = cnt
            save.push(peek)

        while not save.isEmpty():
            s.push(save.pop())
        return indiceMax
    def reverse(s,end):
        pileReverse = Stack()
        pileOrder = Stack()
        for i in range(end):
            pileReverse.push(s.pop())
        for i in range(end):
            pileOrder.push(pileReverse.pop()) 
        for i in range(end):
            s.push(pileOrder.pop()) 

    def getMax2(s,end):
        save = Stack()
        max = s.pop()
        save.push(max)
        indiceMax = 1
        cnt = 1
        while cnt < end:
            peek = s.pop()
            cnt=cnt+1
            if peek>max:
                max = peek
                indiceMax = cnt
            save.push(peek)
        while not save.isEmpty():
            s.push(save.pop())
        return indiceMax

    def pancakesMiamNon(s,len):
        if len<=2:
            return s.items
        iMax = s.getMax2(len)
        s.reverse(iMax)
        s.reverse(len)
        return s.pancakesMiamNon(len-1)

p = Stack()

p.push(5)
p.push(9)
p.push(3)
p.push(6)

p.print()
len = p.getSize()
p.pancakesMiamNon(len)
p.print()

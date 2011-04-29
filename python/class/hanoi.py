#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:
        def __init__(self):
                self.items = []
        def show(self):
                return self.items
        def isEmpty(self):
                return self.items == []
        def push(self, item):
                return self.items.insert(0, item)
        def pop(self):
                return self.items.pop(0)
        def peek(self):
                return self.items[0]
        def size(self):
                return len(self.items)


def goster(nerden, nereye):
        boy = max(a.size(), b.size(), c.size())
        kule1 = a.show()[:]
        kule2 = b.show()[:]
        kule3 = c.show()[:]
      
        for i in range(boy-a.size()):
                kule1.insert(0, '_') 
        for i in range(boy-b.size()):
                kule2.insert(0, '_') 
        for i in range(boy-c.size()):
                kule3.insert(0, '_') 

        print '%d. adım\n' %k[0]
        for i in range(boy):
                print '\t\t', kule1[i], '\t', kule2[i], '\t', kule3[i]
        print '\t\t_________________\n\n'
        k[0]=k[0]+1
        return k


def hanoi(n, nerden, nereye):
        if n==1:
                sozluk[nereye].push(sozluk[nerden].pop())
                return goster(nerden,nereye)

        takas = 6 - nerden - nereye
        hanoi(n-1, nerden, takas)
        sozluk[nereye].push(sozluk[nerden].pop())
        goster(nerden,nereye)
        return hanoi(n-1, takas, nereye)


if __name__ == "__main__":
        a = Stack()
        b = Stack()
        c = Stack()
        disk = 4
        sozluk = { 1:a, 2:b, 3:c }
        for i in range(disk,0,-1):
                a.push(i) 

        k = [0]
        goster(1, 3)
        hanoi(disk, 1, 3)



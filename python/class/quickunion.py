def kok(i):
    while ( i!=id[i] ):
        i=id[i]
    return id[i]

def bul(p,q):
    return kok(p)==kok(q)

def birlestir(p,q):
    i=kok(p)
    j=kok(q)
    id[i]=j


id=[0,1,2,3,4,5,6,7,8,9]
print "   ",id
birlestir(5,6)
print "5-6",id
birlestir(3,4)
print "3-4",id
birlestir(4,9)
print "4-9",id
birlestir(2,9)
print "2-9",id
birlestir(3,5)
print "3-5",id

print "0-2 ?", bul(0,2)
print "3-6 ?", bul(3,6)
print "3-4 ?", bul(3,4)
print "3-8 ?", bul(3,8)

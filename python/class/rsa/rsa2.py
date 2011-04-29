import random

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def ext_gcd(x,y):
    if y == 0:
        return (x,1,0)
    else:
        (d,a,b) = ext_gcd(y, x%y)
        return (d,b,a-(x/y)*b)

def modexp(x,n,p):
    if n == 0:
        return 1
    t = (x*x)%p
    tmp = modexp(t,n/2,p)
    if n%2 != 0:
        tmp = (tmp * x) % p
    return tmp

def RSAgenKeys(p,q):
    n = p * q
    pqminus = (p-1) * (q-1)
    e = int(random.random() * n)
    while gcd(pqminus,e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pqminus,e)
    if b < 0:
        d = pqminus+b
    else:
        d = b
    return ((e,d,n))

(Ae,Ad,n) = RSAgenKeys(p=5563, q=8191)
(Be,Bd,n) = RSAgenKeys(p=5563, q=8191)

m = ord('A')

#M MESAJINI GONDEREN A, ALAN B
a1 = modexp(modexp(m,  Ad, n),  Be, n) #A gonderdi: A private ve B public ile kilitlendi
b1 = modexp(modexp(a1, Bd, n), Ae, n) #B acti: B private ve A public ile kilit acildi
print chr(b1)


#Pb3
#a

def cifra_control(n):
    lista=[int(x) for x in str(n)]
    if sum(lista)>=10:
        return cifra_control(sum(lista))
    else:
        return sum(lista)

#b 

def insereaza_cifra_control(lista):
    lista=lista.split()
    l=[]
    for i in range(len(lista)):
        l+=[lista[i]]
        l+=[cifra_control(lista[i])]
    lista=l 
    return lista

#c

def egale(*L):
    ok=True
    for i in range(len(L)-1):
        if L[i]!=L[i+1]:
            ok=False
    return ok

#d

f=open("cinema.in", "r")
linie=f.read()
linie=insereaza_cifra_control(linie)
i=0
for i in range(len(linie)):
    print(linie[i], end=" ")
    if i%2==1:
        print()

#e

f=open("cinema.in" , "r")
g=open("text.out" , "r")

linie=f.read().split()
linie=[int(x) for x in linie]
linie=sorted(linie)
linie=[str(x) for x in linie]
t=""
for e in linie:
    if e not in t:
        t+=e
        t+=" "
linie=insereaza_cifra_control(t)
linie=[linie[i] for i in range(len(linie)) if i%2==1]


linie2=g.read().split()
linie2=[int(x) for x in linie2]
linie2=sorted(linie2)
linie2=[str(x) for x in linie2]
t=""
for e in linie2:
    if e not in t:
        t+=e
        t+=" "
linie2=insereaza_cifra_control(t)
linie2=[linie2[i] for i in range(len(linie2)) if i%2==1]
if egale(linie, linie2)==True:
    print("da")
else:
    print("nu")

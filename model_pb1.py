#Pb1

#a
from pickle import NONE


def min_max(lista):
    return min(lista), max(lista)

L=[-1, -2, 3, 5]
x,y=min_max(L)


#b
def incarca_fisier(fisier):
    lista=[]
    f=open(fisier, "r")
    for linie in f:
        ok=0
        L=[]
        for ch in linie.split():
            if ok==0:
                if ch=="-":
                    ok=1
                    continue
                else:
                    L.append(int(ch))
            else:
                L+=int(ch)*(-1)
                ok=0
        lista+=[L]
    return lista



#c

g=open("text.out", "w")
lis=incarca_fisier("cinema.in")
ok=0
count=-1
mini=[]
maxi=[]
for vec in lis:
    x,y=min_max(vec)
    count+=1
    if x==y:
        ok=1
        g.write(str(count))
        g.write("\n")
    mini+=[x]
    maxi+=[y]
if ok==0:
    g.write("nu exista")

g.write(str(min(mini)))
g.write("\n")
g.write(str(max(maxi)))
g.write("\n")

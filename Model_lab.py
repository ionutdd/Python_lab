#pb1

#a

def citire_numere(k):
    f = open(k,"r")
    subliste=[]
    for linie in f.readlines():
        linie = [int(nr) for nr in linie.split()]
        subliste.append(linie)
    return subliste


#b

def prelucrare_lista(subliste):
    for poz in range(len(subliste)):
        count_min=subliste[poz].count(min(subliste[poz]))
        for z in range(count_min):
            subliste[poz].remove(min(subliste[poz]))
            
    m = min([len(subliste[poz]) for poz in range(len(subliste))])
    for poz in range(len(subliste)):
        for x in range(m+1, len(subliste[poz])+1):
            subliste[poz].pop(len(subliste[poz])-1)





#c

f="text.in"
K=citire_numere(f)
print(K)
prelucrare_lista(K)
for linie in K:
    print(*linie)

#d

count=0
f="text.in"
S=citire_numere(f)
k = int(input("k= "))
g = open("text.out" , "w")
for linie in S:
    for i in range(len(linie)):
        if int(linie[i])<10**(k) and int(linie[i])>=10**(k-1):
            linie[i]+= " "
            g.write(linie[i])
            count+=1
if count==0:
    g.write("imposibil")    

#pb 2
#a

f = open("cinema.in", "r")      
d={} 
for linie in f.readlines():
    cinema=""
    cha=""
    nume=""
    i=0
    while cha!="%":
        cha=linie[i+1]
        cinema+=linie[i]
        i+=1
    cinema=cinema.strip(" ")
    cha=""
    chaa=""
    i+=1
    while cha!="%":
        cha=linie[i+1]
        nume+=linie[i]
        i+=1
 
    nume=nume.strip(" ")
    cha=""
    chaa=""
    L=[]
    LL=[]
    i+=2
    cha=linie[i]
    chaa=linie[i]
    while cha!="\n":
        while chaa!=" ":
            if chaa!="\n":
                L+=chaa
            i+=1
            try:
                chaa=linie[i]
            except:
                break
        LL+=[L]
        L=[]
        i+=1
        try:
            cha=linie[i]
            chaa=linie[i]
        except:
            break
        
    dd={nume : LL}
    d.update({cinema : dd})

#b

def sterge_ore(d, cinema, film, ore):
    i=-1
    for lista in d[cinema][film]:
        i+=1
        for ora in ore:
            ok=1
            j=-1
            for ch in lista:
                j+=1
                if ch!=ora[j]:
                    ok=0
            if ok==1:
                d[cinema][film]=d[cinema][film][:i]+d[cinema][film][i+1:]


film = input("film= ")
c = input("cinematograf= ")
orre = input("ore= ")
poz=0
ore=[]
ora=[]
k=-1
for i in orre:
    k+=1
    if i!=" ":
        ora+=i
    else:
        ore+=[ora]
        ora=[]
        poz+=1
        k=-1

ore+=[ora]
sterge_ore(d,c,film,ore)
print(d)

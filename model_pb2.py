#Pb2

#a

def deviruseaza(sir):
    L=sir.split()
    t=""
    k=""
    if len(L)!=1:
        for i in range(len(L)):
            t+=L[i][len(L[i])-1]
            for j in range(1,len(L[i])-1):
                t+=L[i][j]
            t+=L[i][0]
            t+=" "
    return t

sir="aorectc aropozitip este aceasta"
print(deviruseaza(sir))

#b

def prime(n, numar_maxim):
    if numar_maxim==0:
        i=2
        L=[]
        for i in range(n):
            count=0
            for d in range(1,i+1):
                if i%d==0:
                    count+=1
            if count==2:
                L+=[i]
    else:
        i=2
        L=[]
        for i in range(n):
            count=0
            for d in range(1,i+1):
                if i%d==0:
                    count+=1
            if count==2:
                L+=[i]
                numar_maxim-=1
            if numar_maxim==0:
                break
    return L

n=int(input("n="))
numar_maxim=int(input("numar_maxim="))
L=prime(n,numar_maxim)
print(L)

#c

f=open("cinema.in" , "r")
g=open("text.out" , "w")
count=0
s=f.readlines()
for linie in s:
    count+=1
i=0
Lista=prime(count+1, 0)
for linie in s:
    i+=1
    sir=""
    if i in Lista:
        sir=deviruseaza(linie)
        g.write(sir)
        g.write("\n")
    else:
        g.write(linie)

f.close()
g.close()

f = open('p022_names.txt', 'r')
def tri(text):
    fichier=f.read()
    files=fichier.split(",")
    files=sorted(files)
    return files
#print(tri(f))

def poids(l):
    Sumlist=[] #on calcule le poids de chaque nom en fonction de ses lettres
    for i in range(len(l)):
        Sumname=0
        for j in l[i]:
            if j=='"':
                Sumname+=0
            else:
                Sumname+=(ord(j)-64)
        Sumlist.append(Sumname)      
    return Sumlist



L=poids(tri(f))[:]
print(L)
A=[0,4,5,6,9,7]
def place(l):
    Sortie=[]
    for k in range(len(l)):
        tnp=(k+1)*l[k]
        Sortie=Sortie +[tnp]
    return Sortie

L1=place(L)[:]

print(place(L)[937])
def SommeList(l):
    S=0 #on calcule la somme totale de la liste
    for i in range(len(l)):
        S+=l[i]
    return S
print(SommeList(L1))

def solve(n):
    Sortie=place(poids(tri(n)))
    Sumtot=SommeList(place(poids(tri(n))))
    return Sumtot
print(solve(f))
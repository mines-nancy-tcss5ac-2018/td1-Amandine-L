def reversenb(n):
    transfert=str(n)
    #on transforme le nombre en liste de chaine de caractère puis on retourne la liste avant de reformer le nombre retourner
    transfert2=list(transfert)
    passage=''
    sortie=0
    list.reverse(transfert2)
    
    for k in range(len(transfert2)):
        passage+=transfert2[k]
    sortie=int(passage)
    return sortie


def palindrome(n):
    if reversenb(n)==n:
        return True
    else:
        return False

def lychrel(n):
    transfert=0
    passage=n
    for i in range(51):
        transfert= passage + reversenb(passage)
        passage=transfert
        if palindrome(transfert):
            return False
    if not(palindrome(transfert)):
        return True

def solve(n):
    Somme=0
    for k in range(n+1):
        if lychrel(k)==True:
            Somme+=1
    return Somme

assert solve(200)==1
print(solve(10000))
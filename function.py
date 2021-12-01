def ReadAnimalsInChaine():
    with open("chaine.txt", "r") as chaine:
        ListMatrixChaine = chaine.read().split("\n")
        ListAnimals = ListMatrixChaine[1].split(" ")
    D1, D2 = {}, {}
    for i, Name in enumerate(ListAnimals):
        D1[str(Name)] = i
        D2[i] = str(Name)
    return D1, D2

def MatChain(filename:str="chaine.txt")->list[list[int]]:
    with open("chaine.txt","r") as c :
        lines=c.read().split("\n")
        MatC=[]
        n = int(lines[0])
        for i in range(2,len(lines)) :
            line=lines[i].split(" ")
            MatC.append(line)
        return MatC

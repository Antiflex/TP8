def ReadAnimalsInChaine():
    with open("chaine.txt", "r") as chaine:
        ListMatrixChaine = chaine.read().split("\n")
        ListAnimals = ListMatrixChaine[1].split(" ")
    D1, D2 = {}, {}
    for i, Name in enumerate(ListAnimals):
        D1[str(Name)] = i
        D2[i] = str(Name)
    return D1, D2

def MatChain(filename:str="chaine.txt", MatC:list[list]=[])->list[list[int]]:
    with open("chaine.txt","r") as c :
        lines=c.read().split("\n")
        MatC=[]
        for i in range(2,len(lines)) :
            line=lines[i].split(" ")
            for j in range(len(line)):
                line[j]=int(line[j])
            MatC.append(line)
        return MatC

def PredaListProie(dico:dict=ReadAnimalsInChaine()[1],Mat:list[list]=MatChain())->dict:
    dictPredaProie:dict[list]={}
    for i,relList in enumerate(Mat):
        dictPredaProie[dico[i]]=[]
        for j,arg in enumerate(relList):
            if arg==1 :
                dictPredaProie[dico[i]].append(dico[j])
    return dictPredaProie

def ListPrédateursProies (Names:dict=ReadAnimalsInChaine()[1], List:list[list]=MatChain())->dict:
    DictPredateursProies = {}
    for i in range (len(List)):
        DictPredateursProies[Names[i]] = []
        for j in range(len(List[i])):
            if List[i][j] == -1:
                DictPredateursProies[Names[i]].append(Names[j])
    return DictPredateursProies

def premiereProie (element:str=ReadAnimalsInChaine()[1][0]):
    dico= ReadAnimalsInChaine()[0]
    if element in dico.keys():
        if PredaListProie()[element]!=[]:
            return PredaListProie()[element][0]
        else:
            return -1

def PathFromPredator(Mat:list[list]=MatChain(),dico0:dict=ReadAnimalsInChaine()[0],elem:str=ReadAnimalsInChaine()[1][0]\
                     ,sep:str="-->")->list :
    dico1=ReadAnimalsInChaine()[1]
    Path=[elem]
    activeAnimal=elem
    while premiereProie(element=activeAnimal)!=-1:
        Path.append(premiereProie(activeAnimal))
        activeAnimal=premiereProie(activeAnimal)
    print(sep.join(Path))
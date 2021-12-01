def MatChain(filename:str="chaine.txt")->list[list[int]]:
    with open("chaine.txt","r") as c :
        lines=c.read().split("\n")
        MatC=[]
        n = int(lines[0])
        for i in range(2,len(lines)) :
            line=lines[i].split(" ")
            MatC.append(line)
        return MatC

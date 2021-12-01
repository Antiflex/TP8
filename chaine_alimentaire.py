
def addPredator(chaine: dict[str, list[str]]) -> bool:
    with open("chaine.txt", 'r') as file:
        content = file.read().split("\n")
    content[1] += " ".join([ani for ani in chaine.keys()])
    content[0] = str(len(content[1].split(" ")))

    pass  # matrice
    with open("chaine.txt", 'w') as file:
        return True


def deleteChElement(animal: str) -> bool:
    with open("chaine.txt", 'r') as file:
        content = file.read().split("\n")
        ani_index = content[1].split(" ").index(animal)

    pass  # matrice
    with open("chaine.txt", 'w') as filewrite:
        pass

    return True


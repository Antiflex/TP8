
def addPredator(chaine: dict[str, list[str]]) -> bool:
    with open("chaine.txt", 'r') as file:
        content = file.read().split("\n")
    content[1] += " ".join([ani for ani in chaine.keys()])
    content[0] = str(len(content[1].split(" ")))

    animal_list = [animal for animal in content[1].split(" ")]
    newlines = [[0 for __ in range(int(content[0]))]
                for pred in chaine.values()]
    for i, predator in enumerate(chaine.keys()):
        for ani_index, animal in enumerate(animal_list):
            if animal in chaine[predator]:
                newlines[i][ani_index] = 1
    newcolumns = [[] newlines]


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


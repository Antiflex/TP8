from function import MatChain


def addPredator(chaine: dict[str, list[str]]) -> bool:
    init_matrice = [[str(el) for el in line] for line in MatChain()]
    with open("chaine.txt", 'r') as file:
        content = file.read().split("\n")
    content[1] += " ".join([ani for ani in chaine.keys()])
    content[0] = str(len(content[1].split(" ")))

    animal_list = [animal for animal in content[1].split(" ")]
    init_matrice += [[0 for __ in range(int(content[0]))]
                     for pred in chaine.values()]

    for ani_index, animal in enumerate(animal_list):
        for i, predator in enumerate(chaine.keys()):
            if animal in chaine[predator]:
                init_matrice[ani_index].append('1')

    with open("chaine.txt", 'w') as file:
        file.write("\n".join(content[0:1] +
                             ([" ".join(line) for line in init_matrice])))


def deleteChElement(animal: str) -> bool:
    with open("chaine.txt", 'r') as file:
        content = file.read().split("\n")
        ani_index = content[1].split(" ").index(animal)

    pass  # matrice
    with open("chaine.txt", 'w') as filewrite:
        pass

    return True

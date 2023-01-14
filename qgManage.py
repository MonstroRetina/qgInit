import os
import platform

def insertCreature():
    creatureName = input("\n Insira o nome: ")
    while(True):
        try:
            creatureMod = int(input("\n Insira o modificador de iniciativa: "))
        except ValueError:
            print("\n====")
            print(" O modificador deve ser um número inteiro!")
            print("====")
            continue
        else:
            break
    newCreature = [creatureName, creatureMod]
    return newCreature

def listCreatures(creatureList):
    if len(creatureList) == 0:
        print("\n A lista está vazia! \n")
    for creature in creatureList:
        print('%s : %i' %(creature[0],creature[1]))

def clear():
    if platform.system() == "Windows":
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')
    clear()

import os
import platform

def insertCreature():
    creature_name = input("\n Insira o nome: ")
    while(True):
        try:
            creature_mod = int(input("\n Insira o modificador de iniciativa: "))
        except ValueError:
            print("\n====")
            print(" O modificador deve ser um número inteiro!")
            print("====")
            continue
        else:
            break
    new_creature = [creature_name, creature_mod]
    return new_creature

def list_creatures(creature_list):
    if len(creature_list) == 0:
        print("\n A lista está vazia! \n")
    for creature in creature_list:
        print('%s : %i' %(creature[0],creature[1]))

def clear():
    if platform.system() == "Windows":
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')
    clear()

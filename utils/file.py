import os
import glob
import utils.manage as manage
import utils.constants as constants

def save(default_creatures):
    manage.clear()
    file_name = input("\n Insira o nome do arquivo: ") + ".txt"
    save_list = []

    for c in default_creatures:
        for i in c:
            save_list.append(str(i) + "\n")

    file_path = constants.FILEPATH + file_name
    save_file = open(file_path,"w+")
    save_file.writelines(save_list)

    save_file.close()
    manage.clear()
    print("\n Grupo salvo com sucesso no arquivo %s!\n" %(file_name))
    input("Pressione Enter para continuar")

def load():
    manage.clear()
    os.chdir(constants.FILEPATH)
    my_files = glob.glob('*.txt')
    print('\n Arquivos salvos: \n')

    for i in my_files:
        tempTuple = os.path.splitext(i)
        print('%s' % (tempTuple[0]))
    file_name = input("\n Insira o arquivo a ser carregado: ")
    file_path = constants.FILEPATH + file_name + '.txt'
    loaded_file = open(file_path,"r")
    loaded_characters = []

    while loaded_file:
        loaded_character = []
        line = loaded_file.readline().rstrip()
        if line == "":
            break
        loaded_character.append(line)
        line = loaded_file.readline().rstrip()
        loaded_character.append(int(line))
        

        loaded_characters.append(loaded_character)
        
    loaded_file.close()
    manage.clear()
    print("\n Grupo carregado com sucesso!\n")
    input("Pressione Enter para continuar")

    return loaded_characters

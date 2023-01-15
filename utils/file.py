import os
import glob
import utils.manage as manage
import utils.constants as constants

def save(defaultCreatures):
    manage.clear()
    file_name = input("\n Insira o nome do arquivo: ")
    saveList = []

    for c in defaultCreatures:
        for i in c:
            saveList.append(str(i) + "\n")

    file_path = constants.FILEPATH + file_name +".txt"
    save_file = open(constants.FILEPATH,"w+")
    save_file.writelines(saveList)

    save_file.close()
    manage.clear()
    print("\n Grupo salvo com sucesso no arquivo %s!\n" %(file_name))
    input("Pressione Enter para continuar")

def load():
    manage.clear()
    constants.FILEPATH = os.path.expanduser('~/QGinit/Save files')
    os.chdir(constants.FILEPATH)
    my_files = glob.glob('*.txt')
    print('\n Arquivos salvos: \n')

    for i in my_files:
        tempTuple = os.path.splitext(i)
        print('%s' % (tempTuple[0]))
    file_name = input("\n Insira o arquivo a ser carregado: ")
    constants.FILEPATH = constants.FILEPATH + '\\' + file_name + '.txt'
    loadedFile = open(constants.FILEPATH,"r")
    loadedCharacters = []

    while loadedFile:
        loadedCharacter = []
        line = loadedFile.readline().rstrip()
        if line == "":
            break
        loadedCharacter.append(line)
        line = loadedFile.readline().rstrip()
        loadedCharacter.append(int(line))
        

        loadedCharacters.append(loadedCharacter)
        
    loadedFile.close()
    manage.clear()
    print("\n Grupo carregado com sucesso!\n")
    input("Pressione Enter para continuar")

    return loadedCharacters
    
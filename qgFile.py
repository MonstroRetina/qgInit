import os
import glob
import qgManage


def save(defaultCreatures):
    qgManage.clear()
    fileName = input("\n Insira o nome do arquivo: ")
    saveList = []

    for c in defaultCreatures:
        for i in c:
            saveList.append(str(i) + "\n")

    filePath = os.path.expanduser('~/QGinit/Save files/%s.txt ' % (fileName))
    saveFile = open(filePath,"w+")
    saveFile.writelines(saveList)

    saveFile.close()
    qgManage.clear()
    print("\n Grupo salvo com sucesso no arquivo %s!\n" %(fileName))
    input("Pressione Enter para continuar")

def load():
    qgManage.clear()
    filePath = os.path.expanduser('~\\QGinit\\Save files')
    os.chdir(filePath)
    my_files = glob.glob('*.txt')
    print('\n Arquivos salvos: \n')

    for i in my_files:
        tempTuple = os.path.splitext(i)
        print('%s' % (tempTuple[0]))
    fileName = input("\n Insira o arquivo a ser carregado: ")
    filePath = filePath + '\\' + fileName + '.txt'
    loadedFile = open(filePath,"r")
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
    qgManage.clear()
    print("\n Grupo carregado com sucesso!\n")
    input("Pressione Enter para continuar")

    return loadedCharacters
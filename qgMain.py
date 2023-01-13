import qgManage
import qgOptions
    
print ('''
 ________    ________  .__       .__  __   
 \_____  \  /  _____/  |__| ____ |__|/  |_ 
  /  / \  \/   \  ___  |  |/    \|  \   __\\
 /   \_/.  \    \_\  \ |  |   |  \  ||  |  
 \_____\ \_/\______  / |__|___|  /__||__|  
        \__>       \/          \/          
 ''')

input("\n Pressione enter para começar\n")

defaultCreatures = []
defaultGroup = []
initCreatures = [defaultCreatures,defaultGroup]

while(True):
    qgManage.clear()
    print(" ======================================")
    if(len(initCreatures[1]) == 0):
        print("\n Personagens jogadores não inseridos!\n")

    print(" OPÇÕES: ")
    print("\n a - Inserir criatura \n b - Rolar iniciativa \n c - Remover criatura \n d - Mostrar encontro \n e - Inserir jogador \n f - Limpar encontro")
    print(" save - salvar grupo de jogadores\n load - carregar grupo de jogadores")
    print("\n sair - fechar o programa")
    option = input("\n Insira a opção: ").strip().lower()

    initCreatures = qgOptions.callOption(option,initCreatures)
    continue
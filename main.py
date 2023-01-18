import utils.manage as manage
import utils.options as options

print ('''
 ________    ________  .__       .__  __   
 \_____  \  /  _____/  |__| ____ |__|/  |_ 
  /  / \  \/   \  ___  |  |/    \|  \   __\\
 /   \_/.  \    \_\  \ |  |   |  \  ||  |  
 \_____\ \_/\______  / |__|___|  /__||__|  
        \__>       \/          \/          
                                Ver. 1.1
 ''')

input("\n Pressione enter para começar\n")

default_creatures = []
default_group = []
init_creatures = [default_creatures,default_group]

while(True):
    manage.clear()
    print(" ======================================")
    if(len(init_creatures[1]) == 0):
        print("\n Personagens jogadores não inseridos!\n")
        print(" ======================================\n")
    if(len(init_creatures[0]) == 0):
        print(" Não há criaturas no Econtro!\n")
        print(" ======================================\n")

    print(" OPÇÕES: ")
    print("\n a - Inserir criatura \n b - Rolar iniciativa \n c - Remover criatura \n d - Mostrar encontro \n e - Inserir jogador \n f - Limpar encontro")
    print(" save - salvar grupo de jogadores\n load - carregar grupo de jogadores")
    print("\n sair - fechar o programa")
    option = input("\n Insira a opção: ").strip().lower()

    init_creatures = options.call_option(option,init_creatures)
    continue

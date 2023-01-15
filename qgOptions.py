import qgManage
import random
import qgFile

def callOption(option,initCreatures):
    
    #inserir criatura
    if option == "a":
        initCreatures[0].append(qgManage.insertCreature())
    
    #rolar iniciativa
    if option == "b":
        initMode = input("\n Iniciativa estática? (Padrão: dinâmica) S/N: ").strip().lower()

        while(True):
            initiatives = []
            
            qgManage.clear()

            for creature in initCreatures[0]:
                roll = random.randint(1,20)
                initiatives.append({'name': creature[0], 'mod': creature[1], 'roll': roll })
            
            def get_roll(e):
                return e['roll'] + e['mod']

            initiatives.sort(reverse=True, key=get_roll)

            if len(initMode) != 0 and initMode[0] == "s":
                qgManage.clear()
                for element in initiatives:
                    print('\n' + element['name'] + ' : %i (%i)' % (element['roll']+element['mod'], element['roll']))
                input("\n Pressione enter para prosseguir...\n")
                break

            for element in initiatives:
                qgManage.clear()
                print('\n' + element['name'] + ' : %i (%i)' % (element['roll']+element['mod'], element['roll']))
                input("\n Pressione enter para o próximo turno...\n")
            
            qgManage.clear()
            encounter = input("\n Fim da rodada. Encerrar repetição? S/N: ").strip().lower()
            if len(encounter) != 0 and encounter[0] == "s":
                break
        return initCreatures

    #remover criatura
    if option == "c":
        creatureRemove = input("\n Insira o nome da criatura a ser removida: ")
        for creature in initCreatures[0]: 
            if creature[0] == creatureRemove:
                initCreatures[0].remove(creature)
        return initCreatures
    
    #exibir encontro
    if option == "d":
        qgManage.clear()
        print(" Criaturas no encontro atual: ")
        qgManage.listCreatures(initCreatures[0])
        input("\n Pressione enter para continuar...")
        return initCreatures

    #exibir jogadores
    if option == "d2":
        print("\n")
        qgManage.clear()
        qgManage.listCreatures(initCreatures[1])
        input("\n Pressione enter para continuar...")
        return initCreatures

    #inserir jogador
    if option == "e":
        jogadorInserido = qgManage.insertCreature()
        initCreatures[0].append(jogadorInserido)
        initCreatures[1].append(jogadorInserido)
        return initCreatures

    #reiniciar encontro
    if option == "f":
        initCreatures[0] = initCreatures[1]
        return initCreatures

    if option == "sair":
        exit()

    if option == "save":
        qgFile.save(initCreatures[1])
        return initCreatures

    if option == "load":
        loadedCreatures = qgFile.load()
        for creature in loadedCreatures:
            if creature not in initCreatures[0]:
                initCreatures[0].append(creature)
            initCreatures[1] = loadedCreatures
        return initCreatures

    print("\n ====")
    print("\n Opção inválida.\n")
    print(" ====")

    return initCreatures

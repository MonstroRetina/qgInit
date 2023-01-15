import random
import utils.manage as manage
import utils.file as file

def callOption(option,initCreatures):
    
    #inserir criatura
    if option == "a":
        initCreatures[0].append(manage.insertCreature())
    
    #rolar iniciativa
    if option == "b":
        initMode = input("\n Iniciativa estática? (Padrão: dinâmica) S/N: ").strip().lower()

        while(True):
            initiatives = []
            
            manage.clear()

            for creature in initCreatures[0]:
                roll = random.randint(1,20)
                initiatives.append({'name': creature[0], 'mod': creature[1], 'roll': roll })
            
            def get_roll(e):
                return e['roll'] + e['mod']

            initiatives.sort(reverse=True, key=get_roll)

            if len(initMode) != 0 and initMode[0] == "s":
                manage.clear()
                for element in initiatives:
                    print('\n' + element['name'] + ' : %i (%i)' % (element['roll']+element['mod'], element['roll']))
                input("\n Pressione enter para prosseguir...\n")
                break

            for element in initiatives:
                manage.clear()
                print('\n' + element['name'] + ' : %i (%i)' % (element['roll']+element['mod'], element['roll']))
                input("\n Pressione enter para o próximo turno...\n")
            
            manage.clear()
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
        manage.clear()
        print(" Criaturas no encontro atual: ")
        manage.listCreatures(initCreatures[0])
        input("\n Pressione enter para continuar...")
        return initCreatures

    #exibir jogadores
    if option == "d2":
        print("\n")
        manage.clear()
        manage.listCreatures(initCreatures[1])
        input("\n Pressione enter para continuar...")
        return initCreatures

    #inserir jogador
    if option == "e":
        jogadorInserido = manage.insertCreature()
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
        file.save(initCreatures[1])
        return initCreatures

    if option == "load":
        loadedCreatures = file.load()
        for creature in loadedCreatures:
            if creature not in initCreatures[0]:
                initCreatures[0].append(creature)
            initCreatures[1] = loadedCreatures
        return initCreatures

    print("\n ====")
    print("\n Opção inválida.\n")
    print(" ====")

    return initCreatures

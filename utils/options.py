import random
import utils.manage as manage
import utils.file as file

def call_option(option,init_creatures):
    
    #inserir criatura
    if option == "a":
        init_creatures[0].append(manage.insertCreature())
    
    #rolar iniciativa
    if option == "b":
        manage.clear()
        init_mode = input("\n Iniciativa estática? (Padrão: dinâmica) S/N: ").strip().lower()

        while(True):
            initiatives = []
            
            manage.clear()

            for creature in init_creatures[0]:
                roll = random.randint(1,20)
                initiatives.append({'name': creature[0], 'mod': creature[1], 'roll': roll })
            
            def get_roll(e):
                return e['roll'] + e['mod']

            initiatives.sort(reverse=True, key=get_roll)

            if len(init_mode) != 0 and init_mode[0] == "s":
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
        return init_creatures

    #remover criatura
    if option == "c":
        creature_remove = input("\n Insira o nome da criatura a ser removida: ")
        for creature in init_creatures[0]: 
            if creature[0] == creature_remove:
                init_creatures[0].remove(creature)
        return init_creatures
    
    #exibir encontro
    if option == "d":
        manage.clear()
        print(" Criaturas no encontro atual: ")
        manage.list_creatures(init_creatures[0])
        input("\n Pressione enter para continuar...")
        return init_creatures

    #exibir jogadores
    if option == "d2":
        print("\n")
        manage.clear()
        manage.list_creatures(init_creatures[1])
        input("\n Pressione enter para continuar...")
        return init_creatures

    #inserir jogador
    if option == "e":
        jogador_inserido = manage.insertCreature()
        init_creatures[0].append(jogador_inserido)
        init_creatures[1].append(jogador_inserido)
        return init_creatures

    #reiniciar encontro
    if option == "f":
        init_creatures[0] = init_creatures[1]
        return init_creatures

    if option == "sair":
        exit()

    if option == "save":
        file.save(init_creatures[1])
        return init_creatures

    if option == "load":
        loaded_creatures = file.load()
        for creature in loaded_creatures:
            if creature not in init_creatures[0]:
                init_creatures[0].append(creature)
            init_creatures[1] = loaded_creatures
        return init_creatures

    print("\n ====")
    print("\n Opção inválida.\n")
    print(" ====")

    return init_creatures

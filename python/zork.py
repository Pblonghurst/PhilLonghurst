player = {
    'name' : 'Phil',
    'attack' : 20,
    'health' : 100,
    'heal' : 15,
}

enemy = {
    'name' : 'Z',
    'attack' : 10,
    'health' : 200,
}

game_running = True
player_won = False  
player_enemy = False

while game_running == True: 

    player_won = False  
    enemy_won = False

    print('Select action')
    print('1)attack')
    print('2)heal')

    player_choice = input()

    if player_choice == '1':
        enemy['health'] = enemy['health'] - player['attack']
        if enemy['health'] <= 0:
            player_won = True
        else :
            player['health'] = player['health'] - enemy['attack']
            if player['health'] <= 0:
                enemy_won = True
       
        print(player['health'])
        print(enemy['health'])
    
    elif player_choice == '2':
        print('heal player')
    else:
        print('Invalid Input')

    if player_won == True:
        print('VICTORY')
    elif enemy_won == True:
        print('DEFEAT')

    if player_won == True or enemy_won == True:
        game_running = False


import time
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
shotgun = []
def w():
    time.sleep(2)

item_count_p1 = 0
item_count_p2 = 0

saw_active = False
beer_use = 0
health = 0
max_health = 0
dealer_health = 0
turn = 1
cuff_active = False
cuff_active_p2 = False
p1_inventory = [] #list of items you have
p2_inventory = []
item_list = ['Cigarettes', 'Magnifying Glass', 'Beer', 'Saw', 'Phone', 'Inverter', 'Handcuffs', 'Expired Medicine', 'Adrenaline'] #list of all items
dealer_knows_current = False #The Dealer in game uses logic 100% correct
dealer_knows_which = []
dealer_knows_all = False
live_count = 0
blank_count = 0

def dealer_knowledge():
    global dealer_knows_which
    global dealer_knows_current
    global dealer_knows_all
    dealer_index = 0
    reme = 0
    for i in dealer_knows_which:
        dealer_knows_which[dealer_index] -= 1
        dealer_index += 1
    if dealer_knows_which != []:
        if dealer_knows_which[0] == 0:
            dealer_knows_current = True
            del dealer_knows_which[0]
            dealer_not_know = shotgun
            for i in dealer_knows_which:
                del dealer_not_know[i]
            if 'Blank' not in dealer_not_know:
                dealer_knows_all = True
            elif 'Live' not in dealer_not_know:
                dealer_knows_all = True
    elif dealer_knows_which == []:
        dealer_knows_all = False
def get_find():
    global find
    if len(shotgun) == 1:
        find = 0
    else:
        find = random.randint(1, len(shotgun) -1)
    

def get_health():
    global health
    global max_health
    global dealer_health
    health = random.randint(2,6)
    max_health = health
    dealer_health = health

def shotgun_round():
    global live_count
    global blank_count
    round1 = random.randint(1,99)
    if round1 % 2 == 0 :
        blank_count += 1
        return "Blank"
    elif round1 % 2 != 0:
        live_count += 1
        return "Live"
    
def shotgun_cap():
    cap = random.randint(3,8)
    return cap
    

def load_shotgun():
    global shotgun_cap, live_count, blank_count
    global shotgun_round
    global shotgun
    for i in range(shotgun_cap()):
        shotgun.append(shotgun_round())
    
print(load_shotgun())
find = random.randint(1, len(shotgun) - 1) #determines which sitll The phone selects

        
def cigs():
    global item_count_p1
    global health
    global max_health 
    if health < max_health:
        health += 1
        time.sleep(2)
        print(f'\n{health} health.')
    else:
        print("\nAlready full health. You wasted an item")
        
    item_count_p1 -= 1
    p1_inventory.remove('Cigarettes')
    
def cigs_p2():
    global item_count_p2
    global dealer_health
    print('\nThe Dealer decides to smoke a cigarette.')
    dealer_health += 1
    item_count_p2 -= 1
    p2_inventory.remove('Cigarettes')
    print(f'\nDealer now at {dealer_health} health')
    w()
    
def mag():
    global shotgun
    global item_count_p1
    if shotgun[0] == 'Blank':
        time.sleep(2)
        print("\nBlank")
        time.sleep(2)
        
    elif shotgun[0] == 'Live':
        time.sleep(2)
        print('\nLive')
        time.sleep(2)
    
    item_count_p1 -= 1
    p1_inventory.remove('Magnifying Glass')
    
def mag_p2():
    global shotgun
    global item_count_p2
    global dealer_knows_current
    dealer_knows_current = True
    item_count_p2 -= 1
    p2_inventory.remove('Magnifying Glass')
    w()
    
def beer():
    global shotgun 
    global item_count_p1
    global beer_use
    global find
    if shotgun[0] == 'Blank':
        print('\nBlank')
    
    elif shotgun[0] == 'Live':
        print('\nLive')
        
    del shotgun[0]
    item_count_p1 -= 1
    beer_use += 1 #Used only for showing tits exact stat at The end of The game
    p1_inventory.remove('Beer')
    get_find()
    dealer_knowledge
    
def beer_p2():
    global shotgun 
    global item_count_p2
    global find
    print('\nThe Dealer decides to drink its beer')
    w()
    if shotgun[0] == 'Blank':
        print('\nBlank')
    
    elif shotgun[0] == 'Live':
        print('\nLive')
    w()
    del shotgun[0]
    item_count_p2 -= 1
    p2_inventory.remove('Beer')
    get_find()
    dealer_knowledge()
    
def saw():
    global saw_active 
    global item_count_p1
    time.sleep(2)
    if not saw_active:
        item_count_p1 -= 1
        saw_active = True
        
        p1_inventory.remove('Saw')
        print('\nYou sawed off the shotgun. Double damage.')
    else:
        print('\nYou already used a saw. Nothing Happens')
    time.sleep(2)
    
def saw_p2():
    global saw_active 
    global item_count_p2
    if not saw_active:
        item_count_p2 -= 1
        saw_active = True
        p2_inventory.remove('Saw')
        print('\nThe Dealer sawed off the shotgun. Double damage.')
    time.sleep(2)
    
def phone(): 
    global item_count_p1
    global shotgun
    global find
    print(f'\nSitll {find + 1}...')
    time.sleep(2)
    print(f'\n{shotgun[find]}')
    time.sleep(2)
    
    item_count_p1 -= 1
    p1_inventory.remove('Phone')
    
def phone_p2(): 
    global item_count_p2
    global find
    print('\nThe Dealer decides to use its phone.')
    dealer_knows_which.append(find)
    item_count_p2 -= 1
    p2_inventory.remove('Phone')
    w()
    
def inv(): 
    global item_count_p1
    global shotgun
    time.sleep(2)
    if shotgun[0] == 'Blank':
        shotgun[0] = 'Live'
        
    elif shotgun[0] == 'Live':
        shotgun[0] = 'Blank'
    print('\nInverted')
    time.sleep(2)
    
    item_count_p1 -= 1
    p1_inventory.remove('Inverter')
    
def inv_p2(): 
    global item_count_p2
    global p2_inventory
    global shotgun
    
    print('\nThe Dealer decides to use its inverter.')
    time.sleep(2)
    if shotgun[0] == 'Blank':
        shotgun[0] = 'Live'
        
    elif shotgun[0] == 'Live':
        shotgun[0] = 'Blank'
    print('\nInverted')
    time.sleep(2)
    
    item_count_p2 -= 1
    p2_inventory.remove('Inverter')
    
def cuff():
    global cuff_active
    global item_count_p1 
    if not cuff_active:
        cuff_active = True
        item_count_p1 -= 1
        
        p1_inventory.remove('Handcuffs')
        print('\nThe Dealer takes The handcuffs and cuffs itself.')
        time.sleep(2)
    else:
        print('\nThe Dealer already has handcuffs on. Nothing happens')
        time.sleep(2)
        
def cuff_p2():
    global cuff_active_p2
    global item_count_p2 
    cuff_active = True
    item_count_p2 -= 1    
    p1_inventory.remove('Handcuffs')
    print('\nThe Dealer cuffs you to The table.')
    time.sleep(2)
        
def med():
    global health
    global max_health
    global item_count_p1 
    chance = random.randint(1, 99)
    print('\nYou swallow The pill.')
    time.sleep(2)
    if chance % 2 == 0:
        health -= 1
        print('\nUnlucky. Lost 1 health.')
        
    elif chance % 2 != 0:
        if health >= max_health:
            print("\nAlready full health. You wasted an item.")
            health = max_health
            
        elif max_health - 1 == health:
            health += 1
            print("\nGained 1 health.")
            
        else:
            health += 2
            print('\nGained 2 health.')
    time.sleep(2)
    item_count_p1 -= 1
    
    p1_inventory.remove('Expired Medicine')
    
def med_p2():
    global dealer_health
    global max_health
    global item_count_p2 
    chance = random.randint(1, 99)
    print('\nThe Dealer takes expired medicine.')
    time.sleep(2)
    if chance % 2 == 0:
        health -= 1
        print('\nThe Dealer lost 1 health.')
        
    elif chance % 2 != 0:
        if max_health - 1 == dealer_health:
            dealer_health += 1
            print("\nThe Deaker gained 1 health.")
            
        else:
            dealer_health += 2
            print('\nThe Dealer gained 2 health.')
    time.sleep(2)
    item_count_p2 -= 1
    
    p2_inventory.remove('Expired Medicine')

def p1():
    global turn, cuff_active, shotgun, dealer_health, max_health, saw_active, health, letters, p1_inventory, find
    while turn == 1:
        ans = input("\n\nA. Shoot Dealer\nB. Shoot Yourself\nC. Use an item\nD. See Dealer items\nE. See health\n").lower()
        if ans == 'a':
            shot = shotgun.pop(0)
            if shot == 'Live':
                print('\n...')
                time.sleep(2)
                print('\n*Boom*')
                time.sleep(2)
                print('\nDealer lost 1 health.')
                time.sleep(2)
                find = random.randint(1, len(shotgun) -1)
                if saw_active:
                    dealer_health -= 2
                    if dealer_health < 0:
                        dealer_health = 0
                        
                else:
                    dealer_health -= 1
                if cuff_active:
                    turn = 1
                    cuff_active = False
                    
                else:
                    turn = 2
                
            elif shot == 'Blank':
                print('\n...')
                time.sleep(2)
                print("\n*Click*")
                time.sleep(2)
                print('\nDealer unharmed')
                time.sleep(2)
                find = random.randint(1, len(shotgun) -1)
                if cuff_active:
                    cuff_active = False
                    turn = 1
                    
                else:
                    turn = 2
            dealer_knowledge()
            saw_active = False
        elif ans == 'b':
            shot = shotgun.pop(0)
            if shot == 'Live':
                print('\n...')
                time.sleep(2)
                print("\n*Boom*")
                time.sleep(2)
                print('\nYou lose 1 health.')
                time.sleep(2)
                find = random.randint(1, len(shotgun) -1)
                if saw_active:
                    health -= 2
                    if health < 0:
                        health = 0
                else:
                    health -=1
                if cuff_active:
                    turn = 1
                    cuff_active = false
                else:
                    turn = 2
                
            elif shot == 'Blank':
                print('\n...')
                time.sleep(2)
                print('\n*Click*')
                time.sleep(2)
                print('\nYou get an extra turn.')
                time.sleep(2)
                find = random.randint(1, len(shotgun) -1)
            dealer_knowledge()
            saw_active = False
                
        elif ans == 'c':
            item_selection_p1 = True
            if item_count_p1 == 0:
                    print('\nYou have no items')
                    item_selection_p1 = False
                    time.sleep(2)
            else:
                print("\n\nPick your item\n\n")
            while item_selection_p1:
                time.sleep(2)
                letter_index = 0
                for i in p1_inventory:
                    print(f'{letters[letter_index]}. {i}')
                    letter_index += 1
                max_letters = letters[0:letter_index]
                ans2 = input().upper()
                if ans2 not in max_letters:
                    print('\nNot an item choice\n')
                    
                elif ans2 in max_letters:
                    ans2 = max_letters.index(ans2)
                    ans3 = p1_inventory[ans2]
                    
                    if ans3 == 'Cigarettes':
                        cigs()
                        
                    elif ans3 == 'Beer':
                        beer()
                        
                    elif ans3 == 'Phone':
                        phone()
                        
                    elif ans3 == "Handcuffs":
                        cuff()
                        
                    elif ans3 == "Magnifying Glass":
                        mag()
                        
                    elif ans3 == 'Inverter':
                        inv()
                        
                    elif ans3 == 'Saw':
                        saw()
                        
                    elif ans3 == 'Expired Medicine':
                        med()
                item_selection_p1 = False
                
        elif ans == 'd':
            if item_count_p2 != 0:
                print('\nThe Dealer has\n')
                time.sleep(2)
                for i in p2_inventory:
                    print(i)
            else:
                print("\nThe Dealer doesn't have any items.")
            time.sleep(2)
            print()
            
        elif ans == 'e':
            time.sleep(2)
            print(f'\nThe Dealer has {dealer_health} health.')
            time.sleep(2)
            print(f'\nYou have {health} health.')
            time.sleep(2)
            
        elif ans == 'debug':
            print(shotgun)

    
def p2():
    global item_count_p1, health, cuff_active_p2, max_health, dealer_health, shotgun, letters, beer_use, saw_active, cuff_active, turn
    while turn == 2:
        time.sleep(2)
        if item_count_p2 != 0:
            if dealer_health != max_health:
                if 'Cigarettes' not in p2_inventory:
                    if 'Expired Medicine' in p2_inventory:
                        med_p2()
                    
                elif 'Cigarettes' in p2_inventory:
                    cigs_p2()
                    
            if find not in dealer_knows_which:
                if 'Phone' in p2_inventory:
                    phone_p2()
                    continue
                
            if not dealer_knows_current or not dealer_knows_all:
                if 'Beer' in p2_inventory:
                    beer_p2()
                
                if 'Magnifying Glass' in p2_inventory:
                    mag_p2()
                    
                    
        if dealer_knows_current or dealer_knows_all:
            shot = shotgun.pop(0)
            if shot == 'Live':
                if 'Saw' in p2_inventory:
                    saw_p2()
                    print('\nThe Dealer points the shotgun at you.')
                    w()
                    print('*Boom*')
                    w()
                    print('You lose 2 health.')
                    health -= 2
                    if health < 0:
                        health = 0
                    saw_active = False
                    dealer_knowledge()
                else:
                    print('\nThe Dealer points the shotgun at you.')
                    w()
                    print('\n*Boom*')
                    w()
                    print('\nYou lose 1 health.')
                    w()
                    health -= 1
                    dealer_knowledge()    
                        
            elif shot == 'Blank':
                if 'Inverter' in p2_inventory:
                    print('The Dealer decides to use his Inverter')
                    if 'Saw' in p2_inventory:
                        saw_p2()
                        print('\nThe Dealer points the shotgun at you.')
                        w()
                        print('\n*Boom*')
                        w()
                        print('You lose 2 health.')
                        health -= 2
                        if health < 0:
                            health = 0
                        saw_active = False
                    else:
                        print('\nThe Dealer points the shotgun at you.')
                        w()
                        print('\n*Boom*')
                        w()
                        print('\nYou lose 1 health.')
                        health -= 1
                    dealer_knowledge()
                elif 'Inverter' not in p2_inventory:
                    print('\nThe Dealer points the shotgun at itself')
                    w()
                    print('\n*Click*')
                    dealer_knowledge()
            
        elif not dealer_knows_current or not dealer_knows_all:
            shot = shotgun.pop(0)
            if live_count > blank_count:
                if 'Saw' in p2_inventory:
                    saw_p2()
                print('\nThe Dealer points the shotgun at you.')
                w()
                if shot == 'Blank':
                    print('\n*Click*')
                    w()
                    if cuff_active_p2:
                        cuff_active_p2 = False
                    else:
                        turn = 1
                    saw_active = False
        
                elif shot == 'Live':
                    print('*Boom*')
                    w()
                    if saw_active:
                        health -= 2
                        if health < 0:
                            health = 0
                        saw_active = False
                        print('\nYou lose 2 health.')
                    else:
                        print('\nYou lose 1 health.')
                        health -= 1
                    if cuff_active_p2:
                        cuff_active_p2 = False
                    else:
                        turn = 1
                    w()
                dealer_knowledge()        
            elif live_count < blank_count:
                print('\nThe Dealer points the shotgun at itself')
                w()
                if shot == 'Live':
                    print('\n*Boom*')
                    w()
                    if saw_active:
                        print('\nThe Dealer loses 2 health.')
                        dealer_health -= 2
                        if dealer_health < 0:
                            dealer_health = 0
                    else:
                        print('\nThe Dealer loses 1 health.')
                        dealer_health -= 1
                    if cuff_active_p2:
                        cuff_active_p2 = False
                    else:
                        turn = 1
                elif shot == 'Blank':
                    print('\n*Click*')
                    w()
                saw_active = False    
                dealer_knowledge()
                w()
            elif live_count == blank_count:
                chance_shot = random.randint(1,100)
                if chance_shot % 2 == 0:
                    print('\nThe Dealer points the shotgun at itself.')
                    if shot == 'Live':
                        print('\n*Boom*')
                        w()
                        if saw_active:
                            print('\nThe Dealer loses 2 health.')
                            dealer_health -= 2
                            if dealer_health < 0:
                                dealer_health = 0
                        else:
                            print('\nThe Dealer loses 1 health.')
                            dealer_health -= 1
                        if cuff_active_p2:
                            cuff_active_p2 = False
                        else:
                            turn = 1
                    elif shot == 'Blank':
                        print('\n*Click*')
                        w()
                    saw_active = False    
                    dealer_knowledge()
                    w()
def get_items():
    global item_count_p1, item_count_p2
    max_items = random.randint(3,8)
    for i in range(max_items):
        item_index = random.randint(0,8)
        p1_inventory.append(item_list[item_index])
        item_count_p1 += 1
    
    for i in range(max_items):
        item_index = random.randint(0,8)
        p2_inventory.append(item_list[item_index])
        item_count_p2 += 1
        
get_items()
get_health()
turn = 2
p2()
                
#Witn done with game, remove starting load_shotgun()
#Witn done with game, remove secret debug option

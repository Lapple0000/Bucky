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
item_list_p1 = [] #list of items you have
item_list_p2 = []
item_list = ['Cigarettes', 'Magnifying Glass', 'Beer', 'Saw', 'Phone', 'Inverter', 'Handcuffs', 'Expired Medicine', 'Adrenaline'] #list of all items
dealer_knows_current = False #The dealer in game uses logic 100% correct
dealer_knows_which = []

def dealer_knowledge():
    global dealer_knows_which
    global dealer_knows_current
    dealer_index = 0
    rem = 0
    for i in dealer_knows_which:
        dealer_knows_which[dealer_index] -= 1
        if dealer_knows_which[dealer_index] == 0:
            rem += 1
            dealer_knows_current = True
    for i in range(rem):
        dealer_knows_which.remove(0)
        

def get_health():
    global health
    global max_health
    global dealer_health
    health = random.randint(2,6)
    max_health = health
    dealer_health = health

def shotgun_round():
    round1 = random.randint(1,99)
    if round1 % 2 == 0 :
        return "Blank"
    elif round1 % 2 != 0:
        return "Live"
    
def shotgun_cap():
    cap = random.randint(3,8)
    return cap
    

def load_shotgun():
    global shotgun_cap
    global shotgun_round
    global shotgun
    for i in range(shotgun_cap()):
        shotgun.append(shotgun_round())
load_shotgun()
find = random.randint(1, len(shotgun) - 1) #determines which shell the phone selects

        
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
    item_list_p1.remove('Cigarettes')
    
def cigs_p2():
    global item_count_p2
    global dealer_health
    print('\nThe Dealer decides to smoke a cigarette.')
    time.sleep(2)
    dealer_health += 1
    item_count_p2 -= 1
    item_list_p2.remove('Cigarettes')
    print(f'\nDealer now at {dealer_health} health')    
    
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
    item_list_p1.remove('Magnifying Glass')
    
def mag_p2():
    global shotgun
    global item_count_p2
    global dealer_knows_current
    dealer_knows_current = True
    item_count_p2 -= 1
    item_list_p2.remove('Magnifying Glass')
    
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
    beer_use += 1 #Used only for showing this exact stat at the end of the game
    item_list_p1.remove('Beer')
    find = random.randint(1, len(shotgun) -1)
    
def beer_p2():
    global shotgun 
    global item_count_p2
    global find
    print('\nThe Dealer decides to drink his beer')
    w()
    if shotgun[0] == 'Blank':
        print('\nBlank')
    
    elif shotgun[0] == 'Live':
        print('\nLive')
    w()
    del shotgun[0]
    item_count_p2 -= 1
    item_list_p2.remove('Beer')
    find = random.randint(1, len(shotgun) -1)
    
def saw():
    global saw_active 
    global item_count_p1
    time.sleep(2)
    if not saw_active:
        item_count_p1 -= 1
        saw_active = True
        
        item_list_p1.remove('Saw')
        print('\nYou sawed off the shotgun. Double damage.')
    else:
        print('\nYou already used a saw. Nothing Happens')
    time.sleep(2)
    
def saw_p2():
    global saw_active 
    global item_count_p2
    time.sleep(2)
    if not saw_active:
        item_count_p2 -= 1
        saw_active = True
        item_list_p2.remove('Saw')
        print('\nThe Dealer off the shotgun. Double damage.')
    time.sleep(2)
    
def phone(): 
    global item_count_p1
    global shotgun
    global find
    print(f'\nShell {find + 1}...')
    time.sleep(2)
    print(f'\n{shotgun[find]}')
    time.sleep(2)
    
    item_count_p1 -= 1
    item_list_p1.remove('Phone')
    
def phone_p2(): 
    global item_count_p2
    global find
    print('\nThe Dealer decides to use his phone.')
    dealer_knows_which.append(find)
    item_count_p2 -= 1
    item_list_p2.remove('Phone')
    
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
    item_list_p1.remove('Inverter')
    
def inv_p2(): 
    global item_count_p2
    global shotgun
    print('\nThe dealer decides to use his inverter.')
    time.sleep(2)
    if shotgun[0] == 'Blank':
        shotgun[0] = 'Live'
        
    elif shotgun[0] == 'Live':
        shotgun[0] = 'Blank'
    print('\nInverted')
    time.sleep(2)
    
    item_count_p2 -= 1
    item_list_p2.remove('Inverter')
    
def cuff():
    global cuff_active
    global item_count_p1 
    if not cuff_active:
        cuff_active = True
        item_count_p1 -= 1
        
        item_list_p1.remove('Handcuffs')
        print('\nThe dealer takes the handcuffs and cuffs himself.')
        time.sleep(2)
    else:
        print('\nThe Dealer already has handcuffs on. Nothing happens')
        time.sleep(2)
        
def cuff_p2():
    global cuff_active_p2
    global item_count_p2 
    cuff_active = True
    item_count_p2 -= 1    
    item_list_p1.remove('Handcuffs')
    print('\nThe Dealer cuffs you to the table.')
    time.sleep(2)
        
def med():
    global health
    global max_health
    global item_count_p1 
    chance = random.randint(1, 99)
    print('\nYou swallow the pill.')
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
    
    item_list_p1.remove('Expired Medicine')
    
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
    
    item_list_p2.remove('Expired Medicine')

def p1():
    global turn, cuff_active, shotgun, dealer_health, max_health, saw_active, health, letters, item_list_p1, find
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
                for i in item_list_p1:
                    print(f'{letters[letter_index]}. {i}')
                    letter_index += 1
                max_letters = letters[0:letter_index]
                ans2 = input().upper()
                if ans2 not in max_letters:
                    print('\nNot an item choice\n')
                    
                elif ans2 in max_letters:
                    ans2 = max_letters.index(ans2)
                    ans3 = item_list_p1[ans2]
                    
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
            print('\nThe Dealer has\n')
            time.sleep(2)
            if item_count_p2 != 0:
                for i in item_list_p2:
                    print(f'\n{i}')
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
    global item_count_p1, health, max_health, dealer_health, shotgun, letters, beer_use, saw_active, cuff_active, turn
    while turn == 2:
        time.sleep(2)
        if item_count_p2 != 0:
            if dealer_health != max_health:
                if 'Cigarettes' not in item_list_p2:
                    if 'Expired Medicine' in item_list_p2:
                        med_p2()
                    
                elif 'Cigarettes' in item_list_p2:
                    cigs_p2()
                    
            if find not in dealer_knows_which:
                if 'Phone' in item_list_p2:
                    phone_p2()
                
            if not dealer_knows_current:
                if 'Beer' in item_list_p2:
                    beer_p2()
                
                if 'Magnifying Glass' in item_list_p2:
                    mag_p2()
                    
                    
            if dealer_knows_current:
                if shotgun[0] == 'Live':
                    if 'Saw' in item_list_p2:
                        saw_p2()
                        
            
                        
        
def get_items():
    global item_count_p1, item_count_p2
    max_items = random.randint(3,8)
    for i in range(max_items):
        item_index = random.randint(0,8)
        item_list_p1.append(item_list[item_index])
        item_count_p1 += 1
    
    for i in range(max_items):
        item_index = random.randint(0,8)
        item_list_p2.append(item_list[item_index])
        item_count_p2 += 1
        
get_items()
get_health()


p1()
                
#When done with game, remove starting load_shotgun()
#When done with game, remove secret debug option

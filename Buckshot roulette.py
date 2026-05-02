'''Things to add
The shotgun storage
health from 2-6
items
shotgun mechanics'''
import time
import random
letters = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
shotgun = []
cig_count = 0 #done
mag_count = 0 #done
beer_count = 0 #done
saw_count = 0 #done 
phone_count = 0 #done
inv_count = 0 #done
cuff_count = 0 #done
adl_count = 0
med_count = 0 #done

item_count_p1 = 0
item_count_p2 = 0

saw_active = False
beer_use = 0
health = 0
max_health = 0
dealer_health = 0
turn = 1
cuff_active = False
item_list_p1 = [] #list of items you have
item_list_p2 = []
item_list = ['Cigarettes', 'Magnifying Glass', 'Beer', 'Saw', 'Phone', 'Inverter', 'Handcuffs', 'Expired Medicine', 'Adrenaline'] #list of all items

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
        
        
def cigs():
    global item_count_p1
    global health
    global max_health
    global cig_count
    if health < max_health:
        health += 1
    else:
        print("\nAlready full health. You wasted an item")
        
    cig_count -= 1
    item_count_p1 -= 1
    
def mag():
    global shotgun
    global mag_count
    global item_count_p1
    if shotgun[0] == 'Blank':
        print("\nBlank")
        
    elif shotgun[0] == 'Live':
        print('\nLive')
    mag_count -= 1
    item_count_p1 -= 1
    
def beer():
    global shotgun
    global beer_count
    global item_count_p1
    global beer_use
    if shotgun[0] == 'Blank':
        print('\nBlank')
    
    elif shotgun[0] == 'Live':
        print('\nLive')
        
    del shotgun[0]
    beer_count -= 1
    item_count_p1 -= 1
    beer_use += 1
    
def saw():
    global saw_active
    global saw_count
    saw_active = True
    saw_count -= 1
    
def phone():
    global phone_count
    global item_count_p1
    global shotgun
    find = random.randint(1, len(shotgun))
    print(f'\nShell {find + 1}...')
    time.sleep(1)
    print(f'\n{shotgun[find]}')
    phone_count -= 1
    item_count_p1 -= 1
    
def inv():
    global inv_count
    global item_count_p1
    global shotgun
    if shotgun[0] == 'Blank':
        shotgun[0] = 'Live'
        
    elif shotgun[0] == 'Live':
        shotgun[0] = 'Blank'
    print('\nInverted')    
    inv_count -= 1
    item_count_p1 -= 1
    
def cuff():
    global cuff_active
    global item_count_p1
    global cuff_count
    cuff_active = True
    item_count_p1 -= 1
    cuff_count -= 1
    
def med():
    global health
    global max_health
    global item_count_p1
    global med_count
    chance = random.randint(1, 99)
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
            
    item_count_p1 -= 1
    med_count -= 1
    

def p1():
    global turn, cuff_active, shotgun, dealer_health, max_health, saw_active, health, letters, item_list_p1
    while turn == 1:
        ans = input("\nA. Shoot Dealer\nB. Shoot Yourself\nC. Use an item\n").lower()
        if ans == 'a':
            shot = shotgun.pop(0)
            if shot == 'Live':
                print('\n...')
                time.sleep(2)
                print('\n*Boom*')
                time.sleep(2)
                print('\nDealer lost 1 health.')
                time.sleep(2)
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
                if cuff_active:
                    cuff_active = False
                    turn = 1
                    
                else:
                    turn = 2
            
        elif ans == 'b':
            shot = shotgun.pop()
            if shot == 'Live':
                print('\n...')
                time.sleep(2)
                print("\n*Boom*")
                time.sleep(2)
                print('\nYou lose 1 health.')
                time.sleep(2)
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
                
        elif ans == 'c':
            print("\nPick your item\n")
            time.sleep(2)
            letter_index = 26
            for i in item_list_p1:
                print(f'\n{letters[letter_index]}. {i}')
                letter_index += 1
            ans2 = input()
            
                

    
def p2():
    global item_count_p1, med_count, cig_count, inv_count, saw_count, cuff_count, mag_count, beer_count, adl_count, phone_count, health, max_health, dealer_health, shotgun, letters, beer_use, saw_active, cuff_active, turn
    while turn == 2:
        time.sleep(2)
        print('\nHmm...')
        
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
        

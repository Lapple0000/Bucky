#When coding the dealer, make sure he doesn't use the magnifying glass when he already knows the current shell or shotgun[0]
'''
beer--
magnifying glass--
saw--
cuffs--
cigs--
adrenaline--
inverter--
phone--
medicine--
'''
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import time
import random
import shotgun_possibilities

def w():
    time.sleep(2)
'''shotgun = []
def load_shotgun(): #permenant assignment
    global shotgun
    shotgun = shotgun_possibilities.load_shotgun()
load_shotgun() #temporary''' #temporary disable


def p_item_removal(item):
    #if item not in p_inventory:
     #   quit('Something went wrong, tried to use item thats not in inventory.')
    for i in range(len(p_inventory)):
        if p_inventory[i] == item:
            p_inventory.pop(i)
            break
        
def d_item_removal(item):
    #if item not in d_inventory:
     #   quit('Something went wrong, tried to use item thats not in inventory.')
    for i in range(len(d_inventory)):
        if d_inventory[i] == item:
            d_inventory.pop(i)
            break
l = 'Live'
b = 'Blank'
d_knows_all = False
d_knows_current = False
item_list = ['Burner Phone', "Magnifying Glass", "Handcuffs", "Inverter", 'Can of Beer', 'Saw', 'Pack of Cigarettes', 'Expired Medicine Tablet', 'Adrenaline']
d_inventory = ['Burner Phone', "Magnifying Glass", "Handcuffs", "Inverter", 'Can of Beer', 'Pack of Cigarettes', 'Expired Medicine Tablet', 'Adrenaline']
p_inventory = ['Burner Phone', "Magnifying Glass", "Handcuffs", "Inverter", 'Can of Beer', 'Pack of Cigarettes', 'Expired Medicine Tablet', 'Adrenaline']
d_adr_inventory = []
def adr_inventory():
    global d_adr_inventory, d_inventory, p_inventory
    for i in d_inventory:
        d_adr_inventory.append(i)
    for i in p_inventory:
        d_adr_inventory.append(i)
p_health = 0
d_health = 0
max_health = 0
d_cuff_active = False
p_cuff_active = False
saw_active = False
turn = 0 # 1 is player, 2 is dealer

def get_health():
    global p_health, d_health, max_health
    max_health = (random.randint(0, 5000) % 5) + 2
    d_health = max_health
    p_health = max_health
    
#this is gonna fucking suck. Coding dealer prediction bullshit
d_knows = []
l_amt = 0
b_amt = 0

def d_all():
    global d_knows_all, d_knows_current, l_amt, b_amt
    b_amt = 0
    l_amt = 0
    d_knows_polarity = []
    for i in shotgun:
        if i == l:
            l_amt += 1
        elif i == b:
            b_amt += 1
    for i in d_knows:
        if not d_knows == []:
            d_knows_polarity.append(shotgun[i])
    if d_knows_polarity.count(l) == l_amt:
        d_knows_all = True
    elif d_knows_polarity.count(b) == b_amt:
        d_knows_all = True
    else:
        d_knows_all = False
    d_knows.sort()
    if 0 in d_knows:
        d_knows_current = True
    elif d_knows_all:
        d_knows_current = True
    else:
        d_knows_current = False

def d_knowledge():
    global d_knows
    for i in d_knows:
        d_knows[d_knows.index(i)] -= 1
#         print(i)
    d_knows.sort()
    if not d_knows == []:
        if d_knows[0] == -1:
            del d_knows[0]
    d_all()
            
    
shotgun = [b, l, l, b, b] #temporary

def p_magnify():
    print('You smash the magnifying glass and look in the chamber...\n')
    w()
    print('Current shell: ' + shotgun[0] + '\n')
    w()
    p_item_removal('Magnifying Glass')
    
def d_magnify():
    global d_knows, d_knows_current
    d_knows.append(0)
    d_knows.sort()
    d_knows_current = True
    print('The Dealer smashes a magnifying glass and looks in the chamber.\n')
    w()
    print('[The Dealer]: Very interesting...\n')
    w()
    d_item_removal('Magnifying Glass')
    d_all()
        
def p_beer():
    print('You shotgun a can of beer....\n') #Pun intended
    w()
    print(f'You eject the shell, it was {shotgun.pop(0)}.\n')
    w()
    p_item_removal('Can of Beer')
    
def d_beer():
    print('The Dealer chugs a can of beer....\n') #Pun intended
    w()
    print(f'The Dealer ejects the shell, it was {shotgun.pop(0)}.\n')
    w()
    d_item_removal('Can of Beer')
    d_knowledge()
    
def p_inverter():
    print('You use the Inverter...\n')
    w()
    if shotgun[0] == b:
        shotgun[0] = l
        
    elif shotgun[0] == b:
        shotgun[0] = l
        
    p_item_removal('Inverter')
    
def d_inverter():
    print('The Dealer uses the Inverter...\n')
    w()
    if shotgun[0] == b:
        shotgun[0] = l
        
    elif shotgun[0] == b:
        shotgun[0] = l
        
    d_item_removal('Inverter')
    d_all()
    
def p_phone():
    print('You pick up a burner phone and dial the only contact in there.\n')
    time.sleep(3)
    
    if len(shotgun) <= 2:
        print('Mysterious Voice: Damn, tough luck.\n')
        w()
        
    else:
        phone_prediction = random.randint(0, 2000) % len(shotgun)
        if phone_prediction == 0:
            phoneprediction = -1
        print(f'Mysterious Voice: Shell number {phone_prediction+1}...')
        w()
        print(f'Mysterious Voice: {shotgun[phone_prediction]}\n')
        w()
    print('You snap the phone in half.\n')
    w()
    p_item_removal('Burner Phone')
    
def d_phone():
    print('The Dealer picks up a burner phone and dials an unknown number.\n')
    time.sleep(2)
    
    if len(shotgun) <= 2:
        print('[The Dealer]: Shit...\n')
        w()
        print('''Also shouldn't happen btw''')
        
    else:
        phone_prediction = random.randint(0, 2000) % len(shotgun)
        if phone_prediction == 0:
            phoneprediction = -1
        print(f'[The Dealer]: Very interesting...\n')
        w()
        
    print('The Dealer snaps the phone in half.\n')
    w()
    d_item_removal('Burner Phone')
    if phone_prediction not in d_knows:
        d_knows.append(phone_prediction)
        d_all()

def p_saw():
    global saw_active
    if not saw_active:
        print('You used the saw to cut the barrel off.\n')
        w()
        print("That's illegal in 5 states.\n")
        w()
        p_item_removal('Saw')
        saw_active = True
    elif saw_active:
        print('The shotgun is already cut.\n')
        w()
        
def d_saw():
    global saw_active
    if not saw_active:
        print('The Dealer grabs a saw to cut the barrel off.\n')
        w()
        print("It likely doesn't care about laws.\n")
        w()
        d_item_removal('Saw')
        saw_active = True
    elif saw_active:
        print('This should not happen, There is something wrong with the code that is making the dealer use a saw when the saw has already been used\n')
        w()
    
def p_cuff():
    global p_cuff_active
    if not p_cuff_active:
        print('The Dealer takes a pair of handcuffs from you and puts them on itself.\n')
        w()
        print("The Dealer's next turn will be skipped.\n")
        w()
        p_item_removal('Handcuffs')
        p_cuff_active = True
    elif p_cuff_active:
        print('The Dealer already has cuffs on itself\n')
        w()
        
def d_cuff():
    global d_cuff_active
    if not d_cuff_active:
        print('The Dealer takes a pair of handcuffs and puts them on you.\n')
        w()
        print("Your next turn will be skipped.\n")
        w()
        d_item_removal('Handcuffs')
        d_cuff_active = True
    elif d_cuff_active:
        print('This should not happen. Dealer is trying to use handcuffs when handcuffs are already in use\n')
        w()

def p_cig():
    global p_health, d_health, max_health
    print('You smoke a cigarette...\n')
    w()
    if p_health == max_health:
        print('You are already at full health. Nothing happens.\n')
    elif p_health < max_health:
        print('You gain 1 health.\n')
        p_health += 1
    w()
    p_item_removal('Pack of Cigarettes')

def d_cig():
    global d_health, d_health, max_health
    print('The Dealer smokes a cigarette...\n')
    w()
    if d_health == max_health:
        print('This should not happen. The Dealer is trying to smoke at full health\n')
    elif d_health < max_health:
        print('The Dealer gains 1 health.\n')
        d_health += 1
    w()
    d_item_removal('Pack of Cigarettes')

def p_adrenaline():
    if len(p_inventory) >= 9:
        print("Don't get greedy now...\n")
        w()
    else:
        good = False
        for i in d_inventory:
            if i != 'Adrenaline':
                good = True
        if d_inventory == []:
            print('The Dealer has no items.\n')
            w()
        elif ('Adrenaline' in d_inventory) and (not good):
            print('The Dealer only has adrenaline. You may not take its adrenaline.\n')
            w()
        else:
            print("You pump yourself with adrenaline. You may take one of The Dealer's items.\n")
            w()
            choice_valid = False
            while not choice_valid:
                for i in d_inventory:
                    print(f'{letters[d_inventory.index(i)]}. {i}')
                print()
                choice = input().lower()
                if choice.upper() not in letters[0:len(d_inventory)]:
                    print('Not a valid choice. Try again.\n')
                    time.sleep(1)
                elif choice.upper() in letters[0:len(d_inventory)]:
                    if d_inventory[letters.index(choice.upper())] == "Adrenaline":
                        print('''You are not able to take The Dealer's adrenaline.''')
                    else:
                        p_inventory.append(d_inventory.pop(letters.index(choice.upper())))
                        if p_inventory[-1].startswith(('A','E', 'I', 'O', 'U')):
                            print(f'You took an {p_inventory[-1].lower()} from it.\n')#vowels
                        else:
                            print(f'You took a {p_inventory[-1].lower()} from it.\n')#not vowels
                            w()
                        p_item_usage(p_inventory[-1])
                        p_item_removal('Adrenaline')
                        choice_valid = True

def d_adrenaline(choice):
    if len(d_inventory) >= 9:
        print("Don't get greedy now...\n")
        w()
    else:
        good = False
        for i in p_inventory:
            if i != 'Adrenaline':
                good = True
        if p_inventory == []:
            print('This should not happen, the dealer is trying to use adenaline when you have nothing\n')
            w()
        elif ('Adrenaline' in p_inventory) and (not good):
            print('This should not happen, the dealer is trying to use adenaline when you only have adrenaline\n')
            w()
        else:
            print('The Dealer pumps itself with adrenaline. The Dealer will take one of your items.\n')
            w()
            choice_valid = False
            while not choice_valid:
                if choice not in p_inventory:
                    print('Dealer tried to make an invalid choice\n')
                    time.sleep(1)
                elif choice in p_inventory:
                    if choice == "Adrenaline":
                        print('This should not happen. Dealer is trying to take your adrenaline')
                    else:
                        d_inventory.append(p_inventory.pop(p_inventory.index(choice)))
                        if d_inventory[-1].startswith(('A','E', 'I', 'O', 'U')):
                            print(f'The Dealer took an {d_inventory[-1].lower()} from you.\n')#vowels
                            w()
                        else:
                            print(f'The Dealer took a {d_inventory[-1].lower()} from you.\n')#not vowels
                            w()
                        d_item_removal('Adrenaline')
                        d_item_usage(d_inventory[-1])
                    choice_valid = True
                    
def p_meds():
    global p_health, max_health
    print('You swallow a tablet of expired medicine.\n')
    w()
    damage = random.randint(0, 5000)
    if damage % 2 == 0:
        print('Unlucky, the medicine poisons you.\n')
        p_health -= 1
    elif damage % 2 == 1:
        if p_health == (max_health - 1):
            print('You lucked out and gained 1 health.\n')
            p_health += 1
        elif p_health < (max_health - 1):
            print('You lucked out and gained 2 health.\n')
            p_health += 2
        elif p_health == max_health:
            print('You are already at full health. Nothing happens\n')
    p_item_removal('Expired Medicine Tablet')
    w()

def d_meds():
    global d_health, max_health
    print('The Dealer swallows a tablet of expired medicine.\n')
    w()
    damage = random.randint(0, 5000)
    if d_health == 1:
        print('This should not happen. Dealer took medicine while at 1 health')
    if damage % 2 == 0:
        print('The Dealer gets poisoned and loses 1 health.\n')
        d_health -= 1
    elif damage % 2 == 1:
        if d_health == (max_health - 1):
            print('The Dealer gained 1 health.\n')
            d_health += 1
        elif d_health < (max_health - 1):
            print('The Dealer gained 2 health.\n')
            d_health += 2
        elif d_health == max_health:
            print('This should not happen. Dealer tried to take medicine at full health\n')
    d_item_removal('Expired Medicine Tablet')
    w()


def p_item_usage(ans):
    ans1 = item_list.index(ans)
    if ans1 == 0:
        p_phone()
    elif ans1 == 1:
        p_magnify()
    elif ans1 == 2:
        p_cuff()
    elif ans1 == 3:
        p_inverter()
    elif ans1 == 4:
        p_beer()
    elif ans1 == 5:
        p_saw()
    elif ans1 == 6:
        p_cig()
    elif ans1 == 7:
        p_meds()
    elif ans1 == 8:
        p_adrenaline()

def d_item_usage(ans):
    ans1 = item_list.index(ans)
    if ans1 == 0:
        d_phone()
    elif ans1 == 1:
        d_magnify()
    elif ans1 == 2:
        d_cuff()
    elif ans1 == 3:
        d_inverter()
    elif ans1 == 4:
        d_beer()
    elif ans1 == 5:
        d_saw()
    elif ans1 == 6:
        d_cig()
    elif ans1 == 7:
        d_meds()
    elif ans1 == 8:
        d_adrenaline()


def d_item_usage2(item):
    if item in d_adr_inventory:
        print()
        if item in d_inventory:
            d_item_usage(item)
        else:
            if 'Adrenaline' in d_inventory:
                d_adrenaline(item)
    else:
        return False
    
            











#time to code the dealer
def dealer():
    global turn, d_cuff_active, p_cuff_active, l, b, shotgun
    while turn == 2:
        d_all()
        #Healing items
        while d_health < max_health:
            #Cigs
            d_item_usage2('Pack of Cigarettes')
            #Meds
            if 'Pack of Cigarettes' not in d_adr_inventory: #meds is an exception to the item_usage2 thing
                if 'Expired Medicine Tablet' in d_adr_inventory:
                    if 'Expired Medicine Tablet' not in d_inventory:
                        if 'Adrenaline' in d_inventory:
                            if d_health == 1:
                                break
                            elif d_health > 1:
                                d_adrenaline('Expired Medicine Tablet')
                        elif 'Adrenaline' not in d_inventory:
                            break
                    elif 'Expired Medicine Tablet' in d_inventory:
                        if d_health == 1:
                            break
                        elif d_health > 1:
                            d_item_usage('Expired Medicine Tablet')
                else:
                    break
        #Revealing items
        while not d_knows_current:
            
            a = d_item_usage2('Magnifying Glass')
            
            b = d_item_usage2('Can of Beer')
            
            if not (a or b):
                break
            
        if ('Inverter' in d_adr_inventory) and (d_knows_current) and (shotgun[0] == b):
            d_item_usage2('Inverter')
            
        while (d_knows_current) and (('Inverter' not in d_inventory) or (('Inverter' not in d_adr_inventory) or ('Adrenaline' not in d_inventory))):
            if shotgun != []:
                if shotgun[0] == b:
                    if 'Can of Beer' in d_adr_inventory:
                        d_item_usage2('Can of Beer')
                    else:
                        break
                else:
                    break
            else:
                break
        while ('Burner Phone' in d_inventory) or (('Burner Phone' in d_adr_inventory) and ('Adrenaline') in d_inventory):
            if len(shotgun) < 3:
                break
            else:
                d_item_usage2('Burner Phone')
        
        #misc items
        if shotgun != []:
            if (d_knows_current and (shotgun[0] == l) and (not saw_active)) or ((not d_knows_current) and (l_amt > b_amt)):
                d_item_usage2('Saw')
            
        if not d_cuff_active:
            d_item_usage2('Handcuffs')
            
        if shotgun == []:
            turn = 0
            d_cuff_active = False
            
        elif d_cuff_active and (shotgun != []):
            d_cuff_active = False
            
        else:
            turn = 1

def player():
    global turn, d_cuff_active, p_cuff_active, l, b, shotgun

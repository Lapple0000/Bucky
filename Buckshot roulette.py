'''Things to add
The shotgun storage
health from 2-6
items
shotgun mechanics'''
import time
import random
letters = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
shotgun = []
cigarette_count = 0
mag_glass_count = 0

def get_health():
    return random.randint(2,6)
health = get_health()
max_health = health

def shotgun_round():
    round1 = random.randint(1,99)
    if round1 % 2 == 0 :
        return "blank"
    if round1 % 2 != 0:
        return "live"
    
def shotgun_cap():
    cap = random.randint(3,8)
    return cap
    

def load_shotgun():
    global shotgun_cap
    global shotgun_round
    global shotgun
    for i in range(shotgun_cap()):
        shotgun.append(shotgun_round())
        
        
def cigarettes():
    global health
    global max_health
    global cigarette_count
    if health < max_health:
        health += 1
    else:
        print("\nAlready full health. You wasted an item\n")
        
    cigarette_count -= 1
    
def mag_glass():
    global shotgun
    global mag_glass_count
    if shotgun[0] == 'blank':
        print("Blank")
        
    elif shotgun[0] == 'live':
        print('Live')
    mag_glass_count -= 1
    
load_shotgun()
mag_glass()
live = 'Live'
blank = 'Blank'
Live = live
Blank = blank
b = blank
l = live
live_count = 0
blank_count = 0
shotgun = []
import erthith
import random

shell_2 = {"1l1b":
           {"pos_1": [l, b],
           'pos_2': [b, l]}}

shell_3 = {"1l2b":
           {'pos_1': [l, b, b],
            'pos_2': [b, l, b],
            'pos_3': [b, b, l]},
           "2l1b":
           {'pos_1': [l, l, b],
            'pos_2': [l, b, l],
            'pos_3': [b, l, l]}}

shell_4 = {"1l3b":
           {'pos_1': [l, b, b, b],
            'pos_2': [b, l, b, b],
            'pos_3': [b, b, l, b],
            'pos_4': [b, b, b, l]},
           "2l2b":
           {'pos_1': [l, l, b, b],
            'pos_2': [l, b, l, b],
            'pos_3': [l, b, b, l],
            'pos_4': [b, l, l, b],
            'pos_5': [b, l, b, l],
            'pos_6': [b, b, l, l]},
           "3l1b":
           {'pos_1': [l, l, l, b],
            'pos_2': [l, l, b, l],
            'pos_3': [l, b, l, l],
            'pos_4': [b, l, l, l]}} 

shell_5 = {"1l4b":
           {'pos_1': [l, b, b, b, b],
            'pos_2': [b, l, b, b, b],
            'pos_3': [b, b, l, b, b],
            'pos_4': [b, b, b, l, b],
            'pos_5': [b, b, b, b, l]},
           "2l3b":
           {'pos_1': [l, l, b, b, b],
            'pos_2': [l, b, l, b, b],
            'pos_3': [l, b, b, l, b],
            'pos_4': [l, b, b, b, l],
            'pos_5': [b, l, l, b, b],
            'pos_6': [b, l, b, l, b],
            'pos_7': [b, l, b, b, l],
            'pos_8': [b, b, l, l, b],
            'pos_9': [b, b, l, b, l],
            'pos_10': [b, b, b, l, l]},
           "3l2b":
           {'pos_1': [l, l, l, b, b],
            'pos_2': [l, l, b, l, b],
            'pos_3': [l, l, b, b, l],
            'pos_4': [l, b, l, l, b],
            'pos_5': [l, b, l, b, l],
            'pos_6': [l, b, b, l, l],
            'pos_7': [b, l, l, l, b],
            'pos_8': [b, l, l, b, l],
            'pos_9': [b, l, b, l, l],
            'pos_10': [b, b, l, l, l]},
           "4l1b":
           {'pos_1': [l, l, l, l, b],
            'pos_2': [l, l, l, b, l],
            'pos_3': [l, l, b, l, l],
            'pos_4': [l, b, l, l, l],
            'pos_5': [b, l, l, l, l]}}

shell_6 = {"2l4b":
           {'pos_1': [l, l, b, b, b, b],
            'pos_2': [l, b, l, b, b, b],
            'pos_3': [l, b, b, l, b, b],
            'pos_4': [l, b, b, b, l, b],
            'pos_5': [l, b, b, b, b, l],
            'pos_6': [b, l, l, b, b, b],
            'pos_7': [b, l, b, l, b, b],
            'pos_8': [b, l, b, b, l, b],
            'pos_9': [b, l, b, b, b, l],
            'pos_10': [b, b, l, l, b, b],
            'pos_11': [b, b, l, b, l, b],
            'pos_12': [b, b, l, b, b, l],
            'pos_13': [b, b, b, l, l, b],
            'pos_14': [b, b, b, l, b, l],
            'pos_15': [b, b, b, b, l, l]},
           "3l3b":
           {'pos_1': [l, l, l, b, b, b],
            'pos_2': [l, l, b, l, b, b],
            'pos_3': [l, l, b, b, l, b],
            'pos_4': [l, l, b, b, b, l],
            'pos_5': [l, b, l, l, b, b],
            'pos_6': [l, b, l, b, l, b],
            'pos_7': [l, b, l, b, b, l],
            'pos_8': [l, b, b, l, l, b],
            'pos_9': [l, b, b, l, b, l],
            'pos_10': [l, b, b, b, l, l],
            'pos_11': [b, l, l, l, b, b],
            'pos_12': [b, l, l, b, l, b],
            'pos_13': [b, l, l, b, b, l],
            'pos_14': [b, l, b, l, l, b],
            'pos_15': [b, l, b, l, b, l],
            'pos_16': [b, l, b, b, l, l],
            'pos_17': [b, b, l, l, l, b],
            'pos_18': [b, b, l, l, b, l],
            'pos_19': [b, b, l, b, l, l],
            'pos_20': [b, b, b, l, l, l]},
           "4l2b":
           {'pos_1': [b, b, l, l, l, l],
            'pos_2': [b, l, b, l, l, l],
            'pos_3': [b, l, l, b, l, l],
            'pos_4': [b, l, l, l, b, l],
            'pos_5': [b, l, l, l, l, b],
            'pos_6': [l, b, b, l, l, l],
            'pos_7': [l, b, l, b, l, l],
            'pos_8': [l, b, l, l, b, l],
            'pos_9': [l, b, l, l, l, b],
            'pos_10': [l, l, b, b, l, l],
            'pos_11': [l, l, b, l, b, l],
            'pos_12': [l, l, b, l, l, b],
            'pos_13': [l, l, l, b, b, l],
            'pos_14': [l, l, l, b, l, b],
            'pos_15': [l, l, l, l, b, b]}}

shell_7 = {"3l4b":
           {'pos_1': [l, l, l, b, b, b, b],
            'pos_2': [l, l, b, l, b, b, b],
            'pos_3': [l, l, b, b, l, b, b],
            'pos_4': [l, l, b, b, b, l, b],
            'pos_5': [l, l, b, b, b, b, l],
            'pos_6': [l, b, l, l, b, b, b],
            'pos_7': [l, b, l, b, l, b, b],
            'pos_8': [l, b, l, b, b, l, b],
            'pos_9': [l, b, l, b, b, b, l],
            'pos_10': [l, b, b, l, l, b, b],
            'pos_11': [l, b, b, l, b, l, b],
            'pos_12': [l, b, b, l, b, b, l],
            'pos_13': [l, b, b, b, l, l, b],
            'pos_14': [l, b, b, b, l, b, l],
            'pos_15': [l, b, b, b, b, l, l],
            'pos_16': [b, l, l, l, b, b, b],
            'pos_17': [b, l, l, b, l, b, b],
            'pos_18': [b, l, l, b, b, l, b],
            'pos_19': [b, l, l, b, b, b, l],
            'pos_20': [b, l, b, l, l, b, b],
            'pos_21': [b, l, b, l, b, l, b],
            'pos_22': [b, l, b, l, b, b, l],
            'pos_23': [b, l, b, b, l, l, b],
            'pos_24': [b, l, b, b, l, b, l],
            'pos_25': [b, l, b, b, b, l, l],
            'pos_26': [b, b, l, l, l, b, b],
            'pos_27': [b, b, l, l, b, l, b],
            'pos_28': [b, b, l, l, b, b, l],
            'pos_29': [b, b, l, b, l, l, b],
            'pos_30': [b, b, l, b, l, b, l],
            'pos_31': [b, b, l, b, b, l, l],
            'pos_32': [b, b, b, l, l, l, b],
            'pos_33': [b, b, b, l, l, b, l],
            'pos_34': [b, b, b, l, b, l, l],
            'pos_35': [b, b, b, b, l, l, l]},
           "4l3b":
            {'pos_1': [b, b, b, l, l, l, l],
            'pos_2': [b, b, l, b, l, l, l],
            'pos_3': [b, b, l, l, b, l, l],
            'pos_4': [b, b, l, l, l, b, l],
            'pos_5': [b, b, l, l, l, l, b],
            'pos_6': [b, l, b, b, l, l, l],
            'pos_7': [b, l, b, l, b, l, l],
            'pos_8': [b, l, b, l, l, b, l],
            'pos_9': [b, l, b, l, l, l, b],
            'pos_10': [b, l, l, b, b, l, l],
            'pos_11': [b, l, l, b, l, b, l],
            'pos_12': [b, l, l, b, l, l, b],
            'pos_13': [b, l, l, l, b, b, l],
            'pos_14': [b, l, l, l, b, l, b],
            'pos_15': [b, l, l, l, l, b, b],
            'pos_16': [l, b, b, b, l, l, l],
            'pos_17': [l, b, b, l, b, l, l],
            'pos_18': [l, b, b, l, l, b, l],
            'pos_19': [l, b, b, l, l, l, b],
            'pos_20': [l, b, l, b, b, l, l],
            'pos_21': [l, b, l, b, l, b, l],
            'pos_22': [l, b, l, b, l, l, b],
            'pos_23': [l, b, l, l, b, b, l],
            'pos_24': [l, b, l, l, b, l, b],
            'pos_25': [l, b, l, l, l, b, b],
            'pos_26': [l, l, b, b, b, l, l],
            'pos_27': [l, l, b, b, l, b, l],
            'pos_28': [l, l, b, b, l, l, b],
            'pos_29': [l, l, b, l, b, b, l],
            'pos_30': [l, l, b, l, b, l, b],
            'pos_31': [l, l, b, l, l, b, b],
            'pos_32': [l, l, l, b, b, b, l],
            'pos_33': [l, l, l, b, b, l, b],
            'pos_34': [l, l, l, b, l, b, b],
            'pos_35': [l, l, l, l, b, b, b]}}

shell_8 = {"4l4b":
           {'pos_1': [l, l, l, l, b, b, b, b],
            'pos_2': [l, l, l, b, l, b, b, b],
            'pos_3': [l, l, l, b, b, l, b, b],
            'pos_4': [l, l, l, b, b, b, l, b],
            'pos_5': [l, l, l, b, b, b, b, l],
            'pos_6': [l, l, b, l, l, b, b, b],
            'pos_7': [l, l, b, l, b, l, b, b],
            'pos_8': [l, l, b, l, b, b, l, b],
            'pos_9': [l, l, b, l, b, b, b, l],
            'pos_10': [l, l, b, b, l, l, b, b],
            'pos_11': [l, l, b, b, l, b, l, b],
            'pos_12': [l, l, b, b, l, b, b, l],
            'pos_13': [l, l, b, b, b, l, l, b],
            'pos_14': [l, l, b, b, b, l, b, l],
            'pos_15': [l, l, b, b, b, b, l, l],
            'pos_16': [l, b, l, l, l, b, b, b],
            'pos_17': [l, b, l, l, b, l, b, b],
            'pos_18': [l, b, l, l, b, b, l, b],
            'pos_19': [l, b, l, l, b, b, b, l],
            'pos_20': [l, b, b, l, l, l, b, b],
            'pos_21': [l, b, b, l, l, b, l, b],
            'pos_22': [l, b, b, l, l, b, b, l],
            'pos_23': [l, b, b, l, b, l, l, b],
            'pos_24': [l, b, b, l, b, l, b, l],
            'pos_25': [l, b, b, l, b, b, l, l],
            'pos_26': [l, b, b, b, l, l, l, b],
            'pos_27': [l, b, b, b, l, l, b, l],
            'pos_28': [l, b, b, b, l, b, l, l],
            'pos_29': [l, b, b, b, b, l, l, l],
            'pos_30': [b, l, l, l, l, b, b, b],
            'pos_31': [b, l, l, l, b, l, b, b],
            'pos_32': [b, l, l, l, b, b, l, b],
            'pos_33': [b, l, l, l, b, b, b, l],
            'pos_34': [b, l, l, b, l, l, b, b],
            'pos_35': [b, l, l, b, l, b, l, b],
            'pos_36': [b, l, l, b, l, b, b, l],
            'pos_37': [b, l, l, b, b, l, l, b],
            'pos_38': [b, l, l, b, b, l, b, l],
            'pos_39': [b, l, l, b, b, b, l, l],
            'pos_40': [b, l, b, l, l, l, b, b],
            'pos_41': [b, l, b, l, l, b, l, b],
            'pos_42': [b, l, b, l, l, b, b, l],
            'pos_43': [b, l, b, l, b, l, l, b],
            'pos_44': [b, l, b, l, b, l, b, l],
            'pos_45': [b, l, b, l, b, b, l, l],
            'pos_46': [b, l, b, b, l, l, l, b],
            'pos_47': [b, l, b, b, l, l, b, l],
            'pos_48': [b, l, b, b, l, b, l, l],
            'pos_49': [b, l, b, b, b, l, l, l],
            'pos_50': [b, b, l, l, l, l, b, b],
            'pos_51': [b, b, l, l, l, b, l, b],
            'pos_52': [b, b, l, l, l, b, b, l],
            'pos_53': [b, b, l, l, b, l, l, b],
            'pos_54': [b, b, l, l, b, l, b, l],
            'pos_55': [b, b, l, l, b, b, l, l],
            'pos_56': [b, b, l, b, l, l, l, b],
            'pos_57': [b, b, l, b, l, l, b, l],
            'pos_58': [b, b, l, b, l, b, l, l],
            'pos_59': [b, b, l, b, b, l, l, l],
            'pos_60': [b, b, b, l, l, l, l, b],
            'pos_61': [b, b, b, l, l, l, b, l],
            'pos_62': [b, b, b, l, l, b, l, l],
            'pos_63': [b, b, b, l, b, l, l, l],
            'pos_64': [b, b, b, b, l, l, l, l]}} 

def all_pos(yes):
    for i in yes:
        print(f'{i}:\n')
        for j in yes[i]:
            print('\n' + j + ':')
            for k in yes[i][j]:
                print(f"{k}")
        print('\n\n\n\n')
        
shell_list = [shell_2, shell_3, shell_4, shell_5, shell_6, shell_7, shell_8]
        
def load_shotgun():
    global shell_list, shotgun_cap, live_count, blank_count, shotgun, shell_2, shell_3, shell_4, shell_5, shell_6, shell_7, shell_8
    shell_choice = random.randint(0,6)
    shell_amount_list = []
    pos_list = []
    
    for i in shell_list[shell_choice]:
        shell_amount_list.append(i)
    shell_amount_rand = random.randint(0, len(shell_amount_list) - 1)
    for j in (shell_list[shell_choice])[shell_amount_list[shell_amount_rand]]:
        pos_list.append(j)
    pos_rand = random.randint(0, len(pos_list) - 1)
    shotgun = (shell_list[shell_choice])[(shell_amount_list[shell_amount_rand])][(pos_list[pos_rand])]
    
load_shotgun()
print(shotgun)
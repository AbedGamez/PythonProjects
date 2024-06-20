# Locked/Unlocked
bed_mixer = False
blue_bed = False
yellow_bed = False
wheeled_bed = False
green_bed = False
red_bed = False
lucky_bed = False
purple_bed = False
white_bed = False
pink_bed = False
rainbow_bed = False
magical_bed = False
garbage_bed = False
quest_bed = False
car_bed = False
stray_bed = False
time_bed = False
math_bed = False
dirty_bed = False
apple_bed = False
space_bed = False
nuclear_bed = False
rocket_bed_E = False
rocket_bed_Fb = False
diamond_bed = False
bedrock_bed = False
stone_bed = False
underwater_bed = False
dream_bed = False
orange_bed = False
winning_bed = False
combat_bed = False
gold_bed = False
aura_bed = False
magma_bed = False
secret_agent_bed = False
love_bed = False
garbage_one = False
garbage_two = False
garbage_three = False
nuclear_one = False
nuclear_two = False
rocket_fuel = False
rocket_bed_F = False
win_mmm = False
win_ms = True
cave = False
road = False
#pvp items
bp_m = False
tank_a = False
en_c = False
dmg_o = False
sp_d = False
advbp_m = False
heal_c = False

# Battle Points
bp = 0

# filter
date_added = True
proper_form = False

# bed counters
bed_c = 0
bed_cvr = 0
bed_winc = 0

# modules
import random
import time

#elemental mountain variables
fire = 0
firea = 0
water = 0
air = 0
plant = 0
earth = 0

#day and night
day_time = True
night_time = False

#love valley
lcards = 0
freelcard = True

#school
schoolsignup = False
day_one = True
day_two = False
day_final = False
scoresc = 0
books = False
nexts = 0

#levels
levelexp = 0
level_t = False
level_th = False
level_f = False
level_fi = False
level_s = False
level_se = False
level_e = False
level_n = False
level_te = False
level_el = False
level_tw = False
sjxuh = True

#quests
q_o = False
q_t = False
q_th = False
q_f = False
q_fi = False
q_s = False
q_se = False
q_e = False
callo = True
callt = True
callth = True
callf = True
callfi = True
calls = True
callse = True
calle = True
doneo = False
donet = False
doneth = False
donef = False
donefi = False
dones = False
donese = False
donee = False
questcounter = 0
#gem shop
gems = 0
chancem = False
prizem = False

name = input("What is your name?")
time.sleep(1)





# welcome message
print("Welcome to...")
time.sleep(2)
print("Find")
print(" The")
print("  BEDS!")
time.sleep(0.8)
print("Version 1.7")
time.sleep(2)
print("")
print("")



# start
closegamesure=True
while closegamesure==True:
    print("________________________________")
    print("Places to search...")
    if blue_bed==False:
        print("Blue Walls")
    if blue_bed==True:
        print("Blue Walls ✓")
    if yellow_bed==False:
        print("Yellow Walls")
    if yellow_bed==True:
        print("Yellow Walls ✓")
    if red_bed==False:
        print("Red Walls")
    if red_bed==True:
        print("Red Walls ✓")
    if white_bed==False:
        print("White Walls")
    if white_bed==True:
        print("White Walls ✓")
    if lucky_bed==False or bed_mixer==False or wheeled_bed==False:
        print("Wheel Spin")
    if lucky_bed==True and bed_mixer==True and wheeled_bed==True:
        print("Wheel Spin ✓")
    if dream_bed==False:
        print("Sleep")
    if dream_bed==True:
        print("Sleep ✓")
    if stray_bed==False:
        print("Road")
    if stray_bed==True:
        print("Road ✓")
    if road == True:
        if math_bed==False:
            print("School")
        if math_bed==True:
            print("School ✓")
        if apple_bed==False:
            print("Tree")
        if apple_bed==True:
            print("Tree ✓")
        if dirty_bed==False or garbage_bed==False:
            print("Dumpster")
        if dirty_bed==True and garbage_bed==True:
            print("Dumpster ✓")
    if underwater_bed==True and rocket_bed_E==True and rocket_fuel==True:
        print("Underwater ✓")
    if underwater_bed==False or rocket_bed_E==False or rocket_fuel==False:
        print("Underwater")
    if space_bed==False:
        print("Space")
    if space_bed==True:
        print("Space ✓")
    if cave == False:
        print("Nuclear mark")
    if cave == True:
        if bedrock_bed==False:
            print("Cave")
        if bedrock_bed==True:
            print("Cave ✓")
    if time_bed==False:
        print("Time Temple")
    if time_bed==True:
        print("Time Temple ✓")
    if secret_agent_bed==False:
        print("Vault ")
    if secret_agent_bed==True:
        print("Vault ✓")
    if gold_bed == False or aura_bed == False or magma_bed == False:
        print("Elemental Mountain")
    if gold_bed == True and aura_bed == True and magma_bed == True:
        print("Elemental Mountain ✓")
    if love_bed == True:
        print("Love Valley ✓")
    if love_bed == False:
        print("Love Valley")
    print("")
    print("")
    if day_time==True:
        print("Time: Day")
    if night_time==True:
        print("Time: Night")
    print("______________________________")
    print("commands:")
    print(" 1- Beds")
    print(" 2- Inventory")
    if bed_mixer == False:
        print(" 3- ????? - unlock using wheel spin")
    if bed_mixer == True:
        print(" 3- Bed Mixer")
    print(" 4- update Log")
    if win_mmm == False:
        print(" 5- ??????? - unlock by getting all beds")
    if win_mmm == True:
        print(" 5- Credits")
    if level_t==False:
        print(" 6- ?????? - Reach level 2")
    if level_t==True:
        print(" 6- Quests")
    print(" 7- Gem shop")
    print(" 8- Bed Center")
    print(" 9- Profile")
    print("10- Pause")
    print("______________________________")
    if levelexp > 1 and level_t == False:
        print("")
        print("You Leveled up to level 2!")
        print("")
        time.sleep(3.5)
        level_t = True
        levelexp = levelexp - 2
    if levelexp > 3 and level_th == False:
        print("")
        print("You Leveled up to level 3!")
        print("")
        time.sleep(3.5)
        level_th = True
        levelexp = levelexp - 4
    if levelexp > 9 and level_f == False:
        print("")
        print("You Leveled up to level 4!")
        print("")
        time.sleep(3.5)
        level_f = True
        levelexp = levelexp - 10
    if levelexp > 13 and level_fi == False:
        print("")
        print("You Leveled up to level 5!")
        print("")
        time.sleep(3.5)
        level_fi = True
        levelexp = levelexp - 14
    if levelexp > 18 and level_s == False:
        print("")
        print("You Leveled up to level 6!")
        print("")
        time.sleep(3.5)
        level_s = True
        levelexp = levelexp - 19
    if levelexp > 22 and level_se == False:
        print("")
        print("You Leveled up to level 7!")
        print("")
        time.sleep(3.5)
        level_se = True
        levelexp = levelexp - 23
    if levelexp > 26 and level_e == False:
        print("")
        print("You Leveled up to level 8!")
        print("")
        time.sleep(3.5)
        level_e = True
        levelexp = levelexp - 27
    if levelexp > 31 and level_n == False:
        print("")
        print("You Leveled up to level 9!")
        print("")
        time.sleep(3.5)
        level_n = True
        levelexp = levelexp - 32
    if levelexp > 36 and level_te == False:
        print("")
        print("You Leveled up to level 10!")
        print("")
        time.sleep(3.5)
        level_te = True
        levelexp = levelexp - 37
    if level_t==True and sjxuh == True:
        print("")
        print("Quests Unlocked! type (quests) to check it out")
        sjxuh=False
        time.sleep(3)
        print("")
    if rainbow_bed==True and q_o == False and callo == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callo=False
    if magical_bed==True and q_t == False and callt == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callt=False
    if winning_bed==True and q_th == False and callth == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callth=False
    if math_bed==True and scoresc==100 and q_f == False and callf == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callf=False
    if bed_winc >= 5 and q_fi == False and callfi == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callfi=False
    if combat_bed==True  and q_se == False and callse == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        callse=False
    if bed_winc >= 10 and q_e == False and calle == True:
        print("")
        print("you have finished a quest type (quests) to claim your prize!")
        print("")
        time.sleep(3)
        calle=False
    startbed = input("Type a command or a place to search. ")
        
    
    
    #capital and lowercase
    if startbed!=startbed.capitalize() or startbed==startbed.upper() or startbed==startbed.capitalize():
        startbed = startbed.lower()

    # quests
    if startbed == "quests" and level_t == False:
        print("")
        print("(Quests) Locked! Reach level 2 to unlock this command")
        time.sleep(3)
    if startbed == "quests" and level_t == True:
        print("")
        print("__________________________")
        if callo == False and doneo == False:
                doneo=True
                print("You completed a Easy Quest!")
                time.sleep(2)
                print("Obtained 2x gems")
                gems = gems + 2
                questcounter = questcounter + 1
                time.sleep(2)
        if callt == False and donet == False:
            donet=True
            print("You completed a Easy Quest!")
            time.sleep(2)
            print("Obtained 2x gems")
            gems = gems + 2
            questcounter = questcounter + 1
            time.sleep(2)
        if callth == False and doneth == False:
            doneth=True
            print("You completed a Medium Quest!")
            time.sleep(2)
            print("Obtained 3x gems")
            gems = gems + 3
            questcounter = questcounter + 1
            time.sleep(2)
        if callf == False and donef == False:
            donef=True
            print("You completed a Medium Quest!")
            time.sleep(2)
            print("Obtained 3x gems")
            gems = gems + 3
            questcounter = questcounter + 1
            time.sleep(2)
        if callfi == False and donefi == False:
            donefi=True
            print("You completed a Medium Quest!")
            time.sleep(2)
            print("Obtained 3x gems")
            gems = gems + 3
            questcounter = questcounter + 1
            time.sleep(2)
        if callse == False and donese == False:
            donese=True
            print("You completed a Hard Quest!")
            time.sleep(2)
            print("Obtained 5x gems")
            gems = gems + 5
            questcounter = questcounter + 1
            time.sleep(2)
        if calle == False and donef == False:
            donef=True
            print("You completed a Hard Quest!")
            time.sleep(2)
            print("Obtained 5x gems")
            gems = gems + 5
            questcounter = questcounter + 1
            time.sleep(2)
        if questcounter >= 5 and dones == False:
            dones=True
            print("You completed a Hard Quest!")
            time.sleep(2)
            print("Obtained 5x gems")
            gems = gems + 5
            time.sleep(2)
            print("")
            print("(Quest Bed) Unlocked! type (beds) to check out your collection")
            quest_bed=True
            bed_c = bed_c + 1
            levelexp = levelexp + 10
            questcounter = questcounter + 1
            time.sleep(3)
        print("")
        print("")
        print("Quests:")
        while 1:
            if level_t == True and rainbow_bed == False:
                print("1- Easy - lv.2 : Get the Rainbow bed (2 gems)")
            if level_t == True and rainbow_bed == True:
                print("1- Easy - lv.2 : Get the Rainbow bed (COMPLETED)")
            if level_th==False:
                print("2- Easy - lv.3 : (LOCKED)")
            if level_th == True and magical_bed == False:
                print("2- Easy - lv.3 : Get the Magical bed (2 gems)")
            if level_th == True and magical_bed == True:
                print("2- Easy - lv.3 : Get the Magical bed (COMPLETED)")
            if level_f==False:
                print("3- Medium - lv.4 : (LOCKED)")
                print("4- Medium - lv.4 : (LOCKED)")
            if level_f == True and winning_bed == False:
                print("3- Medium - lv.4 : Get the Winning bed (3 gems)")
            if level_f == True and winning_bed == True:
                print("3- Medium - lv.4 : Get the Winning bed (COMPLETED)")
            if level_f == True and math_bed==False:
                print("4- Medium - lv.4 : Get a 100% score in the school (3 gems)")
            if level_f == True and scoresc>=100 and math_bed==True:
                print("4- Medium - lv.4 Get a 100% score in the school (COMPLETED)")
            if level_f == True and scoresc < 100 and math_bed==True:
                print("4- Medium - lv.4 Get a 100% score in the school (FAILED)")
            if level_s==False:
                print("5- Medium - lv.6 : (LOCKED)")
                print("6- Hard - lv.6 : (LOCKED)")
            if level_s == True and bed_winc < 5:
                print("5- Medium - lv.6 : Win 5 Battles (3 gems)")
            if level_s == True and bed_winc >= 5:
                print("5- Medium - lv.6 : Win 5 battles (COMPLETED)")
            if level_s == True and questcounter < 5:
                print("6- Hard - lv.6 : Finish 5 Quests (3 gems + new bed)")
            if level_s == True and questcounter >=5:
                print("6- Hard - lv.6 : Finish 5 Quests (COMPLETED)")
            if level_se==False:
                print("7- Hard - lv.7 : (LOCKED)")
                print("8- Hard - lv.7 : (LOCKED)")
            if level_se == True and combat_bed == True:
                print("7- Hard - lv.7 : Get the Combat bed (COMPLETED)")
            if level_se == True and combat_bed==False:
                print("7- Hard - lv.7 : Get the Combat bed(5 gems)")
            if level_se == True and bed_winc < 10:
                print("8- Hard - lv.7 : Win 10 Battles (5 gems)")
            if level_se==True and bed_winc >= 10:
                print("8- Hard - lv.7 : Win 10 battles (COMPLETED)")
            print("____________________________________")
            print("type the number of any quest to get more info and see your progress")
            print("")
            print("back")
            print("________________________")
            quests = input("")
            if quests == "1":
                print("_________________________")
                print("Difficulty : Easy")
                print("Location : Bed Mixer")
                print("Obtain the rainbow bed")
                print("Level requirment : 2")
                print("Prize : 2 Gems")
                if rainbow_bed==True:
                    print("Quest Status: Completed")
                if level_t == False:
                    print("Quest Status: LOCKED")
                if rainbow_bed==False and level_t == True:
                    print("Quest Status: not completed")
                input("type anything to close...")
            if quests == "2":
                print("_________________________")
                print("Difficulty : Easy")
                print("Location : Bed Mixer")
                print("Obtain the magical bed")
                print("Level requirment : 3")
                print("Prize : 2 Gems")
                if magical_bed==True:
                    print("Quest Status: Completed")
                if level_th == False:
                    print("Quest Status: LOCKED")
                if magical_bed==False and level_th == True:
                    print("Quest Status: not completed")
                input("type anything to close...")
            if quests == "3":
                print("_________________________")
                print("Difficulty : Medium")
                print("Location : Bed Center > Battle district")
                print("Obtain the Winning bed")
                print("Level requirment : 4")
                print("Prize : 3 Gems")
                if winning_bed==True:
                    print("Quest Status: Completed")
                if level_f == False:
                    print("Quest Status: LOCKED")
                if winning_bed==False and level_f == True:
                    print("Quest Status: not completed")
                input("type anything to close...")
            if quests == "4":
                print("_________________________")
                print("Difficulty : Medium")
                print("Location : Bed Center > Battle district")
                print("Win 5 Battles in total")
                print("Level requirment : 4")
                print("Prize : 3 Gems")
                if bed_winc >= 5:
                    print("Quest Status: Completed")
                if level_f == False:
                    print("Quest Status: LOCKED")
                if bed_winc < 5 and level_f == True:
                    print("Quest Status: " + str(bed_winc) + "/5")
                input("type anything to close...")
            if quests == "5":
                print("_________________________")
                print("Difficulty : Medium")
                print("Location : School")
                print("Get a 100% in the school")
                print("Level requirment : 4")
                print("Prize : 3 Gems")
                if scoresc == 100:
                    print("Quest Status: Completed")
                if level_f == False:
                    print("Quest Status: LOCKED")
                if math_bed==False and level_f == True:
                    print("Quest Status: not completed")
                if math_bed==True and scoresc != 100:
                    print("Quest Status: FAILED")
                input("type anything to close...")
            if quests == "6":
                print("_________________________")
                print("Difficulty : Hard")
                print("Location : Quests")
                print("Finish 5 Quests")
                print("Level requirment : 6")
                print("Prize : 5 Gems")
                if questcounter >= 5:
                    print("Quest Status: Completed")
                if level_s == False:
                    print("Quest Status: LOCKED")
                if questcounter < 5 and level_s==True:
                    print("Quest Status: " + str(bed_winc) + "/5")
                input("type anything to close...")
            if quests == "7":
                print("_________________________")
                print("Difficulty : Hard")
                print("Location : Bed Center > Shopping district")
                print("Buy the Combat bed")
                print("Level requirment : 4")
                print("Prize : 5 Gems")
                if combat_bed==True:
                    print("Quest Status: Completed")
                if level_se == False:
                    print("Quest Status: LOCKED")
                if combat_bed==False and level_se==True:
                    print("Quest Status: not completed")
                input("type anything to close...")
            if quests == "8":
                print("_________________________")
                print("Difficulty : Hard")
                print("Location : Bed Center > Battle district")
                print("Win 10 Battles in total")
                print("Level requirment : 4")
                print("Prize : 3 Gems")
                if bed_winc >= 10:
                    print("Quest Status: Completed")
                if level_se == False:
                    print("Quest Status: LOCKED")
                if bed_winc < 10 and level_se==True:
                    print("Quest Status: " + str(bed_winc) + "/10")
                input("type anything to close...")
            if quests == "back":
                print("")
                print("Closing Quests...")
                print("")
                print("")
                time.sleep(1.2)
                break
                
    if startbed == "gem shop":
        while 1:
            print("")
            print("")
            print("")
            print("Gem Shop___________________________________")
            print("Gems: " + str(gems))
            print("")
            print("Chance Multiplier        10 Gems     Retrieve Items")
            print("Prize Multiplier         12 Gems")
            print("3 more items coming soon!")
            print("")
            print("")
            print("Retrieve Items")
            print("close")
            print("What do you want to do/buy?")
            gemshopbuy = input("")
            if gemshopbuy!=gemshopbuy.capitalize() or gemshopbuy==gemshopbuy.upper() or gemshopbuy==gemshopbuy.capitalize():
                gemshopbuy = gemshopbuy.lower()
            if gemshopbuy == "retrieve items":
                print("")
                print("")
                print("Insert 15 Characters Code")
                itemcode = input("")
                if itemcode=="125634341578901" and chancem==True:
                    print("")
                    print("Code Already Redeemed...")
                    time.sleep(2)
                if itemcode=="125634341578901" and chancem==False:
                    print("")
                    print("Chance Multiplier Redeemed!")
                    time.sleep(2)
                    print("(Chance Multiplier) Unlocked!")
                    time.sleep(2)
                    chancem = True
                if itemcode=="155860441558511" and prizem==True:
                    print("")
                    print("Code Already Redeemed...")
                    time.sleep(2)
                if itemcode=="155860441558511" and prizem == False:
                    print("")
                    print("Prize Multiplier Redeemed!")
                    time.sleep(2)
                    print("(Prize Multiplier) Unlocked!")
                    time.sleep(2)
                    prizem = True
                
            if gemshopbuy == "close":
                print("")
                print("closing gem shop...")
                time.sleep(1.2)
                break
            if gemshopbuy == "prize multiplier" and prizem == True:
                print("")
                print("Item Already Obtained...")
                time.sleep(2)
            if gemshopbuy == "prize multiplier" and prizem == False:
                while 1:
                    print("___________________________________")
                    print("Item: Prize Multiplier")
                    print("Price: 12 Gems")
                    print("Discription: Multiplies Prizes by 2")
                    print("")
                    print("Do you want to buy a Prize Multiplier? (yes/no)")
                    hahabuymulti = input("")
                    if hahabuymulti=="yes" and gems < 12:
                        print("")
                        print("ERROR")
                        time.sleep(2)
                        print("Insufficient Gems")
                        time.sleep(2)
                    if hahabuymulti == "yes" and gems >=12:
                        print("")
                        print("Prize Multiplier Purchased!")
                        time.sleep(2)
                        print("(Prize Multiplier) Unlocked!")
                        time.sleep(3)
                        print("PLEASE DO NOT SHARE THIS CODE")
                        print("Retrieval Code: 155860441558511")
                        time.sleep(3)
                        gems = gems - 12
                        prizem = True
                        break
                    if hahabuymulti == "no":
                        break
            if gemshopbuy == "chance multiplier" and chancem == True:
                print("")
                print("Item Already Obtained...")
                time.sleep(2)
            if gemshopbuy == "chance multiplier" and chancem == False:
                while 1:
                    print("___________________________________")
                    print("Item: Chance Multiplier")
                    print("Price: 10 Gems")
                    print("Discription: Multiplies the chances to get something by 2")
                    print("")
                    print("Do you want to buy a Chance Multiplier? (yes/no)")
                    hahabuymulti = input("")
                    if hahabuymulti=="yes" and gems < 10:
                        print("")
                        print("ERROR")
                        time.sleep(2)
                        print("Insufficient Gems")
                        time.sleep(2)
                        break
                    if hahabuymulti == "yes" and gems >=10:
                        print("")
                        print("Chance Multiplier Purchased!")
                        time.sleep(2)
                        print("(Chance Multiplier) Unlocked!")
                        time.sleep(3)
                        print("PLEASE DO NOT SHARE THIS CODE")
                        print("Retrieval Code: 125634341578901")
                        time.sleep(3)
                        gems = gems - 10
                        chancem = True
                        break
                    if hahabuymulti == "no":
                        break

    # inventory
    if startbed == "inventory":
        while 1:
            print("")
            print("")
            print("Inventory:")
            print("")
            if gems==0 and books==False and lcards==0 and fire==0 and firea == 0 and water == 0 and air == 0 and plant == 0 and earth == 0 and bp == 0 and garbage_one == False and garbage_two == False and garbage_three == False and nuclear_one == False and nuclear_two == False and rocket_fuel == False:
                print("So empty here ;-;")
            if bp != 0:
                print("Battle Points: " + str(bp))
            if gems != 0:
                print("Gems: " + str(gems))
            if garbage_one == True and garbage_two == False and garbage_three == False:
                print("Garbage x1")
            if garbage_one == True and garbage_two == True and garbage_three == False:
                print("Garbage x2")
            if garbage_one == True and garbage_two == True and garbage_three == True:
                print("Garbage x3")
            if nuclear_one == True and nuclear_two == False:
                print("Nuclear  Fuel x1")
            if nuclear_one == True and nuclear_two == True:
                print("Nuclear Fuel x2")
            if rocket_fuel == True:
                print("Rocket Fuel x1")
            if fire != 0:
                print("Fire Matter x" + str(fire))
            if water != 0:
                print("Water Matter x" + str(water))
            if plant != 0:
                print("Plant Matter x" + str(plant))
            if firea != 0:
                print("Fire Aura x" + str(firea))
            if air != 0:
                print("Air Aura x" + str(air))
            if earth != 0:
                print("Earth Aura x" + str(earth))
            if lcards != 0:
                print("L card x" + str(lcards))
            if books == True:
                print("Math Book x1")
            print("")
            print("")
            print("type the name of any item to check it out")
            inv = input("and if your Done type (back)")
            if inv!=inv.capitalize() or inv==inv.upper() or inv==inv.capitalize():
                inv = inv.lower()
            if inv == "garbage" and garbage_one == True:
                print("")
                if garbage_two == False:
                    print("Garbage x1")
                if garbage_one==True and garbage_two == True and garbage_three == False:
                    print("Garbage x2")
                if garbage_three==True:
                    print("Garbage x3")
                print("_________________________")
                print("Garbage that stinks, although I heard of a bed made of garbage...")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "nuclear fuel" and nuclear_one == True:
                print("")
                if nuclear_one == True and nuclear_two == False:
                    print("Nuclear Fuel x1")
                if nuclear_one == True and nuclear_two == True:
                    print("Nuclear Fuel x2")
                print("_________________________")
                print("a very expensive and dangerous kind of fuel its used for destruction but rumors say you can form a very destructive bed using it")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "rocket fuel" and rocket_fuel == True:
                print("")
                print("Rocket Fuel")
                print("_________________________")
                print("fuel used for rockets")
                print("")
                print("_________________________")
                print("use")
                print("type anything else to close")
                print("")
                inventoryback = input("")
                if inventoryback == "use" and rocket_bed_Fb == True:
                    print("")
                    print("Rocket bed is already charged...")
                    time.sleep(2.5)
                if inventoryback == "use" and rocket_bed_E == False:
                    print("")
                    print("it seems like I need a rocket to use the fuel on...")
                    time.sleep(2.5)
                if inventoryback == "use" and rocket_bed_E == True and rocket_bed_Fb==False:
                    print("")
                    print("you filled up the rocket's tank...")
                    time.sleep(2)
                    print("ROCKET BED CHARGED!")
                    time.sleep(2.5)
                    print("")
                    print("(Rocket Bed - Charged) Unlocked! type (beds) to check out your collection")
                    time.sleep(3)
                    rocket_bed_Fb=True
                    rocket_bed_F = True
                    bed_c = bed_c + 1
                    levelexp = levelexp + 5
            if inv == "l card" and lcards !=0:
                print("")
                print("L card x" + str(lcards))
                print("_________________________")
                print("A card that can be filled up with text its usually used at love valley")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "fire matter" and fire !=0:
                print("")
                print("Fire Matter x" + str(fire))
                print("_________________________")
                print("A matter that can be mixed with other matters to form a aura")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "battle points" and bp !=0:
                print("")
                print("Battle Points x" + str(bp))
                print("_________________________")
                print("Points gained from winning bed battles they can be used in the shopping district to buy some items!")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "water matter" and water !=0:
                print("")
                print("Water Matter x" + str(water))
                print("_________________________")
                print("A matter that can be mixed with other matters to form a aura")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "plant matter" and plant !=0:
                print("")
                print("Plant Matter x" + str(plant))
                print("_________________________")
                print("A matter that can be mixed with other matters to form a aura")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "fire aura" and firea !=0:
                print("")
                print("Fire Aura x" + str(firea))
                print("_________________________")
                print("An aura that can be mixed with other auras to form beds")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "air aura" and air !=0:
                print("")
                print("Air Aura x" + str(air))
                print("_________________________")
                print("An aura that can be mixed with other auras to form beds")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "earth aura" and earth !=0:
                print("")
                print("Earth Aura x" + str(earth))
                print("_________________________")
                print("An aura that can be mixed with other auras to form beds")
                print("")
                print("_________________________")
                print("")
                print("type anything to close")
                print("")
                inventoryback = input("")
            if inv == "math book" and books == True:
                print("")
                print("Math Book")
                print("_________________________")
                print("An book obtained from the math-only school its used for revising for there final tests")
                print("")
                print("_________________________")
                print("use")
                print("type anything else to close")
                print("")
                inventoryback = input("")
                if inventoryback=="use":
                    pagesmath=1
                    while 1:
                         if pagesmath==2:
                             print("")
                             print("")
                             print("Math Book : 2/2")
                             print("")
                             print("Practice:")
                             print("")
                             print("1 x 1 = 1")
                             print("cause this means 1 of 1")
                             print("")
                             print("1 x 2 = 2")
                             print("cause this means 1 of 2")
                             print("")
                             print("2 x 1 = 2")
                             print("cause this means 2 of 1 or 1 and 1 which is 2")
                             print("")
                             print("back")
                             print("close")
                         if pagesmath==1:
                             print("")
                             print("")
                             print("Math Book : 1/2")
                             print("_________________________________")
                             print("")
                             print("Multiplication - First Lesson")
                             print("")
                             print("multiplication is like addition but instead of repeating the addition you can just do it in a simple way")
                             print("")
                             print("Example:")
                             print("instead of 2 + 2 + 2 + 2")
                             print("we do 2 x 4 its the excact same thing")
                             print("2 x 4 means 2 + 2 4 times")
                             print("")
                             print("2 + 2 + 2 + 2 = 8")
                             print("")
                             print("2 x 4 = 8")
                             print("")
                             print("next page")
                             print("close")
                         pagescroll = input("")
                         if pagescroll=="close":
                             pagesmath = 1
                             break
                         if pagescroll=="back" and pagesmath==2:
                             pagesmath = 1
                         if pagescroll=="next page" and pagesmath==1:
                             pagesmath = 2
                            
            if inv == "back":
                print("")
                print("Closing Inventory...")
                print("")
                print("")
                time.sleep(1.2)
                break

    # update log
    if startbed == "update log":
        print("")
        print("")
        print("________________________________________________")
        print("Version 1.7 Update Log (MAJOR UPDATE)-")
        print("")
        print("")
        print("New Searching Location (love valley)")
        print("New searching location (Vault)")
        print("New command (gem shop)")
        print("New command (profile)")
        print("New command (pause)")
        print("")
        print("2 new beds")
        print("2 new Battle beds")
        print("")
        print("reworked (sleep)")
        print("reworked (school and buffed math bed)")
        print("reworked (bed mixer)")
        print("reworked (quests)")
        print("reworked (Quest Bed)")
        print("")
        print("Added Day and night!")
        print("Added many quality of life changes!")
        print("Added Levels!")
        print("Added a New way to obtain the quest bed!")
        print("")
        print("")
        print("")
        print("Quest rework - You will have to level up to level 2 to unlock the command now. to level up you need to unlock more beds. progress will be shown in the profile. after this you do some quests that make you get gems. those gems can be used in the gem shop to buy some items that drastically boost your progress and they can be retrieved back using the code that comes while purchasing the items so you can redeem them and use them any time even if you restart the game. to get the quest bed you have to finish any 5 quests.")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("and more small changes")
        print("")
        print("")
        
        print("")
        print("Enjoy the update!")
        
        print("")
        input("Done Reading? type anything to close")
        print("")

    # credits
    if startbed == "credits" and win_mmm == True:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Find")
        time.sleep(0.8)
        print(" The")
        time.sleep(1.2)
        print("  BEDS")
        time.sleep(2)
        print("")
        print("")
        print("Made by (AbedGamez)")
        time.sleep(3)
        print("")
        print("Idea taken from Roblox: Find the markers")
        print("")
        time.sleep(3)
        print("Youtube : https://m.youtube.com/c/AbedGamez")
        print("")
        time.sleep(3)
        print("Discord : https://discord.gg/jSjv9mzXdm")
        print("")
        time.sleep(3)
        print("")
        time.sleep(3)
        print("")
        print("And again congratulations!!")
        time.sleep(3)
        print("")
        print("Made in the 18th of September 2022")
        time.sleep(3)
        print("")
        print("Find")
        time.sleep(0.8)
        print(" The")
        time.sleep(1.2)
        print("  BEDS")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

    if startbed == "credits" and win_mmm == False:
        print("")
        print("(Credits) Locked! try typing it again after getting all of the beds!!")
        print("")
        print("")
        time.sleep(2)
    
    
    #profile
    if startbed=="profile":
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Player Profile:______________________")
        print("Name: " + name)
        print("Beds: " + str(bed_c) + "/36")
        if level_t == False:
            print("Level: 1 (" + str(levelexp) + "/2)")
        if level_t == True and level_th == False:
            print("Level: 2 (" + str(levelexp) + "/4)")
        if level_th == True and level_f == False:
            print("Level: 3 (" + str(levelexp) + "/10)")
        if level_f == True and level_fi == False:
            print("Level: 4 (" + str(levelexp) + "/14)")
        if level_fi == True and level_s == False:
            print("Level: 5 (" + str(levelexp) + "/19)")
        if level_s == True and level_se == False:
            print("Level: 6 (" + str(levelexp) + "/23)")
        if level_se == True and level_e == False:
            print("Level: 7 (" + str(levelexp) + "/27)")
        if level_e == True and level_n == False:
            print("Level: 8 (" + str(levelexp) + "/32)")
        if level_n == True and level_te == False:
            print("Level: 9 (" + str(levelexp) + "/37)")
        if level_te == True and level_el == False:
            print("Level: 10 (" + str(levelexp) + "/43) MAX LEVEL")
        print("Battle Points: " + str(bp))
        print("Gems: " + str(gems))
        print("Battles won: " + str(bed_winc))
        print("_____________________________________")
        print("")
        print("")
        print("")
        print("")
        input("Done reading? type anything to close")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        
        
    
    
    # pause
    if startbed == "pause":
        print("Pausing game...")
        time.sleep(2.2)
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        pauseaskk=True
        while pauseaskk==True:
            print("Find")
            print(" The")
            print("  BEDS")
            print("Version 1.7")
            print("_______________")
            print("continue")
            print("close")
            pauseask=input("What do you want to do?")
            print("")
            print("")
            print("")
            if pauseask=="close":
                    print("Game Closed!")
                    time.sleep(1.2)
                    closegamesure=False
                    pauseaskk=False
                        
                
            if pauseask=="continue":
                print("continuing Game...")
                time.sleep(2.2)
                print("")
                print("")
                print("")
                print("")
                break
    #love valley
    if startbed == "love valley" and love_bed == True:
        print("")
        print("i have the love bed i think am good")
    if startbed=="love valley" and love_bed == False:
        print("")
        print("You have entered the love valley")
        time.sleep(2)
        if freelcard==True:
            if prizem==True:
                print("you obtained 4x L cards as a gift for entering for the first time!")
                lcards = lcards + 4
            if prizem==False:
                print("you obtained 2x L cards as a gift for entering for the first time!")
                lcards = lcards + 2
            time.sleep(5)
            print("Gaurd: Hey! Can you help us!")
            time.sleep(3)
            print("Gaurd: The kids in our valley are crying so loudly can you use your L cards to make them happy? I promise i will award you")
            time.sleep(8.5)
            print("")
            print("*you accepted the mission*")
            freelcard = False
            kidsleft=5
            lovealready = False
        while 1:
            print("")
            print("")
            print("Kids Left: " + str(kidsleft))
            print("_______________")
            print("fill cards")
            print("give cards")
            print("back")
            lovevalleyask = input("")
            if lovevalleyask=="back":
                print("")
                print("you got out of love valley")
                time.sleep(2.2)
                break
            if lovevalleyask=="fill cards" and lcards == 0:
                print("")
                print("you have 0 L cards buy more from the bed center!")
                time.sleep(3)
                print("")
            if lovevalleyask=="fill cards" and lovealready == True and lcards >= 1:
                    print("")
                    print("you can fill 1 card in total giveaway your previous one to fill a new one")
                    time.sleep(3)
            if lovevalleyask=="fill cards" and lcards >= 1 and lovealready == False:
                while 1:
                    print("cards left to fill: " + str(lcards))
                    print("")
                    print("type your love message:")
                    print("")
                    lovefill=input("")
                    if lovefill.count("") < 6:
                        print("")
                        print("the kids wont like the card its too short")
                        time.sleep(3)
                    if lovefill.count("") <= 30 and lovefill.count("") > 6:
                        print("")
                        print("the kids should like that")
                        time.sleep(2)
                        loveinsidec = lovefill
                        lovealready = True
                        lcards = lcards - 1
                        break
            if lovevalleyask=="give cards" and lovealready==False:
                print("")
                print("you didnt fill any card..")
                time.sleep(3)
            if lovevalleyask == "give cards" and kidsleft==0:
                print("Gaurd: 0 kids are left thanks for helping!")
            if lovevalleyask == "give cards" and lovealready==True and kidsleft>=1:
                print("")
                print("you went to one of the kids")
                time.sleep(3)
                print("you gave him a L card")
                time.sleep(2.5)
                print("")
                print("Kid: lemme read it...")
                time.sleep(3)
                print("Kid: " + lovefill + "...")
                time.sleep(6)
                print("Kid: I like it! THANK YOU :)")
                time.sleep(4)
                print("")
                print("")
                lovealready=False
                kidsleft = kidsleft - 1
            if kidsleft==0 and love_bed==False:
                print("")
                print("Gaurd: Thank you sir here is your reward as promised")
                time.sleep(2)
                print("")
                print("(Love Bed) Unlocked! type (beds) to check out your collection!")
                bed_c = bed_c + 1
                bed_cvr = bed_cvr + 1
                levelexp = levelexp + 7
                love_bed=True
                time.sleep(3)
    
    #Vault
    if startbed == "vault" and secret_agent_bed==True:
        print("")
        print("")
        print("")
        print("the vault is already unlocked...")
        time.sleep(5)
    if startbed == "vault" and secret_agent_bed==False:
        print("")
        print("")
        print("")
        print("you found a locked vault")
        time.sleep(5)
        print("it appears it can be unlocked using a 10 digit secret code...")
        time.sleep(6)
        print("you tried to search for hints..")
        time.sleep(4)
        while 1:
            print("")
            print("")
            print("")
            print("locations:")
            print("lab")
            print("floor")
            print("board")
            print("insert")
            vaultchoose = input("choose a location... | ")
            if vaultchoose == "lab":
                print("")
                print("you went to the lab")
                print("First Hint:")
                print("- 2 - 5 - - 7 - - -")
                input("Done? type anything to go back")
            if vaultchoose == "floor":
                print("")
                print("you went to the lab")
                print("Second Hint:")
                print("7 - - - - - - - 8 9")
                input("Done? type anything to go back")
            if vaultchoose == "board":
                print("")
                print("you went to the lab")
                print("Second Hint:")
                print("- - 6 - 6 4 - 1 - -")
                input("Done? type anything to go back")
            if vaultchoose == "insert":
                print("")
                print("insert 10 digit code")
                print("__________________________")
                vaulti = input("")
                if vaulti=="7265647189":
                    print("")
                    print("")
                    print("Access Granted!")
                    time.sleep(3)
                    print("you found a bed!")
                    time.sleep(2.5)
                    print("")
                    print("(Secret Agent Bed) Unlocked! type (beds) to check out your collection!")
                    time.sleep(3)
                    secret_agent_bed=True
                    bed_c = bed_c + 1
                    bed_cvr = bed_cvr + 1
                    levelexp = levelexp + 10
                    break
                else:
                    print("")
                    print("")
                    print("WRONG!")
                    time.sleep(1.8)
                    
                
        
        
    # sleep
    if startbed == "sleep" and magical_bed == False and bed_c < 1:
        print("")
        print("Looks like I need a bed to sleep on...")
        time.sleep(1.2)
    if startbed == "sleep" and dream_bed == True:
        print("")
        print("*you slept on your dream bed*")
        time.sleep(2.5)
        time.sleep(1.5)
        print("")
        print("")
        daynightchanger = ["day", "day", "day", "night", "night"]
        dtchangerr = random.choice(daynightchanger)
        if dtchangerr=="night" and night_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still night time... ")
            time.sleep(4)
        if dtchangerr=="day" and day_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still day time... ")
            time.sleep(4)
        if dtchangerr=="night" and night_time==False:
            print("you slept for 9 hours....")
            time.sleep(1)
            print("its night time!")
            time.sleep(4)
            day_time=False
            night_time=True
        if dtchangerr=="day" and day_time==False:
            print("you slept for 13 hours....")
            time.sleep(1)
            print("its day time!")
            time.sleep(4)
            day_time=True
            night_time=False
    if startbed == "sleep" and magical_bed == False and bed_c == 1:
        print("")
        print("")
        print("*you slept on your bed*")
        time.sleep(2.5)
        print("")
        time.sleep(1.5)
        print("")
        print("")
        daynightchanger = ["day", "day", "day", "night", "night"]
        dtchangerr = random.choice(daynightchanger)
        if dtchangerr=="night" and night_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still night time... ")
            time.sleep(4)
        if dtchangerr=="day" and day_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still day time... ")
            time.sleep(4)
        if dtchangerr=="night" and night_time==False:
            print("you slept for 9 hours....")
            time.sleep(1)
            print("its night time!")
            time.sleep(4)
            day_time=False
            night_time=True
        if dtchangerr=="day" and day_time==False:
            print("you slept for 13 hours....")
            time.sleep(1)
            print("its day time!")
            time.sleep(4)
            day_time=True
            night_time=False
    if startbed == "sleep" and magical_bed == False and bed_c >= 2:
        print("")
        print("")
        print("*you slept on one of your beds*")
        print("")
        time.sleep(2.5)
        print("")
        print("")
        daynightchanger = ["day", "day", "day", "day", "night"]
        dtchangerr = random.choice(daynightchanger)
        if dtchangerr=="night" and night_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still night time... ")
            time.sleep(4)
        if dtchangerr=="day" and day_time==True:
            print("you got a nightmare and woke up intantly")
            time.sleep(1)
            print("its still day time... ")
            time.sleep(4)
        if dtchangerr=="night" and night_time==False:
            print("you slept for 9 hours....")
            time.sleep(1)
            print("its night time!")
            time.sleep(4)
            day_time=False
            night_time=True
        if dtchangerr=="day" and day_time==False:
            print("you slept for 13 hours....")
            time.sleep(1)
            print("its day time!")
            time.sleep(4)
            day_time=True
            night_time=False
    if startbed == "sleep" and magical_bed == True and dream_bed == False:
        print("")
        print("")
        print("*you slept on your magical bed*")
        print("")
        time.sleep(2.5)
        print("*you started dreaming*")
        time.sleep(1.5)
        if chancem==False:
            dream = ['night', 'night', 'dream', 'dream', 'dream']
        if chancem==True:
            dream = ['dream', 'dream', 'dream', 'dream', 'dream']
        dreamr = random.choice(dream)
        dreamj = "".join(dreamr)
        print("")
        if dreamj == "night":
            print("NIGHTMARE!!!")
            time.sleep(1.2)
            print("a monster showed up and ate you...")
            time.sleep(1.5)
            print("*you waked up...*")
            time.sleep(0.8)
            if night_time==True:
                print("its still night time")
            if day_time==True:
                print("its still day time")
        if dreamj == "dream":
            print("")
            print("*your dream was so fun and peaceful*")
            print("")
            time.sleep(1.5)
            print("you were in a village with monsters attacking!!")
            time.sleep(1.5)
            print("you shooted them and defeated them")
            time.sleep(1.5)
            print("and everyone cheered up with your name!!")
            time.sleep(1.5)
            print("*you waked up and found a dream bed next to you!!*")
            time.sleep(1.5)
            print("(Dream Bed) Unlocked! type (beds) to check out your collection!")
            dream_bed = True
            bed_c = bed_c + 1
            bed_cvr = bed_cvr + 1
            levelexp = levelexp + 7
            time.sleep(3)
            if night_time==True:
                print("its still night time")
                print("")
                time.sleep(2.5)
            if day_time==True:
                print("its still day time")
                print("")
                time.sleep(2.5)

    # road
    if startbed == "road" and car_bed == False:
        print("")
        print("hmm it looks like i need a car...")
        print("")
        time.sleep(2)
    if startbed == "road" and stray_bed == True:
        print("")
        print("i dont wanna drive again maybe i will go search the new locations i found out about")
        time.sleep(4)
    if startbed == "road" and car_bed == True and stray_bed == False:
        print("")
        print("*you hopped on your car bed*")
        time.sleep(2)
        print("you started driving")
        time.sleep(2)
        print("You found a MASSIVE dumpster...")
        time.sleep(3)
        print("you found a math only school...")
        time.sleep(3)
        print("you found a tree with a questionable size")
        time.sleep(3)
        print("")
        print("you found a stray poor bed")
        time.sleep(2)
        print("(Stray Bed) Unlocked! type (beds) to checkout your collection!")
        time.sleep(3)
        print("")
        print("search areas (school,tree,dumpster) Unlocked! type (school) or (tree) or (dumpster) to check them out")
        time.sleep(6)
        print("")
        road = True
        stray_bed = True
        bed_c = bed_c + 1
        levelexp = levelexp + 5
        
        
        
        
        
        
        
        
        
        
        
        

    # school
    if startbed == "school" and stray_bed == True and math_bed == True:
        print("")
        print("Welcome you already have gotten a math bed you cant obtain a new one sorry :)")
        time.sleep(4)
        print("")
    if startbed == "school" and stray_bed == False:
        print("")
        print("What School??")
        time.sleep(2)
    if startbed == "school" and stray_bed == True and math_bed == False and schoolsignup==False:
        print("")
        print("Welcome to the math only school")
        print("")
        time.sleep(2)
        print("I think your here for the bed that only smart people can have")
        time.sleep(2.4)
        print("")
        print("in that case you can join our school")
        print("and its totally free :>")
        time.sleep(5)
        while 1:
            enterschool = input("do you wanna join? (yes/no)")
            if enterschool=="yes":
                print("Alright!")
                time.sleep(2)
                print("so school will be open every day at daytime... getting a 85%+ score will award you a math bed")
                time.sleep(3)
                print("")
                print("")
                print("school starts tommorow cya!")
                time.sleep(6)
                schoolsignup=True
                night_time=True
                day_time=False
                break
            if enterschool=="no":
                print("Alright!")
                time.sleep(1.5)
                break
    if startbed=="school" and stray_bed==True and schoolsignup==True and math_bed == False and day_time==True:
        print("")
        print("")
        if day_final==True:
            print("")
            print("here it is")
            time.sleep(1.5)
            print("the day where you will be testing your self to see if your worthy of having the most intelligent bed ever")
            time.sleep(6.5)
            print("THE MATH BED!!")
            time.sleep(3)
            print("")
            print("Test starts NOW")
            time.sleep(2)
            print("")
            print("")
            print("")
            scoresc = 0
            print("Name: " + name)
            print("Score 0/100")
            print("you should get a 85%+ score to pass!")
            time.sleep(5)
            print("")
            print("")
            print("")
            print("Question 1/8")
            print("3 x 4")
            qonet = input("Answer: ")
            if qonet=="12":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 15
            if qonet!="12":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 2/8")
            print("4 x 7")
            qonet = input("Answer: ")
            if qonet=="28":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 15
            if qonet!="28":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 3/8")
            print("1 x 2 x 3")
            qonet = input("Answer: ")
            if qonet=="6":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 10
            if qonet!="6":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 4/8")
            print("2 x 2 x 3")
            qonet = input("Answer: ")
            if qonet=="12":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 15
            if qonet!="12":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 5/8")
            print("6 x 5")
            qonet = input("Answer: ")
            if qonet=="30":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 10
            if qonet!="30":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 6/8")
            print("3 x 3")
            qonet = input("Answer: ")
            if qonet=="9":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 10
            if qonet!="9":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 7/8")
            print("2 x 4")
            qonet = input("Answer: ")
            if qonet=="8":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 10
            if qonet!="8":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("")
            print("Question 8/8")
            print("6 x 3")
            qonet = input("Answer: ")
            if qonet=="18":
                print("Correct!")
                time.sleep(2)
                scoresc = scoresc + 15
            if qonet!="18":
                print("Wrong!")
                time.sleep(2)
            print("")
            print("Alright here are the final results!")
            print("Name: " + name)
            print("Score: " + str(scoresc) + "/100")
            print("")
            if scoresc < 85:
                print("You Failed!")
                time.sleep(2)
                print("Come Back Tommorow To Retry...")
                night_time = True
                day_time = False
            if scoresc >= 85:
                print("You Passed!")
                time.sleep(2)
                print("here is your reward")
                print("")
                print("")
                time.sleep(2)
                print("(Math Bed) Unlocked! type (beds) to check out your collection")
                time.sleep(3)
                print("")
                print("Goodbye!")
                time.sleep(1.5)
                math_bed = True
                levelexp=levelexp+7
        if day_one==True:
            print("")
            time.sleep(4)
            print("")
            print("so first of all we will have 2 days of school this one being the first")
            print("so each student will recieve a math book you will have to revise it very well so you can pass the final test tommorow")
            input("type anything to continue...")
            print("")
            print("obtained 1x Math Book")
            time.sleep(2.5)
            books = True
            print("")
            print("that was it for today revise well for tommorow!")
            time.sleep(3)
            night_time = True
            day_time = False
            day_one = False
            day_final = True
            
            
        







    # tree
    if startbed == "tree" and stray_bed == True and apple_bed == True:
        print("")
        print("ALL ITEMS OBTAINED...")
        print("")
        time.sleep(2)
    if startbed == "tree" and stray_bed == False:
        print("")
        print("what tree??")
        time.sleep(2)
    if startbed == "tree" and stray_bed == True and apple_bed == False:
        print("")
        print("you hopped on your car bed and drove to the tree...")
        print("")
        time.sleep(3)
        print("Possible finds :")
        if chancem == False:
            print("NEW BED: 30%")
            print("Re Shake : 50%")
            print("nothing : 20%")
        if chancem==True:
            print("NEW BED: 60%")
            print("Re Shake : 30%")
            print("nothing : 10%")
        time.sleep(3)
        while 1:
            print("")
            print("*you shaked the tree*")
            print("")
            time.sleep(1.5)
            if chancem==False:
                tree = ['nothing', 're shake', 're shake', 're shake', 're shake', 're shake', 'nothing', 'apple bed', 'apple bed', 'apple bed']
            if chancem==True:
                tree = ['nothing', 're shake', 're shake', 're shake', 'apple bed', 'apple bed', 'apple bed', 'apple bed', 'apple bed', 'apple bed']
            treer = random.choice(tree)
            treej = "".join(treer)
            print(treej + "!")
            time.sleep(1.2)
            if treej == "apple bed":
                print("")
                print("the tree dropped an apple bed")
                print("")
                print("(Apple Bed) Unlocked! Type (beds) to check out your collection!")
                print("")
                time.sleep(3)
                apple_bed = True
                bed_c = bed_c + 1
                bed_cvr = bed_cvr + 1
                levelexp=levelexp+7
                break
            if treej == "nothing":
                print("")
                print("you accidentally broke the trunk while shaking and nothing dropped..")
                time.sleep(2)
                print("")
                print("you planted the tree again...")
                print("")
                time.sleep(1.5)
                print("You waited  until the tree growed again...")
                time.sleep(10)
                print("")
                print("The tree grew back up!! lets shake it again!!")
                time.sleep(1.5)
            if treej == "re shake":
                print("")
                print("you got nothing although luckily the trunk didnt break and you can reshake it!!")
                time.sleep(1)

    # dumpster
    if startbed == "dumpster" and stray_bed == True and garbage_three == True and dirty_bed == True:
        print("")
        print("ALL ITEMS OBTAINED...")
        print("")
        time.sleep(2)
    if startbed == "dumpster" and stray_bed == False:
        print("")
        print("what dumpster??")
        time.sleep(2)
    if startbed == "dumpster" and stray_bed == True and dirty_bed == False or garbage_three == False and stray_bed == True and startbed == "dumpster":
        print("")
        print("you hopped on your car bed and drove to the dumpster...")
        print("")
        time.sleep(3)
        if chancem==False:
            print("Possible finds :")
            print("Garbage : 40%")
            print("NEW BED : 40%")
            print("rotten food : 20%")
        if chancem==True:
            print("Possible finds :")
            print("Garbage : 50%")
            print("NEW BED : 50%")
        time.sleep(3)
        while 1:
            print("")
            print("*you searched the dumpster*")
            print("")
            time.sleep(1.5)
            if chancem == False:
                dumpster = ['rotten food', 'dirty bed', 'dirty bed', 'garbage', 'garbage']
            if chancem == True:
                dumpster = ['dirty bed', 'garbage']
            dumpsterr = random.choice(dumpster)
            dumpsterj = "".join(dumpsterr)
            print("you found a " + dumpsterj)
            if dumpsterj == "rotten food":
                time.sleep(1)
                print("")
                print("ewww..")
                print("")
                time.sleep(2)
                break
            if dumpsterj == "dirty bed" and dirty_bed == True:
                time.sleep(1)
                print("")
                print("Eh, I already have that...")
                print("")
                time.sleep(2)
                break
            if dumpsterj == "dirty bed" and dirty_bed == False:
                time.sleep(1)
                print("")
                print("(Dirty Bed) Unlocked! type (beds) to check out your collection!")
                print("")
                time.sleep(3)
                dirty_bed = True
                bed_c = bed_c + 1
                bed_cvr = bed_cvr + 1
                levelexp=levelexp+7
                break
            if dumpsterj == "garbage" and garbage_three == True:
                time.sleep(1)
                print("")
                print("You have the maximum count of garbage")
                print("")
                time.sleep(1.8)
                break
            if dumpsterj == "garbage" and garbage_two == True and garbage_one == True and garbage_three == False:
                time.sleep(1)
                print("")
                print("1x Garbage Stored.")
                print("")
                time.sleep(2.4)
                garbage_three = True
                break
            if dumpsterj == "garbage" and garbage_one == True and garbage_two == False:
                time.sleep(1)
                print("")
                print("1x Garbage Stored.")
                print("")
                time.sleep(2.4)
                garbage_two = True
                break
            if dumpsterj == "garbage" and garbage_one == False:
                time.sleep(1)
                print("")
                if chancem==False:
                    print("1x Garbage Stored.")
                    print("")
                    time.sleep(2.4)
                    garbage_one = True
                if chancem==True:
                    print("2x Garbage Stored.")
                    print("")
                    time.sleep(2.4)
                    garbage_one = True
                    garbage_two = True
                break
            if dumpsterj == "garbage" and garbage_one == True and garbage_two == False:
                time.sleep(1)
                print("")
                print("1x Garbage Stored.")
                print("")
                time.sleep(2.4)
                garbage_two = True
                break
            if dumpsterj == "garbage" and garbage_two == True and garbage_one == True and garbage_three == False:
                time.sleep(1)
                print("")
                print("1x Garbage Stored.")
                print("")
                time.sleep(2.4)
                garbage_three = True
                break

    # time temple
    if startbed == "time temple" and time_bed == True:
        print("Hi wanna play again?")
        time.sleep(1)
        print("NONONONO JUST GO AWAY YOUR NOT WAISTING MY TIME AGAIN")
        time.sleep(3)
        print("okay...")
        time.sleep(1)
    if startbed == "time temple" and time_bed == False:
        print("Welcome...")
        time.sleep(1)
        print("")
        print("i think you came here for the patience test")
        print("")
        time.sleep(2)
        print("Alright lets start...")
        print("")
        time.sleep(1)
        print("First test the 10 seconds test...")
        print("")
        time.sleep(1.5)
        print("Here i will start the timer.. in 3 2 1")
        time.sleep(3)
        print("")
        print("Now  WAIT 10 SECONDS...")
        time.sleep(10)
        print("")
        print("Wow you acctully did it")
        time.sleep(1)
        print("")
        print("Now for the second test THE 15 SECONDS TEST!!")
        print("")
        time.sleep(1)
        print("NOW WAIT 15 SECONDS...")
        time.sleep(15)
        print("")
        print("Wow no one has passed this challenge for 2 whole years")
        print("")
        time.sleep(2)
        print("NOW FOR THE THIRD TEST THAT NO ONE EVER PASSED THE 25 SECONDS TEST")
        time.sleep(3)
        print("")
        print("WAIT 25 SECONDS NOW!!!")
        print("")
        time.sleep(25)
        print("Wai-  wait- you acctully did it....")
        print("")
        time.sleep(3)
        print("Here is your prize as promised...")
        print("")
        time.sleep(2)
        print("")
        print("(Time Waster Bed) Unlocked! type (beds) to check out your collection!")
        time.sleep(3)
        print("")
        print("")
        time_bed = True
        bed_c = bed_c + 1
        bed_cvr = bed_cvr + 1
        levelexp=levelexp+7

    # space
    if rocket_bed_F == False and startbed == "space":
        print("")
        print("Hmmm.. it looks like i need a charged rocket")
        print("")
        time.sleep(1.5)
    if rocket_bed_F == True and space_bed == True and nuclear_two == True and startbed == "space":
        print("it was scary there i dont wanna come back...")
        time.sleep(2.5)
    if rocket_bed_F == True and space_bed == False and startbed == "space" or rocket_bed_F == True and nuclear_two == False and startbed == "space":
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("   __l__")
        print("  |     |")
        print("  |     |")
        print(" _|     |_")
        print("")
        time.sleep(1)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.3)
        print("")
        time.sleep(0.5)
        print("*You reached the space!*")
        time.sleep(3)
        print("you landed at the closest planet")
        time.sleep(4)
        print("")
        print("")
        print("a old man ran into you!")
        time.sleep(4)
        print("")
        print("old man: Hey some aliens stole 4 of my nuclear fuel and their planning to nuke the entire planet please help me get them back I will reward you please...")
        time.sleep(14)
        print("")
        print("*you accepted to help the old man*")
        time.sleep(4)
        print("")
        print("old man: wait before you go take this bed with you")
        time.sleep(5)
        print("")
        print("Obtained (Space Bed) Temporarily!")
        time.sleep(5)
        print("The space bed teleported you to the aliens")
        time.sleep(5)
        print("")
        print("")
        print("Aliens: INTRUDERS!!")
        time.sleep(4)
        print("")
        print("*you told them that your a comedic*")
        time.sleep(4)
        print("Aliens: Oh really.. Show us some of your jokes")
        time.sleep(4)
        print("")
        while 1:
            alaugheda = False
            print("")
            print("Say a joke")
            jokehaha=input("")
            jokehahac = jokehaha.count("") - 1
            if jokehahac >= 0 and jokehahac <= 29:
                print("Aliens: Thats not funny")
                time.sleep(2)
            if jokehahac >= 30 and jokehahac <= 90:
                print("Aliens: HAHAHAHA")
                time.sleep(3)
                alaugheda = True
                break
            if jokehahac > 90:
                print("Aliens: not funnyyy its too long")
                time.sleep(3)
        if alaugheda == True:
            print("")
            print("")
            print("*you got through the aliens and got back the stolen nuclear fuel*")
            time.sleep(6)
            print("")
            print("Aliens: Hey what do you think are you doing COME BACK")
            time.sleep(5)
            print("")
            print("Aliens: ALIENS ATTACK!!")
            time.sleep(5)
            print("*the space bed tells you to use it to fight*")
            time.sleep(6)
            print("")
            while 1:
                print("Choose a move:")
                print("void         pressure")
                mvcalien = input("")
                if mvcalien =="pressure" or mvcalien == "void":
                    print("")
                    if mvcalien=="pressure":
                        print("Space Bed Used Pressure!")
                    if mvcalien=="void":
                        print("Space Bed Used Void")
                    time.sleep(2.5)
                    print("Aliens lost some health")
                    time.sleep(2.5)
                    if mvcalien=="void":
                        print("6 Aliens Fainted 14 Aliens left")
                    if mvcalien=="pressure":
                        print("13 Aliens Fainted 7 Aliens left")
                    time.sleep(2.5)
                    print("")
                    print("The Aliens got slowed down due to the damage!")
                    time.sleep(5)
                    print("")
                    print("*The Space Bed Teleported You Back to the old man*")
                    time.sleep(5)
                    print("Old Man: Your back!! with my stolen nuclear fuel too!")
                    print("")
                    time.sleep(6)
                    print("Old Man: Well here is your promised prize")
                    time.sleep(4)
                    print("Obtained 2x Nuclear Fuel")
                    time.sleep(3)
                    print("")
                    print("You went Back to your rocket bed...")
                    time.sleep(4)
                    print("Launching in 5")
                    time.sleep(1)
                    print("4")
                    time.sleep(1)
                    print("3")
                    time.sleep(1)
                    print("2")
                    time.sleep(1)
                    print("Old Man: WAIT!!")
                    time.sleep(3)
                    print("*You turned off the rocket bed...*")
                    time.sleep(4)
                    print("Old Man: The space bed told me it wants to join you!")
                    time.sleep(5)
                    print("Old Man: So take it with you")
                    time.sleep(4)
                    print("")
                    print("(Space Bed) Unlocked! Type (beds) to checkout your collection!")
                    space_bed = True
                    bed_c = bed_c + 1
                    bed_cvr = bed_cvr + 1
                    levelexp=levelexp+7
                    time.sleep(3)
                    print("")
                    print("Old Man: See you and thanks again!!")
                    time.sleep(4)
                    print("")
                    print("2")
                    time.sleep(1)
                    print("1")
                    time.sleep(1)
                    print("Launching! Destination: Earth!")
                    time.sleep(3.5)
                    print("*you got back to earth*")
                    time.sleep(2)
                    nuclear_one=True
                    nuclear_two=True
                    break
                
            
        
    # nuclear mark
    if startbed == "nuclear mark" and nuclear_bed == False:
        print("")
        print("hmm a (x) mark, it says nuclear here... weird")
        time.sleep(3)
        print("")
    if startbed == "nuclear mark" and nuclear_bed == True and cave == False:
        print("")
        print("*you placed the nuclear bed on a (x) mark*")
        time.sleep(2)
        print("*you ignited and ran away*")
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1!!!")
        time.sleep(1)
        print("*the bed exploded*")
        time.sleep(1)
        print("")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("*you revealed a hidden cave!!*")
        print("")
        time.sleep(1)
        print("Search area (Cave) Unlocked! type cave to search the area!!")
        time.sleep(3)
        cave = True

    # hidden cave
    if startbed == "cave" and cave == False:
        print("")
        print("What cave?")
        time.sleep(1.5)
        print("")
    if startbed == "cave" and cave == True and diamond_bed == True and bedrock_bed == True and stone_bed == True:
        print("")
        print("All Cave items already found... i better not go there again")
        print("")
    if startbed == "cave" and cave == True and bedrock_bed == False:
        print("")
        print("*you entered the cave*")
        print("")
        cgzero = True
        cgtwo = True
        cgthree = True
        time.sleep(1)
        while cgzero == True:
            print("")
            print("Ground Level : 0")
            print("")
            print("Possible Finds:")
            print("Ground Level 1 : NEW BED")
            print("Ground Level 2 : NEW BED")
            print("Ground Level 3 : NEW BED")
            print("")
            if chancem == False:
                print("Do you wanna mine to ground level (1) - There is a 20% chance to encounter lava and die")
            if chancem == True:
                print("Do you wanna mine to ground level (1) - There is a 10% chance to encounter lava and die")
            print("")
            caving = input("(yes/no)")
            if caving == "no":
                print("Alright am always here incase you changed your mind...")
                cgzero = False
            if caving == "yes":
                print("")
                print("*you mined down*")
                if chancem == True:
                    cone = ['Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'LAVA!!', 'Stone Bed!']
                if chancem==False:
                    cone = ['Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'Stone Bed!', 'LAVA!!', 'LAVA!!']
                coner = random.choice(cone)
                conej = "".join(coner)
                time.sleep(1.5)
                if conej == "LAVA!!":
                    print("*You encountered Lava*")
                    print("You burnt to death...")
                    time.sleep(2)
                    print("")
                    cgzero = False
                if conej == "Stone Bed!":
                    print("*Ground Level 1 Reached Succesfully!*")
                    time.sleep(1)
                    print("")
                    print("*You found a Stone Bed!*")
                    time.sleep(0.5)
                    if stone_bed == True:
                        print("Although you already have it...")
                    if stone_bed == False:
                        print("(Stone Bed) Unlocked! type beds to check out your collection!")
                        bed_c = bed_c + 1
                        bed_cvr = bed_cvr + 1
                        stone_bed = True
                        levelexp=levelexp+7
                        time.sleep(3)
                    print("")
                    while cgtwo == True:
                        cgzero = False
                        print("")
                        print("")
                        print("Ground Level : 1")
                        print("")
                        print("Possible Finds:")
                        print("Ground Level 1 : Stone Bed - Unlocked")
                        print("Ground Level 2 : NEW BED")
                        print("Ground Level 3 : NEW BED")
                        print("")
                        if chancem == False:
                            print("Do you wanna mine to ground level (2) - There is a 30% chance to encounter lava and die")
                        if chancem==True:
                            print("Do you wanna mine to ground level (2) - There is a 15% chance to encounter lava and die")
                        ctwo = input("(yes/no)")
                        if ctwo == "no":
                            print("Alright!")
                            print("")
                            print("*you got back up to land*")
                            cgtwo = False
                        if ctwo == "yes":
                            print("")
                            print("")
                            print("*you mined down*")
                            if chancem==True:
                                ctwo = ['Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!',  'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!' , 'Diamond Bed!',  'LAVA!!']
                            if chancem==False:
                                ctwo = ['Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!', 'Diamond Bed!',  'Diamond Bed!', 'Diamond Bed!', 'LAVA!!', 'LAVA!!', 'LAVA!!']
                            ctwor = random.choice(ctwo)
                            ctwoj = "".join(ctwor)
                            time.sleep(1.5)
                            if ctwoj == "LAVA!!":
                                print("*You encountered Lava*")
                                print("You burnt to death...")
                                time.sleep(2)
                                print("")
                                cgtwo = False

                            if ctwoj == "Diamond Bed!":
                                print("*Ground Level 2 Reached Succesfully!*")
                                time.sleep(1)
                                print("")
                                print("*You found a Diamond Bed!*")
                                time.sleep(0.5)
                                if diamond_bed == True:
                                    print("Although you already have it... ")
                                    time.sleep(1)
                                if diamond_bed == False:
                                    print("(Diamond Bed) Unlocked! type beds to check out your collection!")
                                    diamond_bed = True
                                    bed_c = bed_c + 1
                                    bed_cvr = bed_cvr + 1
                                    levelexp= levelexp + 7
                                    print("")
                                    time.sleep(3)
                                while cgthree == True:
                                    cgtwo = False
                                    print("")
                                    print("")
                                    print("Ground Level : 2")
                                    print("")
                                    print("Possible Finds:")
                                    print("Ground Level 1 : Stone Bed - Unlocked")
                                    print("Ground Level 2 : Diamond Bed - Unlocked")
                                    print("Ground Level 3 : NEW BED")
                                    print("")
                                    if chancem==True:
                                        print("Do you wanna mine to ground level (3) - There is a 20% chance to encounter lava and die")
                                    if chancem==False:
                                        print("Do you wanna mine to ground level (3) - There is a 40% chance to encounter lava and die")
                                    ctwo = input("(yes/no)")
                                    if ctwo == "no":
                                        print("Alright!")
                                        print("")
                                        print("*you got back up to land*")
                                        cgthree = False
                                    if ctwo == "yes":
                                        print("")
                                        print("")
                                        print("*you mined down*")
                                        if chancem==False:
                                            ctwo = ['Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'LAVA!!', 'LAVA!!', 'LAVA!!', 'LAVA!!']
                                        if chancem==True:
                                            ctwo = ['Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'Bedrock Bed!', 'LAVA!!', 'LAVA!!']
                                        ctwor = random.choice(ctwo)
                                        ctwoj = "".join(ctwor)
                                        time.sleep(1.5)
                                        if ctwoj == "LAVA!!":
                                            print("*You encountered Lava*")
                                            print("You burnt to death...")
                                            time.sleep(2)
                                            print("")
                                            cgthree = False
                                        if ctwoj == "Bedrock Bed!":
                                            print("*Ground Level 3 Reached Succesfully!*")
                                            time.sleep(1)
                                            print("")
                                            print("*You found a Bedrock Bed!*")
                                            time.sleep(0.5)
                                            if bedrock_bed == True:
                                                print("Although you already have it... ")
                                                time.sleep(1)
                                            if bedrock_bed == False:
                                                print("(Bedrock Bed) Unlocked! type beds to check out your collection!")
                                                bedrock_bed = True
                                                bed_c = bed_c + 1
                                                levelexp = levelexp + 10
                                                print("")
                                                time.sleep(3)
                                                print(
                                                    "I have searched the whole cave lemme go back up AND NEVER RETURN...")
                                                time.sleep(2)
                                                cgthree = False

    # underwater
    if startbed == "underwater":
        print("")
        print("")
        if chancem==True:
            print("Possible Finds:")
            print("Rocket fuel - 30%")
            print("Underwater Bed - 30%")
            print("Rocket Bed - Empty - 30%")
            print("Dead fish - 10%")
        if chancem==False:
            print("Possible Finds:")
            print("Rocket fuel - 20%")
            print("Underwater Bed - 15%")
            print("Rocket Bed - Empty - 25%")
            print("Dead fish - 40%")
        time.sleep(3)
        print("")
        print("*you searched underwater*")
        print("")
        time.sleep(2)
        if chancem==False:
            underwaterf = ['Rocket Fuel!', 'Rocket Fuel!', 'Rocket Fuel!', 'Rocket Fuel!', 'Rocket Bed!!', 'Rocket Bed!!', 'Rocket Bed!!', 'Rocket Bed!!', 'Rocket Bed!!', 'underwater bed!', 'underwater bed!',  'underwater bed!', 'Dead fish', 'Dead fish', 'Dead fish', 'Dead fish', 'Dead fish', 'Dead fish', 'Dead fish', 'Dead fish']
        if chancem==True:
            underwaterf = ['Rocket Fuel!', 'Rocket Fuel!', 'Rocket Fuel!', 'underwater bed!', 'underwater bed!',  'underwater bed!', 'Rocket Bed!!', 'Rocket Bed!!', 'Rocket Bed!!', 'Dead fish']
        underwaterr = random.choice(underwaterf)
        underwaterj = "".join(underwaterr)
        print("You found a " + underwaterj)
        if underwaterj == "underwater bed!" and underwater_bed == True:
            print("")
            print("BED ALREADY OBTAINED...")
            print("")
            time.sleep(1.5)
        if underwaterj == "underwater bed!" and underwater_bed == False:
            time.sleep(0.8)
            print("")
            print("(Underwater Bed) Unlocked! type (beds) to check out your collection!")
            print("")
            time.sleep(3)
            print("")
            underwater_bed = True
            bed_c = bed_c + 1
            bed_cvr = bed_cvr + 1
            levelexp = levelexp + 7
        if underwaterj == "Rocket Bed!!" and rocket_bed_E == True:
            print("")
            print("Bed already obtained...")
            print("")
            time.sleep(0.8)
        if underwaterj == "Rocket Bed!!" and rocket_bed_E == False:
            print("")
            print("(Rocket Bed - Empty) Unlocked! type (beds) to check out your collection!")
            print("")
            time.sleep(3)
            rocket_bed_E = True
            bed_c = bed_c + 1
            levelexp = levelexp + 3
        if underwaterj == "Rocket Fuel!" and rocket_fuel == True:
            print("")
            print("You have the Maximum amount of rocket fuels please use it to obtain a new one")
            time.sleep(1)
        if underwaterj == "Rocket Fuel!" and rocket_fuel == False:
            print("")
            print("Stored 1x Rocket Fuel")
            time.sleep(1)
            rocket_fuel = True
            print("")
        if underwaterj == "Dead fish":
            print("")
            time.sleep(0.8)

    # white bed
    if white_bed == False and startbed == "white walls":
        print("")
        print("*You searched behind the white walls*")
        time.sleep(1.5)
        print("")
        print("You found a white bed!!")
        time.sleep(1.5)
        print("(White Bed) Unlocked! Type (beds) to check out your collection!!")
        print("")
        white_bed = True
        bed_c = bed_c + 1
        levelexp = levelexp + 1
        time.sleep(3)
    elif white_bed == True and startbed == "white walls":
        print("")
        print("*You searched behind the white walls*")
        time.sleep(1.5)
        print("")
        print("You found nothing!")
        print("")

    # red bed
    if red_bed == False and startbed == "red walls":
        print("")
        print("*You searched behind the red walls*")
        time.sleep(1.5)
        print("")
        print("You found a red bed!!")
        time.sleep(1.5)
        print("(Red Bed) Unlocked! Type (beds) to check out your collection!!")
        print("")
        red_bed = True
        bed_c = bed_c + 1
        levelexp = levelexp + 1
        time.sleep(3)
    elif red_bed == True and startbed == "red walls":
        print("")
        print("*You searched behind the red walls*")
        time.sleep(1.5)
        print("")
        print("You found nothing!")
        print("")

    # blue bed
    if blue_bed == False and startbed == "blue walls":
        print("")
        print("*You searched behind the blue walls*")
        time.sleep(1.5)
        print("")
        print("You found a blue bed!!")
        time.sleep(1.5)
        print("(Blue Bed) Unlocked! Type (beds) to check out your collection!!")
        print("")
        blue_bed = True
        bed_c = bed_c + 1
        levelexp = levelexp + 1
        time.sleep(3)
    elif blue_bed == True and startbed == "blue walls":
        print("")
        print("*You searched behind the blue walls*")
        time.sleep(1.5)
        print("")
        print("You found nothing!")
        print("")

    # yellow bed
    if yellow_bed == False and startbed == "yellow walls":
        print("")
        print("*You searched behind the yellow walls*")
        time.sleep(1.5)
        print("")
        print("You found a yellow bed!!")
        time.sleep(1.5)
        print("(Yellow Bed) Unlocked! Type (beds) to check out your collection!!")
        print("")
        yellow_bed = True
        bed_c = bed_c + 1
        levelexp = levelexp + 1
        time.sleep(3)
    elif yellow_bed == True and startbed == "yellow walls":
        print("")
        print("*You searched behind the yellow walls*")
        time.sleep(1.5)
        print("")
        print("You found nothing!")
        print("")

    # wheel spin error
    if lucky_bed == True and bed_mixer == True and wheeled_bed == True and startbed == "wheel spin":
        print("")
        print("")
        print("⚠️ALL PRIZES OBTAINED...⚠️")
        print("")
        print("")
    # wheel spin
    if startbed == "wheel spin" and lucky_bed == False or bed_mixer == False and startbed == "wheel spin" or startbed == "wheel spin" and wheeled_bed == False:
        while 1:
            print("Possible Prizes :")
            print("")
            if chancem==False:
                print("NEW BED / 10%")
                print("NEW BED / 15%")
                print("NEW COMMAND / 15%")
                print("Nothing / 60%")
            if chancem==True:
                print("NEW BED / 20%")
                print("NEW BED / 30%")
                print("NEW COMMAND / 30%")
                print("Nothing / 20%")
            print("")
            print("")
            print("*you spun the wheel*")
            time.sleep(0.5)
            print("you won a...")
            print("")
            time.sleep(2)
            if chancem==False:
                wheel = ['you won a Bed Mixer!!!', 'you won a Bed Mixer!!!', 'you won a Lucky Bed!!!', 'you won a Bed Mixer!!!', 'you won a Wheeled Bed!!!', 'you won a Wheeled Bed!!!', 'you won a Wheeled Bed!!!', 'you won a Lucky Bed!!!', 'you won  nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing', 'you won nothing']
            if chancem==True:
                wheel = ['you won a Bed Mixer!!!', 'you won a Bed Mixer!!!', 'you won a Lucky Bed!!!', 'you won a Bed Mixer!!!', 'you won a Wheeled Bed!!!', 'you won a Wheeled Bed!!!', 'you won a Wheeled Bed!!!', 'you won a Lucky Bed!!!', 'you won nothing', 'you won nothing']
            wheelr = random.choice(wheel)
            wheelj = "".join(wheelr)
            print("🌟" + wheelj + "🌟")

            # lucky bed
            if wheelj == "you won a Lucky Bed!!!" and lucky_bed == True:
                print("")
                print("Prize already obtained...")
                print("")
                print("Re-Spinning...")
                time.sleep(1.5)
                print("")
            if wheelj == "you won a Lucky Bed!!!" and lucky_bed == False:
                print("(Lucky Bed) Unlocked! type (beds) to check out your collection!")
                lucky_bed = True
                bed_c = bed_c + 1
                levelexp = levelexp + 5
                print("")
                print("")
                time.sleep(3)
                print("")
                break

            # bed mixer - wheel
            if wheelj == "you won a Bed Mixer!!!" and bed_mixer == True:
                print("")
                print("Prize already obtained")
                print("")
                print("Re-Spinning....")
                print("")
                time.sleep(1.5)
                print("")
            if wheelj == "you won a Bed Mixer!!!" and bed_mixer == False:
                print("(Bed Mixer) Unlocked! type (Bed Mixer) to check it out!")
                print("")
                print("")
                print("")
                time.sleep(3)
                bed_mixer = True
                break

            # wheeled bed
            if wheelj == "you won a Wheeled Bed!!!" and wheeled_bed == True:
                print("")
                print("")
                print("Prize already obtained...")
                print("")
            if wheelj == "you won a Wheeled Bed!!!" and wheeled_bed == False:
                wheeled_bed = True
                bed_c = bed_c + 1
                levelexp = levelexp + 3
                print("(Wheeled Bed) Unlocked! type (beds) to check out your collection!")
                time.sleep(3)
                print("")
                print("")
                print("")
                break

            # nothing
            if wheelj == "you won nothing":
                print("Re-Spinning...")
                time.sleep(1.5)
                print("")
                print("")

    # bed mixer
    if bed_mixer == True and startbed == "bed mixer":
        while 1:
            print("")
            print("")
            print("Bed Mixer:")
            print("Possible Mixes - ")
            print("")
            print(" 1- green bed")
            print(" 2- purple bed")
            print(" 3- pink bed")
            print(" 4- orange bed")
            print(" 5- rainbow bed")
            print(" 6- magical bed")
            print(" 7- nuclear bed")
            print(" 8- car bed")
            print(" 9- garbage bed")
            print("10- aura bed")
            print("11- gold bed")
            print("12- magma bed")
            print("close")
            bm = input("so what bed do you want to form?")

            if bm == "close":
                print("")
                print("Closing Bed Mixer...")
                time.sleep(1.2)
                print("")
                break



            # magma bed - mixer
            if bm=="magma bed" and magma_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="magma bed" and magma_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Magma Bed")
                    print("Rarity: Very Rare")
                    print("Requirments: 3x Earth auras and 2x Fire auras")
                    print("do you want to form a magma bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and earth < 3 or firea < 2 and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and earth >= 3 and firea >= 2:
                        print("you mixed 3 earth auras and 2 fire auras...")
                        time.sleep(2)
                        print("")
                        print("(Magma Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        magma_bed = True
                        bed_c = bed_c + 1
                        bed_cvr = bed_cvr + 1
                        earth = earth - 3
                        firea = firea - 2
                        levelexp = levelexp + 7
                        break
                
                
                
            # gold bed - mixer
            if bm=="gold bed" and gold_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="gold bed" and gold_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Gold Bed")
                    print("Rarity: Very Rare")
                    print("Requirments: 2x Earth auras, 2x Fire auras and 1x Air aura")
                    print("do you want to form a gold bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and earth < 2 or firea < 2 and bedmixc == "yes" or air < 1 and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and earth >= 2 and firea >= 2 and air >= 1:
                        print("you mixed 2 earth auras, 2 fire auras and 1 air aura....")
                        time.sleep(2)
                        print("")
                        print("(Gold Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        gold_bed = True
                        bed_c = bed_c + 1
                        bed_cvr = bed_cvr + 1
                        earth = earth - 2
                        firea = firea - 2
                        air = air - 1
                        levelexp = levelexp + 7
                        break
                    
                
                
                
            # aura bed - mixer
            if bm=="aura bed" and aura_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="aura bed" and aura_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Aura Bed")
                    print("Rarity: Rare")
                    print("Requirments: 1x Earth auras, 1x Fire auras and 1x Air aura")
                    print("do you want to form a aura bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and earth < 1 or firea < 1 and bedmixc == "yes" or air < 1 and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and earth >= 1 and firea >= 1 and air >= 1:
                        print("you mixed 1 earth auras, 1 fire auras and 1 air aura....")
                        time.sleep(2)
                        print("")
                        print("(Aura Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        aura_bed = True
                        bed_c = bed_c + 1
                        earth = earth - 1
                        firea = firea - 1
                        air = air - 1
                        levelexp = levelexp + 5
                        break
                
                
            # garbage bed mixer
            if bm=="garbage bed" and garbage_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="garbage bed" and garbage_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Garbage Bed")
                    print("Rarity: Extremely Rare")
                    print("Requirments: 3x garbage and magical bed")
                    print("do you want to form a garbage bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and garbage_three == False or magical_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and garbage_three==True and magical_bed==True:
                        print("you mixed 3x garbage and magical bed....")
                        time.sleep(2)
                        print("")
                        print("(Garbage Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        garbage_bed = True
                        bed_c = bed_c + 1
                        bed_cvr = bed_cvr + 1
                        levelexp = levelexp + 10
                        break

            # car bed - mixer
            if bm=="car bed" and car_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="car bed" and car_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Car Bed")
                    print("Rarity: Rare")
                    print("Requirments: wheeled bed and magical bed")
                    print("do you want to form a car bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and wheeled_bed== False or magical_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and wheeled_bed==True and magical_bed==True:
                        print("you mixed a wheeled bed and magical bed")
                        time.sleep(2)
                        print("")
                        print("(Car Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        car_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 5
                        break

            # magical bed - mixer
            if bm=="magical bed" and magical_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="magical bed" and magical_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Magical Bed")
                    print("Rarity: Rare")
                    print("Requirments: Rainbow Bed and Lucky Bed")
                    print("do you want to form a magical bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and lucky_bed== False or rainbow_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and lucky_bed==True and rainbow_bed==True:
                        print("you mixed a rainbow bed and lucky bed")
                        time.sleep(2)
                        print("")
                        print("(Magical Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        magical_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 5
                        break

            # Nuclear Bed - mixer
            if bm=="nuclear bed" and nuclear_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="nuclear bed" and nuclear_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Nuclear Bed")
                    print("Rarity: Very Rare")
                    print("Requirments: 2x garbage and magical bed")
                    print("do you want to form a nuclear bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and nuclear_two == False or magical_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and nuclear_two ==True and magical_bed==True:
                        print("you mixed 2x nuclear and magical bed....")
                        time.sleep(2)
                        print("")
                        print("(Nuclear Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        nuclear_bed = True
                        bed_c = bed_c + 1
                        bed_cvr = bed_cvr + 1
                        levelexp = levelexp + 7
                        break


            # orange bed - mixer
            if bm=="orange bed" and orange_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="orange bed" and orange_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Orange Bed")
                    print("Rarity: Uncommon")
                    print("Requirments: Yellow bed and Red bed")
                    print("do you want to form a orange bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and yellow_bed== False or red_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and yellow_bed==True and red_bed==True:
                        print("you mixed a yellow bed and red bed")
                        time.sleep(2)
                        print("")
                        print("(Orange Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        orange_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 3
                        break

            # rainbow bed - mixer
            if bm=="rainbow bed" and rainbow_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="rainbow bed" and rainbow_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Rainbow Bed")
                    print("Rarity: Rare")
                    print("Requirments: Blue bed, Yellow bed, Red bed, White bed, Green bed, Purple bed, Pink bed and Orange bed")
                    print("do you want to form a rainbow bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and blue_bed== False or yellow_bed==False and bedmixc == "yes" or bedmixc == "yes" and red_bed== False or white_bed==False and bedmixc == "yes" or bedmixc == "yes" and green_bed== False or purple_bed==False and bedmixc == "yes" or bedmixc == "yes" and pink_bed== False or orange_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and blue_bed==True and yellow_bed==True and red_bed==True and white_bed==True and green_bed==True and purple_bed==True and pink_bed == True and orange_bed==True:
                        print("you mixed the beds: Blue, Yellow, Red, White, Green, Purple, Pink and Orange....")
                        time.sleep(2)
                        print("")
                        print("(Rainbow Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        rainbow_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 5
                        break

            # pink bed - mixer
            if bm=="pink bed" and pink_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="pink bed" and pink_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Pink Bed")
                    print("Rarity: Uncommon")
                    print("Requirments: White bed and Red bed")
                    print("do you want to form a pink bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and white_bed== False or red_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and white_bed==True and red_bed==True:
                        print("you mixed a white bed and red bed")
                        time.sleep(2)
                        print("")
                        print("(Pink Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        pink_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 3
                        break

            # green bed - mixer
            if bm=="green bed" and green_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="green bed" and green_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Green Bed")
                    print("Rarity: Uncommon")
                    print("Requirments: Blue bed and Yellow bed")
                    print("do you want to form a green bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and blue_bed== False or yellow_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and blue_bed==True and yellow_bed==True:
                        print("you mixed a yellow bed and blue bed")
                        time.sleep(2)
                        print("")
                        print("(Green Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        green_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 3
                        break

            # purple bed - mixer
            if bm=="purple bed" and purple_bed==True:
                print("")
                print("Bed Already Obtained...")
                time.sleep(2)
            if bm=="purple bed" and purple_bed==False:
                while 1:
                    print("")
                    print("___________________________")
                    print("Purple Bed")
                    print("Rarity: Uncommon")
                    print("Requirments: Blue bed and Red bed")
                    print("do you want to form a purple bed? (yes/no)")
                    bedmixc = input("")
                    if bedmixc == "no":
                        print("")
                        time.sleep(0.3)
                        break
                    if bedmixc == "yes" and blue_bed== False or red_bed==False and bedmixc == "yes":
                        print("ERROR")
                        time.sleep(1)
                        print("Insufficient requirments")
                        time.sleep(1)
                        print("")
                        break
                    if bedmixc == "yes" and blue_bed==True and red_bed==True:
                        print("you mixed a purple bed and blue bed")
                        time.sleep(2)
                        print("")
                        print("(Purple Bed) Unlocked! type (beds) to check out your collection")
                        time.sleep(3)
                        purple_bed = True
                        bed_c = bed_c + 1
                        levelexp = levelexp + 3
                        break

    # bed mixer locked
    if bed_mixer == False and startbed == "bed mixer":
        print("")
        print("(Bed Mixer) Locked! try opening it from the wheel spin!!")
        print("")
        print("")
        time.sleep(2)
        





    if startbed == "bed center":
        print("")
        print("You entered the bed center...")
        time.sleep(2)
        print("")
        print("")
        while 1:
            print("What do you want to do?")
            print("")
            print("1- battle")
            print("2- shop")
            print("back")
            tpc = input("")
            if tpc == "back":
                print("")
                print("you got out of the bed center...")
                time.sleep(2)
                print("")
                print("")
                break
            if tpc == "shop":
                print("You went to the shopping district")
                time.sleep(2)
                while 1:
                    print("")
                    print("")
                    print("Bed Shop__________")
                    print("Battle Points: " + str(bp))
                    print("")
                    print("L card         1BP")
                    print("rocket fuel     1BP")
                    print("garbage         1BP")
                    print("nuclear fuel    2BP")
                    if bp_m==False:
                        print("bp multiplier   2BP")
                    if bp_m==True:
                        print("adv bp Multiplier 5BP")
                    print("tanky armor     5BP")
                    print("energy coat     5BP")
                    print("damage orb      5BP")
                    print("speed drink     5BP")
                    print("heal charm      5BP")
                    print("combat bed      8BP")
                    print("back")
                    print("What do you want to buy?")
                    bshop = input("")
                    if bshop == "back":
                        print("")
                        print("Going Back...")
                        print("")
                        print("")
                        time.sleep(2)
                        break
                    if bshop == "L card" or bshop=="l card":
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("L card")
                            print("Cost : 1BP")
                            print("")
                            print("a card that can be used to make kids happy rumors say there are too many crying kids at (love valley)")
                            print("")
                            print("")
                            print("Are you sure you want to buy a L card? (yes/no)")
                            lcbuy = input("")
                            if lcbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if lcbuy == "yes" and bp < 1:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if lcbuy == "yes" and bp >= 1:
                                    print("")
                                    time.sleep(1)
                                    print("1x L card Purchased!")
                                    time.sleep(1.5)
                                    bp = bp - 1
                                    lcards = lcards + 1
                                    break
                                    
                    if bshop == "rocket fuel" and rocket_fuel == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have a Rocket Fuel")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "rocket fuel" and rocket_fuel == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Rocket Fuel")
                            print("Cost : 1 Battle Points")
                            print("")
                            print("a special kind of fuel used to charge up a rocket")
                            print("")
                            print("")
                            print("Are you sure you want to buy a Rocket Fuel? (yes/no)")
                            hbuy = input("")
                            if hbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if hbuy == "yes" and bp < 1:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if hbuy == "yes" and bp >= 1:
                                    print("")
                                    time.sleep(1)
                                    print("Rocket Fuel Purchased!")
                                    time.sleep(1.5)
                                    bp = bp - 1
                                    rocket_fuel = True
                                    break
                    if bshop == "heal charm" and heal_c == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an heal charm")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "heal charm" and heal_c == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Heal Charm")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("a magical charm that heals your bed by 1.5 hitpoints every round")
                            print("")
                            print("")
                            print("Are you sure you want to buy an heal charm? (yes/no)")
                            hbuy = input("")
                            if hbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if hbuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if hbuy == "yes" and bp >= 5:
                                    print("")
                                    time.sleep(1)
                                    print("Heal Charm Purchased!")
                                    time.sleep(1.5)
                                    bp = bp - 5
                                    heal_c = True
                                    break
                    if bshop == "adv bp multiplier" and advbp_m == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an adv bp multiplier")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "adv bp multiplier" and advbp_m == False and bp_m==True:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("adv bp multiplier")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("Multiplies your Battle Points gained from a battle by 3")
                            print("")
                            print("")
                            print("Are you sure you want to buy an adv bp multiplier? (yes/no)")
                            ambuy = input("")
                            if ambuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if ambuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if ambuy == "yes" and bp >= 5:
                                print("")
                                time.sleep(1)
                                print("Advanced BP Multiplier Purchased!")
                                time.sleep(1.5)
                                bp = bp - 5
                                advbp_m = True
                                break
                    if bshop == "speed drink" and sp_d == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an speed drink")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "speed drink" and sp_d == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("speed drink")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("a sweet drink, very sweet that it can increase the speed of any bed by 3")
                            print("")
                            print("")
                            print("Are you sure you want to buy an speed drink? (yes/no)")
                            sbuy = input("")
                            if sbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if sbuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if sbuy == "yes" and bp >= 5:
                                print("")
                                time.sleep(1)
                                print("Speed Drink Purchased!")
                                time.sleep(1.5)
                                bp = bp - 5
                                sp_d = True
                                break
                    if bshop == "bp multiplier" and bp_m == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an bp multiplier")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "bp multiplier" and bp_m == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("bp multiplier")
                            print("Cost : 2 Battle Points")
                            print("")
                            print("Multiplies your Battle Points gained from a battle by 2")
                            print("")
                            print("")
                            print("Are you sure you want to buy an bp multiplier? (yes/no)")
                            mbuy = input("")
                            if mbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if mbuy == "yes" and bp < 2:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if mbuy == "yes" and bp >= 2:
                                print("")
                                time.sleep(1)
                                print("BP Multiplier Purchased!")
                                time.sleep(1.5)
                                bp = bp - 2
                                bp_m = True
                                break
                    if bshop == "tanky armor" and tank_a == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an Tanky Armor")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "tanky armor" and tank_a == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Tanky Armor")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("Some Rare Bulky Armor that increases the base health of any bed by 5")
                            print("")
                            print("")
                            print("Are you sure you want to buy an Tanky Armor? (yes/no)")
                            tbuy = input("")
                            if tbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if tbuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if tbuy == "yes" and bp >= 5:
                                print("")
                                time.sleep(1)
                                print("Tanky Armor Purchased!")
                                time.sleep(1.5)
                                bp = bp - 5
                                tank_a = True
                                break
                    if bshop == "energy coat" and en_c == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an energy coat")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "energy coat" and en_c == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Energy Coat")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("a coat full of energy that increases the base energy of any bed by 5")
                            print("")
                            print("")
                            print("Are you sure you want to buy an Energy Coat? (yes/no)")
                            ebuy = input("")
                            if ebuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if ebuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if ebuy == "yes" and bp >= 5:
                                print("")
                                time.sleep(1)
                                print("Energy Coat Purchased!")
                                time.sleep(1.5)
                                bp = bp - 5
                                en_c = True
                                break
                    if bshop == "damage orb" and dmg_o == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an damage orb")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "damage orb" and dmg_o == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Damage Orb")
                            print("Cost : 5 Battle Points")
                            print("")
                            print("a red orb that appears to increase the damage of any move by 25%")
                            print("")
                            print("")
                            print("Are you sure you want to buy an Damage Orb? (yes/no)")
                            dbuy = input("")
                            if dbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if dbuy == "yes" and bp < 5:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if dbuy == "yes" and bp >= 5:
                                print("")
                                time.sleep(1)
                                print("Damage Orb Purchased!")
                                time.sleep(1.5)
                                bp = bp - 5
                                dmg_o = True
                                break
                    if bshop == "combat bed" and combat_bed == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You Already have an combat bed")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "combat bed" and combat_bed == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("Combat Bed")
                            print("Cost : 8 Battle Points")
                            print("")
                            print("a skilled bed that is very strong you might want to use it for battles")
                            print("")
                            print("")
                            print("Are you sure you want to buy an Combat Bed? (yes/no)")
                            cbuy = input("")
                            if cbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if cbuy == "yes" and bp < 8:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if cbuy == "yes" and bp >= 8:
                                print("")
                                time.sleep(1)
                                print("Combat Bed Purchased!")
                                time.sleep(1.5)
                                bp = bp - 8
                                print("(Combat Bed) Unlocked! type (beds) to check out your collection")
                                time.sleep(3)
                                combat_bed = True
                                bed_c = bed_c + 1
                                levelexp=levelexp+10
                                break
                    if bshop == "nuclear fuel" and nuclear_two == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You have the maximum amount of nuclear fuel")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "nuclear fuel" and nuclear_two == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("1x Nuclear Fuel")
                            print("Cost : 2 Battle Points")
                            print("")
                            print("Used for crafting the nuclear bed")
                            print("")
                            print("")
                            print("Are you sure you want to buy 1x Nuclear? (yes/no)")
                            nbuy = input("")
                            if nbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if nbuy == "yes" and bp < 2:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if nbuy == "yes" and bp >= 2:
                                print("")
                                time.sleep(1)
                                print("1x Nuclear Fuel Purchased!")
                                time.sleep(1.5)
                                bp = bp - 2
                                if nuclear_one == True and nuclear_two == False:
                                    nuclear_two = True
                                if nuclear_one == False:
                                    nuclear_one = True
                                break
                    if bshop == "garbage" and garbage_three == True:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("You have the maximum amount of garbage")
                        time.sleep(1.5)
                        print("")
                        print("")
                    if bshop == "garbage" and garbage_three == False:
                        print("")
                        while 1:
                            time.sleep(0.6)
                            print("_______________________")
                            print("1x Garbage")
                            print("Cost : 1 Battle Point")
                            print("")
                            print("Used for crafting the garbage bed")
                            print("")
                            print("")
                            print("Are you sure you want to buy 1x Garbage? (yes/no)")
                            gbuy = input("")
                            if gbuy == "no":
                                print("")
                                print("")
                                time.sleep(1)
                                break
                            if gbuy == "yes" and bp < 1:
                                print("")
                                print("ERROR")
                                time.sleep(1)
                                print("Insufficient Battle Points")
                                time.sleep(1.5)
                                break
                            if gbuy == "yes" and bp >= 1:
                                print("")
                                time.sleep(1)
                                print("1x Garbage Purchased!")
                                time.sleep(1.5)
                                bp = bp - 1
                                if garbage_two == True and garbage_three == False:
                                    garbage_three = True
                                if garbage_one == True and garbage_two == False:
                                    garbage_two = True
                                if garbage_one == False:
                                    garbage_one = True
                                break

            if tpc=="battle" and bed_cvr < 1:
                print("")
                print("ERROR")
                time.sleep(2)
                print("you need a (very rare+) bed to access the colosseum")
            if tpc == "battle" and bed_cvr >=1:

                # player
                chosen = ""
                chosen_hp = ""
                chosen_en = ""
                chosen_m = ""
                chosen_m2 = 0
                chosen_mn = ""
                chosen_m2n = ""
                chosen_men = ""
                chosen_m2en = 0
                chosen_h = 0
                chosen_hn = ""
                chosen_hen = 0
                chosen_s = ""

                # npc
                chosenc = ""
                chosenc_hp = ""
                chosenc_en = ""
                chosenc_m = ""
                chosenc_m2 = 0
                chosenc_mn = ""
                chosenc_m2n = ""
                chosenc_h = 0
                chosenc_hn = ""
                chosenc_hen = 0
                chosenc_men = ""
                chosenc_m2en = 0
                chosenc_s = ""

                # moves
                nightmare = 4
                nightmaren = "nightmare"
                nightmareen = 3
                dream_reaper = 5.5
                dream_reapern = "dream reaper"
                dream_reaperen = 5

                confusion = 5.5
                confusionn = "confusion"
                confusionen = 5
                homework = 6.5
                homeworkn = "homework"
                homeworken = 6

                apple_drop = 5
                apple_dropn = "apple drop"
                apple_dropen = 4
                apple_rain = 7
                apple_rainn = "apple rain"
                apple_rainen = 6

                mud_wave = 7
                mud_waven = "mud wave"
                mud_waveen = 6
                mud_blast = 5
                mud_blastn = "mud blast"
                mud_blasten = 4

                banana_peel = 8
                banana_peeln = "banana peel"
                banana_peelen = 7
                toxic_slap = 6.5
                toxic_slapn = "toxic slap"
                toxic_slapen = 6

                bloody_water = 5
                bloody_watern = "bloody water"
                bloody_wateren = 4
                underwater_pull = 7
                underwater_pulln = "underwater pull"
                underwater_pullen = 6

                void = 5
                voidn = "void"
                voiden = 4
                pressure = 7.5
                pressuren = "pressure"
                pressureen = 7

                nuke = 9
                nuken = "nuke"
                nukeen = 8
                explode = 6
                exploden = "explode"
                explodeen = 5

                stone_slam = 6
                stone_slamn = "stone slam"
                stone_slamen = 5
                crush = 5
                crushn = "crush"
                crushen = 4

                diamond_beam = 5
                diamond_beamn = "diamond beam"
                diamond_beamen = 4
                shine = 4
                shinen = "shine"
                shineen = 3

                bedrock_throw = 4
                bedrock_thrown = "bedrock throw"
                bedrock_throwen = 3
                bedrock_crush = 5
                bedrock_crushn = "bedrock crush"
                bedrock_crushen = 4

                times_up = 6
                times_upn = "times up"
                times_upen = 5
                time_explosion = 4
                time_explosionn = "time explosion"
                time_explosionen = 3

                winning_slash = 6
                winning_slashn = "winning slash"
                winning_slashen = 5
                champion_strike = 7
                champion_striken = "champion strike"
                champion_strikeen = 6

                fist_barrage = 10
                fist_barragen = "fist barrage"
                fist_barrageen = 9
                punch_revolver = 6
                punch_revolvern = "punch revolver"
                punch_revolveren = 5
                
                gold_meteor = 6
                gold_meteorn = "gold meteor"
                gold_meteoren = 5
                gold_smash = 5
                gold_smashn = "gold smash"
                gold_smashen = 4
                
                magma_meteors = 8
                magma_meteorsn = "magma meteors"
                magma_meteorsen = 7
                magma_fist = 6.5
                magma_fistn = "magma fist"
                magma_fisten = 6
                
                tricky_punch = 8
                tricky_punchn = "tricky punch"
                tricky_punchen = 7
                heal_up = 6
                heal_upn = "heal up"
                heal_upen = 7.5
                
                love_arrows = 5.5
                love_arrowsn = "love arrows"
                love_arrowsen = 5
                love_beam = 7
                love_beamn = "love beam"
                love_beamen = 6
                
                rainbow_blast = 9
                rainbow_blastn = "rainbow blast"
                rainbow_blasten = 8
                magical_wall = 6
                magical_walln = "magical wall"
                magical_wallen = 5


                # bed stats
                # love bed
                lo_b = "Love Bed"
                lo_hp = 22
                lo_en = 27
                lo_m = love_arrows
                lo_mn = love_arrowsn
                lo_men = love_arrowsen
                lo_m2 = love_beam
                lo_m2n = love_beamn
                lo_m2en = love_beamen
                lo_s = 23.6
                
                #secret agent bed
                secret_b = "Secret Agent Bed"
                secret_hp = 25
                secret_en = 29
                secret_m = tricky_punch
                secret_mn = tricky_punchn
                secret_men = tricky_punchen
                secret_h = heal_up
                secret_hn = heal_upn
                secret_hen = heal_upen
                secret_s = 24.55
                
                #magma bed
                magma_b = "Magma Bed"
                magma_hp = 23
                magma_en = 28
                magma_m = magma_meteors
                magma_mn = magma_meteorsn
                magma_men = magma_meteorsen
                magma_m2 = magma_fist
                magma_m2n = magma_fistn
                magma_m2en = magma_fisten
                magma_s = 19
                
                #gold bed
                gold_b = "Gold Bed"
                gold_hp = 21
                gold_en = 21
                gold_m = gold_meteor
                gold_mn = gold_meteorn
                gold_men = gold_meteoren
                gold_m2 = gold_smash
                gold_m2n = gold_smashn
                gold_m2en = gold_smashen
                gold_s = 22
                
                # Time Waster Bed
                time_b = "Time Waster Bed"
                time_hp = 18
                time_en = 23
                time_m = time_explosion
                time_mn = time_explosionn
                time_men = time_explosionen
                time_m2 = times_up
                time_m2n = times_upn
                time_m2en = times_upen
                time_s = 24

                # space bed
                space_b = "Space Bed"
                space_hp = 21
                space_en = 26
                space_m = void
                space_mn = voidn
                space_men = voiden
                space_m2 = pressure
                space_m2n = pressuren
                space_m2en = pressureen
                space_s = 23

                # dream bed
                dream_b = "Dream Bed"
                dream_hp = 18
                dream_en = 18
                dream_m = dream_reaper
                dream_mn = dream_reapern
                dream_men = dream_reaperen
                dream_m2 = nightmare
                dream_m2n = nightmaren
                dream_m2en = nightmareen
                dream_s = 25

                # Underwater bed
                uw_b = "Underwater Bed"
                uw_hp = 26
                uw_en = 24
                uw_m = underwater_pull
                uw_mn = underwater_pulln
                uw_men = underwater_pullen
                uw_m2 = bloody_water
                uw_m2n = bloody_watern
                uw_m2en = bloody_wateren
                uw_s = 24

                # Nuclear bed
                nuclear_b = "Nuclear Bed"
                nuclear_hp = 26
                nuclear_en = 29
                nuclear_m = nuke
                nuclear_mn = nuken
                nuclear_men = nukeen
                nuclear_m2 = explode
                nuclear_m2n = exploden
                nuclear_m2en = explodeen
                nuclear_s = 20

                # bedrock bed
                bedrock_b = "Bedrock Bed"
                bedrock_hp = 32
                bedrock_en = 22
                bedrock_m = bedrock_throw
                bedrock_mn = bedrock_thrown
                bedrock_men = bedrock_throwen
                bedrock_m2 = bedrock_crush
                bedrock_m2n = bedrock_crushn
                bedrock_m2en = bedrock_crushen
                bedrock_s = 18

                # Quest Bed
                quest_b = "Quest Bed"
                quest_hp = 28
                quest_en = 29
                quest_m = rainbow_blast
                quest_mn = rainbow_blastn
                quest_men = rainbow_blasten
                quest_m2 = magical_wall
                quest_m2n = magical_walln
                quest_m2en = magical_wallen
                quest_s = 24.5

                # math bed
                math_b = "Math Bed"
                math_hp = 21
                math_en = 19
                math_m = confusion
                math_mn = confusionn
                math_men = confusionen
                math_m2 = homework
                math_m2n = homeworkn
                math_m2en = homeworken
                math_s = 23.5

                # apple bed
                apple_b = "Apple Bed"
                apple_hp = 22
                apple_en = 22
                apple_m = apple_drop
                apple_mn = apple_dropn
                apple_men = apple_dropen
                apple_m2 = apple_rain
                apple_m2n = apple_rainn
                apple_m2en = apple_rainen
                apple_s = 23

                # Dirty Bed
                dirty_b = "Dirty Bed"
                dirty_hp = 24
                dirty_en = 23
                dirty_m = mud_wave
                dirty_mn = mud_waven
                dirty_men = mud_waveen
                dirty_m2 = mud_blast
                dirty_m2n = mud_blastn
                dirty_m2en = mud_blasten
                dirty_s = 15

                # Garbage bed
                garbage_b = "Garbage Bed"
                garbage_hp = 28
                garbage_en = 28
                garbage_m = banana_peel
                garbage_mn = banana_peeln
                garbage_men = banana_peelen
                garbage_m2 = toxic_slap
                garbage_m2n = toxic_slapn
                garbage_m2en = toxic_slapen
                garbage_s = 22

                # Stone bed
                stone_b = "Stone Bed"
                stone_hp = 29
                stone_en = 22
                stone_m = crush
                stone_mn = crushn
                stone_men = crushen
                stone_m2 = stone_slam
                stone_m2n = stone_slamn
                stone_m2en = stone_slamen
                stone_s = 22

                # Diamond bed
                diamond_b = "Diamond Bed"
                diamond_hp = 30
                diamond_en = 22
                diamond_m = shine
                diamond_mn = shinen
                diamond_men = shineen
                diamond_m2 = diamond_beam
                diamond_m2n = diamond_beamn
                diamond_m2en = diamond_beamen
                diamond_s = 20

                # Winning bed
                win_b = "Winning Bed"
                win_hp = 26
                win_en = 23
                win_m = winning_slash
                win_mn = winning_slashn
                win_men = winning_slashen
                win_m2 = champion_strike
                win_m2n = champion_striken
                win_m2en = champion_strikeen
                win_s = 24

                # Combat Bed
                combat_b = "Combat Bed"
                combat_hp = 28
                combat_en = 33
                combat_m = punch_revolver
                combat_mn = punch_revolvern
                combat_men = punch_revolveren
                combat_m2 = fist_barrage
                combat_m2n = fist_barragen
                combat_m2en = fist_barrageen
                combat_s = 24



                # start
                print("You've Entered The Battle District...")
                time.sleep(2)
                print("")
                lala = True
                while lala == True:
                    print("")
                    print("")
                    print("Choose a bed to battle with")
                    if dream_bed == True:
                        print("dream bed")
                    if math_bed == True:
                        print("math bed")
                    if apple_bed == True:
                        print("apple bed")
                    if dirty_bed == True:
                        print("dirty bed")
                    if garbage_bed == True:
                        print("garbage bed")
                    if underwater_bed == True:
                        print("underwater bed")
                    if space_bed == True:
                        print("space bed")
                    if nuclear_bed == True:
                        print("nuclear bed")
                    if stone_bed == True:
                        print("stone bed")
                    if diamond_bed == True:
                        print("diamond bed")
                    if bedrock_bed == True:
                        print("bedrock bed")
                    if quest_bed == True:
                        print("quest bed")
                    if time_bed == True:
                        print("time waster bed")
                    if gold_bed==True:
                        print("gold bed")
                    if magma_bed==True:
                        print("magma bed")
                    if secret_agent_bed==True:
                        print("secret agent bed")
                    if love_bed==True:
                        print("love bed")
                    if winning_bed == True:
                        print("winning bed")
                    if combat_bed == True:
                        print("combat bed")
                    bchooser = input("")
                    if bchooser == "secret agent bed" and secret_agent_bed == True:
                        print("______________________")
                        print("Secret Agent Bed")
                        print("HitPoints: " + str(secret_hp))
                        print("Energy: " + str(secret_en))
                        print("Speed: " + str(secret_s))
                        print("Moves:")
                        print("tricky punch: dmg: 8 / cost: 7")
                        print("heal up: heal: 6 / cost: 7.5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "love bed" and love_bed == True:
                        print("______________________")
                        print("Love Bed")
                        print("HitPoints: " + str(lo_hp))
                        print("Energy: " + str(lo_en))
                        print("Speed: " + str(lo_s))
                        print("Moves:")
                        print("love arrows: dmg: 5.5 / cost: 5")
                        print("love beam: dmg: 7 / cost: 6")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "dream bed" and dream_bed == True:
                        print("______________________")
                        print("Dream Bed")
                        print("HitPoints: " + str(dream_hp))
                        print("Energy: " + str(dream_en))
                        print("Speed: " + str(dream_s))
                        print("Moves:")
                        print("nightmare: dmg: 4 / cost: 3")
                        print("dream reaper: dmg: 5.5 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "math bed" and math_bed == True:
                        print("")
                        print("______________________")
                        print("Math Bed")
                        print("HitPoints: " + str(math_hp))
                        print("Energy: " + str(math_en))
                        print("Speed: " + str(math_s))
                        print("Moves:")
                        print("confusion: dmg: 5 / cost: 4")
                        print("homework: dmg: 6.5 / cost: 6")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "apple bed" and apple_bed == True:
                        print("")
                        print("______________________")
                        print("Apple Bed")
                        print("HitPoints: " + str(apple_hp))
                        print("Energy: " + str(apple_en))
                        print("Speed: " + str(apple_s))
                        print("Moves:")
                        print("apple rain: dmg: 7 / cost: 6")
                        print("apple drop: dmg: 5 / cost: 4")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "dirty bed" and dirty_bed == True:
                        print("______________________")
                        print("Dirty Bed")
                        print("HitPoints: " + str(dirty_hp))
                        print("Energy: " + str(dirty_en))
                        print("Speed: " + str(dirty_s))
                        print("Moves:")
                        print("mud wave: dmg: 7 / cost: 6")
                        print("mud blast: dmg: 6 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "garbage bed" and garbage_bed == True:
                        print("")
                        print("______________________")
                        print("Garbage Bed")
                        print("HitPoints: " + str(garbage_hp))
                        print("Energy: " + str(garbage_en))
                        print("Speed: " + str(garbage_s))
                        print("Moves:")
                        print("banana peel: dmg: 8 / cost: 7")
                        print("toxic slap: dmg: 6.5 / cost: 6")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "underwater bed" and underwater_bed == True:
                        print("")
                        print("______________________")
                        print("Underwater Bed")
                        print("HitPoints: " + str(uw_hp))
                        print("Energy: " + str(uw_en))
                        print("Speed: " + str(uw_s))
                        print("Moves:")
                        print("bloody water: dmg: 5 / cost: 4")
                        print("underwater pull: dmg: 7 / cost: 6")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "space bed" and space_bed == True:
                        print("")
                        print("______________________")
                        print("Space Bed")
                        print("HitPoints: " + str(space_hp))
                        print("Energy: " + str(space_en))
                        print("Speed: " + str(space_s))
                        print("Moves:")
                        print("void: dmg: 5 / cost: 4")
                        print("pressure: dmg: 7.5 / cost: 7")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "nuclear bed" and nuclear_bed == True:
                        print("")
                        print("______________________")
                        print("Nuclear Bed")
                        print("HitPoints: " + str(nuclear_hp))
                        print("Energy: " + str(nuclear_en))
                        print("Speed: " + str(nuclear_s))
                        print("Moves:")
                        print("nuke: dmg: 9 / cost: 8")
                        print("explode: dmg: 6 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "stone bed" and stone_bed == True:
                        print("")
                        print("______________________")
                        print("Stone Bed")
                        print("HitPoints: " + str(stone_hp))
                        print("Energy: " + str(stone_en))
                        print("Speed: " + str(stone_s))
                        print("Moves:")
                        print("crush: dmg: 5 / cost: 4")
                        print("stone slam: dmg: 6 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "diamond bed" and diamond_bed == True:
                        print("")
                        print("______________________")
                        print("Diamond Bed")
                        print("HitPoints: " + str(diamond_hp))
                        print("Energy: " + str(diamond_en))
                        print("Speed: " + str(diamond_s))
                        print("Moves:")
                        print("shine: dmg: 4 / cost: 3")
                        print("diamond beam: dmg: 5 / cost: 4")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "bedrock bed" and bedrock_bed == True:
                        print("______________________")
                        print("Bedrock Bed")
                        print("HitPoints: " + str(bedrock_hp))
                        print("Energy: " + str(bedrock_en))
                        print("Speed: " + str(bedrock_s))
                        print("Moves:")
                        print("bedrock crush: dmg: 5 / cost: 4")
                        print("bedrock throw: dmg: 4 / cost: 3")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "quest bed" and quest_bed == True:
                        print("")
                        print("______________________")
                        print("Quest Bed")
                        print("HitPoints: " + str(quest_hp))
                        print("Energy: " + str(quest_en))
                        print("Speed: " + str(quest_s))
                        print("Moves:")
                        print("Rainbow Blast: dmg: 9 / cost: 8")
                        print("magical wall : dmg: 6 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "time waster bed" and time_bed == True:
                        print("")
                        print("______________________")
                        print("Time Waster Bed")
                        print("HitPoints: " + str(time_hp))
                        print("Energy: " + str(time_en))
                        print("Speed: " + str(time_s))
                        print("Moves:")
                        print("times up: dmg: 6 / cost: 5")
                        print("time explosion: dmg: 4 / cost: 3")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "gold bed" and gold_bed == True:
                        print("")
                        print("______________________")
                        print("Gold Bed")
                        print("HitPoints: " + str(gold_hp))
                        print("Energy: " + str(gold_en))
                        print("Speed: " + str(gold_s))
                        print("Moves:")
                        print("gold meteor: dmg: 6 / cost: 5")
                        print("gold smash: dmg: 5 / cost: 4")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "magma bed" and magma_bed==True:
                        print("")
                        print("______________________")
                        print("Magma Bed")
                        print("HitPoints: " + str(magma_hp))
                        print("Energy: " + str(magma_en))
                        print("Speed: " + str(magma_s))
                        print("Moves:")
                        print("magma meteors: dmg: 8 / cost: 7")
                        print("magma fist: dmg: 6.5 / cost: 6")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "winning bed" and winning_bed == True:
                        print("")
                        print("______________________")
                        print("Winning Bed")
                        print("HitPoints: " + str(win_hp))
                        print("Energy: " + str(win_en))
                        print("Speed: " + str(win_s))
                        print("Moves:")
                        print("champion strike: dmg: 7 / cost: 6")
                        print("winning slash: dmg: 6 / cost: 5")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    elif bchooser == "combat bed" and combat_bed == True:
                        print("")
                        print("______________________")
                        print("Combat Bed")
                        print("HitPoints: " + str(combat_hp))
                        print("Energy: " + str(combat_en))
                        print("Speed: " + str(combat_s))
                        print("Moves:")
                        print("punch revolver: dmg: 6 / cost: 5")
                        print("fist barrage: dmg: 10 / cost: 9")
                        print("")
                        print("Are you sure you want to choose this bed? (yes/no)")
                        chosealr = input("")
                        if chosealr == "no":
                            continue
                        if chosealr == "yes":
                            print("")
                    else:
                        continue
                    while 1:
                        print("________________________")
                        print("Battle Points: " + str(bp))
                        print("teleport back")
                        print("change bed")
                        print("battle")
                        battle = input("")
                        if battle == "teleport back":
                            print("Teleporting back...")
                            time.sleep(1.2)
                            lala = False
                            break
                        if battle == "change bed":
                            break
                        if battle == "battle":
                            if bchooser == "dream bed":
                                chosen = dream_b
                                chosen_hp = dream_hp
                                chosen_en = dream_en
                                chosen_m = dream_m
                                chosen_m2 = dream_m2
                                chosen_mn = dream_mn
                                chosen_m2n = dream_m2n
                                chosen_men = dream_men
                                chosen_m2en = dream_m2en
                                chosen_s = dream_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 6.8
                                    chosen_m2 = 4.1
                            elif bchooser == "math bed":
                                chosen = math_b
                                chosen_hp = math_hp
                                chosen_en = math_en
                                chosen_m = math_m
                                chosen_m2 = math_m2
                                chosen_mn = math_mn
                                chosen_m2n = math_m2n
                                chosen_men = math_men
                                chosen_m2en = math_m2en
                                chosen_s = math_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 5
                                    chosen_m2 = 6.8
                            elif bchooser == "apple bed":
                                chosen = apple_b
                                chosen_hp = apple_hp
                                chosen_en = apple_en
                                chosen_m = apple_m
                                chosen_m2 = apple_m2
                                chosen_mn = apple_mn
                                chosen_m2n = apple_m2n
                                chosen_men = apple_men
                                chosen_m2en = apple_m2en
                                chosen_s = apple_s
                                if dmg_o==True:
                                    chosen_m = 6.2
                                    chosen_m2 = 8.7
                            elif bchooser == "dirty bed":
                                chosen = dirty_b
                                chosen_hp = dirty_hp
                                chosen_en = dirty_en
                                chosen_m = dirty_m
                                chosen_m2 = dirty_m2
                                chosen_mn = dirty_mn
                                chosen_m2n = dirty_m2n
                                chosen_men = dirty_men
                                chosen_m2en = dirty_m2en
                                chosen_s = dirty_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 8.7
                                    chosen_m2 = 6.2
                            elif bchooser == "garbage bed":
                                chosen = garbage_b
                                chosen_hp = garbage_hp
                                chosen_en = garbage_en
                                chosen_m = garbage_m
                                chosen_m2 = garbage_m2
                                chosen_mn = garbage_mn
                                chosen_m2n = garbage_m2n
                                chosen_men = garbage_men
                                chosen_m2en = garbage_m2en
                                chosen_s = garbage_s
                                if dmg_o==True:
                                    chosen_m = 10
                                    chosen_m2 = 8.1
                            elif bchooser == "underwater bed":
                                chosen = uw_b
                                chosen_hp = uw_hp
                                chosen_en = uw_en
                                chosen_m = uw_m
                                chosen_m2 = uw_m2
                                chosen_mn = uw_mn
                                chosen_m2n = uw_m2n
                                chosen_men = uw_men
                                chosen_m2en = uw_m2en
                                chosen_s = uw_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 8.7
                                    chosen_m2 = 6.2
                            elif bchooser == "space bed":
                                chosen = space_b
                                chosen_hp = space_hp
                                chosen_en = space_en
                                chosen_m = space_m
                                chosen_m2 = space_m2
                                chosen_mn = space_mn
                                chosen_m2n = space_m2n
                                chosen_men = space_men
                                chosen_m2en = space_m2en
                                chosen_s = space_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 5
                                    chosen_m2 = 8.7
                            elif bchooser == "nuclear bed":
                                chosen = nuclear_b
                                chosen_hp = nuclear_hp
                                chosen_en = nuclear_en
                                chosen_m = nuclear_m
                                chosen_m2 = nuclear_m2
                                chosen_mn = nuclear_mn
                                chosen_m2n = nuclear_m2n
                                chosen_men = nuclear_men
                                chosen_m2en = nuclear_m2en
                                chosen_s = nuclear_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 11.2
                                    chosen_m2 = 7.5
                            elif bchooser == "stone bed":
                                chosen = stone_b
                                chosen_hp = stone_hp
                                chosen_en = stone_en
                                chosen_m = stone_m
                                chosen_m2 = stone_m2
                                chosen_mn = stone_mn
                                chosen_m2n = stone_m2n
                                chosen_men = stone_men
                                chosen_m2en = stone_m2en
                                chosen_s = stone_s
                                if dmg_o==True:
                                    chosen_m = 6.2
                                    chosen_m2 = 7.5
                            elif bchooser == "diamond bed":
                                chosen = diamond_b
                                chosen_hp = diamond_hp
                                chosen_en = diamond_en
                                chosen_m = diamond_m
                                chosen_m2 = diamond_m2
                                chosen_mn = diamond_mn
                                chosen_m2n = diamond_m2n
                                chosen_men = diamond_men
                                chosen_m2en = diamond_m2en
                                chosen_s = diamond_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 5
                                    chosen_m2 = 6.2
                            elif bchooser == "bedrock bed":
                                chosen = bedrock_b
                                chosen_hp = bedrock_hp
                                chosen_en = bedrock_en
                                chosen_m = bedrock_m
                                chosen_m2 = bedrock_m2
                                chosen_mn = bedrock_mn
                                chosen_m2n = bedrock_m2n
                                chosen_men = bedrock_men
                                chosen_m2en = bedrock_m2en
                                chosen_s = bedrock_s
                                if dmg_o==True:
                                    chosen_m = 5
                                    chosen_m2 = 6.2
                            elif bchooser == "quest bed":
                                chosen = quest_b
                                chosen_hp = quest_hp
                                chosen_en = quest_en
                                chosen_m = quest_m
                                chosen_m2 = quest_m2
                                chosen_mn = quest_mn
                                chosen_m2n = quest_m2n
                                chosen_men = quest_men
                                chosen_m2en = quest_m2en
                                chosen_s = quest_s
                                if dmg_o==True:
                                    chosen_m = 11.2
                                    chosen_m2 = 7.5
                            elif bchooser == "time waster bed":
                                chosen = time_b
                                chosen_hp = time_hp
                                chosen_en = time_en
                                chosen_m = time_m
                                chosen_m2 = time_m2
                                chosen_mn = time_mn
                                chosen_m2n = time_m2n
                                chosen_men = time_men
                                chosen_m2en = time_m2en
                                chosen_s = time_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 5
                                    chosen_m2 = 7.5
                            if bchooser == "gold bed":
                                chosen = gold_b
                                chosen_hp = gold_hp
                                chosen_en = gold_en
                                chosen_m = gold_m
                                chosen_m2 = gold_m2
                                chosen_mn = gold_mn
                                chosen_m2n = gold_m2n
                                chosen_men = gold_men
                                chosen_m2en = gold_m2en
                                chosen_s = gold_s
                                print("")
                                if dmg_o==True:
                                    chosen_m = 7.5
                                    chosen_m2 = 6.2
                            elif bchooser == "magma bed":
                                chosen = magma_b
                                chosen_hp = magma_hp
                                chosen_en = magma_en
                                chosen_m = magma_m
                                chosen_m2 = magma_m2
                                chosen_mn = magma_mn
                                chosen_m2n = magma_m2n
                                chosen_men = magma_men
                                chosen_m2en = magma_m2en
                                chosen_s = magma_s
                                if dmg_o == True:
                                    chosen_m = 10
                                    chosen_m2 = 8.1
                            elif bchooser == "secret agent bed":
                                chosen = secret_b
                                chosen_hp = secret_hp
                                chosen_en = secret_en
                                chosen_m = secret_m
                                chosen_h = secret_h
                                chosen_mn = secret_mn
                                chosen_hn = secret_hn
                                chosen_men = secret_men
                                chosen_hen = secret_hen
                                chosen_s = secret_s
                                if dmg_o == True:
                                    chosen_m = 8.7
                                    
                            elif bchooser == "love bed":
                                chosen = lo_b
                                chosen_hp = lo_hp
                                chosen_en = lo_en
                                chosen_m = lo_m
                                chosen_m2 = lo_m2
                                chosen_mn = lo_mn
                                chosen_m2n = lo_m2n
                                chosen_men = lo_men
                                chosen_m2en = lo_m2en
                                chosen_s = lo_s
                                if dmg_o == True:
                                    chosen_m = 6.8
                                    chosen_m2 = 8.7
                                    
                            elif bchooser == "winning bed":
                                chosen = win_b
                                chosen_hp = win_hp
                                chosen_en = win_en
                                chosen_m = win_m
                                chosen_m2 = win_m2
                                chosen_mn = win_mn
                                chosen_m2n = win_m2n
                                chosen_men = win_men
                                chosen_m2en = win_m2en
                                chosen_s = win_s
                                if dmg_o==True:
                                    chosen_m = 7.5
                                    chosen_m2 = 8.7
                            elif bchooser == "combat bed":
                                chosen = combat_b
                                chosen_hp = combat_hp
                                chosen_en = combat_en
                                chosen_m = combat_m
                                chosen_m2 = combat_m2
                                chosen_mn = combat_mn
                                chosen_m2n = combat_m2n
                                chosen_men = combat_men
                                chosen_m2en = combat_m2en
                                chosen_s = combat_s
                                if dmg_o == True:
                                    chosen_m = 7.5
                                    chosen_m2 = 12.5
                            if tank_a == True:
                                chosen_hp = chosen_hp + 5
                            if en_c == True:
                                chosen_en = chosen_en + 5
                            if sp_d==True:
                                chosen_s = chosen_s + 3
                            if chosen!=secret_b:
                                chosen_h = 0
                                chosen_hn = " | "
                                chosen_hen = 0
                            if chosen==secret_b:
                                chosen_m2 = 0
                                chosen_m2n = " | "
                                chosen_m2en = 0
                            print("")
                            print("")
                            print("")
                            print("Searching for a battle...")
                            print("")
                            btips = ['If your Opponent used the same bed as yours you will always be faster', 'Losing all of your energy can also cause your bed to faint!', 'if you do not want to use any move just type something else than the name of the move', 'All beds under the rarity of Very Rare are not battle beds like common and uncommon']
                            btipsr = random.choice(btips)
                            print("Tip: " + btipsr)
                            time.sleep(5)
                            print("")
                            print("")
                            print("")
                            npc = False
                            npcn = ['Abdul', 'Rehan', 'Kevin', 'Jimmy', 'Jeremey', 'Mariam', 'Fatima', 'Lia', 'Jessie',
                                    'Maya', 'Ninja Boy', 'Ninja Girl', 'Rich Man', 'Rich Woman', 'Scientist', 'Teacher']
                            npcnr = random.choice(npcn)
                            npcnj = "".join(npcnr)
                            npc = npcnj
                            chosenl = [dream_b, math_b, apple_b, dirty_b, garbage_b, uw_b, space_b, nuclear_b, stone_b,
                                       diamond_b, bedrock_b, quest_b, time_b, gold_b, magma_bed, win_b, combat_b, secret_b, lo_b]
                            chosenr = random.choice(chosenl)
                            chosenc = chosenr
                            if chosenc == dream_b:
                                chosenc = dream_b
                                chosenc_hp = dream_hp
                                chosenc_en = dream_en
                                chosenc_m = dream_m
                                chosenc_m2 = dream_m2
                                chosenc_mn = dream_mn
                                chosenc_m2n = dream_m2n
                                chosenc_men = dream_men
                                chosenc_m2en = dream_m2en
                                chosenc_s = dream_s
                            if chosenc == math_b:
                                chosenc = math_b
                                chosenc_hp = math_hp
                                chosenc_en = math_en
                                chosenc_m = math_m
                                chosenc_m2 = math_m2
                                chosenc_mn = math_mn
                                chosenc_m2n = math_m2n
                                chosenc_men = math_men
                                chosenc_m2en = math_m2en
                                chosenc_s = math_s
                            if chosenc == apple_b:
                                chosenc = apple_b
                                chosenc_hp = apple_hp
                                chosenc_en = apple_en
                                chosenc_m = apple_m
                                chosenc_m2 = apple_m2
                                chosenc_mn = apple_mn
                                chosenc_m2n = apple_m2n
                                chosenc_men = apple_men
                                chosenc_m2en = apple_m2en
                                chosenc_s = apple_s
                            if chosenc == dirty_b:
                                chosenc = dirty_b
                                chosenc_hp = dirty_hp
                                chosenc_en = dirty_en
                                chosenc_m = dirty_m
                                chosenc_m2 = dirty_m2
                                chosenc_mn = dirty_mn
                                chosenc_m2n = dirty_m2n
                                chosenc_men = dirty_men
                                chosenc_m2en = dirty_m2en
                                chosenc_s = dirty_s
                            if chosenc == garbage_b:
                                chosenc = garbage_b
                                chosenc_hp = garbage_hp
                                chosenc_en = garbage_en
                                chosenc_m = garbage_m
                                chosenc_m2 = garbage_m2
                                chosenc_mn = garbage_mn
                                chosenc_m2n = garbage_m2n
                                chosenc_men = garbage_men
                                chosenc_m2en = garbage_m2en
                                chosenc_s = garbage_s
                            if chosenc == uw_b:
                                chosenc = uw_b
                                chosenc_hp = uw_hp
                                chosenc_en = uw_en
                                chosenc_m = uw_m
                                chosenc_m2 = uw_m2
                                chosenc_mn = uw_mn
                                chosenc_m2n = uw_m2n
                                chosenc_men = uw_men
                                chosenc_m2en = uw_m2en
                                chosenc_s = uw_s
                            if chosenc == space_b:
                                chosenc = space_b
                                chosenc_hp = space_hp
                                chosenc_en = space_en
                                chosenc_m = space_m
                                chosenc_m2 = space_m2
                                chosenc_mn = space_mn
                                chosenc_m2n = space_m2n
                                chosenc_men = space_men
                                chosenc_m2en = space_m2en
                                chosenc_s = space_s
                            if chosenc == nuclear_b:
                                chosenc = nuclear_b
                                chosenc_hp = nuclear_hp
                                chosenc_en = nuclear_en
                                chosenc_m = nuclear_m
                                chosenc_m2 = nuclear_m2
                                chosenc_mn = nuclear_mn
                                chosenc_m2n = nuclear_m2n
                                chosenc_men = nuclear_men
                                chosenc_m2en = nuclear_m2en
                                chosenc_s = nuclear_s
                            if chosenc == stone_b:
                                chosenc = stone_b
                                chosenc_hp = stone_hp
                                chosenc_en = stone_en
                                chosenc_m = stone_m
                                chosenc_m2 = stone_m2
                                chosenc_mn = stone_mn
                                chosenc_m2n = stone_m2n
                                chosenc_men = stone_men
                                chosenc_m2en = stone_m2en
                                chosenc_s = stone_s
                            if chosenc == diamond_b:
                                chosenc = diamond_b
                                chosenc_hp = diamond_hp
                                chosenc_en = diamond_en
                                chosenc_m = diamond_m
                                chosenc_m2 = diamond_m2
                                chosenc_mn = diamond_mn
                                chosenc_m2n = diamond_m2n
                                chosenc_men = diamond_men
                                chosenc_m2en = diamond_m2en
                                chosenc_s = diamond_s
                            if chosenc == bedrock_b:
                                chosenc = bedrock_b
                                chosenc_hp = bedrock_hp
                                chosenc_en = bedrock_en
                                chosenc_m = bedrock_m
                                chosenc_m2 = bedrock_m2
                                chosenc_mn = bedrock_mn
                                chosenc_m2n = bedrock_m2n
                                chosenc_men = bedrock_men
                                chosenc_m2en = bedrock_m2en
                                chosenc_s = bedrock_s
                            if chosenc == quest_b:
                                chosenc = quest_b
                                chosenc_hp = quest_hp
                                chosenc_en = quest_en
                                chosenc_m = quest_m
                                chosenc_m2 = quest_m2
                                chosenc_mn = quest_mn
                                chosenc_m2n = quest_m2n
                                chosenc_men = quest_men
                                chosenc_m2en = quest_m2en
                                chosenc_s = quest_s
                            if chosenc == time_b:
                                chosenc = time_b
                                chosenc_hp = time_hp
                                chosenc_en = time_en
                                chosenc_m = time_m
                                chosenc_m2 = time_m2
                                chosenc_mn = time_mn
                                chosenc_m2n = time_m2n
                                chosenc_men = time_men
                                chosenc_m2en = time_m2en
                                chosenc_s = time_s
                                print("")
                            chosenc = chosenr
                            if chosenc == gold_b:
                                chosenc = gold_b
                                chosenc_hp = gold_hp
                                chosenc_en = gold_en
                                chosenc_m = gold_m
                                chosenc_m2 = gold_m2
                                chosenc_mn = gold_mn
                                chosenc_m2n = gold_m2n
                                chosenc_men = gold_men
                                chosenc_m2en = gold_m2en
                                chosenc_s = gold_s
                            if chosenc == magma_b:
                                chosenc = magma_b
                                chosenc_hp = magma_hp
                                chosenc_en = magma_en
                                chosenc_m = magma_m
                                chosenc_m2 = magma_m2
                                chosenc_mn = magma_mn
                                chosenc_m2n = magma_m2n
                                chosenc_men = magma_men
                                chosenc_m2en = magma_m2en
                                chosenc_s = magma_s
                            if chosenc == win_b:
                                chosenc = win_b
                                chosenc_hp = win_hp
                                chosenc_en = win_en
                                chosenc_m = win_m
                                chosenc_m2 = win_m2
                                chosenc_mn = win_mn
                                chosenc_m2n = win_m2n
                                chosenc_men = win_men
                                chosenc_m2en = win_m2en
                                chosenc_s = win_s
                            if chosenc == secret_b:
                                chosenc = secret_b
                                chosenc_hp = secret_hp
                                chosenc_en = secret_en
                                chosenc_m = secret_m
                                chosenc_h = secret_h
                                chosenc_mn = secret_mn
                                chosenc_hn = secret_hn
                                chosenc_men = secret_men
                                chosenc_hen = secret_hen
                                chosenc_s = secret_s
                            if chosenc == lo_b:
                                chosenc = lo_b
                                chosenc_hp = lo_hp
                                chosenc_en = lo_en
                                chosenc_m = lo_m
                                chosenc_m2 = lo_m2
                                chosenc_mn = lo_mn
                                chosenc_m2n = lo_m2n
                                chosenc_men = lo_men
                                chosenc_m2en = lo_m2en
                                chosenc_s = lo_s
                            if chosenc == combat_b:
                                chosenc = combat_b
                                chosenc_hp = combat_hp
                                chosenc_en = combat_en
                                chosenc_m = combat_m
                                chosenc_m2 = combat_m2
                                chosenc_mn = combat_mn
                                chosenc_m2n = combat_m2n
                                chosenc_men = combat_men
                                chosenc_m2en = combat_m2en
                                chosenc_s = combat_s
                                print("")
                            if chosenc!=secret_b:
                                chosenc_h = 0
                                chosenc_hn = ""
                                chosenc_hen = 0
                            if chosenc==secret_b:
                                chosenc_m2 = 0
                                chosenc_m2n = ""
                                chosenc_m2en = 0
                            print("")
                            print("")
                            print("Battle Started!")
                            time.sleep(1)
                            print(name + " VS " + npc)
                            time.sleep(3)
                            print(name + ": " + chosen + " Go!")
                            heal_cc = False
                            if dmg_o==True:
                                print("you equipped the damage orb to your bed")
                                time.sleep(1)
                            if en_c==True:
                                print("you equipped the energy coat to your bed")
                                time.sleep(1)
                            if tank_a==True:
                                print("you equipped the tanky armor to your bed")
                                time.sleep(1)
                            if sp_d==True:
                                print("you equipped the speed drink to your bed")
                                time.sleep(1)
                            if heal_c==True:
                                time.sleep(1)
                                print("you equipped the heal charm to your bed")
                            time.sleep(3)
                            print(str(npc) + ": " + str(chosenc) + " Go!")
                            battlei = ['nothing', 'nothing', 'nothing', 'nothing', 'nothing', 'nothing', 'nothing',
                                       'nothing', 'nothing', 'nothing', 'nothing', 'nothing', 'nothing', 'nothing',
                                       'nothing', 'nothing', 'heal', 'speed', 'energy', 'tanky']
                            battleir = random.choice(battlei)
                            battleij = "".join(battleir)
                            if battleij == 'nothing':
                                ""
                            if battleij == 'heal':
                                time.sleep(2)
                                print(npc + " Equipped an heal charm to there bed")
                                heal_cc = True
                            if battleij == 'speed':
                                time.sleep(2)
                                print(npc + " Equipped an speed drink to there bed")
                                chosenc_s = chosenc_s + 3
                            if battleij == 'energy':
                                time.sleep(2)
                                print(npc + " Equipped an energy coat to there bed")
                                chosenc_en = chosenc_en + 5
                            if battleij == 'tanky':
                                time.sleep(2)
                                print(npc + " Equipped an tanky armor to there bed")
                                chosenc_hp = chosenc_hp + 5
                            time.sleep(3)
                            while 1:
                                if float(chosen_hp) <= 0 or float(chosen_en) <= 0 or float(chosenc_hp) <= 0 or float(
                                        chosenc_en) <= 0:
                                    if float(chosen_hp) <= 0 or float(chosen_en) <= 0:
                                        print(chosen + " Fainted!")
                                        time.sleep(3.5)
                                        print(npc + " Won!")
                                        time.sleep(3)
                                        print("")
                                        print("")
                                        break
                                    if float(chosenc_hp) <= 0 or float(chosenc_en) <= 0:
                                        print("Opposing " + chosenc + " Fainted!")
                                        time.sleep(3.5)
                                        print(name + " Won!")
                                        time.sleep(3)
                                        print("")
                                        if winning_bed == False:
                                            print("(Winning Bed) Unlocked! type (beds) to check out your collection!")
                                            time.sleep(3)
                                            winning_bed = True
                                            bed_c = bed_c + 1
                                            levelexp=levelexp+7
                                        bed_winc = bed_winc + 1
                                        print("")
                                        if bp_m == False:
                                            print("+1 Battle Point!")
                                            bp = bp + 1
                                        if bp_m == True and advbp_m==False:
                                            print("+2 Battle Points!")
                                            bp = bp + 2
                                        if advbp_m==True:
                                            print("+3 Battle Points!")
                                            bp = bp + 3
                                        time.sleep(2.5)
                                        break
                                if chosenc!=secret_b:
                                    npc_l = [chosenc_mn, chosenc_m2n]
                                    npc_r = random.choice(npc_l)
                                    npc_j = "".join(npc_r)
                                if chosenc==secret_b:
                                    npc_l = [chosenc_mn, chosenc_hn]
                                    npc_r = random.choice(npc_l)
                                    npc_j = "".join(npc_r)
                                print("")
                                print("________________________________________")
                                print(npc + ": " + chosenc + " | HP- " + str(chosenc_hp) + " | Energy - " + str(
                                    chosenc_en))
                                print("________________________________________")
                                print("")
                                print(
                                    name + ": " + chosen + " | HP- " + str(chosen_hp) + " | Energy- " + str(chosen_en))
                                print("________________________________________")
                                print("Moves:")
                                print("")
                                print("")
                                print(chosen_mn + "     " + chosen_m2n + "     " + chosen_hn)
                                mvchoose = input("")
                                if mvchoose!=mvchoose.capitalize() or mvchoose==mvchoose.upper() or mvchoose==mvchoose.capitalize():
                                    mvchoose = mvchoose.lower()
                                if chosen_s >= chosenc_s:
                                    if mvchoose == chosen_mn:
                                        chosenc_hp = chosenc_hp - chosen_m
                                        chosen_en = chosen_en - chosen_men
                                        print(chosen + " Used " + chosen_mn + "!")
                                        if dmg_o == True:
                                            time.sleep(3)
                                            print("The Damage Orb Increased the damage of the move!")
                                        time.sleep(2.5)
                                        print("Opposing " + chosenc + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if mvchoose == chosen_m2n:
                                        chosenc_hp = chosenc_hp - chosen_m2
                                        chosen_en = chosen_en - chosen_m2en
                                        print(chosen + " Used " + chosen_m2n + "!")
                                        if dmg_o == True:
                                            time.sleep(3)
                                            print("The Damage Orb Increased the damage of the move!")
                                        time.sleep(2.5)
                                        print("Opposing " + chosenc + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if mvchoose == chosen_hn:
                                        chosen_hp = chosen_hp +chosen_h
                                        chosen_en = chosen_en - chosen_hen
                                        print(chosen + " Used " + chosen_hn + "!")
                                        time.sleep(3)
                                        print(chosen + " Healed Up!")
                                        time.sleep(2.5)
                                    if float(chosen_hp) <= 0 or float(chosen_en) <= 0 or float(
                                            chosenc_hp) <= 0 or float(chosenc_en) <= 0:
                                        if float(chosen_hp) <= 0 or float(chosen_en) <= 0:
                                            print(chosen + " Fainted!")
                                            time.sleep(3.5)
                                            print(npc + " Won!")
                                            time.sleep(3)
                                            print("")
                                            print("")
                                            break
                                        if float(chosenc_hp) <= 0 or float(chosenc_en) <= 0:
                                            print("Opposing " + chosenc + " Fainted!")
                                            time.sleep(3.5)
                                            print(name + " Won!")
                                            time.sleep(3)
                                            print("")
                                            if winning_bed == False:
                                                print(
                                                    "(Winning Bed) Unlocked! type (beds) to check out your collection!")
                                                time.sleep(3)
                                                winning_bed = True
                                                bed_c = bed_c + 1
                                                levelexp=levelexp+7
                                            bed_winc = bed_winc + 1
                                            print("")
                                            print("")
                                            if bp_m == False:
                                                print("+1 Battle Point!")
                                                bp = bp + 1
                                            if bp_m == True and advbp_m == False:
                                                print("+2 Battle Points!")
                                                bp = bp + 2
                                            if advbp_m == True:
                                                print("+3 Battle Points!")
                                                bp = bp + 3
                                            time.sleep(2.5)
                                            break
                                    if npc_j == chosenc_mn:
                                        chosen_hp = chosen_hp - chosenc_m
                                        chosenc_en = chosenc_en - chosenc_men
                                        print("Opposing " + chosenc + " Used " + chosenc_mn + "!")
                                        time.sleep(3)
                                        print(chosen + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if npc_j == chosenc_m2n:
                                        chosen_hp = chosen_hp - chosenc_m2
                                        chosenc_en = chosenc_en - chosenc_m2en
                                        print("Opposing " + chosenc + " Used " + chosenc_m2n + "!")
                                        time.sleep(3)
                                        print(chosen + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if npc_j == chosenc_hn:
                                        chosenc_hp = chosenc_hp +chosenc_h
                                        chosenc_en = chosenc_en - chosenc_hen
                                        print("Opposing " + chosenc + " Used " + chosenc_hn + "!")
                                        time.sleep(3)
                                        print("Opposing " + chosenc + " Healed Up!")
                                        time.sleep(2.5)
                                    if heal_c == True:
                                        time.sleep(0)
                                        chosen_hp = chosen_hp + 1.5
                                        print(chosen + " gained a little bit of health thanks to the heal charm")
                                        time.sleep(2.5)
                                    if heal_cc == True:
                                        chosenc_hp = chosenc_hp + 1.5
                                        time.sleep(0)
                                        print(chosenc + " gained a little bit of health thanks to the heal charm")
                                        time.sleep(2.5)
                                if chosenc_s > chosen_s:
                                    if npc_j == chosenc_mn:
                                        chosen_hp = chosen_hp - chosenc_m
                                        chosenc_en = chosenc_en - chosenc_men
                                        print("Opposing " + chosenc + " Used " + chosenc_mn + "!")
                                        time.sleep(3)
                                        print(chosen + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if npc_j == chosenc_m2n:
                                        chosen_hp = chosen_hp - chosenc_m2
                                        chosenc_en = chosenc_en - chosenc_m2en
                                        print("Opposing " + chosenc + " Used " + chosenc_m2n + "!")
                                        time.sleep(3)
                                        print(chosen + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if npc_j == chosenc_hn:
                                        chosenc_hp = chosenc_hp +chosenc_h
                                        chosenc_en = chosenc_en - chosenc_hen
                                        print("Opposing " + chosenc + " Used " + chosenc_hn + "!")
                                        time.sleep(3)
                                        print("Opposing " + chosenc + " Healed Up!")
                                        time.sleep(2.5)
                                    if float(chosen_hp) <= 0 or float(chosen_en) <= 0 or float(
                                            chosenc_hp) <= 0 or float(chosenc_en) <= 0:
                                        if float(chosen_hp) <= 0 or float(chosen_en) <= 0:
                                            print(chosen + " Fainted!")
                                            time.sleep(3.5)
                                            print(npc + " Won!")
                                            time.sleep(3)
                                            print("")
                                            print("")
                                            break
                                        if float(chosenc_hp) <= 0 or float(chosenc_en) <= 0:
                                            print("Opposing " + chosenc + " Fainted!")
                                            time.sleep(3.5)
                                            print(name + " Won!")
                                            time.sleep(3)
                                            print("")
                                            if winning_bed == False:
                                                print(
                                                    "(Winning Bed) Unlocked! type (beds) to check out your collection!")
                                                time.sleep(3)
                                                winning_bed = True
                                                bed_c = bed_c + 1
                                                levelexp=levelexp+7
                                            print("")
                                            bed_winc = bed_winc + 1
                                            if bp_m == False:
                                                print("+1 Battle Point!")
                                                bp = bp + 1
                                            if bp_m == True and advbp_m == False:
                                                print("+2 Battle Points!")
                                                bp = bp + 2
                                            if advbp_m == True:
                                                print("+3 Battle Points!")
                                                bp = bp + 3
                                            time.sleep(2.5)
                                            break
                                    if mvchoose == chosen_mn:
                                        chosenc_hp = chosenc_hp - chosen_m
                                        chosen_en = chosen_en - chosen_men
                                        print(chosen + " Used " + chosen_mn + "!")
                                        if dmg_o == True:
                                            time.sleep(3)
                                            print("The Damage Orb Increased the damage of the move!")
                                        time.sleep(2.5)
                                        print("Opposing " + chosenc + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if mvchoose == chosen_m2n:
                                        chosenc_hp = chosenc_hp - chosen_m2
                                        chosen_en = chosen_en - chosen_m2en
                                        print(chosen + " Used " + chosen_m2n + "!")
                                        if dmg_o == True:
                                            time.sleep(3)
                                            print("The Damage Orb Increased the damage of the move!")
                                        time.sleep(2.5)
                                        print("Opposing " + chosenc + " Lost Some Health!")
                                        time.sleep(2.5)
                                    if mvchoose == chosen_hn:
                                        chosen_hp = chosen_hp +chosen_h
                                        chosen_en = chosen_en - chosen_hen
                                        print(chosen + " Used " + chosen_hn + "!")
                                        time.sleep(3)
                                        print(chosen + " Healed Up!")
                                        time.sleep(2.5)
                                    if heal_c == True:
                                        time.sleep(0)
                                        chosen_hp = chosen_hp + 1.5
                                        print(chosen + " gained a little bit of health thanks to the heal charm")
                                        time.sleep(2.5)
                                    if heal_cc == True:
                                        chosenc_hp = chosenc_hp + 1.5
                                        time.sleep(0)
                                        print(chosenc + " gained a little bit of health thanks to the heal charm")
                                        time.sleep(2.5);



    # elemental mountain
    if startbed == "elemental mountain":
        print("*you climbed the elemental mountain*")
        time.sleep(2)
        while 1:
            print("")
            print("")
            print("What do you want to do?")
            print("matter trials")
            print("matter mixer")
            print("back")
            matterc = input("")
            if matterc == "matter mixer":
                while 1:
                    print("")
                    print("What aura do you wanna form?")
                    print("earth aura (1fire, 1water, 1plant)")
                    print("air aura (1fire, 1water)")
                    print("fire aura (2fire)")
                    print("close")
                    mmix = input()
                    if mmix == "close":
                        print("")
                        time.sleep(1.2)
                        break
                    if mmix == "earth aura" and fire == 0 or water == 0 and mmix == "earth aura" or plant == 0 and mmix == "earth aura":
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("insufficient requirments...")
                        time.sleep(1.5)
                    if mmix == "earth aura" and fire !=0 and water!=0 and plant!=0:
                        print("")
                        print("You mixed the matters")
                        time.sleep(2)
                        print("...")
                        time.sleep(1)
                        print("You formed a earth aura!")
                        time.sleep(1.5)
                        print("1x earth aura obtained!")
                        time.sleep(2)
                        earth = earth + 1
                        fire = fire - 1
                        water = water - 1
                        plant = plant - 1
                    if mmix == "air aura" and fire == 0 or water == 0 and mmix == "air aura":
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("insufficient requirments...")
                        time.sleep(1.5)
                    if mmix == "air aura" and fire !=0 and water!=0:
                        print("")
                        print("You mixed the matters")
                        time.sleep(2)
                        print("...")
                        time.sleep(1)
                        print("You formed a air aura!")
                        time.sleep(1.5)
                        print("1x air aura obtained!")
                        time.sleep(2)
                        air = air + 1
                        fire = fire - 1
                        water = water - 1
                    if mmix == "fire aura" and fire < 2:
                        print("")
                        print("ERROR")
                        time.sleep(1)
                        print("insufficient requirments...")
                        time.sleep(1.5)
                    if mmix == "fire aura" and fire >=2:
                        print("")
                        print("You mixed the matters")
                        time.sleep(2)
                        print("...")
                        time.sleep(1)
                        print("You formed a fire aura!")
                        time.sleep(1.5)
                        print("1x fire aura obtained!")
                        time.sleep(2)
                        firea = firea + 1
                        fire = fire - 2
            if matterc == "back":
                print("")
                print("*you got out of the elemental mountain...*")
                time.sleep(1.2)
                print("")
                print("")
                break
            if matterc == "matter trials":
                while 1:
                    print("")
                    print("Choose a type of trial")
                    print("puzzle")
                    print("random")
                    print("riddle")
                    print("back")
                    trialc = input("")
                    if trialc == "back":
                        print("")
                        time.sleep(0.7)
                        break
                    if trialc == "riddle":
                        print("")
                        riddlecc = False
                        riddlec = ["1", "2", "3", "4", "5"]
                        riddler = random.choice(riddlec)
                        print("")
                        if riddler=="1":
                            while 1:
                                print("a fruit that is green from the outside and red from the inside")
                                print("give up")
                                riddleo = input("")
                                if riddleo == "watermelon" or riddleo == "watermelons" or riddleo == "a watermelon":
                                    print("correct!")
                                    print("")
                                    riddlecc = True
                                    break
                                if riddleo == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if riddler=="2":
                            while 1:
                                print("a object that floats with no wings or handles")
                                print("give up")
                                riddlet = input("")
                                if riddlet == "cloud" or riddlet == "clouds" or riddlet == "a cloud":
                                    print("correct!")
                                    print("")
                                    riddlecc = True
                                    break
                                if riddlet == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if riddler=="3":
                            while 1:
                                print("a way that no one walked through")
                                print("give up")
                                riddleth = input("")
                                if riddleth == "the milky way" or riddleth == "the milky way galaxy" or riddleth == "milky way" or riddleth == "milky way galaxy":
                                    print("correct!")
                                    print("")
                                    riddlecc = True
                                    break
                                if riddleth == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if riddler=="4":
                            while 1:
                                print("what has legs but cannot walk")
                                print("give up")
                                riddlef = input("")
                                if riddlef == "chair" or riddlef == "chairs" or riddlef == "a chair":
                                    print("correct!")
                                    print("")
                                    riddlecc = True
                                    break
                                if riddlef == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if riddler=="5":
                            while 1:
                                print("what has a head and tail but has no body")
                                print("give up")
                                riddlefi = input("")
                                if riddlefi == "a coin" or riddlefi == "coins" or riddlefi == "coin":
                                    print("correct!")
                                    print("")
                                    riddlecc = True
                                    break
                                if riddlefi == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break                         
                        if riddlecc == True:
                            time.sleep(2)
                            print("")
                            print("")
                            riddlepr = ['fire', 'water', 'plant']
                            riddleprr = random.choice(riddlepr)
                            riddleprt = ['fire', 'water', 'plant']
                            riddleprtr = random.choice(riddleprt)
                            print("you finished the trial")
                            print("")
                            time.sleep(1.5)
                            if riddleprr == "fire":
                                if prizem == False:
                                    fire = fire + 1
                                if prizem == True:
                                    fire = fire + 2
                            if riddleprr == "water":
                                if prizem == False:
                                    water = water + 1
                                if prizem == True:
                                    water = water + 2
                            if riddleprr == "plant":
                                if prizem == False:
                                    plant = plant + 1
                                if prizem == True:
                                    plant = plant + 2
                            if riddleprtr == "fire":
                                if prizem == False:
                                    fire = fire + 1
                                if prizem == True:
                                    fire = fire + 2
                            if riddleprtr == "water":
                                if prizem == False:
                                    water = water + 1
                                if prizem == True:
                                    water = water + 2
                            if riddleprtr == "plant":
                                if prizem == False:
                                    plant = plant + 1
                                if prizem == True:
                                    plant = plant + 2
                            print("you obtained some prizes")
                            time.sleep(1.5)
                            if riddleprr == "fire" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 2x fire matter...")
                                if prizem == True:
                                    print("you obtained 4x fire matter...")
                                time.sleep(2)
                            if riddleprr == "fire" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 1x fire matter and 1x water matter")
                                if prizem == True:
                                    print("you obtained 2x fire matter and 2x water matter")
                                time.sleep(2)
                            if riddleprr == "fire" and riddleprtr == "plant":
                                if prizem == False:
                                    print("you obtained 1x fire matter and 1x plant matter")
                                if prizem == True:
                                    print("you obtained 2x fire matter and 2x plant matter")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 2x water matter...")
                                if prizem == True:
                                    print("you obtained 4x water matter...")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 1x water matter and 1x fire matter...")
                                if prizem == True:
                                    print("you obtained 2x water matter and 2x fire matter...")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "plant":
                                if prizem==False:
                                    print("you obtained 1x water matter and 1x plant matter...")
                                if prizem == True:
                                    print("you obtained 2x water matter and 2x plant matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "plant":
                                if prizem == False:
                                    print("you obtained 2x plant matter...")
                                if prizem == True:
                                    print("you obtained 4x plant matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 1x plant matter and 1x fire matter...")
                                if prizem == True:
                                    print("you obtained 2x plant matter and 2x fire matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 1x plant matter and 1x water matter...")
                                if prizem == True:
                                    print("you obtained 2x plant matter and 2x water matter...")
                                time.sleep(2)
                    if trialc == "random":
                        print("")
                        print("you tried to get a random matter...")
                        time.sleep(2)
                        if chancem == False:
                            randommat = ['fire', 'water', 'plant', 'n', 'n', "n"]
                        if chancem==True:
                            randommat = ['fire', 'water', 'plant']
                        randommatr = random.choice(randommat)
                        if randommatr == "water":
                            if prizem==False:
                                print("you obtained 1x water matter")
                                time.sleep(1.5)
                            
                                water=water+1
                            if prizem==True:
                                print("you obtained 2x water matter")
                                time.sleep(1.5)
                            
                                water=water+2
                        if randommatr == "plant":
                            if prizem == False:
                                print("you obtained 1x plant matter")
                                time.sleep(1.5)
                                plant=plant+1
                            if prizem==True:
                                print("you obtained 2x plant matter")
                                time.sleep(1.5)
                            
                                plant=plant+2
                        if randommatr == "fire":
                            if prizem==False:
                                print("you obtained 1x fire matter")
                                time.sleep(1.5)
                                fire=fire+1
                            if prizem==True:
                                print("you obtained 2x fire matter")
                                time.sleep(1.5)
                                fire=fire+2
                        if randommatr == "n":
                            print("you failed obtaining a matter")
                            time.sleep(1.5)
                    if trialc == "puzzle":
                        print("")
                        puzzlecc = False
                        puzzlec = ["1", "2", "3", "4", "5"]
                        puzzler = random.choice(puzzlec)
                        print("")
                        if puzzler=="1":
                            while 1:
                                print("Solve the puzzle")
                                print("- - 3 - 4 - -")
                                print("2 - - - - 6 3")
                                print("- 1 - 5 - - -")
                                print("give up")
                                puzzleo = input("")
                                if puzzleo == "2135463":
                                    print("correct!")
                                    print("")
                                    puzzlecc = True
                                    break
                                if puzzleo == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if puzzler=="2":
                            while 1:
                                print("Solve the puzzle")
                                print("9 - 3 - - - -")
                                print("- - - - 0 6 -")
                                print("- 2 - 6 - - 1")
                                print("give up")
                                puzzlet = input("")
                                if puzzlet == "9236061":
                                    print("correct!")
                                    print("")
                                    puzzlecc = True
                                    break
                                if puzzlet == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if puzzler=="3":
                            while 1:
                                print("Solve the puzzle")
                                print("9 2 - - - - 5")
                                print("- - - - 6 6 -")
                                print("- - 5 5 - - -")
                                print("give up")
                                puzzleth = input("")
                                if puzzleth == "9255665":
                                    print("correct!")
                                    print("")
                                    puzzlecc = True
                                    break
                                if puzzleth == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if puzzler=="4":
                            while 1:
                                print("Solve the puzzle")
                                print("- - 2 - - - 3")
                                print("- 6 - 4 0 6 -")
                                print("0 - - - - - -")
                                print("give up")
                                puzzlet = input("")
                                if puzzlet == "0624063":
                                    print("correct!")
                                    print("")
                                    puzzlecc = True
                                    break
                                if puzzlet == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if puzzler=="5":
                            while 1:
                                print("Solve the puzzle")
                                print("6 - - 1 - - 3")
                                print("- - 8 - 3 - -")
                                print("- 5 - - - 0 -")
                                print("give up")
                                puzzleth = input("")
                                if puzzleth == "6581303":
                                    print("correct!")
                                    print("")
                                    puzzlecc = True
                                    break
                                if puzzleth == "give up":
                                    print("")
                                    print("*you gave up*")
                                    time.sleep(1.5)
                                    print("")
                                    break
                        if puzzlecc == True:
                            time.sleep(2)
                            print("")
                            print("")
                            riddlepr = ['fire', 'water', 'plant']
                            riddleprr = random.choice(riddlepr)
                            riddleprt = ['fire', 'water', 'plant']
                            riddleprtr = random.choice(riddleprt)
                            print("you finished the trial")
                            print("")
                            time.sleep(1.5)
                            if riddleprr == "fire":
                                if prizem == False:
                                    fire = fire + 1
                                if prizem == True:
                                    fire = fire + 2
                            if riddleprr == "water":
                                if prizem == False:
                                    water = water + 1
                                if prizem == True:
                                    water = water + 2
                            if riddleprr == "plant":
                                if prizem == False:
                                    plant = plant + 1
                                if prizem == True:
                                    plant = plant + 2
                            if riddleprtr == "fire":
                                if prizem == False:
                                    fire = fire + 1
                                if prizem == True:
                                    fire = fire + 2
                            if riddleprtr == "water":
                                if prizem == False:
                                    water = water + 1
                                if prizem == True:
                                    water = water + 2
                            if riddleprtr == "plant":
                                if prizem == False:
                                    plant = plant + 1
                                if prizem == True:
                                    plant = plant + 2
                            print("you obtained some prizes")
                            time.sleep(1.5)
                            if riddleprr == "fire" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 2x fire matter...")
                                if prizem == True:
                                    print("you obtained 4x fire matter...")
                                time.sleep(2)
                            if riddleprr == "fire" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 1x fire matter and 1x water matter")
                                if prizem == True:
                                    print("you obtained 2x fire matter and 2x water matter")
                                time.sleep(2)
                            if riddleprr == "fire" and riddleprtr == "plant":
                                if prizem == False:
                                    print("you obtained 1x fire matter and 1x plant matter")
                                if prizem == True:
                                    print("you obtained 2x fire matter and 2x plant matter")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 2x water matter...")
                                if prizem == True:
                                    print("you obtained 4x water matter...")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 1x water matter and 1x fire matter...")
                                if prizem == True:
                                    print("you obtained 2x water matter and 2x fire matter...")
                                time.sleep(2)
                            if riddleprr == "water" and riddleprtr == "plant":
                                if prizem==False:
                                    print("you obtained 1x water matter and 1x plant matter...")
                                if prizem == True:
                                    print("you obtained 2x water matter and 2x plant matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "plant":
                                if prizem == False:
                                    print("you obtained 2x plant matter...")
                                if prizem == True:
                                    print("you obtained 4x plant matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "fire":
                                if prizem == False:
                                    print("you obtained 1x plant matter and 1x fire matter...")
                                if prizem == True:
                                    print("you obtained 2x plant matter and 2x fire matter...")
                                time.sleep(2)
                            if riddleprr == "plant" and riddleprtr == "water":
                                if prizem == False:
                                    print("you obtained 1x plant matter and 1x water matter...")
                                if prizem == True:
                                    print("you obtained 2x plant matter and 2x water matter...")
                                time.sleep(2)
    							
    # bed storage
    if startbed == "beds":
        while 1:
            print("")
            print("")
            print("")
            print("Bed Collection: " + str(bed_c) + "/36")
            if proper_form == True:
                if blue_bed == False:
                    print(" 1 - ???????")
                if blue_bed == True:
                    print(" 1 - Blue Bed (Common)")
                if yellow_bed == False:
                    print(" 2 - ??????????")
                if yellow_bed == True:
                    print(" 2 - Yellow Bed (Common)")
                if red_bed == False:
                    print(" 3 - ???????")
                if red_bed == True:
                    print(" 3 - Red Bed (Common)")
                if white_bed == False:
                    print(" 4 - ?????????")
                if white_bed == True:
                    print(" 4 - White Bed (Common)")
                if green_bed == False:
                    print(" 5 - ?????????")
                if green_bed == True:
                    print(" 5 - Green Bed (Uncommon)")
                if purple_bed == False:
                    print(" 6 - ??????????")
                if purple_bed == True:
                    print(" 6 - Purple Bed (Uncommon)")
                if orange_bed == False:
                    print(" 7 - ??????????")
                if orange_bed == True:
                    print(" 7 - Orange Bed (Uncommon)")
                if pink_bed == False:
                    print(" 8 - ????????")
                if pink_bed == True:
                    print(" 8 - Pink Bed (Uncommon)")
                if rainbow_bed == False:
                    print(" 9 - ???????????")
                if rainbow_bed == True:
                    print(" 9 - Rainbow Bed (Rare)")
                if wheeled_bed == False:
                    print("10 - ???????????")
                if wheeled_bed == True:
                    print("10 - Wheeled Bed (Uncommon)")
                if lucky_bed == False:
                    print("11 - ?????????")
                if lucky_bed == True:
                    print("11 - Lucky Bed (Rare)")
                if magical_bed == False:
                    print("12 - ???????????")
                if magical_bed == True:
                    print("12 - Magical Bed (Rare)")
                if dream_bed == False:
                    print("13 - ?????????")
                if dream_bed == True:
                    print("13 - Dream Bed (Very Rare)")
                if car_bed == False:
                    print("14 - ???????")
                if car_bed == True:
                    print("14 - Car Bed (Rare)")
                if stray_bed == False:
                    print("15 - ?????????")
                if stray_bed == True:
                    print("15 - Stray Bed (Rare)")
                if math_bed == False:
                    print("16 - ????????")
                if math_bed == True:
                    print("16 - Math Bed (Very Rare)")
                if apple_bed == False:
                    print("17 - ?????????")
                if apple_bed == True:
                    print("17 - Apple Bed (Very Rare)")
                if dirty_bed == False:
                    print("18 - ?????????")
                if dirty_bed == True:
                    print("18 - Dirty Bed (Very Rare)")
                if garbage_bed == False:
                    print("19 - ???????????")
                if garbage_bed == True:
                    print("19 - Garbage Bed (Extremely Rare)")
                if underwater_bed == False:
                    print("20 - ??????????????")
                if underwater_bed == True:
                    print("20 - Underwater Bed (Very Rare)")
                if rocket_bed_E == False:
                    print("21 - ????????????????")
                if rocket_bed_E == True:
                    print("21 - Rocket Bed - Empty (Uncommon)")
                if rocket_bed_Fb == False:
                    print("22 - ??????????????????")
                if rocket_bed_Fb == True:
                    print("22 - Rocket Bed - Charged (Rare)")
                if space_bed == False:
                    print("23 - ?????????")
                if space_bed == True:
                    print("23 - Space Bed (Very Rare)")
                if nuclear_bed == False:
                    print("24 - ???????????")
                if nuclear_bed == True:
                    print("24 - Nuclear Bed (Very Rare)")
                if stone_bed == False:
                    print("25 - ?????????")
                if stone_bed == True:
                    print("25 - Stone Bed (Very Rare)")
                if diamond_bed == False:
                    print("26 - ???????????")
                if diamond_bed == True:
                    print("26 - Diamond Bed (Very Rare)")
                if bedrock_bed == False:
                    print("27 - ???????????")
                if bedrock_bed == True:
                    print("27 - Bedrock Bed (Extremely Rare)")
                if quest_bed == False:
                    print("28 - ????????")
                if quest_bed == True:
                    print("28 - Quest Bed (Extremely Rare)")
                if time_bed == False:
                    print("29 - ???????????????")
                if time_bed == True:
                    print("29 - Time Waster Bed (Very Rare)")
                if aura_bed==False:
                    print("30 - ????????")
                if aura_bed==True:
                    print("30 - Aura Bed (Rare)")
                if gold_bed==False:
                    print("31 - ????????")
                if gold_bed==True:
                    print("31 - Gold Bed (Very Rare)")
                if magma_bed==False:
                    print("32 - ?????????")
                if magma_bed==True:
                    print("32 - Magma Bed (Very Rare)")
                if secret_agent_bed==False:
                    print("33 - ????????????????")
                if secret_agent_bed==True:
                    print("33 - Secret Agent Bed (Extremely Rare)")
                if winning_bed == False:
                    print("34 - ???????????")
                if winning_bed == True:
                    print("34 - Winning Bed (Very Rare)")
                if combat_bed == False:
                    print("35 - ??????????")
                if combat_bed == True:
                    print("35 - Combat Bed (Extremely Rare)")
                if love_bed==False:
                    print("36 - ????????")
                if love_bed==True:
                    print("36 - Love Bed (Very Rare)")
                print("filter")
                print("back")
                bedsd = input("What do you want to do?")
                if bedsd == "filter":
                    while 1:
                        print("")
                        print("Filter to:")
                        if date_added == True:
                            fltr = input("date added * | proper form")
                            if fltr == "date added":
                                date_added = True
                                proper_form = False
                                break
                            if fltr == "proper form":
                                date_added = False
                                proper_form = True
                                break
                        if proper_form == True:
                            fltr = input("date added | proper form *")
                            if fltr == "date added":
                                date_added = True
                                proper_form = False
                                break
                            if fltr == "proper form":
                                date_added = False
                                proper_form = True
                                break

                if bedsd == "back":
                    print("")
                    print("Closing beds command...")
                    print("")
                    print("")
                    break
                print("")
                print("")
                print("")
            if date_added == True:
                if blue_bed == False:
                    print(" 1 - ???????")
                if blue_bed == True:
                    print(" 1 - Blue Bed (Common)")
                if yellow_bed == False:
                    print(" 2 - ??????????")
                if yellow_bed == True:
                    print(" 2 - Yellow Bed (Common)")
                if wheeled_bed == False:
                    print(" 3 - ???????????")
                if wheeled_bed == True:
                    print(" 3 - Wheeled Bed (Uncommon)")
                if green_bed == False:
                    print(" 4 - ?????????")
                if green_bed == True:
                    print(" 4 - Green Bed (Uncommon)")
                if red_bed == False:
                    print(" 5 - ???????")
                if red_bed == True:
                    print(" 5 - Red Bed (Common)")
                if lucky_bed == False:
                    print(" 6 - ?????????")
                if lucky_bed == True:
                    print(" 6 - Lucky Bed (Rare)")
                if purple_bed == False:
                    print(" 7 - ??????????")
                if purple_bed == True:
                    print(" 7 - Purple Bed (Uncommon)")
                if white_bed == False:
                    print(" 8 - ?????????")
                if white_bed == True:
                    print(" 8 - White Bed (Common)")
                if pink_bed == False:
                    print(" 9 - ????????")
                if pink_bed == True:
                    print(" 9 - Pink Bed (Uncommon)")
                if rainbow_bed == False:
                    print("10 - ???????????")
                if rainbow_bed == True:
                    print("10 - Rainbow Bed (Rare)")
                if rocket_bed_E == False:
                    print("11 - ??????????????????")
                if rocket_bed_E == True:
                    print("11 - Rocket Bed - Empty (Uncommon)")
                if rocket_bed_Fb == False:
                    print("12 - ????????????????????")
                if rocket_bed_Fb == True:
                    print("12 - Rocket Bed - Charged (Rare)")
                if space_bed == False:
                    print("13 - ?????????")
                if space_bed == True:
                    print("13 - Space Bed (Very Rare)")
                if magical_bed == False:
                    print("14 - ???????????")
                if magical_bed == True:
                    print("14 - Magical Bed (Rare)")
                if nuclear_bed == False:
                    print("15 - ???????????")
                if nuclear_bed == True:
                    print("15 - Nuclear Bed (Very Rare)")
                if stone_bed == False:
                    print("16 - ?????????")
                if stone_bed == True:
                    print("16 - Stone Bed (Very Rare)")
                if diamond_bed == False:
                    print("17 - ???????????")
                if diamond_bed == True:
                    print("17 - Diamond Bed (Very Rare)")
                if bedrock_bed == False:
                    print("18 - ???????????")
                if bedrock_bed == True:
                    print("18 - Bedrock Bed (Extremely Rare)")
                if quest_bed == False:
                    print("19 - ?????????")
                if quest_bed == True:
                    print("19 - Quest Bed (Extremely Rare)")
                if time_bed == False:
                    print("20 - ???????????????")
                if time_bed == True:
                    print("20 - Time Waster Bed (Very Rare)")
                if dirty_bed == False:
                    print("21 - ?????????")
                if dirty_bed == True:
                    print("21 - Dirty Bed (Very Rare)")
                if garbage_bed == False:
                    print("22 - ???????????")
                if garbage_bed == True:
                    print("22 - Garbage Bed (Extremely Rare)")
                if apple_bed == False:
                    print("23 - ?????????")
                if apple_bed == True:
                    print("23 - Apple Bed (Very Rare)")
                if math_bed == False:
                    print("24 - ????????")
                if math_bed == True:
                    print("24 - Math Bed (Very Rare)")
                if underwater_bed == False:
                    print("25 - ??????????????")
                if underwater_bed == True:
                    print("25 - Underwater Bed (Very Rare)")
                if stray_bed == False:
                    print("26 - ?????????")
                if stray_bed == True:
                    print("26 - Stray Bed (Rare)")
                if car_bed == False:
                    print("27 - ???????")
                if car_bed == True:
                    print("27 - Car Bed (Rare)")
                if dream_bed == False:
                    print("28 - ?????????")
                if dream_bed == True:
                    print("28 - Dream Bed (Rare)")
                if orange_bed == False:
                    print("29 - ?????????")
                if orange_bed == True:
                    print("29 - Orange Bed (Uncommon)")
                if winning_bed == False:
                    print("30 - ???????????")
                if winning_bed == True:
                    print("30 - Winning Bed (Very Rare)")
                if combat_bed == False:
                    print("31 - ??????????")
                if combat_bed == True:
                    print("31 - Combat Bed (Extremely Rare)")
                if gold_bed==False:
                    print("32 - ????????")
                if gold_bed==True:
                    print("32 - Gold Bed (Very Rare)")
                if aura_bed==False:
                    print("33 - ????????")
                if aura_bed==True:
                    print("33 - Aura Bed (Rare)")
                if magma_bed==False:
                    print("34 - ?????????")
                if magma_bed==True:
                    print("34 - Magma Bed (Very Rare)")
                if secret_agent_bed==False:
                    print("35 - ????????????????")
                if secret_agent_bed==True:
                    print("35 - Secret Agent Bed (Extremely Rare)")
                if love_bed==False:
                    print("36 - ????????")
                if love_bed==True:
                    print("36 - Love Bed (Very Rare)")
                print("filter")
                print("back")
                bedsd = input("What do you want to do?")
                if bedsd == "filter":
                    while 1:
                        print("")
                        print("Filter to:")
                        if date_added == True:
                            fltr = input("date added * | proper form")
                            if fltr == "date added":
                                date_added = True
                                proper_form = False
                                break
                            if fltr == "proper form":
                                date_added = False
                                proper_form = True
                                break
                        if proper_form == True:
                            fltr = input("date added | proper form *")
                            if fltr == "date added":
                                date_added = True
                                proper_form = False
                                break
                            if fltr == "proper form":
                                date_added = False
                                proper_form = True
                                break

                if bedsd == "back":
                    print("")
                    print("Closing beds command...")
                    print("")
                    print("")
                    break
                print("")
                print("")
                print("")

    # win message
    if love_bed == True and secret_agent_bed == True and magma_bed == True and aura_bed == True and gold_bed==True and combat_bed == True and winning_bed == True and car_bed == True and stray_bed == True and orange_bed == True and dream_bed == True and underwater_bed == True and math_bed == True and dirty_bed == True and garbage_bed == True and apple_bed == True and time_bed == True and quest_bed == True and nuclear_bed == True and magical_bed == True and stone_bed == True and diamond_bed == True and bedrock_bed == True and rocket_bed_E == True and rocket_bed_Fb == True and space_bed == True and rainbow_bed == True and pink_bed == True and purple_bed == True and lucky_bed == True and white_bed == True and red_bed == True and green_bed == True and yellow_bed == True and wheeled_bed == True and blue_bed == True:
        while win_ms == True:
            print("___________________________________________________")
            print("YOU FOUND ALL OF THE BEDS")
            time.sleep(3)
            print("🎉CONGRATULATIONS!!!!🎉")
            print("___________________________________________________")
            time.sleep(9)
            print("")
            print("(Credits) Unlocked! type (credits) to check it out")
            time.sleep(3)
            win_mmm = True
            win_ms = False
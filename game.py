print("**************************************  Welcome to Adventure Time  **************************************")
PlayerName=input("Put Your Name ")                                                                                             
print("Hello,",PlayerName ,"welcome to Adventure Time, HOPE U ENJOY ")
import time
from random import*
time.sleep(0.5)
print("use /help")
fit=0
wallet=0
inventory=""
while fit==0:
    command=input("-------------------")
    if command=="/help":
        print("*****************************************************  HELP LIST  *****************************************************")
        time.sleep(0.5)
        print("/shop = take u to the shop")
        print("/hunt = to hunt ")
        print("/fish = to fish")
        print("/wallet = to cheak ur wallet")
        print("/inventory = to cheak ur inventory")
        print("/profil = to see ur profile")
    #shop
    elif command=="/shop":
        print("*****************************************************  THE SHOP  *****************************************************")
        print(" SHOP :                                                                                                             ")
        print("          |||   Weapons   |||   |||   Cost   |||")
        print("          |||    knife    |||   |||    90    |||")
        print("          |||     Axe     |||   |||    110   |||")
        print("          |||    sword    |||   |||    250   |||")
        print("          |||     gun     |||   |||    550   |||")
        time.sleep(1.5)
        buy=input("if u will buy somthing YES/NO ")
        if buy=="yes" or buy=="YES" :
            buywep=input("what do u need ")
            #knife
            if buywep=="knife" or buywep=="KNIFE":
                if wallet>90:
                    wallet=wallet-90
                    print("a KNIFE added in your inventory")
                    inventory+="Knife, "
                else:
                    print("you don't have enought money to buy this item, cheak your /wallet")
            #axe
            elif buywep=="axe" or buywep=="AXE":
                if wallet>110:
                    wallet=wallet-110
                    print("an AXE added in your inventory")
                    inventory+="Axe, "
                else:
                    print("you don't have enought money to buy this item, cheak your /wallet")
            #sword
            elif buywep=="sword" or buywep=="SWORD":
                if wallet>250:
                    wallet=wallet-250
                    print("a SWORD added in your inventory")
                    inventory+="Sword, "
                else:
                    print("you don't have enought money to buy this item, cheak your /wallet")
            #gun
            elif buywep=="gun" or buywep=="GUN":
                if wallet>550:
                    wallet=wallet-550
                    print("a GUN added in your inventory")
                    inventory+="Gun, "
                else:
                    print("you don't have enought money to buy this item, cheak your /wallet")       
            else:
                print("????")
        else:
            print("see u soon")
    #hunt
    elif command=="/hunt":
        t=randint(1,7)
        if t==1:
            print("u just hunted a goat +20 coins")
            wallet+=20
        elif t==2:
            print("u just hunted a Skunk +10 coins")
            wallet+=10
        elif t==3:
            print("u just hunted a pig +15 coins")
            wallet+=15
        elif t==4:
            print("u just hunted a sheep +30 coins")
            wallet+=30
        elif t==5:
            print("u got nothing, maybe next time")
        elif t==6:
            print("u got nothing, maybe next time")
        else:
            print("u got nothing, maybe next time")
    #hunt
    elif command=="/fish":
        t=randint(1,7)
        if t==1:
            print("You cast out your line and brought back a fish +10 coins ")
            wallet+=10
        elif t==2:
            print("You cast out your line and brought back a rare fish +50 coins")
            wallet+=50
        elif t==3:
            print("You cast out your line and brought back a garbage +2 coins")
            wallet+=2
        elif t==4:
            print("You cast out your line and brought back a Seaweed +5 coins")
            wallet+=5
        elif t==5:
            print("You cast out your line and brought back nothing, maybe next time")
        elif t==6:
            print("You cast out your line and brought back nothing, maybe next time")
        else:
            print("You cast out your line and brought back nothing, maybe next time")
    #wallet
    elif command=="/wallet":
        print("you have ",wallet,"coin in your wallet")
    #inventory
    elif command=="/inventory":
        if inventory=="":
            print("your inventory is empty")
        else:
            print("you have",inventory,"in your inventory")
    elif command=="/profile":
        print("*****************************************************  PROFILE  *****************************************************")
        print("")
        print("                                                  Name =  ",PlayerName,)
        print("                                                  wallet =  ",wallet,)
        print("                                                  inventory = ",inventory)

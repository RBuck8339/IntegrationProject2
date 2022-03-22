#Ronan Buck
#This is a small text-based boss fight
print("Hello There!"*6)
print("This is your fight against Boss")
print("You have 4 spells to use against Boss")
print("Your spells are: \n Fireball \n Thunder \n Punch \n Barrier")
print("Input your spell in order to attack or defend")
print("Fireball, Thunder, and Punch attack Boss, and Barrier will heal you")
print("You have 500 health and Boss has 2000 health, KILL IT!")
import random
PlayerHealth=int(500)
BossHealth=int(2000)
Fireball=int(2**5+50) #equals 82
Thunder=int(100000//1000-30) #equals 70
Punch=int(4*25*2/3) #equals 66
Barrier=int(9%2*50+25) #equals 75
def NewFight(GodHealth,PlayerHealth,burn): #end fight
    Fireball = int(2 ** 5 + 60)  # equals 92
    Thunder = int(100000 // 1000 - 30+60)  # equals 100
    Punch = int(6*25/2)  # equals 75
    Barrier = int(9 % 2 * 50 + 40)  # equals 90
    if GodHealth > 0 and PlayerHealth > 0:
        while burn>=75: #burn mechanic using random module
            print("God was hurt by burn")
            BurnDecrease=random.randint(0,7)
            GodHealth=GodHealth-30
            burn=burn-BurnDecrease
            if burn<75: #burning
                print("God's health is now: ", (GodHealth), sep="")
        Attack = input("Please choose a spell: ")
        if Attack == "Fireball" or Attack=="fireball":
            print("God's health is: ", int(GodHealth - Fireball), sep="")
            GodHealth = int(GodHealth - Fireball)
            print("God attacks, you now have: ", PlayerHealth - 50, sep="")
            PlayerHealth = int(PlayerHealth - 50)
            burn=random.randint(0,100)
            if burn>=75:
                print("You have burned God")
            NewFight(GodHealth, PlayerHealth,burn)
        elif Attack == "Thunder" or Attack=="thunder":
            print("God's health is: ", int(GodHealth - Thunder), sep="")
            GodHealth = int(GodHealth - Thunder)
            print("God attacks you, you now have: ", PlayerHealth-50, sep="")
            PlayerHealth = int(PlayerHealth - 50)
            NewFight(GodHealth, PlayerHealth,burn)
        elif Attack == "Punch" or Attack=="punch":
            print("God's health is: ", int(GodHealth - Punch), sep="")
            GodHealth = int(GodHealth - Punch)
            print("God attacks you,", end="")
            print("you now have: ", PlayerHealth - 50, sep="")
            PlayerHealth = int(PlayerHealth - 50)
            NewFight(GodHealth, PlayerHealth,burn)
        elif Attack == "Barrier" or Attack=="barrier":
            PlayerHealth = int(PlayerHealth + Barrier)  # Heals Player
            print("You now have: ", int(PlayerHealth), "HP", sep="")
            print("God attacks, you now have: ", int(PlayerHealth-50), sep="")
            PlayerHealth = int(PlayerHealth - 50)
            NewFight(GodHealth,PlayerHealth,burn)
        else:
            burn=0
            NewFight(GodHealth,PlayerHealth,burn)
    elif GodHealth <= 0 and PlayerHealth > 0:
        print("You have defeated God")
    elif (GodHealth > 0) and (PlayerHealth <= 0):
        print("You Lost...")
def Ambush(): #if player decides to go home
    print("The Ambusher lunges at you and stabs you")
    print("You have only 25 turns to defeat the Ambusher ", end="")
    print("or else you will bleed out")
    print("Due to your weakness you feel that your barrier is weaker")
    PlayerHealth = 800
    AmbusherHealth = 1250
    Barrier=60
    for x in range(25): #repeated combat system from main, but only 25 turns
        if AmbusherHealth > 0 and PlayerHealth > 0:
            Attack = input("Please choose a spell: ")
            if Attack == "Fireball" or Attack=="fireball":
                print("It's health is: ", int(AmbusherHealth-Fireball),sep="")
                AmbusherHealth = int(BossHealth - Fireball)
                print("Boss attacks, you now have: ", PlayerHealth-50, sep="")
                PlayerHealth = int(PlayerHealth - 50)
            elif Attack == "Thunder" or Attack=="thunder":
                print("It's health is: ",int(AmbusherHealth-Thunder),sep="")
                AmbusherHealth = int(AmbusherHealth - Punch)
                print("It attacks you, you now have: ",PlayerHealth-50,sep="")
                PlayerHealth = int(PlayerHealth - 50)
            elif Attack == "Punch" or Attack=="punch":
                print("It's health is: ",int(AmbusherHealth-Punch),sep="")
                AmbusherHealth=int(AmbusherHealth-Punch)
                print("Ambusher attacks you,", end="")
                print("you now have: ",PlayerHealth -50,sep="")
                PlayerHealth = int(PlayerHealth - 50)
            elif Attack == "Barrier" or Attack=="barrier":
                PlayerHealth = int(PlayerHealth + Barrier)  # Heals Player
                print("You now have: ", int(PlayerHealth), "HP", sep="")
                print("It attacks, you now have: ", PlayerHealth-50,sep="") #see if way to fix characters
                PlayerHealth = int(PlayerHealth - 50)
        elif AmbusherHealth>0 and PlayerHealth<=0:
            print("You lost")
        elif AmbusherHealth<=0 and PlayerHealth>0:
            print("You have defeated the Ambusher")
            print("You treat your wounds and armed with a newfound ",end="")
            print("rage you continue on to fight God himself")
            print("As soon as you see the God of this world, you tremble")
            print("However, you feel your spells get stronger")
            print("Your Fireball now has a chance to burn the target")
            print("Your Thunder is stronger")
            print("Your Punch hits harder")
            print("Your Barrier heals for more")
            GodHealth = 5000
            PlayerHealth = 1500
            burn=0
            NewFight(GodHealth,PlayerHealth,burn)
    print("You have succumbed to your stab wound")
    print("You have died")
def Continue(): #text
    print("After defeating the Boss, you are now able to go home and relax")
    print("You now have a big choice to make")
    print("Say yes to go home to your family, say no to continue fighting")
    answer=input("Would you like to go home or continue fighting?")
    answer=list(answer.upper())
    if answer[0]=="N":
        GodHealth = 5000
        PlayerHealth = 1500
        burn = 0
        NewFight(burn,GodHealth,PlayerHealth)
    elif answer[0]=="Y":
        print("You come home to find your family murdered")
        print("You are attacked by a strong enemy")
        print("It appears mostly human, but its behavior is definitely not")
        Ambush()
    elif answer[0]!="Y" and answer[0]!="N":
        print('Please try again')
        Continue()
def main(PlayerHealth,BossHealth): #the combat system to be repeated
    BossHealth=BossHealth+0
    PlayerHealth=PlayerHealth+0
    if BossHealth>0 and PlayerHealth>0:
        Attack = input("Please choose a spell: ")
        if Attack=="Fireball" or Attack=="fireball":
            print("Boss's health is: ", int(BossHealth-Fireball), sep="")
            BossHealth-=Fireball
            print("Boss attacks, you now have: ", PlayerHealth-50, sep="")
            PlayerHealth=int(PlayerHealth-50)
            main(PlayerHealth,BossHealth)
        elif Attack=="Thunder" or Attack=="thunder":
            print("Boss's health is: ", int(BossHealth-Thunder), sep="")
            BossHealth-=Thunder
            print("Boss attacks you, you now have: ", PlayerHealth-50, sep="")
            PlayerHealth=int(PlayerHealth-50)
            main(PlayerHealth,BossHealth)
        elif Attack=="Punch" or Attack=="punch":
            print("Boss's health is: ", int(BossHealth-Punch), sep="")
            BossHealth-=Punch
            print("Boss attacks you,", end="")
            print("you now have: ", PlayerHealth-50, sep="")
            PlayerHealth=int(PlayerHealth-50)
            main(PlayerHealth,BossHealth)
        elif Attack=="Barrier" or Attack=="barrier":
            PlayerHealth+= Barrier #Heals Player
            print("You now have: ", int(PlayerHealth), "HP", sep="")
            print("Boss attacks, you now have: ", int(PlayerHealth-50),sep="")
            PlayerHealth=int(PlayerHealth-50)
            main(PlayerHealth,BossHealth)
        else:
            print("Please enter a valid spell")
            main(PlayerHealth,BossHealth)
    elif BossHealth<=0 and PlayerHealth>0:
        print("YOU WIN!"+"YOU WIN!"+"YOU WIN!"+"YOU WIN!")
        Continue()
    elif (BossHealth>0) and(PlayerHealth<=0):
        print("You Lost...")
main(PlayerHealth,BossHealth)


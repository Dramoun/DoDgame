from random import randrange

class gameSystem:

  def __init__(self):
    self.stageTimer = 1
    self.stageRand = 1
    self.restRand = 1
    self.diffF = 1
    self.diffP = 1
    self.diffC = 1
    self.diffM = 1
    self.diffB = (self.diffF+self.diffP+self.diffC+self.diffM)/4

  def sRandGen(self):
    self.stageRand = randrange(1,5)

  def restRandGen(self):
    self.restRand = randrange(1,3)
    
  def roadStart(self):
    print("--------------------------")
    print("You wake up on a road.")
    print("Inspect yourself.")
    p1.name = input("What is your name? ")
    print("--------------------------")
    p1.displayStats()
    gs.roadBasic()
    
  def roadBasic(self):
    
    while True:
      print("--------------------------")
      roadInput = input("You are on a road. Do you want to inspect yourself or wonder forward again? ")
    
      if roadInput == "inspect":
        print("--------------------------")
        print("Inspect yourself.")
        p1.displayStats()

      elif roadInput == "wonder":
        print("--------------------------")
        print("You wonder forward to find meaning.")
        gs.combatManager()

      elif roadInput == "admin":
        end = False #test loop boolean

        #test loop
        while end != True:
          print("--------------------------")
          ask = input("What would you like to do? ")
          print("--------------------------")

        #if input is dmg, add or substract the amount to damage stat
          if ask == "dmg":
          
            while True:
              
              try:
                p1.dmgChange(int(input("Input a number: ")))
                break
                
              except ValueError:
                print("!!Write a number!!")

        #if input is hp, add or substract the amount to health stat
          elif ask == "hp":
          
            while True:
              
              try:
                p1.hpChange(int(input("Input a number: ")))
                break
                
              except ValueError:
                print("!!Write a number!!")

        #if input is money, add or substract the amount money stat
          elif ask == "money":
          
            while True:
              
              try:
                p1.moneyChange(int(input("Input a number: ")))
                break
                
              except ValueError:
                print("!!Write a number!!")
                
        #display stats
          elif ask == "stats":
            p1.displayStats()

        #test healing shop
          elif ask == "healShop":
            p1.buyHp()

        #test gym
          elif ask == "gym":
            p1.fitGym()

        #display all commands
          elif ask == "help":
            print("dmg")
            print("hp")
            print("money")
            print("stats")
            print("healShop")
            print("gym")
            print("help")
            print("end")
            print("rand")

        #end program
          elif ask == "end":
            break

          elif ask == "rand":
            x = randrange(10)
            print(x)

        #message if input was not from command list
          else:
            print("Invalid input. Type 'help' for commands.")


      else:
        print("--------------------------")
        print("Options: inspect, wonder")


  def restArea(self):

    print("You enter a shop.")
    print("--------------------------")
    p1.buyHp()
    print("You leave the shop.")
    print("--------------------------")

    print("You enter a gym.")
    print("--------------------------")
    p1.fitGym()
    print("You leave the gym.")
    print("--------------------------")

  def combatManager(self):
    gs.sRandGen()
    
    if gs.stageRand == 1 and self.stageTimer != 3:
      print("You wonder into a forrest and find an enemy. Fight me, coward! ")
      
      while e.hpF > 0 and p1.health > 0:
        e.forestEnemy()

      if e.hpF <= 0:
        print("Forest enemy is ded.")
        self.diffF += 0.1
        e.forestEreset()
        self.stageTimer += 1
        p1.moneyChange(50)
        gs.roadBasic()

      elif p1.health <= 0:
        print("YOu fought him and that was the last thing you did!")
        input()
        exit()
        

    elif gs.stageRand == 2 and self.stageTimer != 3:
      print("You find a cave, go in and find an enemy. You should not have come here, outsider! ")

      while e.hpC > 0 and p1.health > 0:
        e.caveEnemy()

      if e.hpC <= 0:
        print("Cave enemy is ded.")
        self.diffC += 0.1
        e.caveEreset()
        self.stageTimer += 1
        p1.moneyChange(50)
        gs.roadBasic()

      elif p1.health <= 0:
        print("You did not come out of that cave alive and the game end!")
        input()
        exit()


    elif gs.stageRand == 3 and self.stageTimer != 3:
      print("You walked far into the mountain until an enemy blocked your path. Fight me, you ugly creature! ")

      while e.hpM > 0 and p1.health > 0:
        e.mountainEnemy()

      if e.hpM <= 0:
        print("Mountains enemy is ded.")
        self.diffM += 0.1
        e.mountainEreset()
        self.stageTimer += 1
        p1.moneyChange(50)
        gs.roadBasic()

      elif p1.health <= 0:
        print("You were called ugly and crushed to death!")
        input()
        exit()

        
    elif gs.stageRand == 4 and self.stageTimer != 3 :
      print("You wondered into a plain field and a little enemy jumped you. I will cut you to pieces.")

      while e.hpP > 0 and p1.health > 0:
        e.plainEnemy()

      if e.hpP <= 0:
        print("Plains enemy is ded.")
        self.diffP += 0.1
        e.plainEreset()
        self.stageTimer += 1
        p1.moneyChange(50)
        gs.roadBasic()

      elif p1.health <= 0:
        print("You were cut to pieces and the game end!")
        input()
        exit()

    elif self.stageTimer == 3:
      gs.restArea()
      print("A bigger enemy waited for you close to the road. It seems that you have killed his grunts. You will pay with your life, mortal.")
      
      while e.hpB > 0 and p1.health > 0:
        e.bossEnemy()

      if e.hpB <= 0:
        print("Boss  is ded.")
        e.bossEreset()
        self.stageTimer = 1
        p1.health += 50
        p1.moneyChange(200)
        gs.roadBasic()

      elif p1.health <= 0:
        print("You paid with your life and the game end!")
        input()
        exit()


class enemySystem:

  def __init__(self):
    self.hpF = 60 * gs.diffF
    self.dmgF = 10 * gs.diffF
    self.heavyBool = False
    
    self.hpP = 50 * gs.diffP
    self.dmgP = 11 * gs.diffP
    self.plainCount = 0
    
    self.hpC = 40 * gs.diffC
    self.dmgC = 12 * gs.diffC
    self.cavePassive = False
    
    self.hpM = 65 * gs.diffM
    self.dmgM = 5 * gs.diffM
    self.mountainPassive = 2.5 - (self.hpM/round(65 * gs.diffM))
    self.mountainSpecial = False
    
    self.hpB = 200 * gs.diffB
    self.dmgB = 10 * gs.diffB
    
    self.randAttackNum = 1
    self.randAttackNumBoss = 1
    self.bossSpecial = False

  def randAttack(self):
    self.randAttackNum = randrange(1,3)

  def randAttackBoss(self):
    self.randAttackNumBoss = randrange(1,3)#randrange(1,4) if he has 3 attacks in first half
  
  def forestEnemy(self):
    print("--------------------------")
    
    e.randAttack()
    
    while True:
      fightChoice = input("attack, parry or block? ")

      if self.heavyBool == False:
        
        if self.randAttackNum == 1 and fightChoice == "attack":
          p1.health -= e.dmgF
          e.hpF -= p1.damage
          print("You and the enemy both attacked each other.")
          break

        elif self.randAttackNum == 1 and fightChoice == "block":
          print("You blocked an attack from the enemy")
          break

        elif self.randAttackNum == 2 and fightChoice == "attack":
          print("Enemy blocked your attack.")
          self.heavyBool = True
          break

        elif self.randAttackNum == 2 and fightChoice == "block":
          print("You and the enemy both blocked, nothing happends.")
          self.heavyBool = True
          break

        elif self.randAttackNum == 1 and fightChoice == "parry":
          p1.health -= round((e.dmgF)*0.5)
          e.hpF -= round((p1.damage)+((e.dmgF)*0.5))
          print("Enemy attack parried and damage partly reflected.")
          break

        elif self.randAttackNum == 2 and fightChoice == "parry":
          print("Enemy was about to block when he saw you parry nothing, so he bashed you with his shield.")
          p1.health -= round((e.dmgF)*0.25)
          self.heavyBool = True
          break
          
        else:
          print(" ")
          print("Thats not a choice!!")
          
      else:
        
        if fightChoice == "attack":
          p1.health -= round((e.dmgF)*1.5)
          e.hpF -= round((p1.damage)*0.5)
          print("Enemy used great force to attack you and his attack did significantly more damage then yours.")
          self.heavyBool = False
          break
          
        elif fightChoice == "block":
          p1.health -= round((e.dmgF)*0.5)
          print("Heavy attack from the enemy was only partly blocked.")
          self.heavyBool = False
          break
                
        elif fightChoice == "parry":
          e.hpF -= round((e.dmgF)*1.5)
          print("Materfull parry. Enemies attack completely deflected!!")
          self.heavyBool = False
          break
        
        else:
          print(" ")
          print("Thats not a choice!!")
          
  def forestEreset(self):
    self.hpF = round(60 * gs.diffF)
    self.dmgF = round(10 * gs.diffF)
    self.heavyBool = False


  def caveEnemy(self):
    print("--------------------------")
    
    e.randAttack()
    
    while True:
      fightChoice = input("attack, parry or block? ")

      if self.randAttackNum == 1 and fightChoice == "attack":
      
        if self.cavePassive == True:
           p1.health -= (e.dmgC*2)
           print("Enemy critical hit you, but you managed to hit him too.")
           self.cavePassive = False
            
        else:
           p1.health -= e.dmgC
           print("You and the enemy both attacked each other.")
            
        e.hpC -= p1.damage
        break

      elif self.randAttackNum == 1 and fightChoice == "block":

        if self.cavePassive == True:
           print("You blocked a critical attack from the enemy")
           self.cavePassive = False

        else:
           print("You blocked an attack from the enemy")
        
        break

      elif self.randAttackNum == 2 and fightChoice == "attack":
        print("Enemy dodged your attack and stabbed you.")
        self.cavePassive = True
        p1.health -= round(e.dmgC*0.5)
        break

      elif self.randAttackNum == 2 and fightChoice == "block":
        print("You blocked while enemy awaited an attack, nothing happends.")
        break

      elif self.randAttackNum == 1 and fightChoice == "parry":
        
        if self.cavePassive == True:
           e.hpC -= (e.dmgC*2)
           print("Enemy tried to critical hit you, but you parried it.")
           self.cavePassive = False
            
        else:
           p1.health -= round((e.dmgC)*0.5)
           e.hpC -= round((p1.damage)+((e.dmgC)*0.5))
           print("Enemy attack parried and damage partly reflected.")
            
        break

      elif self.randAttackNum == 2 and fightChoice == "parry":
        print("Both of you were ready to counter attack, but noone did.")
        break
          
      else:
        print(" ")
        print("Thats not a choice!!")

  def caveEreset(self):
    self.hpC = round(40 * gs.diffC)
    self.dmgC = round(12 * gs.diffC)
    self.cavePassive = False


  def mountainEnemy(self):
    print("--------------------------")

    e.randAttack()

    while True:
      fightChoice = input("attack, parry or block? ")

      if round(e.hpM/(65 * gs.diffM)) > 0.1 and self.mountainSpecial == True:

        if self.randAttackNum == 1 and fightChoice == "attack":
          p1.health -= round(e.dmgM * self.mountainPassive)
          e.hpM -= p1.damage
          print("You and the enemy both attacked each other.")
          break

        elif self.randAttackNum == 1 and fightChoice == "block":
          print("You blocked an attack from the enemy")
          break

        elif self.randAttackNum == 2 and fightChoice == "attack":
          print("Enemy blocked your attack and cut himself.")
          e.hpM -= round(e.hpM * 0.5)
          self.mountainSpecial = False
          break

        elif self.randAttackNum == 2 and fightChoice == "block":
          print("You blocked while the enemy cut himself")
          e.hpM -= round(e.hpM * 0.5)
          self.mountainSpecial = False
          break

        elif self.randAttackNum == 1 and fightChoice == "parry":
          p1.health -= round((e.dmgM * self.mountainPassive)*0.5)
          e.hpM -= round((p1.damage*0.5)+((e.dmgM * self.mountainPassive)*0.5))
          print("Enemy attack parried and damage partly reflected.")
          break

        elif self.randAttackNum == 2 and fightChoice == "parry":
          print("Enemy was about to cut himself, but you stoped him thinking he was aiming at you.")
          break

      elif self.mountainSpecial == False or round(e.hpM/(65 * gs.diffM)) <= 0.1:
        
        if fightChoice == "attack":
          p1.health -= round(e.dmgM * self.mountainPassive)
          e.hpM -= p1.damage
          print("You and the enemy both attacked each other.")
          self.mountainSpecial = True
          break

        elif fightChoice == "block":
          print("You blocked an attack from the enemy")
          self.mountainSpecial = True
          break

        elif fightChoice == "parry":
          p1.health -= round((e.dmgM * self.mountainPassive)*0.5)
          e.hpM -= round((p1.damage*0.5)+((e.dmgM * self.mountainPassive)*0.5))
          print("Enemy attack parried and damage partly reflected.")
          break
          
      else:
        print(" ")
        print("Thats not a choice!!")

  def mountainEreset(self):
    self.hpM = round(65 * gs.diffM)
    self.dmgM = round(5 * gs.diffM)
    self.mountainSpecial = False
                       

  def plainEnemy(self):
    print("--------------------------")
    
    e.randAttack()
    
    while True:
      fightChoice = input("attack, parry or block? ")

      if self.plainCount < 4:
        
        if self.randAttackNum == 1 and fightChoice == "attack":
          p1.health -= e.dmgP
          e.hpP -= p1.damage
          self.plainCount += 1
          print("You and the enemy both attacked each other.")
          break

        elif self.randAttackNum == 1 and fightChoice == "block":
          print("You blocked an attack from the enemy")
          break

        elif self.randAttackNum == 2 and fightChoice == "attack":
          print("While you were attacking, the enemy succesfully cut you twice.")
          p1.health -= round(e.dmgP*1.5)
          e.hpP -= p1.damage
          self.plainCount += 2
          break

        elif self.randAttackNum == 2 and fightChoice == "block":
          print("You have blocked both enemies cuts.")
          break

        elif self.randAttackNum == 1 and fightChoice == "parry":
          p1.health -= round((e.dmgP)*0.5)
          e.hpP -= round((p1.damage)+((e.dmgP)*0.5))
          print("Enemy attack parried and damage partly reflected.")
          self.plainCount += 1
          break

        elif self.randAttackNum == 2 and fightChoice == "parry":
          print("One of enemies cuts parried, the other hit you.")
          p1.health -= round((e.dmgP)*0.75)
          e.hpP -= round((e.dmgP)*0.75)
          self.plainCount += 1
          break
          
        else:
          print(" ")
          print("Thats not a choice!!")
          
      else:
        
        if fightChoice == "attack":
          p1.health -= round((e.dmgP)*2)
          print("Enemy used great force to attack you and your attacked missed.")
          self.plainCount = 0
          break
          
        elif fightChoice == "block":
          p1.health -= round((e.dmgP)*0.25)
          print("Heavy attack from the enemy was mostly blocked.")
          self.plainCount = 0
          break
                
        elif fightChoice == "parry":
          e.hpP -= round((e.dmgP)*0.5)
          p1.health -= round((e.dmgP)*0.75)
          print("You mostly parried enemies attack and deflected some damage back. ")
          self.plainCount = 0
          break
        
        else:
          print(" ")
          print("Thats not a choice!!")

  def plainEreset(self):
    self.hpP = round(50 * gs.diffP)
    self.dmgP = round(11 * gs.diffP)
    self.plainCount = 0
    

  def bossEnemy(self):
    print("--------------------------")

    e.randAttackBoss()
    e.randAttack()
    
    while True:
      fightChoice = input("attack, parry or block? ")
      
      if round(self.hpB/(200 * gs.diffB)) > 0.5 :

        if self.randAttackNumBoss == 1 and fightChoice == "attack":
          print("You and the boss both attacked.")
          p1.health -= e.dmgB
          e.hpB -= p1.damage
          break

        elif self.randAttackNumBoss == 1 and fightChoice == "block":
          print("You have blocked bosses attack.")
          break

        elif self.randAttackNumBoss == 1 and fightChoice == "parry":
          print("You have partly parried bosses attack and deflected some dmg.")
          p1.health -= round((e.dmgB)*0.5)
          e.hpB -= round((p1.damage)+((e.dmgB)*0.5))
          break

        elif self.randAttackNumBoss == 2 and fightChoice == "attack":
          print("Boss has blocked your attack.")
          break

        elif self.randAttackNumBoss == 2 and fightChoice == "block":
          print("Both you and the boss waited in defence stances.")
          break

        elif self.randAttackNumBoss == 2 and fightChoice == "parry":
          print("You awaited an attack and the boss bashed you with his shield.")
          p1.health -= round(e.dmgB*0.25)
          break
        #first half attack 3 disabled
        """ 
        elif self.randAttackNumBoss == 3 and fightChoice == "attack":
          print("Boss attacked you with great force and made you miss your attack.")
          p1.health -= round(e.dmgB*1.5)
          break

        elif self.randAttackNumBoss == 3 and fightChoice == "block":
          print("You mostly blocked bosses heavy attack.")
          p1.health -= round(e.dmgB*0.5)
          break
        
        elif self.randAttackNumBoss == 3 and fightChoice == "parry":
          print("You have deflected bosses heavy attack.")
          e.hpB -= round(e.dmgB*1.5)
          break

        else:
          print(" ")
          print("Thats not a choice!!")
        """
      else:

        if self.bossSpecial == False:
  
          if self.randAttackNum == 1 and fightChoice == "attack":
            print("You and the boss both attacked.")
            p1.health -= e.dmgB
            e.hpB -= p1.damage
            break

          elif self.randAttackNum == 1 and fightChoice == "block":
            print("You have blocked bosses attack.")
            break

          elif self.randAttackNum == 1 and fightChoice == "parry":
            print("You have partly parried bosses attack and deflected some dmg.")
            p1.health -= round((e.dmgB)*0.5)
            e.hpB -= round((p1.damage)+((e.dmgB)*0.5))
            break

          elif self.randAttackNum == 2 and fightChoice == "attack":
            print("Enemy let you hit him, intentionaly. You managed to do more damage.")
            e.hpB -= round(p1.damage * 1.5)
            self.bossSpecial = True
            break

          elif self.randAttackNum == 2 and fightChoice == "block":
            print("Enemy seems to be growing in size while you are awating an attack. Imposible!")
            self.bossSpecial = True
            break

          elif self.randAttackNum == 2 and fightChoice == "parry":
            print("Enemy seems to be growing in size while you are awating an attack to parry. You quickly cut him.")
            e.hpB -= round(p1.damage * 0.75)
            self.bossSpecial = True
            break

          else:
            print(" ")
            print("Thats not a choice!!")
            
        elif self.bossSpecial == True:

          if fightChoice == "attack":
            print("Huge boss attack you with immese force and you were unable to attack back. Boss grew smaller again.")
            p1.health -= round(e.dmgB * 3)
            self.bossSpecial = False
            break

          elif fightChoice == "block":
            print("You were able to block only some of the damage before boss went back to his normal size.")
            p1.health -= e.dmgB
            self.bossSpecial = False
            break

          elif fightChoice == "parry":
            print("You managed to parry the huge attack boss sent your way, but only deflected some damage. Boss went back to his normal size.")
            e.hpB -= e.dmgB
            self.bossSpecial = False
            break

          else:
            print(" ")
            print("Thats not a choice!!")

          
  def bossEreset(self):
    self.hpB = 200 * gs.diffB
    self.dmgB = 20 * gs.diffB
    self.bossSpecial == False


class Human:
  
  def __init__(self, name, damage, health, money):
    self.name = name
    self.damage = damage
    self.health = health
    self.money = money

  def displayStats(self):
    print("Your status: ")
    print("Name: " + self.name)
    print("Damage: " + str(self.damage))
    print("Health: " + str(self.health))
    print("Money: " + str(self.money))

  def hpChange(self, dmgPoints):
    self.health += dmgPoints

  def dmgChange(self, strPoints):
    self.damage += strPoints
    self.damage = round(self.damage)
    
  def moneyChange(self, moneyPoints):
    self.money += moneyPoints

  #enter the healShop actions
  def buyHp(self):
    print("How much do you want to heal? ")
    numTry = 0

    #angry loop
    while numTry !=3:
      healFor = input("half or full? ")

      #half heal choice check
      if healFor == "half":

        #money check
        if self.money < 50:
          print("Come back with enough money.")
          print("--------------------------")
          break

        #50 hp heal
        elif p1.health < 50:
          p1.hpChange(50)
          p1.moneyChange(-50)
          print("Healed for half, come again!")
          break

        else:
          p1.hpChange(100-p1.health)
          p1.moneyChange(-50)
          print("Healed for half, come again!")
          break

      #full heal choice check
      elif healFor == "full":

        #money check
        if self.money < 150:
          print("Come back with enough money.")
          print("--------------------------")
          break

        #healing missing hp to 100
        else:
          p1.hpChange(100-p1.health)
          p1.moneyChange(-150)
          print("Fully healed, come again!")
          break

      #input anything else then the options
      else:
        print("Thats not an option!")
        numTry +=1

  #enter the gym actions
  def fitGym(self):
    print("How you wanna train? ")
    numTryFit = 0
    powerTrain = 0.2

    #angry loop
    while numTryFit !=2:
      trainFor = input("basic or power? ")

      #basic choice check
      if trainFor == "basic":

        #money check
        if self.money < 50:
          print("Come back with enough money.")
          print("--------------------------")
          break

        #basic damage change
        else:
          p1.dmgChange(self.damage * 0.1)
          powerTrain += 0.1
          p1.moneyChange(-50)
          print("Nice gainz, brother. Come again!")
          break

      #power choice check
      elif trainFor == "power":

        #money check
        if self.money < 250:
          print("Come back with enough money.")
          print("--------------------------")
          break

        #power damage change
        else:
          p1.dmgChange(powerTrain * 10)
          p1.moneyChange(-250)
          print("POWER GAINZ!!!!")
          break

      #input anything else then the options 
      else:
        print("Thats not an option!")
        numTryFit +=1


p1 = Human("example", 15, 100, 0) #shortcut to playerOne class
gs = gameSystem() #shortcut to gameSystem class
e = enemySystem() #shortcut to Enemy class

gs.roadStart()

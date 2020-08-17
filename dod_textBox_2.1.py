"""
game logic start
"""

from random import randrange
import tkinter as tk
import tkinter.font as tkFont

class windowEvents:
  
  def __init__(self):
    self.aB = False
    self.bB = False
    self.pB = False
    self.OneB = False
    self.TwoB = False

  def combatActive(self):
    attackButton["state"] = "normal"
    blockButton["state"] = "normal"
    parryButton["state"] = "normal"

    actionOneButton["state"] = "disabled"
    actionTwoButton["state"] = "disabled"

  def actionActive(self):
    attackButton["state"] = "disabled"
    blockButton["state"] = "disabled"
    parryButton["state"] = "disabled"

    actionOneButton["state"] = "normal"
    actionTwoButton["state"] = "normal"

  def attackButton(self):
    self.aB= True
    gs.roadManager()

  def blockButton(self):
    self.bB = True
    gs.roadManager()

  def parryButton(self):
    self.pB = True
    gs.roadManager()

  def buttonReset(self):
    self.aB = False
    self.bB = False
    self.pB = False
    self.OneB = False
    self.TwoB = False

  def actionOneButton(self):
    self.OneB = True
    gs.roadManager()

  def actionTwoButton(self):
    self.TwoB = True
    gs.roadManager()

class gameSystem:

  def __init__(self):
    self.eKillCount = 0
    self.stageRand = 1
    self.restRand = 1
    self.diffF = 1
    self.diffP = 1
    self.diffC = 1
    self.diffM = 1
    self.diffB = (self.diffF+self.diffP+self.diffC+self.diffM)/4
    self.enemyAlive = False
    self.healShopCount = 0
    self.fitShopCount = 0
    

  def sRandGen(self):
    self.stageRand = randrange(1,5)
    
  def restRandGen(self):
    self.restRand = randrange(1,3)

  def roadManager(self):
    p1.displayStats()
    
    if self.eKillCount == 2 and self.fitShopCount != 2:
      
      if self.eKillCount == 2 and self.healShopCount == 0:
        we.actionActive()
        gs.textEdit("You enter a shop.")
        gs.textEdit("How much you wanna heal? half or full")
        self.healShopCount = 1
        we.buttonReset()

      elif self.eKillCount == 2 and self.healShopCount == 1:
        self.healShopCount = 2
        p1.buyHp()

      elif self.eKillCount == 2 and self.fitShopCount == 0 and self.healShopCount == 2:
        gs.textEdit("You enter a shop.")
        gs.textEdit("How you wanna train? basic or power")
        self.fitShopCount = 1
        we.buttonReset()

      elif self.eKillCount == 2 and self.fitShopCount == 1:
        self.fitShopCount = 2
        p1.fitGym()
        
    else:
      we.combatActive()
      gs.combatManager()
      we.buttonReset()

  def roadStart(self):
    p1.displayStats()
    gs.roadManager()

  def newIsLast(self):
    lastText["text"] = newText["text"]

  def textEdit(self, new):
    gs.newIsLast()
    newText["text"] = new
    
  def combatManager(self):

    if not self.enemyAlive:
      gs.sRandGen()

    if gs.stageRand == 1 and self.eKillCount != 2:
      
      gs.textEdit("You wonder into a forrest and find an enemy. Fight me, coward! ")
      self.enemyAlive = True
      e.forestEnemy()

      if p1.health <= 0:
        gs.textEdit("You fought him and that was the last thing you did!")
        quit()
        
      elif e.hpF <= 0:
        gs.textEdit("Forest enemy is ded. Action button to move forward. ")
        self.diffF += 0.1
        e.forestEreset()
        self.eKillCount += 1
        p1.moneyChange(75)
        self.enemyAlive = False
        we.actionActive()
        we.buttonReset()

    elif gs.stageRand == 2 and self.eKillCount != 2:
      gs.textEdit("You find a cave, go in and find an enemy. You should not have come here, outsider! ")
      self.enemyAlive = True
      e.caveEnemy()
      
      if p1.health <= 0:
        gs.textEdit("You did not come out of that cave alive and the game end!")
        quit()

      elif e.hpC <= 0:
        gs.textEdit("Cave enemy is ded. Action button to move forward. ")
        self.diffC += 0.1
        e.caveEreset()
        self.eKillCount += 1
        p1.moneyChange(75)
        self.enemyAlive = False
        we.actionActive()
        we.buttonReset()

    elif gs.stageRand == 3 and self.eKillCount != 2:
      gs.textEdit("You walked far into the mountain until an enemy blocked your path. Fight me, you ugly creature! ")
      self.enemyAlive = True
      e.mountainEnemy()

      if p1.health <= 0:
        gs.textEdit("You were called ugly and crushed to death!")
        quit()

      elif e.hpM <= 0:
        gs.textEdit("Mountains enemy is ded. Action button to move forward. ")
        self.diffM += 0.1
        e.mountainEreset()
        self.eKillCount += 1
        p1.moneyChange(75)
        self.enemyAlive = False
        we.actionActive()
        we.buttonReset()
        
    elif gs.stageRand == 4 and self.eKillCount != 2 :
      gs.textEdit("You wondered into a plain field and a little enemy jumped you. I will cut you to pieces.")
      self.enemyAlive = True
      e.plainEnemy()

      if p1.health <= 0:
        gs.textEdit("You were cut to pieces and the game end!")
        quit()

      elif e.hpP <= 0:
        gs.textEdit("Plains enemy is ded. Action button to move forward. ")
        self.diffP += 0.1
        e.plainEreset()
        self.eKillCount += 1
        p1.moneyChange(75)
        self.enemyAlive = False
        we.actionActive()
        we.buttonReset()

    elif self.eKillCount == 2:
      gs.textEdit("A bigger enemy waited for you close to the road. It seems that you have killed his grunts. ")
      self.enemyAlive = True
      e.bossEnemy()

      if p1.health <= 0:
        gs.textEdit("You paid with your life and the game end!")
        quit()
        
      elif e.hpB <= 0:
        gs.textEdit("Boss is ded. Action button to move forward. ")
        e.bossEreset()
        self.eKillCount = 0
        p1.health += 50
        p1.moneyChange(150)
        self.enemyAlive = False
        we.actionActive()
        we.buttonReset()
        gs.healShopCount = 0
        gs.fitShopCount = 0

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
    self.dmgB = 8 * gs.diffB
    
    self.randAttackNum = 1
    self.bossBlockSpecial = False
    self.bossSpecial = False

  def randAttack(self):
    self.randAttackNum = randrange(1,3)

  def forestEnemy(self):
    
    e.randAttack()
    gs.textEdit("Attack, Parry or Block? ")

    if self.heavyBool == False:
        
      if self.randAttackNum == 1 and we.aB == True:
        p1.health -= e.dmgF
        e.hpF -= p1.damage
        gs.textEdit("You and the enemy both attacked each other.")

      elif self.randAttackNum == 1 and we.bB == True:
        gs.textEdit("You blocked an attack from the enemy")

      elif self.randAttackNum == 2 and we.aB == True:
        gs.textEdit("Enemy blocked your attack.")
        self.heavyBool = True

      elif self.randAttackNum == 2 and we.bB == True:
        gs.textEdit("You and the enemy both blocked, nothing happends.")
        self.heavyBool = True

      elif self.randAttackNum == 1 and we.pB == True:
        p1.health -= round((e.dmgF)*0.5)
        e.hpF -= round((p1.damage)+((e.dmgF)*0.5))
        gs.textEdit("Enemy attack parried and damage partly reflected.")

      elif self.randAttackNum == 2 and we.pB == True:
        gs.textEdit("Enemy was about to block when he saw you parry nothing, so he bashed you with his shield.")
        p1.health -= round((e.dmgF)*0.25)
        self.heavyBool = True
          
    else:
        
      if we.aB == True:
        p1.health -= round((e.dmgF)*1.5)
        e.hpF -= round((p1.damage)*0.5)
        gs.textEdit("Enemy used great force to attack you and his attack did significantly more damage then yours.")
        self.heavyBool = False
          
      elif we.bB == True:
        p1.health -= round((e.dmgF)*0.5)
        gs.textEdit("Heavy attack from the enemy was only partly blocked.")
        self.heavyBool = False
                
      elif we.pB == True:
        e.hpF -= round((e.dmgF)*1.5)
        gs.textEdit("Materfull parry. Enemies attack completely deflected!!")
        self.heavyBool = False
          
  def forestEreset(self):
    self.hpF = round(60 * gs.diffF)
    self.dmgF = round(10 * gs.diffF)
    self.heavyBool = False

  def caveEnemy(self):

    e.randAttack()
    gs.textEdit("Attack, Parry or Block? ")
      
    if self.randAttackNum == 1 and we.aB == True:
      
      if self.cavePassive == True:
          p1.health -= (e.dmgC*2)
          gs.textEdit("Enemy critical hit you, but you managed to hit him too.")
          self.cavePassive = False
            
      else:
          p1.health -= e.dmgC
          gs.textEdit("You and the enemy both attacked each other.")
            
      e.hpC -= p1.damage

    elif self.randAttackNum == 1 and we.bB == True:

      if self.cavePassive == True:
          gs.textEdit("You blocked a critical attack from the enemy")
          self.cavePassive = False

      else:
          gs.textEdit("You blocked an attack from the enemy")

    elif self.randAttackNum == 2 and we.aB == True:
      gs.textEdit("Enemy dodged your attack and stabbed you.")
      self.cavePassive = True
      p1.health -= round(e.dmgC*0.5)

    elif self.randAttackNum == 2 and we.bB == True:
      gs.textEdit("You blocked while enemy awaited an attack, nothing happends.")

    elif self.randAttackNum == 1 and we.pB == True:
        
      if self.cavePassive == True:
          e.hpC -= (e.dmgC*2)
          gs.textEdit("Enemy tried to critical hit you, but you parried it.")
          self.cavePassive = False
            
      else:
          p1.health -= round((e.dmgC)*0.5)
          e.hpC -= round((p1.damage)+((e.dmgC)*0.5))
          gs.textEdit("Enemy attack parried and damage partly reflected.")

    elif self.randAttackNum == 2 and we.pB == True:
      gs.textEdit("Both of you were ready to counter attack, but noone did.")
          
  def caveEreset(self):
    self.hpC = round(40 * gs.diffC)
    self.dmgC = round(12 * gs.diffC)
    self.cavePassive = False


  def mountainEnemy(self):

    e.randAttack()
    gs.textEdit("Attack, Parry or Block? ")
    
    if round(e.hpM/(65 * gs.diffM)) > 0.1 and self.mountainSpecial == True:

      if self.randAttackNum == 1 and we.aB == True:
        p1.health -= round(e.dmgM * self.mountainPassive)
        e.hpM -= p1.damage
        gs.textEdit("You and the enemy both attacked each other.")

      elif self.randAttackNum == 1 and we.bB == True:
        gs.textEdit("You blocked an attack from the enemy")

      elif self.randAttackNum == 2 and we.aB == True:
        gs.textEdit("Enemy blocked your attack and cut himself.")
        e.hpM -= round(e.hpM * 0.5)
        self.mountainSpecial = False

      elif self.randAttackNum == 2 and we.bB == True:
        gs.textEdit("You blocked while the enemy cut himself")
        e.hpM -= round(e.hpM * 0.5)
        self.mountainSpecial = False

      elif self.randAttackNum == 1 and we.pB == True:
        p1.health -= round((e.dmgM * self.mountainPassive)*0.5)
        e.hpM -= round((p1.damage*0.5)+((e.dmgM * self.mountainPassive)*0.5))
        gs.textEdit("Enemy attack parried and damage partly reflected.")
      elif self.randAttackNum == 2 and we.pB == True:
        gs.textEdit("Enemy was about to cut himself, but you stoped him thinking he was aiming at you.")

    elif self.mountainSpecial == False or round(e.hpM/(65 * gs.diffM)) <= 0.1:
        
      if we.aB == True:
        p1.health -= round(e.dmgM * self.mountainPassive)
        e.hpM -= p1.damage
        gs.textEdit("You and the enemy both attacked each other.")
        self.mountainSpecial = True

      elif we.bB == True:
        gs.textEdit("You blocked an attack from the enemy")
        self.mountainSpecial = True

      elif we.pB == True:
        p1.health -= round((e.dmgM * self.mountainPassive)*0.5)
        e.hpM -= round((p1.damage*0.5)+((e.dmgM * self.mountainPassive)*0.5))
        gs.textEdit("Enemy attack parried and damage partly reflected.")

  def mountainEreset(self):
    self.hpM = round(65 * gs.diffM)
    self.dmgM = round(5 * gs.diffM)
    self.mountainSpecial = False
                       

  def plainEnemy(self):

    e.randAttack()
    gs.textEdit("Attack, Parry or Block? ")
    
    if self.plainCount < 4:
        
      if self.randAttackNum == 1 and we.aB == True:
        p1.health -= e.dmgP
        e.hpP -= p1.damage
        self.plainCount += 1
        gs.textEdit("You and the enemy both attacked each other.")
        
      elif self.randAttackNum == 1 and we.bB == True:
        gs.textEdit("You blocked an attack from the enemy")

      elif self.randAttackNum == 2 and we.aB == True:
        gs.textEdit("While you were attacking, the enemy succesfully cut you twice.")
        p1.health -= round(e.dmgP*1.5)
        e.hpP -= p1.damage
        self.plainCount += 2

      elif self.randAttackNum == 2 and we.bB == True:
        gs.textEdit("You have blocked both enemies cuts.")

      elif self.randAttackNum == 1 and we.pB == True:
        p1.health -= round((e.dmgP)*0.5)
        e.hpP -= round((p1.damage)+((e.dmgP)*0.5))
        gs.textEdit("Enemy attack parried and damage partly reflected.")
        self.plainCount += 1

      elif self.randAttackNum == 2 and we.pB == True:
        gs.textEdit("One of enemies cuts parried, the other hit you.")
        p1.health -= round((e.dmgP)*0.75)
        e.hpP -= round((e.dmgP)*0.75)
        self.plainCount += 1
                
    else:
        
      if we.aB == True:
        p1.health -= round((e.dmgP)*2)
        gs.textEdit("Enemy used great force to attack you and your attacked missed.")
        self.plainCount = 0
          
      elif we.bB == True:
        p1.health -= round((e.dmgP)*0.25)
        gs.textEdit("Heavy attack from the enemy was mostly blocked.")
        self.plainCount = 0
                
      elif we.pB == True:
        e.hpP -= round((e.dmgP)*0.5)
        p1.health -= round((e.dmgP)*0.75)
        gs.textEdit("You mostly parried enemies attack and deflected some damage back. ")
        self.plainCount = 0

  def plainEreset(self):
    self.hpP = round(50 * gs.diffP)
    self.dmgP = round(11 * gs.diffP)
    self.plainCount = 0
    

  def bossEnemy(self):

    e.randAttack()
    gs.textEdit("You will pay with your life, mortal. Attack, Parry or Block? ")

    if round(self.hpB/(200 * gs.diffB)) > 0.5 :
      
      if self.bossBlockSpecial == False:
        
        if self.randAttackNum == 1 and we.aB == True:
          p1.health -= e.dmgB
          e.hpB -= p1.damage
          gs.textEdit("You and the boss both attacked each other.")

        elif self.randAttackNum == 1 and we.bB == True:
          gs.textEdit("You blocked an attack from the boss")

        elif self.randAttackNum == 2 and we.aB == True:
          gs.textEdit("Boss blocked your attack.")
          self.bossBlockSpecial = True

        elif self.randAttackNum == 2 and we.bB == True:
          gs.textEdit("You and the boss both blocked, nothing happends.")
          self.bossBlockSpecial = True

        elif self.randAttackNum == 1 and we.pB == True:
          p1.health -= round((e.dmgB)*0.5)
          e.hpB -= round((p1.damage)+((e.dmgB)*0.5))
          gs.textEdit("Boss attack parried and damage partly reflected.")

        elif self.randAttackNum == 2 and we.pB == True:
          gs.textEdit("Boss was about to block when he saw you parry nothing, so he bashed you with his shield.")
          p1.health -= round((e.dmgB)*0.25)
          self.bossBlockSpecial = True
          
      else:
          
        if we.aB == True:
          p1.health -= round((e.dmgB)*1.5)
          e.hpB -= round((p1.damage)*0.5)
          gs.textEdit("Boss used great force to attack you and his attack did significantly more damage then yours.")
          self.bossBlockSpecial = False
            
        elif we.bB == True:
          p1.health -= round((e.dmgB)*0.5)
          gs.textEdit("Heavy attack from the boss was only partly blocked.")
          self.bossBlockSpecial = False
                  
        elif we.pB == True:
          e.hpB -= round((e.dmgB)*1.5)
          gs.textEdit("Materfull parry. Bosses attack completely deflected!!")
          self.bossBlockSpecial = False

    else:

      if self.bossSpecial == False:
  
        if self.randAttackNum == 1 and we.aB == True:
          gs.textEdit("You and the boss both attacked.")
          p1.health -= e.dmgB
          e.hpB -= p1.damage

        elif self.randAttackNum == 1 and we.bB == True:
          gs.textEdit("You have blocked bosses attack.")

        elif self.randAttackNum == 1 and we.pB == True:
          gs.textEdit("You have partly parried bosses attack and deflected some dmg.")
          p1.health -= round((e.dmgB)*0.5)
          e.hpB -= round((p1.damage)+((e.dmgB)*0.5))

        elif self.randAttackNum == 2 and we.aB == True:
          gs.textEdit("Enemy let you hit him, intentionaly. You managed to do more damage.")
          e.hpB -= round(p1.damage * 1.5)
          self.bossSpecial = True

        elif self.randAttackNum == 2 and we.bB == True:
          gs.textEdit("Enemy seems to be growing in size while you are awating an attack. Imposible!")
          self.bossSpecial = True

        elif self.randAttackNum == 2 and we.pB == True:
          gs.textEdit("Enemy seems to be growing in size while you are awating an attack to parry. You quickly cut him.")
          e.hpB -= round(p1.damage * 0.75)
          self.bossSpecial = True

      elif self.bossSpecial == True:

        if we.aB == True:
          gs.textEdit("Huge boss attack you with immese force and you were unable to attack back. Boss grew smaller again.")
          p1.health -= round(e.dmgB * 3)
          self.bossSpecial = False

        elif we.bB == True:
          gs.textEdit("You were able to block only some of the damage before boss went back to his normal size.")
          p1.health -= e.dmgB
          self.bossSpecial = False

        elif we.pB == True:
          gs.textEdit("You managed to parry the huge attack, but only deflected some damage. Boss went back to his normal size.")
          e.hpB -= e.dmgB
          p1.health -= round(e.dmgB * 0.5)
          self.bossSpecial = False


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
     hpBoxTwo["text"] = int(self.health)
     strBoxTwo["text"] = int(self.damage)
     moneyBoxTwo["text"] = int(self.money)

  def hpChange(self, dmgPoints):
    self.health += dmgPoints

  def dmgChange(self, strPoints):
    self.damage += strPoints
    self.damage = round(self.damage)
    
  def moneyChange(self, moneyPoints):
    self.money += moneyPoints

  #enter the healShop actions
  def buyHp(self):
    
    if we.OneB == True:

      if self.money < 50:
        gs.textEdit("Come back with enough money. Action button to move forward. ")

      elif p1.health <= 50:
          p1.hpChange(50)
          p1.moneyChange(-50)
          gs.textEdit("Healed for half, come again! Action button to move forward. ")

      elif p1.health > 50:
        p1.hpChange(100-p1.health)
        p1.moneyChange(-50)
        gs.textEdit("Healed for half, come again! Action button to move forward. ")

    elif we.TwoB == True:

      if self.money < 150:
        gs.textEdit("Come back with enough money. Action button to move forward. ")

      else:
        p1.hpChange(100-p1.health)
        p1.moneyChange(-150)
        gs.textEdit("Fully healed, come again! Action button to move forward. ")

  #enter the gym actions
  def fitGym(self):
    powerTrain = 0.2
    
    if we.OneB == True:

      if self.money < 50:
        gs.textEdit("Come back with enough money.Action button to move forward. ")

      else:
        p1.dmgChange(self.damage * 0.1)
        powerTrain += 0.1
        p1.moneyChange(-50)
        gs.textEdit("Nice gainz, brother. Come again! Action button to move forward. ")

    elif we.TwoB == True:

      if self.money < 250:
        gs.textEdit("Come back with enough money. Action button to move forward. ")

      else:
        p1.dmgChange(powerTrain * 10)
        p1.moneyChange(-250)
        gs.textEdit("POWER GAINZ!!!! Action button to move forward. ")




"""
game logic end
"""

p1 = Human("example", 15, 100, 0) #shortcut to playerOne class
gs = gameSystem() #shortcut to gameSystem class
e = enemySystem() #shortcut to Enemy class
we = windowEvents() #shortcut to window events class

"""
window start
"""

window = tk.Tk()
window.title("DnD")

fontStyle = tkFont.Font(family="Lucida Grande", size=10)

window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, weight=1)

textFrame = tk.Frame(master=window)
textFrame.grid(row=0,column=0)
textFrame.rowconfigure(0, minsize=50, weight=1)
textFrame.columnconfigure([0, 1], minsize=50, weight=1)
     
    #right side of top row frame stats box
textRight = tk.Frame(master=textFrame)
textRight.grid(row=0,column=1)
textRight.rowconfigure([0,3], weight=1)
textRight.columnconfigure([0, 1], weight=1)

statsBoxOne = tk.Label( master=textRight, text="Stats",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
statsBoxOne.grid(row=0,column=0)
statsBoxTwo = tk.Label(master=textRight, text="last seen",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
statsBoxTwo.grid(row=0,column=1)

hpBoxOne = tk.Label(master=textRight, text="Health",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
hpBoxOne.grid(row=1,column=0)
hpBoxTwo = tk.Label(master=textRight, text="",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
hpBoxTwo.grid(row=1,column=1)

strBoxOne = tk.Label(master=textRight, text="Strength",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
strBoxOne.grid(row=2,column=0)
strBoxTwo = tk.Label(master=textRight, text="",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
strBoxTwo.grid(row=2,column=1)

moneyBoxOne = tk.Label(master=textRight, text="Money",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
moneyBoxOne.grid(row=3,column=0)
moneyBoxTwo = tk.Label(master=textRight, text="",font=fontStyle, width=13, relief=tk.SUNKEN, borderwidth=5)
moneyBoxTwo.grid(row=3,column=1)

    #stats box end

    #left side of the top row frame
textLeft = tk.Frame(master=textFrame)
textLeft.grid(row=0,column=0)

lastText = tk.Label(master=textLeft, text="You wake up on a road and inspect yourself.",relief=tk.SUNKEN,height=3, width=80, font=fontStyle,borderwidth=5)
lastText.pack()
newText = tk.Label(master=textLeft, text="Action One to move forward.",relief=tk.SUNKEN,height=3, width=80, font=fontStyle,borderwidth=5)
newText.pack()
    #left side ends

    #bottom row with buttons
buttonFrame = tk.Frame(master=window)
buttonFrame.grid(row=1,column=0)

    #buttons
attackButton = tk.Button(
  state = "disabled",
  master = buttonFrame,
  text="Attack",
  font=fontStyle,
  width=15,
  borderwidth=3,
  command = we.attackButton
)

blockButton = tk.Button(
  state = "disabled",
  master = buttonFrame,
  text="Block",
  font=fontStyle,
  width=15,
  borderwidth=3,
  command = we.blockButton
)

parryButton = tk.Button(
  state = "disabled",
  master = buttonFrame,
  text="Parry",
  font=fontStyle,
  width=15,
  borderwidth=3,
  command = we.parryButton
)
actionOneButton = tk.Button(
  master = buttonFrame,
  text="Action One",
  font=fontStyle,
  width=15,
  borderwidth=3,
  command = we.actionOneButton
)
actionTwoButton = tk.Button(
  master = buttonFrame,
  text="Action Two",
  font=fontStyle,
  width=15,
  borderwidth=3,
  command = we.actionTwoButton
)

attackButton.pack(side=tk.LEFT)
blockButton.pack(side=tk.LEFT)
parryButton.pack(side=tk.LEFT)
actionOneButton.pack(side=tk.LEFT, padx=30)
actionTwoButton.pack()


    #bottom side button ends
window.mainloop()

"""
window end
"""


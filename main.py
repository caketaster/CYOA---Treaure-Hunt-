print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first_choice=input("You climb from your horse. 2 dark and winding pathways are before you. Type L or R to proceed. \n")
if first_choice == "L":
  lake_choice=input("The dark and winding path leads to a lake. You see a promising looking house across the lake. Will you swim (S) or look for another path (P)? \n")
  if lake_choice == "S":
    print("You start swimming. You then realise you can't swim. Sharks are approaching. They have laser-guns on their faces. You realise the lake is made of petrol. Now it's on fire. Your arms and legs fall off. END.")
  elif lake_choice == "P":
    house_choice2=input("You find a path to a bridge and cross to the house. You can either enter the house (E) or look in the garden (G). \n")
    if house_choice2 == "E":
      print("You enter the house. A ghost appears. Not a friendly one. It's aggressively gay. You are bummed. It's not so bad. You move in with the ghost, but never find the treasure. END. ")
    elif house_choice2 == "G":
      garden_choice=input("The garden is kinda spooky. You step over grasping plants and through a tangle of bushes. Before you are 2 freshly-dug plots. Surely the treasure lies beneath one of them! Which will you choose, L or R? \n")
      if garden_choice == "R":
        print("You dig deeper and deeper, and eventually come across a wooden box. It's a coffin! You open it and the corpse is..... YOU. This shits you right up. You immediately die. END.")
      elif garden_choice == "L":
        print("You dig and dig, using your bare hands, the sweat pouring from your face. Eventually you reach a wooden box. You open it. Inside is a USB drive and a 24 word seed phrase. You just found all the Bitcoinz. ALL THE BITCOINZ. You move to San Diego and fund the cure for tiredness. You're the most famous person in the world, and probably the best person ever. Congrats. END.")
      
    
  
elif first_choice == "R":
  house_choice=input("The path leads to a bridge. You cross the bridge and see a scary old house before you. Enter the house (E) or look around the garden (G)? \n")
  if house_choice == "E":
    print("You enter the house. A ghost appears. Not a friendly one. It's aggressively gay. You are bummed. It's not so bad. You move in with the ghost, but never find the treasure. END. ")
  elif house_choice == "G":
    garden_choice=input("The garden is kinda spooky. You step over grasping plants and through a tangle of bushes. Before you are 2 freshly-dug plots. Surely the treasure lies beneath one of them! Which will you choose, L or R? \n")
    if garden_choice == "R":
      print("You dig deeper and deeper, and eventually come across a wooden box. It's a coffin! You open it and the corpse is..... YOU. This shits you right up. You immediately die. END.")
    elif garden_choice == "L":
      print("You dig and dig, using your bare hands, the sweat pouring from your face. Eventually you reach a wooden box. You open it. Inside is a USB drive and a 24 word seed phrase. You just found ALL THE BITCOINZ. You move to San Francisco and fund the cure for cancer. You're the most famous person in the world, and probably the best person ever. Congrats. END.")
    
  
 
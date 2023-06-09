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
print("\nYour mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
want_to_go = input('\nYou\'re at a cross road. Where do you want to go? Type "left" or "right"\n\n').lower()
if want_to_go == "left":
  print('''
     _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                    
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'
 
  ''')
  lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n\n').lower()
  if lake == "wait":
    print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
    ''')
    door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?\n\n').lower()
    if door == "red":
      print('''
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''')
      print("Burned by fire.\n\nGame over.")
    elif door == "blue":
      print('''
              .         __      '        .       '       .
  *            _-~  ~-_      .         '      .
 .   .        /___  ___\  '             .             .
             / (O)  (o) \         *         ___    *  .
   __,-~-~-,/    -..-    \  .-~~-.   __..-~~   ~~-.._
.-~  `V~V~V'`\ -v----v-   \/     /.-~  //..  \   \.  `~-._
  //.     \.' `\..___..---/    /''    .    '   .   ..
                     ''/ \\..'  \'   V~V~V'  //  /  ' .  ' /  \ . '  \\\ \ \
      ''')
      print("Eaten by beasts.\n\nGame over.")
    elif door == "yellow":
      print('''
.----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. |
| | _____  _____ | | |     _____    | | | ____  _____  | |
| ||_   _||_   _|| | |    |_   _|   | | ||_   \|_   _| | |
| |  | | /\ | |  | | |      | |     | | |  |   \ | |   | |
| |  | |/  \| |  | | |      | |     | | |  | |\ \| |   | |
| |  |   /\   |  | | |     _| |_    | | | _| |_\   |_  | |
| |  |__/  \__|  | | |    |_____|   | | ||_____|\____| | |
| |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' 
      ''')
      print("You Win!")
    else:
      print('''
               _..._
             ,'     `.
           ,'         `.
         ,'    _   ,-.  `.
         |    (_)  `-'   |
         |        >      |
         |     ,----.    |
         |    /,-""-.\   |
         `.  |/      "  ,'
           `.         ,'
             `._____,'
      ''')
      print("Game Over.")
  else:
    print('''
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \
           /_`       '_\
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-' ap
    ''')
    print("\nAttacked by trout.\n\nGAME OVER.")
else:
  print("\nFall into a hole.\n\nGAME OVER.")
  print('''
         o  o
     o        o 
    o          o  
    o          o
     o        o  
        o  o  
  ''')
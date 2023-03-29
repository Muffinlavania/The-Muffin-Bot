import sys,os,random,time,re,pickle,calendar
from datetime import datetime
WINDOWS = os.name=='nt'
if not WINDOWS:
  from getkey import getkey as GETkey
else:
  import msvcrt

somekeys = {'H': 'up', 'P': 'down', 'K': 'left', 'M': 'right', '\\r': 'enter', '\\x08': 'backspace','\\xe0':'yippe yay','\\t':'tab'}
def getkey():
  return (h if (h:=str(msvcrt.getch())[2:-1]) not in somekeys.keys() or h in ['P','H','K','M'] else somekeys[h] if h!='\\xe0' else somekeys[str(msvcrt.getch())[2:-1]]).lower() if WINDOWS else GETkey.lower()
UP='up' if WINDOWS else keys.UP
DOWN='down' if WINDOWS else keys.DOWN
RIGHT='right' if WINDOWS else keys.RIGHT
LEFT='left' if WINDOWS else keys.LEFT

#Got to indent after each '''
def c():
  os.system('clear' if os.name!='nt' else 'cls')

black = "\033[0;30m" 
red = "\033[0;31m" 
green = "\033[0;32m" 
yellow = "\033[0;33m" 
blue = "\033[0;34m" 
magenta = "\033[0;35m" 
cyan = "\033[0;36m" 
white = "\033[0;37m" 
bright_black = "\033[0;90m" 
bright_red = "\033[0;91m" 
bright_green = "\033[0;92m" 
bright_yellow = "\033[0;93m" 
bright_blue = "\033[0;94m" 
bright_magenta = "\033[0;95m" 
bright_cyan = "\033[0;96m" 
bright_white = "\033[0;97m"
bold='\033[01m'
reset='\033[0m'
reset1='\033[0m'
z6969=False
Truehtta=True
board_slots=['-','-','-','-','-','-','-','-','-']
turn='X'
turns = ["X","O"]
wins2=0
wins1=0
stalling=True

maze1='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX-------------------------------------------T----XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX---┌┐-------------------------------------------XXXX+
|XXXX---└┘-------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''

stuffwhynot=True
maze1=list(maze1)
z=1
mazeq=maze1
def mazeg():
  global z,mazeq,stuffwhynot,maze1
  z=1
  mazeq=maze1
  stuffwhynot=True
  black = "\033[0;30m" 
  red = "\033[0;31m" 
  green = "\033[0;32m" 
  yellow = "\033[0;33m" 
  blue = "\033[0;34m" 
  magenta = "\033[0;35m" 
  cyan = "\033[0;36m" 
  white = "\033[0;37m" 
  bright_black = "\033[0;90m" 
  bright_red = "\033[0;91m" 
  bright_green = "\033[0;92m" 
  bright_yellow = "\033[0;93m" 
  bright_blue = "\033[0;94m" 
  bright_magenta = "\033[0;95m" 
  bright_cyan = "\033[0;96m" 
  bright_white = "\033[0;97m"
  bold='\033[01m'
  reset='\033[0m'
  maze2='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------T-XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------XXXX+
|XXXX-------------------------------XXXXXXX----------XXXX+
|XXXX-------------------------------XXXXXXX----------XXXX+
|XXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXX+
|XXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------XXXX+
|XXXXX-----------------------------------------------XXXX+
|XXXXX-----------------------------------------------XXXX+
|XXXXX┌┐------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXX└┘------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
  '''
  maze3='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX------------XXXX------------------------------T-XXXX+
|XXXX------------XXXX--------------------------------XXXX+
|XXXX------------XXXX-------------XXXXXXXXXXXXXXXXXXXXXXX+
|XXXX------------XXXX-------------XXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXX----------------------------XXXX----------XXXX+
|XXXXXXXXXX----------------------------XXXX----------XXXX+
|XXXXXXXXXX----------------------------XXXX------XXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXX--------------------------XXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXX----------------------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------XX---------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------XXXX+
|XXXX┌┐-----------------------------------XX---------XXXX+
|XXXX└┘-----------------------------------XX---------XXXX+
|XXXX-------------------------------------XX---------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
  '''
  maze4='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX-----------------------------------------T------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------┌┐----------------------XXXX+
|XXXX------------------------└┘----------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXX------------------------------------------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
  '''
  maze1=list(maze1)
  maze2=list(maze2)
  maze3=list(maze3)
  maze4=list(maze4)
  stuff={
    1:maze1,
    2:maze2,
    3:maze3,
    4:maze4
  }
  goods=['-','W','U']
  colorchoice=white
  colorchoice2=yellow
  def printhint():
    c()
    if z==1:
      print("Collect the Treasure at the top right corner!")
    if z==2:
      print("Navigate the maze to the treasure at the top right!")
    if z==3:
      print("Your goal is to get to the top right corner where the treasure is!")
    input("[ENTER TO CONTINUE]\n")
    c()
  def nextlevel():
    global z,mazeq,stuffwhynot
    z+=1
    if z==4:
      stuffwhynot=False
    mazeq=stuff[z]
  def move(dir):
    global secrets
    if dir=='left':
      if mazeq[box3-2]=='T' or mazeq[box4-2]=='T' or mazeq[box2-2]=='T' or mazeq[box1-2]=='T':
        nextlevel()
      elif mazeq[box1-2] in goods and mazeq[box3-2] in goods:
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1-2]='┌'
        mazeq[box2-2]='┐'
        mazeq[box3-2]='└'
        mazeq[box4-2]='┘'
    if dir=='right':
      if mazeq[box2+2]=='T' or mazeq[box4+2]=='T' or mazeq[box1+2]=='T' or mazeq[box3+2]=='T':
        nextlevel()
      elif mazeq[box2+2] in goods and mazeq[box4+2] in goods:
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1+2]='┌'
        mazeq[box2+2]='┐'
        mazeq[box3+2]='└'
        mazeq[box4+2]='┘'
    if dir=='up':
      if mazeq[box3-118]=='T' or mazeq[box4-118]=='T' or mazeq[box2-59]=='T' or mazeq[box1-59]=='T':
        nextlevel()
      elif mazeq[box2-59] in goods and mazeq[box1-59] in goods:
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1-59]='┌'
        mazeq[box2-59]='┐'
        mazeq[box3-59]='└'
        mazeq[box4-59]='┘'
    if dir=='down':
      if mazeq[box3+59]=='T' or mazeq[box4+59]=='T' or mazeq[box2+118]=='T' or mazeq[box1+128]=='T':
        nextlevel()
      elif mazeq[box3+59] in goods and mazeq[box4+59] in goods:
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1+59]='┌'
        mazeq[box2+59]='┐'
        mazeq[box3+59]='└'
        mazeq[box4+59]='┘'
  def printmaze(themaze):
    themaze2=themaze
    places=[]
    for loligag in [box1,box2,box3,box4]:
      f=[loligag+1,loligag+2,loligag+3,loligag,loligag-1,loligag-2,loligag-3,loligag-59,loligag+61,loligag-60,loligag+59,loligag+58,loligag-57,loligag+57,loligag-61]
      for thhhhhhhhhhhhhhhh in f:
        places.append(thhhhhhhhhhhhhhhh)
    numbithink=-1
    for i in themaze2:
      numbithink+=1
      if numbithink in places or i=='T' or i=='\n':
        if i=='|':
          print("",end="")
        elif i=='X':
          print(colorchoice+"X"+reset,end="")
        elif i=='-':
          print(" "+reset,end="")
        elif i=='+':
          print("",end="")
        elif i=="T":
          print(colorchoice2+"T",end="")
        elif i=='W':
          print(colorchoice+"W"+reset,end="")
        elif i=='Y':
          print(colorchoice+"Y"+reset,end="")
        elif i=='U':
          print(colorchoice+"X"+reset,end="")
        else:
          print(i,end="")
      else:
        print(reset+'.',end="")
  stuffwhynot=True
  while stuffwhynot:
    print('\t\t\t\t\t Level '+str(z))
    box1=int(mazeq.index('┌'))
    box2=int(mazeq.index('┐'))
    box3=int(mazeq.index('└'))
    box4=int(mazeq.index('┘'))
    printmaze(mazeq)
    keyz=getkey()
    if keyz=='h':
      printhint()
    if keyz=='w' or keyz==UP:
      move('up')
    if keyz=='a' or keyz==LEFT:
      move('left')
    if keyz=='s' or keyz==DOWN:
      move('down')
    if keyz=='d' or keyz==RIGHT:
      move("right")
    c()

def rps():
  global wins1,wins2,stalling
  wins1=0
  wins2=0
  yes=("yes","y","yes ","yea")
  no=("No","no","n","no ")
  r=("R","r","rock")
  s=("S","s","scissors")
  p=("P","p","paper")
  print("This is a Rock Paper Scissors simulator!")
  time.sleep(2)
  print("You will be facing the computer!")
  time.sleep(2)
  print("Say your first move!")
  print("'R' for rock  'S' for scissors  'P' for paper")
  stalling=True
  while stalling:
      rps=input()
      com=random.randint(1,3)
      if com==3:
          comp="rock"
      if com==2:
          comp="scissors"
      if com==1:
          comp="paper"
      if rps in r:
          print("Rock!")
          time.sleep(1)
          print("Paper!")
          time.sleep(1)
          print("Scissors!")
          time.sleep(1)
          print("Shoot!")
          time.sleep(1)
          print("You held out rock")
          time.sleep(1.5)
          print("The computer held out "+comp)
          time.sleep(1.5)
          if comp=="paper":
              print("You lost!")
              wins2=wins2+1
          if comp=="rock":
              print("You tied!")
          if comp=="scissors":
              print("You win!")
              wins1=wins1+1
      if rps in s:
          print("Rock!")
          time.sleep(1)
          print("Paper!")
          time.sleep(1)
          print("Scissors!")
          time.sleep(1)
          print("Shoot!")
          time.sleep(1)
          print("You held out scissors")
          time.sleep(1.5)
          print("The computer held out "+comp)
          time.sleep(1.5)
          if comp=="paper":
              print("You win!")
              wins1=wins1+1
          if comp=="rock":
              print("You lose!")
              wins2=wins2+1
          if comp=="scissors":
              print("You tied!")
      if rps in p:
          print("Rock!")
          time.sleep(1)
          print("Paper!")
          time.sleep(1)
          print("Scissors!")
          time.sleep(1)
          print("Shoot!")
          time.sleep(1)
          print("You held out paper")
          time.sleep(1.5)
          print("The computer held out "+comp)
          time.sleep(2)
          if comp=="paper":
              print("You tied!")
          if comp=="rock":
              print("You win!")
              wins1=wins1+1
          if comp=="scissors":
              print("You lose!")
              wins2=wins2+1
      time.sleep(2)
      c()
      print("Your score is "+str(wins1))
      print("The computers score is "+str(wins2))
      print("Want to go again?")
      go=input().lower()
      if go in yes:
          print("Ok! Say your move(r,p,s)")
          continue
      elif go in no:
          print("Ok! See you later")
          time.sleep(1.5)
          stalling=False
      else:
          print("Invalid Input, proceeding to next turn (Say your move)")
          continue      
      c()
  return wins1

def tictactoe():
  global z6969,Truehtta,board_slots
  z6969=False
  board_slots=['-','-','-','-','-','-','-','-','-']
  def judge():
    global Truehtta,z6969
    if (board_slots[0]=="X" and board_slots[1]=="X" and board_slots[2]=="X") or (board_slots[0]=="X" and board_slots[3]=="X" and board_slots[6]=="X") or (board_slots[1]=="X" and board_slots[4]=="X" and board_slots[7]=="X") or (board_slots[2]=="X" and board_slots[5]=="X" and board_slots[8]=="X") or (board_slots[3]=="X" and board_slots[4]=="X" and board_slots[5]=="X") or (board_slots[6]=="X" and board_slots[7]=="X" and board_slots[8]=="X") or (board_slots[0]=="X" and board_slots[4]=="X" and board_slots[8]=="X") or (board_slots[2]=="X" and board_slots[4]=="X" and board_slots[6]=="X"):
      Truehtta=False
      z6969=True
    if (board_slots[0]=="O" and board_slots[1]=="O" and board_slots[2]=="O") or (board_slots[0]=="O" and board_slots[3]=="O" and board_slots[6]=="O") or (board_slots[1]=="O" and board_slots[4]=="O" and board_slots[7]=="O") or (board_slots[2]=="O" and board_slots[5]=="O" and board_slots[8]=="O") or (board_slots[3]=="O" and board_slots[4]=="O" and board_slots[5]=="O") or (board_slots[6]=="O" and board_slots[7]=="O" and board_slots[8]=="O") or (board_slots[0]=="O" and board_slots[4]=="O" and board_slots[8]=="O") or (board_slots[2]=="O" and board_slots[4]=="O" and board_slots[6]=="O"):
      z6969=False
      Truehtta=False
  def r():
    print(reset)
  def change():
    global turn
    if turn==turns[0]:
      turn=turns[1]
    else:
      turn=turns[0]
  def print_board():
    print("\t\t\t\t\t\t\t|"+board_slots[0]+"|"+board_slots[1]+"|"+board_slots[2]+"|\n\t\t\t\t\t\t\t|"+board_slots[3]+"|"+board_slots[4]+"|"+board_slots[5]+"|\n\t\t\t\t\t\t\t|"+board_slots[6]+"|"+board_slots[7]+"|"+board_slots[8]+"|\n\t\t\t\t\t\t\t")
    print("The turn belongs to '"+turn+"'")
  def comp_play():
    global Truehtta,board_slots
    while Truehtta:
      judge()
      if Truehtta:
        if '-' in board_slots:
          change()
          if turn==turns[1]:
            print_board()
            print(blue+bold+'\nThe computer is deciding where to go..')
            going=True
            time.sleep(2)
            while going:
              computer_roll=random.randint(0,8)
              if board_slots[computer_roll]=="-":
                print("The computer put an O at slot "+str(computer_roll+1))
                r()
                time.sleep(2.5)
                board_slots[computer_roll]="O"
                going=False
                break
              else:
                continue
          if turn==turns[0]:
            guessing=True
            while guessing:
              print_board()
              print(green+"\nIt is your turn! \nSay the number of the slot you want to do your move, (1-9)")
              r()
              move=input()
              if move.isdigit():
                if int(move)<10 and int(move)>0:
                  if board_slots[int(move)-1]=="-":
                    board_slots[int(move)-1]="X"
                    guessing=False
                  else:
                    print("That slot is already taken")
                    time.sleep(2)
                else:
                  print("You have to enter number between 1 and 9!")
                  time.sleep(2)
              else:
                print("You have to enter a number!")
                time.sleep(2)
              c()
          c()
        else:
          r()
          print("The Game has ended! No one won....")
          time.sleep(2)
          z6969='n'
          Truehtta=False
        print("\a")
        c()
  comp_play()
  c()
  if z6969==False:
    print("You lost!")
  if z6969==True:
    print("You won!")
  if z6969=='n':
    print("You tied!")
  time.sleep(2)
  Truehtta=True
  return z6969

def timer():
    m=0
    t=True
    while t:
        print("How long do you want to run for?(In seconds)")
        s = input()
        if s.isdigit():
            s=int(s)
            while s>59:
                s-=60
                m+=1
            t=False
        else:
            print("Bruh, enter a number only!")
            time.sleep(3)
            c()
    c()
    fg=True
    while fg:
        if s==-1:
            s=59
            m-=1
            if m<0:
                break
        print(""+str(m)+" minutes\t"+str(s)+" seconds")
        time.sleep(1)
        s-=1    
        
        c()
    print("\aDone. [CTRL+C To exit]")
    while True:
      try:
        time.sleep(1)
        print("\a",end="")
      except:
        c()
        break

def stop():
    print("How long do you want the stopwatch to run?(In seconds)")
    secru=input()
    c()
    goo=0
    while goo != int(secru):
        print(str(goo))
        time.sleep(.1)
        goo+=.1
        goo=round(goo,1)
        c()
    print(str(goo))
    print("\aDone. [CTRL+C To exit]")
    while True:
      try:
        time.sleep(1)
        print('\a',end="")
      except:
        c()
        break

def timestary():
  print("Which do you want?")
  print("1: Timer")
  print("2: Stopwatch")
  ww=input()
  if int(ww)==1:
      timer()
  if int(ww)==2:
      stop()



turnturnpls='P'
wildz=False
skipp=False
skipp2=False
deck=[]
deck2=[]
tyforthat2=True
noplsing=True
goingforitithink=True
def uno():
  global tyforthat2,noplsing,goingforitithink,start,wildz,skipp,skipp2,deck,deck2,turnturnpls,reset1,dicts
  turnturnpls='P'
  wildz=False
  skipp=False
  skipp2=False
  deck=[]
  deck2=[]
  tyforthat2=True
  noplsing=True
  goingforitithink=True
  reset1='\033[0m'
  def reset():
    print(reset1,end="")
  def underline(yuikjh):
    return "\u0332".join(yuikjh)
  bold='\033[01m'
  zero='''
  ┌─────────┐
  | ┌─────┐ |
  | |     | |
  | |     | |
  | |     | |
  | └─────┘ |
  └─────────┘'''
  one='''
  ┌─────────┐
  |   /|    |
  |  / |    |
  |    |    |
  |    |    |
  |  -----  |
  └─────────┘'''
  two='''
  ┌─────────┐
  |  -──┐   |
  |     |   |
  |  ┌──┘   |
  |  |      |
  |  └──-   |
  └─────────┘'''
  three='''
  ┌─────────┐
  |   ───┐  |
  |      |  |
  |    ──|  |
  |      |  |
  |   ───┘  |
  └─────────┘'''
  four='''
  ┌─────────┐
  | |    |  |
  | |    |  |
  | └────|  |
  |      |  |
  |      |  |
  └─────────┘'''
  five='''
  ┌─────────┐
  |  ┌────  |
  |  |      |
  |  └───┐  |
  |      |  |
  |  ────┘  |
  └─────────┘'''
  six='''
  ┌─────────┐
  |  ┌──    |
  |  |      |
  |  |───┐  |
  |  |   |  |
  |  └───┘  |
  └─────────┘'''
  seven='''
  ┌─────────┐
  |  ────── |
  |      /  |
  |     /   |
  |    /    |  
  |   /     |
  └─────────┘'''
  eight='''
  ┌─────────┐
  |  ┌───┐  |
  |  |   |  |
  |  |───|  |
  |  |   |  |
  |  └───┘  |
  └─────────┘'''
  nine='''
  ┌─────────┐
  |  ┌───┐  |
  |  |   |  |
  |  └───|  |
  |      |  |
  |      |  |
  └─────────┘'''
  plus2='''
  ┌─────────┐
  |    -──┐ |
  | |     | |
  |─┼─ ┌──┘ |
  | |  |    |
  |    └──- |
  └─────────┘'''
  plus4='\033[40m'+'''
  ┌─────────┐
  |   |   | |
  | | |   | |
  |─┼─└───| |
  | |     | |
  |       | |
  └─────────┘'''+reset1
  wild=bold+'\033[40m'+'''
  ┌─────────┐
  |'''+'\033[41m'+'''    '''+'\033[40m'+'''|'''+'\033[44m'+'''    '''+'\033[40m'+'''|\n|'''+'\033[41m'+'''    '''+'\033[40m'+'''|'''+'\033[44m'+'''    '''+'\033[40m'+'''|'''+'''
  |────┼────|
  '''+'''|'''+'\033[43m'+'''    '''+'\033[40m'+'''|'''+'\033[42m'+'''    '''+'\033[40m'+'''|\n'''+'''|'''+'\033[43m'+'''    '''+'\033[40m'+'''|'''+'\033[42m'+'''    '''+'\033[40m'+'''|'''+'\033[40m'+'''
  └─────────┘
  '''+bold
  skip='''
  ┌─────────┐
  | ┌────/┐ |
  | |   / | |
  | |  /  | |
  | | /   | |
  | └/────┘ |
  └─────────┘'''
  reverse='''
  ┌─────────┐
  |    _    |
  |┌──┘ \   |
  || ┌─_/ _ |
  || └───┘ ||
  |└───────┘|
  └─────────┘'''
  dicts={
    'Red 1':["Red",1],'Blue 1':["Blue",1],
    'Red 2':["Red",2],'Blue 2':["Blue",2],
    'Red 3':["Red",3],'Blue 3':["Blue",3],
    'Red 4':["Red",4],'Blue 4':["Blue",4],
    'Red 5':["Red",5],'Blue 5':["Blue",5],
    'Red 6':["Red",6],'Blue 6':["Blue",6],
    'Red 7':["Red",7],'Blue 7':["Blue",7],
    'Red 8':["Red",8],'Blue 8':["Blue",8],
    'Red 9':["Red",9],'Blue 9':["Blue",9],
    'Red 0':["Red",0],'Blue 0':["Blue",0],
    'Yellow 1':["Yellow",1],'Green 1':["Green",1],
    'Yellow 2':["Yellow",2],'Green 2':["Green",2],
    'Yellow 3':["Yellow",3],'Green 3':["Green",3],
    'Yellow 4':["Yellow",4],'Green 4':["Green",4],
    'Yellow 5':["Yellow",5],'Green 5':["Green",5],
    'Yellow 6':["Yellow",6],'Green 6':["Green",6],
    'Yellow 7':["Yellow",7],'Green 7':["Green",7],
    'Yellow 8':["Yellow",8],'Green 8':["Green",8],
    'Yellow 9':["Yellow",9],'Green 9':["Green",9],
    'Yellow 0':["Yellow",0],'Green 0':["Green",0],
    '+4 Card':['All','/','+4'],'Wild Card':['All','/','W'],
    "Green +2 Card":["Green",'+2'],"Yellow +2 Card":["Yellow",'+2'],
    "Red +2 Card":["Red",'+2'],"Blue +2 Card":["Blue",'+2'],
    "Red Reverse Card":["Red",'R'],"Blue Reverse Card":["Blue","R"],
    "Green Reverse Card":["Green",'R'],"Yellow Reverse Card":["Yellow","R"],
    "Red Skip Card":["Red",'S'],"Yellow Skip Card":["Yellow",'S'],
    "Green Skip Card":["Green",'S'],"Blue Skip Card":["Blue","S"]
  }
  #Just cool printing
  def printt(thingggg,dela=.04):
    for i in thingggg:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(dela)
    print("")
  def clear():
    c()
  pattern=re.compile('\x1b+\[+3+[0-9]+m+')
  def normconvert(a690):
    a692=pattern.sub("",a690)
    return a692
  printt("Welcome to Uno!\n")
  print(underline("New features:"))
  print("Lowercase letters now work! red 6 = Red 6")
  print("You can now play again after winning or losing! ([In beta] Please report bugs if you find any)\n")
  #Rules and stuff here(Or not)
  printt("Hit enter to continue (Say 'rules' for the rules of Uno!)")
  werthebest=input()
  clear()
  if werthebest.lower() in ['rule','rules','rules ']:
    printt(underline("Here are the rules of Uno:"))
    printt("The objective of the game is to get rid of all of your cards")
    printt("There are many card types, these are:")
    printt("A Red, Green, Yellow, and Blue version of 0 through 9")
    printt("A Red, Green, Yellow, and Blue versions of Reverse Cards, Skip Cards, and +2 cards")
    printt("Wild Cards, and +4 cards")
    printt("At the beginning of the game, you will get 5 random cards, and there will be one starting card in play")
    printt("To play a card ,it must 1) Have a matching color to the card in play, 2) Have a matching number to the card in play3) Be a Wild Card or a +4 Card, or the card in play is one of these")
    printt("The multi-colored 0-9 cards have no special atributes, but the other cards do")
    time.sleep(2)
    print("(Hit enter to learn more)")
    input()
    tryyour=""
    while tryyour.lower() not in ['no','n']:
      clear()
      print("What would you like to learn more about?")
      print("1) Wild Cards")
      print("2) +4 cards")
      print("3) Reverse Cards and Skip Cards")
      print("4) +2 Cards")
      print("(Say n to exit)")
      tryyour=input("")
      clear()
      if tryyour=="1":
        printt(bold+"Wild Cards:")
        reset()
        printt("Wild Cards are cards that can be placed on any card")
        printt("Once placed, the person who placed it can pick what color the next card must be, excluding other wild cards or +4 cards")
        print("[Enter to continue]")
        input()
        clear()
      if tryyour=="2":
        printt(bold+"+4 Cards:")
        reset()
        printt("+4 Cards are used to give the opponent +4 cards!")
        printt("This can give you a tremendous lead, and +4 Cards can be placed on any card type!")
        print("[Enter to continue]")
        input()
        clear()
      if tryyour=="3":
        printt(bold+"Reverse Cards and Skip Cards")
        reset()
        printt("Reverse Cards are semi useless in 2 player mode...")
        printt("Reverse Cards are used to switch the order of how the turns go")
        printt("Skip Cards are used to skip the opponent's turn!")
        printt("Skip Cards basically give you another turn")
        print("[Enter to continue]")
        input()
        clear()
      if tryyour=="4":
        printt(bold+"+2 Cards")
        reset()
        printt("+2 Cards give your opponent +2 cards!")
        printt("This will give you a slight advantage!")
        print("[Enter to continue]")
        input()
        clear()
  #List of cards in uno
  cards=['\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+'Red +2 Card','\033[33m'+'Yellow +2 Card','\033[32m'+'Green +2 Card','\033[34m'+'Blue +2 Card','\033[31m'+'Red Skip Card','\033[33m'+'Yellow Skip Card','\033[32m'+'Green Skip Card','\033[34m'+'Blue Skip Card','\033[31m'+'Red Reverse Card','\033[32m'+'Green Reverse Card','\033[33m'+'Yellow Reverse Card','\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+"Red 0",'\033[33m'+'Yellow 0','\033[34m'+'Blue 0','\033[32m'+'Green 0','\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+"Red 0",'\033[33m'+'Yellow 0','\033[34m'+'Blue 0','\033[32m'+'Green 0','+4 Card','+4 Card','+4 Card','\033[31m'+'Red +2 Card','\033[33m'+'Yellow +2 Card','\033[32m'+'Green +2 Card','\033[34m'+'Blue +2 Card','\033[31m'+'Red Skip Card','\033[33m'+'Yellow Skip Card','\033[32m'+'Green Skip Card','\033[34m'+'Blue Skip Card','\033[31m'+'Red Reverse Card','\033[32m'+'Green Reverse Card','\033[33m'+'Yellow Reverse Card']
  start=random.choice(cards)
  for retyu in range(3):
    cards.append("Wild Card")
  def setup():
    global turnturnpls,wildz,skipp,skipp2,deck,deck2
    turnturnpls='P'
    wildz=False
    skipp=False
    skipp2=False
    deck=[]
    deck2=[]
    #Deck generation
    for i in range(5): #Deck list will be your deck, number = how many cards
      deck.append(random.choice(cards))
    for i in range(5):
      deck2.append(random.choice(cards))
  setup()
  def cardsr():
    for f in deck:
      print(f,end=reset1)
      if deck.index(f)-(len(deck)+1)!=-1:
        print(",",end="")
      if deck.index(f)==4 and deck.index(f)!=len(deck)-1:
        print('')
  def compcards():
    for f in deck2:
      print(f,end=reset1)
      if deck2.index(f)!=len(deck2)-1:
        print(",",end="")
    print("")
  graph=[]
  '\x1b[34m'
  '\x1b[33m'
  '\x1b[32m'
  def cardconvert(a1):
    if '\x1b[31m' in a1 or '\x1b[32m' in a1 or '\x1b[33m' in a1 or '\x1b[34m' in a1:
      a1=a1[5:]
    if dicts[a1][1]=="/":
      if dicts[a1][2]=="W":
        return wild+reset1
      if dicts[a1][2]=="+4":
        return plus4+reset1
    elif dicts[a1][0]=="Red":
      if dicts[a1][1]==1:
        return '\033[31m'+one+reset1
      if dicts[a1][1]==2:
        return '\033[31m'+two+reset1
      if dicts[a1][1]==3:
        return '\033[31m'+three+reset1
      if dicts[a1][1]==4:
        return '\033[31m'+four+reset1
      if dicts[a1][1]==5:
        return '\033[31m'+five+reset1
      if dicts[a1][1]==6:
        return '\033[31m'+six+reset1
      if dicts[a1][1]==7:
        return '\033[31m'+seven+reset1
      if dicts[a1][1]==8:
        return '\033[31m'+eight+reset1
      if dicts[a1][1]==9:
        return '\033[31m'+nine+reset1
      if dicts[a1][1]==0:
        return '\033[31m'+zero+reset1
      if dicts[a1][1]=='+2':
        return '\033[31m'+plus2+reset1
      if dicts[a1][1]=='S':
        return '\033[31m'+skip+reset1
      if dicts[a1][1]=='R':
        return '\033[31m'+reverse+reset1
    elif dicts[a1][0]=="Blue":
      if dicts[a1][1]==1:
        return '\033[34m'+one+reset1
      if dicts[a1][1]==2:
        return '\033[34m'+two+reset1
      if dicts[a1][1]==3:
        return '\033[34m'+three+reset1
      if dicts[a1][1]==4:
        return '\033[34m'+four+reset1
      if dicts[a1][1]==5:
        return '\033[34m'+five+reset1
      if dicts[a1][1]==6:
        return '\033[34m'+six+reset1
      if dicts[a1][1]==7:
        return '\033[34m'+seven+reset1
      if dicts[a1][1]==8:
        return '\033[34m'+eight+reset1
      if dicts[a1][1]==9:
        return '\033[34m'+nine+reset1
      if dicts[a1][1]==0:
        return '\033[34m'+zero+reset1
      if dicts[a1][1]=='+2':
        return '\033[34m'+plus2+reset1
      if dicts[a1][1]=='S':
        return '\033[34m'+skip+reset1
      if dicts[a1][1]=='R':
        return '\033[34m'+reverse+reset1
    elif dicts[a1][0]=="Yellow":
      if dicts[a1][1]==1:
        return '\033[33m'+one+reset1
      if dicts[a1][1]==2:
        return '\033[33m'+two+reset1
      if dicts[a1][1]==3:
        return '\033[33m'+three+reset1
      if dicts[a1][1]==4:
        return '\033[33m'+four+reset1
      if dicts[a1][1]==5:
        return '\033[33m'+five+reset1
      if dicts[a1][1]==6:
        return '\033[33m'+six+reset1
      if dicts[a1][1]==7:
        return '\033[33m'+seven+reset1
      if dicts[a1][1]==8:
        return '\033[33m'+eight+reset1
      if dicts[a1][1]==9:
        return '\033[33m'+nine+reset1
      if dicts[a1][1]==0:
        return '\033[33m'+zero+reset1
      if dicts[a1][1]=='+2':
        return '\033[33m'+plus2+reset1
      if dicts[a1][1]=='S':
        return '\033[33m'+skip+reset1
      if dicts[a1][1]=='R':
        return '\033[33m'+reverse+reset1
    elif dicts[a1][0]=="Green":
      if dicts[a1][1]==1:
        return '\033[32m'+one+reset1
      if dicts[a1][1]==2:
        return '\033[32m'+two+reset1
      if dicts[a1][1]==3:
        return '\033[32m'+three+reset1
      if dicts[a1][1]==4:
        return '\033[32m'+four+reset1
      if dicts[a1][1]==5:
        return '\033[32m'+five+reset1
      if dicts[a1][1]==6:
        return '\033[32m'+six+reset1
      if dicts[a1][1]==7:
        return '\033[32m'+seven+reset1
      if dicts[a1][1]==8:
        return '\033[32m'+eight+reset1
      if dicts[a1][1]==9:
        return '\033[32m'+nine+reset1
      if dicts[a1][1]==0:
        return '\033[32m'+zero+reset1
      if dicts[a1][1]=='+2':
        return '\033[32m'+plus2+reset1
      if dicts[a1][1]=='S':
        return '\033[32m'+skip+reset1
      if dicts[a1][1]=='R':
        return '\033[32m'+reverse+reset1
  for w in deck:
    z=cardconvert(w)
    graph.append(z)
  def cardsg():
    for i in graph:
      print(i,end='')
      print('\n'+deck[graph.index(i)])
  clear()
  sumoo=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
  theeee=""
  def judge(theone,thedeck):
    global theeee,start2
    if theone!='/':
      deck1=[]
      deck66=[]
      start2=normconvert(start)
      theone=normconvert(theone)
      for a2 in thedeck:
        a2=normconvert(a2)
        deck1.append(a2)
      for thhh in deck1:
        deck66.append(thhh.lower())
      theonez1=theone
      if theone.isdigit()==False and theone.isspace()==False:
        theonez1=theone.lower()
      if theonez1 in deck66 or theone in sumoo[:len(deck1)]:
          if theone.isdigit()==False:
            theone=deck1[deck66.index(theonez1)]
          if theone.isdigit():
              theone=deck1[int(theone)-1]
          else:
            theeee=theone
          if dicts[theone][0]==dicts[start2][0] or dicts[theone][1]==dicts[start2][1] or dicts[start2][0]=="All" or dicts[theone][0]=='All':
            theeee=thedeck[deck1.index(theone)]
            del thedeck[thedeck.index(theeee)]
            return True
          else:
            print("You cant place that card!")
            time.sleep(3)
            clear()
      else:
        print("Invalid Card...")
        time.sleep(3)
        clear()
    else:
      return False
  def compturn():
    zomg=True
    choose=False
    iseeu2=""
    printt("\nThe computer is making its move..")
    time.sleep(2)
    global deck,start,dicts,skipp2,wildz,tyforthat2
    if '+4 Card' in deck2:
      printt("The opponent placed a +4 card!")
      start='+4 Card'
      time.sleep(1)
      printt("Getting 4 cards...")
      deck2.remove('+4 Card')
      for i in range(4):
        deck.append(random.choice(cards))
      start="+4 Card"
      time.sleep(2)
    elif 'Wild Card' in deck2:
      wildz=True
      print("The opponent placed a Wild Card!")
      time.sleep(1)
      rety=random.choice(['Red','Yellow','Blue','Green'])
      printt("The computer decided to make your next card a "+rety+" Card!")
      dicts['Wild Card'][0]=rety
      deck2.remove("Wild Card")
      start="Wild Card"
      time.sleep(2)
    else:
      for iseeu in deck2:
        iseeu2=normconvert(iseeu)
        start3=normconvert(start)
        if zomg==True:
          if dicts[iseeu2][0]==dicts[start3][0] or dicts[iseeu2][1]==dicts[start3][1] or dicts[start3][0]=="All":
            printt("The computer placed a "+iseeu)
            reset()
            start=iseeu
            time.sleep(2)
            deck2.remove(iseeu)
            zomg=False
            choose=True
            if "+2" in iseeu2:
              printt("The computer played a +2 card! Taking +2 cards...")
              for i in range(2):
                time.sleep(1)
                deck.append(random.choice(cards))  
            elif "Reverse" in iseeu2:
              printt("The computer switched the order of which the turns go!")
              printt("This doesnt really help with 2 players...")
              time.sleep(3)
            elif "Skip" in iseeu2:
              printt("Skipping your turn...")
              skipp2=True
              time.sleep(2)
      zomg=True
      if choose==False:
        printt("The computer didnt have a card!")
        time.sleep(1)
        printt("Taking a card...")
        time.sleep(.5)
        print('\a',end='')
        deck2.append(random.choice(cards))
        time.sleep(1.5)
      else:
        choose=False
    clear()
    if len(deck2)==1:
      print(bold+'\033[31m'+underline("Computer says:Uno!"))
    if len(deck2)==0 or deck2==[]:
      for i in range(5):
        print(bold+'\033[31m'+"Computer wins!")
        time.sleep(.3)
        print(bold+'\033[34m'+"Computer wins!")
        time.sleep(.3)
        print(bold+'\033[32m'+"Computer wins!")
        time.sleep(.3)
        print(bold+'\033[33m'+"Computer wins!")
        time.sleep(.3)
      time.sleep(2)
      clear()
      tyforthat2=False
  def gamething():
    global dicts,start,theonez,turnturnpls,skipp,deck,deck2,theeee,wildz,skipp2,tyforthat2,tyforthat,goingforitithink
    tyforthat=True
    while tyforthat:
      startcard = cardconvert(start)
      start69=normconvert(start)
      print(reset1+"Card in play:")
      print(startcard+'\n'+start+"("+dicts[start69][0]+")")
      reset()
      dicts['Wild Card'][0]=="All"
      if turnturnpls=="P":
        print(bold+'\nWhich card would you like to place?\n(Say n if you dont have a move/want to pick up a card, e to exit)')
        reset()
        print(underline("Your cards:"))
        cardsr()
        print("")
        print(underline("Computer's cards:"))
        for oranumberoraletter in range(len(deck2)):
          print("?",end="  ")
        print("")
        printt("(Say the position of the card(Ex: "+deck[0]+reset1+" = 1"+") or the card name)",0.03)
        reset()
        try:
          theonez=input()
          if theonez.lower() == 'e':
            raise LeaveNowOrDie
        except:
          tyforthat=False 
        if theonez.lower() in ['n','no','nope']:
          z=random.choice(cards)
          printt("You drew a "+z)
          reset()
          time.sleep(2)
          deck.append(z)
          theeee=start
          theonez='/'
          turnturnpls="C"
          clear()
        f=judge(theonez,deck)
        if f==True:
          if "Skip" in theeee:
            printt("You played a Skip Card! Skipping the computers turn!")
            skipp=True
          elif "+4" in theeee:
            printt("You played a "+underline("+4 card")+"!")
            printt("Giving the computer +4 cards..")
            for i in range(4):
              print("\a",end="")
              time.sleep(.5)
              deck2.append(random.choice(cards))
            time.sleep(1)
            print("")
          elif 'Wild' in theeee:
            wildz=True
            while True:
              printt("You played a "+underline("Wild Card")+"!")
              time.sleep(1)
              printt("What color do you want the computer to next play?\n(Red,Yellow,Blue,Green)")
              coor=input()
              if coor.lower() in ['red','yellow','green','blue']:
                coor=coor.lower()
                coor=coor[0].upper()+coor[1:]
                printt("The color is now "+coor)
                dicts["Wild Card"][0]=coor
                time.sleep(2)
                break
              else:
                print("You have to pick a color!")
                time.sleep(3)
                clear()
          elif "+2" in theeee:
            printt("You played a +2 card! Giving the computer +2 cards...")
            for i in range(2):
              print("\a",end="")
              time.sleep(1)
              deck2.append(random.choice(cards))
            print("")
            time.sleep(1)
          elif "Reverse" in theeee:
            printt("You switched the order of which the turns go!")
            time.sleep(1)
            printt("This doesnt really help with 2 players...")
            time.sleep(3)
          else:
            printt("You played a "+theeee)
            time.sleep(2)
          if len(deck)==1:
            print(bold+'\033[32m'+underline("You say:Uno!"))
            reset()
            time.sleep(2)
          if deck==[] or len(deck)==0:
            clear()
            goingforitithink=True
            clear()
            tyforthat=False
          start=theeee
          clear()
          if skipp==False:
            turnturnpls='C'
          else:
            skipp=False
          if wildz==False:
            dicts['Wild Card'][0]="All"
          else:
            wildz=False
      elif turnturnpls=="C":
        if turnturnpls=='C':
          reset()
          compturn()
          if tyforthat2==False:
            tyforthat2=True
            tyforthat=False
          if skipp2==False:
            turnturnpls='P'
          else:
            skipp2=False
            turnturnpls='C'
          if wildz==False:
            dicts['Wild Card'][0]="All"
          else:
            wildz=False
  gamething()
  if goingforitithink==True:
    return True
  else:
    return False

colorz=[red,yellow,bright_yellow,green,blue,magenta]
def pattern():
  z=0
  f=1
  o=-1
  g=.03
  rain=True
  thenum=12
  yual=50
  try:
    while True:
      o+=1
      z+=f
      print(' '*z,end="")
      if rain==True:
        print(colorz[o%6],end="")
      else:
        print(random.choice(colorz),end="")
      print('*'*thenum)
      if z>yual:
        f=-1
      if z<1:
        f=1
      time.sleep(g)
  except KeyboardInterrupt:
    pass


p1='\033[38;5;1m'
p2='\033[38;5;2m'
p3='\033[38;5;3m'
p4='\033[38;5;4m'
p5='\033[38;5;5m'
p6='\033[38;5;6m'
p7='\033[38;5;7m'
p8='\033[38;5;8m'
p9='\033[38;5;9m'
p0='\033[38;5;10m'
reset='\033[0m'
spots={
  124:13,138:3,152:3,166:23, #Top
  358:1,372:0,386:0,400:2, #Lower
  590:1,604:0,618:0,632:2, #Lower
  822:14,836:4,850:4,864:24  #Bottom
}

spotmoving=''
dolro={
  '2':p2,
  '3':p3,
  '4':p4,
  '5':p5,
  '6':p6,
  '7':p7,
  '8':p8,
  '9':p9,
  '0':p0,
  '1':p1
}
board209='''
┌─────────────┬─────────────┬─────────────┬─────────────┐
│             │             │             │             │
│      -      │      -      │      -      │      -      │ 
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │ 
│      -      │      -      │      -      │      -      │
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │
│      -      │      -      │      -      │      -      │
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │
│      -      │      -      │      -      │      -      │
│             │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
'''
eeee=''
upslots=[124,138, 152, 166, 358, 372, 386, 400, 590, 604, 618, 632, 822, 836, 850, 864]
downslots=upslots[::-1]#Neat trick for reversing
rightslots=[166,400,632,864,152,386,618,850,138,372,604,836,124,358,590,822]
leftslots=rightslots[::-1]
score209=0
def pls2048():
  global board209,score209,upslots,downslots,leftslots,rightslots,dolro,p1,p2,p3,p4,p5,p6,p7,p8,p9,p0,spots,reset,eeee,spotmoving
  #WORKSSSSSSSSSSSSSSSSSS YESSSSSSSSSSSSS
  board209='''
┌─────────────┬─────────────┬─────────────┬─────────────┐
│             │             │             │             │
│      -      │      -      │      -      │      -      │ 
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │ 
│      -      │      -      │      -      │      -      │
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │
│      -      │      -      │      -      │      -      │
│             │             │             │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │
│      -      │      -      │      -      │      -      │
│             │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
'''
  board209=list(board209)
  def next1(argumenty):
    global score209
    if argumenty=='1':
      score209+=20
      return '2   '
    elif argumenty=='2':
      score209+=30
      return '3   '
    elif argumenty=='3':
      score209+=40
      return '4   '
    elif argumenty=='4':
      score209+=50
      return '5   '
    elif argumenty=='5':
      score209+=60
      return '6   '
    elif argumenty=='6':
      score209+=70
      return '7   '
    elif argumenty=='7':
      score209+=80
      return '8   '
    elif argumenty=='8':
      score209+=90
      return '9   '
    elif argumenty=='9':
      score209+=100
      return '0   '
    else:
      return '1   '
  def startboard209(tt=False):
    if tt==False:
      yuiop=random.choice([1,2,1])
    else:
      yuiop=2
    for i in range(yuiop):
      if '-' in board209:
        good=True
        while good:
          thingietoreplace=upslots[random.randint(0,15)]
          if board209[thingietoreplace]=='-':
            board209[thingietoreplace]=random.choice(['1','2','1'])
            good=False
  def printboard209():
    for ip in board209:
      dolro.setdefault(ip,'')
      print(dolro[ip]+ip+reset,end="")
  #Will go the direction it was specified once. If the space is not a '-', it will stop and see if it is equal to it. If it is equal to it, make it the higher number. Got to check the numbers from where it is moving from to back, so like up we have to check the top numbers
  def move(dir):
    global board209,eeee,spotmoving
    indexes=[a for a,i in enumerate(board209) if i in ['2','4','8']]
    if dir=='up': 
      for thejigjgf in range(2):
        tyu=upslots
        for pos1 in tyu:
          pos2=pos1
          if spots[pos2] not in [13,3,23]: #If it is not a top piece
            if board209[pos2]!='-':#If it is a number
              spotmoving=board209[pos2]
              #print(spotmoving+" ok")
              #print(board209[upslots[upslots.index(pos1)-4]])
              fff=True
              while pos2 not in [124,138,152,166] and fff==True:
                if board209[upslots[upslots.index(pos2)-4]]=='-':
                  board209[pos2]='-'
                  board209[upslots[upslots.index(pos2)-4]]=spotmoving[0]
                  pos2=upslots[upslots.index(pos2)-4]
                  spotmoving=board209[pos2]
                if board209[upslots[upslots.index(pos2)-4]]!='-':
                  if board209[upslots[upslots.index(pos2)-4]]==spotmoving:
                    eeee=next1(spotmoving)
                    board209[upslots[upslots.index(pos2)-4]:(upslots[upslots.index(pos2)-4]+4)]=eeee
                    board209[pos2]='-'
                    pos2=upslots[upslots.index(pos2)-4]
                    spotmoving=board209[pos2]
                    fff=False
                  else:
                    fff=False
    if dir=='down':
      for thejigjgf1 in range(2):
        tyu1=downslots
        for pos13 in tyu1:
          pos12=pos13
          if spots[pos12] not in [14,4,24]: #If it is not a top piece
            if board209[pos12]!='-':#If it is a number
              spotmoving=board209[pos12]
              #print(spotmoving+" ok")
              #print(board209[upslots[upslots.index(pos1)-4]])
              fff2=True
              while pos12 not in [822,836,850,864] and fff2==True:
                if board209[downslots[downslots.index(pos12)-4]]=='-':
                  board209[pos12]='-'
                  board209[downslots[downslots.index(pos12)-4]]=spotmoving[0]
                  pos12=downslots[downslots.index(pos12)-4]
                  spotmoving=board209[pos12]
                if board209[downslots[downslots.index(pos12)-4]]!='-':
                  if board209[downslots[downslots.index(pos12)-4]]==spotmoving:
                    eeee=next1(spotmoving)
                    board209[downslots[downslots.index(pos12)-4]:downslots[downslots.index(pos12)-4]+4]=eeee
                    board209[pos12]='-'
                    pos12=downslots[downslots.index(pos12)-4]
                    spotmoving=board209[pos12]
                    fff2=False
                  else:
                    fff2=False
    if dir=='right':
      for thejigjgf3 in range(2):
        tyu13=rightslots
        for pos132 in tyu13:
          pos122=pos132
          if spots[pos122] not in [24,2,23]: #If it is not a top piece
            if board209[pos122]!='-':#If it is a number
              spotmoving=board209[pos122]
              #print(spotmoving+" ok")
              #print(board209[upslots[upslots.index(pos1)-4]])
              fff3=True
              while pos122 not in [166,400,632,864] and fff3==True:
                if board209[rightslots[rightslots.index(pos122)-4]]=='-':
                  board209[pos122]='-'
                  board209[rightslots[rightslots.index(pos122)-4]]=spotmoving[0]
                  pos122=rightslots[rightslots.index(pos122)-4]
                  spotmoving=board209[pos122]
                if board209[rightslots[rightslots.index(pos122)-4]]!='-':
                  if board209[rightslots[rightslots.index(pos122)-4]]==spotmoving:
                    eeee=next1(spotmoving)
                    board209[rightslots[rightslots.index(pos122)-4]:rightslots[rightslots.index(pos122)-4]+4]=eeee
                    board209[pos122]='-'
                    pos122=rightslots[rightslots.index(pos122)-4]
                    spotmoving=board209[pos122]
                    fff3=False
                  else:
                    fff3=False
    if dir=='left':
      for thejigjgf0 in range(2):
        tyu0=leftslots
        for pos0 in tyu0:
          pos01=pos0
          if spots[pos01] not in [14,1,13]: #If it is not a top piece
            if board209[pos01]!='-':#If it is a number
              spotmoving=board209[pos01]
              #print(spotmoving+" ok")
              #print(board209[upslots[upslots.index(pos1)-4]])
              fff0=True
              while pos01 not in [124,358,590,822] and fff0==True:
                if board209[leftslots[leftslots.index(pos01)-4]]=='-':
                  board209[pos01]='-'
                  board209[leftslots[leftslots.index(pos01)-4]]=spotmoving[0]
                  pos01=leftslots[leftslots.index(pos01)-4]
                  spotmoving=board209[pos01]
                if board209[leftslots[leftslots.index(pos01)-4]]!='-':
                  if board209[leftslots[leftslots.index(pos01)-4]]==spotmoving:
                    eeee=next1(spotmoving)
                    board209[leftslots[leftslots.index(pos01)-4]:leftslots[leftslots.index(pos01)-4]+4]=eeee
                    board209[pos01]='-'
                    pos01=leftslots[leftslots.index(pos01)-4]
                    spotmoving=board209[pos01]
                    fff0=False
                  else:
                    fff0=False
  startboard209(True)
  score209=0
  #try:
  while True:
    c()
    printboard209()
    print("Score: "+str(score209))
    if '-' in board209:
      keyz=getkey()
      if keyz in ['w',UP]:
        move('up')
      if keyz in ['s',DOWN]:
        move('down')
      if keyz in ['d',RIGHT]:
        move('right')
      if keyz in ['a',LEFT]:
        move('left')
      if keyz in ['c','q']:
        c()
      startboard209()
    else:
      c()
      print("\t\t\t\t\t    You lost!\n\t\t\t\t\tFinal Score: "+str(score209))
      printboard209()
      raise NotokError
  #except:
  #  pass


toda=datetime.today()
timety=''
nameoff='bob'
c()
Listdesearches=["1) Welcome to Google, 'The Google Man!' How would you like to get started?","2) Chill out to your favorite beats! Links are in Music.txt!","3) Interested in getting the most out of your bot? Maybe just take 'thamoney'","4) Take a gra"]
#3 feet 3 3/8 inches=1meter
def convert(thek,econd):
  if econd=='M to F':
    return thek/3.2808399 
  if econd=='F to M':
    return thek*3.2808399

def printt(thingggg,dela=.04):
  for i in thingggg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(dela)
  print("")
#need weather?
#need google?

start=''
dicts=''
def clearline():
    sys.stdout.write('\x1b[1A') 
    sys.stdout.write('\x1b[2K')

money=100
muffin=cyan+"The Muffin Man:"+reset
muffin2=cyan+"The Muffin Man©:"+reset
muffin3=cyan+"The "+yellow+"Google"+cyan+" Man:"+reset
muffin=cyan+"The Muffin Man:"+reset
elem='''
Hydrogen       H   1
Helium         He  2
Lithium        Li  3
Beryllium      Be  4
Boron          B   5
Carbon         C   6
Nitrogen       N   7
Oxygen         O   8
Fluorine       F   9
Neon           Ne  10
Sodium         Na  11
Magnesium      Mg  12
Aluminium      Al  13
Silicon        Si  14
Phosphorus     P   15
Sulfur         S   16
Chlorine       Cl  17
Argon          Ar  18
Potassium      K   19
Calcium        Ca  20
Scandium       Sc  21
Titanium       Ti  22
Vanadium       V   23
Chromium       Cr  24
Manganese      Mn  25
Iron           Fe  26
Cobalt         Co  27
Nickel         Ni  28
Copper         Cu  29
Zinc           Zn  30
Gallium        Ga  31
Germanium      Ge  32
Arsenic        As  33
Selenium       Se  34
Bromine        Br  35
Krypton        Kr  36
Rubidium       Rb  37
Strontium      Sr  38
Yttrium        Y   39
Zirconium      Zr  40
Niobium        Nb  41
Molybdenum     Mo  42
Technetium     Tc  43
Ruthenium      Ru  44
Rhodium        Rh  45
Palladium      Pd  46
Silver         Ag  47
Cadmium        Cd  48
Indium         In  49
Tin            Sn  50
Antimony       Sb  51
Tellurium      Te  52
Iodine         I   53
Xenon          Xe  54
Cesium         Cs  55
Barium         Ba  56
Lanthanum      La  57
Cerium         Ce  58
Praseodymium   Pr  59
Neodymium      Nd  60
Promethium     Pm  61
Samarium       Sm  62
Europium       Eu  63
Gadolinium     Gd  64
Terbium        Tb  65
Dysprosium     Dy  66
Holmium        Ho  67
Erbium         Er  68
Thulium        Tm  69
Ytterbium      Yb  70
Lutetium       Lu  71
Hafnium        Hf  72
Tantalum       Ta  73
Tungsten       W   74
Rhenium        Re  75
Osmium         Os  76
Iridium        Ir  77
Platinum       Pt  78
Gold           Au  79
Mercury        Hg  80
Thallium       Tl  81
Lead           Pb  82
Bismuth        Bi  83
Polonium       Po  84
Astatine       At  85
Radon          Rn  86
Francium       Fr  87
Radium         Ra  88
Actinium       Ac  89
Thorium        Th  90
Protactinium   Pa  91
Uranium        U   92
Neptunium      Np  93
Plutonium      Pu  94
Americium      Am  95
Curium         Cm  96
Berkelium      Bk  97
Californium    Cf  98
Einsteinium    Es  99
Fermium        Fm  100
Mendelevium    Md  101
Nobelium       No  102
Lawrencium     Lr  103
Rutherfordium  Rf  104
Dubnium        Db  105
Seaborgium     Sg  106
Bohrium        Bh  107
Hassium        Hs  108
Meitnerium     Mt  109
Darmstadtium   Ds  110
Roentgenium    Rg  111
Copernicium    Cn  112
Nihonium       Nh  113
Flerovium      Fl  114
Moscovium      Mc  115
Livermorium    Lv  116
Tennessine     Ts  117
Oganesson      Og  118
'''

helpdict={
  'need help help':muffin+" Say 'need help' to get to know some of the commands!",
  'need help pog':muffin+" Say 'need pog' because you have to",
  'need help python':muffin+" Say 'need python' to code one line... impressive",
  'need help gamble':muffin+" Say 'need gamble' to go to the casino!",
  'need help games':muffin+" Say 'need games' if you are craving some money or games!",
  'need help game':muffin+" Say 'need game' if you are craving some money or games!",
  'need help chat':muffin+" Say 'need chat' if you want to talk to the computer",
  'need help clear':muffin+" Say 'need clear' to clear the screen of text",
  'need help joke':muffin+" Say 'need joke' to get some awful jokes",
  'need help convert':muffin+" Say 'need convert' to change centimeters to inches!",
  'need help time':muffin+" Say 'need time' to get the time since the epoch, in UTC",
  'need help calendar':muffin+" Say 'need calendar' to get the current month's calendar!",
  'need help schedule':muffin+" Say 'need schedule' to get a list of all the tasks you made with 'need todo'!",
  'need help tasks':muffin+" Say 'need tasks' to get a list of all the tasks you made with 'need todo'!",
  'need help todo':muffin+" Say 'need todo' to schedule a task for you to do! Say 'need tasks' to view when your task is going to happen!(Only works if you fork project)",
  'need help timer':muffin+" Say 'need timer' to get a timer and stopwatch!",
  'need help stopwatch':muffin+" Say 'need stopwatch' to get a timer and stopwatch!",
  'need help fortnite':muffin+" Dude really? If you want say `need fortnite`, whatever",
  'need help money':muffin+" Say 'need money' to get your balance",
  'need help elements':muffin+" Say 'need elements' to get a periodic table!",
  'need help work':muffin+" Say 'need work' to work! You just get some money man, but to save your data you got to fork this project",
  'need help subs':muffin+" You a youtuber?",
  'need help girlfriend':muffin+" Bro you desperate",
  'need help quest':muffin+" You want to battle some ogres? Say 'need quest'",
  'need help rainbow':muffin+" Its just a rainbow! Say 'need rainbow'"
 
  
}
creeper=["Creeper, aww man","So we back in the mine, got our pick axe swinging from side to side,","Side, side to side","This task a grueling one,","Hope to find some diamonds tonight, night, night","Diamonds tonight","Heads up, you hear a sound,","Turn around and look up, total shock fills your body,","Oh no it's you again,","I could never forget those eyes, eyes, eyes,","Eyes, eyes, eyes","'Cause baby tonight,","The creeper's trying to steal all our stuff again,","'Cause baby tonight, you grab your pick, shovel and bolt again,","And run, run until it's done, done,","Until the sun comes up in the morn'","'Cause baby tonight, the creeper's trying to steal all our stuff again","Just when you think you're safe,","Overhear some hissing from right behind,","Right, right behind","That's a nice life you have,","Shame it's gotta end at this time, time, time,","Time, time, time, time","Blows up, then your health bar drops,","You could use a 1-up, get inside don't be tardy,","So now you're stuck in there,","Half a heart is left but don't die, die, die","Die, die, die, die","'Cause baby tonight,","The creeper's trying to steal all your stuff again,","'Cause baby tonight, you grab your pick, shovel and bolt again,","And run, run until it's done, done,","Until the sun comes up in the morn'","'Cause baby tonight,","The creeper's trying to steal all your stuff again,","Creepers, you're mine","Dig up diamonds, and craft those diamonds and make some armor,","Get it baby, go and forge that like you so, MLG pro,","The sword's made of diamonds, so come at me bro","Training in your room under the torch light,","Hone that form to get you ready for the big fight,","Every single day and the whole night,","Creeper's out prowlin' - alright","Look at me, look at you,","Take my revenge that's what I'm gonna do,","I'm a warrior baby, what else is new,","And my blade's gonna tear through you","Bring it","'Cause baby tonight,","The creeper's trying to steal all our stuff again,","Yeah baby tonight, grab your sword, armor and gold, take your revenge,","So fight, fight like it's the last,","Last night of your life, life, show them your bite,","'Cause baby tonight,","The creeper's trying to steal all our stuff again,","'Cause baby tonight, you grab your pick, shovel and bolt again,","And run, run until it's done, done,","Until the sun comes up in the morn'","'Cause baby tonight, the creepers tried to steal all our stuff again"]
jokes=['Why did the italian play Among Us?'+green+' He wanted to be the impasta','Did you hear about the guy scared of negative numbers?'+green+" He'll stop at nothing to avoid them",'Did you hear about the clasutophobic astronaut?'+green+" He just wanted some space","Why shouldn't you trust atoms? "+green+"They make up everything","Why can't you change a pirate?"+green+" Because they argh who they argh","Why did the man consult his bed for insurance?"+green+" Because his sheets got him covered","Why are clowns never hunted?"+green+" They taste funny",'Why did the football coach go to the bank?'+green+" He wanted his quaterback"]
print(muffin+" Welcome "+nameoff+', say "need help" to start!\nWARNING: this was made years ago, humor, code, and overall everything is outdated as hell (and cringe)')

slotops=['🍒','🍋','Ⓙ','🍊','🍇','🍉']
slot1='🍒'
slot2='🍒'
slot3='🍒'

slottemp='''
||||||||||||||||
| '''+slot1+'''  | '''+slot2+'''  | '''+slot3+'''  |
||||||||||||||||
'''

def upslot():
  global slottemp
  slottemp='''
||||||||||||||||
| '''+slot1+'''  | '''+slot2+'''  | '''+slot3+'''  |
||||||||||||||||
'''

def cleartime(arghere):
  time.sleep(arghere)
  c()

def inputt(arnife):
  return input(arnife).lower().strip()

statesz='''
Alabama         Montgomery   Yellowhammer State
Alaska         Juneau   The Last Frontier
Arizona         Phoenix   The Grand Canyon State
Arkansas        Little Rock   The Natural State
California      Sacramento   The Golden State
Colorado        Denver   The Centennial State
Connecticut     Hartford   The Constitution State
Delaware        Dover   The First State
Florida         Tallahassee   The Sunshine State
Georgia         Atlanta   The Peach State
Hawaii          Honolulu   The Aloha State
Idaho           Boise   The Gem State
Illinois        Springfield   Prairie State
Indiana         Indianapolis   The Hoosier State
Iowa            Des Moines   The Hawkeye State
Kansas          Topeka   The Sunflower State
Kentucky        Frankfort   The Bluegrass State
Louisiana       Baton Rouge   The Pelican State
Maine           Augusta   The Pine Tree State
Maryland        Annapolis   The Old Line State
Massachusetts   Boston   The Bay State
Michigan        Lansing   The Great Lakes State
Minnesota       St. Paul   The North Star State
Mississippi     Jackson   The Magnolia State
Missouri        Jefferson City   The Show Me State
Montana         Helena   The Treasure State
Nebraska        Lincoln   The Cornhusker State
Nevada          Carson City   The Silver State
New Hampshire   Concord   The Granite State
New Jersey      Trenton   The Garden State
New Mexico      Santa Fe   The Land of Enchantment
New York        Albany   The Empire State
North Carolina  Raleigh   The Tar Heel State
North Dakota    Bismarck   The Peace Garden State
Ohio            Columbus   The Buckeye State
Oklahoma        Oklahoma City     The Sooner State
Oregon          Salem   The Beaver State
Pennsylvania    Harrisburg   The Keystone State
Rhode Island    Providence   The Ocean State
South Carolina  Columbia   The Palmetto State
South Dakota    Pierre   Mount Rushmore State
Tennessee       Nashville   The Volunteer State
Texas           Austin   The Lone Star State
Utah            Salt Lake City   The Beehive State
Vermont         Montpelier   The Green Mountain State
Virginia        Richmond   The Old Dominion State
Washington      Olympia   The Evergreen State
West Virginia   Charleston   The Mountain State
Wisconsin       Madison   The Badger State
Wyoming         Cheyenne   The Equality or Cowboy State
'''

rickast='''
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
'''

allstarshrek='''
Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead

Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the backstreets?
You'll never know if you don't go
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

It's a cool place, and they say it gets colder
You're bundled up now, wait 'til you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how 'bout yours?
That's the way I like it and I'll never get bored

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
All that glitters is gold
Only shooting stars break the mold

Go for the moon
Go for the moon
Go for the moon
Go for the moon

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars

Somebody once asked, “could I spare some change for gas?
I need to get myself away from this place"
I said, "Yep, what a concept
I could use a little fuel myself and we could all use a little change"

Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the backstreets?
You'll never know if you don't go (Go!)
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

And all that glitters is gold
Only shooting stars break the mold
'''

wernumber1='''
Hey!
We are Number One
Hey!
We are Number One

Now listen closely
Here's a little lesson in trickery
This is going down in history
If you wanna be a Villain Number One
You have to chase a superhero on the run
Just follow my moves, and sneak around
Be careful not to make a sound
(Shh)
(No, don't touch that!)

We are Number One
Hey!
We are Number One
We are Number One

Ha ha ha
Now look at this net, that I just found
When I say go, be ready to throw
Go!
(Throw it on him, not me!)
(Ugh, let's try something else)
Now watch and learn, here's the deal
He'll slip and slide on this banana peel!
(Ha ha ha, gasp! what are you doing!?)

We are Number One
Hey!
We are Number One
We are Number One
Hey!
We are Number One
Hey!
Hey!
'''


def printt(thingggg,dela=.03):
  for i in thingggg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(dela)
  print("")

def battleque():
  ogre1=100
  ogre2=100
  player1=100
  while (ogre1>0 or ogre2>0) and player1>0:
    shieding=False
    letsgetit=''
    while letsgetit not in ['a','attack','b','block','p','potion']:
      c()
      print(muffin+" You have "+green+str(player1)+reset+" health remaining!")
      print(muffin+" The Ogres have "+red+str(ogre1)+reset+' and '+red+str(ogre2)+reset+" health left!")
      print(muffin+random.choice([" Bro you got to keep attacking",' Lets get this bread',' Wonder if one of them is Shrek?',' I dont think they want to have some tea']))
      print(blue+"A to attack "+green+" B to block "+magenta+" P for potions"+reset)
      letsgetit=input(">> ").lower().strip()
    if letsgetit in ['a','attack']:
      c()
      printt(muffin+" Who do you want to attack?\n1) Ogre 1 ("+red+str(ogre1)+reset+")\n2) Ogre 2 ("+red+str(ogre2)+reset+")")
      enepls=input(">  ").strip().lower()
      if enepls not in ['1','ogre1','ogre 1','2','ogre2','ogre 2']:
        printt(muffin+" Bro i dont know what you said, im just going to do the first one")
      printt(muffin+" You charge up to the ogre and swing your Supa-sharp-V.3000-Mega-Super-Ogre-Slayer-Longsword")
      attackrange=random.randint(30,60)
      if attackrange<35:
        printt(muffin+" You realize you actually dont know what a Supa-sharp-V.3000-Mega-Super-Ogre-Slayer-Longsword is...")
        printt(muffin+" You only deal "+str(attackrange)+" damage to the ogre")
      elif attackrange>40:
        printt(muffin+" You land a hit!")
        printt(muffin+" You dealt "+str(attackrange)+" damage!")
      else:
        printt(muffin+" You hit the thing with the thing")
      if enepls not in ['1','ogre1','ogre 1','2','ogre2','ogre 2'] or enepls in ['1','ogre1','ogre 1']:
        if ogre1>0:
          ogre1-=attackrange
        else:
          printt(muffin+random.choice([" Do you really hate the ogre that much?",' Bro hes already dead....',' Quit slapping dead bodies']))
      if enepls in ['2','ogre2','ogre 2']:
        if ogre2>0:
          ogre2-=attackrange
        else:
          printt(muffin+random.choice([" Do you really hate the ogre that much?",' Bro hes already dead....',' Quit slapping dead bodies']))
    elif letsgetit in ['p','potions','potion']:
      printt(muffin+" Who do you want to attack?\n1) Ogre 1 ("+red+str(ogre1)+reset+")\n2) Ogre 2 ("+red+str(ogre2)+reset+")")
      enepls=input(">  ").strip().lower()
      c()
      printt(muffin+" You pull out a potion from the ground, like any other day")
      f1221=random.randint(1,3)
      if f1221==1:
        printt(muffin+" It looks pretty green, so you decide to drink it")
        they12=random.randint(20,30)
        time.sleep(1)
        printt(muffin+" Instead of dying, you actually feel better!"+green+" ("+str(they12)+" health gained!)"+reset)
        player1+=they12
      if f1221==2:
        printt(muffin+" A purple one this time. Wonder what it does. You decide to chuck it at the ogre")
        time.sleep(1)
        anorand=random.randint(1,2)
        if anorand==1:
          printt(muffin+" The ogre stops for a moment.")
          time.sleep(1)
          printt(muffin+" Suddenly the ogre starts to make weird 'oof' noises")
          time.sleep(1)
          popoo2=True
          randrangeobi=random.randint(25,40)
          if enepls in ['1','ogre1','ogre 1'] or enepls not in ['1','ogre1','ogre 1','2','ogre2','ogre 2']:
            if ogre1>0:
              ogre1-=ANOrando
              teezers='Ogre 1'
            else:
              popoo2=False
          else:
            if ogre2>0:
              ogre2-=randrangeobi
              teezers='Ogre 2'
            else:
              popoo2=False
          printt(muffin+" Seems like it worked? "+green+"("+teezers+" lost "+str(randrangeobi)+" health!)")
        else:
          printt(muffin+" The ogre catches the potion in midair, and starts to drink it???")
          time.sleep(1.5)
          ANOrando=random.randint(10,20)
          popoo=True
          if enepls in ['1','ogre1','ogre 1'] or enepls not in ['1','ogre1','ogre 1','2','ogre2','ogre 2']:
            if ogre1>0:
              ogre1+=ANOrando
              teezers='Ogre 1'
            else:
              popoo=False
          else:
            if ogre2>0:
              ogre2+=ANOrando
              teezers='Ogre 2'
            else:
              popoo=False
          printt(muffin+" You remember smelling onions before throwing the potion.... "+red+"("+teezers+" gained "+str(ANOrando)+" health!)"+reset)
          if not popoo:
            printt(muffin+" But hes still dead.")
      if f1221==3:
        printt(muffin+" A red potion! Must be dangerous! You throw it straight at the ogre")
        teeniprb=random.randint(1,3)
        mustaatc=random.randint(20,70)
        if teeniprb in [1,2]:
          printt(muffin+" The ogre looks like he just ate Burger King Foot lettuce")
          bruhmmmm=False
          if enepls in ['1','ogre1','ogre 1'] or enepls not in ['1','ogre1','ogre 1','2','ogre2','ogre 2']:
            if ogre1>0:
              ogre1-=mustaatc
              teezers='Ogre 1'
            else:
              bruhmmmm=True
          else:
            if ogre2>0:
              ogre2-=mustaatc
              teezers='Ogre 2'
            else:
              bruhmmmm=True
          time.sleep(.5)
          printt(muffin+" ("+green+str(mustaatc)+" damage to "+teezers+reset+")!")
          if bruhmmmm:
            printt(muffin+" (Stop slapping dead bodies!)")
        else:
          printt(muffin+" The ogre gets a direct hit!")
          time.sleep(1)
          printt(muffin+" Wait the potion is flipping cranberry juice....")
          printt("(0 damage dealt)")
      thetyie=random.randint(1,3)
      if thetyie==1:
        healo=random.randint(15,25)
        printt(muffin+" After throwing your potion, some weird fairy comes and heals "+str(healo)+" health")
        player1+=healo
    elif letsgetit in ['b','block','shield']:
      printt(muffin+" Bruh this option was just to have three options..")
      time.sleep(1) 
      printt(muffin+" Whatever, you decide to grab a shield from the ground.")
      time.sleep(1)
      shieding=True
    input('[Enter to Continue]')
    c()
    ogre1a=random.randint(5,20)
    ogre2a=random.randint(5,20)
    damage=0
    if ogre1>0 and ogre2>0:
      printt(muffin+" The Ogres both attack!")
      printt(muffin+" The first Ogre "+random.choice(['swings his club','doesnt like you','turns to you'])+" and deals "+str(ogre1a)+" damage")
      printt(muffin+" The second Ogre "+random.choice(['swings his wood axe','smells you','doesnt like your hair'])+" and deals "+str(ogre2a)+" damage")
      player1-=ogre1a
      player1-=ogre2a
      damage=ogre2a+ogre1a
    elif ogre1>0:
      printt(muffin+" The first Ogre "+random.choice(['swings his club','doesnt like you','turns to you'])+" and deals "+str(ogre1a)+" damage")
      player1-=ogre1a
      damage=ogre1a
    elif ogre2>0:
      printt(muffin+" The second Ogre "+random.choice(['swings his wood axe','smells you','doesnt like your hair'])+" and deals "+str(ogre2a)+" damage")
      player1-=ogre2a
      damage=ogre2a
    time.sleep(1)
    if shieding:
      shieldrandonnes=random.randint(1,5)
      if shieldrandonnes==1:
        printt(muffin+" Your shield turned out to be a feather... Nice defense man.. (0 damage blocked)")
      if shieldrandonnes==2:
        printt(muffin+" Your shield turned out to be a plate of steel! ("+str(damage/1.5)+" damage blocked)")
        player1+=damage/1.5
      if shieldrandonnes==3:
        printt(muffin+" Your shield absorbed... Stuff? Your shield is some sort of jello? A slime? I dunno, but it blocked "+str(damage/2.5)+" damage")
        player1+=damage/2.5
      if shieldrandonnes==4:
        printt(muffin+" Your shield turned out to be an A+ grade fortified shield! Just lying around. (blocked "+str(damage)+" damage)")
        player1+=damage
      if shieldrandonnes==5:
        printt(muffin+" Your shield is an Uno Reverse Card. You gained "+str(damage)+" health.")
        player1+=damage*2
    input('[Enter to continue]')
    c()
  if player1>0:
    return 'win'
  else:
    return 'nope'

def chat():
  print(muffin+" You want to chat with me?")
  tyureii=inputt(">> ")
  if tyureii in ['e','y','ye','yea','yes','sure','why not','ok']:
    c()
    print(muffin+" Umm ok... I dont really gossip but sureeeee, how are ya?")
    feeldi=inputt("Chat > ")
    if feeldi in ['good','great','spectacular','']:
      print(muffin+" Cool beans man")
    elif feeldi in ['sad','depressed','lonely','sadness','mad','madness','not good','not ok',]:
      print(muffin+" Well i got a cool little animations here, if you want i could play it, its quite satisfying")
      simtimee=inputt("Chat > ")
      if simtimee in ['y','sure','ye'] or 'yes' in simtimee or 'yea' in simtimee:
        print(muffin+" Yayyyyyyyy Ok, after you hit enter it will start. Press Control+C to stop the animation!")
        input("[Enter to begin]")
        pattern()
        c()
        print(muffin+" Cool right? Onto more questions though, this is just the first")
      else:
        print(muffin+" Ok... I guess maybe next time")
    elif feeldi in ['on top of the world','on cloud nine']:
      print(muffin+" We got one happy boi right here, good to see that")
    else:
      print(muffin+" Umm i hope that means you are doing good? I cant really understand much....")
    print(muffin+" Well uhhh I dont know what to talk about.. well here, do you know any memes?")
    memesright=inputt("Chat > ")
    if memesright in ['y','yes','yea','sure','ye']:
      print(muffin+" Well I was built on memes, so say one and ill see if I know it")
      amemey=inputt("Chat > ")
      if 'number one' in amemey:
        print(muffin+" We are number oneee\n"+wernumber1)
      if 'shrek' in amemey or 'allstar' in amemey or 'all star' in amemey:
        print(muffin+" *Shrek=1000*\n"+allstarshrek+'\n')
      if 'rickroll' in amemey or 'rick astley' in amemey or 'rick roll' in amemey:
        print(muffin+" Get rickrolled\n"+rickast)
    else:
      print(muffin+' Well thats it, thats all i got')
    print(muffin+" Maybe more coming soon? Who knows")

def games():
  global money
  doinggames=True
  while doinggames:
    outofthis=0
    c()
    print(muffin+" This is where you can get some stonkz")
    print(muffin+" Winning a game means you get some money")
    print(muffin+" You got "+str(money)+" monies")
    print(muffin+" Here are the options, say 'n' to exit")
    print("1) Tic Tac Toe\n2) A Maze\n3) Uno\n4) Rock Paper Scissors")
    omg=inputt('>> ')
    if omg in ['1','2','3','4']:
      if omg=='1':
        z143=tictactoe()
        if z143==True:
          outofthis+=10
      if omg=='2':
        mazeg()
        outofthis+=20
      if omg=='3':
        z4325=uno()
        if z4325==True:
          outofthis+=50
      if omg=='4':
        therick=rps()
        money+=therick*4
      money+=outofthis
    elif omg in ['n','no']:
      doinggames=False
    else:
      c()
      print(muffin+" Bro you got to put 1,2,3,4,5 or n\n")


timetime={}

def save():
  with open(nameoff+".dat",'wb') as save:
    pickle.dump(money, save, protocol = 2)


def load():
  try:
    global money
    with open(nameoff+".dat",'rb') as save:
        money = pickle.load(save)
  except:
    pass


def save2():
  with open(nameoff+"1.dat",'wb') as save:
    pickle.dump(timetime, save, protocol = 2)


def load2():
  try:
    global timetime
    with open(nameoff+"1.dat",'rb') as save:
        timetime = pickle.load(save)
  except:
    pass


def save3():
  with open(nameoff+"2.dat",'wb') as save:
    pickle.dump(timety, save, protocol = 2)


def load3():
  try:
    global timety
    with open(nameoff+"2.dat",'rb') as save:
        timety = pickle.load(save)
    if timety-time.time()<=0:
      return False
    else:
      return True
  except:
    return False


def gamble():
  global money,slot1,slot2,slot3
  c()
  print(muffin+" This is where you blow your money bro")
  print(muffin+" You got "+str(money)+" monies in your wallet")
  if money>10:
    print(muffin+" Here's what you can do dude")
    print("1) Slots")
    print("2) Flip a coin")
    print("3) Dice")
    gambew=inputt(">> ")
    if gambew in ['1','slots']:
      trying=True
      while trying:
        print(muffin+" How much would you like to bet?[10-1000]")
        idunnodud=input(">> ").strip()
        try:
          if int(idunnodud)>=10 and 1000>int(idunnodud) and int(idunnodud)<=money:
            trying=False
          else:
            c()
            print(muffin+" *cringe* You got to say a legal bet")
        except:
          c()
          print(muffin+" Enter a legal number dude")
      money-=int(idunnodud)
      gainslo=0
      c()
      print("Spinning Slots...")
      time.sleep(1)
      slot1=random.choice(slotops)
      slot2=random.choice(slotops)
      slot3=random.choice(slotops)
      if slot1==slot2 or slot2==slot3 or slot3==slot1:
        gainslo+=round(int(idunnodud)/2)
      if slot1==slot2==slot3:
        gainslo+=int(idunnodud)
      if slot1=='Ⓙ':
        gainslo+=round(int(idunnodud))
      if slot2=='Ⓙ':
        gainslo+=round(int(idunnodud))
      if slot3=='Ⓙ':
        gainslo+=round(int(idunnodud))
      upslot()
      print(slottemp)
      print('\n'+muffin+" You got "+str(gainslo)+' monies')
      money+=gainslo
      input('[Enter to continue]')
      c()
    elif gambew in ['2','flip','flip coin','flip a coin']:
      rying=True
      while rying:
        print(muffin+" How much would you like to bet?[10-1000]")
        idunnodude=input(">> ").strip()
        try:
          if int(idunnodude)>=10 and 1000>int(idunnodude) and int(idunnodude)<=money:
            rying=False
          else:
            c()
            print(muffin+" *cringe* You got to say a legal bet")
        except:
          c()
          print(muffin+" Enter a legal number dude")
      money-=int(idunnodude)
      tailsoheads=True
      while tailsoheads:
        print(muffin+" Heads or tails?")
        headsup=inputt('')
        if headsup in ['heads','tails']:
          tailsoheads=False
        else:
          print(muffin+" You got to say heads or tails man")
      c()
      print("Flipping coin....")
      time.sleep(2)
      coin=random.choice(['heads','tails'])
      print(muffin+" The coin landed on "+coin)
      if coin==headsup:
        print(muffin+" You won "+str(int(idunnodude)*1.5))
        money+=int(idunnodude)*1.5
      else:
        print(muffin+" Better luck next time dude")
      input("[Enter to continue]")
    elif gambew in ['3','dice']:
      c()
      lrying=True
      while lrying:
        print(muffin+" How much would you like to bet?[10-1000]")
        dunnodude=input(">> ").strip()
        try:
          if int(dunnodude)>=10 and 1000>int(dunnodude) and int(dunnodude)<=money:
            lrying=False
          else:
            c()
            print(muffin+" *cringe* You got to say a legal bet")
        except:
          c()
          print(muffin+" Enter a legal number dude")
      money-=int(dunnodude)
      diceboi=True
      while diceboi:
        print(muffin+" Which number would you like to bet on \n(1-6, win= 5 times your bet)")
        therollbyu=input()
        if therollbyu in ['1','2','3','4','5','6']:
          diceboi=False
        else:
          print(muffin+" You got to say 1,2,3,4,5, or 6 man")
      c()
      therollbyme=random.choice(['1','2','3','4','5','6'])
      print('Rolling Dice....')
      time.sleep(2)
      print("\aThe dice landed on "+therollbyme)
      if therollbyme==therollbyu:
        print(muffin+" Its your lucky day!")
        print(muffin+" Here take my "+str(int(dunnodude)*5)+" monies")
        money+=int(dunnodude)*5
      else:
        print(muffin+" RIP you lost")
      input('[Enter to continue]')
    c()
  else:
    print(muffin+" You're broke man, try playing games for money.\n"+muffin+" Or just work")

pooplo=-1

def help():
  c()
  print(muffin+" These are most of the commands man, some of them are secret. Just say 'need' then the name\n\n")
  print(bright_black+"---------\nCommands:\n--------- "+red+"\n\nhelp, python, gamble, pog, game\n\n"+bright_red+"uno, rps, tictactoe, maze, 2048\n\n"+yellow+"chat, joke, clear, save, convert\n\n"+bright_yellow+"muffin, stuff, creeper, fortnite, todo, tasks\n\n"+green+"calendar, timer, stopwatch, error, today\n\n"+cyan+"elements, money, google, rickroll, work\n\n"+blue+"rainbow, subs, time, girlfriend, "+bold+"quest\n\n"+reset+magenta+"name, gas, friend, zigzag\n\n\n")
  print(muffin+" Say 'need help' then the command name to get some help on this")
  input('[Enter to continue]')
  c()


def ask():
  global pooplo,timetime,money,timety,toda,Listdesearches,nameoff
  load()
  while True:
    t=inputt(bold+'Main'+reset+' > ')
    if t=='need meme':
      print(muffin+" No memes here")
    elif t in ['need money','need balance','need wealth','need rich']:
      print(muffin+" You got "+str(money)+" monies")
    elif t in ['need joke','need jokes']:
      print(muffin+" Your life")
      print(muffin+" Jk man, say n to stop, say anything else to keep the jokes coming")
      plsmemeing=True
      tjelist=-1
      while plsmemeing:
        tjelist+=1
        randty=input('>> ').lower().strip()
        if randty in ['n','no']:
          plsmemeing=False
        else:
          if tjelist==len(jokes):
            print(muffin+" Thats all I got man")
            plsmemeing=False
          else:
            re=jokes[tjelist]
            print(muffin+' '+re+reset)
    elif t in ['need game','need games']:
      games()
    elif t in ['need directions','need locations']:
      print(muffin+" At the next right, turn left")
    elif t in ['need bathroom']:
      print(muffin+" Bro you cant even walk to the bathroom? You think im a toilet?")
    elif t in ['need love']:
      print(muffin+" Very sad times here")
    elif t in ['need gas']:
      print(muffin+" Bro ill give you some gas for 69.69")
      print(muffin+" What you say?")
      gaspls=input(">> ").lower()
      if (gasplsq in gaspls for gasplsq in['yes','y','yea','sure']):
        print(muffin+" Bro you just got scammed")
        money-=69
      else:
        print(muffin+" Bruh")
    elif t in ['need clear','clear']:
      c()
      print(muffin+" Cleared the screen of stuff")
    elif t in ['need dinner','need feast']:
      print(muffin+" Go outside and hunt a turkey boi. Bring him home and chop him up in cubed centimeters. Then roast him on a lava pool")
    elif t in ['need lunch']:
      print(muffin+" Go grab a spaghetti and cheese sandwich")
    elif t in ['need a command','need command']:
      print(muffin+" Say 'need rainbow'")
    elif t in ['need?','need ?','need something']:
      print(muffin+" Yes")
    elif t in ['need rainbow']:
      rdnav=-1
      for tyuyt in range(1000):
        rdnav+=1
        print([red,yellow,bright_yellow,green,blue][rdnav%5]+"rainbow",end="  ")
      print(reset+"[Enter to continue]")
      input()
      c()
    elif t in ['need recipe','need breakfast']:
      print(muffin+" Bro just take two eggs and throw them at the wall. Maybe eat them too")
    elif t in ['need covid','need coronavirus','need covid 19']:
      print(muffin+" Bruh no you dont")
    elif t in ['need zig','need zag','need ziggy','need zigzag']:
      print(muffin+" Ok bro, enter to be satisfied. Also hit Control+C (Copy) to exit the thing")
      input('[Enter to start]')
      pattern()
      c()
      print(muffin+" Pretty cool right?")
    elif t in ['need communism','need putin']:
      print(muffin+" https://i.ytimg.com/vi/xY9BOHRXAQ0/hqdefault.jpg, Go to line 1446")
    elif t in ['need fortnite','need to play fornite']:
      print(muffin+" Bruh cringe")
    elif t in ['need minecraft','need creeper','need creeper aw man','need pickaxe','need c']:
      pooplo+=1
      if pooplo<=len(creeper):
        print(muffin+" "+creeper[pooplo])
    elif t=='need help':
      help()
    elif t in ['need muffin','need muffins']:
      print(muffin,end=" ")
      for i in range(400):
        print("Muffin",end=" ")
      input('[Enter to continue]')
      c()
    elif t in ['need sample','need sample text']:
      print(muffin+" What sample bro, i got nothing")
    elif t=='need python':
      print(muffin+" Here dude i can take one line of code and give you the result, here try it")
      lineofstuff=input('>>> ')
      try:
        if 'os' not in lineofstuff:
          eval(lineofstuff)
        print(muffin+" GG, you did it")
      except:
        print(muffin+" Bro that isnt real code")
    elif t in['need time','need clock']:
      print(muffin+' '+time.asctime(time.localtime(time.time())))
    elif t in ['need calender','need calendar']:
      print(muffin+' Here is the calender for the month bro')
      print(calendar.month(toda.year,toda.month))
    elif t in ['need gamble','need to gamble','need bet']:
      gamble()
    elif t in ['need today']:
      print(muffin+" "+str(toda)[:10])
    elif t in ['need save','need to save']:
      save()
      print(muffin+" I saved your "+str(money)+" in your safe file")
    elif t in ['need stuff','need things']:
      print(muffin+" "+red+"H"+yellow+"e"+bright_yellow+"r"+green+"e"+blue+"s"+reset+" some "+bold+"stuff"+reset)
    elif t in ['need name','need my name','need your name']:
      print(muffin+" Wait do you want to know my name? Or want me to say your name?")
      inifsnfd=input(">> ")
      if inifsnfd in ['1','your name','the muffin man','yours','your']:
        c()
        print(muffin+" Bruh look at my name ITS RIGHT THERE")
      else:
        c()
        print(muffin+" Im going to say your name ok?")
        time.sleep(3)
        print("Doing random things.....")
        time.sleep(random.randint(1,2))
        print("Obtaining gud knowledge")
        time.sleep(random.choice([1,1.5,.75,2]))
        print("Getting your ip... (jk m8)")
        time.sleep(random.choice([1,1.25,.75,.5]))
        c()
        print(muffin+" Your name is "+nameoff)
        print(muffin+" But you already knew that..")
    elif t=='need nothing':
      print(muffin+" Bruh moment")
    elif t in ['need bruh','need bruh moment']:
      print(muffin+" BRUHHHHHHHHHH")
    elif t in ['need convert','need convertion','need inch to cm','need cm to inch']:
      print(muffin+" I got you bro, but I can only do cm and inch, or feet and meters")
      tyuisomuch=''
      while tyuisomuch not in ['1','2','3','4']: 
        print(muffin+" So what you want?\n1) Cm to in\n2) In to Cm\n3) Feet to Meter\n4) Meter to Feet")
        tyuisomuch=input()
        if tyuisomuch=='1':
          print(muffin+" Enter your cms")
          cmsthe=input()
          try:
            print(muffin+" Thats "+str(round(float(cmsthe)*2.54,6))+" inches man")
          except:
            print(muffin+" Dude that not a real number")
        if tyuisomuch=='2':
          print(muffin+" Enter your inches")
          cmsthe=input()
          try:
            print(muffin+" Thats "+str(round(float(cmsthe)/2.54,6))+" centimeters man")
          except:
            print(muffin+" Dude that not a real number")
        if tyuisomuch=='3':
          try:
            print(muffin+" Enter your feet")
            tytybro=input()
            z=convert(tytybro,'F to M')
            print(muffin+" Thats "+str(round(z,5)+" meters man"))
          except:
            print(muffin+" Dude that not a real number")
        if tyuisomuch=='4':
          try:
            print(muffin+" Enter your meters")
            tytybro=input()
            z=convert(tytybro,'M to F')
            print(muffin+" Thats "+str(round(z,5)+" feet man"))
          except:
            print(muffin+" Dude that not a real number")
    elif t=='need you':
      print(muffin+" Bro I'm here")
    elif t in ['need funny','need works','need rickrolls','need googles','need converts','need gambles','need gamess']:
      print(muffin+" Dude just say it normally")
    elif t in ['need google','need search','need internet']:
      c()
      printt(muffin+" Welcome to 100PercentGoogle!")
      time.sleep(1)
      printt(muffin3+" What would you like to search noble user?")
      input(yellow+"Search 100PercentGoogle > "+reset)
      c()
      for i in range(5):
        print("Loading |")
        cleartime(.2)
        print("Loading /")
        cleartime(.2)
        print("Loading -")
        cleartime(.2)
        print('Loading \\')
        cleartime(.2)
      c()
      time.sleep(1)
      zsearc=random.randint(1,4)
      listdeser=['1','2','3','4']
      printt(muffin3+" We could only find "+str(zsearc)+" items..")
      time.sleep(.5)
      printt(muffin3+" Well here they are!")
      for i in range(0,zsearc):
        printt(Listdesearches[i],0.03)
      searchops=input(">> ")
      if searchops in listdeser[0:zsearc]:
        printt(yellow+"Google: Welcome to the search results Muf-")
        time.sleep(.5)
        clearline()
        printt(muffin3+" Hello User! Here are your search results from the trustworthy 100PercentGoogle!")
        if searchops =='1':
          printt(muffin3+" .... I thought I deleted this...")
          time.sleep(.5)
          printt(muffin3+" User you didnt see anything ok?")
          time.sleep(2)
          c()
        if searchops =='2':
          printt(muffin3+" Seems like a 100PercentGoogle generated link! I Guess go to Music.txt and check it out")
          input('[Enter to continue]')
          c()
        if searchops =='3':
          printt(muffin3+" Dont listen to him user, Google only knows so much. Anyway who would have a command like 'thamoney', crazy right...")
          input('[Enter to continue]')
          c()
        if searchops =='4':
          printt(muffin3+" User, mind overlooking this?")
          time.sleep(1)
          printt(muffin3+" Seems like my creator didnt take the time to put that 4th result in the game...")
          time.sleep(.5)
          printt("[You see the bot searching google for another search result...]",0.03)
          Listdesearches[-1]="4) Error: Could not import 'Google' object"
          input('[Enter to continue]')
          c()
      else:
        c()
        printt(yellow+"Google: TheGoogleMan, You have not customized your search results! ANy mistaes will let to a blan-",0.02)
        time.sleep(1)
        c()
        printt(muffin3+" Oh shut up Google..")
    elif t in ['need friend','need friends']:
      print(muffin+" Thats pretty sad")
      print(muffin+" Asking a bot to be your friend")
      print(muffin+" But whatever, say 'need chat' if you really want a friend")
    elif t in ['need gamer','need to game']:
      print(muffin+" Gamer time")
    elif t in ['need main','need main.py']:
      print(muffin+" Bruh look at your lttle prompt below what does it say?")
    elif t in ['need battery','need charge']:
      print(muffin+" Bro plug in your device, im not an electrical grid")
    elif t in ['need subs','need subscribers','need likes']:
      print(muffin+" Hey guys, welcome to another episode of i dont have a life! Pls sub and like, i will give you a cookie")
    elif t in ['need code']:
      print(muffin+" If you want to code just say 'need python' bro. If you want some code, too bad im just a bot")
    elif t in ['need repl','need repl.it']:
      print(muffin+" Well its your lucky day!")
    elif t in ['need rap','need beatbox']:
      print(muffin+" Im not siri bro.. but maybe one day")
    elif t in ['need the muffin man','need muffin man','need the_muffin_man']:
      print(muffin+" You still havent looked at my name huh?")
    elif t in [' ']:
      print(muffin+" ...")
    elif t in ['need bug','need error','need 404']:
      print(muffin+" Error: '"+nameoff+"'s life' Does not exist.")
    elif t in ['need creator','need muffinlavania','need maker']:
      print(muffin+" Yep, thats me.. Muffinlavania... Hi")
    elif t in ['need the manager','need the boss']:
      print(muffin+" Bro no you dont i can give you your 69 gucci smartwatches")
    elif t in ['need schedule','need schdule','need task','need tasks','need s']:
      print(muffin+" Heres all your tasks man")
      load2()
      lolzers=[]
      if len(timetime.keys())>0:
        for taskt,timet in timetime.items():
          if timet-time.time()>0:
            print(taskt.title()+": In "+str(round(timet-time.time()))+" seconds")
          else:
            lolzers.append(taskt.title()+": Was at "+time.asctime(time.localtime(timet))+" ("+str(abs(round(timet-time.time())))+" seconds ago")
      else:
        print("None")
      print(muffin+" Finished/passed tasks:")
      for bruhmn in lolzers:
        print(bruhmn)
      if len(lolzers)==0:
        print('None')
    elif t=='need bot':
      print(muffin+" Am bot, pls talk")
    elif t=='need thamoney':
      print(muffin+" Here you go man")
      money+=100
    elif t in ['need ight ima head out','ight ima head out']:
      print(muffin+" A man of culture i see")
    elif t in ['need bing','need yahoo','need internet explorer']:
      print(muffin+" Bro... You didnt just as me for that")
    elif t in ['need rickroll','need rick astley']:
      print(muffin+rickast)
    elif t in ['need reminder','need todo']:
      print(muffin+" Do you want to schedule something to do?")
      maybeig=input(">> ")
      if [f for f in ['yes','yea','sure','ye'] if f in maybeig] or maybeig=='y':
        gggin=True
        while gggin:
          print(muffin+" Ok, first tell me at what time do you want to schedule this for? Say (number) + _ + (days,hours,minutes) Only pick one bro (Picking one or two units will confuse the computer)")
          thescheduled=input('>> ').strip()
          try:
            if thescheduled[0:thescheduled.index('_')].isdigit() and thescheduled[thescheduled.index('_')+1:].strip() in ['hours','hour','minute','minutes','min','mins','days','day'] and thescheduled.index('_')!=-1:
              gggin=False
            else:
              c()
              print(muffin+" You have to put a digit first(no 'need'), then an underscore then your units bro(pick hours,minutes,seconds)")
          except:
            c()
            print(muffin+" Thats not what I asked for man")
        c()
        print(muffin+" Now tell me what you want this event to be(the name of the task)")
        nameotask=input(">> ").strip()
        if thescheduled[thescheduled.index('_')+1:].strip() in ['hour','hours']:
          timethatitwas=time.time()+60*60*int(thescheduled[0])
          addedtime=thescheduled[0:thescheduled.index('_')]+" hours"
        if thescheduled[thescheduled.index('_')+1:].strip() in ['min','mins','minutes','minute']:
          timethatitwas=time.time()+60*int(thescheduled[0])
          addedtime=thescheduled[0:thescheduled.index('_')]+" minutes"
        if thescheduled[thescheduled.index('_')+1:].strip() in ['day','days']:
          timethatitwas=time.time()+60*60*24*int(thescheduled[0])
          addedtime=thescheduled[0:thescheduled.index('_')]+" days"
        print(muffin+" So "+nameotask+" is happening in "+addedtime+", i will save that to your safe file")
        timetime[nameotask]=timethatitwas
        save2()
        print(muffin+" Saved! Say 'need tasks' for your tasks!")
    elif t in ['need timer','need stopwatch','need to time']:
      timestary()
    elif t=='need':
      print(muffin+" Specify what you need boi")
    elif t=='need need':
      print(muffin+" Big brain right here")
    elif 'need need need' in t:
      print(muffin+" Ok stop")
    elif t in ['need greeting','need hi','need hello','need welcome']:
      print(muffin+" Hello! I am the Muffin Man!")
    elif t in ['need draw','need drawing','need pencil']:
      print(muffin+" Dude im not a pencil")
    elif t in ['need RPG','need story','need quest']:
      print(muffin+" Wait you came here to do a quest?")
      questbruh=input(">> ")
      if questbruh.lower() in ['yes','y','sure','yea','ye']:
        print(muffin+" Ummm... ok here goes nothing I guess")
        time.sleep(3)
        c()
        namequest=green+random.choice(['Jack','Joe','Rick','Cris','Demetris','Tim'])+reset
        printt(muffin+" You, "+namequest+", for some reason venture into the woods.")
        time.sleep(2)
        printt(muffin+" But these are no ordinary woods. As it turns out, these woods are the resting place of an evil witch from the 18th century")
        time.sleep(2)
        printt(muffin+" After venturing for a few minutes, you realize that you have no idea what you are doing out in these woods.")
        time.sleep(2.5)
        printt(muffin+" So you start heading back to house, 69 miles away from civilization")
        time.sleep(1)
        printt(muffin+" Yet when you get about 100 feet away from your house, 2 evil ogres pop out of the ground!")
        time.sleep(1)
        printt(muffin+" (Again these are not any other woods)",0.02)
        time.sleep(1.5)
        printt(muffin+" Luckily you decided to bring your Supa-sharp-V.3000-Mega-Super-Ogre-Slayer-Longsword on your walk!")
        printt('[Enter to continue]')
        input()
        gigigg=True
        while gigigg:
          c()
          wewd=battleque()
          if wewd=='win':
            print(muffin+" GG you won!")
            gigigg=False
          else:
            print(muffin+" Bruh rip")
            print(muffin+" Want to play again?")
            yeyeyey=input(">> ").lower().strip()
            if yeyeyey in ['yes','y','yea','sure','ye']:
              battleque()
            else:
              print(muffin+" Ok bye")
          
      else:
        print(muffin+" kthxbai")
    elif t in ['need drink','need water']:
      print(muffin+" Heres some "+blue+"virtual water"+reset+". Thats all i got")
    elif t in ['need work','need to work']:
      ethe=random.randint(100,150)
      timety=time.time()+60*60
      ethe2=load3()
      if ethe2==False:
        print(muffin+" Heres some "+str(ethe)+" monies bro")
        money+=ethe
        save3()
      else:
        print(muffin+" Chill dude you have to wait "+str(round(timety-time.time()))+" seconds")
    elif t == 'need gatorade':
      print(muffin+" No gatorade here sir")
    elif t=='need gamer bread':
      print(muffin+" Bro dont you have some already")
    elif t in ['need pls meme','need meme pls']:
      print(muffin+" Dude im not Dank Memer")
    elif t in ['need pog','need poggers','need pogger','need pog time']:
      print(muffin+bold+green+" POG"+reset)
    elif t in ['need life','need live']:
      print(muffin+" Very sad times here")
    elif t in ['need squid','need squids']:
      print(muffin+" This is a splash free zone")
      print(muffin+" All squids will be thrown into the "+red+"Red Sea")
    elif t in ['need maze','need a maze']:
      mazeg()
    elif t in ['need animal','need bird','need lion','need cat','need dog','need dogs','need cats','need zebras','need birds','need bears','need fish','need rat','need rats']:
      print(muffin+" Bro why would i have animals")
    elif t in ['need monies']:
      pritn(muffin+"Money money money money ")
    elif t in ['need roblox']:
      print(muffin+" Roblox noob time")
    elif t in ['need bass','i need bass','i need the bass','need the bass']:
      print(muffin+" Go watch Davie504")
    elif t in ['thx','thanks','thank you'] or 'thx' in t:
      print(muffin+" Your welcome?")
    elif  t in ['need rename']:
      print(muffin+ "Ok, what would you like me to call you?")
      tutuq=input("Name > ")
      print(muffin+" Ok man, im going to call you "+tutuq+" from now on.")
      nameoff=tutuq
    elif t in ['need elements','need periodic table','need pt']:
      print(elem+muffin+" Here I got you bro \n")
      print("[Enter to continue]")
      input()
      c()
    elif t in ['need copyright','need copyright claim']:
      print(muffin2+' Bro please d-[Content is claimed.]')
    elif t in ['need dead','need death','need die']:
      print(muffin+" I was never alive")
    elif t in ['need girlfriend','need gf','need boyfriend','need bf']:
      print(muffin+" I can hook you up with big chungus")
    elif t in ['need chat','need talk']:
      chat()
    elif t in ['need lol','need lmao','need lmbo']:
      print(muffin+" Dude i literally cant laugh. YOU do it")
    elif t in ['f','f in chat','e']:
      print(muffin+" Wise words")
    elif t in ['need food','need foods','need bagel']:
      print(muffin+" I dont have any bro, don't rob me")
    elif t in ['need cookie','need sweet','need treat']:
      print(muffin+" Heres a poptart, thats all i got")
    elif t in ['need 69','need 420','need 69420','need 42069']:
      print(muffin+" #bestnumber2020 69420")
    elif t in ['need coffin','need coffin dance']:
      print(muffin+" Insert Coffin Dance here")
    elif t in ['need load']:
      print(muffin+" LOADINGDWIAUBFE FIUBESDUYKGVBaEBFBYFBFEBHFEEFYBEF BUEFB SUEFF UYEF FBYHEFGGEU")
    elif t in ['need shrek','need all star']:
      print(muffin+" Bruh\n"+allstarshrek)
    elif t in ['need 2048','need matching game']:
      pls2048()
      print('')
    elif t in ['need tictactoe','need tic tac toe']:
      tictactoe()
    elif t in ['need uno','need dos']:
      uno()
    elif t in ['need rps','need rock paper scissors','need rsp']:
      rps()
    elif t in ['need number one','need we are number one','need we are number 1','need number 1']:
      print(muffin+" I am number one\n"+wernumber1)
    elif 'need spag' in t or 'need somebody touching my spag' in t:
      print(muffin+" SOMEBODY TOUCHING MY SPAGET")
    elif t in ['need exit']:
      print(muffin+" Bye")
      sys.exit() 
    elif t in helpdict.keys():
      print(helpdict[t])

ask()

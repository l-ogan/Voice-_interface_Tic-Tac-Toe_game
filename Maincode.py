#Tic tac toe game with voice interface
import random
import pyaudio
from gtts import gTTS
import playsound
import os

def speak(text):
    tts=gTTS(text=text,lang="en")
    r=random.randint(1,100000)
    filename="aud"+str(r)+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
   
    
def display_board(b):
    print(" "+"|"+" "+"|")
    print(b[7]+"|"+b[8]+"|"+b[9])
    print(" "+"|"+" "+"|")
    print("_ _ _ ")
    print(" "+"|"+" "+"|")
    print(b[4]+"|"+b[5]+"|"+b[6])
    print(" "+"|"+" "+"|")
    print("_ _ _ ")
    print(" "+"|"+" "+"|")
    print(b[1]+"|"+b[2]+"|"+b[3])
    print(" "+"|"+" "+"|")
    print("\n"*3)
    

    
def player_choose():
    marker=''
    while marker!="x" and marker!="O":
        speak("player 1 choose X or O")
        marker=input('X or O: ').upper()
        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")
        
def player_marker(board,marker,position):
    board[position]=marker

def win_check(b,marker):
   return ((b[7]==b[8]==b[9]==marker) or
   (b[4]==b[5]==b[6]==marker) or
   (b[1]==b[2]==b[3]==marker) or
   (b[7]==b[5]==b[3]==marker) or
   (b[1]==b[5]==b[9]==marker) or
   (b[1]==b[4]==b[7]==marker) or
   (b[2]==b[5]==b[8]==marker) or
   (b[3]==b[6]==b[9]==marker))

    
def go_first():
    flip=random.randint(0,1)
    if flip==0:
        return "player_1"
    else:
        return "player_2"
    
def space_check(board,position):
    return board[position]==''

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return True
    return False

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position):
        position=int(input("Choose a position:(1-9)=> "))
    return position
    
def replay():
    speak("Would you like to play once again")
    choice=input("Want to paly again y or n: ").upper
    return choice=="y"

#Main Logic To Play The Game
speak("Welcome To The Tic-Tac-Toe Game")  
speak("This game is created by shridhar")  
while True:
    ips=[" "]*10
    player1_marker,player2_marker=player_choose()
    turn=go_first()
    print(turn+"will go first")
    speak("Are you ready to play")
    play_game=input("Ready to play y or n : ")
    speak("Here it goes")
    speak("Best Of Luck")
    if play_game=="y":
        game_on=True
    else:
        game_on=False
        
    while game_on:
        if turn=="player_1":
            display_board(ips)
            speak("Player 1s turn")
            position=player_choice(ips)
            player_marker(ips,player1_marker,position)
            if win_check(ips,player1_marker)==True:
                display_board(ips)
                speak("Player1 Has Won The game")
                game_on=False
            else:
                if full_check(ips):
                    display_board(ips)
                    speak("It's a Tie")
                    game_on=False
                else:
                    turn="player_2"
        else:
            display_board(ips)
            speak("Player 2s turn")
            position=player_choice(ips)
            player_marker(ips,player2_marker,position)
            if win_check(ips,player2_marker):
                display_board(ips)
                speak("Player2 Has Won The game")
                game_on=False
            else:
                if full_check(ips):
                    display_board(ips)
                    speak("It's a Tie")
                    game_on=False
                else:
                    turn="player_1"
    if not replay():
        speak("Thanks for playing the game")
        break
    

















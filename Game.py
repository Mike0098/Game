
import time
global gold
global apples
gold = 0
apples = 0

def start():
        print("hello and Welcome")
        name = raw_input("What's your name:")
        print ("Welcome, "+name+"!")
        print ("The objective of this game is to collect apples.")
        print("The more apples you collect, the more you con sell.")
        choice = raw_input("Do you want to play?")
        if choice == "Y":
                begin()

                if choice == "N":
                        print ("Okay then...")
                def begin():
                        global apples
                print("Lets get started!")
                pick = raw_input("Do you want to pick an apple Y/N")
                if pick == "Y":
                                time.sleep(1)
                                print ("You pick an apple.")
                                apples=apples+1
                                
                                
start()

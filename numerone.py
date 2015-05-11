#!/usr/bin/env python

#
# Imports under here
#

import os
from random import randint

#
# System based functions
#
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#
# Class definition
#

class Numerone():
    """ Here it is, let's train """

    #
    # Class members
    #
    

    #
    # Class methods
    #

    def __init__(self):
        self.lunghezza = 25
        self.__menu()

    def __printHeader(self):
            clearScreen()

            print("""

            d8b   db db    db .88b  d88. d88888b d8888b.  .d88b.  d8b   db d88888b 
            888o  88 88    88 88'YbdP`88 88'     88  `8D .8P  Y8. 888o  88 88'     
            88V8o 88 88    88 88  88  88 88ooooo 88oobY' 88    88 88V8o 88 88ooooo 
            88 V8o88 88    88 88  88  88 88~~~~~ 88`8b   88    88 88 V8o88 88~~~~~ 
            88  V888 88b  d88 88  88  88 88.     88 `88. `8b  d8' 88  V888 88.     
            VP   V8P ~Y8888P' YP  YP  YP Y88888P 88   YD  `Y88P'  VP   V8P Y88888P 
                                                                                
            """
            )

    def __esci(self):
        return False

    def __nuovo(self):

        self.__printHeader()

        print("### Nuovo numero ###\n")

        try: 
            self.lunghezza = int(raw_input("Lunghezza numerone: "))
        except ValueError:
            print("Non valido")
            return True

        numero = str(randint(10**(self.lunghezza-1), (10**(self.lunghezza)-1)))
        print("Il nuemrone: \n")
        print(numero + "\n")
        raw_input("Memorizzalo, quando sei pronto premi invio per la verifica!\n")
        
        self.__printHeader()
        tentativo = raw_input("Inserisci il numerone:\n\n")

        if tentativo == numero:
            print("\nGOOD JOB!")
        else:
            print("\nSEI UNA PIPPA...")

        raw_input()
        return True

    def __menu(self):
        # Awesome python "switch"
        opzioni = {
                "0" : self.__esci,
                "1" : self.__nuovo,
                }
        loop = True
        while(loop):
            self.__printHeader()

            print("[1] Nuovo numero.")
            print("[0] Esci.")
            
            scelta = raw_input()

            # Error handling like a boss
            try:
                loop = opzioni[scelta]()
            except KeyError:
                pass
                                                     
if __name__ == "__main__":
    Numerone()

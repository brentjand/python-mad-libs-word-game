
import sys
import random

from mad_libs_wordgame.menu import show_menu
from mad_libs_wordgame.manual_storylines import economic_storyline
from mad_libs_wordgame.manual_storylines import scientific_storyline
from mad_libs_wordgame.manual_storylines import musical_storyline
from mad_libs_wordgame.automated_storylines import auto_economic_storyline
from mad_libs_wordgame.automated_storylines import auto_scientific_storyline
from mad_libs_wordgame.automated_storylines import auto_musical_storyline

while True:
    show_menu()
    player_input = input("Select an option: ")
    if player_input == "1":
        print("")
        economic_storyline()

    elif player_input == "2":
        print("")
        scientific_storyline()

    elif player_input == "3":
        print("")
        musical_storyline()

    elif player_input == "4":
        options = ["1","2","3"]
        automate = random.choice(options)
        if automate == "1":
            print(auto_economic_storyline())

        elif automate == "2":
            print(auto_scientific_storyline())

        elif automate == "3":
            print(auto_musical_storyline())

    elif player_input == "5":
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid option, try again.")

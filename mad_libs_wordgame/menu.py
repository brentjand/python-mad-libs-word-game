import time

def show_menu():
    print("")
    print("-----------------------------------------------------------------------------")
    print("                             Welcome to Mad Libs!                            ")
    print("                           The Phrasical Word Game                           ")
    print("-----------------------------------------------------------------------------")
    print("Ⓐ  Ⓑ  Ⓒ  Ⓓ  Ⓔ  Ⓕ  Ⓖ  Ⓗ  Ⓘ  Ⓙ  Ⓚ  Ⓛ  Ⓜ  Ⓝ  Ⓞ  Ⓟ  Ⓠ  Ⓡ  Ⓢ  Ⓣ  Ⓤ  Ⓥ  Ⓦ  Ⓧ  Ⓨ  Ⓩ")
    print("-----------------------------------------------------------------------------")
    print("              To begin, pick one of the options listed below."                )
    print("-----------------------------------------------------------------------------")
    print("                   1. Play an Economic Mad Lib                               ")
    print("                   2. Play a Scientific Mad Lib                              ")
    print("                   3. Play a Musical Mad Lib                                 ")
    print("                   4. Have the Computer Randomly Generate a Mad Lib          ")
    print("                   5. Exit the Game                                          ")
    print("-----------------------------------------------------------------------------")



#Ranomization ensures you are more likely to win the powerball than draw the same story twice.

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

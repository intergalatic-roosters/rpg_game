import ascii
quit = False


while quit == False:
    print(ascii.MAIN_MENU)
    choice = input().capitalize()

    if choice == "Q":
        quit = True

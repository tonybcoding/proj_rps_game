import games


legal_moves = ["rock", "paper", "scissors"]


def display_intro():
    #
    # create white space and present title
    print("\n" * 30)
    print("Welcome to Rock - Paper - Scissors!")
    print("\n" * 3)


def request_name():
    #
    # request name until user actually enters something
    while True:
        name = input("Please enter your name: ")
        if name == "":
            print("It's much better if I know your name!")
        else:
            break
    #
    # return name
    return name.capitalize()


def request_game_mode():
    #
    #
    while True:
        mode = input("Would you like to play '1. Set Rounds' or '2. Best of Rounds'? ")
        if (mode != "1" and mode != "2"):
            print("Please enter a valid option.")
        else:
            break
    return mode


def start_game():
    #
    # display intro and request user's name
    display_intro()
    user_name = request_name()
    #
    # ask desired game mode and instantiate appropriate class
    game_mode = request_game_mode()
    if game_mode = "1"
        game = games.SetRoundsGame()
    else:
        game = games.BestOfRoundsGame()





#
#
#
#
if __name__ == '__main__':
    start_game()
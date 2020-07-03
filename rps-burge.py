import random


legal_moves = ["rock", "paper", "scissors"]


###############################################################################
###############################################################################
###############################################################################


class Game:

    def __init__(self):
        #
        # request user name and store it
        # request game mode, set game type and get number of rounds
        # determine computer v computer or human v computer
        self.__display_intro()
        self.__game_settings()
        #
        # create player objects
        #
        # play game
        #
        # show results


    def __game_settings(self):
        self.user = self.__request_name()
        self.game_type = self.__set_game_type()
        self.game_rounds = self.__num_of_rounds()
        self.game_player_types = self.__set_player_types()      
        print(f"\n\nOkay, we're all set, {self.user}!")
        print(f"Let's play {self.game_rounds} rounds of {self.game_type[3]}: "
            f"{self.game_player_types[0][1]} VS. "
            f"{self.game_player_types[1][1]}")
        print(f"")


    def __set_player_types(self):
        #
        # declare local variables
        # player types list:
        # [[type player 1, description],[type player 2, description]
        # 0 = human, 1 - 4 for computer types
        player_type_list = []
        #
        # if human playing then ask for one player type, if not, ask for both
        if not (self.__is_human_playing()):
            for n in range(2):
                player_type_list.append(self.__computer_player_type(n + 1))
        else:
            player_type_list.append([0, self.user])
            player_type_list.append(self.__computer_player_type(2))
        #
        return player_type_list


    def __computer_player_type(self, player_num):
        #
        type = []
        #
        # print menu of options, get input, and append to list
        options = [ [1, "PC-Random"], [2, "PC-Reflects"], [3, "PC-Cycles"],
                    [4, "PC-Learns"]]
        print(f"\nPlease select computer player {player_num} type:")
        self.__print_options(options)
        print("(5) Surprise me!")
        type.append(self.__get_int_value(1, 5))
        #
        # if "surprise me", then reset type[0] to random value 1-4
        if type[0] == 5:
            type[0] = random.randint(1, 4)
        #
        # assign descriptions
        for n in options:
            if type[0] == n[0]:
                type.append(n[1])
        return type


    def __print_options(self, menu_list):
        #
        # menu_list in form of [[item 1, desc], [item 2, desc], etc.]
        for n in menu_list:
            print(f"({n[0]}) {n[1]}")


    def __get_int_value(self, low, high):
        # 
        while True:
            try:
                value = int(input(">>> "))
                if (value >= low and value <= high):
                    break
                else:
                    print(f"Please enter a value between {low} and {high}.")
            except:
                print("Please enter a number.")
        return value


    def __is_human_playing(self):
        #
        options = [[1, "Play against the Computer"], 
                   [2, "Have Computer play against a second Computer player"]]
        print("\nWhould you like to:")
        self.__print_options(options)
        query = self.__get_int_value(1, 2)
        if query == 1:
            return True
        else:
            return False


    def __set_game_type(self):
        #
        # declare local variables
        game_type_list = []
        game_type = self.__request_game_mode()
        # set user name and game type for this instance
        # game_type list[integer value of game type,
        #                min number of rounds for type,
        #                max number of rounds for type,
        #                human friendly description of round]
        if game_type == 1:
            game_type_list = [1, 1, 100, "Set Rounds"]
        else:
            game_type_list = [2, 3, 100, "Best of Rounds"]
        return game_type_list


    def __request_game_mode(self):
        #
        options = [ [1, "Set Rounds"], [2, "Best of Rounds"] ]
        print(f"\nWould you like to play:")
        self.__print_options(options)
        mode = self.__get_int_value(1, 2)
        return mode


    def __num_of_rounds(self):
        #
        min = self.game_type[1]
        max = self.game_type[2]
        print(f"\nPlease enter number of rounds ({min} to {max}):")
        rounds = self.__get_int_value(min, max)
        return rounds


    def __request_name(self):
        #
        # request name until user actually enters something
        while True:
            user_name = input("Please enter your name:\n>>> ")
            if user_name == "":
                print("It's much better if I know your name!")
            else:
                break
        return user_name


    def __display_intro(self):
        #
        # create white space and present title
        banner_len = 80
        welcome = "Welcome to Rock, Paper, Scissors!"
        space = " " * (int(banner_len/2) - int(len(welcome)/2))
        print("\n" * 30)
        for n in range(3):
            print("/" * banner_len)
        print(f"\n{space}{welcome}\n")
        for n in range(3):
            print("/" * banner_len)
        print("\n")
        print("Please allow me to ask a few questions to "
            "set up your game...\n")


###############################################################################
###############################################################################
###############################################################################


class Player:
    #
    # all subclasses to execute setting of name
    def __init__(self, entered_name):
        self.name = self.setName(entered_name)
    #
    def setName(self, entered_name):
        #
        # if entered_name is blank,
        # create a name from 4 to 12 characters long using random
        # ASCII characters
        name = ""
        if entered_name == "":
            for n in range(random.randint(4, 12)):
                name += chr(random.randint(97, 122))
        else:
            name = entered_name
        return name.capitalize()


class RandomPlayer(Player):
    pass


class RefelctPlayer(Player):
    pass


class CyclePlayer(Player):
    pass


class SmartPlayer(Player):
    pass


class HumanPlayer(Player):
    pass



###############################################################################
###############################################################################
###############################################################################

# main
if __name__ == '__main__':
    game = Game()
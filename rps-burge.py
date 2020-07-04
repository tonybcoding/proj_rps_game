import random


legal_moves = ["rock", "paper", "scissors"]


class Game:

    def __init__(self):
        #
        # display intro, request user's name and 
        # initialize game settings
        self.display_intro()
        self.game_settings()
        #
        # for each gamer in list, instantiate the appropriate player object
        self.player1 = self.instantiate_player(self.game_player_list[0])
        self.player2 = self.instantiate_player(self.game_player_list[1])
        #
        # play game
        self.play_game()

    def play_game(self):
        #
        print(f"\n{self.player1.name} and {self.player2.name} "
              f"have entered the ring!")
        print(f"Game starts now!\n")
        #
        # sending opponent object so current play can compare
        p1_move = ""
        p2_move = ""
        for n in range(1, 50):
            p1_move = self.player1.throw(self.player2)
            p2_move = self.player2.throw(self.player1)
            print(f"(Round {n})\t", end="")
            play_str = (f"{self.player1.name} /{p1_move}/ vs. "
                f"{self.player2.name} /{p2_move}/")
            print(play_str + " " * (50 - len(play_str)), end="")
            # persist moves of both players
            self.player1.move_list.append(p1_move)
            self.player2.move_list.append(p2_move)


            # see who wins this round
            print("--> ", end="")
            if (p1_move == p2_move):
                print("Tie")
            elif ((p1_move == "rock" and p2_move == "scissors") or
                  (p1_move == "scissors" and p2_move == "paper") or
                  (p1_move == "paper" and p2_move == "rock")):
                # persist winning move of player 1 
                self.player1.winning_move_list.append(p1_move)
                print(f"{self.player1.name} wins")
            else:
                # persist winning move of player 2
                self.player2.winning_move_list.append(p2_move)
                print(f"{self.player2.name} wins")

        print(f"Final score: {self.player1.name} - {len(self.player1.winning_move_list)}")
        print(f"Final score: {self.player2.name} - {len(self.player2.winning_move_list)}")

    def instantiate_player(self, player):
        #
        if player[0] == 0:
            new_player = HumanPlayer(player[1])
        elif player[0] == 1:
            new_player = RandomPlayer(player[1])
        elif player[0] == 2:
            new_player = ReflectPlayer(player[1])
        elif player[0] == 3:
            new_player = CyclePlayer(player[1])
        else: # must be last option
            new_player = SmartPlayer(player[1])
        #
        #print(f"Just instantiated player {type(new_player)}")
        return new_player

    def game_settings(self):
        self.user = self.request_name()
        self.game_type = self.set_game_type()
        self.game_rounds = self.num_of_rounds()
        self.game_player_list = self.set_player_types()
        print(f"\n\nOkay, we're all set, {self.user}!")
        print(f"Let's play {self.game_rounds} rounds of {self.game_type[3]}: "
              f"{self.game_player_list[0][1]} VS. "
              f"{self.game_player_list[1][1]}")
        print(f"")

    def set_player_types(self):
        #
        # declare local variables
        # player types list:
        # [[type player 1, description],[type player 2, description]
        # 0 = human, 1 - 4 for computer types
        player_type_list = []
        #
        # if human playing then ask for one player type, if not, ask for both
        if not (self.is_human_playing()):
            for n in range(2):
                player_type_list.append(self.computer_player_type(n + 1))
        else:
            player_type_list.append([0, self.user])
            player_type_list.append(self.computer_player_type(2))
        #
        return player_type_list

    def computer_player_type(self, player_num):
        #
        # print menu of options, get input, and append to list
        type = []
        options = [[1, "PC-Random"], [2, "PC-Reflects"], [3, "PC-Cycles"],
                   [4, "PC-Learns"]]
        print(f"\nPlease select computer player ## {player_num} ## type:")
        self.print_options(options)
        print("(5) Surprise me!")
        type.append(self.get_int_value(1, 5))
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

    def print_options(self, menu_list):
        #
        # menu_list in form of [[item 1, desc], [item 2, desc], etc.]
        for n in menu_list:
            print(f"({n[0]}) {n[1]}")

    def get_int_value(self, low, high):
        #
        while True:
            try:
                value = int(input(">>> "))
                if (value >= low and value <= high):
                    break
                else:
                    print(f"Please enter a value between {low} and {high}.")
            except ValueError:
                print("Please enter a number.")
        return value

    def is_human_playing(self):
        #
        options = [[1, "Play against the Computer"],
                   [2, "Have Computer play against a second Computer player"]]
        print("\nWhould you like to:")
        self.print_options(options)
        query = self.get_int_value(1, 2)
        if query == 1:
            return True
        else:
            return False

    def set_game_type(self):
        #
        # declare local variables
        game_type_list = []
        game_type = self.request_game_type()
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

    def request_game_type(self):
        #
        options = [[1, "Set Rounds"], [2, "Best of Rounds"]]
        print(f"\nWould you like to play:")
        self.print_options(options)
        mode = self.get_int_value(1, 2)
        return mode

    def num_of_rounds(self):
        #
        min = self.game_type[1]
        max = self.game_type[2]
        print(f"\nPlease enter number of rounds ({min} to {max}):")
        rounds = self.get_int_value(min, max)
        return rounds

    def request_name(self):
        #
        # request name until user actually enters something
        while True:
            user_name = input("Please enter your name:\n>>> ")
            if user_name == "":
                print("It's much better if I know your name!")
            else:
                break
        return user_name

    def display_intro(self):
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


class Player:
    #
    # all subclasses to execute setting of name
    def __init__(self, player_name):
        self.name = player_name
        self.move_list = []
        self.winning_move_list = []
    #
    # default class behavior is random selection
    def learn(self, opponent):
        return random.choice(legal_moves)
    #
    # choose next move based on sub-class specific learning
    def throw(self, opponent):
        return self.learn(opponent)


class RandomPlayer(Player):
    # use all super class methods and properties without change
    pass


class ReflectPlayer(Player):
    #
    # override superclass learn method
    def learn(self, opponent):
        #
        # for first move, choose randomly
        if (len(opponent.move_list) == 0):
            return (random.choice(legal_moves))
        #
        # thereafter, use the other player's last move
        else:
            return (opponent.move_list[-1])


class CyclePlayer(Player):
    #
    # override superclass learn method
    def learn(self, opponent):
        #
        # first move is always first entry in legal_moves list
        if (len(self.move_list) == 0):
            return legal_moves[0]
        else:
            # use mod to get remainder since and use that to index
            # legal_moves list
            return legal_moves[len(self.move_list) % len(legal_moves)]


class SmartPlayer(Player):
    #
    # override superclass learn method
    def learn(self, opponent):
        # first three moves or
        # a randomly chosen interval between 12 and 20,
        # choose randomly
        if ((len(self.move_list) <= 3) or
            (len(self.move_list) % random.randint(12, 20) == 0)):
            return (random.choice(legal_moves))
        #
        # otherwise, let's analyze winning weapons
        else:
            win_count_list = self.build_win_count_list(
                self.winning_move_list +
                opponent.winning_move_list)
            #winning_move = self.most_won_move(win_count_list)
            #return (winning_move[0])
            return self.most_won_move(win_count_list)[0]

    def build_win_count_list(self, full_win_list):
        #
        win_count_list = []
        for n in range(len(legal_moves)):
            win_count_list.append([legal_moves[n],
                full_win_list.count(legal_moves[n])])    
        return win_count_list

    def most_won_move(self, win_count_list):
        #
        winning_move = []
        winning_move = win_count_list[0]
        for n in range(1, len(win_count_list)):
            if (win_count_list[n][1] > winning_move[1]):
                winning_move = win_count_list[n]
        return winning_move


class HumanPlayer(Player):
    #
    # override superclass learn method
    def learn(self, opponent):
        #
        options = []
        print(f"{self.name}, please select your next move:")
        for n in range(len(legal_moves)):
            # n + 1 so that menu displasy 1, 2, 3, etc., instead
            # of 0, 1, 2...
            options.append([(n + 1), legal_moves[n]])
        Game.print_options(self, options)
        # this return statement first gets an integer return from users choice
        # based on first and last indeces of second item in options list
        # it then subtracts one to match the legal_moves (0, 1, 2, etc.)
        # and returns that value's string[1]
        return options[(Game.get_int_value(self, options[0][0],
                       options[-1][0])) - 1][1]
        

# main
if __name__ == '__main__':
    game = Game()

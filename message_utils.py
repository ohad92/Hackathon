from termcolor import colored, COLORS

WINNER_FG = "magenta"
G_O_FG = "yellow"
G_O_BG = "on_grey"
S_G_FG = "cyan"
S_G_FG_NAMES = "blue"
S_G_BG = "on_white"
S_S_FG = "white"
S_S_BG = "on_blue"
S_C_FG = "grey"


def game_over_message(correct_ans, group_name):
    print(colored("Game over!",G_O_FG, G_O_BG))
    print(colored("The correct answer was "+str(correct_ans)+"!",G_O_FG,G_O_BG))
    print(colored("Congratulations to the winner: ", G_O_FG,G_O_BG)+colored(group_name,WINNER_FG,G_O_BG))

def start_game_message(player1, player2, game):
    print(colored("Welcome to Quick Maths.",S_G_FG,S_G_BG))
    print(colored("Player 1: ",S_G_FG,S_G_BG)+colored(player1,S_G_FG_NAMES,S_G_BG))
    print(colored("Player 2: ",S_G_FG,S_G_BG)+colored(player1,S_G_FG_NAMES,S_G_BG))
    print(colored("==",S_G_FG,S_G_BG))
    print(colored("Please answer the following question as fast as you can:",S_G_FG,S_G_BG))
    print(colored("How much is "+game+"?",S_G_FG,S_G_BG))

def server_started(IP):
    print(colored("Server started, listening on IP address "+IP,S_S_FG, S_S_BG))

def server_closed():
    print(colored("Game over, sending out offer requests...",S_C_FG,S_S_BG))

if __name__ == '__main__':
    # server_started("127.0.0.1")
    # start_game_message("Mor","Ohad","2+2")
    # game_over_message(4,"Instinct")
    # server_closed()
    # print(COLORS)
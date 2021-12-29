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
    message = colored("Game over!",G_O_FG, G_O_BG)
    message += colored("The correct answer was "+str(correct_ans)+"!",G_O_FG,G_O_BG)
    message += colored("Congratulations to the winner: ", G_O_FG,G_O_BG)+colored(group_name,WINNER_FG,G_O_BG)
    return message

def start_game_message(player1, player2, question):
    message = colored("Welcome to Quick Maths.",S_G_FG,S_G_BG)
    message += colored("Player 1: ",S_G_FG,S_G_BG)+colored(player1,S_G_FG_NAMES,S_G_BG)
    message += colored("Player 2: ",S_G_FG,S_G_BG)+colored(player2,S_G_FG_NAMES,S_G_BG)
    message += colored("==",S_G_FG,S_G_BG)
    message += colored("Please answer the following question as fast as you can:",S_G_FG,S_G_BG)
    message += colored("How much is "+question+"?",S_G_FG,S_G_BG)
    return message

def server_started(IP):
    message = colored("Server started, listening on IP address "+IP,S_S_FG, S_S_BG)
    return message

def server_closed():
    message = colored("Game over, sending out offer requests...",S_C_FG,S_S_BG)
    return message

def client_started():
    message = colored("Client started, listening for offer requests...")
    return message
# if __name__ == '__main__':
    # server_started("127.0.0.1")
    # start_game_message("Mor","Ohad","2+2")
    # game_over_message(4,"Instinct")
    # server_closed()
    # print(COLORS)
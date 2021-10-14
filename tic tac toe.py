import itertools


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # horizontally
    for row in game:
        if all_same(row):
            print(f"player {row[0]} is the WINNER !!!!!!!! horizontally")
            return True
    # Diagonally
    diag = []
    for dia in range(len(game)):
        diag.append(game[dia][dia])
    if all_same(diag):
        print(f"player {diag[0]} is the WINNER !!!!!!!!!! diagonally (\\)")
        return True

    diag = []
    for cols, rows in enumerate(list(reversed(range(len(game))))):
        diag.append(game[cols][rows])
    if all_same(diag):
        print(f"player {diag[0]} is the WINNER !!!!!!!! diagonally (/)")
        return True

    # Vertically
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player {check[0]} is the WINNER !!!!!!!!!!! vertically")
            return True
    return False




def game_board(game_map, player=0, row=0, column=0, show_board=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied. Please try another one.")
            return game_map, False

        if not show_board:
            game[row][column] = player
        print('   0  1  2')
        for count, row in enumerate(game):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: make sure you input row/ column as 0 1 or 2 ", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False


play = True
player = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, show_board=True)
    player_choise = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choise)
        print(f"current player:{current_player}")

        played = False
        while not played:
            row_choise = int(input("What row do you want to play? (0 1 or 2):"))
            col_choise = int(input("What column do you want to play? (0 1 or 2):"))
            game, played = game_board(game, current_player, row_choise, col_choise)

        if win(game):
            game_won = True
            again = input("Do u want to play again? (y/n)  ")
            if again.lower() == "y":
                print("restarting....")
            elif again.lower() == "n":
                print(" Okay byeeeeeee")
                play = False
            else:
                print("Not a valid ans , so .... see u later alligator")
                play = False

#game = game_board(game, player=0, row=2, column=1)

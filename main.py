from tic_tac import Tic_Tac_Toe

x_size = 3
y_size = 3

player_symbols = ["O", "X"]

while True:
    game = Tic_Tac_Toe(x_size, y_size)
    game.create_board()

    game_ended = False

    while True:
        for i in range(0, 2):
            print(f"Player {i + 1}'s turn")
            print("---------------")

            game.matrix_view()

            while True:

                while True:
                    tmp_x = int(input("Enter your X-Coordinate: "))
                    if type(tmp_x) is int and 0 < tmp_x <= x_size:
                        break

                while True:
                    tmp_y = int(input("Enter your Y-Coordinate: "))
                    if type(tmp_y) is int and 0 < tmp_y <= y_size:
                        break

                if game.check_field(tmp_x, tmp_y) is False:
                    print("Field is already in use. Choose another one")
                else:
                    break

            print(f"{tmp_x} and {tmp_y}")

            game.set_element(player_symbols[i], tmp_x - 1, tmp_y - 1)

            if game.check_win(player_symbols[i]):
                print(f"Player {i + 1} wins!")
                game_ended = True
                break

            if game.check_draw(player_symbols[i]):
                print("The game is a draw!")
                game_ended = True
                break

        if game_ended:
            print("Breaked from outer loop")
            break

    while True:
        replay = input("Want to play again? [yes/no]: ")
        if replay == "yes" or replay == "no":
            break

    if replay == "yes":
        print("--------------- New Game ---------------")
        game.restart()
    elif replay == "no":
        print("Ended game")
        break

class Game:
    """
    Runs a single game of Rush-Hour.
    """

    CAR_NAMES = ['Y', 'B', 'O', 'W', 'G', 'R']
    # Yellow, Blue, Orange, White, Green, Red
    VALID_DIRECTIONS = ['u', 'd', 'l', 'r']
    # up, down, right, left
    VALID_ORIENTATIONS = [0, 1]
    MIN_CAR_LENGTH = 2
    MAX_CAR_LENGTH = 4
    USER_INPUT_MSG = "Enter car and direction in the following format:" \
                     "(CarName,DirectionLetter): "

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """
        user_input = input(self.USER_INPUT_MSG)
        if ',' in user_input and len(user_input) == 3:
            input_split = user_input.split(",")
            car_name = input_split[0]
            move = input_split[1]
            if len(car_name) == 1 and len(move) == 1:
                if car_name in self.CAR_NAMES\
                        and move in self.VALID_DIRECTIONS:
                    if self.board.move_car(car_name, move):
                        print(self.board.__str__())

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.board.__str__())
        while True:
            self.__single_turn()
            if self.board.cell_content(self.board.target_location())\
                    is not None:
                break


if __name__ == "__main__":

    import sys
    from car import Car
    from board import Board
    from helper import load_json

    board = Board()  # create a board object
    cars_config = load_json(sys.argv[1])  # load json
    for key in cars_config:
        # iterate over all cars and add only those who fit the rules of
        # game, board, and car classes.
        car_name = key
        car_length = cars_config[key][0]
        car_location = tuple(cars_config[key][1])
        car_orientation = cars_config[key][2]
        if car_name in Game.CAR_NAMES \
                and Game.MIN_CAR_LENGTH <= car_length <= Game.MAX_CAR_LENGTH \
                and car_location in board.cell_list() \
                and car_orientation in Game.VALID_ORIENTATIONS:
            # everything is valid, create a car object
            car = Car(car_name, car_length, car_location, car_orientation)
            board.add_car(car)  # add newly created car to board
    game = Game(board)  # create a game object and send board to it
    game.play()

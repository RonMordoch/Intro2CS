class Board:
    """
    This class is a board represented by 2d-list.
    Each list in a row in the board.
    Cars can move within the board limits, and cannot override each other.
    The board has a target location at a fixed coordinate.
    """
    BOARD_SIZE_CONSTANT = 7
    TARGET_LOCATION = (3, 7)
    EMPTY_CELL = '_'

    def __init__(self):
        self.size = self.BOARD_SIZE_CONSTANT
        self.board = [['_' for _ in range(self.BOARD_SIZE_CONSTANT)]
                      for _ in range(self.BOARD_SIZE_CONSTANT)]
        self.board[self.TARGET_LOCATION[0]].append(self.EMPTY_CELL)
        self.cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        for car in self.cars:
            for coordinate in car.car_coordinates():
                if coordinate in self.cell_list():
                    self.board[coordinate[0]][coordinate[1]] = car.get_name()

        board_strings = []
        for lst in self.board:
            board_strings.append(' '.join(lst))
        return "\n".join(board_strings)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        coordinates_lst = \
            [(i, j) for i in range(self.size) for j in range(self.size)]
        coordinates_lst.append(self.TARGET_LOCATION)
        return coordinates_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        for car in self.cars:
            for movekey in car.possible_moves():
                for coordinate in car.movement_requirements(movekey):
                    if coordinate in self.cell_list():
                        # target location in board
                        if self.board[coordinate[0]][coordinate[1]] \
                                == self.EMPTY_CELL:
                            # target location is empty
                                tup = (car.get_name(), movekey,
                                       car.possible_moves()[movekey])
                                moves_lst.append(tup)
        return moves_lst
        # The return value will be in the given format:
        # [('O','d',"some description"),('R','r',"some description"),
        # ('O','u',"some description")]

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.TARGET_LOCATION
        # In this board, returns (3,7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if self.board[coordinate[0]][coordinate[1]] != self.EMPTY_CELL:
            return self.board[coordinate[0]][coordinate[1]]
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for coo_tuple in car.car_coordinates():
            if coo_tuple not in self.cell_list():
                return False
            elif self.board[coo_tuple[0]][coo_tuple[1]] != self.EMPTY_CELL:
                return False
        # else, we checked all possible inhibitions to add a car:
        self.cars.append(car)
        for coordinate in car.car_coordinates():
            if coordinate in self.cell_list():
                self.board[coordinate[0]][coordinate[1]] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for car in self.cars:
            if car.get_name() == name:
                if movekey in car.possible_moves():
                    for tup in car.movement_requirements(movekey):
                        if tup in self.cell_list():
                            # target location in board
                            if self.board[tup[0]][tup[1]] == self.EMPTY_CELL:
                                # target location is empty
                                cur_location = car.car_coordinates()
                                # save pre-move coordinates
                                if car.move(movekey):
                                    for coo in cur_location:
                                        self.board[coo[0]][coo[1]]\
                                            = self.EMPTY_CELL
                                        # remove previous coordinates
                                    return True
        return False

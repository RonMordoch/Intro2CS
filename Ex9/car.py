class Car:
    """
    Create a car with a given name, length, location.
    Orientation is either vertical or horizontal. With orientation, the car
    vam move up/down or right/left respectively.
    """
    VALID_DIRECTIONS = ['u', 'd', 'l', 'r']  # up, down, right, left
    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
        location,
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        if self.orientation == self.VERTICAL:
            return [(self.location[0] + num, self.location[1])
                    for num in range(self.length)]
        if self.orientation == self.HORIZONTAL:
            return [(self.location[0], self.location[1] + num)
                    for num in range(self.length)]

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.orientation == self.VERTICAL:
            return {'u': 'cause the car to move up',
                    'd': 'cause the car to move down'}
        if self.orientation == self.HORIZONTAL:
            return {'r': 'cause the car to move right',
                    'l': 'cause the car to move left'}

    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this
         move to be legal.
        """
        if movekey == 'u':
            return [(min(self.car_coordinates())[0] - 1,
                     max([self.location])[1])]
        if movekey == 'd':
            return [(max(self.car_coordinates())[0] + 1,
                     max([self.location])[1])]
        if movekey == 'r':
            return [(min([self.location])[0],
                     max(self.car_coordinates())[1] + 1)]
        if movekey == 'l':
            return [(min([self.location])[0],
                     min(self.car_coordinates())[1] - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.VALID_DIRECTIONS:
            require = self.movement_requirements(movekey)
            if self.orientation == self.VERTICAL:
                if movekey == 'u':
                    self.location = (self.location[0] - 1, self.location[1])
                if movekey == 'd':
                    self.location = (self.location[0] + 1, self.location[1])

            if self.orientation == self.HORIZONTAL:
                if movekey == 'l':
                    self.location = (self.location[0], self.location[1] - 1)
                if movekey == 'r':
                    self.location = (self.location[0], self.location[1] + 1)
            # if successfully moved car:
            if require[0] in self.car_coordinates():
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name

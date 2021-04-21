class Asteroid:
    """
    An asteroid object, that moves in space.
    """
    SIZE_CO = 10
    NORM_CONSTANT = -5
    INITIAL_SIZE = 3

    def __init__(self, loc_x, loc_y, speed_x, speed_y):
        self.__loc_x = loc_x
        self.__loc_y = loc_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__size = self.INITIAL_SIZE
        self.__radius = self.__size * self.SIZE_CO + self.NORM_CONSTANT

    def get_location(self):
        """
        :return: tuple containing x-axis, y-axis location, respectively
        """
        return self.__loc_x, self.__loc_y

    def get_speed(self):
        """
        :return: tuple containing x-axis, y-axis speed, respectively
        """
        return self.__speed_x, self.__speed_y

    def get_radius(self):
        """
        :return: asteroid's radius
        """
        return self.__radius

    def get_size(self):
        """
        :return: return asteroid's size
        """
        return self.__size

    def set_location(self, coo_x, coo_y):
        """
        Receives a location and set asteroid location to the given one.
        :param coo_x: number representing x-axis location
        :param coo_y: number representing y-axis location
        :return: None
        """
        self.__loc_x, self.__loc_y = coo_x, coo_y

    def set_speed(self, speed_x, speed_y):
        """
        Receives new speed values and set asteroid speed to the given ones.
        :param speed_x: number representing x-axis speed
        :param speed_y: number representing y-axis speed
        :return: None
        """
        self.__speed_x, self.__speed_y = speed_x, speed_y

    def set_new_size(self, size):
        """
        Reduce current size for asteroid by 1.
        :param size: current size
        :return:
        """
        self.__size = size - 1

    def has_intersection(self, obj):
        """
        Checks if asteroid has intersection with an object, using the
        formula given in the exercise.
        :param obj: an object
        :return: True if there is intersection, else false.
        """
        x_val = (obj.get_location()[0]-self.__loc_x) ** 2
        y_val = (obj.get_location()[1] - self.__loc_y) ** 2
        distance = (x_val + y_val)**0.5
        if distance <= (self.get_radius() + obj.get_radius()):
            return True
        return False


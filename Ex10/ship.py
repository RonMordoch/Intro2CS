import math


class Ship:
    """
    A ship object that can move.
    """

    HEADING_CHANGE = 7
    SHIP_LIVES = 3
    SHIP_RADIUS = 1

    def __init__(self, loc_x, loc_y, speed_x, speed_y, heading):
        self.__loc_x = loc_x
        self.__loc_y = loc_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__heading = heading
        self.__lives = self.SHIP_LIVES
        self.__radius = self.SHIP_RADIUS

    def get_location(self):
        """
        :return: tuple containing x-axis, y-axis location, respectively
        """
        return self.__loc_x, self.__loc_y

    def get_heading(self):
        """
        :return: ship's heading in degrees
        """
        return self.__heading

    def get_heading_radians(self):
        """
        :return: ship's heading in degrees
        """
        return math.radians(self.__heading)

    def get_speed(self):
        """
        :return: tuple containing x-axis, y-axis speed, respectively
        """
        return self.__speed_x, self.__speed_y

    def get_lives(self):
        """
        :return: ship's lives
        """
        return self.__lives

    def get_radius(self):
        """
        :return: ship's radius
        """
        return self.__radius

    def set_location(self, coo_x, coo_y):
        """
        Receives a location and set torpedo location to the given one.
        :param coo_x: number representing x-axis location
        :param coo_y: number representing y-axis location
        :return: None
        """
        self.__loc_x, self.__loc_y = coo_x, coo_y

    def set_heading_left(self):
        """
        Set a new heading for the ship using the class constant.
        :return: None
        """
        self.__heading += self.HEADING_CHANGE

    def set_heading_right(self):
        """
        Set a new heading for the ship using the class constant.
        :return: None
        """
        self.__heading -= self.HEADING_CHANGE

    def set_speed(self):
        """
        Sets new values for ship's speed using the formula described
        in the exercise.
        :return: None
        """
        self.__speed_x = self.__speed_x + math.cos(
            math.radians(self.__heading))
        self.__speed_y = self.__speed_y + math.sin(
            math.radians(self.__heading))

    def set_lives(self):
        """
        Reduces ship's lives by 1.
        :return: None
        """
        self.__lives -= 1

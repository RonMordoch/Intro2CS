import math


class Torpedo:
    """
    A torpedo object, fired by the ship.
    Has location and speed in two axis, heading, radius and lifetime.
    """

    ACC_FAC = 2
    TORPEDO_RADIUS = 4
    TORPEDO_LIFETIME = 200

    def __init__(self, loc_x, loc_y, speed_x, speed_y, heading):
        self.__loc_x = loc_x
        self.__loc_y = loc_y
        self.__speed_x = speed_x + self.ACC_FAC * math.cos(
            math.radians(heading))
        self.__speed_y = speed_y + self.ACC_FAC * math.sin(
            math.radians(heading))
        self.__heading = heading
        self.__radius = self.TORPEDO_RADIUS
        self.__lifetime = self.TORPEDO_LIFETIME

    def get_speed(self):
        """
        :return: tuple containing x-axis, y-axis speed, respectively
        """
        return self.__speed_x, self.__speed_y

    def get_location(self):
        """
        :return: tuple containing x-axis, y-axis location, respectively
        """
        return self.__loc_x, self.__loc_y

    def get_radius(self):
        """
        :return: torpedo's radius
        """
        return self.__radius

    def get_lifetime(self):
        """
        :return: torpedo's lifetime
        """
        return self.__lifetime

    def set_location(self, coo_x, coo_y):
        """
        Receives a location and set torpedo location to the given one.
        :param coo_x: number representing x-axis location
        :param coo_y: number representing y-axis location
        :return: None
        """
        self.__loc_x, self.__loc_y = coo_x, coo_y

    def set_lifetime(self):
        """
        Reduce 1 from torpedo's lifetime.
        :return: None
        """
        self.__lifetime -= 1

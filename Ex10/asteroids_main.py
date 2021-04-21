from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from random import randint
import sys

DEFAULT_ASTEROIDS_NUM = 5


def generate_location():
    """
    Generates a random location for x-axis and y-axis in the range of
    screen's constant sizes.
    :return: tuple representing x-axis location, y-axis location
    """
    loc_x = randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
    loc_y = randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
    return loc_x, loc_y


class GameRunner:
    """
    A game object, manages the screen,ship,asteroid and torpedo classes all
    together to run the game until completion per the game's rules.
    """

    COL_TITLE = "COLLISION!"
    COL_MSG = "Ship was struck by an asteroid!"
    NO_ASTS_MSG = "No asteroids left to explode, you win!"
    NO_LIVES_MSG = "You ran out of lives, you lose!"
    USER_EXIT_MSG = "You pressed 'q' to exit the game."
    ENDGAME_TITLE = "Game over!"

    SHIP_SPEED_X = 0
    SHIP_SPEED_Y = 0
    SHIP_HEAD = 0
    MAX_TORPEDOS = 10
    SCORE_PER_SIZE = {1: 100, 2: 50, 3: 20}
    AST_MIN_SPEED = 1
    AST_MAX_SPEED = 4

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        self.__delta_x = self.__screen_max_x - self.__screen_min_x
        self.__delta_y = self.__screen_max_y - self.__screen_min_y

        self.__ship = Ship(generate_location()[0],
                           generate_location()[1],
                           self.SHIP_SPEED_X,
                           self.SHIP_SPEED_Y,
                           self.SHIP_HEAD)
        self.__asteroids = self.asteroids_lst(asteroids_amount)
        self.__torpedos = []
        self.__score = 0

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        Runs the game loop until one of the end-game requirements are met.
        :return: None
        """
        # first check if game is over
        self.end_game()
        # move objects
        self.move()
        # check for user input
        self.user_input()
        # check for intersections with ship or torpedos
        self.intersections_asteroids_ship()
        self.intersections_asteroids_torpedo()
        # reduce all torpedo lifetime in each round
        self.torpedo_lifetime()
        # draw objects for GUI
        self.draw_obj()

    def asteroids_lst(self, amount):
        """
        Creates a new list containing new asteroids onject and register
         them on screen.
        :param amount: number of asteroids to create.
        :return: asteroids list
        """
        asteroids_list = []
        for i in range(amount):
            # create new asteroid object
            ast = Asteroid(generate_location()[0],
                           generate_location()[1],
                           randint(self.AST_MIN_SPEED, self.AST_MAX_SPEED),
                           randint(self.AST_MIN_SPEED, self.AST_MAX_SPEED))
            asteroids_list.append(ast)
            self.__screen.register_asteroid(ast, Asteroid.get_size(ast))
        return asteroids_list

    def end_game(self):
        """
        Checks if game is over, else do nothing.
        :return: None
        """
        if self.__ship.get_lives() == 0:  # player ran out of lives
            self.__screen.show_message(self.ENDGAME_TITLE, self.NO_LIVES_MSG)
            self.__screen.end_game()
            sys.exit()
        if len(self.__asteroids) == 0:  # no more asteroids left
            self.__screen.show_message(self.ENDGAME_TITLE, self.NO_ASTS_MSG)
            self.__screen.end_game()
            sys.exit()

        if self.__screen.should_end():  # player choose to exit game
            self.__screen.show_message(self.ENDGAME_TITLE,
                                       self.USER_EXIT_MSG)
            self.__screen.end_game()
            sys.exit()

    def move(self):
        """
        Create a new list of all objects in game and move each one.
        :return: None
        """
        # a list of all objects in game - asteroids, torpedos, ship
        obj_lst = self.__asteroids + self.__torpedos + [self.__ship]
        for obj in obj_lst:
            loc_x, loc_y = obj.get_location()
            speed_x, speed_y = obj.get_speed()
            # set new location using the formula described in exercise
            new_loc_x = (speed_x + loc_x - self.__screen_min_x) \
                        % self.__delta_x + self.__screen_min_x
            new_loc_y = (speed_y + loc_y - self.__screen_min_y) \
                        % self.__delta_y + self.__screen_min_y
            # sets new location for the object
            obj.set_location(new_loc_x, new_loc_y)

    def user_input(self):
        """
        Manages user input using Screen class' API and executes function
        correspondingly.
        :return: None
        """
        if self.__screen.is_left_pressed():  # user changed heading of ship
            self.__ship.set_heading_left()
        if self.__screen.is_right_pressed():  # user changed heading of ship
            self.__ship.set_heading_right()
        if self.__screen.is_up_pressed():  # user increased ship's speed
            self.__ship.set_speed()
        if self.__screen.is_space_pressed():  # user fired torpedos
            if len(self.__torpedos) < self.MAX_TORPEDOS:
                # if amount of torpedos fired is less then maximum amount
                self.build_torpedo()
        if self.__screen.is_teleport_pressed():  # user teleport ship
            self.teleport_ship()

    def teleport_ship(self):
        """
        Sets a new random location for ship that does not intersect with
        any location occupied by asteroid.
        :return:
        """
        counter = 0
        while True:
            new_loc_x, new_loc_y = generate_location()
            for ast in self.__asteroids:
                if ast.get_location()[0] != new_loc_x:
                    if ast.get_location()[1] != new_loc_y:
                        self.__ship.set_location(new_loc_x, new_loc_y)
                        counter += 1
                        if ast.has_intersection(self.__ship):
                            counter = 0
                            break
            if counter == len(self.__asteroids):
                break

    def build_torpedo(self):
        """
        Creates a torpedo object, register to the screen and add to class'
        torpedos list.
        :return: None
        """
        loc_x = self.__ship.get_location()[0]
        loc_y = self.__ship.get_location()[1]
        speed_x = self.__ship.get_speed()[0]
        speed_y = self.__ship.get_speed()[1]
        heading = self.__ship.get_heading()

        torpedo = Torpedo(loc_x, loc_y, speed_x, speed_y, heading)
        self.__torpedos.append(torpedo)
        self.__screen.register_torpedo(torpedo)

    def torpedo_lifetime(self):
        """
        Reduce the lifetime of all torpedos.
        If lifetime is zero, unregister torpedo and remove from class' list.
        :return: None
        """
        for torpedo in self.__torpedos:
            torpedo.set_lifetime()
            if torpedo.get_lifetime() == 0:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedos.remove(torpedo)

    def draw_obj(self):
        """
        Draw the ship, all torpedos and all asteroid.
        :return:
        """
        self.__screen.draw_ship(int(self.__ship.get_location()[0]),
                                int(self.__ship.get_location()[1]),
                                self.__ship.get_heading())

        for torpedo in self.__torpedos:
            self.__screen.draw_torpedo(torpedo,
                                       int(torpedo.get_location()[0]),
                                       int(torpedo.get_location()[1]),
                                       self.__ship.get_heading_radians())
        for asteroid in self.__asteroids:
            self.__screen.draw_asteroid(asteroid,
                                        int(asteroid.get_location()[0]),
                                        int(asteroid.get_location()[1]))

    def intersections_asteroids_ship(self):
        """
        Checks if ship has intersection with any asteroid.
        :return: None
        """
        for asteroid in self.__asteroids:
            if asteroid.has_intersection(self.__ship):
                # show collision msg
                self.__screen.show_message(self.COL_TITLE, self.COL_MSG)
                # if player has 1,2, or 3 lives
                if self.__ship.get_lives() > 0:
                    self.__screen.remove_life()
                    self.__ship.set_lives()
                # unregister crashed asteroid from screen and remove from list
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)

    def intersections_asteroids_torpedo(self):
        """
        Checks if any torpedo has intersection with any asteroid.
        :return: None
        """
        for asteroid in self.__asteroids:
            for torpedo in self.__torpedos:
                if asteroid.has_intersection(torpedo):
                    # update player score
                    self.update_score(asteroid)
                    # remove torpedo
                    self.__screen.unregister_torpedo(torpedo)
                    self.__torpedos.remove(torpedo)
                    # if asteroid is size 1, remove completely
                    if asteroid.get_size() == 1:
                        self.__screen.unregister_asteroid(asteroid)
                        self.__asteroids.remove(asteroid)
                    # if asteroid is larger than one, split into 2 asteroids
                    if asteroid.get_size() > 1:
                        self.new_asts(asteroid, torpedo)

    def new_asts(self, asteroid, torpedo):
        """
        Splits the given asteroid into 2 sub-asteroids.
        :param asteroid: The asteroid that was hit
        :param torpedo: The torpedo that hit asteroid.
        :return: None
        """
        size = asteroid.get_size()
        loc_x, loc_y = asteroid.get_location()
        # calculate new speed for sub asteroids
        speed_x, speed_y = self.new_ast_speed(asteroid, torpedo)

        # create the first sub-asteroid
        asteroid_1 = Asteroid(loc_x, loc_y, speed_x, speed_y)
        asteroid_1.set_new_size(size)

        # create the second sub-asteroid, with negative speed
        # for the opposing direction
        asteroid_2 = Asteroid(loc_x, loc_y, -speed_x, -speed_y)
        asteroid_2.set_new_size(size)

        # remove old asteroid
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids.remove(asteroid)

        # add new asteroids to list and register on screen
        self.__asteroids.append(asteroid_1)
        self.__asteroids.append(asteroid_2)
        self.__screen.register_asteroid(asteroid_1, asteroid_1.get_size())
        self.__screen.register_asteroid(asteroid_2, asteroid_2.get_size())

    def new_ast_speed(self, asteroid, torpedo):
        """
        Calculate new speed for sub asteroid.
        :param asteroid: The asteroid that was hit.
        :param torpedo: The torpedo that hit asteroid.
        :return: new speed tuple of x-axis speed,y-axis speed
        """
        tor_speed_x, tor_speed_y = torpedo.get_speed()
        ast_speed_x, ast_speed_y = asteroid.get_speed()
        denominator_const = (ast_speed_x ** 2 + ast_speed_y ** 2) ** 0.5
        # use the formula described in exercise
        new_speed_x = (tor_speed_x + ast_speed_x) / denominator_const
        new_speed_y = (tor_speed_y + ast_speed_y) / denominator_const
        return new_speed_x, new_speed_y

    def update_score(self, obj):
        """
        Update player score per the size of the object.
        :param obj: asteroid that was hit
        :return: None
        """
        size = obj.get_size()
        for key in self.SCORE_PER_SIZE:
            if key == size:
                self.__score += self.SCORE_PER_SIZE[key]
        # update the new score on screen
        self.__screen.set_score(self.__score)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)

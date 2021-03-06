from World import *
import copy


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None, rule_string="B3/S23"):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        self.birth_rules = self.rule_input(rule_string)['birth']
        self.starve_rules = self.rule_input(rule_string)['starve']

        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def rule_input(self, rule_string):
        """
        Checks if input is valid, returns list of birth cases and strave cases

        :param rule_string: rule string input (default by Simulator constructor: "B3/S23")
        :return:  { "brith": [brith cases],
                    "strave": "[strave cases]",
                    }
        """
        birth = []
        starve = []

        b_index = rule_string.index("B")
        s_index = rule_string.index("S")
        birth_string = rule_string[b_index+1:s_index-1]
        starve_string = rule_string[s_index+1:]
        for birth_rule in birth_string:
            birth.append(int(birth_rule))
        for starve_rule in starve_string:
            starve.append(int(starve_rule))

        rules = {
                "birth": birth,
                "starve": starve
            }

        return rules

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        # TODO: Do something to evolve the generation
        curr_world = copy.deepcopy(self.world)
        for row in range(curr_world.width):
            for column in range(curr_world.height):
                neighbours = curr_world.get_neighbours(row, column)
                curr_cell_value = curr_world.get(row, column)
                if self.check_exposure(neighbours):
                    self.world.set(row, column, 0)
                if self.check_overcrowding(neighbours):
                    self.world.set(row, column, 0)
                if self.check_birth(neighbours, curr_cell_value):
                    self.world.set(row, column, 1)
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world



        """    --------------------- RUELS GAME OF LIFE ---------------------      """

    @staticmethod
    def check_exposure(neighbours):
        """
        If a cell has less then 2 neighbours alive, the cell will die. (exposure)

        :return True if he dies
                False if he stays alive
        """
        if sum(neighbours) < 2:
            return True
        else:
            return False

    @staticmethod
    def check_overcrowding(neighbours):
        """
        If a cell has more then 3 neighbours alive, the cell will die. (overcrowding)

        :return True if he dies
                False if he stays alive
        """
        if sum(neighbours) > 3:
            return True
        else:
            return False

    @staticmethod
    def check_birth(neighbours, cell_value):
        """
        If a dead cell has exactly 3 neighbours alive, the cell will become alive (birth).

        :return True if he becomes alive
                False if he stays dead
        """
        if cell_value == 0:
            if sum(neighbours) == 3:
                return True
            else:
                return False
        else:
            return False

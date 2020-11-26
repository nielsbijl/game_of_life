from World import *


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        # TODO: Do something to evolve the generation
        array_world = self.world.world
        for row in range(len(array_world)):
            for column in range(len(array_world[row])):
                if self.check_exposure(self.world.get_neighbours(row, column)):
                    self.world.set(row, column, 0)


        # self.world.set(2, 2, 1)
        # self.world.set(2, 1, 1)
        # self.world.set(2, 3, 1)
        # self.world.set(1, 2, 1)
        # self.world.set(3, 2, 1)
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
        If a cell has less then 2 neighbours alive, the cell will die.

        :return True if he dies
                False if he stays alive
        """
        if sum(neighbours) < 2:
            return True
        else:
            return False

from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        # Check of the simulator update function a World type returns
        self.assertIsInstance(self.sim.update(), World)

        # Check if the simulator kills underpopulated cells
        exposure_simulation = Simulator(World(5))
        exposure_simulation.world.set(2, 2, 1)
        self.assertFalse(exposure_simulation.update().world.any())  # Boolean if there is any value not 0 in array
        self.assertEqual(exposure_simulation.update().world.tolist(), World(5).world.tolist())
        self.assertEqual(exposure_simulation.update(), World(5))  # Can be used because of the _eq_ method in the World class

        # Check if the simulator kills overpopulated cells
        overcrowding_simulation = Simulator(World(5))
        overcrowding_simulation.world.set(2, 2, 1)
        overcrowding_simulation.world.set(2, 1, 1)
        overcrowding_simulation.world.set(2, 3, 1)
        overcrowding_simulation.world.set(1, 2, 1)
        overcrowding_simulation.world.set(3, 2, 1)
        expected = World(5)
        expected.set(2, 1, 0)
        expected.set(2, 1, 1)
        expected.set(2, 3, 1)
        expected.set(1, 2, 1)
        expected.set(3, 2, 1)
        self.assertEqual(overcrowding_simulation.update().get(2, 2), expected.get(2, 2))

        # Check if the simulator let the cell survive with 2 or 3 neighbours alive
        survival_simulation = Simulator(World(10))
        survival_simulation.world.set(0, 0, 1)
        survival_simulation.world.set(1, 0, 1)
        survival_simulation.world.set(0, 1, 1)
        survival_simulation.world.set(1, 1, 1)
        expected = World(10)
        expected.set(0, 0, 1)
        expected.set(0, 1, 1)
        expected.set(1, 0, 1)
        expected.set(1, 1, 1)
        self.assertEqual(survival_simulation.update(), expected)

        # Check if the simulator makes a dead cell alive if it has exactly 3 neighbours alive
        birth_simulation = Simulator(World(5))
        birth_simulation.world.set(2, 1, 1)
        birth_simulation.world.set(2, 2, 1)
        birth_simulation.world.set(2, 3, 1)
        expected = World(5)
        expected.set(1, 2, 1)
        expected.set(2, 2, 1)
        expected.set(3, 2, 1)
        self.assertEqual(birth_simulation.update(), expected)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

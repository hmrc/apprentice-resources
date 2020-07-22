import unittest
import elves


class elvesTestCase(unittest.TestCase):
    def test_01_elves_mass_calulation(self):
        output = elves.amount_of_fuel_needed([6])
        self.assertEqual(output, 0)

    def test_02_elves_mass_calulation(self):
        output = elves.amount_of_fuel_needed([10])
        self.assertEqual(output, 1)

    def test_03_elves_mass_calulation(self):
        output = elves.amount_of_fuel_needed([20])
        self.assertEqual(output, 4)

    def test_04_elves_mass_calulation_float(self):
        output = elves.amount_of_fuel_needed([20.0])
        self.assertEqual(output, 4)

    def test_05_elves_mass_calulation_str(self):
        with self.assertRaises(TypeError):
            elves.amount_of_fuel_needed("Santa")

    def test_06_elves_mass_calulation(self):
        output = elves.amount_of_fuel_needed([20.0])
        self.assertEqual(output, 4)

    def test_07_multiple_values(self):
        output = elves.amount_of_fuel_needed([20.0, 20])
        self.assertEqual(output, 8)


class IntegrationTest(unittest.TestCase):
    def test_simple_file(self):
        output = elves.fuel_calculator("elves_masses.txt")
        # self.assertEqual(output, 8)


if __name__ == "__main__":
    unittest.main()

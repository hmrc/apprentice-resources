def amount_of_fuel_needed(masses):
    total_fuel = 0
    for mass in masses:
        fuel = int(mass / 3) - 2
        total_fuel += fuel
    return total_fuel


def fuel_calculator(masses_filename):
    mass_strings = [line.rstrip("\n") for line in open(masses_filename, "r")]
    masses = []
    for i in range(len(mass_strings)):
        masses.append(int(mass_strings[i]))
    print(amount_of_fuel_needed(masses))
    return amount_of_fuel_needed(masses)

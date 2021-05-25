
from collections import namedtuple
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from gekko import GEKKO
    print("module 'gekko' is installed")
except ModuleNotFoundError:
    print("module 'gekko' is not installed, installing the package")
    install("gekko")
    from gekko import GEKKO

def parse_input(input_path = 'input.txt'):
    Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])
    ingredients = {}
    with open(input_path) as f:
        for line in f:
            words = line.split()
            ingredient, capacity, durability, flavor, texture, calories = words[0], words[2], words[4], words[6], words[8], words[10]
            ingredients[ingredient[:-1]] = Ingredient(int(capacity.strip(',')), int(durability.strip(',')), int(flavor.strip(',')), int(texture.strip(',')), int(calories.strip(',')))
    return ingredients

def solve_part1(data):
    # part 1
    prob = GEKKO() # Initialize gekko
    prob.options.SOLVER=1  # APOPT is an MINLP solver

    # Initialize variables
    Sprinkles = prob.Var(value=25,lb=0,ub=100, integer = True)
    PeanutButter = prob.Var(value=25,lb=0,ub=100, integer = True)
    Frosting = prob.Var(value=25,lb=0,ub=100, integer = True)
    Sugar = prob.Var(value=25,lb=0,ub=100, integer = True)

    # Equations
    capacity = Sprinkles * data['Sprinkles'].capacity + PeanutButter * data['PeanutButter'].capacity + \
                Frosting * data['Frosting'].capacity + Sugar * data['Sugar'].capacity
    durability = Sprinkles * data['Sprinkles'].durability + PeanutButter * data['PeanutButter'].durability + \
                Frosting * data['Frosting'].durability + Sugar * data['Sugar'].durability
    flavor = Sprinkles * data['Sprinkles'].flavor + PeanutButter * data['PeanutButter'].flavor + \
                Frosting * data['Frosting'].flavor + Sugar * data['Sugar'].flavor
    texture = Sprinkles * data['Sprinkles'].texture + PeanutButter * data['PeanutButter'].texture + \
                Frosting * data['Frosting'].texture + Sugar * data['Sugar'].texture

    prob.Equation(Sprinkles + PeanutButter + Frosting + Sugar == 100)
    prob.Equation(capacity >= 0)
    prob.Equation(durability >= 0)
    prob.Equation(flavor >= 0)
    prob.Equation(texture >= 0)

    prob.Obj(- capacity * durability * flavor * texture) # Objective
    prob.solve(disp=False) # Solve

    print('Results: ')
    print('Sprinkles: ' + str(Sprinkles.value))
    print('PeanutButter: ' + str(PeanutButter.value))
    print('Frosting: ' + str(Frosting.value))
    print('Sugar: ' + str(Sugar.value))
    print('Objective: ' + str(-prob.options.objfcnval))


def main():

    if len(sys.argv) < 2:
        data = parse_input()
    else:
        data = parse_input(sys.argv[-1])

    solve_part1(data)


if __name__ == '__main__':
    main()
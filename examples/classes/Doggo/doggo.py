class Dog:

    # tricks = [] - If we put tricks here then it is shared between all dogs

    noise = 'woof'

    def __init__(self, name):
        self.tricks = []
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

    def bark(self):
        print(self.noise)

# This means the below code is only run when we run this script directly
# i.e. Not when we import this module into another
if __name__ == "__main__":
    stanley = Dog('Stanley')
    albert = Dog('Albert')

    stanley.add_trick('sit')
    print(f'stanley knows:{stanley.tricks}') #The f means we can embed code between the {} https://www.python.org/dev/peps/pep-0498/
    albert.add_trick('play dead')
    print(f'albert knows:{albert.tricks}')

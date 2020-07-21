import doggo


class Shihtzu(doggo.Dog):

    breed = 'Shitzu'
    noise = 'wuwuwuw'

    # We can 'override' the 'bark' method so that a Shitzu behaves differently when asked to bark
    # Shihtzu will now do whatever dogs do when they bark but do it 50 times.
    def bark(self):
        for _ in range(50):
            super().bark() # super() return the parent class i.e. Dog


geoff = Shihtzu('Geoff') # Unless we override it, the __init__ method from dog is available
geoff.add_trick('yap a lot') #All the methods available on the dog class are available here
print(geoff.breed)
print(geoff.name)
print(geoff.tricks)
geoff.bark()

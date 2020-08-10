class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
ropo = Cat("Ropo", 1)
toppo = Cat("Toppo", 5)
grace = Cat("Grace", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(ropo.age, toppo.age, grace.age)} years old.")

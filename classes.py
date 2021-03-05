#practice python classes

#class & instance level variables
#class animal:
#    species = '' #something like a static variable?
#
#    def __init__(self, name) -> None:
#        self.name = name    #normal class instance variable
#
#    def __repr__(self) -> str:
#        return "{} species, animal named: {}".format(animal.species, self.name)
#
#def main():
#    
#    #main function
#    a1 = animal('david')
#    animal.species = 'human'
#    a2 = animal('daniel')
#
#    print(a1)
#    print(a2)
#
#    return None


class Animal:

    existingAnimals = 0

    def __init__(self, name) -> None:
        self.name = name
        Animal.existingAnimals+=1

    def __repr__(self) -> str:
        return "hi, i'm a {}. there are {} other animals!".format(self.name, Animal.existingAnimals-1)


def main():

    zoo = []
    zoo.append(Animal("Dog"))
    zoo.append(Animal("Cat"))
    zoo.append(Animal("Bird"))
    zoo.append(Animal("Horse"))
    zoo.append(Animal("Fish"))

    print(Animal.existingAnimals)
    
    for animal in zoo:
        print(animal)

main()
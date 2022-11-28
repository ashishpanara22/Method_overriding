class Animal(): # main class or parent class

    def leg(self): # same method use in two times
        print("most of animal has 4 legs")


class Cow(Animal): # child class of Animal

    def leg(self): # same method use in two times
        print("Cow has four legs")
        

animal = Animal() # object of Animal class
cow = Cow() # object of Cow class

animal.leg() # output of Animal class
cow.leg() # output of Cow class
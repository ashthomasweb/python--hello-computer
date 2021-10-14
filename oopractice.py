
# ALL WRONG

# class Fruit(input):

#     def __init__()
#     def color(self, color):
#         self.color = color

#     def name(self, name):
#         self.name = name

#     def shape(self, shape):
#         self.shape = shape

#     def edible(self, input):
#         self.edible = input

#     def output(self):
#         print(self.color, self.name, self.shape, self.edible)

# apple = Fruit('true')

# apple.color('red')
# apple.name('Fuji')
# apple.shape('roundish')
# apple.output()


# IFFY AT BEST

# class SectionFrame(ttk.Frame):
#     def __init__(self, name, container, width, height, relief, placex, placey):
#         super().__init__()
#         self.name = name
#         self.name = ttk.Frame(container, width= width, height= height)
#         self.name['relief'] = relief
#         self.name.place(x= placex, y= placey)
#         self.name.pack_propagate(False)
#         print(name)

# a = SectionFrame('test1', gui, 50, 100, 'groove', 20, 500)

# b = SectionFrame('test2', gui, 50, 100, 'sunken', 80, 500)

# c = SectionFrame('test3', gui, 50, 100, 'sunken', 150, 500)



class Cat():

    species = 'Felis catus'

    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.years = age
        self.weight = weight

    def found_new_species(input):
        Cat.species = input

class ApexPredator(Cat):

    def __init__(self, kind, environment, name, breed, age, weight):
        super().__init__(name, breed, age, weight)
        self.type = kind
        self.environment = environment



cat1 = Cat('Kaya', 'Sokoke', '13', '8')
cat2 = Cat('Atticus', 'Garfield', '4', '14')


print(cat1.species)
print(cat2.species)

Cat.species = 'Felis Bipedipus'

print(cat1.species)
print(cat2.species)

cat1.species = 'Felis catus'

print(cat1.species)
print(cat2.species)

print(cat1.years)

cat3 = ApexPredator('lioness', 'homestead', 'Kaya', 'Sokoke', '13', '8')

print(cat3.type)
print(cat3.name)

cat3.species = 'Queen'

print(cat3.species)
print(cat3.name)
print(cat3.type)
print(cat3.environment)
print(cat3.breed)
print(cat3.years)
print(cat3.weight)

print(cat1.species, cat2.species, cat3.species)


# proper practice would typically be to make the more general "ApexPredator" class a parent class
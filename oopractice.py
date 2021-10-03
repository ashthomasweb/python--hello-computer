

class Fruit(input):
    def color(self, color):
        self.color = color

    def name(self, name):
        self.name = name

    def shape(self, shape):
        self.shape = shape

    def edible(self, input)
        self.edible = input

    def output(self):
        print(self.color, self.name, self.shape, self.edible)

apple = Fruit('true')

apple.color('red')
apple.name('Fuji')
apple.shape('roundish')
apple.output()












class SectionFrame(ttk.Frame):
    def __init__(self, name, container, width, height, relief, placex, placey):
        super().__init__()
        self.name = name
        self.name = ttk.Frame(container, width= width, height= height)
        self.name['relief'] = relief
        self.name.place(x= placex, y= placey)
        self.name.pack_propagate(False)
        print(name)





a = SectionFrame('test1', gui, 50, 100, 'groove', 20, 500)

b = SectionFrame('test2', gui, 50, 100, 'sunken', 80, 500)

c = SectionFrame('test3', gui, 50, 100, 'sunken', 150, 500)



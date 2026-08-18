#Classes
class Greeter(object):

    #Constructor
    def __init__(self, name):
        self.name = name #create an instance variable

    #Instance method
    def greet(self, caps = False):
        if caps:
            print(f'HELLO {self.name.upper()}')
        else:
            print(f'Hello {self.name}')
g = Greeter('Jessica')
g.greet()
g.greet(caps = True)


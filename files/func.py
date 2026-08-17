# Functions is defined using def keywords
def hello(name, CAPS = False):
    if CAPS:
        print(f'HELLO {name.upper()}')
    else:
        print(f'Hello {name}')
hello('Mira')
hello('tira', CAPS = True)
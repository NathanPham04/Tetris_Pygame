class Iblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['_', 'I', '_', '_'],
                       ['_', 'I', '_', '_'],
                       ['_', 'I', '_', '_'],
                       ['_', 'I', '_', '_']]
        self.shape1 = [['_', '_', '_', '_'],
                       ['I', 'I', 'I', 'I'],
                       ['_', '_', '_', '_'],
                       ['_', '_', '_', '_']]
        self.shape2 = [['_', '_', 'I', '_'],
                       ['_', '_', 'I', '_'],
                       ['_', '_', 'I', '_'],
                       ['_', '_', 'I', '_']]
        self.shape3 = [['_', '_', '_', '_'],
                       ['_', '_', '_', '_'],
                       ['I', 'I', 'I', 'I'],
                       ['_', '_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))


class Oblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['O', 'O'],
                       ['O', 'O']]
        self.shapes = {'0': self.shape0}


    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    def get_shape(self):
        return self.shapes.get(str(self.current))

class Tblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['_', 'T', '_'],
                       ['T', 'T', '_'],
                       ['_', 'T', '_']]
        self.shape1 = [['_', '_', '_'],
                       ['T', 'T', 'T'],
                       ['_', 'T', '_']]
        self.shape2 = [['_', 'T', '_'],
                       ['_', 'T', 'T'],
                       ['_', 'T', '_']]
        self.shape3 = [['_', 'T', '_'],
                       ['T', 'T', 'T'],
                       ['_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))

class Sblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['_', 'S', '_'],
                       ['S', 'S', '_'],
                       ['S', '_', '_']]
        self.shape1 = [['_', '_', '_'],
                       ['S', 'S', '_'],
                       ['_', 'S', 'S']]
        self.shape2 = [['_', '_', 'S'],
                       ['_', 'S', 'S'],
                       ['_', 'S', '_']]
        self.shape3 = [['S', 'S', '_'],
                       ['_', 'S', 'S'],
                       ['_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))

class Zblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['Z', '_', '_'],
                       ['Z', 'Z', '_'],
                       ['_', 'Z', '_']]
        self.shape1 = [['_', '_', '_'],
                       ['_', 'Z', 'Z'],
                       ['Z', 'Z', '_']]
        self.shape2 = [['_', 'Z', '_'],
                       ['_', 'Z', 'Z'],
                       ['_', '_', 'Z']]
        self.shape3 = [['_', 'Z', 'Z'],
                       ['Z', 'Z', '_'],
                       ['_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))

class Jblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['_', 'J', '_'],
                       ['_', 'J', '_'],
                       ['J', 'J', '_']]
        self.shape1 = [['_', '_', '_'],
                       ['J', 'J', 'J'],
                       ['_', '_', 'J']]
        self.shape2 = [['_', 'J', 'J'],
                       ['_', 'J', '_'],
                       ['_', 'J', '_']]
        self.shape3 = [['J', '_', '_'],
                       ['J', 'J', 'J'],
                       ['_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))

class Lblock:
    def __init__(self):
        self.current = 0
        self.shape0 = [['L', 'L', '_'],
                       ['_', 'L', '_'],
                       ['_', 'L', '_']]
        self.shape1 = [['_', '_', '_'],
                       ['L', 'L', 'L'],
                       ['L', '_', '_']]
        self.shape2 = [['_', 'L', '_'],
                       ['_', 'L', '_'],
                       ['_', 'L', 'L']]
        self.shape3 = [['_', '_', 'L'],
                       ['L', 'L', 'L'],
                       ['_', '_', '_']]
        self.shapes = {'0': self.shape0,
                       '1': self.shape1,
                       '2': self.shape2,
                       '3': self.shape3}

    def rotate_right(self):
        self.current = (self.current + 1) % 4

    def rotate_left(self):
        self.current = (self.current - 1) % 4

    def get_shape(self):
        return self.shapes.get(str(self.current))
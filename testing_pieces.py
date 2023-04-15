from pieces import *
import unittest

def print_things(shape):
    for row in range(len(shape[0])):
        for col in range(len(shape)):
            print(shape[col][row], end = '')
        print()

class TestBlock(unittest.TestCase):
    def test_shape1(self):
        x = Lblock()
        for i in range(5):
            shape1 = x.get_shape()
            print_things(shape1)
            print()
            x.rotate_right()


if __name__ == '__main__':
    unittest.main()
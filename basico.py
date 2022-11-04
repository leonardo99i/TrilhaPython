import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3, 4))


def square(x):
    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()

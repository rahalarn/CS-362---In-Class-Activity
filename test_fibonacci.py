import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test1(self):
        self.assertIs(fibonacci.Fib(1), 1)
        self.assertIs(fibonacci.Fib(2), 1)
        self.assertIs(fibonacci.Fib(0), 0)

    def test2(self):
        self.assertIs(fibonacci.Fib(4), 3)
        self.assertIs(fibonacci.Fib(5), 5)

    def test3(self):
        self.assertIs(fibonacci.Fac(0), 1)
        self.assertIs(fibonacci.Fac(1), 1)

    def test4(self):
        self.assertIs(fibonacci.Fac(2), 2)
        self.assertIs(fibonacci.Fac(3), 6)
        self.assertIs(fibonacci.Fac(4), 24)


if __name__ == '__main__':
    unittest.main(verbosity = 2)

import unittest   
#optimizar el el codigo de numeros primos.
def is_prime(value,n =2):

    while value >= 1:
        if n >= value:
            return True
        elif value % n != 0:
            return is_prime(value, n+1)
        else:
            return False
class TestPrime(unittest.TestCase):
    
    def test_with_1(self):
        result = is_prime(1)
        self.assertTrue(result)

    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)

    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)

    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)    

    def test_with_6(self):
        result = is_prime(6)
        self.assertFalse(result)

    def test_with_7(self):
        result = is_prime(7)
        self.assertTrue(result)

    def test_with_89(self):
        result = is_prime(89)
        self.assertTrue(result)    

    def test_with_71(self):
        result = is_prime(71)
        self.assertTrue(result)    

    def test_with_120(self):
        result = is_prime(120)
        self.assertFalse(result)

    def test_with_3000(self):
        result = is_prime(3000)
        self.assertFalse(result)
    
    def test_with_5133(self):
        result = is_prime(5133)
        self.assertFalse(result)

unittest.main()
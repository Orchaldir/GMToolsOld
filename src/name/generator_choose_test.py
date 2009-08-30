import unittest


from name.generator import choose


class GeneratorChooseTest(unittest.TestCase):

    def test_choose(self):
        probabilities = {}
        probabilities['a'] = 2
        probabilities['b'] = 1
        
        self.assertEqual(choose(probabilities, 0), 'a')
        self.assertEqual(choose(probabilities, 1), 'a')
        self.assertEqual(choose(probabilities, 2), 'b')
    
    def test_invalid_number(self):
        probabilities = {}
        probabilities['a'] = 1
        
        self.assertEqual(choose(probabilities, None), None)
        self.assertEqual(choose(probabilities, -1), None)
        self.assertEqual(choose(probabilities, 1), None)
    
    def test_invalid_probabilities(self):
        self.assertEqual(choose(None, 0), None)
        self.assertEqual(choose({}, 0), None)


def get_tests():
    return unittest.makeSuite(GeneratorChooseTest, 'test')
    

import unittest


from name.generator import Generator


class GeneratorTest(unittest.TestCase):

    def test_init(self):
        consonants = {'b':1, 'c':0, 'd':2, 'f':0, 'g':3, 
            'h':0, 'j':4, 'k':0, 'l':5, 'm':0, 'n':0, 'p':0,
            'q':0, 'r':0, 's':0, 't':5, 'v':0, 'w':0, 'x':0, 
            'y':0, 'z':5}
        
        vowels = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
    
        generator = Generator(consonants, vowels, '')     
        
        self.assertEqual(generator.consonants_n, 25) 
        self.assertEqual(generator.vowels_n, 15)
    
    def test_init(self):
        consonants = {'b':1, 'c':0, 'd':2, 'f':0, 'g':3, 
            'h':0, 'j':4, 'k':0, 'l':5, 'm':0, 'n':0, 'p':0,
            'q':0, 'r':0, 's':0, 't':5, 'v':0, 'w':0, 'x':0, 
            'y':0, 'z':5}
        
        vowels = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
    
        generator = Generator(consonants, vowels, 'cvc')     
        
        name = generator.generate()
        self.assertEqual(len(name), 3) 
        self.assertTrue(name[0] in consonants)
        self.assertTrue(name[1] in vowels)
        self.assertTrue(name[2] in consonants)
        
        generator = Generator(consonants, vowels, 'vccv')     
        
        name = generator.generate()
        self.assertEqual(len(name), 4) 
        self.assertTrue(name[0] in vowels)
        self.assertTrue(name[1] in consonants)
        self.assertTrue(name[2] in consonants)
        self.assertTrue(name[3] in vowels)


def get_tests():
    return unittest.makeSuite(GeneratorTest, 'test')
    

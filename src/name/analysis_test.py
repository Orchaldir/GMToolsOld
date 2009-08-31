import unittest


from name.analysis import Analysis


class AnalysisTest(unittest.TestCase):

    def test_get_template(self):
        analysis = Analysis()
        
        self.assertEqual(analysis.get_template('aristoteles'), 'vcvccvcvcvc')
        self.assertEqual(analysis.get_template('oedipus'), 'vvcvcvc')
        self.assertEqual(analysis.get_template('socrates'), 'cvccvcvc')
        self.assertEqual(analysis.get_template('odysseus'), 'vccccvvc')
    
    def test_reduce_template(self):
        analysis = Analysis()
        
        self.assertEqual(analysis.reduce_template('cvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('ccvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvccv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvcvv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvvvvcv'), 'cvcv')
        
    def test_only_consonants(self):
        analysis = Analysis()
        
        self.assertTrue(analysis.only_consonants('bcdfghjklnmpqrstvwxyz'))
        self.assertFalse(analysis.only_consonants('bcdfghjklnmpqrstvwxyza'))
        self.assertFalse(analysis.only_consonants('bcdfghjklnmpqrstvwxyze'))
        self.assertFalse(analysis.only_consonants('bcdfghjklnmpqrstvwxyzi'))
        self.assertFalse(analysis.only_consonants('bcdfghjklnmpqrstvwxyzo'))
        self.assertFalse(analysis.only_consonants('bcdfghjklnmpqrstvwxyzu'))
    
    def test_only_vowels(self):
        analysis = Analysis()
        
        word = 'aeiou'
        
        self.assertTrue(analysis.only_vowels(word))
        
        for char in 'bcdfghjklnmpqrstvwxyz':
            self.assertFalse(analysis.only_vowels(word + char))


def get_tests():
    return unittest.makeSuite(AnalysisTest, 'test')
    

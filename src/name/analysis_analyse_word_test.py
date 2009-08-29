import unittest


from name.analysis import Analysis


class AnalysisAnalyseWordTest(unittest.TestCase):

    def test_analyse_word(self):
        analysis = Analysis()
        
        self.assertTrue(analysis.analyse_word('vbnm'))
        
        self.assertEqual(analysis.vowels_n, 0)
        self.assertEqual(analysis.vowels['a'], 0)
        self.assertEqual(analysis.vowels['e'], 0)
        self.assertEqual(analysis.vowels['i'], 0)
        self.assertEqual(analysis.vowels['o'], 0)
        self.assertEqual(analysis.vowels['u'], 0)
        
        self.assertTrue(analysis.analyse_word('aeiou'))
        
        self.assertEqual(analysis.vowels_n, 5)
        self.assertEqual(analysis.vowels['a'], 1)
        self.assertEqual(analysis.vowels['e'], 1)
        self.assertEqual(analysis.vowels['i'], 1)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 1)
        
        self.assertTrue(analysis.analyse_word('analysis'))
        
        self.assertEqual(analysis.vowels_n, 8)
        self.assertEqual(analysis.vowels['a'], 3)
        self.assertEqual(analysis.vowels['e'], 1)
        self.assertEqual(analysis.vowels['i'], 2)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 1)
        
        self.assertTrue(analysis.analyse_word('UPPERCASE'))
        
        self.assertEqual(analysis.vowels_n, 12)
        self.assertEqual(analysis.vowels['a'], 4)
        self.assertEqual(analysis.vowels['e'], 3)
        self.assertEqual(analysis.vowels['i'], 2)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 2)
    
    def test_invalid_word(self):
        analysis = Analysis()
        
        self.assertFalse(analysis.analyse_word(None))
        self.assertFalse(analysis.analyse_word('a'))
        self.assertFalse(analysis.analyse_word('ab'))
        self.assertFalse(analysis.analyse_word('ab2'))


def get_tests():
    return unittest.makeSuite(AnalysisAnalyseWordTest, 'test')
    

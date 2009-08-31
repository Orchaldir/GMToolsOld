import unittest


from name.analysis import Analysis


class AnalysisAnalyseWordTest(unittest.TestCase):

    def test_analyse_word(self):
        analysis = Analysis()
        
        self.assertTrue(analysis.analyse_word('vbnm'))
        
        self.assertEqual(analysis.consonants_n, 4)
        self.assertEqual(analysis.consonants['b'], 1)
        self.assertEqual(analysis.consonants['c'], 0)
        self.assertEqual(analysis.consonants['d'], 0)
        self.assertEqual(analysis.consonants['f'], 0)
        self.assertEqual(analysis.consonants['g'], 0)
        self.assertEqual(analysis.consonants['h'], 0)
        self.assertEqual(analysis.consonants['j'], 0)
        self.assertEqual(analysis.consonants['k'], 0)
        self.assertEqual(analysis.consonants['l'], 0)
        self.assertEqual(analysis.consonants['m'], 1)
        self.assertEqual(analysis.consonants['n'], 1)
        self.assertEqual(analysis.consonants['p'], 0)
        self.assertEqual(analysis.consonants['q'], 0)
        self.assertEqual(analysis.consonants['r'], 0)
        self.assertEqual(analysis.consonants['s'], 0)
        self.assertEqual(analysis.consonants['t'], 0)
        self.assertEqual(analysis.consonants['v'], 1)
        self.assertEqual(analysis.consonants['w'], 0)
        self.assertEqual(analysis.consonants['x'], 0)
        self.assertEqual(analysis.consonants['y'], 0)
        self.assertEqual(analysis.consonants['z'], 0)
        
        self.assertEqual(analysis.vowels_n, 0)
        self.assertEqual(analysis.vowels['a'], 0)
        self.assertEqual(analysis.vowels['e'], 0)
        self.assertEqual(analysis.vowels['i'], 0)
        self.assertEqual(analysis.vowels['o'], 0)
        self.assertEqual(analysis.vowels['u'], 0)
        
        self.assertEqual(len(analysis.start), 1)
        self.assertEqual(analysis.number, 1)
        self.assertEqual(analysis.start['v'], 1)
        
        self.assertTrue(analysis.analyse_word('aeiou'))
        
        self.assertEqual(analysis.consonants_n, 4)
        self.assertEqual(analysis.consonants['b'], 1)
        self.assertEqual(analysis.consonants['c'], 0)
        self.assertEqual(analysis.consonants['d'], 0)
        self.assertEqual(analysis.consonants['f'], 0)
        self.assertEqual(analysis.consonants['g'], 0)
        self.assertEqual(analysis.consonants['h'], 0)
        self.assertEqual(analysis.consonants['j'], 0)
        self.assertEqual(analysis.consonants['k'], 0)
        self.assertEqual(analysis.consonants['l'], 0)
        self.assertEqual(analysis.consonants['m'], 1)
        self.assertEqual(analysis.consonants['n'], 1)
        self.assertEqual(analysis.consonants['p'], 0)
        self.assertEqual(analysis.consonants['q'], 0)
        self.assertEqual(analysis.consonants['r'], 0)
        self.assertEqual(analysis.consonants['s'], 0)
        self.assertEqual(analysis.consonants['t'], 0)
        self.assertEqual(analysis.consonants['v'], 1)
        self.assertEqual(analysis.consonants['w'], 0)
        self.assertEqual(analysis.consonants['x'], 0)
        self.assertEqual(analysis.consonants['y'], 0)
        self.assertEqual(analysis.consonants['z'], 0)
        
        self.assertEqual(analysis.vowels_n, 5)
        self.assertEqual(analysis.vowels['a'], 1)
        self.assertEqual(analysis.vowels['e'], 1)
        self.assertEqual(analysis.vowels['i'], 1)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 1)
        
        self.assertEqual(len(analysis.start), 2)
        self.assertEqual(analysis.number, 2)
        self.assertEqual(analysis.start['a'], 1)
        self.assertEqual(analysis.start['v'], 1)
        
        self.assertTrue(analysis.analyse_word('analysis'))
        
        self.assertEqual(analysis.consonants_n, 9)
        self.assertEqual(analysis.consonants['b'], 1)
        self.assertEqual(analysis.consonants['c'], 0)
        self.assertEqual(analysis.consonants['d'], 0)
        self.assertEqual(analysis.consonants['f'], 0)
        self.assertEqual(analysis.consonants['g'], 0)
        self.assertEqual(analysis.consonants['h'], 0)
        self.assertEqual(analysis.consonants['j'], 0)
        self.assertEqual(analysis.consonants['k'], 0)
        self.assertEqual(analysis.consonants['l'], 1)
        self.assertEqual(analysis.consonants['m'], 1)
        self.assertEqual(analysis.consonants['n'], 2)
        self.assertEqual(analysis.consonants['p'], 0)
        self.assertEqual(analysis.consonants['q'], 0)
        self.assertEqual(analysis.consonants['r'], 0)
        self.assertEqual(analysis.consonants['s'], 2)
        self.assertEqual(analysis.consonants['t'], 0)
        self.assertEqual(analysis.consonants['v'], 1)
        self.assertEqual(analysis.consonants['w'], 0)
        self.assertEqual(analysis.consonants['x'], 0)
        self.assertEqual(analysis.consonants['y'], 1)
        self.assertEqual(analysis.consonants['z'], 0)
        
        self.assertEqual(analysis.vowels_n, 8)
        self.assertEqual(analysis.vowels['a'], 3)
        self.assertEqual(analysis.vowels['e'], 1)
        self.assertEqual(analysis.vowels['i'], 2)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 1)
        
        self.assertEqual(len(analysis.start), 2)
        self.assertEqual(analysis.number, 3)
        self.assertEqual(analysis.start['a'], 2)
        self.assertEqual(analysis.start['v'], 1)
        
        self.assertTrue(analysis.analyse_word('UPPERCASE'))
        
        self.assertEqual(analysis.consonants_n, 14)
        self.assertEqual(analysis.consonants['b'], 1)
        self.assertEqual(analysis.consonants['c'], 1)
        self.assertEqual(analysis.consonants['d'], 0)
        self.assertEqual(analysis.consonants['f'], 0)
        self.assertEqual(analysis.consonants['g'], 0)
        self.assertEqual(analysis.consonants['h'], 0)
        self.assertEqual(analysis.consonants['j'], 0)
        self.assertEqual(analysis.consonants['k'], 0)
        self.assertEqual(analysis.consonants['l'], 1)
        self.assertEqual(analysis.consonants['m'], 1)
        self.assertEqual(analysis.consonants['n'], 2)
        self.assertEqual(analysis.consonants['p'], 2)
        self.assertEqual(analysis.consonants['q'], 0)
        self.assertEqual(analysis.consonants['r'], 1)
        self.assertEqual(analysis.consonants['s'], 3)
        self.assertEqual(analysis.consonants['t'], 0)
        self.assertEqual(analysis.consonants['v'], 1)
        self.assertEqual(analysis.consonants['w'], 0)
        self.assertEqual(analysis.consonants['x'], 0)
        self.assertEqual(analysis.consonants['y'], 1)
        self.assertEqual(analysis.consonants['z'], 0)
        
        self.assertEqual(analysis.vowels_n, 12)
        self.assertEqual(analysis.vowels['a'], 4)
        self.assertEqual(analysis.vowels['e'], 3)
        self.assertEqual(analysis.vowels['i'], 2)
        self.assertEqual(analysis.vowels['o'], 1)
        self.assertEqual(analysis.vowels['u'], 2)
        
        self.assertEqual(len(analysis.start), 3)
        self.assertEqual(analysis.number, 4)
        self.assertEqual(analysis.start['a'], 2)
        self.assertEqual(analysis.start['u'], 1)
        self.assertEqual(analysis.start['v'], 1)
        
        self.assertTrue(analysis.analyse_word('group'))
        
        self.assertEqual(analysis.groups['ou'], 2)
        
        self.assertTrue(analysis.analyse_word('great'))
        
        self.assertEqual(analysis.c_combs['gr'], 2)
    
    def test_invalid_word(self):
        analysis = Analysis()
        
        self.assertFalse(analysis.analyse_word(None))
        self.assertFalse(analysis.analyse_word('a'))
        self.assertFalse(analysis.analyse_word('ab'))
        self.assertFalse(analysis.analyse_word('ab2'))


def get_tests():
    return unittest.makeSuite(AnalysisAnalyseWordTest, 'test')
    

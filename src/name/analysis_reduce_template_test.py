import unittest


from name.analysis import Analysis


class AnalysisReduceTemplateTest(unittest.TestCase):

    def test_reduce_template(self):
        analysis = Analysis()
        
        self.assertEqual(analysis.reduce_template('cvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('ccvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvvcv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvccv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvcvv'), 'cvcv')
        self.assertEqual(analysis.reduce_template('cvvvvcv'), 'cvcv')


def get_tests():
    return unittest.makeSuite(AnalysisReduceTemplateTest, 'test')
    

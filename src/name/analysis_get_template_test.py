import unittest


from name.analysis import Analysis


class AnalysisGetTemplateTest(unittest.TestCase):

    def test_get_template(self):
        analysis = Analysis()
        
        self.assertEqual(analysis.get_template('aristoteles'), 'vcvccvcvcvc')
        self.assertEqual(analysis.get_template('oedipus'), 'vvcvcvc')
        self.assertEqual(analysis.get_template('socrates'), 'cvccvcvc')
        self.assertEqual(analysis.get_template('odysseus'), 'vccccvvc')


def get_tests():
    return unittest.makeSuite(AnalysisGetTemplateTest, 'test')
    

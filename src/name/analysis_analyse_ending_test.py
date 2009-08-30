import unittest


from name.analysis import Analysis


class AnalysisAnalyseEndingTest(unittest.TestCase):

    def test_analyse_word(self):
        analysis = Analysis()
        
        analysis.analyse_ending('Aristoteles')
        analysis.analyse_ending('Heracles')
        analysis.analyse_ending('Oedipus')
        analysis.analyse_ending('Socrates')
        analysis.analyse_ending('Odysseus')
        
        self.assertEqual(analysis.endings['es'], 3)
        self.assertEqual(analysis.endings['les'], 2)
        self.assertEqual(analysis.endings['tes'], 1)
        self.assertEqual(analysis.endings['us'], 2)
        self.assertEqual(analysis.endings['pus'], 1)
        self.assertEqual(analysis.endings['eus'], 1)


def get_tests():
    return unittest.makeSuite(AnalysisAnalyseEndingTest, 'test')
    

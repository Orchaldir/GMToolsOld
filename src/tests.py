import unittest


import name.analysis_analyse_word_test


if __name__ == "__main__":
    suites = []

    suites.extend(name.analysis_analyse_word_test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  

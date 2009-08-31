import unittest


import name.analysis_analyse_ending_test
import name.analysis_analyse_word_test
import name.analysis_test
import name.generator_test
import name.template_test
import name.template_choose_test


if __name__ == "__main__":
    suites = []

    suites.extend(name.analysis_analyse_ending_test.get_tests())
    suites.extend(name.analysis_analyse_word_test.get_tests())
    suites.extend(name.analysis_test.get_tests())
    suites.extend(name.generator_test.get_tests())    
    suites.extend(name.template_test.get_tests())
    suites.extend(name.template_choose_test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  

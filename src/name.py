from name.analysis import Analysis


if __name__ == "__main__":
    analysis = Analysis()
    
    analysis.analyse_file('../data/greek_m.txt')
    
    print 'Vowels: count=%d' % (analysis.vowels_n)
    print '  a=%d' % (analysis.vowels['a'])
    print '  e=%d' % (analysis.vowels['e'])
    print '  i=%d' % (analysis.vowels['i'])
    print '  o=%d' % (analysis.vowels['o'])
    print '  u=%d' % (analysis.vowels['u'])

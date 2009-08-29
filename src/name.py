from name.analysis import Analysis


if __name__ == "__main__":
    analysis = Analysis()
    
    analysis.analyse_file('../data/greek_m.txt')
    analysis.calculate()
    
    print 'Vowels: count=%d' % (analysis.vowels_n)
    for char, n in analysis.vowels.iteritems():
        print '  %s=%d' % (char, n)
        
    print '\nConsonants: count=%d' % (analysis.consonants_n)
    for char, n in analysis.consonants.iteritems():
        print '  %s=%d' % (char, n)
    
    print '\nStart: count=%d' % (analysis.start_n)
    for char, n in analysis.start.iteritems():
        print '  %s=%d' % (char, n)
    
    print '\nGroups: max=%d avg=%d' % (analysis.groups_max, analysis.groups_avg)
    for char, n in analysis.groups.iteritems():
        print '  %s=%d' % (char, n)

from name.analysis import Analysis


if __name__ == "__main__":
    analysis = Analysis()
    
    filename = 'greek_m'
    
    analysis.analyse_file('../data/' + filename + '.txt')
    analysis.calculate()
    
    print 'Vowels: count=%d' % (analysis.vowels_n)        
    print 'Consonants: count=%d' % (analysis.consonants_n)       
    print 'Endings: max=%d avg=%d' % (analysis.endings_max, analysis.endings_avg)    
    print 'Groups: max=%d avg=%d' % (analysis.groups_max, analysis.groups_avg)
    
    analysis.save('../data/analysis/' + filename + '.txt')

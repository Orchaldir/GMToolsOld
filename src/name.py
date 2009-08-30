from name.analysis import Analysis
from name.generator import Generator
from name.template import Template


if __name__ == "__main__":
    analysis = Analysis()
    
    filename = 'greek_m'
    
    analysis.analyse_file('../data/' + filename + '.txt')
    analysis.calculate()
    
    print 'Vowels: count=%d' % (analysis.vowels_n)        
    print 'Consonants: count=%d' % (analysis.consonants_n)       
    print 'Endings: max=%d avg=%d' % (analysis.endings_max, analysis.endings_avg)    
    print 'Groups: max=%d avg=%d' % (analysis.groups_max, analysis.groups_avg)
    print 'Templates: max=%d avg=%d' % (analysis.templates_max, analysis.templates_avg)
    print 'Reduced Templates: max=%d avg=%d' % (analysis.reduced_templates_max, analysis.reduced_templates_avg)
    
    analysis.save('../data/analysis/' + filename + '.txt')
    
    generator = Generator(analysis.consonants, analysis.vowels)
    template = Template('<cvc|cvcvc|vcvc|vcvcvc>(es|on|os|us|as)') 
    
    for i in range(10):
        print generator.generate(template)

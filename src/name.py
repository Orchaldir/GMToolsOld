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
    
    c_combs = {'th':21, 'st':17, 'ph':16, 'ch':11}
    v_combs = {'eu':48, 'io':32, 'ia':28, 'oo':26, 'ai':26, 'ae':26, 'oe':25, 
        'ei':25, 'eo':24, 'iu':23, 'au':22, 'ao':22}
    
    generator = Generator(analysis.consonants, analysis.vowels, c_combs, v_combs)
    template = Template('<CVC|CVCVC|VCVC|VCVCVC>(es|on|os|us|as)') 
    
    for i in range(10):
        print generator.generate(template)

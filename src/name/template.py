import random  


def choose(probabilities, number):
    if not probabilities or number is None or number < 0:
        return None

    i = 0
    
    for char, n in probabilities.iteritems():
        i += n
        if number < i:
            return char
    
    return None


def choose_random(probabilities, length):
    return choose(probabilities, random.randint(0, length-1))
    
    
class OrSymbol:

    def __init__(self, templates):
        self.templates = templates
     
    def generate(self, generator):
        return random.choice(self.templates).generate(generator)

class OrText:

    def __init__(self, templates):
        self.templates = templates
     
    def generate(self, generator):
        return random.choice(self.templates)
    

class Template:

    def __init__(self, template):
        self.template = []  
        
        or_symbol = False
        or_text = False  
        part = ''
        list_of_parts = [] 
        
        for char in template:
            if char is 'c' or char is 'v' or char is 'C' or char is 'V':
                if or_symbol or or_text:
                    part += char
                else:
                    self.template.append(char)
            elif char is '<':
                if or_text:
                    raise NameError('Error: \'<\' in OrText!') 
                else:
                    or_symbol = True
            elif char is '(':
                if or_symbol:
                    raise NameError('Error: \'(\' in OrSymbol!') 
                else:
                    or_text = True
            elif char is '>':
                if or_symbol:
                    or_symbol = False                    
                    list_of_parts.append(part)
                    templates = []
                    
                    for p in list_of_parts:
                        new = Template(p)
                        templates.append(new)
                    
                    self.template.append(OrSymbol(templates))
                    
                    list_of_parts = []
                    templates = []
                    part = ''
                else:
                    raise NameError('Error with \'>\'!') 
            elif char is ')':
                if or_text:
                    or_text = False                    
                    list_of_parts.append(part)
                    
                    self.template.append(OrText(list_of_parts))
                    
                    part = ''
                else:
                    raise NameError('Error with \')\'!') 
            elif char is '|':
                if or_symbol or or_text:
                    list_of_parts.append(part)
                    part = ''
                else:
                    raise NameError('Error with \'|\'!') 
            elif or_text:
                part += char
                
                
     
    def generate(self, generator):
        name = ''
        
        for e in self.template:
            if e is 'c':
                name += choose_random(generator.consonants, generator.consonants_n)
            elif e is 'v':
                name += choose_random(generator.vowels, generator.vowels_n)
            elif e is 'C':
                name += choose_random(generator.c_combs, generator.c_combs_n)
            elif e is 'V':
                name += choose_random(generator.v_combs, generator.v_combs_n)
            else:
                name += e.generate(generator)
        
        return name

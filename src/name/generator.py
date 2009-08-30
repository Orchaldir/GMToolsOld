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
    

class Generator:

    def __init__(self, consonants, vowels, template):
        self.consonants = consonants
        self.consonants_n = 0
        
        for i in consonants.values():
            self.consonants_n += i
        
        self.vowels = vowels
        self.vowels_n = 0
        
        for i in vowels.values():
            self.vowels_n += i
        
        self.template = template

    def generate(self):
        name = ''
        
        for char in self.template:
            if char is 'c':
                name += choose_random(self.consonants, self.consonants_n)
            elif char is 'v':
                name += choose_random(self.vowels, self.vowels_n)
        
        return name

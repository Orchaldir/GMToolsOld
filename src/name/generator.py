

class Generator:

    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.consonants_n = 0
        
        for i in consonants.values():
            self.consonants_n += i
        
        self.vowels = vowels
        self.vowels_n = 0
        
        for i in vowels.values():
            self.vowels_n += i

    def generate(self, template):
        return template.generate(self)

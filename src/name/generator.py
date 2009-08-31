

class Generator:

    def __init__(self, consonants, vowels, c_combs={}, v_combs={}):
        self.consonants = consonants
        self.consonants_n = 0
        
        for i in self.consonants.values():
            self.consonants_n += i
        
        self.vowels = vowels
        self.vowels_n = 0
        
        for i in self.vowels.values():
            self.vowels_n += i
        
        self.c_combs = c_combs.copy()
        self.c_combs.update(self.consonants)
        self.c_combs_n = 0
        
        for i in self.c_combs.values():
            self.c_combs_n += i
        
        self.v_combs = v_combs.copy()
        self.v_combs.update(self.vowels)
        self.v_combs_n = 0
        
        for i in self.v_combs.values():
            self.v_combs_n += i

    def generate(self, template):
        return template.generate(self)

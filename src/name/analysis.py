

class Analysis:

    def __init__(self):
        self.min = 3
        self.consonants = {'b':0, 'c':0, 'd':0, 'f':0, 'g':0, 
            'h':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'p':0,
            'q':0, 'r':0, 's':0, 't':0, 'v':0, 'w':0, 'x':0, 
            'y':0, 'z':0}
        self.consonants_n = 0
        self.vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        self.vowels_n = 0
        self.start = {}
        self.start_n = 0
    
    def analyse_word(self, word):
        if not word or len(word) < self.min:
            return False
        
        if not word.isalpha():
            return False
        
        lower = word.strip().lower()
        
        if lower[0] in self.start:
            self.start[lower[0]] += 1
        else:
            self.start[lower[0]] = 1
        
        self.start_n += 1
            
        for char in lower:
            if char in self.vowels:
                self.vowels[char] += 1
                self.vowels_n += 1
            elif char in self.consonants:
                self.consonants[char] += 1
                self.consonants_n += 1
    
        return True

    def analyse_file(self, filename):
        f = open(filename, "r")
        
        for word in f:
            self.analyse_word(word[:-1])
        
        f.close()        

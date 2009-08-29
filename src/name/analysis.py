

class Analysis:

    def __init__(self):
        self.min = 3
        self.vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        self.vowels_n = 0
    
    def analyse_word(self, word):
        if not word or len(word) < self.min:
            return False
        
        if not word.isalpha():
            return False
        
        lower = word.strip().lower()
            
        for char in lower:
            if char in self.vowels:
                self.vowels[char] += 1
                self.vowels_n += 1
    
        return True

    def analyse_file(self, filename):
        f = open(filename, "r")
        
        for word in f:
            self.analyse_word(word[:-1])
        
        f.close()        

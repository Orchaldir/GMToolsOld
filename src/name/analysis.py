

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
        
        self.number = 0
        
        self.groups = {}
        self.groups_max = 0
        self.groups_avg = 0
        self.max_group_length = 4
        
        self.endings = {}
        self.endings_max = 0
        self.endings_avg = 0
        self.max_ending_length = 3
    
    def analyse_ending(self, word):
        length = len(word)
        
        for l in range(1,self.max_ending_length):
            if l <= length:
                end = word[length-(1+l):]
                
                self.endings[end] = self.endings.get(end, 0) + 1
    
    def analyse_groups(self, word):
        length = len(word)
        
        for pos in range(length):
            for l in range(1,self.max_group_length):
                if pos + l < length:
                    group = word[pos:pos+l+1]
                    
                    self.groups[group] = self.groups.get(group, 0) + 1
    
    def analyse_word(self, word):
        if not word or len(word) < self.min:
            return False
        
        if not word.isalpha():
            return False
        
        lower = word.strip().lower()
        
        self.start[lower[0]] = self.start.get(lower[0], 0) + 1
        
        self.number += 1
            
        for char in lower:
            if char in self.vowels:
                self.vowels[char] += 1
                self.vowels_n += 1
            elif char in self.consonants:
                self.consonants[char] += 1
                self.consonants_n += 1
        
        self.analyse_ending(lower)
        self.analyse_groups(lower)
    
        return True

    def analyse_file(self, filename):
        f = open(filename, "r")
        
        for word in f:
            self.analyse_word(word[:-1])
        
        f.close()      
    
    def calculate_dict(self, probabilities):    
        n = 1
        p_avg = 1
        p_max = 0
        
        for i in probabilities.values():
            if i > 1:
                p_avg += i
                n += 1
            if i > p_max:
                p_max = i
        
        p_avg = int(p_avg / n)
        
        p_min = p_avg
        to_remove = []
        
        for e, n in probabilities.iteritems():  
            if n < p_min:
                to_remove.append(e)
        
        for e in to_remove:
            del probabilities[e]
        
        return p_max, p_avg
    
    def calculate(self):
        self.endings_max, self.endings_avg = self.calculate_dict(self.endings)
        self.groups_max, self.groups_avg = self.calculate_dict(self.groups)
    
    def save(self, filename):
        f = open(filename, "w")
        
        f.write('Vowels: count=%d\n' % (self.vowels_n))
        for char, n in self.vowels.iteritems():
            f.write('  %s=%d\n' % (char, n))
            
        f.write('\nConsonants: count=%d\n' % (self.consonants_n))
        for char, n in self.consonants.iteritems():
            f.write('  %s=%d\n' % (char, n))
        
        f.write('\nStart:\n')
        for char, n in self.start.iteritems():
            f.write('  %s=%d\n' % (char, n))
        
        f.write('\nEndings: max=%d avg=%d\n' % (self.endings_max, self.endings_avg))
        for char, n in self.endings.iteritems():
            f.write('  %s=%d\n' % (char, n))
        
        f.write('\nGroups: max=%d avg=%d\n' % (self.groups_max, self.groups_avg))
        for char, n in self.groups.iteritems():
            f.write('  %s=%d\n' % (char, n))
        
        f.close()        

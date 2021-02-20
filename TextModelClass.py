#
# finalproject.py (Final Project)
#
# Building a text model  
#

from Helper_Functions import clean_text, generate_sens, stem, compare_dictionaries    

# Classes    
class TextModel:
    def __init__(self, model_name):
        """ constructs a new TextModel object by accepting a string model_name as a parameter
            initializes three attributes: name, words, word_lengths
        """
        self.name = model_name # a string that is a label of this text model (i.e. 'JKRowling'), used for saving and retrieving the model
        self.words = {} # a dictionary records the number of times each word appears in the text 
        self.word_lengths = {} # a dictionary that records the number of times each word length appears
        self.stems = {} # a dictionary that records the number of times each word stem appears in the text
        self.sentence_lengths = {} #  a dictionary that records the number of times each sentence length appears
        self.par_lengths = {} # a dictionary that records the number of times each paragraph length (i.e., the number of sentences in a paragraph) appears
        
    
    def __repr__(self):
        """ returns a string that includes the name of the model as well as the sizes of the dictionaries for each feature of the text
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of paragraph lengths: ' + str(len(self.par_lengths))
        return s
    
    
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces
            to all of the dictionaries in this text model
        """
        word_list = clean_text(s) 
        
        for word in word_list:
            # Add information to self.words
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1
            
            # Add information to self.word_lengths
            if len(word) not in self.word_lengths:
                self.word_lengths[len(word)] = 1
            else:
                self.word_lengths[len(word)] += 1
            
            # Add information to self.stems 
            stem_word = stem(word)
            if stem_word not in self.stems:
                self.stems[stem_word] = 1
            else:
                self.stems[stem_word] += 1
                
        # Add information to self.sentence_lengths and self.par_lengths        
        sentences = generate_sens(s) # generate the list of list of sentences of s
        for par in sentences:
            len_par = 0
            for sen in par:
                len_par += 1
                len_sen = len(sen.split())
                if len_sen in self.sentence_lengths:
                    self.sentence_lengths[len_sen] += 1
                else:
                    self.sentence_lengths[len_sen] = 1
            
            if len_par != 0:
                if len_par in self.par_lengths:
                    self.par_lengths[len_par] += 1
                else:
                    self.par_lengths[len_par] = 1
                
    
    def add_file(self, filename):
        """ input: filename is a string representing the name of the file 
            adds all of the text in the file to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = f.read()
        f.close()
        
        self.add_string(txt)
        
    
    def save_model(self):
        """ saves the TextModel object by writing its various feature dictionaries to files
        """
        
        f = open(self.name + '_words.txt', 'w')
        f.write(str(self.words))
        f.close()
        
        f = open(self.name + '_word_lengths.txt', 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        f = open(self.name + '_stems.txt', 'w')
        f.write(str(self.stems))
        f.close()
        
        f = open(self.name + '_sentence_lengths.txt', 'w')
        f.write(str(self.sentence_lengths))
        f.close()
        
        f = open(self.name + '_par_lengths.txt', 'w')
        f.write(str(self.par_lengths))
        f.close()
        
    
    def read_model(self):
        """ reads the stored dictionaries from the files and assigns them to the attributes of the called TextModel object
        """
        f = open(self.name + '_words.txt', 'r')
        s_words = f.read()
        f.close()
        
        f = open(self.name + '_word_lengths.txt', 'r')
        s_word_lengths = f.read()
        f.close()
        
        f = open(self.name + '_stems.txt', 'r')
        s_stems = f.read()
        f.close()
        
        f = open(self.name + '_sentence_lengths.txt', 'r')
        s_sentence_lengths = f.read()
        f.close()
        
        f = open(self.name + '_par_lengths.txt', 'r')
        s_par_lengths = f.read()
        f.close()
        
        self.words = dict(eval(s_words))
        self.word_lengths = dict(eval(s_word_lengths))
        self.stems = dict(eval(s_stems))
        self.sentence_lengths = dict(eval(s_sentence_lengths))
        self.par_lengths = dict(eval(s_par_lengths))
        
        
    def similarity_scores(self, other):
        """ input: other is another TextModel object
            return a list of log similarity scores measuring the similarity of self and other
        """
        word_score = compare_dictionaries(other.words, self.words)
        result = [word_score]
        
        word_len_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        result += [word_len_score]
        
        stems_score = compare_dictionaries(other.stems, self.stems)
        result += [stems_score]
        
        sen_len_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        result += [sen_len_score]
        
        par_len_score = compare_dictionaries(other.par_lengths, self.par_lengths)
        result += [par_len_score]
        
        return result 
            
        
    def classify(self, source1, source2):
        """ input: source1, source2 are two TextModel objects
            determines which of these other TextModels is the more likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print('scores for ' + source1.name + ':', [round(x, 3) for x in scores1])
        print('scores for ' + source2.name + ':', [round(x, 3) for x in scores2])
        
        weighted_sum1 = 8 * scores1[0] + 5 * scores1[1] + 10 * scores1[2] + 3 * scores1[3] + scores1[4]
        weighted_sum2 = 8 * scores2[0] + 5 * scores2[1] + 10 * scores2[2] + 3 * scores2[3] + scores2[4]
        
        if weighted_sum1 > weighted_sum2:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)
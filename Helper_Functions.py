# Helper functions for the TextModel class
import math

def clean_text(txt):
    """ input: txt is a string of text
        returns a list containing the words in text after it has been "cleaned"
        allows to work with words without worrying about puctuations or special charaters
    """
    result = txt.lower()
    for c in '.,?!;:"':
        result = result.replace(c, '')
        
    return result.split()


def generate_sens(txt):
    """ input: txt is a string of text
        returns a list of lists in which each sublist is a list of strings
        the number of sublists (length of the list) is the number of paragraphs of txt
        the length of each sublist is the number of sentences in the corresponding paragraph of txt 
    """   
    pars = txt.splitlines() # generate a list of paragraphs of txt
    sentences = [] 
    s = ''
    
    for i in range(len(pars)):
        word_list = pars[i].split() # generate a list of all the words of a paragraph
        sentences += [[]]
        for j in range(len(word_list)): # for each word in word_list 
            if word_list[j][-1] in '.?!' or j == len(word_list) - 1: # if the word has an ending-punctuation or it is the last word in the paragraph
                s += word_list[j] 
                sentences[i] += [s] # store the sentence into the i_th list of the "superlist" sentences   
                s = ''
            else:
                s += word_list[j]  
                s += ' '
    return sentences  
                

def has_vowel(s):
    """ input: a string s
        return True if s has at least a vowel, and False otherwise
    """
    vowels = 'aeiou'
    for c in vowels:
        if c in s:
            return True
    return False


def stem(s):
    """ input: s is a string
        return the stem of the word s 
    """
    if len(s) > 0:
        if s[-2:] == 'ee':
            return s
        elif s[-1] == 'e':
            return s[:-1]
        if s[-2:] == 'es':
            s_new = stem(s[:-2])
            return s_new
        elif s[-1:] == 's':
            s_new = stem(s[:-1])
            return s_new
        elif s[-2:] == 'er':
            if len(s) > 3:
                if s[-3] == 'e': # i.e. career
                    return s # return career
                elif s[-3] == s[-4]: 
                    if s[-3] in 'aiou': # in case of shampooer, etc.
                        return s[:-2]  # return shampoo
                    else: # i.e beginner
                        return s[:-3]
                else: 
                    return s[:-2]
            return s
        elif s[-2:] == 'ed':
            if len(s) > 3:
                if s[-3] == 'e': # i.e. freed
                    return s[-1] # return free
                elif s[-3] == s[-4]:
                    if s[-3] in 'aiou': # in case of shampooed
                        return s[:-2] # return shampoo
                    else: # i.e. chatted
                        return s[:-3] # return chat
                else: 
                    return s[:-2]
            return s 
        elif s[-2:] == 'ly':
            return s[-2]
        elif s[-1] == 'y':
            return s[:-1] + 'i'
        elif s[-3:] == 'ing': 
            if len(s) > 4: # not the case of sing, king, ring, ... 
                if s[-5] == s[-4]: # i.e. beginning, mapping, programming, seeing, kneeing... 
                    if s[-4] in 'aeiou': # in the case of seeing, kneeing, ...
                        return s[:-3] # return see, knee
                    else:
                        return s[:-4] # return begin, map, program
                elif has_vowel(s[:-3]): # not the case of thing, string, cling, etc. 
                        return s[:-3]
            return s
        elif s[-3:] == 'ism':
            return s[:-3]
        else:
            return s
    

def compare_dictionaries(d1, d2):
    """ input: d1, d2 are two dictionaries
        return their log similarity score 
    """    
    score = 0
    total = 0
    
    for key in d1:
        total += d1[key]
    
    for key in d2:
        if key in d1:
            prob = d1[key] / total
        else:
            prob = 0.5 / total
        
        score += d2[key] * math.log(prob)
    
    return score
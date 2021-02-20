#
# test.py - run tests to check if the TextModel class is working
#

from TextModelClass import TextModel

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

    
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('The New York Times')
    source1.add_file('NYT_source.txt')


    source2 = TextModel('Wall Street Journal')
    source2.add_file('WSJ_source.txt')

    new1 = TextModel('test1')
    new1.add_file('test1_NYT.txt') # test1_NYT is an article from The New York Times
    new1.classify(source1, source2)
    print("\n")
    
    new2 = TextModel('test2')
    new2.add_file('test2_NYT.txt') # test2_NYT is an article from The New York Times
    new2.classify(source1, source2)
    print("\n")
    
    new3 = TextModel('test3')
    new3.add_file('test3_WSJ.txt') # test3_WSJ is an article from Wall Street Journal
    new3.classify(source1, source2)
    print("\n")
    
    new4 = TextModel('test4')
    new4.add_file('test4_WSJ.txt') # test4_WSJ is an article from Wall Street Journal
    new4.classify(source1, source2)
    print("\n")
    
    
    new5 = TextModel('NBC')
    new5.add_file('test5_NBC.txt') # test5_NBC is an article from NBC News
    new5.classify(source1, source2)
    print("\n")
        
print("============================ Test TextModel Class============================\n")
print("_____ Test add_string and classify methods___ \n")
test()
print("\n ___ Test add_file and classify method ___ \n")
print("Build a text model for The New York Times articles and one for Wall Street Journal articles \n")
print("Then, classify the mysterious texts to be either from The New York Times of Wall Street Journal\n")
run_tests()
print("============================ End Test ===============================")
    

    
   
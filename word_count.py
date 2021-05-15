def wordcountfunc(word):
    word_list = word.split()
    number = len(word_list)
    return number
   

def testwords():
    assert wordcountfunc("madam") == 1
    assert wordcountfunc("Joe and friends") == 3


def func(word):
    temp = word [::-1]
    if word.lower() == temp.lower():
        return "is palindrome"
    else:
       return "is not palindrome"

def test_method():
    assert func("Madam") == "is palindrome"
    assert func("Joe") == "is not palindrome"
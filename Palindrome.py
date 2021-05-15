def checkpalindrome(word):
    temp = word [::-1]
    if word.lower() == temp.lower():
        return "is palindrome"
    else:
       return "is not palindrome"

checkpalindrome("Joe")
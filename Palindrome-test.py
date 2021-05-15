import unittest
import Palindrome

class testCaseAdd(unittest.TestCase):
      def test_volume(self):
            self.assertEqual(Palindrome.checkpalindrome("Madam"),"is palindrome")
            self.assertEqual(Palindrome.checkpalindrome("Joe"),"is not palindrome")





if __name__ == '__main__':
    unittest.main()
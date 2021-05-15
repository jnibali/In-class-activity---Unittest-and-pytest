import unittest
import word_count

class testCaseAdd(unittest.TestCase):
      def test_volume(self):
            self.assertEqual(word_count.wordcountfunc("Madam"),1)
            self.assertEqual(word_count.wordcountfunc("Joe and friends"),3)
            self.assertEqual(word_count.wordcountfunc(""),0)





if __name__ == '__main__':
    unittest.main()
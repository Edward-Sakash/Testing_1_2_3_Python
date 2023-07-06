def is_palindrome(string):
    # Remove spaces, punctuation, and convert to lowercase
    string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the string is equal to its reverse
    return string == string[::-1]

import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        string = ''
        result = is_palindrome(string)
        self.assertTrue(result)

    def test_palindrome_string(self):
        string = 'A man, a plan, a canal: Panama'
        result = is_palindrome(string)
        self.assertTrue(result)

    def test_non_palindrome_string(self):
        string = 'OpenAI'
        result = is_palindrome(string)
        self.assertFalse(result)

    def test_palindrome_numbers(self):
        string = '12321'
        result = is_palindrome(string)
        self.assertTrue(result)

    def test_non_palindrome_numbers(self):
        string = '12345'
        result = is_palindrome(string)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

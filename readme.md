# Exercise 1 (Unittest - Average):
Write a function called calculate_average that takes in a list of numbers and returns the average of those numbers.
Your task is to implement the calculate_average function and write unit tests to verify its correctness.
def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return total / len(numbers)
import unittest

class TestCalculateAverage(unittest._____):
    def test_empty_list(self):
        numbers = []
        result = calculate_average(numbers)
        self.assertIsNone(______)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, ____)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = calculate_average(numbers)
        self.assertEqual(____, ____)

    def test_mixed_numbers(self):
        numbers = [-1, 2, -3, 4, -5]
        result = calculate_average(numbers)
        self.______(___, ____)

# Exercise 2 (Test - Palindrom):
Implement a function called is_palindrome that takes in a string and returns True if the string is a palindrome, and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
Your task is to implement the is_palindrome function and write unit tests to verify its correctness.
def is_palindrome(string):
    # Remove spaces, punctuation, and convert to lowercase
    string = ''.join(char.lower() for ____ in _____ if char.isalnum())
    # Check if the string is equal to its reverse
    return string == string[::-1]
import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        string = ''
        result = ________(___)
        self.assert____(result)

    def test_palindrome_word(self):
        string = 'level'
        result = ________(___)
        self.assert___(_____)

    def test_non_palindrome_word(self):
        string = 'hello'
        result = is_palindrome(______)
        self.assert______(_____)

    def test_palindrome_sentence(self):
        string = 'A man, a plan, a canal, Panama'
        result = ________(string)
        self.____(_____)

    def test_non_palindrome_sentence(self):
        string = 'OpenAI is amazing'
        result = _______(___)
        self.______(___)

# Exercise 3 (Test - Anagram):
Implement a function called anagram_groups that takes in a list of strings and groups the anagrams together. An anagram is a word formed by rearranging the letters of another word. Your function should return a list of lists, where each inner list contains a group of anagrams.
Your task is to implement the anagram_groups function and write unit tests to verify its correctness.
def anagram_groups(words):
    groups = {}
    for word in words:
        # Normalize the word by sorting its letters
        sorted_word = ''.join(sorted(word.lower()))
        # Add the word to its corresponding group
        groups.setdefault(sorted_word, []).append(word)
    return list(groups.values())
import unittest

class TestAnagramGroups(unittest.TestCase):
    def test_empty_list(self):
        words = []
        result = ______
        self.assert_(___, [])

    def test_no_anagrams(self):
        words = ['hello', 'world', 'python']
        result = ______
        self.assert____(___, [['hello'], ['world'], ['python']])

    def test_single_anagram_group(self):
        words = ['listen', 'silent', 'enlist']
        result = _____
        self.assert_____(____, [['listen', 'silent', 'enlist']])

    def test_multiple_anagram_groups(self):
        words = ['debitcard', 'badcredit', 'elvis', 'lives', 'silent', 'listen']
        result = ____
        self.______(____, ______)

    def test_case_insensitive(self):
        words = ['debitcard', 'BadCredit', 'Elvis', 'lives', 'silent', 'listen']
        result = ______
        _____.______(____, _________) 
        
               
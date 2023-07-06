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
        result = anagram_groups(words)
        self.assertListEqual(result, [])

    def test_no_anagrams(self):
        words = ['hello', 'world', 'python']
        result = anagram_groups(words)
        self.assertListEqual(result, [['hello'], ['world'], ['python']])

    def test_single_anagram_group(self):
        words = ['listen', 'silent', 'enlist']
        result = anagram_groups(words)
        self.assertListEqual(result, [['listen', 'silent', 'enlist']])

    def test_multiple_anagram_groups(self):
        words = ['debitcard', 'badcredit', 'elvis', 'lives', 'silent', 'listen']
        result = anagram_groups(words)
        self.assertListEqual(result, [['debitcard', 'badcredit'], ['elvis', 'lives'], ['silent', 'listen']])

    def test_case_insensitive(self):
        words = ['debitcard', 'BadCredit', 'Elvis', 'lives', 'silent', 'listen']
        result = anagram_groups(words)
        self.assertListEqual(result, [['debitcard', 'BadCredit'], ['Elvis', 'lives'], ['silent', 'listen']])

if __name__ == '__main__':
    unittest.main()

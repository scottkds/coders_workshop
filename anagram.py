import unittest


def remove_anagrams(array):
    """Removed words that are comprised of the exact same letters."""
    seen_words = set()
    non_anagrams = []
    for idx, word in enumerate(array):
        sorted_characters = ''.join(sorted(word.lower()))
        if sorted_characters not in seen_words:
            seen_words.add(sorted_characters)
            non_anagrams.append(word)

    return non_anagrams

class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        self.assertEqual(remove_anagrams(['pam', 'map', 'amp']), ['pam'])
        self.assertEqual(remove_anagrams(['Pam', 'map', 'pam']), ['Pam'])
        self.assertEqual(remove_anagrams(['pam', 'aaa', 'bbb']), ['pam', 'aaa', 'bbb'])

    
if __name__ == '__main__':

    unittest.main()

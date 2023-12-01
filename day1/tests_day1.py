import unittest

from day1 import replace_digit_words_with_ints


class MyTestCase(unittest.TestCase):
    def test_replace_digit_words_with_ints_one_success(self):
        string = replace_digit_words_with_ints("2one2")
        self.assertEqual(string, "212")

    def test_replace_digit_words_with_ints_two_success(self):
        string = replace_digit_words_with_ints("2two2")
        self.assertEqual(string, "222")

    def test_replace_digit_words_with_ints_three_success(self):
        string = replace_digit_words_with_ints("2three2")
        self.assertEqual(string, "232")

    def test_replace_digit_words_with_ints_four_success(self):
        string = replace_digit_words_with_ints("2four2")
        self.assertEqual(string, "242")

    def test_replace_digit_words_with_ints_five_success(self):
        string = replace_digit_words_with_ints("2five2")
        self.assertEqual(string, "252")

    def test_replace_digit_words_with_ints_six_success(self):
        string = replace_digit_words_with_ints("2six2")
        self.assertEqual(string, "262")

    def test_replace_digit_words_with_ints_seven_success(self):
        string = replace_digit_words_with_ints("2seven2")
        self.assertEqual(string, "272")

    def test_replace_digit_words_with_ints_eight_success(self):
        string = replace_digit_words_with_ints("2eight2")
        self.assertEqual(string, "282")

    def test_replace_digit_words_with_ints_nine_success(self):
        string = replace_digit_words_with_ints("2nine2")
        self.assertEqual(string, "292")


if __name__ == '__main__':
    unittest.main()

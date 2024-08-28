import unittest

from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_heading_top(self):
        md = """
# Hello
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        self.assertEqual("Hello", extract_title(md))
    
    def test_heading_mid(self):
        md = """
This is **bolded** paragraph
# Hello
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        self.assertEqual("Hello", extract_title(md))


if __name__ == "__main__":
    unittest.main()
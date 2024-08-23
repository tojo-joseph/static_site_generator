import unittest

from block_markdown import block_to_block_type, markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_string(self):
        new_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        self.assertEqual(['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'], markdown_to_blocks(new_text))


    def test_block_heading(self):
        new_block = "# This is a heading"
        self.assertEqual("heading", block_to_block_type(new_block))
    
    def test_block_code(self):
        new_block = "```\nThis is a piece\n```"
        self.assertEqual("code", block_to_block_type(new_block))
    
    def test_block_quote(self):
        new_block = "> This is a quote\n> of all quotes"
        self.assertEqual("quote", block_to_block_type(new_block))
    
    def test_block_unordered(self):
        new_block = "* item 1\n* item 2"
        self.assertEqual("unordered_list", block_to_block_type(new_block))
    
    def test_block_ordered(self):
        new_block = "1. item 1\n2. item 2\n3. item 3"
        self.assertEqual("ordered_list", block_to_block_type(new_block))
    
    def test_block_paragraph(self):
        new_block = "This is a heading of all headings."
        self.assertEqual("paragraph", block_to_block_type(new_block))

if __name__ == "__main__":
    unittest.main()

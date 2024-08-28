import unittest

from block_markdown import block_to_block_type, markdown_to_blocks, markdown_to_html_node

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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>", html)
    

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>", html)


    def test_lists(self):
        md = """
- This is a list
- with new list
- items 

1. This is
2. an ordered
3. list

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><ul><li>This is a list</li><li>with new list</li><li>items</li></ul><ol><li>This is</li><li>an ordered</li><li>list</li></ol></div>", html)


    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>", html)
    

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>", html)


if __name__ == "__main__":
    unittest.main()

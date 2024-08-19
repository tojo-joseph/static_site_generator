import unittest

from split_delimiter import split_nodes_delimiter
from split_delimiter import text_type_text
from split_delimiter import text_type_bold
from split_delimiter import text_type_italic
from split_delimiter import text_type_code
from textnode import TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_exception(self):
        new_test_node = [TextNode("Here's a ` symbol", "text")]
        with self.assertRaises(Exception):
            split_nodes_delimiter(new_test_node, "`", text_type_text)
    
    def test_bold(self):
        new_test_node = [TextNode("Here's a **bold text**", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("bold text", text_type_bold)
        ], split_nodes_delimiter(new_test_node, "**", text_type_bold))

    def test_double_bold(self):
        new_test_node = [TextNode("Here's a **bold text** and another **bold word**", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode(" and another ", text_type_text),
            TextNode("bold word", text_type_bold),
        ], split_nodes_delimiter(new_test_node, "**", text_type_bold))

    def test_italic(self):
        new_test_node = [TextNode("Here's a *italic text*", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("italic text", text_type_italic)
        ], split_nodes_delimiter(new_test_node, "*", text_type_italic))

    def test_double_italic(self):
        new_test_node = [TextNode("Here's a *italic text* and another *italic sentence*", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("italic text", text_type_italic),
            TextNode(" and another ", text_type_text),
            TextNode("italic sentence", text_type_italic)
        ], split_nodes_delimiter(new_test_node, "*", text_type_italic))

    def test_code(self):
        new_test_node = [TextNode("Here's a `piece of code`", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("piece of code", text_type_code)
        ], split_nodes_delimiter(new_test_node, "`", text_type_code))

    def test_double_code(self):
        new_test_node = [TextNode("Here's a `piece of code` and another `similar piece`", "text")]
        self.assertEqual([
            TextNode("Here's a ", text_type_text),
            TextNode("piece of code", text_type_code),
            TextNode(" and another ", text_type_text),
            TextNode("similar piece", text_type_code)
        ], split_nodes_delimiter(new_test_node, "`", text_type_code))

if __name__ == "__main__":
    unittest.main()
        
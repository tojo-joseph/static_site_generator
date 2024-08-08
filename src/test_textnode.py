import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a super text node", 'light')
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        new_node = TextNode('This is a pointless test', 'light')
        new_expert_node = TextNode('This is a pointless test', 'light' )
        self.assertEqual(new_node, new_expert_node)
        
    def test_text_type(self):
        new_minor_node = TextNode('This is a pointless test', 'light')
        new_major_node = TextNode('This is a pointless test', 'bold' )
        self.assertNotEqual(new_minor_node, new_major_node)


if __name__ == "__main__":
    unittest.main()

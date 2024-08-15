import unittest

from textnode import TextNode
from htmlnode import LeafNode
from textnode_converter import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_exception(self):
        node = TextNode("Coolest text node ever", None, 'https://www.google.com')
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        

    def test_text(self):
        node1 = TextNode("Coolest text node ever", 'text')
        new_node1 = text_node_to_html_node(node1)
        self.assertEqual(new_node1.tag, None )
        self.assertEqual(new_node1.value, node1.text)
        
        

    def test_link(self):
        node5 = TextNode("Coolest text node ever", 'link', 'https://www.google.com')
        new_node5 = text_node_to_html_node(node5)
        self.assertEqual(new_node5.tag, "a")
        self.assertEqual(new_node5.value, node5.text)
        self.assertEqual(new_node5.props, {"url": node5.url})
    
    def test_image(self):
        node6 = TextNode("Coolest text node ever", 'image', None, 'https://www.google.com', 'alt text')
        new_node6 = text_node_to_html_node(node6)
        self.assertEqual(new_node6.tag, "img")
        self.assertEqual(new_node6.value, "")
        self.assertEqual(new_node6.props, { "src": node6.src, "alt": node6.alt})



if __name__ == "__main__":
    unittest.main()
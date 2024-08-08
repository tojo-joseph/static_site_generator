import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_value(self):
        node = HTMLNode('a', 'Xyz', None, { "href": 'http://www.google.com', "target": "_blank"})
        node1 = HTMLNode('p', 'abcd', None, { "class": 'new-paragraph', "style": "{padding: 0}"})
        node2 = HTMLNode('img', None, None, { "src": 'http://www.unsplash.com', "alt": "new_image", "style": "{width: 40, height: 40}"})
        self.assertEqual('href="http://www.google.com" target="_blank" ', node.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_leaf(self):
        node3 = LeafNode("p", "This is a paragraph of text.")
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual('<p>This is a paragraph of text.</p>', node3.to_html())
        self.assertEqual('<a href="https://www.google.com" target="_blank">Click me!</a>', node4.to_html())


if __name__ == "__main__":
    unittest.main()
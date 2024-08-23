import unittest
from image_extractor import split_nodes_image
from split_delimiter import text_type_text
from image_extractor import text_type_image
from textnode import TextNode

class TestSplitNodesImage(unittest.TestCase):
    def test_no_images(self):
        node = TextNode("This is text with no images", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with no images", text_type_text)], new_nodes)




    def test_single_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and text", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and text", text_type_text)], new_nodes)
    
    
    def test_double_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")], new_nodes)


    def test_double_image_and_text(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")], new_nodes)


    def test_triple_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif")], new_nodes)
    
    
    def test_triple_image_and_text(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and more text", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and more text", text_type_text)], new_nodes)
    

if __name__ == "__main__":
    unittest.main()
import unittest

from text_converter import text_to_textnodes
from textnode import TextNode
from split_delimiter import text_type_text, text_type_italic, text_type_bold, text_type_code
from image_extractor import text_type_image, text_type_link

class TestTextConverter(unittest.TestCase):
    def test_link(self):
        new_text = "There is an image and a link ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and [link](https://boot.dev)"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("There is an image and a link ", text_type_text), TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and ", text_type_text), TextNode("link", text_type_link, "https://www.boot.dev")], result)
    
    def test_bold(self):
        new_text = "There is a **bold** text in here"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("There is a ", text_type_text), TextNode("bold", text_type_bold), TextNode(" text in here", text_type_text)], result)

    def test_italic(self):
        new_text = "There is an *italic* text here"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("There is an ", text_type_text), TextNode("italic", text_type_italic), TextNode(" text here", text_type_text)], result)

    def test_code(self):
        new_text = "There is a piece of `code` in this `block`"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("There is a piece of ", text_type_text), TextNode("code", text_type_code), TextNode(" in this ", text_type_text), TextNode("block", text_type_code)], result)

    def test_image(self):
        new_text = "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("This is an ", text_type_text), TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")], result)

    def test_link(self):
        new_text = "This is a [link](https://boot.dev)"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("This is a ", text_type_text), TextNode("link", text_type_link, "https://boot.dev")], result)

    def test_all(self):
        new_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(new_text)
        self.assertEqual([TextNode("This is ", text_type_text), TextNode("text", text_type_bold), TextNode(" with an ", text_type_text), TextNode("italic", text_type_italic), TextNode(" word and a ", text_type_text), TextNode("code block", text_type_code), TextNode(" and an ", text_type_text), TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", text_type_text), TextNode("link", text_type_link, "https://boot.dev")], result)        

if __name__ == "__main__":
    unittest.main()












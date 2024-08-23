import unittest
from image_extractor import split_nodes_link
from split_delimiter import text_type_text
from image_extractor import text_type_link
from textnode import TextNode

class TestSplitNodesLink(unittest.TestCase):
    def test_no_links(self):
        node = TextNode("This is text with no links", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with no links", text_type_text)], new_nodes)


    def test_single_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev")], new_nodes)
    
    
    def test_double_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")], new_nodes)


    def test_double_link_and_text(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and text", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"), TextNode(" and text", text_type_text)], new_nodes)


    def test_triple_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to boot dev](https://www.boot.dev)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"), TextNode(" and ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev")], new_nodes)
    
    
    def test_triple_link_and_text(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to boot dev](https://www.boot.dev) and text", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"), TextNode(" and ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and text", text_type_text)], new_nodes)
    

if __name__ == "__main__":
    unittest.main()
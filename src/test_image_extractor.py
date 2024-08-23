import unittest
from image_extractor import extract_markdown_images
from image_extractor import extract_markdown_links

class TestImageExtractor(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], extract_markdown_images(text))

    def test_links(self):
        link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], extract_markdown_links(link_text))

if __name__ == "__main__":
    unittest.main()
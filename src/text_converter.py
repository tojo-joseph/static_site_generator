from image_extractor import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter
from textnode import TextNode
from split_delimiter import text_type_text, text_type_bold, text_type_italic, text_type_code


def text_to_textnodes(text):
    initial_node = [TextNode(text, text_type_text)]
    bold_formatted = split_nodes_delimiter(initial_node, "**", text_type_bold)
    italic_formatted = split_nodes_delimiter(bold_formatted, "*", text_type_italic)
    code_formatted = split_nodes_delimiter(italic_formatted, "`", text_type_code)
    image_updated_text = split_nodes_image(code_formatted)
    link_updated_text = split_nodes_link(image_updated_text)
    
    return link_updated_text


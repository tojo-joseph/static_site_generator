import re

from textnode import TextNode
from split_delimiter import text_type_text

text_type_image = "image"
text_type_link = "link"

def extract_markdown_images(text):
    image_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    result = []
    result.extend(image_matches)
    return result

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    final_result = []
    final_result.extend(link_matches)
    return final_result

def split_nodes_image(old_nodes):
    split_image_result = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            split_image_result.append(old_node)
            continue
        old_node_text = old_node.text
        image_matched = extract_markdown_images(old_node_text)
        if len(image_matched) == 0:
            split_image_result.append(old_node)
            continue
        elif old_node.text == "":
            continue
        else:
            starting_oldnode_text = old_node.text
            for image_alt, image_link in image_matched:
                sections = starting_oldnode_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0] != "":
                    split_image_result.append(TextNode(sections[0], text_type_text))
                    split_image_result.append(TextNode(image_alt, text_type_image, image_link))
                starting_oldnode_text = sections[1]
            if starting_oldnode_text != "":
                split_image_result.append(TextNode(starting_oldnode_text, text_type_text))      
    return split_image_result

def split_nodes_link(old_nodes):
    split_link_result = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            split_link_result.append(old_node)
            continue
        old_node_text = old_node.text
        link_matched = extract_markdown_links(old_node_text)
        if len(link_matched) == 0:
            split_link_result.append(old_node)
            continue
        elif old_node.text == "":
            continue
        else:
            starting_oldnode_text = old_node.text
            for link_alt, link_link in link_matched:
                sections = starting_oldnode_text.split(f"[{link_alt}]({link_link})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, link section not closed")
                if sections[0] != "":
                    split_link_result.append(TextNode(sections[0], text_type_text))
                    split_link_result.append(TextNode(link_alt, text_type_link, link_link))
                starting_oldnode_text = sections[1]
            if starting_oldnode_text != "":
                split_link_result.append(TextNode(starting_oldnode_text, text_type_text))

    return split_link_result


        



    







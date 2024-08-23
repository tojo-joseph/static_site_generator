from image_extractor import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter


def text_to_textnodes(text):
    image_updated_text = split_nodes_image(text)
    link_updated_text = split_nodes_link(image_updated_text)
    final_text = split_nodes_delimiter(link_updated_text)
    return final_text

new_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
result = text_to_textnodes(new_text)
print(result)
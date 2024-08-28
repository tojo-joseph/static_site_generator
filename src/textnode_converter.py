from textnode import TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        text_node = LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        text_node = LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        text_node = LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        text_node = LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        text_node = LeafNode("a", text_node.text, {"href": text_node.url} )
    elif text_node.text_type == "image":
        text_node = LeafNode("img", "", {"src": text_node.src, "alt": text_node.alt})
    else:
        raise Exception("The TextNode type is invalid")
    return text_node

def main():
    new_textnode = TextNode("Coolest text node ever", 'text')
    converted_node = text_node_to_html_node(new_textnode)
    return converted_node

result = main()
print(result)
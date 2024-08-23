from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        # splitting text according to delimiter
        for i in range(0, len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(sections[i], text_type_text))
            else:
                result.append(TextNode(sections[i], text_type))
    
    return result


    

    
class TextNode:
    def __init__(self, text, text_type, url=None, src=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.src = src
        self.alt = alt
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url}, {self.src}, {self.alt})"

def main():
    my_node = TextNode("Coolest text node ever", 'light', 'https://www.google.com')
    return my_node

result = main()
print(result)
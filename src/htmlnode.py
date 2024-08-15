class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('The HTML feature was not implemented')
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" ' 
        return result
    
    def __repr__(self):
        return f"HTMLNode Object Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('Value is required for a leafnode')
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html().strip()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)
    
    def to_html(self, acc=''):
        if self.tag == None:
            raise ValueError('The tag is required in ParentNode')
        acc += f"<{self.tag}>"
        if self.children == None:
            raise ValueError('This property is required in ParentNode')
        if len(self.children) == 0:
            return 
        else:
            for child in self.children:
                acc += child.to_html()
            acc += f"</{self.tag}>"
            return acc
        
    
def main():
    my_node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], None)
    return my_node.to_html()

result = main()
print(result)


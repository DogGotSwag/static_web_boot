class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method")
    
    def props_to_html(self):
        string = ""
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        return string
    
    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        children: {self.children}
        props: {self.props}
        """

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("has no tag")
        if self.children is None:
            raise ValueError("children value is missing")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
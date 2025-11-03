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
        
    
dis_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}


test = HTMLNode("a", "hello fn", "h2", dis_dict)
print(test)


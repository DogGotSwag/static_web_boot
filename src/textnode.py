from enum import Enum
    
class TextType(Enum):
    PLAIN_TEXT = "plain",
    ITALIC_TEXT = "italic",
    CODE_TEXT = "code",
    LINK = "link",
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType[text_type]
        self.url = url

    def __eg__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text, self.text_type.value[0], self.url})"
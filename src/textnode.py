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
        self.text_type = text_type
        self.url = url
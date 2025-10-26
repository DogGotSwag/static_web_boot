from enum import Enum
    
class TextType(Enum):
    PLAIN_TEXT = "",
    ITALIC_TEXT = "",
    CODE_TEXT = "",
    LINKS = "",
    IMAGES = ""

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
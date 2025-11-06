from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("wrong type")
    
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text, {"href": ""})
    
    if text_node.text_type is TextType.IMAGE:
        return LeafNode("i", text_node.text, {"src": "", "alt" : ""})


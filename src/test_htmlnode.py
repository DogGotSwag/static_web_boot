import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

test_props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test_node = HTMLNode("a", "hello", "p", test_props)
        self.assertEqual(test_node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_tag(self):
        test_node = HTMLNode("h1", "hello", "p", test_props)
        self.assertEqual(test_node.tag, "h1")

    def test_value(self):
        test_node = HTMLNode("h6", "motto motto", "p", test_props)
        self.assertEqual(test_node.value, "motto motto")


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("big bold fr", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>big bold fr</b>")

    def test_italic(self):
        node = TextNode("very italic text por favor", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>very italic text por favor</i>")

    def test_italic(self):
        node = TextNode("coding in c means ur good", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>coding in c means ur good</i>")

import unittest
from htmlnode import HTMLNode

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
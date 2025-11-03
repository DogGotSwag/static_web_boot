import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h3(self):
        node = LeafNode("h3", "Title Here")
        self.assertEqual(node.to_html(), "<h3>Title Here</h3>")

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_value_two(self):
        node = LeafNode("p", "")
        self.assertRaises(ValueError, node.to_html)

    def test_raw_text(self):
        node = LeafNode(None, "helo world")
        self.assertEqual("helo world", node.to_html())

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"} )
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_inside(self):
        child_node = LeafNode("span", "child")
        nested_parent_node = ParentNode("div", [child_node])
        parent_node = ParentNode("div", [child_node, nested_parent_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><div><span>child</span></div></div>"
        )

    def test_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_no_grandchildren(self):
        nested_parent_node = ParentNode("div", [])
        parent_node = ParentNode("div", [nested_parent_node])
        self.assertEqual(parent_node.to_html(), "<div><div></div></div>")

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

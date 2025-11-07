import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com/")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is maybe a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.google.com/")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_all_not_equal(self):
        node = TextNode("no regular F150", TextType.LINK, "https://www.google.com/")
        node2 = TextNode("dis a raptor", TextType.TEXT)
        self.assertNotEqual(node, node2)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_code_delimiter_two(self):
        node = TextNode("`code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode("", TextType.TEXT),
            ]
        )

    def test_bold_delimiter(self):
        node = TextNode("big big **bold** text ong", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("big big ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text ong", TextType.TEXT),
            ]
        )

    def test_bold_delimiter_two(self):
        node = TextNode("**bold alone**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.TEXT),
                TextNode("bold alone", TextType.BOLD),
                TextNode("", TextType.TEXT),
            ]
        )

    def test_italic_delimiter(self):
        node = TextNode("very fancy _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("very fancy ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ]
        )
        
    def test_italic_delimiter_two(self):
        node = TextNode("_lonely text_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.TEXT),
                TextNode("lonely text", TextType.ITALIC),
                TextNode("", TextType.TEXT),
            ]
        )
        


if __name__ == "__main__":
    unittest.main()
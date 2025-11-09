import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)

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
                TextNode("code block", TextType.CODE),
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
                TextNode("bold alone", TextType.BOLD),
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
                TextNode("lonely text", TextType.ITALIC),
            ]
        )
        
class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_two(self):
        matches = extract_markdown_images(
            "![potato image](https://efr.farms.com/potato_pic.png) hhmm look a potato"
        )
        self.assertListEqual([("potato image", "https://efr.farms.com/potato_pic.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [to boot dev](https://boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://boot.dev")], matches)

    def test_extract_markdown_links_three(self):
        matches = extract_markdown_links(
            "![to google](https://img.com/poo) dis not a link "
        )
        self.assertListEqual([], matches)

class TestSplitNodesImageAndLINKS(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )   

    def test_split_links_and_images(self):
        node = TextNode(
        "free young melvin [to melvin petition](https://www.freeyungmelvin.com) and [to youtube](https://www.youtube.com/why) This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(nodes)


        self.assertListEqual(
            [
                TextNode("free young melvin ", TextType.TEXT),
                TextNode("to melvin petition", TextType.LINK, "https://www.freeyungmelvin.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/why"),
                TextNode(" This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),

            ],
            new_nodes
        )   



if __name__ == "__main__":
    unittest.main()
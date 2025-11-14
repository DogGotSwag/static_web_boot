import unittest
from block_markdown import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quotes(self):
        md = """
> dis here a
> text in a p
> tag here

> This is another paragraph with _italic_

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>> dis here a > text in a p > tag here</blockquote><blockquote>> This is another paragraph with <i>italic</i></blockquote></div>",
        )
    def test_unordered(self):
        md = """
- list item one
- list item two
- here goes there `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>- list item one</li><li>- list item two</li><li>- here goes there <code>code</code> here</li></ul></div>",
        )

    def test_ordered(self):
        md = """
1. list item one
2. list item two
3. here goes there `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>1. list item one</li><li>2. list item two</li><li>3. here goes there <code>code</code> here</li></ol></div>",
        )
import unittest
from htmlnode import ParentNode
from htmlnode import LeafNode

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
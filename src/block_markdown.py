from enum import Enum
import re
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes, TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph", 
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED = "unordered_list",
    ORDERED = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    final_list = []
    for block in blocks:
        if block.strip() == "" or block.strip() == "\n":
            continue
        final_list.append(block.strip())     
    return final_list

def check_each_line(pattern, text):
    for line in text.split('\n'):
        match_obj = re.match(pattern, line)
        if match_obj is None:
            return False
    return True

def ordered_lines_check(text):
    index = 1
    for line in text.split('\n'):
        match_obj = re.match(r"^\d\.\s[\s\S]{1,}", line)
        if match_obj is None:
            return False
        if int(line[0]) != index:
            return False
        index += 1
    return True

def block_to_block_type(block_text):
    heading_re = r"^\#{1,6}\s{1}[\w\S]{1,}"
    code_re = r"^\`{3}[\s\S]{1,}\`{3}$"
    quote_re = r"^\>[\s\S]{1,}"
    unordered_re = r"^\-\s[\s\S]{1,}"
    if re.match(heading_re, block_text) is not None:
        return BlockType.HEADING
    elif re.match(code_re, block_text) is not None:
        return BlockType.CODE
    elif check_each_line(quote_re, block_text):
        return BlockType.QUOTE
    elif check_each_line(unordered_re, block_text):
        return BlockType.UNORDERED
    elif ordered_lines_check(block_text):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH

def children_from_lines(block, tag):
    text = ""
    if tag == "blockquote":
        text =  " ".join(list(map( lambda x: x.split(" ", 1)[1],block.split('\n'))))
    else:
        text = " ".join(block.split('\n'))
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    parent_html_node = ParentNode(tag, html_nodes)
    return parent_html_node

def make_list(block, tag):
    all_list_items = []
    for line in block.split('\n'):
        text_only = line.split(" ", 1)
        text_nodes = text_to_textnodes(text_only[1])
        html_nodes = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            html_nodes.append(html_node)
        list_item = ParentNode("li", html_nodes)
        all_list_items.append(list_item)
    return ParentNode(tag, all_list_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []

    for block in blocks:
        type_of_block = block_to_block_type(block)
        match type_of_block:
            case BlockType.PARAGRAPH:
                html_children.append(children_from_lines(block, "p"))
            case BlockType.HEADING:
                for line in block.split('\n'):
                    text = line.split(" ", 1)
                    textnodes = text_to_textnodes(text[1])
                    html_child = []
                    for tn in textnodes:
                        html_node = text_node_to_html_node(tn)
                        html_child.append(html_node)
                    this_header = ParentNode(f"h{len(text[0])}", html_child)
                    html_children.append(this_header)
            case BlockType.CODE:
                lines = block.split("\n")
                text = ""
                for line in lines:
                    if line == "```":
                        continue
                    text += f"{line}{"\n"}"
                textnode = TextNode(text, TextType.TEXT)
                htmlnode = text_node_to_html_node(textnode)
                html_children.append(ParentNode("pre", [ParentNode("code", [htmlnode])]))
            case BlockType.QUOTE:
                html_children.append(children_from_lines(block, "blockquote"))
            case BlockType.UNORDERED:
                html_children.append(make_list(block, "ul"))
            case BlockType.ORDERED:
                html_children.append(make_list(block, "ol"))
    return ParentNode("div", html_children)


md = """
> This is a
> blockquote block

this is paragraph text

"""

print(markdown_to_html_node(md).to_html())

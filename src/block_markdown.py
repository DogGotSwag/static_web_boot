from enum import Enum
import re
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
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
    text = " ".join(block.split('\n'))
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    parent_html_node = ParentNode(tag, html_nodes)
    return parent_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []

    for block in blocks:
        type_of_block = block_to_block_type(block)
        match type_of_block:
            case BlockType.PARAGRAPH:
                html_children.append(children_from_lines(block, "p"))
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                tag = "blockquote"
                html_children.append(children_from_lines(block, "blockquote"))
            case BlockType.UNORDERED:
                pass
            case BlockType.ORDERED:
                pass
    return ParentNode("div", html_children)

md = """
> dis here a
> text in a p
> tag here

> This is another paragraph with _italic_

"""

print(markdown_to_html_node(md).to_html())

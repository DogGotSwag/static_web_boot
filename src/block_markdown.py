from enum import Enum
import re

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
    
block_to_block_type("1. hello dis a list\n2. list part two")
    
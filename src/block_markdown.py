from enum import Enum
import re

class blockType(Enum):
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

def block_to_block_type(block_text):
    heading_re = r"^\#{1,6}\s{1}[\w\S]{1,}"
    code_re = r"^\`{3}[\s\S]*\`{3}$"
    quote_re = r"^\>[\s\S]*"
    unordered_re = r"^\-\s[\s\S]*"
    if re.match(heading_re, block_text) is not None:
        print("heading")
    elif re.match(code_re, block_text) is not None:
        print("code")
    elif check_each_line(quote_re, block_text):
        print("quote")
    elif check_each_line(unordered_re, block_text):
        print("unordered")
    
        

    

block_to_block_type("- hello dis a list\n-list part two")
    
from enum import Enum

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



def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    final_list = []
    for block in blocks:
        lines = block.split('\n')
        kept_lines = []
        for line in lines:
            if line != "":
                kept_lines.append(line.strip())
        joined_lines = '\n'.join(kept_lines)
        final_list.append(joined_lines)            
    return final_list

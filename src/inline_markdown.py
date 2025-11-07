from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    all_results = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            all_results.append(old_node)
        else:
            split_result = old_node.text.split(delimiter)
            if len(split_result) == 1:
                raise ValueError("invalid Markdown syntax")
            result = [
                TextNode(split_result[0], TextType.TEXT),
                TextNode(split_result[1], text_type),
                TextNode(split_result[2], TextType.TEXT),
            ]
            all_results.extend(result)
    return all_results

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

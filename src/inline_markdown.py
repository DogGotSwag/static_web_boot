from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    all_results = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            all_results.append(old_node)
        else:
            split_result = old_node.text.split(delimiter)
            if len(split_result) % 2 == 0:
                raise ValueError("invalid Markdown syntax")
            for i in range(len(split_result)):
                if split_result[i] == "":
                    continue
                if i % 2 == 0:
                    all_results.append(TextNode(split_result[i], TextType.TEXT))
                else:
                    all_results.append(TextNode(split_result[i], text_type))
    return all_results

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    all_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_images(text)
        if len(links) == 0:
            if text != "":
                all_nodes.append(node)
        else:
            sections = text.split(f"![{links[0][0]}]({links[0][1]})", 1)
            all_nodes.extend(split_nodes_image([TextNode(sections[0],TextType.TEXT)]))
            all_nodes.append(TextNode(links[0][0], TextType.IMAGE, links[0][1]))
            all_nodes.extend(split_nodes_image([TextNode(sections[1],TextType.TEXT)]))
    return all_nodes

def split_nodes_link(old_nodes):
    all_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            if text != "":
                all_nodes.append(node)
        else:
            sections = text.split(f"[{links[0][0]}]({links[0][1]})", 1)
            all_nodes.extend(split_nodes_link([TextNode(sections[0],TextType.TEXT)]))
            all_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
            all_nodes.extend(split_nodes_link([TextNode(sections[1],TextType.TEXT)]))
    return all_nodes

# def text_to_textnodes(text):
#     nodes = split_nodes_link(split_nodes_image([TextNode(text, TextType.TEXT)]))
#     res = split_nodes_delimiter(nodes, "**", TextType.BOLD)
#     res_two = split_nodes_delimiter(res, "`", TextType.CODE)
#     res_three = split_nodes_delimiter(res_two, "_", TextType.ITALIC)
#     return res_three

# res = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

# for node in res:
#     print(node)
import re
from htmlnode import HTMLNode
from leafnode import ParentNode, LeafNode
from inline_util import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    # print(blocks, 'blocks')
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    # print(ParentNode("div", children, None), 'node')
    return ParentNode("div", children, None)
    
def block_to_html_node(block):
        block_type = block_to_block_type(block)
        if block_type == 'heading':
            return header_to_html_node(block)
        elif block_type == "code":
            return code_to_html_node(block)
        elif block_type == 'quote':
            return quote_to_html_node(block)
        elif block_type == 'unordered_list':
            return ul_to_html_node(block)
        elif block_type == 'ordered_list':
            return ol_to_html_node(block)
        elif block_type == 'paragraph':
            return paragraph_to_html_node(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    print(text_nodes)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def ul_to_html_node(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[2:]
        text = text.strip()
        # print(text)
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ul', html_items)

def ol_to_html_node(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[3:]
        text = text.strip()
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ol', html_items)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode('pre', code)

def quote_to_html_node(block):
    lines = block.split('\n')
    for line in lines:
        line = line[1:]
        line.strip()
    stripped_text = ' '.join(lines)
    children = text_to_children(stripped_text)
    return ParentNode('blockquote', children)

def header_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1:]
    text = text.strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)




def markdown_to_blocks(markdown):
    # takes the entire document and returns a list of block strings
    initial_blocks = markdown.split('\n\n')
    empty_blocks_filtered = list(filter(lambda x : x != '', initial_blocks))
    remove_whitespaces = list(map(lambda x : x.strip(), empty_blocks_filtered))
    return remove_whitespaces

def block_to_block_type(block):
    # 6 types of blocks paragraph, heading, code, quote, unordered_list and ordered_list
    # we'll return one of the above
    # the input block argument is a string
    if check_if_heading(block):
        return 'heading'
    elif block[:3] == '```' and block[-3:] =='```':
        return 'code'
    elif check_if_quote(block):
        return 'quote'
    elif check_if_unordered_list(block):
        return 'unordered_list'
    elif check_if_ordered_list(block):
        return 'ordered_list'
    else:
        return 'paragraph'
    
def check_if_ordered_list(block):
    lines = block.split('\n')
    for i in range(0, len(lines)):
        if not lines[i][0].isdigit() or not lines[i][1] == '.' or not lines[i][2] == ' ':
            return False
    return True

def check_if_unordered_list(block):
    lines = block.split('\n')
    for line in lines:
        if not (line[0] != '*' or line[0] != '-') or not line[1] == ' ':
            return False
    return True
    
    
def check_if_quote(block):
    if block[0] != '>':
        return False
    lines = block.split('\n')
    for line in lines:
        if line[0] != '>':
            return False
    return True

def check_if_heading(block):

    if block[0] != '#':
        return False
    
    for i in range(0, len(block)):
        if block[i] == '#' and block[i+1] == ' ':
            return True
    return False






# if __name__ == "__main__":
#     markdown_ex = """
#     # This is a heading

#     This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#     * This is the first list item in a list block
#     * This is a list item
#     * This is another list item
#     """
#     markdown_to_blocks(markdown_ex)

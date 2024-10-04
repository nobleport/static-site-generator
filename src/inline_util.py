from textnode import TextNode
import re

delimiter_options = {
    '`': "code",
    '*': "italics",
    '**': "bold"
}

text_type_text="text"
text_type_code="code"
text_type_bold="bold"
text_type_italics="italics"
text_type_image="image"
text_type_link="link"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old nodes is a list of nodes
    # split old 'text' type nodes into more nodes that are split by the delimiter
    #need to convert a raw markdown string into a list of textnode objects
    if delimiter not in delimiter_options:
        raise Exception("Not a valid delimiter")
    nodes = old_nodes
    split_nodes = []

    for node in nodes:
        if node.text_type != 'text':
            split_nodes.append(node)
        else:
            text = node.text
            split_text = text.split(delimiter)
            split_inner_line = []
            if len(split_text) % 2 != 1:
                raise Exception('invalid Markdown syntax')
            
            i = 0
            while i < len(split_text):
                if split_text[i] == '':
                    i += 1
                elif i % 2 == 0:
                    current_node = TextNode(split_text[i], text_type_text)
                    split_nodes.append(current_node)
                    i += 1
                elif i % 2 == 1:
                    current_node = TextNode(split_text[i], text_type)
                    split_nodes.append(current_node)
                    i += 1
    return split_nodes
    
def extract_markdown_images(markdown_text):
    #returns a list of tuples
    # each tuple should contain the alt text and the url of any markdown images
    return_list = []
    extracted_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text)
    for match in extracted_matches:
        return_list.append(match)
    if len(return_list) == 0:
        return None
    return return_list

def extract_markdown_links(text):
    return_list = []
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        return_list.append(match)
    if len(return_list) == 0:
        return None
    return return_list

def split_nodes_image(old_nodes):
    new_nodes_list = []
    for node in old_nodes:
        extracted_alt_urls = extract_markdown_images(node.text)
        if extracted_alt_urls is None:
            new_nodes_list.append(node)
            continue
        current_text = node.text
        # print(extracted_alt_urls, 'this is the extracted urls')
        for alt_image in extracted_alt_urls:
            split_text = current_text.split(f'![{alt_image[0]}]({alt_image[1]})')
            if not split_text[0] and not split_text[1]:
                current_image_type_node = TextNode(alt_image[0], text_type_image, alt_image[1])
                new_nodes_list.append(current_image_type_node)
                break
            text_before_image = split_text[0]
            current_text_type_node = TextNode(text_before_image, text_type_text)
            current_image_type_node = TextNode(alt_image[0], text_type_image, alt_image[1])
            if current_text_type_node.text == '':
               continue
            else: 
                new_nodes_list.append(current_text_type_node)
            new_nodes_list.append(current_image_type_node)
            current_text = split_text[1]
        if current_text and node.text != f"![{extracted_alt_urls[0][0]}]({extracted_alt_urls[0][1]})":
            final_text_node = TextNode(current_text, text_type_text)
            new_nodes_list.append(final_text_node)

    return new_nodes_list

    
def split_nodes_link(old_nodes):
    new_nodes_list = []
    for node in old_nodes:
        extracted_alt_urls = extract_markdown_links(node.text)
        if extracted_alt_urls is None:
            new_nodes_list.append(node)
            continue
        current_text = node.text
        # print(extracted_alt_urls)
        for alt_image in extracted_alt_urls:
            split_text = current_text.split(f'[{alt_image[0]}]({alt_image[1]})')
            if not split_text[0] and not split_text[1]:
                current_link_type_node = TextNode(alt_image[0], text_type_link, alt_image[1])
                new_nodes_list.append(current_link_type_node)
                continue
            text_before_image = split_text[0]
            current_text_type_node = TextNode(text_before_image, text_type_text)
            current_link_type_node = TextNode(alt_image[0], text_type_link, alt_image[1])
            if current_text_type_node.text == '':
               continue
            else: 
                new_nodes_list.append(current_text_type_node)
            new_nodes_list.append(current_link_type_node)
            current_text = split_text[1]
        if current_text and node.text != f"[{extracted_alt_urls[0][0]}]({extracted_alt_urls[0][1]})":
            final_text_node = TextNode(current_text, text_type_text)
            new_nodes_list.append(final_text_node)
    return new_nodes_list

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    # print(nodes, '1')
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    # print(nodes, '2')
    nodes = split_nodes_delimiter(nodes, "*", text_type_italics)
    # print(nodes, '3')
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    # print(nodes, '4')
    nodes = split_nodes_image(nodes)
    # print(nodes, '5')
    nodes = split_nodes_link(nodes)
    # print(nodes, '6')
    return nodes

if __name__ == "__main__":
    text="![image](https://www.example.com/image.png)"
    print(text.split("![image](https://www.example.com/image.png)"))
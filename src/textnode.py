from leafnode import LeafNode

options_dict = {
        'text_type_text': "text",
        'text_type_bold': "bold",
        'text_type_italic': "italics",
        'text_type_code': "code",
        'text_type_link': "link",
        'text_type_image': "image"
        }

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(node):
        if node.text_type == options_dict['text_type_text']:
            return LeafNode(None, node.text)
        elif node.text_type == options_dict['text_type_bold']:
            return LeafNode('b', node.text)
        elif node.text_type == options_dict['text_type_italic']:
            return LeafNode('i', node.text)
        elif node.text_type == options_dict['text_type_code']:
            return LeafNode('code', node.text)
        elif node.text_type == options_dict['text_type_link']:
            props = {'href': node.url}
            return LeafNode('a', node.text, props)
        elif node.text_type == options_dict['text_type_image']:
            props = {
                    'src': node.url,
                    'alt': node.text
                     }
            return LeafNode('img', '', props)
    
        
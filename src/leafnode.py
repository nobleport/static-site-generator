from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):        
        super().__init__(tag=tag, value=value, children=None, props = props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('LeafNode requires a value')
        #renders the leaf node as an HTML string (it returns a string)
        if self.tag is None:
            return self.value
        start_tag = f'<{self.tag}{self.props_to_html()}>'
        end_tag = f'</{self.tag}>'
        return f'{start_tag}{self.value}{end_tag}'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, children: {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('Parent Node requires a tag')
        if self.children is None:
            raise ValueError('Parent node requires child nodes')
        start_tag = f'<{self.tag}{self.props_to_html()}>'
        end_tag = f'</{self.tag}>'
        internal_constructor = ''
        print(self.children, 'THESE ARE THE CHILDREN')
        for child in self.children:
            # print(child, 'child')
            if child is not None:
                internal_constructor += f'{child.to_html()}'
        final_constructor = f'{start_tag}{internal_constructor}{end_tag}'
        return final_constructor
        #final_construct = f'{}'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


        

        
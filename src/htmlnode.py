class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # tag is a string representing the tag name, "p", "a", "h1" etc
    # value is a string representing the value of the tag (text inside)
    # childred a list of html node objects representing the children of the node
    # props is a dictionary of k-v pairs representing attributes of the html tag, like <a> tag
        # might have {"href":"https://www.google.com"}
    

    #node without value is assumed to have children and not without children will have a value
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        node_props = self.props
        string_constructor = ""
        for key, value in node_props.items():
            string_constructor += f' {key}="{value}"'
        return string_constructor

    def __eq__(self, other):
        # Compare tag, value, children, and props for equality
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
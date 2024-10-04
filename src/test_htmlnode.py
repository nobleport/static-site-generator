import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "this is the value", props={"href":"https://www.google.com"})
        node2 = HTMLNode("a", "this is the value", props={"href":"https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("a", "not the value")
        node2 = HTMLNode("a", "this is the value")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "this is the value", props={"href":"https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        # node2 = HTMLNode("a", "this is the value", props={"href":"https://www.google.com"})
        
        
if __name__ == "__main__":
    unittest.main()
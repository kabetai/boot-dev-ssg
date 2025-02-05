import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_different_texttypes(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://gutenberg.org")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://gutenberg.org")
        self.assertNotEqual(node,node2)

    def test_different_text(self):
        node  = TextNode("This is not really a text node", TextType.IMAGE, "https://gutenberg.org")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://gutenberg.org")
        self.assertNotEqual(node,node2)
    
    
    def test_different_url(self):
        node  = TextNode("This is a text node", TextType.IMAGE, "https://eff.org")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://gutenberg.org")
        self.assertNotEqual(node,node2)
    
    def test_none_url(self):
        node  = TextNode("This is a text node", TextType.IMAGE, None)
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://gutenberg.org")
        self.assertNotEqual(node,node2)
    
    def test_text_to_html(self):
        node = TextNode("This is text node", TextType.TEXT)
        node2 = LeafNode(None,"This is text node")
        self.assertEqual(node.text_node_to_html_node(),node2)

    def test_link_leaf_node(self):
        node = TextNode("Click me", TextType.URL, "boot.dev")
        actual = node.text_node_to_html_node()
        expected = LeafNode("a","Click me",{"href":"boot.dev"})
        self.assertEqual(actual,expected)

    def test_image_to_leaf_node(self):
        node = TextNode("surprised pikachu", TextType.IMAGE, "surprised_pikachu.jpg")
        actual = node.text_node_to_html_node()
        expected = LeafNode("img","",{"src":"surprised_pikachu.jpg", "alt":"surprised pikachu"})
        self.assertEqual(actual,expected)

if __name__ == "__main__":
    unittest.main()

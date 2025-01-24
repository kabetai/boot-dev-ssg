import unittest

from textnode import TextNode, TextType


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
    

if __name__ == "__main__":
    unittest.main()

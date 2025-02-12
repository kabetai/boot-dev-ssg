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

    def test_split_one_text_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_with_delimiter([node], "`", TextType.CODE)
        expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,expected)

    def test_nothing_to_split(self):
        node= TextNode("This text has nothing to split",TextType.TEXT)
        expected = [TextNode("This text has nothing to split",TextType.TEXT)]
        new_nodes = TextNode.split_nodes_with_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes,expected)

    def test_invalid_syntax(self):
        node = TextNode("This text is not *valid Markdown",TextType.TEXT)
        self.assertRaises(Exception, TextNode.split_nodes_with_delimiter, [node],"*",TextType.ITALIC)

    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = TextNode.extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(matches,expected)
    
    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual= TextNode.extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual,expected)

    def test_extract_no_link(self):
        text = "This is text without link"
        actual = TextNode.extract_markdown_links(text)
        self.assertEqual(len(actual),0)

    def test_extract_no_image(self):
        text = "This is text without image"
        actual = TextNode.extract_markdown_images(text)
        self.assertEqual(len(actual),0)
    
    def test_split_on_image(self):
        text_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif),TextType.TEXT)
        images = TextNode.split_nodes_for_image([text_node]) 
        self.assertEqual(images[1].text_type, TextType.IMAGE)


if __name__ == "__main__":
    unittest.main()

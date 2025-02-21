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
        text_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",TextType.TEXT)
        images = TextNode.split_nodes_for_image([text_node]) 
        image = images[1]
        self.assertEqual(image.text_type, TextType.IMAGE)

    def test_split_on_multiple_images(self):
        images_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a jpeg ![A JPEG](https://i.imgur.com/abc.jpeg)",TextType.TEXT)
        images = TextNode.split_nodes_for_image([images_node])
        self.assertEqual(images[0].text, "This is text with a ")
        self.assertEqual(images[1].text_type, TextType.IMAGE)
        self.assertEqual(images[2].text, " and a jpeg ")
        self.assertEqual(images[3].text_type, TextType.IMAGE)

    def test_split_on_link(self):
        links_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        links = TextNode.split_nodes_for_link([links_node])
        self.assertEqual(links[0].text, "This is text with a link ") 
        self.assertEqual(links[1].text_type,TextType.URL) 
        self.assertEqual(links[2].text, " and ") 
        self.assertEqual(links[3].text_type, TextType.URL) 

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ",TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ",TextType.TEXT),
            TextNode("italic",TextType.ITALIC),
            TextNode(" word and a ",TextType.TEXT),
            TextNode("code block",TextType.CODE),
            TextNode(" and an ",TextType.TEXT),
            TextNode("obi wan image",TextType.IMAGE,"https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.URL, "https://boot.dev")
        ]

        nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(expected,nodes)

    def test_markdown_to_blocks(self):
        markdown = """ 
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.


        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        blocks = TextNode.markdown_to_blocks(markdown)
        self.assertEqual(len(blocks),3)
        self.assertEqual(blocks[0],"# This is a heading")
        self.assertEqual(blocks[1],
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        self.assertEqual(blocks[2],"""* This is the first list item in a list block
        * This is a list item
        * This is another list item""")

if __name__ == "__main__":
    unittest.main()

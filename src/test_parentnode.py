import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_tag(self):
        node = ParentNode(None, None, {"color":"red"})
        self.assertRaises(ValueError, node.to_html)

    def test_no_props(self):
        node = ParentNode("span", None, {"color":"red"})
        self.assertRaises(ValueError, node.to_html)

    def test_one_level_children(self):
        node = ParentNode("p",[
            LeafNode("b","Bold text"),
            LeafNode(None,"Just text"),
            LeafNode("i","Italic text"),
            LeafNode(None,"Even more text"),
            ],
        )
        html = node.to_html()
        expected = f"<p><b>Bold text</b>Just text<i>Italic text</i>Even more text</p>"
        self.assertEqual(html,expected)

    def test_children_with_parent_node(self):
        level2_node = ParentNode("span",[
            LeafNode("b","Bold text"),
            LeafNode(None,"Just text"),
            LeafNode("i","Italic text"),
            LeafNode(None,"Even more text"),
            ],{"color":"red"}
        )
        node = ParentNode("p", [
            LeafNode("b","Another Bold text"),
            level2_node,
            LeafNode("a","Link",{"href":"boot.dev"}),
            
        ],)
        html = node.to_html()
        expected = f'<p><b>Another Bold text</b><span color="red"><b>Bold text</b>Just text<i>Italic text</i>Even more text</span><a href="boot.dev">Link</a></p>'
        self.assertEqual(html,expected)



if __name__=="__main__":
    unittest.main()

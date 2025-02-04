import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_no_tag(self):
        node = LeafNode(None,"This is paragraph of text.")
        expected = "This is paragraph of text."
        self.assertEqual(expected,node.to_html())

    def test_no_value(self):
        node = LeafNode("p")
        self.assertRaises(ValueError,node.to_html)

    def test_leaf(self):
        node = LeafNode("p","This is paragraph of text.", {"label": "I am a leaf", "color":"red"})
        expected = f'<p label="I am a leaf" color="red">This is paragraph of text.</p>'
        html = node.to_html()
        self.assertEqual(expected,html)



if __name__=="__main__":
    unittest.main()

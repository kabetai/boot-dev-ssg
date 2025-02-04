import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node= HTMLNode("span", "This is text", None, {("style","blue"),("label","OPIS")})
        node2=HTMLNode("span", "This is text", None, {("style","blue"),("label","OPIS")})
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_no_props(self):
        node=HTMLNode("span", "This is text", None, None)
        actual = node.props_to_html()
        self.assertEqual("", actual)




if __name__=="__main__":
    unittest.main()


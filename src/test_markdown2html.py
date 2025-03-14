import unittest

from markdown2html import Markdown2HTML 

class TestMarkdown2Html(unittest.TestCase):

    def test_h1(self):
        h1 = "# This is heading h1"
        result = markdown2html.heading_tag_for_heading_block(h1)
        self.assertEqual(result,"<h1>")

    def test_h2(self):
        h2 = "## This is heading h2"
        result = markdown2html.heading_tag_for_heading_block(h2)
        self.assertEqual(result,"<h2>")

    def test_h3(self):
        h3 = "### This is heading h3"
        result = markdown2html.heading_tag_for_heading_block(h3)
        self.assertEqual(result,"<h3>")

    def test_h4(self):
        h4 = "#### This is heading h4"
        result = markdown2html.heading_tag_for_heading_block(h4)
        self.assertEqual(result,"<h4>")

    def test_h5(self):
        h5 = "##### This is heading h5"
        result = markdown2html.heading_tag_for_heading_block(h5)
        self.assertEqual(result,"<h5>")

    def test_h6(self):
        h6 = "###### This is heading h6"
        result = markdown2html.heading_tag_for_heading_block(h6)
        self.assertEqual(result,"<h6>")

if __name__=="__main__":
    unittest.main()


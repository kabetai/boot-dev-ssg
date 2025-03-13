import unittest

from markdown2html import Markdown2Html as converter

class TestMarkdown2Html(unittest.TestCase):

    def test_h1(self):
        h1 = "# This is heading h1"
        result = converter.heading_tag_for_heading_block(h1)
        self.assertEqual(result,"<h1>)

if __name__=="__main__":
    unittest.main()

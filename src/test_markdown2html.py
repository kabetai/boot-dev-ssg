import unittest

from markdown2html import Markdown2HTML 

class TestMarkdown2Html(unittest.TestCase):

    def test_h1(self):
        h1 = "# This is heading h1"
        Markdown2HTML.convert_markdown_to_html(h1)
        # result = Markdown2HTML.heading_tag_for_heading_block(h1)
        #self.assertEqual(result,"<h1> This is heading h1</h1>")

if __name__=="__main__":
    unittest.main()


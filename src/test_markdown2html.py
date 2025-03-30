import unittest

from markdown2html import Markdown2HTML 

class TestMarkdown2Html(unittest.TestCase):

    def test_h1(self):
        h1 = "# This is heading h1"
        result = Markdown2HTML.heading_tag_for_heading_block(h1)
        self.assertEqual(result,"<h1>")

    def test_h2(self):
        h2 = "## This is heading h2"
        result = Markdown2HTML.heading_tag_for_heading_block(h2)
        self.assertEqual(result,"<h2>")

    def test_h3(self):
        h3 = "### This is heading h3"
        result = Markdown2HTML.heading_tag_for_heading_block(h3)
        self.assertEqual(result,"<h3>")

    def test_h4(self):
        h4 = "#### This is heading h4"
        result = Markdown2HTML.heading_tag_for_heading_block(h4)
        self.assertEqual(result,"<h4>")

    def test_h5(self):
        h5 = "##### This is heading h5"
        result = Markdown2HTML.heading_tag_for_heading_block(h5)
        self.assertEqual(result,"<h5>")

    def test_h6(self):
        h6 = "###### This is heading h6"
        result = Markdown2HTML.heading_tag_for_heading_block(h6)
        self.assertEqual(result,"<h6>")

    def test_convert(self):
        markdown = """* Item 1
        * Item 2
        * Item 3
        * Item 4

### This is heading 3

< Quote text line
< Quote tex line 2
< Quote text line 3

- unordered with - item markers
- more unordered items
- and one more unordered item

* unordered list with asterisk
* second item on the list
* third one
* a fourth one
* and one more

1. now we have ordred list
2. a second item
3. third item 
4. one more itme
5. fifth item

```<div class="color=blue">
        <a href="https://acme.com">asme</a>
        </div>```
        """
        results = Markdown2HTML.convert_markdown_to_html(markdown)

if __name__=="__main__":
    unittest.main()


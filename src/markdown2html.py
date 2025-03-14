from textnode import TextType
from blocktype import BlockType

class Markdown2HTML:

    def convertMarkdownToHtml(markdown):
        text2blocks = TextType.markdown_to_blocks(markdown)
        print(f"{len(text2blocks)} blocks from markdown document")

    def heading_tag_for_heading_block(block):
        #count #
        level = block.count("#")
        text = block[block.rfind("#"):]
        tag = f"<h{level}>"
        return tag

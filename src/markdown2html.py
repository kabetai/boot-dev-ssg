from textnode import *
from blocktype import BlockType

class Markdown2HTML:

    def convert_markdown_to_html(markdown):
        text2blocks = TextNode.markdown_to_blocks(markdown)
        print(f"{len(text2blocks)} blocks from markdown document")
        for block in text2blocks:
            block_type = BlockType.block_to_blocktype(block)
            print(f"block type {block_type}")


    def heading_tag_for_heading_block(block):
        #count #
        level = block.count("#")
        text = block[block.rfind("#")+1:]
        tag = f"<h{level}>{text}</h{level}>"
        return tag

    def code_block_to_code_tag(block):
        code_md = "```"


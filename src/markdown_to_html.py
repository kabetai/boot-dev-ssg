from htmlnode import HTMLNode
from blocktype import BlockType

class Converter:

    def markdown_to_html(markdown):
        # 1. Break text to markdown blocks
        blocks = BlockType.block_to_blocktype(markdown)
        # 2. 

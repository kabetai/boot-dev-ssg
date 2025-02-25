import re
import unittest

from textnode import TextNode, TextType
from block_type import BlockType
from leafnode import LeafNode

class TestBlockType(unittest.TestCase):

    def test1_heading_block(self):
        h1_block = "# This is heading h1"
        result = BlockType.block_to_blocktype(h1_block)
        self.assertEqual(result, BlockType.HEADING)

    def test2_heading_block(self):
        h2_block = "## This is heading h2"
        result = BlockType.block_to_blocktype(h2_block)
        self.assertEqual(result, BlockType.HEADING)

    def test3_heading(self):
        h3_block = "### This is heading h3"
        result = BlockType.block_to_blocktype(h3_block)
        self.assertEqual(result, BlockType.HEADING)

    def test4_heading(self):
        h4_block = "#### This is heading h4"
        result = BlockType.block_to_blocktype(h4_block)
        self.assertEqual(result, BlockType.HEADING)

    def test5_heading(self):
        h5_block = "##### This is heading h5"
        result = BlockType.block_to_blocktype(h5_block)
        self.assertEqual(result, BlockType.HEADING)

    def test6_heading(self):
        h6_block = "###### This is 6th heading"
        result = BlockType.block_to_blocktype(h6_block)
        self.assertEqual(result, BlockType.HEADING)

    #def test_header2(self):


if __name__=="__main__":
    unittest.main()

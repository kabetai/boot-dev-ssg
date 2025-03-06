import re
import unittest

from textnode import TextNode, TextType
from blocktype import BlockType
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

    def test_code_block(self):
        code_block = "```:sp %:h/```"
        result = BlockType.block_to_blocktype(code_block)
        self.assertEqual(result, BlockType.CODE)

    def test_multiline_code_block(self):
        multiline='''```<div class="color=blue">
        <a href="https://acme.com">asme</a>
        </div>```'''
        result = BlockType.block_to_blocktype(multiline)
        self.assertEqual(result, BlockType.CODE)
    
    def test_quote(self):
        quote = "< this is a quote"
        result = BlockType.block_to_blocktype(quote)
        self.assertEqual(result, BlockType.QUOTE)

    def test_multiline_quote(self):
        multiline = """< first line
        <
        < second line
        < third line """
        result = BlockType.block_to_blocktype(multiline)
        self.assertEqual(result, BlockType.QUOTE)

    def test_multiline_unordered_list(self):
        unordered_list = """* Item 1
        * Item 2
        * Item 3
        * Item 4"""
        result = BlockType.block_to_blocktype(unordered_list)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_multiline_ordered_list(self):
        ordered_list = """1. Item I
        2. Item II
        3. Item III
        4. Item IV"""
        result = BlockType.block_to_blocktype(ordered_list)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragrapgh(self):
        paragraph = "This is just text with no special meaning or formatting."
        result = BlockType.block_to_blocktype(paragraph)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_for_empty(self):
        empty= ""
        with self.assertRaises(ValueError):
            BlockType.block_to_blocktype(empty)

if __name__=="__main__":
    unittest.main()

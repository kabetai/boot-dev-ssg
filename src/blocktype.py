import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

    #@classsmethod
    def block_to_blocktype(block):
        heading_pattern = "^(#){1,6} [\w| ]+"
        # this is pattern for one line code, not multiline
        code_pattern = "^[`]{3}.+[`]{3}$"
        multiline_code = "^```[\s\S]*```$"
        quote_pattern = "$< .*"
        unordered_list_pattern = ""
        ordered_list_pattern=""

        if len(block) == 0:
            raise ValueError("Can't convert from empty text")
        if re.fullmatch(heading_pattern,block):
            return BlockType.HEADING
        if re.fullmatch(code_pattern,block):
           return BlockType.CODE
        if re.fullmatch(multiline_code,block):
            return BlockType.CODE
        if re.fullmatch(quote_pattern,block):
           return BlockType.QUOTE
        if re.fullmatch(unordered_list_pattern,block):
           return BlockType.UNORDERED_LIST
        if re.fullmatch(ordered_list_pattern,block):
            return BlockType.ORDERED_LIST

        return BlockType.PARAGRAPH   

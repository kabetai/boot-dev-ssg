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
        if(len(block) == 0):
            raise ValueError("Can't convert from empty text")
        if(re.fullmatch(heading_pattern,block)):
            return BlockType.HEADING
    

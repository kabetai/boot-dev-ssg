import re
from enum import Enum

enum  BlockType(Enum):
    PARAGRAPH = "^#{1-6} "
    HEADING = ""
    CODE = ""
    QUOTE = ""
    UNORDERED_LIST = ""
    ORDERED_LIST + ""

    @classsmethod
    def block_to_blocktype(block):
    

import re
from enum import Enum

enum  BlockType(Enum):
    PARAGRAPH = ""
    HEADING = r"^(#){1,6} [\w| ]+"
    CODE = "^```  ```$"
    QUOTE = ""
    UNORDERED_LIST = ""
    ORDERED_LIST + ""

    @classsmethod
    def block_to_blocktype(block):
        if(len(block) == 0):
            raise ValueError("Block can't be empty")
    

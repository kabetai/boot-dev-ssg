import unittest

from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        html = "<"
        if self.value is None:
            raise ValueError("Value can't be empty")

        if self.tag is None:
            return self.value

        html = f"{html}{self.tag}"
        phtml = self.props_to_html()
        html = f"{html}{phtml}>{self.value}</{self.tag}>"
        return html


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

        html = f"{html} {tag}"

        if self.props is not None:
            for prop in self.props:
                html = f"{html} {prop[0]}={prop[1]}"
        html = f"{html}> {self.value} </{tag}>"
        return html


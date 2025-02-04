from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag=None, children=None, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        html = "<"

        if self.tag is None:
            raise ValueError("There cannot be ParentNode with no tag")

        if self.children is None:
            raise ValueError("ParentNode has to have children")

        html = f"{html}{self.tag}"

        if self.props is not None:
            phtml = self.props_to_html()
            html = f"{html}{phtml}" 

        html = f"{html}>"

        for child in self.children:
            chtml = child.to_html()
            html = f"{html}{chtml}"

        html = f"{html}</{self.tag}>"
        
        return html

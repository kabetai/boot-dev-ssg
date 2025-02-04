class HTMLNode:

    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html=""
        if self.props is None:
            return ""
        else:
            for prop in self.props:
                html = f"{html} {prop[0]}={prop[1]}"
            return html


    def __repr__(self):
        return "HTML Node - tag: {self.tag}, properties: {self.properties}, children: {self.properties}, value: {self.value}"
        



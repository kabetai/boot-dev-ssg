def class HTMLNode:

    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        html = ""
        if value:
            html = html+value
        else:
            for child in children:
                html = html + props_to_html(child)

        raise NotImplementedError

    def props_to_html(self):
        html=""
        for prop in self.props:
            html = f"{html} {prop[0]}={prop[1]}"
            print(f"{html} {prop[0]}={prop[1]}")
        return html



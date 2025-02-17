import re
from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    URL = "link"
    IMAGE = "image"
    TEXT = "text"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if isinstance(node, TextNode):
            if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
                return True
        return False

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node):
        ttype = text_node.text_type
        if ttype == TextType.TEXT:
            return LeafNode(None,text_node.text)

        if ttype == TextType.BOLD:
            return LeafNode("b",text_node.text)

        if ttype == TextType.ITALIC:
            return LeafNode("i",text_node.text)

        if ttype == TextType.CODE:
            return LeafNode("code",text_node.text)
        
        if ttype == TextType.URL:
            return LeafNode("a",text_node.text,{"href":text_node.url})

        if ttype == TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})

        raise Exception("Unknown Text type")

    def split_nodes_with_delimiter(nodes, delimiter,text_type):
        splitted_nodes = []
        if len(nodes)==0:
            return nodes
        if text_type == TextType.TEXT:
            return nodes

        for node in nodes:
            if node.text_type == TextType.TEXT:
                unpacked = TextNode.unpack_node(node,delimiter,text_type)
                splitted_nodes.extend(unpacked)
            else:
                splitted_nodes.append(node)
        return splitted_nodes

    def unpack_node(node, delimiter, text_type):
        node_texts = node.text.split(delimiter)
        if len(node_texts) == 1:
            ## nothing to split
            return [node]

        if len(node_texts) % 3 != 0:
            raise Exception("Invalid Markdown syntax")

        unpacked = [TextNode(node_texts[0],TextType.TEXT),
                    TextNode(node_texts[1],text_type),
                    TextNode(node_texts[2],TextType.TEXT)]
        return unpacked
        
    def extract_markdown_images(text):
        regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(regex, text)
        return matches

    def extract_markdown_links(text):
        regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(regex,text)
        return matches


    def split_nodes_for_image(nodes):
        new_nodes = []
        if len(nodes)==0:
            return nodes

        for node in nodes:
            images = TextNode.extract_markdown_images(node.text)
            print(f" IMAGES {images}, {len(images)}")
            text = node.text
            for image in images:
                img_node = TextNode.process_img_src(image)
                print(f"img_node alt text {img_node.text}, src {img_node.url}")
                sections = text.split(f"![{image[0]}]({image[1]}), 1")
                print(f"SECTIONS {sections}")
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)
                new_nodes.append(img_node)
                text = sections[1]
                print(f"text after extraction {text}")
        return new_nodes

    def process_img_src(image):
        alt_text = image[0]
        img_url = image[1]
        print(f"image {alt_text} {img_url}")
        return TextNode(alt_text,TextType.IMAGE,img_url)

    def split_nodes_for_link(nodes):
        new_nodes = []
        if len(nodes) == 0:
            return nodes
        
        for node in nodes:
            links = TextNode.extract_markdown_links(node.text)
            for link in links:
                text = link[0]
                url = link[1]
                sections = node.text.split(f"[{text}]({url})",1)
                textnode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textnode)
                linknode = TextNode(text,TextType.LINK,url)
                new_nodes.append(linknode)
        return new_nodes


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
        to_split = node.text
        node_texts = to_split.split(delimiter)
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
            text = node.text
            for image in images:
                img_node = TextNode.process_img_src(image)
                reg = f"!\[{img_node.text}\]\({img_node.url}\)"
                sections = re.split(reg,text)
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)
                new_nodes.append(img_node)
                text = sections[1]
            rest = TextNode(text,TextType.TEXT)
            new_nodes.append(rest)
        return new_nodes

    def process_img_src(image):
        alt_text = image[0]
        img_url = image[1]
        return TextNode(alt_text,TextType.IMAGE,img_url)

    def split_nodes_for_link(nodes):
        new_nodes = []
        if len(nodes) == 0:
            return nodes
        
        for node in nodes:
            links = TextNode.extract_markdown_links(node.text)
            text = node.text
            for link in links:
                link_node = TextNode(link[0],TextType.URL,link[1])
                reg = f"\[{link_node.text}\]\({link_node.url}\)"
                sections = re.split(reg,text)
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)
                new_nodes.append(link_node)
                text = sections[1]
            rest = TextNode(text,TextType.TEXT)
            new_nodes.append(rest)
        return new_nodes

    def text_to_textnodes(text):
        nodes = []
        if len(text) > 0: 
            node = TextNode(text,TextType.TEXT) 
            bolds = TextNode.split_nodes_with_delimiter([node],"**",TextType.BOLD)
            if len(bolds) > 1:
                nodes.append(bolds[0])
                nodes.append(bolds[1])
                rest = bolds[2]
            else:
                rest =  bolds

            italics = TextNode.split_nodes_with_delimiter([rest],"*",TextType.ITALIC)
            if len(italics) > 0:
                nodes.append(italics[0])
                nodes.append(italics[1])
                rest = italics[2]
            else:
                rest = italics
            
            codes = TextNode.split_nodes_with_delimiter([rest],"`",TextType.CODE)
            if len(codes) > 1:
                nodes.append(codes[0])
                nodes.append(codes[1])
                rest = codes[2]
            else:
                rest = codes

            images = TextNode.split_nodes_for_image([rest])
            if len(images) > 1:
                nodes.append(images[0])
                nodes.append(images[1])
                rest = images[2]
            else:
                rest = images

            links = TextNode.split_nodes_for_link([rest])
            nodes.append(links[0])
            nodes.append(links[1])
        return nodes
        
    def markdown_to_blocks(markdown):
        blocks = re.split("\n\n",markdown)
        trimmed = [line.strip() for line in blocks]
        filtered_blocks = [line for line in trimmed if len(line) >0]
        return filtered_blocks

1

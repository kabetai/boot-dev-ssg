from textnode import TextNode, TextType


def main():
    txtnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(repr(txtnode))


print("Hello world")
main()

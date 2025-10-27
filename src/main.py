from textnode import TextNode, TextType

def main():
    obj = TextNode("some anchor text", TextType.LINK, "https://www.boot.dev")
    objTwo = TextNode("some aanchor text", TextType.LINK, "https://www.boot.dev")
    print(obj)
    print(obj == objTwo)

main()
from textnode import TextNode

def main():
    obj = TextNode("some anchor text", "LINK", "https://www.boot.dev")
    objTwo = TextNode("some aanchor text", "LINK", "https://www.boot.dev")
    print(obj)
    print(obj == objTwo)

main()
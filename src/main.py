from textnode import TextNode, TextType

def main():
    try:
        node = TextNode(
            "This is some anchor text",
            TextType.LINK,
            "https://www.boot.dev",
        ) 
        
        print(node)


    except Exception as e:
        return f"Error: {e}"




if __name__ == "__main__":
    main()


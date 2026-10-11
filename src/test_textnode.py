import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("Bussy Bunny", TextType.LINK)
        node2 = TextNode("Bussy Bunny", TextType.BOLD)

        self.assertNotEqual(node,node2)

    def test_different_text(self):
        node = TextNode("JhondoBondo", TextType.BOLD)
        node2 = TextNode("Gunter", TextType.BOLD)

        self.assertNotEqual(node,node2)

    def test_different_url(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Boot.dev", TextType.LINK, "https://example.com")

        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT, None)

        self.assertEqual(node,node2)


    def test_different_link_urls(self):
        node = TextNode(
                "Google",
                TextType.LINK,
                "https://google.com"
                )

        node2 = TextNode(
                "Google",
                TextType.LINK,
                "https;//Docker.com"
                )

        self.assertNotEqual(node,node2)
    
    def test_text_to_html(self):
        node = TextNode("Hello", TextType.TEXT)

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")


    def test_bold_to_html(self):
        node = TextNode("Important", TextType.BOLD)

        html_node = text_node_to_html_node(node)

        self.assertEqual(
            html_node.to_html(),
            "<b>Important</b>"
        )

    def test_italic_to_html(self):
        node = TextNode("Peperonita", TextType.ITALIC)

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.to_html(), "<i>Peperonita</i>")


if __name__ == "__main__":
    unittest.main()

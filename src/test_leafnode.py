import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(
                node.to_html(),
                "<p>Hello, world!</p>"
                )


    def test_leaf_to_html_a(self):
        node = LeafNode(
                "a",
                "Click here",
                {"href": "https://www.boot.dev"}
                )

        self.assertEqual(
                node.to_html(),
                '<a href="https://www.boot.dev">Click here</a>'
                )

    
    def test_leaf_to_html_raw(self):
        node = LeafNode(
                None,
                "Plain text"
                )

        self.assertEqual(
                node.to_html(),
                "Plain text"
                )
    
    def test_leaf_to_html_bold(self):
        node = LeafNode(
                "b",
                "Important"
                )

        self.assertEqual(
                node.to_html(),
                '<b>Important</b>'
                )


if __name__ == "__main__":
    unittest.main()


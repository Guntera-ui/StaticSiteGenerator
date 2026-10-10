import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
        "a",
        "Click here",
        None,
        {
                "href": "https://www.boot.dev",
                "target": "_blank"
                }
        )


        self.assertEqual(
                node.props_to_html(),
                ' href="https://www.boot.dev" target="_blank"'
                )

    def test_empty_props(self):
        node = HTMLNode(props={})

        self.assertEqual(node.props_to_html(), "")


    def test_single_prop(self):
        node = HTMLNode(
            tag="img",
            props={"src": "image.png"}
        )

        self.assertEqual(
            node.props_to_html(),
            ' src="image.png"'
        )

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="p", value="Hello")

        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()

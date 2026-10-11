import unittest
from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_missing_children(self):
        parent = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_multiple_children(self):
        child = LeafNode("b","Bold")
        child2 = LeafNode(None, " normal")
        child3 = LeafNode("i", "italic")
        parent = ParentNode("p", [child, child2, child3])
        self.assertEqual(
                parent.to_html(),
                "<p><b>Bold</b> normal<i>italic</i></p>"
                )
    
    def test_to_html_missing_tag(self):
        child = LeafNode("p", "Winter is coming...")
        parent = ParentNode(None,[child])
        with self.assertRaises(ValueError):
            parent.to_html()





if __name__ == "__main__":
    unittest.main()


import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    )
import re




class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_bold(self):
        node = TextNode(
            "Hello **world** again",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD
        )

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" again", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_no_matching_delimiter(self):
        node = TextNode(
            "Just normal text",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD
        )

        self.assertEqual(result, [node])

    def test_unmatched_delimiter(self):
        node = TextNode(
            "This **is unfinished",
            TextType.TEXT
        )

        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD
            )
    
def test_extract_images(self):
    text = "Look at ![cat](cat.png) and ![dog](dog.jpg)"

    result = extract_markdown_images(text)

    self.assertEqual(
        result,
        [("cat", "cat.png"), ("dog", "dog.jpg")]
    )


    def test_extract_links(self):
        text = "Visit [Google](https://google.com)"

        result = extract_markdown_links(text)

        
        self.assertEqual(
        result,
        [("Google", "https://google.com")]
    )


    def test_no_matches(self):
        text = "This is just plain text."

        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])


    def test_links_ignore_images(self):
        text = "![cat](cat.png) and [Google](https://google.com)"

        result = extract_markdown_links(text)

        self.assertEqual(
            result,
        [("Google", "https://google.com")]
        )

    def test_split_images(self):
        node = TextNode(
            "See ![cat](cat.png) and ![dog](dog.png)",
            TextType.TEXT,
        )

        result = split_nodes_image([node])

        expected = [
            TextNode("See ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "dog.png"),
        ]

        self.assertEqual(result, expected)


    def test_split_links(self):
        node = TextNode(
            "Visit [Google](https://google.com) today",
            TextType.TEXT,
        )

        result = split_nodes_link([node])

        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" today", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_split_image_no_match(self):
        node = TextNode("Just normal text", TextType.TEXT)

        result = split_nodes_image([node])

        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()


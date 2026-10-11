
from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            node = ParentNode("p", text_to_children(text))

        elif block_type == BlockType.HEADING:
            level = len(block) - len(block.lstrip("#"))
            text = block[level + 1:]
            node = ParentNode(f"h{level}", text_to_children(text))

        elif block_type == BlockType.CODE:
            text = block[4:-3]
            code_node = text_node_to_html_node(
                TextNode(text, TextType.CODE)
            )
            node = ParentNode("pre", [code_node])

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            text = " ".join(
                line[1:].strip() for line in lines
            )
            node = ParentNode("blockquote", text_to_children(text))

        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))

            node = ParentNode("ul", items)

        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                text = line.split(". ", 1)[1]
                items.append(ParentNode("li", text_to_children(text)))

            node = ParentNode("ol", items)

        else:
            raise ValueError(f"Unsupported block type: {block_type}")

        children.append(node)

    return ParentNode("div", children)


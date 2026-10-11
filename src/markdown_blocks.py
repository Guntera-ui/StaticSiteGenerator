def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    # Heading: 1–6 # characters followed by a space
    hashes = len(block) - len(block.lstrip("#"))

    if 1 <= hashes <= 6 and block[hashes:hashes + 1] == " ":
        return BlockType.HEADING

    # Code block
    if block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.CODE

    lines = block.split("\n")

    # Quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    if all(
        line.startswith(f"{index}. ")
        for index, line in enumerate(lines, start=1)
    ):
        return BlockType.ORDERED_LIST

    # Default
    return BlockType.PARAGRAPH


import re


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")

    if (markdown_block.startswith("# ") or markdown_block.startswith("## ") or markdown_block.startswith("### ") or markdown_block.startswith("#### ") or markdown_block.startswith("##### ") or markdown_block.startswith("###### ")):
        return f"heading"
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return f"code"
    elif markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif markdown_block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    elif markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif markdown_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    else:
        return "paragraph"
        
    





new_block = "tests resrser e sreser"
result = block_to_block_type(new_block)

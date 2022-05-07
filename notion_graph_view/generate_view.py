from notion_graph_view.parser import BlockParser
from notion_graph_view.parser import my_graph
from notion_graph_view.render import render
from notion_graph_view.config import *


def read_page() -> None:
    block = notion.blocks.retrieve(PAGE_ID)
    BlockParser(block)
    render(my_graph.get_graph())


if __name__ == '__main__':
    read_page()

import pynecone as pc

from ThinkAPI.components.section_header import section_header


def grid_item(State, section_name: str, color_index: int):
    return section_header(section_name, color_index)

import pynecone as pc

from ThinkAPI.components.section_header import section_header


def render_item(item):
    print(item)
    return pc.text(item)


def grid_item(State, section_name: str, color_index: int):

    return pc.vstack(
        section_header(section_name, color_index),
        pc.ordered_list(
            pc.foreach(
                State.items,
                lambda item: render_item(item),
            ),
        ),
        pc.cond(
            State.show_input,
            pc.hstack(
                pc.input(on_blur=State.set_new_item),
                pc.button(pc.icon(tag="CheckIcon"), on_click=State.add_item),
            ),
            pc.button(pc.icon(tag="AddIcon"), on_click=State.open_input),
        ),
        height="5rem",
    )

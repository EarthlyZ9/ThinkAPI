import pynecone as pc

from ThinkAPI.components.layout.base_modal import base_modal
from ThinkAPI.global_state import AppState


def project_item(item):
    return pc.box(pc.text(item), _hover={"background_color": "grey"})


def add_project_modal_header(State):
    return pc.hstack(
        pc.heading("Add a New Project", font_size="1.3em"),
        pc.button(
            pc.icon(tag="CloseIcon"),
            on_click=State.open_add_project_modal,
        ),
        justify="space-between",
    )


class AddProjectModelState(AppState):
    is_modal_open: bool = False

    def open_modal(self):
        self.is_modal_open = not self.is_modal_open


def add_project_modal_body():
    return pc.hstack(pc.input(), pc.button("Add"))


def drawer_projects_header(State):
    return pc.hstack(
        pc.heading("Projects"),
        pc.button(
            pc.icon(tag="AddIcon"), on_click=State.open_modal, width="fit-content"
        ),
        base_modal(State, "Add a New Project", add_project_modal_body),
        justify="space-between",
    )


def drawer(State):
    return pc.box(
        pc.button(pc.icon(tag="HamburgerIcon"), on_click=State.open_drawer),
        pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    pc.drawer_header(drawer_projects_header(AddProjectModelState)),
                    pc.drawer_body(pc.vstack(pc.foreach(State.projects, project_item))),
                    pc.drawer_footer(pc.button("Close", on_click=State.open_drawer)),
                )
            ),
            on_overlay_click=State.open_drawer,
            on_esc=State.open_drawer,
            is_open=State.is_drawer_open,
        ),
    )

import pynecone as pc

from ThinkAPI.components.layout.drawer import drawer
from ThinkAPI.global_state import AppState


class DrawerState(AppState):
    is_drawer_open: bool = False

    def open_drawer(self):
        self.is_drawer_open = not self.is_drawer_open


def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/favicon.ico", width="50px"),
                pc.heading("ThinkAPI"),
            ),
            drawer(DrawerState),
            width="100%",
            display="flex",
            justify="space-between",
        ),
        display="flex",
        align_items="center",
        padding_x="1em",
        bg="rgba(255,255,255, 0.97)",
        width="100%",
        height="8vh",
    )

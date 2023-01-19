"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from ThinkAPI.pages.think_page import think_page
from ThinkAPI.global_state import AppState
from ThinkAPI.global_style import style as global_style
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Think NOW!",
                href="/think",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


def think():
    return think_page()


# Add state and page to the app.
app = pc.App(state=AppState, style=global_style, stylesheets=[
    "https://fonts.googleapis.com/css2?family=Sofia+Sans&display=swap"
])
app.add_page(index, title="ThinkAPI")
app.add_page(think)
app.compile()

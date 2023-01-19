import pynecone as pc


def modal_header(State, title):
    return pc.hstack(
        pc.heading(title, font_size="1.3em"),
        pc.button(
            pc.icon(tag="CloseIcon"),
            on_click=State.open_modal,
        ),
        justify="space-between",
    )


def base_modal(State, modal_title: str, modal_body):
    return pc.modal(
        pc.modal_overlay(
            pc.modal_content(
                pc.modal_header(
                    modal_header(State, modal_title),
                    padding_y="0px !important",
                    margin_bottom="1em",
                ),
                pc.modal_body(modal_body()),
                padding_y="1.5em",
            ),
        ),
        is_open=State.is_modal_open,
        on_overlay_click=State.open_modal,
        on_esc=State.open_modal,
    )

import pynecone as pc
from ThinkAPI import styles


def section_header(name, color_index):
    color = styles.colors[color_index]
    previous = styles.colors[color_index - 1]

    if color_index == 0:
        previous = color

    after_style = {
        "content": '""',
        "position": "absolute",
        "left": "0",
        "bottom": "0",
        "width": "0",
        "height": "0",
        "border_left": f"1.5rem solid {previous}",
        "border_top": f"1.5rem solid {color}",
        "border_bottom": f"1.5rem solid {color}",
    }

    before_style = {
        "content": '""',
        "position": "absolute",
        "right": "-1.5rem",
        "bottom": "0",
        "width": "0",
        "height": "0",
        "border_left": f"1.5rem solid {color}",
        "border_top": "1.5rem solid transparent",
        "border_bottom": "1.5rem solid transparent",
    }

    if color_index == 4:
        before_style = None

    return pc.hstack(
        pc.box(
            pc.center(pc.text(name, color="black", text_align="center"), height="100%"),
            width="100%",
            height="3rem",
            position="relative",
            background=color,
            _after=after_style,
            _before=before_style,
        ),
        width="100%",
    )

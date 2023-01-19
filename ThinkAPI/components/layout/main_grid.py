import pynecone as pc

from ThinkAPI.components.grid_item import grid_item


def main_grid():
    return pc.grid(
        pc.grid_item(grid_item(None, "App/Domain", 0)),
        pc.grid_item(grid_item(None, "Model", 1)),
        pc.grid_item(grid_item(None, "View/Controller", 2)),
        pc.grid_item(grid_item(None, "Serializer", 3)),
        pc.grid_item(grid_item(None, "URL", 4)),
        template_columns="repeat(5, 1fr)",
        height="92vh",
        width="100%",
        margin_top="0px !important",
        background_color="ivory",
    )

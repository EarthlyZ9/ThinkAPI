import pynecone as pc

from ThinkAPI.components.layout.main_grid import main_grid
from ThinkAPI.components.layout.navbar import navbar


def think_page():
    return pc.vstack(navbar(), main_grid(), height="100vh")

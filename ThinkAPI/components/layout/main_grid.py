from typing import Union, List

import pynecone as pc

from ThinkAPI.components.grid_item import grid_item
from ThinkAPI.global_state import AppState
from ThinkAPI.models.item import Item


class SectionBaseState(AppState):
    pass


class Section1State(SectionBaseState):
    new_item: str
    selected_item: Union[str, None] = None
    show_input: bool = False
    items: List[Item] = []
    section_num = 1

    def get_items(self):
        with pc.session() as session:
            self.items = (
                session.query(Item).filter(Item.section == self.section_num).all()
            )

    def open_input(self):
        self.show_input = not self.show_input

    def add_item(self):
        self.items += [self.new_item]
        with pc.session() as session:
            session.add(Item(name=self.new_item, section=self.section_num))
            session.commit()
        self.new_item = None
        self.show_input = False


class Section2State(SectionBaseState):
    new_item: str
    selected_item: Union[str, None] = None
    show_input: bool = False
    items: List[Item] = []
    section_num = 2

    def get_items(self):
        with pc.session() as session:
            self.items = (
                session.query(Item).filter(Item.section == self.section_num).all()
            )
        print(self.items)

    def open_input(self):
        self.show_input = not self.show_input

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = None
        self.show_input = False


class Section3State(SectionBaseState):
    new_item: str
    selected_item: Union[str, None] = None
    show_input: bool = False
    items: List[Item] = []
    section_num = 3

    def get_items(self):
        with pc.session() as session:
            self.items = (
                session.query(Item).filter(Item.section == self.section_num).all()
            )
        print(self.items)

    def open_input(self):
        self.show_input = not self.show_input

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = None
        self.show_input = False


class Section4State(SectionBaseState):
    new_item: str
    selected_item: Union[str, None] = None
    show_input: bool = False
    items: List[Item] = []
    section_num = 4

    def get_items(self):
        with pc.session() as session:
            self.items = (
                session.query(Item).filter(Item.section == self.section_num).all()
            )
        print(self.items)

    def open_input(self):
        self.show_input = not self.show_input

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = None
        self.show_input = False


class Section5State(SectionBaseState):
    new_item: str
    selected_item: Union[str, None] = None
    show_input: bool = False
    items: List[Item] = []
    section_num = 5

    def get_items(self):
        with pc.session() as session:
            self.items = (
                session.query(Item).filter(Item.section == self.section_num).all()
            )
            print(self.items)

    def open_input(self):
        self.show_input = not self.show_input

    def add_item(self):
        self.items += [self.new_item]
        self.new_item = None
        self.show_input = False


def main_grid():
    return pc.grid(
        pc.grid_item(grid_item(Section1State, "App/Domain", 0)),
        pc.grid_item(grid_item(Section2State, "Model", 1)),
        pc.grid_item(grid_item(Section3State, "View/Controller", 2)),
        pc.grid_item(grid_item(Section4State, "Serializer", 3)),
        pc.grid_item(grid_item(Section5State, "URL", 4)),
        template_columns="repeat(5, 1fr)",
        height="92vh",
        width="100%",
        margin_top="0px !important",
        background_color="ivory",
    )

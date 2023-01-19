import datetime
from typing import Union

import pynecone as pc


class Item(pc.Model, table=True):
    name: str
    section: int
    notes: Union[str, None]
    created_at: datetime.datetime = datetime.datetime.now()

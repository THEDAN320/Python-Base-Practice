"""test module..."""

from typing import Annotated

from pydantic import BaseModel, Field, StrictInt


class User(BaseModel):
    """User class.

    :param tg_id: user id from telegram."""

    tg_id: Annotated[StrictInt, Field(gt=10, description="lala")]


User(tg_id=9)

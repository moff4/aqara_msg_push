# pylint: disable=no-name-in-module
from pydantic import BaseModel, Field


class TopLevelMessage(BaseModel):
    # Authorized user's unique identifier
    open_id: str = Field(alias='openId')

    # Message unique identification id
    msg_id: str = Field(alias='msgId')

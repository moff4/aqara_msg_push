# pylint: disable=no-name-in-module
from typing import Optional

from pydantic import BaseModel, Field

from .enums import TriggerResult, TriggerType
from .mixin import TimeMixin


class TriggerSource(TimeMixin, BaseModel):

    # Message trigger type, see the description of "Trigger Type" below for details
    type: TriggerType

    # The trigger object id that caused the message change, such as the linkage id
    id: Optional[str]


class DeviceStateMessage(TimeMixin, BaseModel):
    # Object id, such as: device id or scene id or linkage id
    subject_id: str = Field(alias='subjectId')

    # The attribute id of the object, such as the on-off state of the socket
    resource_id: str = Field(alias='resourceId')

    # The value to which the attribute of the object is changed
    value: str

    # The status change result, success or failure, see the description of "Trigger result" below for details
    status_code: TriggerResult = Field(alias='statusCode')

    # Message trigger reason
    trigger_source: Optional[TriggerSource] = Field(alias='triggerSource')

    # When the user uses User-defined subscription mode, the parameters passed through the "subscribe resource"
    # interface will be returned as it is when the message is generated.
    attach: Optional[str]

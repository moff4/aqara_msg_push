
from typing import Any

from pydantic import Field

from .base import TopLevelMessage
from .device_attr_msg import DeviceStateMessage
from .enums import EventType
from .event import EVENT_MSG_REGISTRY
from .mixin import TimeMixin


class EventNotificationMessage(TimeMixin, TopLevelMessage):
    # Event message notification type
    event_type: EventType = Field(alias='eventType')

    # Specific message content
    data: Any

    def __init__(self, *a: Any, **b: Any) -> None:
        super().__init__(*a, **b)
        submodel = EVENT_MSG_REGISTRY[self.event_type]
        self.data = submodel(**self.data)


class DeviceAttributeMessage(TimeMixin, TopLevelMessage):

    # Message type, resource_report
    msg_type: str = Field(alias='msgType')

    # Message content
    data: list[DeviceStateMessage]


class DeviceControlFailureMessage(TimeMixin, TopLevelMessage):

    # Message content
    data: list[DeviceStateMessage]

    # Message type, control_fail
    event_type: EventType = Field(EventType.CONTROL_FAIL, alias='eventType')

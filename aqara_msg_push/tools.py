
from typing import Any, Type

from .schema import DeviceAttributeMessage, DeviceControlFailureMessage, EventNotificationMessage, TopLevelMessage


def get_object(data: dict[str, Any]) -> TopLevelMessage:
    if 'msgType' in data:
        model = DeviceAttributeMessage  # type: Type[TopLevelMessage]
    elif data.get('eventType') == 'control_fail':
        model = DeviceControlFailureMessage
    else:
        model = EventNotificationMessage
    return model(**data)

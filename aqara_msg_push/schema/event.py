# pylint: disable=no-name-in-module
from typing import Callable, Optional, Type

from mapping_shortcuts.decors import create_class_collector
from pydantic import BaseModel, Field

from .enums import EventType
from .mixin import TimeMixin


class EventMsg(BaseModel):
    ...


collector_tools = create_class_collector()
event_msg_registrator = collector_tools[0]  # type: Callable[[EventType], Callable[[Type[EventMsg]], Type[EventMsg]]]
EVENT_MSG_REGISTRY = collector_tools[1]  # type: dict[EventType, Type[EventMsg]]


@event_msg_registrator(EventType.GATEWAY_BIND)
class GatewayBind(TimeMixin, EventMsg):
    """
    Gateway binding notification message
    """
    # subject model
    model: str

    # Device id
    did: str

    # Random code bound when the device is added
    bind_key: Optional[str] = Field(alias='bindKey')

    # Subdevice info list
    sub_dids: Optional[list[str]] = Field(alias='subDids')


@event_msg_registrator(EventType.SUBDEVICE_BIND)
class SubdeviceBind(TimeMixin, EventMsg):
    """
    Sub-device binding notification message
    """
    # subject model
    model: str

    # Device id
    did: str

    # Gateway device id
    parent_did: str = Field(alias='parentDid')


@event_msg_registrator(EventType.GATEWAY_UNBIND)
class GatewayUnbind(TimeMixin, EventMsg):
    """
    Gateway unbinding notification message
    """
    # Device id
    did: str

    # Subdevice info list
    sub_dids: Optional[list[str]] = Field(alias='subDids')

    # Reasons for unbinding,
    # 2-gateway operation,
    # 3-cloud operation,
    # 4-gateway reset to the factory,
    # 5-cloud reset gateway
    cause: int


@event_msg_registrator(EventType.UNBIND_SUB_GW)
class UnbindSubGW(TimeMixin, EventMsg):
    """
    Sub-device unbinding notification message
    """
    # Device id
    did: str

    # Gateway device id
    parent_did: str = Field(alias='parentDid')

    # Reason for unbinding,
    # 12-Cloud triggers sub-device unbinding,
    # 13-gateway triggers sub-device unbinding,
    # 17-sub-device replacement and unbinding
    cause: int


@event_msg_registrator(EventType.GATEWAY_ONLINE)
class GatewayOnline(TimeMixin, EventMsg):
    """
    Gateway online notification message
    """
    # Device id
    did: str

    # Subdevice info list
    sub_dids: Optional[list[str]] = Field(alias='subDids')


@event_msg_registrator(EventType.GATEWAY_OFFLINE)
class GatewayOffline(TimeMixin, EventMsg):
    """
    Gateway offline notification message
    """
    # Device id
    did: str

    # Subdevice info list
    sub_dids: Optional[list[str]] = Field(alias='subDids')


@event_msg_registrator(EventType.SUBDEVICE_ONLINE)
class SubdeviceOnline(TimeMixin, EventMsg):
    """
    Sub-device online notification message
    """
    # Device id
    did: str

    # Online reason,
    # 11-sub device heartbeat goes online
    # 16-sub device is bound online
    cause: int


@event_msg_registrator(EventType.SUBDEVICE_OFFLINE)
class SubdeviceOffline(TimeMixin, EventMsg):
    """
    Sub-device offline notification message
    """
    # Device id
    did: str

    # Offline reason,
    # 12-sub device is offline without heartbeat,
    # 15-sub device is unbound offline,
    cause: int


@event_msg_registrator(EventType.DEV_NAME_CHANGE)
class DevNameChange(TimeMixin, EventMsg):
    """
    Modify device name notification message
    """

    # Gateway id
    parent_did: str = Field(alias='parentDid')

    # Position id
    position_id: str = Field(alias='positionId')

    # subject model
    model: str

    # Device name
    deviceName: str

    # Device id
    did: str


@event_msg_registrator(EventType.DEV_POSITION_ASSIGN)
class DevPositionAssign(TimeMixin, EventMsg):
    """
    Modify device position notification message
    """
    # Position name
    position_name: str = Field(alias='positionName')

    # Position id
    position_id: str = Field(alias='positionId')

    # Device id array
    dids: list[str]


class ChangeValues(BaseModel):
    # Resource id
    resource_id: str = Field(alias='resourceId')

    # Updated name
    name: str


@event_msg_registrator(EventType.RESOURCE_ALIAS_CHANGED)
class ResourceAliasChanged(TimeMixin, EventMsg):
    """
    Modify device attribute name notification message
    """
    # Modify value array
    changeValues: list[ChangeValues]

    # Device id
    did: str


@event_msg_registrator(EventType.LINKAGE_CREATED)
class LinkageCreated(TimeMixin, EventMsg):
    """
    Create automation notification messages
    """
    # subject model
    model: str

    # Linkage id
    linkage_id: str = Field(alias='linkageId')


@event_msg_registrator(EventType.SCENE_CREATED)
class SceneCreated(TimeMixin, EventMsg):
    """
    Create scene notification message
    """
    # subject model
    model: str

    # Scene id
    scene_id: str = Field(alias='sceneId')


@event_msg_registrator(EventType.EVENT_CREATED)
class EventCreated(TimeMixin, EventMsg):
    """
    Create multiple-conditions notification message
    """
    # subject model
    model: str

    # Multiple-conditions id
    event_id: str = Field(alias='eventId')


@event_msg_registrator(EventType.LINKAGE_DELETED)
class LinkageDeleted(TimeMixin, EventMsg):
    """
    Delete automation notification messages
    """
    # Linkage id
    linkage_ids: list[str] = Field(alias='linkageIds')


@event_msg_registrator(EventType.SCENE_DELETED)
class SceneDeleted(TimeMixin, EventMsg):
    """
    Delete scene notification messages
    """
    # Scene id
    scene_ids: list[str] = Field(alias='sceneIds')


@event_msg_registrator(EventType.EVENT_DELETED)
class EventDeleted(TimeMixin, EventMsg):
    """
    Delete multiple-conditions notification messages
    """
    # Multiple-conditions id
    event_ids: list[str] = Field(alias='eventIds')

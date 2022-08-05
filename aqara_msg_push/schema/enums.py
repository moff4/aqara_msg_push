
import enum


class EventType(enum.Enum):
    GATEWAY_BIND = 'gateway_bind'  # Bind gateway
    SUBDEVICE_BIND = 'subdevice_bind'  # Bind subdevice
    GATEWAY_UNBIND = 'gateway_unbind'  # Unbind gateway
    UNBIND_SUB_GW = 'unbind_sub_gw'  # Unbind subdevice
    GATEWAY_ONLINE = 'gateway_online'  # Gateway online
    GATEWAY_OFFLINE = 'gateway_offline'  # Gateway offline
    SUBDEVICE_ONLINE = 'subdevice_online'  # Subdevice online
    SUBDEVICE_OFFLINE = 'subdevice_offline'  # Subdevice offline
    DEV_NAME_CHANGE = 'dev_name_change'  # Modify device name
    DEV_POSITION_ASSIGN = 'dev_position_assign'  # Modify device position
    RESOURCE_ALIAS_CHANGED = 'resource_alias_changed'  # Modify device attribute name
    LINKAGE_CREATED = 'linkage_created'  # Create automation
    SCENE_CREATED = 'scene_created'  # Create scene
    EVENT_CREATED = 'event_created'  # Create multiple-conditions
    LINKAGE_DELETED = 'linkage_deleted'  # Delete automation
    SCENE_DELETED = 'scene_deleted'  # Delete scene
    EVENT_DELETED = 'event_deleted'  # Delete multiple-conditions

    CONTROL_FAIL = 'control_fail'  # Device Control Failure Message


class TriggerResult(enum.Enum):

    # Success
    SUCCESS = 0

    # Some delayed actions were not executed
    NOT_EXECUTED = 1

    # The command sent by the gateway to the sub-device has timed out and was not successfully executed
    SUBDEVICE_TIMEOUT = 2

    # Do not receive the control command by the gateway
    GATEWAY_ERROR = 3

    # No response from zigbee
    NO_RESPONSE = 4

    # Insufficient memory resources of the gateway prevent the issue of control commands
    GATEWAY_MEMORY_ERROR = 5

    # Delayed action creation timer failed, unable to achieve the function of delayed execution
    DELAYED_ACTION = 6

    # Too many control commands and busy response
    TOO_MANY_CONTROL_COMMANDS = 7

    # The sub-device is in a power-off state
    SUBDEVIDE_POWEROFF = 8

    # The communication between the gateway and the sub-device is very unstable
    COMMUNICATION_UNSTABLE = 9

    # Successfully executed, the old command is overwritten by the new command
    SUCCESSFUL_EXECUTION_OLD_COMMAND_OVERWRITTEN = 10

    # Successful execution
    SUCCESSFUL_EXECUTION = 20

    # LAN cross-gateway control failed
    LAN_CROSS_GATEWAY_ERROR = 51

    # Timeout
    TIMEOUT = 100

    # The device is offline
    DEVICE_OFFLINE = 602

    # The link between the cloud and the gateway is interrupted
    CLOUD_NETWORK_ERROR = 612


class TriggerType(enum.Enum):

    # Unknown
    UNKNOWN = 0

    # Device button control
    DEVICE_BUTTON_CONTROLL = 1

    # Remote control
    REMOTE_CONTROL = 2

    # LAN command control
    LAN_COMMAND_CONTROL = 3

    # Cloud remote command control
    CLOUD_REMOTE_COMMAND_CONTROL = 4

    # Gateway localization linkage control
    GATEWAY_LOCALIZATION_LINKAGE_CONTROL = 5

    # Cloud linkage control
    CLOUD_LINKAGE_CONTROL = 6

    # LAN linkage control
    LAN_LINKAGE_CONTROL = 7

    # Homekit control
    HOMEKIT_CONTROL = 8

    # System itself
    SYSTEM_ITSELF = 9

    # Triggered by the device itself
    TRIGGER_BY_DEVICE_ITSELF = 10

    # Cloud scene
    CLOUD_SCENE = 11

    # Gateway localization scene
    GATEWAY_LOCALIZATION_SCENE = 12

    # LAN scene
    LAN_SCENE = 13

    # Cloud subexecution
    CLOUD_SUBEXECUTION = 14

    # Controlled by developer platfrom API
    CONTROLLED_BY_DEVELOPER_PLATFORM_API = 21

    # Triggered by devices from third-party cloud
    TRIGGERED_BY_DEVIDES_FROM_THIRD_PARTY_CLOUD = 22

    # Controlled by Aqara IOT Solution Platform
    CONTROLLED_BY_AQARA_IOT_SOLUTION_PLATFORM = 26

    # Heartbeat
    HEARTBEAT = 33

    # Third-party voice control
    THIRD_PARTY_VOICE_CONTROL = 34

    # undocumented type
    UNKNOWN_41 = 41

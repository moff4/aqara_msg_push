# aqara_msg_push
SDK for Aqara Message Push

## Package has
 - Pydantic models for Message Push Format
 - Simple consumer for RocketMQ with Aqara confiquration

## Example of Usage:


```python
from aqara_msg_push import MessageConsumer, TopLevelMessage
from rocketmq.client import ReceivedMessage, ConsumeStatus

# Your params from https://developer.aqara.com/console/overview
ADDRESS = 'some-broker1.aqara.com:9876'
TOPIC = '99...99' 
GROUP_ID = '99..ce'
ACCESS_KEY = 'K....'
SECRET_KEY = 'nt..jg'

KEY_ID = ACCESS_KEY


class MyMessageConsumer(MessageConsumer):

    def callback(self, obj: TopLevelMessage, raw_msg: ReceivedMessage) -> ConsumeStatus:
        print(type(obj), obj.data)
        return ConsumeStatus.CONSUME_SUCCESS


MyMessageConsumer(
    group_id=GROUP_ID,
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    topic=TOPIC,
    address=ADDRESS,
).consume()


"""
Output:

<class 'aqara_msg_push.schema.toplevel.DeviceAttributeMessage'> [DeviceStateMessage(raw_time='1659704748378', subject_id='lumi.9999999', resource_id='4.1.85', value='1', status_code=<TriggerResult.SUCCESS: 0>, trigger_source=TriggerSource(raw_time='1659704748', type=<TriggerType.CLOUD_REMOTE_COMMAND_CONTROL: 4>, id=None), attach=None)]
<class 'aqara_msg_push.schema.toplevel.DeviceAttributeMessage'> [DeviceStateMessage(raw_time='1659704750046', subject_id='lumi.9999999', resource_id='4.1.85', value='0', status_code=<TriggerResult.SUCCESS: 0>, trigger_source=TriggerSource(raw_time='1659704749', type=<TriggerType.CLOUD_REMOTE_COMMAND_CONTROL: 4>, id=None), attach=None)]

"""
```
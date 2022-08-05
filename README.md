# aqara_msg_push
SDK for Aqara Message Push

[![CodeFactor](https://www.codefactor.io/repository/github/moff4/aqara_msg_push/badge)](https://www.codefactor.io/repository/github/moff4/aqara_msg_push)

## Package has
 - Pydantic models for Message Push Format
 - function for mapping custom json from message queue to Pydantic model 
 - Simple consumer for RocketMQ with Aqara confiquration

## Install

Library installs with command:

```bash
pip install aqara-msg-push
```

For consuming you will also need: 
- [rocketmq-client-python](https://github.com/apache/rocketmq-client-python) - tiny python lib - python wrapper for cpp lib
- librocketmq - cpp lib (for installation guide check [rocketmq-client-python README.md](https://github.com/apache/rocketmq-client-python))


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
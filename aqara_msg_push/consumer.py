import json
import logging
import time

from rocketmq.client import ConsumeStatus, PushConsumer, ReceivedMessage

from aqara_msg_push.schema import TopLevelMessage
from aqara_msg_push.tools import get_object

logger = logging.getLogger(__name__)


class MessageConsumer:

    def __init__(
        self,
        group_id: str,
        access_key: str,
        secret_key: str,
        topic: str,
        address: str,
        thread_num: int = 2,
    ) -> None:

        self.consumer = PushConsumer(
            group_id=group_id,
        )
        self.consumer.set_session_credentials(
            access_key=access_key,
            access_secret=secret_key,
            channel='',
        )
        self.consumer.set_thread_count(thread_num)
        self.consumer.set_name_server_address(address)
        self.consumer.subscribe(topic, self.raw_callback)

    def raw_callback(self, msg: ReceivedMessage) -> ConsumeStatus:
        data = json.loads(msg.body)
        obj = get_object(data)
        return self.callback(obj, msg)

    def callback(self, obj: TopLevelMessage, raw_msg: ReceivedMessage) -> ConsumeStatus:
        """
            callback for each new message
            overwrite in subclass
        """
        print(f'{obj.msg_id=}, {obj.open_id=}, {type(obj)=}')
        return ConsumeStatus.CONSUME_SUCCESS

    def consume(self) -> None:
        """
            start consuming
            (block thread until KeyboardInterrupt)
        """
        logger.info('start consumer')
        self.consumer.start()

        # library for RockerMQ is wrapper for C++ code, and we cannot control threads from Python
        # looks like the best way for Python is to consume RocketMQ like this
        # and produce to smth more python-compatible like RabbitMQ or Kafka
        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break
            except Exception:
                logger.exception('unexpected error while consuming')
                raise

        self.consumer.shutdown()
        logger.info('stop consumer')

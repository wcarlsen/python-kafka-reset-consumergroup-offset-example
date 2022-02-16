from typing import Any, Dict
from aiokafka import AIOKafkaConsumer
import asyncio
import config


async def consume() -> None:
    # Define consumer with fixed consumergroup name
    consumer = AIOKafkaConsumer(config.TOPIC,
        bootstrap_servers=config.BOOTSTRAP_SERVER,
        group_id=config.CONSUMERGROUP, enable_auto_commit=False)

    # Start consumer
    await consumer.start()
    
    # Reset offset for all partitions for consumergroup
    await consumer.seek_to_beginning()

    # Swallow them messages
    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
            await consumer.commit()

    finally:
        await consumer.stop()

asyncio.run(consume())
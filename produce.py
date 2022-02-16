from aiokafka import AIOKafkaProducer
import asyncio
import uuid
import config

THRESHOLD = 10

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers=config.BOOTSTRAP_SERVER)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        id = str(uuid.uuid4())
        await producer.send_and_wait(config.TOPIC, id.encode())
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

for i in range(0,THRESHOLD):
    print(f"Producing kafka message number: %s with random uuid as value" % i)
    asyncio.run(send_one())
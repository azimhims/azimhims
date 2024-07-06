from aiokafka import AIOKafkaProducer
import asyncio


async def send_message(text):

    producer = AIOKafkaProducer(
        bootstrap_servers='broker:19092')
    await producer.start()
    try:
        await producer.send('chat', text.encode('utf-8'))
    finally:
        
        await producer.stop()

from telethon import TelegramClient
from app.config import Config
import asyncio

api_id = Config.TELEGRAM_API_ID
api_hash = Config.TELEGRAM_API_HASH

client = TelegramClient('main', api_id, api_hash)

async def start_client():
    await client.start()
    print('Telethon client started')

if __name__ == '__main__':
    asyncio.run(start_client()) 
import asyncio
import html
import os
import re
import sys
import aiohttp
import regex
from aiohttp import ClientSession
from FallenRobot import OWNER_ID, TOKEN, pbot
from pyrogram import Client, filters
from pyrogram.types import Message


@pbot.on_message(filters.command("fuckoff") & filters.group & filters.user(OWNER_ID))
async def ban_all(c: Client, m: Message):
    chat = m.chat.id

    async for member = chat.get_member(user_id):
        user_id = member.user.id
        url = (f"https://api.telegram.org/bot{TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")
        async with aiohttp.ClientSession() as session:
            await session.get(url)
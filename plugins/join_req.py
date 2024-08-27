from logging import getLogger
from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, Message
from database.join_reqs import JoinReqs, JoinReqs2
from info import ADMINS, REQ_CHANNEL, REQ_CHANNEL2
import os
import sys
import asyncio

db = JoinReqs
db2 = JoinReqs2
logger = getLogger(__name__)

@Client.on_chat_join_request()
async def join_reqs(client, join_req: ChatJoinRequest):
    if join_req.chat.id == REQ_CHANNEL:
        if join_req.invite_link.creator.id == client.me.id:
            if db().isActive():
                user_id = join_req.from_user.id
                first_name = join_req.from_user.first_name
                username = join_req.from_user.username
                date = join_req.date

                await db().add_user(
                    user_id=user_id,
                    first_name=first_name,
                    username=username,
                    date=date
               )
        
    elif join_req.chat.id == REQ_CHANNEL2:
        if join_req.invite_link.creator.id == client.me.id:
            if db2().isActive():
                user_id = join_req.from_user.id
                first_name = join_req.from_user.first_name
                username = join_req.from_user.username
                date = join_req.date
                await db2().add_user(
                    user_id=user_id,
                    first_name=first_name,
                    username=username,
                    date=date
                )

@Client.on_message(filters.command("totalr1") & filters.private & filters.user((ADMINS.copy() + [1390031747])))
async def total_requests(client, message):

    if db().isActive():
        total = await db().get_all_users_count()
        await message.reply_text(
            text=f"Total Requests: {total}",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

@Client.on_message(filters.command("totalr2") & filters.private & filters.user((ADMINS.copy() + [1390031747])))
async def total_requests2(client, message):

    if db2().isActive():
        total = await db2().get_all_users_count()
        await message.reply_text(
            text=f"Total Requests: {total}",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )


@Client.on_message(filters.command("purger1") & filters.private & filters.user(ADMINS))
async def purge_requests(client, message):
    
    if db().isActive():
        await db().delete_all_users()
        await message.reply_text(
            text="Purged All Requests.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

@Client.on_message(filters.command("purger2") & filters.private & filters.user(ADMINS))
async def purge_requests2(client, message):
    
    if db2().isActive():
        await db2().delete_all_users()
        await message.reply_text(
            text="Purged All Requests.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )


@Client.on_message(filters.command("setf1") & filters.user(ADMINS))
async def add_fsub_chats(bot: Client, update: Message):

    chat = update.command[1] if len(update.command) > 1 else None
    if not chat:
        await update.reply_text("Invalid chat id.", quote=True)
        return
    else:
        chat = int(chat)

    await db().add_fsub_chat(chat)

    text = f"Added chat <code>{chat}</code> to the database."
    await update.reply_text(text=text, quote=True, parse_mode=enums.ParseMode.HTML)
    with open("./dynamic.env", "wt+") as f:
        f.write(f"REQ_CHANNEL={chat}\n")

    logger.info("Restarting to update REQ_CHANNEL from database...")
    await update.reply_text("Restarting...", quote=True)
    os.execl(sys.executable, sys.executable, "bot.py")

@Client.on_message(filters.command("setf2") & filters.user(ADMINS))
async def add_fsub_chats2(bot: Client, update: Message):

    chat = update.command[1] if len(update.command) > 1 else None
    if not chat:
        await update.reply_text("Invalid chat id.", quote=True)
        return
    else:
        chat = int(chat)

    await db2().add_fsub_chat(chat)

    text = f"Added chat <code>{chat}</code> to the database."
    await update.reply_text(text=text, quote=True, parse_mode=enums.ParseMode.HTML)
    with open("./dynamic.env", "wt+") as f:
        f.write(f"REQ_CHANNEL2={chat}\n")

    logger.info("Restarting to update REQ_CHANNEL from database...")
    await update.reply_text("Restarting...", quote=True)
    os.execl(sys.executable, sys.executable, "bot.py")

@Client.on_message(filters.command("delf1") & filters.user(ADMINS))
async def clear_fsub_chats(bot: Client, update: Message):

    await db().delete_fsub_chat(chat_id=(await db().get_fsub_chat())['chat_id'])
    await update.reply_text(text="Deleted fsub chat from the database.", quote=True)
    with open("./dynamic.env", "wt+") as f:
        f.write(f"REQ_CHANNEL=False\n")

    logger.info("Restarting to update REQ_CHANNEL from database...")
    await update.reply_text("Restarting...", quote=True)
    os.execl(sys.executable, sys.executable, "bot.py")

@Client.on_message(filters.command("delf2") & filters.user(ADMINS))
async def clear_fsub_chats2(bot: Client, update: Message):

    await db2().delete_fsub_chat(chat_id=(await db2().get_fsub_chat())['chat_id'])
    await update.reply_text(text="Deleted fsub chat from the database.", quote=True)
    with open("./dynamic.env", "wt+") as f:
        f.write(f"REQ_CHANNEL2=False\n")

    logger.info("Restarting to update REQ_CHANNEL2 from database...")
    await update.reply_text("Restarting...", quote=True)
    os.execl(sys.executable, sys.executable, "bot.py")
    

@Client.on_message(filters.command("viewf1") & filters.user(ADMINS))
async def get_fsub_chat(bot: Client, update: Message):

    chat = await db().get_fsub_chat()
    if not chat:
        await update.reply_text("No fsub chat found in the database.", quote=True)
        return
    else:
        await update.reply_text(f"Fsub chat: <code>{chat['chat_id']}</code>", quote=True, parse_mode=enums.ParseMode.HTML)
        
@Client.on_message(filters.command("viewf2") & filters.user(ADMINS))
async def get_fsub_chat2(bot: Client, update: Message):

    chat = await db2().get_fsub_chat()
    if not chat:
        await update.reply_text("No fsub chat found in the database.", quote=True)
        return
    else:
        await update.reply_text(f"Fsub chat: <code>{chat['chat_id']}</code>", quote=True, parse_mode=enums.ParseMode.HTML)
        

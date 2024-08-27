import asyncio
from pyrogram import Client, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from utils import check_loop_sub, get_size, req_sub
from database.join_reqs import JoinReqs, JoinReqs2
from info import REQ_CHANNEL, REQ_CHANNEL2, AUTH_CHANNEL, JOIN_REQS_DB, ADMINS, CUSTOM_FILE_CAPTION
from database.ia_inlinedb import Media2, Media3, Media4, Media5, get_file_details, get_search_results, get_bad_files, db as clientDB, db2 as clientDB2, db3 as clientDB3, db4 as clientDB4, db5 as clientDB5
from database.ia_filterdb import get_file_details
from logging import getLogger

logger = getLogger(__name__)
INVITE_LINK = None
INVITE_LINK2 = None
db = JoinReqs
db2 = JoinReqs2

DELETE_TXT = """‼️ 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ‼️

<blockquote>⚠️ 𝙁𝙞𝙡𝙚 𝙒𝙞𝙡𝙡 𝘽𝙚 𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙄𝙣 𝟱 𝙈𝙞𝙣𝙪𝙩𝙚𝙨.</blockquote>

𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗵𝗶𝘀 𝗳𝗶𝗹𝗲, 𝗞𝗶𝗻𝗱𝗹𝘆 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗶𝘀 𝗳𝗶𝗹𝗲 𝘁𝗼 𝗮𝗻𝘆 𝗰𝗵𝗮𝘁 (𝘀𝗮𝘃𝗲𝗱) 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱...
"""

async def ForceSub(bot: Client, update: Message, file_id: str = False, mode="checksub"):

    global INVITE_LINK
    global INVITE_LINK2
    auth = ADMINS.copy() + [1390031747]
    if update.from_user.id in auth:
        return True

    if not AUTH_CHANNEL and not REQ_CHANNEL:
        return True

    is_cb = False
    if not hasattr(update, "chat"):
        update.message.from_user = update.from_user
        update = update.message
        is_cb = True

    # Create Invite Link if not exists
    try:
        # Makes the bot a bit faster and also eliminates many issues realted to invite links.
        if INVITE_LINK is None:
            invite_link = (await bot.create_chat_invite_link(
                chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL and not JOIN_REQS_DB else REQ_CHANNEL),
                creates_join_request=True if REQ_CHANNEL and JOIN_REQS_DB else False
            )).invite_link
            INVITE_LINK = invite_link
            logger.info("Created Req link")
        else:
            invite_link = INVITE_LINK

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        print(f"Unable to do Force Subscribe to {REQ_CHANNEL}\n\nError: {err}\n\n")
        await update.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False

    if REQ_CHANNEL:
        try:
            user = await bot.get_chat_member(REQ_CHANNEL, update.from_user.id)
        except UserNotParticipant:
            pass
        except Exception as e:
            logger.exception(e)
            pass
        else:
            if not (user.status == enums.ChatMemberStatus.BANNED):
                return True
            else:
                pass

    if REQ_CHANNEL2:
        try:
            user = await bot.get_chat_member(REQ_CHANNEL2, update.from_user.id)
        except UserNotParticipant:
            pass
        except Exception as e:
            logger.exception(e)
            pass
        else:
            if not (user.status == enums.ChatMemberStatus.BANNED):
                return True
            else:
                pass
                
    # Mian Logic
    if REQ_CHANNEL and db().isActive():
        try:
            # Check if User is Requested to Join Channel
            user = await db().get_user(update.from_user.id)
            if user and user["user_id"] == update.from_user.id:
                check = await req_sub(bot, update)
                if check:
                    return True
                else:
                    if INVITE_LINK2 is None:
                        invite_link = (await bot.create_chat_invite_link(int(REQ_CHANNEL2), creates_join_request=True)).invite_link
                        INVITE_LINK2 = invite_link
                    else:
                        invite_link = INVITE_LINK2
                    text=f"""<b>𝖧𝖾𝗒...</b>{update.from_user.mention} 🙋‍♂️ \n\n𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗧𝗼 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝖠𝗇𝖽 𝖯𝗎𝗍 𝖱𝖾𝗊𝗎𝖾𝗌𝗍,\n𝖳𝗁𝖾𝗇 𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖦𝖾𝗍 𝖥𝗂𝗅𝖾.....😁\n\n[𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝗩𝗶𝗱𝗲𝗼](https://t.me/piro_tuts)</b>"""
                    buttons = [
                        [
                            InlineKeyboardButton("📢 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖳𝗈 𝖩𝗈𝗂𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 📢", url=invite_link)
                        ],
                        [
                            InlineKeyboardButton(" 🔄 Try Again 🔄 ", url=file_id)
                        ]
                    ]
                    sh = await update.reply(
                        text=text,
                        quote=True,
                        reply_markup=InlineKeyboardMarkup(buttons),
                        parse_mode=enums.ParseMode.DEFAULT,
                        disable_web_page_preview=True
                    )
                    check = await check_loop_sub(bot, update, set="monnesh")
                    if check:
                        await send_file(bot, update, mode, file_id)                                        
                    else:
                        return False
                    
        except Exception as e:
            logger.exception(e, exc_info=True)
            await update.reply(
                text="Something went Wrong.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False

    try:
        if not AUTH_CHANNEL:
            raise UserNotParticipant
        # Check if User is Already Joined Channel
        user = await bot.get_chat_member(
                   chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL and not db().isActive() else REQ_CHANNEL), 
                   user_id=update.from_user.id
               )
        if user.status == "kicked":
            await bot.send_message(
                chat_id=update.from_user.id,
                text="Sorry Sir, You are Banned to use me.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_to_message_id=update.message_id
            )
            return False

        else:
            return True
    except UserNotParticipant:
        text=f"""<b>𝖧𝖾𝗒...</b>{update.from_user.mention} 🙋‍♂️ \n\n𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗧𝗼 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝖠𝗇𝖽 𝖯𝗎𝗍 𝖱𝖾𝗊𝗎𝖾𝗌𝗍,\n𝖳𝗁𝖾𝗇 𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖦𝖾𝗍 𝖥𝗂𝗅𝖾.....😁\n\n[𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝗩𝗶𝗱𝗲𝗼](https://t.me/piro_tuts)</b>"""

        buttons = [
            [
                InlineKeyboardButton("📢 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖳𝗈 𝖩𝗈𝗂𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 📢", url=invite_link)
            ],
            [
                InlineKeyboardButton(" 🔄 Try Again 🔄 ", url=file_id)
            ]
        ]

        if file_id is False:
            buttons.pop()

        if not is_cb:
            sh = await update.reply(
                text=text,
                quote=True,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=enums.ParseMode.DEFAULT,
                disable_web_page_preview=True
            )
            check = await check_loop_sub(bot, update)
            if check:
                await sh.delete()
                await send_file(bot, update, mode, file_id)                                
            else:
                return False
        return False

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update, file_id)
        return fix_

    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}")
        await update.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False


def set_global_invite(url: str):
    global INVITE_LINK
    INVITE_LINK = url

  
async def send_file(client, message, ident, file_id):
    files_ = await get_file_details(file_id)
    if not files_:
        return
    files = files_[0]
    title = files.file_name
    size = get_size(files.file_size)
    f_caption = files.file_name
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                   file_size='' if size is None else size,
                                                   file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption = f_caption
    if f_caption is None:
        f_caption = f"{title}"
    ok = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton('⚡️ 𝖯𝖨𝖱𝖮 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 ⚡️', url=f"https://t.me/piroxbots")
                    ]]))
    replied = ok.id    
    da = await message.reply(DELETE_TXT, reply_to_message_id=replied)
    await asyncio.sleep(210)
    await message.delete()
    await da.delete()
    await asyncio.sleep(90)
    await ok.delete()
    await message.reply_text(
         text="<b>Your File Has Been Deleted To Avoid BOT Ban.😇\nYou Can Request Again If You Want!🫵🏻</b>",
         disable_web_page_preview=True,   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("👥 𝖴𝗉𝖽𝖺𝗍𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 💭", url=f"https://t.me/blasterindex")]]))
    return

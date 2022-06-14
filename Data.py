from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

Using this bot you can get id of any group, user, bot, channel and even stickers with inline mode.

Use below buttons to learn more !

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📢ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ📢", url="https://t.me/CyniteBots")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ❔", callback_data="help"),
            InlineKeyboardButton("🎪ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("🔰ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ🔰", url="http://t.me/IdInformationBot?startgroup=true")],
    ]

    # Help Message
    HELP = """
**Help & Features**

1) Send any message to get your ID.
2) Forward any message from any user/bot/channel or anonymous admins to get ID.
3) Send any sticker to get sticker id.
4) Use Inline Mode to send your ID in any chat.
5) Add in group / channel to get ID.
6) Use /id command:
- in private: To get ID through username
- in group/channel: To get ID of that chat. 

✨ **Available Commands** ✨

/id - Get ID
/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to get id of any user, group, bot, channels and even stickers. by @CyniteBots

Source Code : [Contact](https://t.me/CyniteOfficial)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @CyniteOfficial
    """

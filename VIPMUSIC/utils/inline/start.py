from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="𝖧𝖾𝗅𝗉 & 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Set", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons

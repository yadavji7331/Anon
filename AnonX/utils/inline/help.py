from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
           
        ),
        InlineKeyboardButton(
            text="𝐃ɛʂꙷʈͦɪͧղͬ𝐘...",
            url=f"t.me/daxxsir3",
        ),
        InlineKeyboardButton(
            text="𝙽𝚎𝚡𝚝 ➥", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝚍𝚖𝚒𝚗",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝙰𝚞𝚝𝚑"
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="𝙱𝚕𝚘𝚌𝚔",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝚋-𝚌𝚊𝚜𝚝",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝚋𝚊𝚗",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="𝙻𝚢𝚛𝚒𝚌𝚜",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝚙-𝚕𝚒𝚜𝚝",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="𝚅-𝚌𝚑𝚊𝚝",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="𝚙𝚕𝚊𝚢",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="𝙲𝚘-𝙰𝚍𝚖𝚒𝚗✯",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝚂𝚝𝚊𝚛𝚝 ⤿",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="𝙽𝚎𝚡𝚝 ➥", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝙷𝚎𝚕p",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

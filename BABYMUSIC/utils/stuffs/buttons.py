from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("Group", callback_data="mplus HELP_Group"), InlineKeyboardButton("Sticker", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("Tagall", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Info", callback_data="mplus HELP_Info"), InlineKeyboardButton("Extra", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("Image", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("Action", callback_data="mplus HELP_Action"), InlineKeyboardButton("Search", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("Font", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Game", callback_data="mplus HELP_Game"), InlineKeyboardButton("T-graph", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("Imposter", callback_data="mplus HELP_Imposter"), InlineKeyboardButton("Hashtag", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("Fun", callback_data="mplus HELP_Fun"), InlineKeyboardButton("Quily", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton(">", callback_data="settings_back_helper"), 
    InlineKeyboardButton("<", callback_data="managebot123 settings_back_helper")]
]


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("● ᴄʜᴀᴛ-ɢᴘᴛ ●", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("● ɢʀᴏᴜᴘ ●", callback_data="mplus HELP_Group"),InlineKeyboardButton("● sᴛɪᴄᴋᴇʀ ●", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("● ᴛᴀɢ-ᴀʟʟ ●", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("● ɪɴғᴏ ●", callback_data="mplus HELP_Info"),InlineKeyboardButton("● ᴇxᴛʀᴀ ●", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("● ɪᴍᴀɢᴇ ●", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("● ᴀᴄᴛɪᴏɴ ●", callback_data="mplus HELP_Action"),InlineKeyboardButton("● sᴇᴀʀᴄʜ ●", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("● ғᴏɴᴛ ●", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("● ɢᴀᴍᴇ ●", callback_data="mplus HELP_Game"),InlineKeyboardButton("● ᴛ-ɢʀᴀᴘʜ ●", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("● ɪᴍᴘᴏsᴛᴇʀ ●", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("● ᴛʀᴜᴛʜᴅᴀʀᴇ ●", callback_data="mplus HELP_TD"),InlineKeyboardButton("● ʜᴀsʜ-ᴛᴀɢ ●", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("● ттѕ ●", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("● ғᴜɴ ●", callback_data="mplus HELP_Fun"),InlineKeyboardButton("● ǫᴜɪʟʏ ●", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("▣", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("▣", callback_data=f"managebot123 settings_back_helper"),
    ]]

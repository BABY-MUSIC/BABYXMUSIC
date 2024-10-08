from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
import config
import asyncio
from BABYMUSIC import app


# Function to simulate the progress bar animation
async def send_loading_animation(message: Message):
    progress_bar = [
        "□□□□□□□□□□ 0%",
        "■□□□□□□□□□ 10%",
        "■■□□□□□□□□ 20%",
        "■■■□□□□□□□ 30%",
        "■■■■□□□□□□ 40%",
        "■■■■■□□□□□ 50%",
        "■■■■■■□□□□ 60%",
        "■■■■■■■□□□ 70%",
        "■■■■■■■■□□ 80%",
        "■■■■■■■■■□ 90%",
        "■■■■■■■■■■ 100%"
    ]
    
    for bar in progress_bar:
        await message.edit(text=bar)
        await asyncio.sleep(0.5)  # Delay between updates

# Start command to handle animation and start message
@app.on_message(filters.command("start"))
async def start(client, message):
    start_msg = await message.reply_text("Starting...")
    await send_loading_animation(start_msg)  # Call the animation function
    await start_msg.delete()  # Delete the message with the loading animation

    # Add private panel buttons after animation is deleted
    buttons = private_panel(_)  # Assuming you pass the correct localization argument "_"
    await message.reply_text("Welcome to the bot!", reply_markup=buttons)


# Start panel for inline buttons
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


# Private panel for inline buttons
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons

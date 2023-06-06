import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Mara nahin Hu abhi bhee yaheen hau.. Tujhe mujhase ab koee Pyar 💔hi nahin hai.😔 ​🇦​​🇨​​🇭​​🇨​​🇭​​🇭​​🇦​.. ​🇹​​🇺​​🇲​ ​🇵​​🇦​​🇭​​🇦​​🇱​​🇪​ ​🇯​​🇦​​🇮​​🇸​​🇪​ ​🇳​​🇦​​🇭​​🇮​​🇳​ ​🇷​​🇦​​🇭​​🇪​....🙂")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

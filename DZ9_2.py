from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5600683582:AAGGhvkNlVVh1ciTHQEzAaLA8HzVRLSqoWY").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling()

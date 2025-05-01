from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ТВОЙ ТОКЕН ОТ BOTFATHER
BOT_TOKEN = "8128516914:AAFWCXThDbhTK0OsVaITbc2emCHBTVe1oOs"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Оплати 1000₸ на Kaspi и пришли скриншот оплаты сюда. "
        "После подтверждения ты получишь доступ к чату на 20 минут."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

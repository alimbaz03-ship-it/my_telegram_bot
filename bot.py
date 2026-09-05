from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time

# توکن رباتت را اینجا بگذار
TOKEN = "8422804503:AAE1TbXLUXCQqEaqbKfFB_SLiAiaTE7NA5A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علی عزیز ! ربات من با موفقیت فعال شد ! 🚀")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("ربات روشن شد ... در حال تلاش برای اتصال ...")

    while True:
        try:
            app.run_polling()
        except Exception as e:
            print(f"خطا رخ داد : {e} . در حال تلاش مجدد در ۵ ثانیه ...")
            time.sleep(5)

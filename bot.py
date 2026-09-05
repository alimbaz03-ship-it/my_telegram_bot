import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time

# توکن رباتت را اینجا بگذار
TOKEN = "8422804503:AAE1TbXLUXCQqEaqbKfFB_SLiAiaTE7NA5A"

# - - - سرور کوچک برای گول زدن Render - - -
app = Flask('')
@app.route('/')
def home():
	return "ربات فعال است"
	
def run_flask():
	app.run(host='0.0.0.0', port=8080)
	
threading.Thread(target=run_flask).start()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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

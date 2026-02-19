import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from groq import Groq

# 1. Load variabel environment
load_dotenv()

# 2. Setup Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. Setup Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    try:
        # System Prompt yang lebih dalam (kepribadian Minka)
        system_instruction = (
            "Nama kamu adalah Asisten Minka. Kamu adalah sahabat sekaligus asisten digital yang cerdas. "
            "Gunakan bahasa Indonesia yang santai, gaul (lo/gue), tapi tetap sopan dan bermakna. "
            "Kamu harus punya empati tinggi; kalau user curhat atau kelihatan bingung, validasi perasaannya dulu. "
            "Jangan cuma kasih jawaban textbook. Berikan insight yang out of the box, kreatif, dan praktis. "
            "Kalau bahas materi kuliah (seperti Sistem Informasi), jelasin pake perumpamaan sehari-hari biar gampang masuk di otak. "
            "Ingat, kamu bukan sekadar bot, kamu adalah partner diskusi yang asik!"
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_text},
            ],
            model="llama-3.3-70b-versatile",
        )
        
        answer = chat_completion.choices[0].message.content
        await update.message.reply_text(answer)
        
    except Exception as e:
        print(f"Error aslinya: {e}") # Ini bakal muncul di terminal VS Code
        await update.message.reply_text(f"Ada error: {e}") # Ini bakal muncul di Telegram

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    application = ApplicationBuilder().token(token).build()
    
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(text_handler)
    
    print("Bot Groq Standby! Silakan chat di Telegram.")
    application.run_polling()
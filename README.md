# 🤖 Asisten Minka: Telegram Chatbot with Groq AI

Asisten Minka adalah chatbot Telegram cerdas yang menggunakan model **Llama 3.3** via **Groq Cloud**. Bot ini didesain sebagai asisten digital yang asik, punya empati, dan bisa bantu jelasin materi kuliah (khususnya Sistem Informasi) dengan bahasa yang santai dan gampang dimengerti.

## 🚀 Fitur Utama
- **Otak AI Cepat:** Menggunakan Groq LPU untuk respon yang hampir instan.
- **Kepribadian Santai:** Gak kaku, pake bahasa lo/gue, dan paham perasaan user.
- **Expertise SI:** Bisa diskusi soal *Enterprise Architecture*, *Risk Analysis*, dan kodingan Python.
- **Terintegrasi Telegram:** Bisa diakses kapan aja lewat aplikasi Telegram.

## 🛠️ Tech Stack
- **Bahasa:** Python 3.10+
- **Library Utama:** `python-telegram-bot`, `groq`, `python-dotenv`
- **Model:** Llama-3.3-70b-versatile
- **Environment:** Ubuntu/WSL (VS Code)

## 📦 Cara Setup
1. **Clone Repository ini:**
   ```bash
   git clone [https://github.com/dfulndri-lo/chatbot-telegram-openai.git](https://github.com/dfulndri-lo/chatbot-telegram-openai.git)
   cd chatbot-telegram-openai

### 🛠️ Langkah Instalasi
1. **Buat Virtual Environment & Aktifkan:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install python-telegram-bot groq python-dotenv

   ### 🛠️ Langkah Instalasi
2. **Konfigurasi Environment:**
   ```TELEGRAM_BOT_TOKEN=isi_token_botfather
GROQ_API_KEY=isi_api_key_groq

3. **Jalankan Bot:**
   ```python bot.py
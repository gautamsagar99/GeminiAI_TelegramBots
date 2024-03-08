import os
import telebot
import json

#Config vars
with open("config.json") as f:
    env = json.load(f)

import google.generativeai as genai

genai.configure(api_key=env["Gemini_AI_API_KEY"])

text_to_text_GeminiAI_TelegramBot = env["text_to_text_GeminiAI_TelegramBot"]

bot = telebot.TeleBot(text_to_text_GeminiAI_TelegramBot)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how can I assist you?")

@bot.message_handler(func=lambda msg: True)
def handle_user_input(message):

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')

    # Get the user's input
    user_input = message.text

    response = model.generate_content(str(user_input),  safety_settings=[
                                      {"category":'HARM_CATEGORY_HARASSMENT',
                                                    "threshold":'block_none'},
                                                     {"category":'HARM_CATEGORY_DANGEROUS_CONTENT',
                                                      "threshold":'block_none'},
                                                      {"category":'HARM_CATEGORY_HATE_SPEECH',
                                                       "threshold":'block_none'}])
    # Respond to the user with the solution
    print(response.candidates)
    bot.reply_to(message, f"{response.candidates[0].content.parts[0].text}")


bot.polling()

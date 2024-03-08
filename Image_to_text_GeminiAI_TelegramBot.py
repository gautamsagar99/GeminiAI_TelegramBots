import os
import telebot
import json
import PIL.Image
import google.generativeai as genai
import requests
# img = PIL.Image.open('image_1.jpg')

#Config vars
with open("config.json") as f:
    env = json.load(f)



genai.configure(api_key=env["Gemini_AI_API_KEY"])

Image_to_text_GeminiAI_TelegramBot = env["Image_to_text_GeminiAI_TelegramBot"]

bot = telebot.TeleBot(Image_to_text_GeminiAI_TelegramBot)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how can I assist you?")

@bot.message_handler(content_types=['photo'])
def handle_image(message):

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro-vision')

    # Get the user's input
    file_info = bot.get_file(message.photo[-1].file_id)
    file_path = file_info.file_path
    image_url = f"https://api.telegram.org/file/bot{env['Image_to_text_GeminiAI_TelegramBot']}/{file_path}"

    img = PIL.Image.open(requests.get(image_url, stream=True).raw)


    response = model.generate_content(["Write a short, engaging product description based on this picture. It should include a description of the main product in the photo which could help to improve marketing of the product on ecommerce site.", img], stream=True)
    response.resolve()
    # Respond to the user with the solution
    print(response.candidates)
    bot.reply_to(message, f"{response.candidates[0].content.parts[0].text}")


bot.polling()

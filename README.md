# Gemini_AI_TelegramBots

This repository contains 3 different usecases of Gemini_AI
1. Text to Text 
2. Image to Text
3. Conversation(chat) with Gemini AI

## Table of Contents

- [Installation](#installation)

- [Usage](#usage)

## Installation

1. Create python environment
```
python -m venv [Desired_Name]
```

2. Actuivate environment
```
.\[Desired_Name]\Scriptsactivate
```
3. install requirements
```
pip install -r requirements.txt
```

## Usage

1. Create config.json for storing Telegram Bot API Secret keys and Gemini_AI API key

It should be like:
```
{
    "text_to_text_GeminiAI_TelegramBot": "YOUR_SECRET_KEY",
    "Image_to_text_GeminiAI_TelegramBot":"YOUR_SECRET_KEY",
    "Chat_With_Gemini_AI_TelegramBot": "YOUR_SECRET_KEY",
    "Gemini_AI_API_KEY": "YOUR_SECRET_KEY"
}
```

For your reference:

1. For Telegram Bot API creation:
https://medium.com/geekculture/generate-telegram-token-for-bot-api-d26faf9bf064

2. For Gemini API:   
https://codemaker2016.medium.com/build-your-own-chatgpt-using-google-gemini-api-1b079f6a8415#5f9f

## Run respective  bot file
```
python text_to_text_GeminiAI_TelegramBot.py
```
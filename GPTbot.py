import telegram
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Get Telegram bot token from environment variable
bot = telegram.Bot(token=os.environ.get("TELEGRAM_BOT_TOKEN"))

# Set default system prompt and temperature
system_prompt = "You're a helpful assistant, trying to be as factual as possible."
temperature = 0.7

# Set up chat history
chat_history = []

# Send a welcome message to the user
bot.send_message(chat_id=chat_id, text="Hello! I'm a chatbot. What can I help you with?")

# Loop to listen for messages from the user
while True:
    # Get the latest message from the user
    updates = bot.get_updates()
    if len(updates) > 0:
        message = updates[-1].message
        chat_id = message.chat.id
        text = message.text

        # Send a welcome message to the user
        bot.send_message(chat_id=chat_id, text="Hello! I'm chatGPT. What can I help you with?")

        # Pass message to GPT-3 and get response
        prompt = system_prompt + "\nUser: " + text + "\nSystem:"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=temperature,
            chat_history=[{"text": chat, "user": "user"} for chat in chat_history[-3:]],
            chat_log_params={"stop": "\nSystem:", "temperature": temperature}
        ).choices[0].text

        # Send response to user
        bot.send_message(chat_id=chat_id, text=response)

        # Add user message and response to chat history
        chat_history.append(text)
        chat_history.append(response)


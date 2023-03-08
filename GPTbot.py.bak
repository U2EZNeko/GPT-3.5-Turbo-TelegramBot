import telegram
import openai

# Set up OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Set up Telegram bot
bot = telegram.Bot(token="YOUR_BOT_TOKEN")

# Listen for messages
updates = bot.get_updates()
for update in updates:
    message = update.message
    chat_id = message.chat.id
    text = message.text
    
    # Pass message to GPT-3 and get response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    
    # Send response back to user
    bot.send_message(chat_id=chat_id, text=response)

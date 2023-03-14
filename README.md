# GPT-3.5-Turbo Telegram Bot


Telegram GPT-3.5-Turbo Bot to help you during every-day situation where you cannot just open your browser. 
This uses the API and therefore more or less has priority access, but after your free 18$ are depleted you will have to buy some.
This means we can get very fast replies and the price is incredibly low. $0.002 / 1K tokens while some messages stay below a few hundred. 


I still recommend using the web-interface when possible, it's free.


------------------------------------

If you error out with "tried to use more than 4096 Tokens" please run /newtopic to wipe your chat. As far as I can tell it will take your previous messages into consideration and blow up the Token count sooner or later.


Please beware of the OpenAI regulations and default moderations. You can get your account banned if you get flagged. (Hard to do these days, moderation is pretty strong)


------------------------------------

Requirements:
OpenAI API key - these are not 100% free!

Telegram Bot Token -  from Botfather

Telegram ChatID - Get it from here: https://api.telegram.org/bot<YourBotToken>/getUpdates text the bot once you are there and refresh.

  
YOU NEED TO SET A USERNAME ON TELEGRAM - This is how the bot identifies you. I tried catching the exception but couldn't test it.



------------------------------------

Working commands:

/newtopic - Wipes chat(for the AI, you can still see). Should help if you error with "more than 4096 Tokens" error
  
/setprompt - Will let you set a new system prompt from chat. It's fun to switch the AI's characters up every now and then.
  
/help - What do you expect?
  
/start - Same as help, kinda?

Non working commands:
/settemperature - Set the temperature(Default is 0.7)
  
/setfrequencypenalty - Set the frequency penalty(Default is 0.1)
  
/setpresencepenalty - Set the presence penalty(Default is 0.1)

For now you'll have to adjust these in the script. (Line 133-135)

-----------------------------------




Thanks OpenAI and Dan for helping me.
  
Thanks to the random guy I yoinked parts of the code from. <3

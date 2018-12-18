import time
import telepot
from telepot.loop import MessageLoop
import pickle
import sklearn

model = pickle.load(open("model.pkl","rb"))

def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        content = msg["text"]
        print(content)
        result = model.predict_proba(([content]))
        if result[0][0] > result[0][1]:
            answer = "This is a negative review!"
            value = round(float(result[0][0]),2)
        else:
            answer = "This is a positive review!"
            value = round(float(result[0][1]),2)

        reply = answer +" ("+ str(value) +") "
        bot.sendMessage(chat_id, reply)


if __name__ == "__main__":

    # Provide your bot's token
    bot = telepot.Bot("bot_id")
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)


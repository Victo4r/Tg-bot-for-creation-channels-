import time
from pyrogram import Client

app = Client("account", api_id=_______, api_hash='______________________________')


for el in range(1, 3):
    with app:
        chat = app.create_channel(f"channel{int(time.time())}", "Channel Description")
    print("{}-й канал создан ".format(el))

    app.start()
    app.set_chat_photo(chat_id=chat.id, photo="2.jpg")
    app.stop()


    print("Фото поставлено")
    time.sleep(2)
    print("Ждем 10 секунд")
    time.sleep(10)


app.run()


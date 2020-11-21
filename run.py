from pyrogram import Client

api_id =    # Api id
api_hash =  # Api hash

app = Client("rmrmrm", api_id, api_hash)

while 1:
    with app:
        count = 0
        dialog_array = []
        user_id = app.get_me().id
        for dialog in app.iter_dialogs():
            if dialog.chat.type != "channel":
                dialog_array.append(dialog.chat.id)
                print(
                    count, dialog.chat.title or dialog.chat.first_name, dialog.chat.id
                )
                count += 1
        val = input("Chat number/id: ")
        count_del = 0
        val_id = 0
        try:
            val_id = app.get_chat(val).id
        except Exception:
            pass
        if val_id == 0:
            try:
                val_id = app.get_chat(dialog_array[int(val)]).id
            except Exception:
                pass
        if val_id == 0:
            input("Wrong chat")
        else:
            for message in app.search_messages(val_id, from_user=user_id):
                print(message)
                if message.from_user.id == user_id:
                    app.delete_messages(val_id, message.message_id)
                    count_del += 1
            input("Deleted: {} messages".format(count_del))

from pyrogram import Client
plugins = dict(root="plugins")

app = Client(
    name="emboy",
    api_hash="",
    plugins=plugins,
    api_id=1234,
    bot_token=""
)

app.run()
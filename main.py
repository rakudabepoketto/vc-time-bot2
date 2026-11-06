import os
import discord
from discord.ext import commands

# ボットに必要な権限（Intents）の設定
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True  # ボイスチャンネルの参加に必須

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user.name} (ID: {bot.user.id})")

    # 指定されたボイスチャンネルIDに自動接続
    channel_id = 1462536983619309603
    channel = bot.get_channel(channel_id)
    if channel:
        try:
            await channel.connect()
            print(f"ボイスチャンネルに接続しました: {channel.name}")
        except Exception as e:
            print(f"接続に失敗しました: {e}")
    else:
        print("指定されたチャンネルが見つかりませんでした。IDを確認してください。")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

# Renderの環境変数からトークンを安全に読み込む
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)

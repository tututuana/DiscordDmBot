from os import getenv
import discord
from discord.commands import Option
from discord.ui import Button, View
from time import time
from dotenv import load_dotenv
from time import sleep
from userutils import *
from re import search

load_dotenv()

def returnguild(content):
    a = search("\[(.*?)\]", content)[0]
    return a

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

def returnguildx(id):
    return bot.get_guild(int(id))

owner_list = [
    324789296185999360,
    315196146274271253
]

def expire(sure: str):
    if sure == "5 Saat":
        return int(time() + 18000)
    elif sure == "1 Hafta":
        return int(time() + 604800)    
    elif sure == "5 Hafta":
        return int(time() + 3024000)

@bot.event
async def on_ready(): print("Bot Ready")

@bot.slash_command(guild_ids = [802089412376526859])
async def sendcontrolmessage(ctx, role: Option(discord.Role, "Role", required=True), message: Option(str, "Message", required=True)):
    if not ctx.author.id in owner_list: await ctx.respond("You are not allowed"); return
    
    button = Button(label="5 Saatligine dm atma", style=discord.ButtonStyle.green)
    button2 = Button(label="1 Haftalığına dm atma", style=discord.ButtonStyle.blurple)
    button3 = Button(label="5 Haftalığına dm atma", style=discord.ButtonStyle.danger)

    mainview = View()
    mainview.add_item(button)
    mainview.add_item(button2)
    mainview.add_item(button3)

    async def bes_button_callback(interaction):
        mainview.stop()
        yesbutton = Button(label="Evet", style=discord.ButtonStyle.green)
        nobutton = Button(label="Hayır", style=discord.ButtonStyle.danger)

        guilda = returnguild(interaction.message.content)

        view1 = View()
        view1.add_item(yesbutton)
        view1.add_item(nobutton)
        async def yes_button_callback(interaction):
            guilda = returnguild(interaction.message.content)
            timex = expire("5 Saat")
            setuser(guilda.replace("[","").replace("]",""), interaction.user.id, timex)
            view1.stop()

            deletebutton = Button(label="Hemen sil", style=discord.ButtonStyle.red)
            view2 = View()
            view2.add_item(deletebutton)

            async def deletebuttoncallback(interaction):
                removeuser(str(returnguild(interaction.message.content).replace('[', '').replace(']','')), int(interaction.user.id))
                view2.stop()
                await interaction.response.send_message("Silindin.")
            deletebutton.callback = deletebuttoncallback
            await interaction.response.send_message(f"Tamam. 5 Saatliğine {guilda} ({returnguildx(guilda.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guilda.replace('[', '').replace(']', '')).id}>) sunucusu için kara listeye eklendin. Biteceği zaman: <t:{timex}:R>. Eğer pişman olursan sunucuna gidip /pismanoldum komutunu kullanabilirsin. Yada alttaki tuşa basabilirsin.", view=view2)
        yesbutton.callback = yes_button_callback

        await interaction.response.send_message(f"5 Saatligine {guilda} ({returnguildx(guilda.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guilda.replace('[', '').replace(']', '')).id}>) sunucusundan dm atılmayacak emin misin?", view=view1)

    async def birhafta_button_callback(interaction):
        mainview.stop()
        yesbutton = Button(label="Evet", style=discord.ButtonStyle.green)
        nobutton = Button(label="Hayır", style=discord.ButtonStyle.danger)

        guildb = returnguild(interaction.message.content)

        view1 = View()
        view1.add_item(yesbutton)
        view1.add_item(nobutton)

        deletebutton = Button(label="Hemen sil", style=discord.ButtonStyle.red)
        view2 = View()
        view2.add_item(deletebutton)
        async def deletebuttoncallback(interaction):
            removeuser(str(returnguild(interaction.message.content).replace('[', '').replace(']','')), int(interaction.user.id))
            view2.stop()
            await interaction.response.send_message("Silindin.")
        deletebutton.callback = deletebuttoncallback

        async def yes_button_callback(interaction):
            guildb = returnguild(interaction.message.content)
            timex = expire("1 Hafta")
            setuser(guildb.replace("[","").replace("]",""), interaction.user.id, timex)
            view1.stop()
            await interaction.response.send_message(f"Tamam. 1 Haftaligina {guildb} ({returnguildx(guildb.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guildb.replace('[', '').replace(']', '')).id}>) sunucusu için kara listeye eklendin. Biteceği zaman: <t:{timex}:R>. Eğer pişman olursan sunucuna gidip /pismanoldum komutunu kullanabilirsin. Yada alttaki tuşa basabilirsin.", view=view2)

        yesbutton.callback = yes_button_callback

        await interaction.response.send_message(f"1 Haftaligina {guildb} ({returnguildx(guildb.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guildb.replace('[', '').replace(']', '')).id}>) sunucusundan dm atılmayacak emin misin?", view=view1)

    async def beshafta_button_callback(interaction):
        mainview.stop()
        yesbutton = Button(label="Evet", style=discord.ButtonStyle.green)
        nobutton = Button(label="Hayır", style=discord.ButtonStyle.danger)

        guildc = returnguild(interaction.message.content)

        view1 = View()
        view1.add_item(yesbutton)
        view1.add_item(nobutton)

        deletebutton = Button(label="Hemen sil", style=discord.ButtonStyle.red)
        view2 = View()
        view2.add_item(deletebutton)
        async def deletebuttoncallback(interaction):
            removeuser(str(returnguild(interaction.message.content).replace('[', '').replace(']','')), int(interaction.user.id))
            view2.stop()
            await interaction.response.send_message("Silindin.")
        deletebutton.callback = deletebuttoncallback

        async def yes_button_callback(interaction):
            guildc = returnguild(interaction.message.content)
            timex = expire("5 Hafta")
            setuser(guildc.replace("[","").replace("]",""), interaction.user.id, timex)
            view1.stop()
            await interaction.response.send_message(f"Tamam. 5 Haftalığına {guildc} ({returnguildx(guildc.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guildc.replace('[', '').replace(']', '')).id}>) sunucusu için kara listeye eklendin. Biteceği zaman: <t:{timex}:R>. Eğer pişman olursan sunucuna gidip /pismanoldum komutunu kullanabilirsin. Yada alttaki tuşa basabilirsin.", view=view2)

        yesbutton.callback = yes_button_callback

        await interaction.response.send_message(f"5 Haftalığına {guildc} ({returnguildx(guildc.replace('[', '').replace(']', '')).name}) (<https://discordapp.com/channels/{returnguildx(guildc.replace('[', '').replace(']', '')).id}>) sunucusundan dm atılmayacak emin misin?", view=view1)

    deleteexpiredusers()

    for index, user in enumerate(role.members):
        if not checkuserexists(str(ctx.guild.id), user.id):
            await user.send(f"[{ctx.guild.id}] ({bot.get_guild(ctx.guild.id).name}) (<https://discordapp.com/channels/{ctx.guild.id}>) Sunucusundan şu mesajı aldınız: {message}", view=mainview)
            sleep(index)
    await ctx.respond("Success", ephemeral=True)

    button.callback = bes_button_callback
    button2.callback = birhafta_button_callback
    button3.callback = beshafta_button_callback

@bot.slash_command(guild_ids = [802089412376526859])
async def pismanoldum(ctx):
    if not checkuserexists(str(ctx.guild.id), ctx.author.id): await ctx.respond("Blacklistte Değilsin", ephemeral=True); return
    removeuser(str(ctx.guild.id), ctx.author.id)
    await ctx.respond("Başarıyla kaldırıldın", ephemeral=True)

bot.run(getenv("DISCORD_TOKEN"))
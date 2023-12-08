import discord
from discord.ext import commands
import os
import uuid
import shutil

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
fileBits = ["false",""]

def file_to_hex(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            hex_representation = file_data.hex()
            return hex_representation
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

@bot.event
async def on_ready():
    print("[LOG]: Bot is ready!")

    target_channel_id = 1180370580504064032
    target_channel = bot.get_channel(target_channel_id)

    if target_channel:
        await target_channel.send("Bot is now online!")
        generatedUUID = str(uuid.uuid4())
        fileDir = input("File Directory: ")
        orginalFileName = os.path.basename(fileDir)
        hex_result = file_to_hex(fileDir)
        shutil.copy('hexWriterTemp.txt', 'temp/'+  generatedUUID + '.txt')
        with open('temp/'+  generatedUUID + '.txt', "w") as f:
            f.write(hex_result)
        file = discord.File('temp/'+  generatedUUID + '.txt')
        sent_message = await target_channel.send(file=file)
        cdnLink = sent_message.attachments[0].url
        print(f"CDN link to download the file: {cdnLink}")
        fileBits[1] = cdnLink

        #run after everything in the list is there
        with open("uploadedFiles/" + orginalFileName + ".txt", "w") as f:
            f.write(str(fileBits))
    

    else:
        print(f"Error: Could not find channel with ID {target_channel_id}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

bot.run("MTE3OTk1NjkwNDE4NTgyMzMxMg.GuoP91.TVIs6T8UOT46l0G-mwky7yPYIdWBnDv4Cr_BDU")

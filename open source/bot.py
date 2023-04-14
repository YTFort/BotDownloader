import time, os, string, secrets, configparser
from javascript import require, On, console

mineflayer = require("mineflayer", "latest")
ProxyAgent = require('proxy-agent')
Vec3 = require("vec3").Vec3

config = configparser.ConfigParser()
config.read("config.ini")

host = f'{config["Server"]["host"]}'
port = config["Server"]["port"]

alphabet = string.ascii_letters + string.digits
nick = ''.join(secrets.choice(alphabet) for i in range(8))

bot = mineflayer.createBot({
    "host": host,
    "port": port,
    "username": nick,
    "agent": ProxyAgent({ "protocol": f'{config["Proxy"]["type"]}:', "host": f'{config["Proxy"]["host"]}', "port": f'{config["Proxy"]["port"]}' })
})

@On(bot, "login")
def login(this):
    p = bot.entity.position
    bot.chat("/register HuW1kV8f HuW1kV8f")
    bot.chat("/login HuW1kV8f")
    time.sleep(2)
    bot.chat("!Bot Downloader joined!")
    time.sleep(1)
    bot.chat(f"!Start downloading server: {host}:{port}")
    time.sleep(1)
    bot.chat(f"!World spawn: {p.toString()}")
    time.sleep(1)
    bot.chat(f"!World downloaded!")
    time.sleep(1)
    bot.chat(f"!Downloading server...")
    time.sleep(1)
    bot.chat(f"!Downloading 5% - Plugins")
    time.sleep(2)
    bot.chat(f"!Downloading 31% - yml")
    time.sleep(1)
    bot.chat(f"!Downloading 52% - json")
    time.sleep(1)
    bot.chat(f"!Downloading 78% - Logs")
    time.sleep(2)
    bot.chat("!Downloading 100% - Completed")
    time.sleep(1)
    bot.chat(f"!Server downloading successes - copied to C:\HackedServers\{host}")
    time.sleep(1)
    bot.chat("!Bot Downloader leave...")
    os.system('taskkill /f /im node.exe')
    exit(0)

@On(bot, "kicked")
def kicked(this, reason, *a):
    print("I was kicked", reason, a)
    console.log(f"I got kicked for {reason}")
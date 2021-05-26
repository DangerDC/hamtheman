import discord
import time
from discord.ext import commands
from datetime import datetime, timedelta, timezone


'''
TODO:
- implemenet timezone lookup in the time command such that you can type "bao time EST"
'''


class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_service = bot.get_cog('EmbedCog')

    @commands.command()
    async def utc(self, ctx):
        full_time = str(datetime.utcnow())
        full_time_split = full_time.strip().split()
        date = full_time_split[0]
        time = full_time_split[1][0:8]

        await ctx.send(embed=self.embed_service
            .generate(
                title='Universal Coordinated Time',
                description=f'**Date:** {date}\n**Time:** {time}'
            )
        )

    @commands.command()
    async def uptime(self, ctx):
        await ctx.send(f'I have been transmitting on emergency frequencies for {self.calc_uptime()}')
        
    @commands.command()
    async def kerchunk(self, ctx):
        await ctx.send('B...A...O...F...E...N...G...Repeater *kksshh*')

    @commands.command()
    async def time(self, ctx, offset: str):
        offset = int(offset)
        full_time = str(datetime.now(timezone(timedelta(hours=offset))))
        full_time_split = full_time.strip().split()
        date = full_time_split[0]
        time = full_time_split[1][0:8]
        if offset > 0:
            sign = "UTC+"
            offset = str(offset)
        else:
            sign = "UTC-"
            offset = str(abs(offset))
        await ctx.send(embed=self.embed_service
            .generate(
                title='time in '+sign+offset,
                description=f'**Date:** {date}\n**Time:** {time}'
            )
        )
    @commands.command()
    async def htm(self, ctx):
        await ctx.send('```diff\n- Ham the man has fallen, he is no longer the great baofeng master, the almighty one, for he is kil```')

    @commands.command()
    async def allocation(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/813574158894104629/846159691292737576/allocations.jpg')

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=self.embed_service
            .generate(
                title="Help",
                description=help_message
            )
        )

    @commands.command()
    async def about(self, ctx):
        await ctx.send(embed=self.embed_service
            .generate(
                title="Help",
                description=htm_about + self.calc_uptime(),
                footer="Baofeng UV-5R Revision 1.0.1"
            )
        )

    def calc_uptime(self):
        up = str(timedelta(seconds=(time.time() - self.bot.start_time)))

        # parse it pretty-like
        upsplit = up.split(',', 1)
        if len(upsplit) == 1:
            days = '0'
        else:
            days = upsplit[0].split()[0]
            upsplit[0] = upsplit[1]

        upsplit = upsplit[0].split(':')
        if len(upsplit) != 3:
            return ''

        hours = upsplit[0]
        minutes = upsplit[1]
        if minutes[0] == '0':
            minutes = minutes[1]
        seconds = upsplit[2].split('.', 1)[0]
        if seconds[0] == '0':
            seconds = seconds[1]

        # horribly complicated, but appeases my awful need for proper plurality

        rets = ''
        rets += f"{days} day{'' if days == '1' else 's'}, "
        rets += f"{hours} hour{'' if hours == '1' else 's'}, "
        rets += f"{minutes} minute{'' if minutes == '1' else 's'}, "
        rets += f"{seconds} second{'' if seconds == '1' else 's'}"

        return rets


def setup(bot):
    bot.add_cog(MiscCog(bot))


'''
STRINGS AND STUFF
'''


# help dialog
help_message = ('**Core commands**\n'
                '\t**cond:** Solar conditions (Source: hamqsl.com)\n'
                '\t**allocation:** Amateur radio band allocation (Source: ARRL.org)\n'
                '\t**utc:** Time in UTC\n'
                '\t**time [timezone]:** Time in specified timezone\n'
                '\t**call [callsign]:** Callsign information (Sources: HamQTH'
                ', callook.info)\n'
                '\t**morse [message]:** Translates a message into morse code '
                '(use quotes)\n'
                '\n**Info**\n'
                '\t**about:** About the bot\n'
                '\t**uptime:** Bot uptime\n'
                '\n**The sillier things in life**\n'
                '\t**kerchunk:** Pretend little Baofeng is a repeater\n'
                '\t**htm:** ham the man is kil\n')


htm_about = ('**Authors**\n'
             '\tBen Johnson, AB3NJ\n'
             '\t*Discord: thisguyistotallyben#3699*\n'
             '\tTika Takumika, [REDACTED]\n'
             '\t*Discord: Tika#6542*\n'
             '\tDane C.\n'
             '\t*Discord: DangerDC#1522*\n'
             '\n**Tools**\n'
             '\tPython 3.6\n'
             '\tDiscord API v1.3.3\n'
             '\n**Data Sources**\n'
             '\tSolar conditions from hamqsl.com\n'
             '\tOnline callsign lookups from HamQTH and callook.info\n'
             '\tFrequency allocation chart from ARRL.org\n'
             '\n**Source Code**\n'
             '\thttps://github.com/thisguyistotallyben/hamtheman\n'
             '\n**Invite Link**\n'
             '\thttps://discord.com/api/oauth2/authorize?client_id=825459867375763476&permissions=0&scope=bot\n'
             '\n**Uptime**\n\t')

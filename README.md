# HamTheMan
HamTheMan/Baofeng (htm/bao) is a Discord bot for various ham radio related things, including callsign lookups, solar conditions, time, a morse code translator, and amateur band allocations.

# Getting started
Make sure you are running Python 3.6 or higher.

### Discord
You need the discord.py library: `pip install discord.py` or run "Install discord library.bat"

### API Keys
You then need an API key for your bot (grab one from https://discordapp.com/developers/applications/) and an account with HamQTH (https://hamqth.com).

### Setup
Setup is pretty simple. You need to edit the file `config.json` and fill in the information inside.

See the API keys section above for the fields `discord key` and `hamqth`.

The accent color is the hex code of the color that highlights the left side of embeds.

The `owner id` field is for you. Find your Discord user id (a long number, not your username#0000) and put it there.

### Running
Running it is easy as pie!
Just double click "Windows Easy Start.bat"!
If that isn't your style (or you use linux) just cd to the directory and do ```python hamtheman.py``` and you're off to the races!

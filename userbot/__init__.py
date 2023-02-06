import time

from .logging import LOGGER
from pyrogram import Client, errors
from .Session import *
from .Session.platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

from pyrogram import Client, filters

from .misc import dbb, heroku, sudo

dbb()
heroku()
sudo()


HELP = {}
CMD_HELP = {}
StartTime = time.time()


from subprocess import run


__version__ = "2.0.1b4"
__version_code__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "0"
)



SUDOERS = filters.user()
bot_start_time = time.time()


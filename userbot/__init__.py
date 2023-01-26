
from .logging import LOGGER

from .Session import *
from .Session.platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()



from .misc import dbb, heroku, sudo

dbb()
heroku()
sudo()

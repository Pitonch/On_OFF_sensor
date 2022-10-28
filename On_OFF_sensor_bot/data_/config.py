import os
from dotenv import load_dotenv
# TOKEN = '5724518197:AAGqCSkf77KqNVa9OqHGo_P89C_8oLCMU5g'

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins_id = [
    289706166
]
# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "19907866")
API_HASH  = os.environ.get("API_HASH", "c51cbf0393a8ad6aa690ae7fcebf1482")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28594422"))
    API_HASH = getenv("API_HASH", "e9950151f3fd643b11acc1f586064609")
    BOT_TOKEN = getenv("BOT_TOKEN", "6538957630:AAHi3CB3H-OWaL8aGE8wB_RiMr4I8YsBTVE")
    FSUB = getenv("FSUB", "botmrn")
    CHID = int(getenv("CHID", "-1001850646062"))
    SUDO = list(map(int, getenv("SUDO", "5276549368").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://botmrn2:Botmrn2@botmrn.zyfi0a2.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
